#!/usr/bin/env python3
"""Generate a local HTML dashboard and CSV table from audit JSON.

The audit JSON should follow references/reporting-guide.md. The script is tolerant:
if it only receives normalized items without scores, it still creates a navigation view.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any, Dict, List, Optional

LABELS = ["reference", "healthy", "adjustable", "fragile", "critical", "unscored"]


def label_from_score(score: Any) -> str:
    try:
        value = float(score)
    except (TypeError, ValueError):
        return "unscored"
    if value >= 90:
        return "reference"
    if value >= 75:
        return "healthy"
    if value >= 60:
        return "adjustable"
    if value >= 40:
        return "fragile"
    return "critical"


def load_items(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    if isinstance(data.get("items"), list):
        return [dict(x) for x in data["items"] if isinstance(x, dict)]
    if isinstance(data.get("artifacts"), list):
        return [dict(x) for x in data["artifacts"] if isinstance(x, dict)]
    return []


def item_score(item: Dict[str, Any]) -> Any:
    return item.get("score", item.get("final_score", ""))


def item_label(item: Dict[str, Any]) -> str:
    return str(item.get("rating_label") or item.get("label") or label_from_score(item_score(item))).lower()


def build_children(items: List[Dict[str, Any]]) -> Dict[str, List[str]]:
    children: Dict[str, List[str]] = defaultdict(list)
    ids = {str(item.get("id", "")) for item in items}
    for item in items:
        item_id = str(item.get("id", ""))
        parent = str(item.get("parent_id", item.get("parent", "")) or "")
        if parent and parent in ids:
            children[parent].append(item_id)
    return children


def bullet_list(values: Any) -> str:
    if not values:
        return ""
    if isinstance(values, str):
        return f"<p>{escape(values)}</p>"
    if isinstance(values, list):
        return "<ul>" + "".join(f"<li>{escape(str(v))}</li>" for v in values[:8]) + "</ul>"
    return f"<p>{escape(str(values))}</p>"


def score_trace_table(item: Dict[str, Any]) -> str:
    trace = item.get("score_trace") if isinstance(item.get("score_trace"), dict) else {}
    rows = []
    fields = [
        ("artifact_quality_score", item.get("artifact_quality_score", trace.get("artifact_quality_score", ""))),
        ("relationship_quality_score", item.get("relationship_quality_score", trace.get("relationship_quality_score", ""))),
        ("maturity_risk", item.get("maturity_risk", trace.get("maturity_risk", ""))),
        ("cap_applied", trace.get("cap_applied", "")),
        ("cap_value", trace.get("cap_value", "")),
        ("cap_reason", trace.get("cap_reason", "")),
    ]
    for name, value in fields:
        if value not in (None, "", []):
            rows.append(f"<tr><th>{escape(str(name))}</th><td>{escape(str(value))}</td></tr>")
    if not rows:
        return ""
    return '<h4>Score trace</h4><table class="trace">' + ''.join(rows) + '</table>'


def render_item(item_id: str, by_id: Dict[str, Dict[str, Any]], children: Dict[str, List[str]], depth: int = 0) -> str:
    item = by_id[item_id]
    label = item_label(item)
    score = item_score(item)
    score_text = "-" if score in (None, "") else escape(str(score))
    item_type = escape(str(item.get("type", "unknown")))
    title = escape(str(item.get("title", "untitled")))
    pitch = escape(str(item.get("pitch", item.get("description", "")) or ""))
    intrinsic = escape(str(item.get("intrinsic_assessment", "") or ""))
    relational = escape(str(item.get("relational_assessment", "") or ""))
    evidence = bullet_list(item.get("evidence_bullets") or item.get("evidence") or [])
    impact = bullet_list(item.get("impact_bullets") or item.get("impacts") or [])
    recs = bullet_list(item.get("recommendation_bullets") or item.get("recommendations") or [])
    trace_html = score_trace_table(item)
    margin = depth * 18
    html = [
        f'<details class="card {label}" style="margin-left:{margin}px" open>',
        f'<summary><span class="score">{score_text}</span><span class="label">{escape(label)}</span><span class="type">{item_type}</span><strong>{title}</strong><span class="id">{escape(str(item_id))}</span></summary>',
        '<div class="body">',
    ]
    if pitch:
        html.append(f'<p class="pitch">{pitch}</p>')
    if intrinsic:
        html.append(f'<p><b>Intrinsic:</b> {intrinsic}</p>')
    if relational:
        html.append(f'<p><b>Relational:</b> {relational}</p>')
    if trace_html:
        html.append(trace_html)
    if evidence:
        html.append('<h4>Evidence</h4>' + evidence)
    if impact:
        html.append('<h4>Impact</h4>' + impact)
    if recs:
        html.append('<h4>Recommendations</h4>' + recs)
    for child_id in children.get(item_id, []):
        html.append(render_item(child_id, by_id, children, depth + 1))
    html.append('</div></details>')
    return "\n".join(html)


def render_html(data: Dict[str, Any], items: List[Dict[str, Any]]) -> str:
    by_id = {str(item.get("id", f"missing-{idx}")): item for idx, item in enumerate(items, start=1)}
    children = build_children(items)
    child_ids = {child for group in children.values() for child in group}
    roots = [item_id for item_id in by_id if item_id not in child_ids]
    labels = Counter(item_label(item) for item in items)
    scored = [float(item_score(item)) for item in items if str(item_score(item)).replace(".", "", 1).isdigit()]
    global_score = round(sum(scored) / len(scored), 1) if scored else None
    generated_at = datetime.now(timezone.utc).isoformat()
    cards = []
    for label in LABELS:
        cards.append(f'<div class="metric {label}"><b>{labels.get(label, 0)}</b><span>{label}</span></div>')
    tree_html = "\n".join(render_item(root, by_id, children, 0) for root in roots)
    score_text = "-" if global_score is None else str(global_score)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Backlog Discovery Audit Dashboard</title>
<style>
:root {{ --bg:#f6f8fa; --ink:#18222c; --muted:#5f6b76; --card:#ffffff; --line:#d9e0e6; }}
body {{ margin:0; font-family: Arial, Helvetica, sans-serif; background:var(--bg); color:var(--ink); }}
header {{ padding:24px 32px; background:#102a36; color:#fff; }}
header h1 {{ margin:0 0 8px; font-size:24px; }}
header p {{ margin:0; color:#c9d7df; }}
main {{ padding:24px 32px 48px; }}
.metrics {{ display:flex; gap:12px; flex-wrap:wrap; margin:16px 0 24px; }}
.metric {{ background:var(--card); border-left:6px solid #999; border-radius:10px; padding:12px 16px; min-width:120px; box-shadow:0 1px 2px rgba(0,0,0,.08); }}
.metric b {{ display:block; font-size:24px; }}
.metric span {{ color:var(--muted); text-transform:uppercase; font-size:11px; letter-spacing:.05em; }}
.card {{ background:var(--card); margin:10px 0; border:1px solid var(--line); border-left:8px solid #999; border-radius:10px; box-shadow:0 1px 2px rgba(0,0,0,.05); }}
summary {{ cursor:pointer; padding:12px 14px; display:flex; gap:10px; align-items:center; }}
summary strong {{ flex:1; }}
.body {{ padding:0 18px 14px; }}
.score {{ font-weight:bold; min-width:42px; text-align:center; background:#eef2f4; border-radius:6px; padding:4px 6px; }}
.label,.type,.id {{ font-size:11px; text-transform:uppercase; color:var(--muted); background:#eef2f4; border-radius:999px; padding:4px 8px; }}
.pitch {{ font-size:14px; line-height:1.4; }}
h4 {{ margin-bottom:4px; }}
ul {{ margin-top:4px; }}
table.trace {{ border-collapse:collapse; font-size:12px; margin:8px 0 12px; }}
table.trace th, table.trace td {{ border:1px solid var(--line); padding:4px 7px; text-align:left; vertical-align:top; }}
table.trace th {{ background:#eef2f4; color:var(--muted); }}
.reference {{ border-left-color:#2f7d32; }}
.healthy {{ border-left-color:#5f8f32; }}
.adjustable {{ border-left-color:#c28b00; }}
.fragile {{ border-left-color:#c75d00; }}
.critical {{ border-left-color:#b3261e; }}
.unscored {{ border-left-color:#8a8f94; }}
.controls {{ margin:16px 0; }}
button {{ border:1px solid var(--line); background:#fff; border-radius:8px; padding:8px 12px; cursor:pointer; }}
</style>
<script>
function setAll(open) {{ document.querySelectorAll('details').forEach(d => d.open = open); }}
</script>
</head>
<body>
<header>
<h1>Backlog Discovery Audit Dashboard</h1>
<p>Generated at {escape(generated_at)}. Global score: {escape(score_text)}. Items: {len(items)}.</p>
</header>
<main>
<section class="metrics">{''.join(cards)}</section>
<div class="controls"><button onclick="setAll(true)">Expand all</button> <button onclick="setAll(false)">Collapse all</button></div>
<section>{tree_html}</section>
</main>
</body>
</html>'''


def write_csv(path: Path, items: List[Dict[str, Any]]) -> None:
    fields = [
        "id", "type", "title", "parent_id", "score", "rating_label", "confidence",
        "artifact_quality_score", "relationship_quality_score", "maturity_risk",
        "cap_applied", "cap_value", "cap_reason",
        "pitch", "intrinsic_assessment", "relational_assessment",
        "evidence_bullets", "impact_bullets", "recommendation_bullets",
    ]
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for item in items:
            row = {}
            for field in fields:
                value = item.get(field, "")
                if field in {"cap_applied", "cap_value", "cap_reason"}:
                    trace = item.get("score_trace") if isinstance(item.get("score_trace"), dict) else {}
                    value = trace.get(field, value)
                if isinstance(value, list):
                    value = " | ".join(str(x) for x in value)
                row[field] = value
            if not row.get("rating_label"):
                row["rating_label"] = item_label(item)
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build HTML dashboard and CSV from audit JSON.")
    parser.add_argument("audit_json", help="Audit JSON file.")
    parser.add_argument("--outdir", default=".", help="Output directory.")
    parser.add_argument("--prefix", default="backlog_audit", help="Output filename prefix.")
    args = parser.parse_args()

    input_path = Path(args.audit_json)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    data = json.loads(input_path.read_text(encoding="utf-8"))
    items = load_items(data)
    html_path = outdir / f"{args.prefix}_dashboard.html"
    csv_path = outdir / f"{args.prefix}_items.csv"
    summary_path = outdir / f"{args.prefix}_summary.json"
    html_path.write_text(render_html(data, items), encoding="utf-8")
    write_csv(csv_path, items)
    labels = Counter(item_label(item) for item in items)
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "item_count": len(items),
        "label_counts": dict(labels),
        "html": str(html_path),
        "csv": str(csv_path),
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
