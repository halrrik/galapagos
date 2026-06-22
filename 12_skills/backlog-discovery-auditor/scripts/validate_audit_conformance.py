#!/usr/bin/env python3
"""Validate backlog audit JSON conformance.

This script does not replace expert judgment. It catches contradictions that make an
audit unsafe to use, especially high scores on empty, untraceable, or falsely-ready
artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

LABEL_RANGES = [
    (90, 100, "reference"),
    (75, 89.999, "healthy"),
    (60, 74.999, "adjustable"),
    (40, 59.999, "fragile"),
    (0, 39.999, "critical"),
]

ACTIVE_WORDS = {
    "active", "doing", "in progress", "in development", "development", "desenvolvimento",
    "em desenvolvimento", "implementing", "implementation", "wip", "committed", "selected",
}
CLOSED_WORDS = {
    "done", "closed", "complete", "completed", "concluido", "concluida", "concluída",
    "resolvido", "resolved", "released", "deployed",
}
INTAKE_WORDS = {"new", "novo", "nova", "backlog", "intake", "triage", "to do", "todo"}

TEXT_FIELDS_BY_TYPE = {
    "initiative": ["description", "objectives", "pitch", "intrinsic_assessment"],
    "epic": ["description", "objectives", "pitch", "intrinsic_assessment"],
    "feature": ["description", "objectives", "pitch", "intrinsic_assessment"],
    "user_story": ["description", "acceptance_criteria", "pitch", "intrinsic_assessment"],
}


def norm(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def label_from_score(score: Any) -> str:
    try:
        value = float(score)
    except (TypeError, ValueError):
        return "unscored"
    for low, high, label in LABEL_RANGES:
        if low <= value <= high:
            return label
    return "unscored"


def is_active_status(status: Any) -> bool:
    s = norm(status)
    return any(word in s for word in ACTIVE_WORDS)


def is_closed_status(status: Any) -> bool:
    s = norm(status)
    return any(word in s for word in CLOSED_WORDS)


def is_intake_status(status: Any) -> bool:
    s = norm(status)
    return bool(s) and any(word == s or word in s for word in INTAKE_WORDS)


def meaningful_text(value: Any) -> bool:
    text = norm(value)
    if not text:
        return False
    placeholders = {
        "na", "n/a", "none", "null", "-", "--", "todo", "tbd", "a definir",
        "sem descricao", "sem descrição", "em branco", "vazio", "empty",
    }
    if text in placeholders:
        return False
    return len(re.sub(r"[^a-z0-9áéíóúàèìòùãõâêîôûçñ]", "", text, flags=re.I)) >= 12


def item_has_minimum_text(item: Dict[str, Any]) -> bool:
    item_type = norm(item.get("type"))
    fields = TEXT_FIELDS_BY_TYPE.get(item_type, ["description", "pitch", "intrinsic_assessment"])
    return any(meaningful_text(item.get(field)) for field in fields)


def load_items(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    if isinstance(data.get("items"), list):
        return [dict(x) for x in data["items"] if isinstance(x, dict)]
    if isinstance(data.get("artifacts"), list):
        return [dict(x) for x in data["artifacts"] if isinstance(x, dict)]
    raise ValueError("Audit JSON must contain an items or artifacts array.")


def build_children(items: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    by_parent: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    ids = {str(item.get("id", "")): item for item in items}
    for item in items:
        parent = str(item.get("parent_id", item.get("parent", "")) or "")
        if parent and parent in ids:
            by_parent[parent].append(item)
    return by_parent


def add(violations: List[Dict[str, Any]], item: Dict[str, Any], code: str, severity: str, message: str) -> None:
    violations.append({
        "id": item.get("id", ""),
        "type": item.get("type", ""),
        "title": item.get("title", ""),
        "code": code,
        "severity": severity,
        "message": message,
    })


def validate_item(item: Dict[str, Any], children: List[Dict[str, Any]], violations: List[Dict[str, Any]]) -> None:
    score = item.get("score", item.get("final_score"))
    try:
        score_value = float(score)
    except (TypeError, ValueError):
        score_value = None
    label = norm(item.get("rating_label") or item.get("label") or label_from_score(score))
    expected_label = label_from_score(score)
    trace = item.get("score_trace")
    item_type = norm(item.get("type"))
    empty = not item_has_minimum_text(item)
    active_or_closed = is_active_status(item.get("status")) or is_closed_status(item.get("status"))

    if score_value is not None and expected_label != "unscored" and label != expected_label:
        add(violations, item, "label_score_mismatch", "error", f"rating_label '{label}' does not match score {score_value}; expected '{expected_label}'.")

    if trace is None:
        add(violations, item, "missing_score_trace", "error", "Scored item is missing score_trace.")
    elif isinstance(trace, dict):
        final_score = trace.get("final_score")
        try:
            trace_final = float(final_score)
        except (TypeError, ValueError):
            trace_final = None
        if score_value is not None and trace_final is not None and abs(score_value - trace_final) > 0.01:
            add(violations, item, "score_trace_mismatch", "error", f"score {score_value} differs from score_trace.final_score {trace_final}.")
        if trace.get("status_used_as_quality_input") is True:
            add(violations, item, "status_used_as_quality_input", "error", "Status was marked as a quality-score input; status may only be maturity context.")
        if trace.get("cap_applied") and not meaningful_text(trace.get("cap_reason")):
            add(violations, item, "cap_without_reason", "error", "A cap was applied but cap_reason is missing or too vague.")
        cap_value = trace.get("cap_value")
        try:
            cap_float = float(cap_value)
        except (TypeError, ValueError):
            cap_float = None
        if trace.get("cap_applied") and cap_float is not None and score_value is not None and score_value > cap_float:
            add(violations, item, "score_exceeds_cap", "error", f"score {score_value} exceeds applied cap {cap_float}.")

    if score_value is not None and empty and active_or_closed and score_value > 40:
        add(violations, item, "empty_used_item_high_score", "error", "Item appears empty/placeholder but has active or closed status and score above 40.")

    if item_type == "user_story" and score_value is not None and empty and score_value > 55:
        add(violations, item, "empty_story_high_score", "error", "User story lacks minimum executable text and score is above 55.")

    if item_type in {"initiative", "epic", "feature"} and score_value is not None:
        empty_children = [child for child in children if not item_has_minimum_text(child)]
        critical_children = [child for child in children if label_from_score(child.get("score", child.get("final_score"))) == "critical"]
        active_closed_children = [child for child in children if is_active_status(child.get("status")) or is_closed_status(child.get("status"))]

        if empty and children and score_value > 45:
            add(violations, item, "empty_parent_with_children_high_score", "error", "Parent item is empty/placeholder but has children and score above 45.")
        if empty and active_closed_children and score_value > 35:
            add(violations, item, "empty_parent_with_used_children_high_score", "error", "Parent item is empty/placeholder and has active/closed children, but score is above 35.")
        if children and len(empty_children) == len(children) and score_value > 50:
            add(violations, item, "parent_all_children_empty_high_score", "error", "All direct children appear empty/placeholder, but parent score is above 50.")
        if children and len(empty_children) > len(children) / 2 and score_value > 60:
            add(violations, item, "parent_most_children_empty_high_score", "error", "Most direct children appear empty/placeholder, but parent score is above 60.")
        if critical_children and label in {"healthy", "reference"}:
            reason = ""
            if isinstance(trace, dict):
                reason = str(trace.get("cap_not_applied_reason", ""))
            if not meaningful_text(reason):
                add(violations, item, "healthy_parent_with_critical_children", "error", "Parent is healthy/reference with critical direct children and no explicit cap_not_applied_reason.")


def validate(data: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    items = load_items(data)
    by_parent = build_children(items)
    violations: List[Dict[str, Any]] = []
    warnings: List[Dict[str, Any]] = []
    for item in items:
        validate_item(item, by_parent.get(str(item.get("id", "")), []), violations)
    return violations, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate audit JSON conformance for backlog-discovery-auditor.")
    parser.add_argument("audit_json", help="Audit JSON file to validate.")
    parser.add_argument("--out", help="Optional output JSON report path.")
    parser.add_argument("--warnings-ok", action="store_true", help="Exit 0 if only warnings are found.")
    args = parser.parse_args()

    path = Path(args.audit_json)
    data = json.loads(path.read_text(encoding="utf-8"))
    violations, warnings = validate(data)
    report = {
        "input": str(path),
        "passed": not violations,
        "violation_count": len(violations),
        "warning_count": len(warnings),
        "violations": violations,
        "warnings": warnings,
    }
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if not violations else 2


if __name__ == "__main__":
    raise SystemExit(main())
