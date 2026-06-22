# Reporting Guide

## Output strategy

For small inputs, a Markdown report may be enough. For large inputs, do not dump all artifacts into chat. Generate artifacts:

1. JSON as source of truth.
2. HTML dashboard for collapsible navigation.
3. CSV for spreadsheet import.
4. XLSX when the environment has spreadsheet tooling and the user needs a polished workbook.
5. PDF only after the report structure is stable.

## Audit JSON structure

Use this structure as the durable output:

```json
{
  "metadata": {
    "project_name": "optional",
    "generated_at": "iso timestamp",
    "model_version": "manual or skill version",
    "notes": []
  },
  "summary": {
    "total_items": 0,
    "scored_items": 0,
    "global_score": null,
    "rating_label": null,
    "label_counts": {},
    "critical_findings": []
  },
  "items": [
    {
      "id": "...",
      "type": "user_story",
      "title": "...",
      "parent_id": "...",
      "score": 72,
      "rating_label": "adjustable",
      "artifact_quality_score": 68,
      "relationship_quality_score": 75,
      "maturity_risk": "medium",
      "score_trace": {
        "base_score": 74,
        "artifact_quality_score": 68,
        "relationship_quality_score": 75,
        "maturity_risk": "medium",
        "caps_applied": [],
        "cap_applied": false,
        "cap_value": null,
        "cap_reason": "",
        "cap_not_applied_reason": "",
        "final_score": 72,
        "rating_label": "adjustable",
        "status_used_as_quality_input": false
      },
      "intrinsic_assessment": "...",
      "relational_assessment": "...",
      "pitch": "...",
      "evidence_bullets": [],
      "impact_bullets": [],
      "recommendation_bullets": [],
      "confidence": "medium",
      "evidence_sources_used": ["title", "description", "acceptance_criteria"]
    }
  ],
  "tree": []
}
```

## Pitch style

The pitch is a short diagnostic paragraph. It should not be motivational. It should explain what is useful, what is weak, and why that matters.

Good:

> The feature describes a relevant approval capability, but the child stories only cover the happy path. Approval rejection, permission rules, and integration dependency are mentioned in the feature and not represented in the stories, which creates execution and validation risk.

Bad:

> This feature is good but needs improvement.

## Evidence bullets

Evidence bullets should name what was observed. Avoid vague advice.

Examples:

- Description explains the expected behavior but not the success condition.
- Acceptance criteria exist, but they are written as implementation tasks instead of observable outcomes.
- Child stories cover registration and search, but not approval, although approval appears in the feature title.
- Dependency on an external system appears in comments only.

## Recommendation bullets

Recommendations must be actionable.

Examples:

- Add an acceptance criterion for the rejection flow.
- Create a child story for permission validation.
- Move dependency information from comments into the main description or dependency field.
- Review the parent link; this story appears to belong to feature ABC-123.

## Global summary

For each initiative, include:

- score and label
- executive reading
- strongest evidence
- main decomposition gaps
- highest-risk artifacts
- recommended next actions

## HTML dashboard

Use collapsible sections for initiatives, epics, features, and stories. Use score labels as visual classes. Keep the dashboard simple and local: no external assets, no remote scripts, no external CSS.

## Spreadsheet output

Recommended sheets:

- `Dashboard`: global score, label counts, critical findings, top risks.
- `Items`: one row per artifact.
- `Hierarchy`: parent-child tree with depth.
- `Initiatives`: grouped summary by initiative.
- `Calibration`: scoring labels, caps, and definitions.

Use conditional formatting by score range when creating XLSX.

## Required conformance checks

Before delivering final JSON, validate the audit file with `scripts/validate_audit_conformance.py` when possible. The audit is not final if any of these contradictions exist:

- score and `score_trace.final_score` disagree;
- `rating_label` does not match the final score range;
- a scored item is missing `score_trace`;
- `status_used_as_quality_input` is true;
- a cap was applied but has no `cap_reason`;
- an empty active/completed item is scored as healthy/reference;
- a parent with empty or critical direct children is scored as healthy/reference without an explicit cap-not-applied reason.

## Score trace display

HTML, CSV, and spreadsheet outputs should expose at least:

- artifact quality score;
- relationship quality score;
- maturity risk;
- cap applied;
- cap value;
- cap reason;
- false readiness flag when present.
