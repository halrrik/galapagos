#!/usr/bin/env python3
"""Normalize backlog/discovery exports into a tree-ready JSON file.

Supported inputs: CSV, JSON, XML, and a minimal XLSX reader for simple first-sheet tables.
The script uses only Python standard library modules.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from xml.etree import ElementTree as ET

ALIASES = {
    "id": ["id", "work item id", "work_item_id", "item id", "key", "codigo", "code"],
    "title": ["title", "titulo", "name", "summary", "subject"],
    "description": ["description", "descricao", "descricaoo", "desc", "body", "details"],
    "type": ["type", "tipo", "work item type", "item type", "artifact type", "categoria"],
    "parent_id": ["parent", "parent id", "parent_id", "pai", "id pai", "parent work item", "parent work item id"],
    "acceptance_criteria": ["acceptance criteria", "acceptance_criteria", "criterios de aceite", "criterio de aceite", "acceptance", "criterios"],
    "objectives": ["objectives", "objetivos", "objective", "goal", "goals", "resultado esperado", "expected outcome"],
    "observations": ["observations", "observacoes", "observacao", "notes", "notas"],
    "risks": ["risks", "riscos", "risk"],
    "dependencies": ["dependencies", "dependencias", "dependency", "blocked by"],
    "comments": ["comments", "comentarios", "discussion"],
    "attachments": ["attachments", "anexos", "links", "attachment_text"],
    "status": ["status", "state", "estado"],
}

TYPE_ALIASES = {
    "initiative": "initiative",
    "iniciativa": "initiative",
    "epic": "epic",
    "epico": "epic",
    "epico": "epic",
    "feature": "feature",
    "funcionalidade": "feature",
    "funcionalidad": "feature",
    "story": "user_story",
    "user story": "user_story",
    "user_story": "user_story",
    "historia": "user_story",
    "historia de usuario": "user_story",
    "bug": "bug",
    "defect": "bug",
    "task": "task",
    "tarefa": "task",
}

EXPECTED_PARENT = {
    "epic": {"initiative"},
    "feature": {"epic"},
    "user_story": {"feature"},
}


def strip_accents(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))


def norm_key(value: Any) -> str:
    text = strip_accents(str(value or "")).strip().lower()
    text = re.sub(r"[_\-]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def clean(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    return str(value).strip()


def canonical_field_map(headers: Iterable[str]) -> Dict[str, str]:
    lookup: Dict[str, str] = {}
    for canonical, aliases in ALIASES.items():
        for alias in aliases:
            lookup[norm_key(alias)] = canonical
    result: Dict[str, str] = {}
    used: set[str] = set()
    for header in headers:
        key = norm_key(header)
        canonical = lookup.get(key)
        if canonical and canonical not in used:
            result[header] = canonical
            used.add(canonical)
        else:
            result[header] = header
    return result


def canonical_type(value: str) -> str:
    key = norm_key(value)
    return TYPE_ALIASES.get(key, key.replace(" ", "_") if key else "unknown")


def read_csv(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample) if sample.strip() else csv.excel
        reader = csv.DictReader(f, dialect=dialect)
        return [dict(row) for row in reader]


def read_json(path: Path) -> List[Dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return [dict(x) for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        for key in ("items", "records", "artifacts", "work_items", "data"):
            value = data.get(key)
            if isinstance(value, list):
                return [dict(x) for x in value if isinstance(x, dict)]
    raise ValueError("JSON must be a list of objects or contain an items/records/artifacts/work_items/data array.")


def read_xml(path: Path) -> List[Dict[str, Any]]:
    root = ET.parse(path).getroot()
    candidates = list(root.findall(".//item")) or list(root.findall(".//record")) or list(root.findall(".//workItem"))
    if not candidates and len(root):
        candidates = list(root)
    rows: List[Dict[str, Any]] = []
    for elem in candidates:
        row: Dict[str, Any] = dict(elem.attrib)
        for child in list(elem):
            tag = child.tag.split("}")[-1]
            text = "".join(child.itertext()).strip()
            if text:
                row[tag] = text
        if row:
            rows.append(row)
    return rows


def xlsx_col_to_index(cell_ref: str) -> int:
    letters = re.sub(r"[^A-Z]", "", cell_ref.upper())
    total = 0
    for ch in letters:
        total = total * 26 + (ord(ch) - ord("A") + 1)
    return total - 1


def read_xlsx_minimal(path: Path) -> List[Dict[str, Any]]:
    with zipfile.ZipFile(path) as z:
        shared: List[str] = []
        if "xl/sharedStrings.xml" in z.namelist():
            root = ET.fromstring(z.read("xl/sharedStrings.xml"))
            ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
            for si in root.findall("a:si", ns):
                text = "".join(t.text or "" for t in si.findall(".//a:t", ns))
                shared.append(text)
        sheet_name = "xl/worksheets/sheet1.xml"
        if sheet_name not in z.namelist():
            sheets = [n for n in z.namelist() if n.startswith("xl/worksheets/sheet") and n.endswith(".xml")]
            if not sheets:
                raise ValueError("No worksheet XML found in XLSX.")
            sheet_name = sorted(sheets)[0]
        root = ET.fromstring(z.read(sheet_name))
    ns = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    table: List[List[str]] = []
    for row in root.findall(".//a:sheetData/a:row", ns):
        values: Dict[int, str] = {}
        for c in row.findall("a:c", ns):
            ref = c.attrib.get("r", "A1")
            idx = xlsx_col_to_index(ref)
            cell_type = c.attrib.get("t")
            v = c.find("a:v", ns)
            value = ""
            if v is not None and v.text is not None:
                raw = v.text
                if cell_type == "s":
                    value = shared[int(raw)] if raw.isdigit() and int(raw) < len(shared) else raw
                else:
                    value = raw
            is_elem = c.find("a:is", ns)
            if is_elem is not None:
                value = "".join(t.text or "" for t in is_elem.findall(".//a:t", ns))
            values[idx] = value
        if values:
            width = max(values) + 1
            table.append([values.get(i, "") for i in range(width)])
    if not table:
        return []
    headers = [clean(x) for x in table[0]]
    rows: List[Dict[str, Any]] = []
    for values in table[1:]:
        row = {headers[i]: values[i] if i < len(values) else "" for i in range(len(headers)) if headers[i]}
        if any(clean(v) for v in row.values()):
            rows.append(row)
    return rows


def load_rows(path: Path) -> List[Dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return read_csv(path)
    if suffix == ".json":
        return read_json(path)
    if suffix == ".xml":
        return read_xml(path)
    if suffix == ".xlsx":
        return read_xlsx_minimal(path)
    raise ValueError(f"Unsupported input type: {suffix}")


def normalize_rows(rows: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
    if not rows:
        return [], ["No rows found in input."]
    headers = list({k for row in rows for k in row.keys()})
    fmap = canonical_field_map(headers)
    warnings: List[str] = []
    items: List[Dict[str, Any]] = []
    for idx, row in enumerate(rows, start=1):
        normalized: Dict[str, Any] = {
            "id": "",
            "type": "unknown",
            "title": "",
            "description": "",
            "parent_id": "",
            "status": "",
            "acceptance_criteria": "",
            "objectives": "",
            "observations": "",
            "risks": "",
            "dependencies": "",
            "comments": "",
            "attachments": "",
            "extra_fields": {},
            "children_ids": [],
            "source_row": idx,
        }
        for original, value in row.items():
            key = fmap.get(original, original)
            val = clean(value)
            if key in normalized and key != "extra_fields":
                normalized[key] = val
            else:
                normalized["extra_fields"][str(original)] = val
        normalized["id"] = clean(normalized.get("id"))
        normalized["parent_id"] = clean(normalized.get("parent_id"))
        normalized["type"] = canonical_type(clean(normalized.get("type")))
        if not normalized["id"]:
            normalized["id"] = f"__missing_id_row_{idx}"
            warnings.append(f"Row {idx}: missing id; generated {normalized['id']}.")
        items.append(normalized)
    return items, warnings


def detect_structure(items: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], List[str]]:
    warnings: List[str] = []
    ids = [item["id"] for item in items]
    counts = Counter(ids)
    duplicates = [item_id for item_id, count in counts.items() if count > 1]
    if duplicates:
        warnings.extend(f"Duplicate id: {item_id}" for item_id in duplicates)
    by_id = {item["id"]: item for item in items}
    for item in items:
        parent_id = item.get("parent_id") or ""
        if parent_id and parent_id in by_id:
            by_id[parent_id].setdefault("children_ids", []).append(item["id"])
        elif parent_id:
            warnings.append(f"Item {item['id']} references missing parent {parent_id}.")
    roots = [item["id"] for item in items if not item.get("parent_id") or item.get("parent_id") not in by_id]
    for item in items:
        parent_id = item.get("parent_id") or ""
        if not parent_id:
            if item.get("type") not in ("initiative", "unknown"):
                warnings.append(f"Item {item['id']} has no parent but type is {item.get('type')}.")
            continue
        parent = by_id.get(parent_id)
        if not parent:
            continue
        expected = EXPECTED_PARENT.get(item.get("type"))
        if expected and parent.get("type") not in expected:
            warnings.append(
                f"Hierarchy jump: {item['id']} ({item.get('type')}) under {parent_id} ({parent.get('type')})."
            )
    cycles = find_cycles(by_id)
    for cycle in cycles:
        warnings.append("Cycle detected: " + " -> ".join(cycle))
    tree = [build_tree(root_id, by_id, set()) for root_id in roots]
    return {
        "root_ids": roots,
        "tree": tree,
        "counts_by_type": dict(Counter(item.get("type", "unknown") for item in items)),
        "duplicate_ids": duplicates,
        "cycle_count": len(cycles),
        "item_count": len(items),
    }, warnings


def find_cycles(by_id: Dict[str, Dict[str, Any]]) -> List[List[str]]:
    cycles: List[List[str]] = []
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: List[str] = []

    def dfs(item_id: str) -> None:
        if item_id in visiting:
            if item_id in stack:
                cycles.append(stack[stack.index(item_id):] + [item_id])
            return
        if item_id in visited:
            return
        visiting.add(item_id)
        stack.append(item_id)
        for child_id in by_id.get(item_id, {}).get("children_ids", []):
            if child_id in by_id:
                dfs(child_id)
        stack.pop()
        visiting.remove(item_id)
        visited.add(item_id)

    for item_id in by_id:
        dfs(item_id)
    return cycles


def build_tree(item_id: str, by_id: Dict[str, Dict[str, Any]], seen: set[str]) -> Dict[str, Any]:
    item = by_id.get(item_id, {"id": item_id, "title": "missing", "type": "unknown", "children_ids": []})
    if item_id in seen:
        return {"id": item_id, "cycle": True, "children": []}
    next_seen = set(seen)
    next_seen.add(item_id)
    return {
        "id": item_id,
        "type": item.get("type"),
        "title": item.get("title"),
        "children": [build_tree(child_id, by_id, next_seen) for child_id in item.get("children_ids", [])],
    }


def write_summary(path: Path, data: Dict[str, Any], warnings: List[str]) -> None:
    lines = [
        "# Normalization Summary",
        "",
        f"Generated at: {data['metadata']['generated_at']}",
        f"Input file: {data['metadata']['input_file']}",
        f"Total items: {data['structure']['item_count']}",
        "",
        "## Counts by type",
        "",
    ]
    for item_type, count in sorted(data["structure"].get("counts_by_type", {}).items()):
        lines.append(f"- {item_type}: {count}")
    lines += ["", "## Structural warnings", ""]
    if warnings:
        lines.extend(f"- {warning}" for warning in warnings)
    else:
        lines.append("- None detected.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize backlog/discovery exports.")
    parser.add_argument("input", help="Input CSV, JSON, XLSX, or XML file.")
    parser.add_argument("--outdir", default=".", help="Output directory.")
    parser.add_argument("--prefix", default="normalized_backlog", help="Output filename prefix.")
    args = parser.parse_args()

    input_path = Path(args.input)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    rows = load_rows(input_path)
    items, warnings = normalize_rows(rows)
    structure, structure_warnings = detect_structure(items)
    warnings.extend(structure_warnings)

    data = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "input_file": str(input_path),
            "normalizer_version": "0.1.0",
        },
        "items": items,
        "structure": structure,
        "warnings": warnings,
    }

    json_path = outdir / f"{args.prefix}.json"
    summary_path = outdir / f"{args.prefix}_summary.md"
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    write_summary(summary_path, data, warnings)
    print(json.dumps({"json": str(json_path), "summary": str(summary_path), "warnings": len(warnings)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
