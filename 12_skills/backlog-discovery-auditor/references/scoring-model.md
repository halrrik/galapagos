# Scoring Model

Version: `0.2.0-hardening-test`

## Principle

Use severity and risk-based scoring. Do not use pure additive checklist math. A single structural defect can cap the score even when other parts look good.

The score measures risk of poor decision, poor execution, rework, or loss of traceability caused by weak artifact quality or weak decomposition.

## Score labels

| Score | Label | Meaning |
|---:|---|---|
| 90-100 | reference | No material weakness detected from available evidence. Strong clarity, traceability, and execution readiness. |
| 75-89 | healthy | Usable and coherent. Needs minor improvement but does not create major execution or traceability risk. |
| 60-74 | adjustable | Useful base exists, but relevant weaknesses require refinement before relying on it. |
| 40-59 | fragile | Significant risk of misunderstanding, rework, or parent-child misalignment. |
| 0-39 | critical | Essential information is missing or the artifact does not answer its core question. |

## Required score trace

Every scored item must include a `score_trace` object.

Minimum shape:

```json
{
  "base_score": 0,
  "artifact_quality_score": 0,
  "relationship_quality_score": null,
  "maturity_risk": "low|medium|high|critical|not_applicable",
  "caps_applied": [],
  "cap_applied": false,
  "cap_value": null,
  "cap_reason": "",
  "cap_not_applied_reason": "",
  "final_score": 0,
  "rating_label": "critical|fragile|adjustable|healthy|reference",
  "status_used_as_quality_input": false
}
```

Rules:

- `score` must equal `score_trace.final_score`.
- `rating_label` must match the final score range.
- `status_used_as_quality_input` must be `false`.
- If a cap applies, `cap_applied` must be `true`, `cap_value` must be set, and `cap_reason` must be specific.
- If a parent with child weaknesses is scored as `healthy` or `reference`, `cap_not_applied_reason` must explicitly explain why no cap applies.

## Scoring dimensions

### Initiative, epic, and feature

| Dimension | Weight | Notes |
|---|---:|---|
| Artifact quality | 45% | Intrinsic clarity, objective, scope, decision usefulness, and written evidence. |
| Relationship quality | 40% | Parent-child coherence, child coverage, traceability, duplicates, gaps, and scope drift. |
| Coverage sufficiency | 15% | Whether decomposition is sufficient for the current maturity and artifact level. |

### User story

| Dimension | Weight | Notes |
|---|---:|---|
| Objective and value clarity | 20% | Why the story exists and who/what benefits. |
| Expected behavior and scope | 25% | What changes, what is in/out, and relevant business/technical boundaries. |
| Acceptance/testability | 25% | How completion can be verified without guessing. |
| Parent relationship | 20% | How it contributes to the feature/epic. |
| Useful language for PO/PM/dev | 10% | Whether product, management, and development can discuss and execute it. |

Do not force a user story template. Evaluate organization, categorization when needed, and good practices.

## Status boundary

Status is not a quality criterion and must not directly add or remove score.

Status may only be used as maturity context when combined with other evidence:

- missing or weak artifact information;
- existing child items;
- child items in active or completed states;
- artifact in active or completed state;
- evidence that the artifact is already being used to guide real work.

Canonical rule:

> Status does not score artifact quality. Status only helps grade maturity risk when weak information is combined with decomposition or execution evidence.

## Empty-field severity model

Do not punish empty fields as an absolute rule. Punish empty fields according to usage.

| Situation | Diagnosis | Maximum score |
|---|---|---:|
| Empty initiative/epic/feature, new or intake, no children | Incomplete/not assessable; no real decomposition evidence yet | 65 |
| Empty user story, new or intake | Missing executable information, but may still be in intake | 55 |
| Empty user story in active execution | Severe execution risk | 40 |
| Empty user story completed/closed | Severe evidence and traceability failure | 35 |
| Empty feature/epic with children created | Parent contract missing; decomposition exists without reference | 45 |
| Empty feature/epic with active or completed children | Execution/decomposition without clear parent contract | 35 |
| Well-written parent with all direct user stories empty/critical | False readiness; parent looks good but execution layer is broken | 50 |
| Well-written parent with most direct user stories empty/critical | Major decomposition weakness | 60 |
| Child understandable by itself but weak or unclear relation to parent | Traceability gap | 70 |
| Required parent is missing and cannot be recovered | Orphaned artifact | 60 |
| Required parent missing and item also lacks useful description | Orphaned plus intrinsically weak | 40 |
| Spike without question, expected learning, or output | Empty spike; label does not provide exemption | 45 |

The final score cannot exceed the strictest applicable cap.

## Critical caps

Use score caps when severe defects exist. The cap is a maximum score, not an automatic score.

### Cap at 39 or lower

Apply when:

- artifact lacks enough information to understand what it is and shows evidence of real use;
- artifact does not answer the core question for its type;
- story cannot be executed because essential information is absent;
- parent-child relation is absent or nonsensical;
- item is orphaned and its place in the hierarchy cannot be recovered;
- parent promise is materially uncovered by children while work appears active or complete;
- empty story is active or complete.

### Cap at 59 or lower

Apply when:

- item is understandable but highly ambiguous;
- story has no meaningful validation/acceptance signal;
- feature is understandable but stories cover only a narrow part of it;
- epic or initiative is mostly a label with weak decomposition;
- important dependencies or risks are visible but not addressed;
- item seems attached to the wrong parent but some relationship exists;
- parent is well written but direct child stories are mostly empty, critical, or not traceable.

### Cap at 74 or lower

Apply when:

- item is usable but incomplete;
- acceptance criteria exist but are weak or not observable;
- decomposition is mostly coherent but has relevant gaps;
- wording requires substantial interpretation;
- critical evidence exists only in comments or attachments instead of the main fields;
- story is understandable for business but not executable enough for development, or technical enough for development but lacking objective/value.

## False readiness

Flag `false_readiness` when an artifact appears mature because it has a good title, polished wording, children, or progress signals, but the underlying written contract is missing or the children do not support it.

Examples:

- feature description is strong, but direct stories are empty or only spikes without questions/outputs;
- feature is empty, but stories already exist beneath it;
- story follows a template but does not say what must be validated;
- parent has several children, but they duplicate each other or cover only a narrow slice of the promise.

False readiness should usually create a cap.

## Similarity and duplication

Detect duplicate or near-duplicate titles/descriptions when possible. Similarity is a risk signal, not an automatic score by itself.

Recommended treatment:

- 100% duplicate story under same parent: cap at 74 unless intentionally split and justified.
- 85-99% similar stories under same parent: flag for review and cap at 89 unless there is clear distinction.
- Duplicate title with different parent: flag as possible reuse, taxonomy issue, or unclear ownership.

## Suggested starting score logic

Use this sequence:

1. Identify the core question for the artifact type.
2. Decide whether the artifact answers it.
3. Check empty fields and whether the item shows evidence of real use.
4. Evaluate parent-child coherence and coverage.
5. Identify false readiness risk.
6. Identify the worst defect and its severity.
7. Apply any score cap.
8. Estimate score within the capped range using evidence quality.
9. Write `score_trace`.
10. Write the pitch explaining why the score is where it is.

## Calibration rule

When scores feel wrong during real use, adjust caps and severity definitions first. Do not add many tiny weighted criteria before validating whether the severity model is working.
