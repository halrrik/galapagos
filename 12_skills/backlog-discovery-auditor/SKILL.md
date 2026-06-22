---
name: backlog-discovery-auditor
description: audit discovery and backlog hierarchies from csv, json, xlsx, xml, or structured text when the user needs to evaluate initiatives, epics, features, and user stories. use this skill to reconstruct parent-child trees, validate artifact quality, score items from 0 to 100, classify them into executive labels, detect weak decomposition, empty or misleading artifacts, false readiness, duplicate/similar work items, and generate structured json, markdown, csv, html dashboard, or spreadsheet-ready reports.
---

# Backlog Discovery Auditor

Version: `0.2.0-hardening-test`

## Purpose

Use this skill to audit whether a discovery/backlog hierarchy is understandable, executable, traceable, and coherently decomposed from initiative to epic to feature to user story.

This skill does not reward agile ceremony, perfect templates, or wording such as "As a / I want / so that" by itself. It evaluates whether each artifact answers the question it exists to answer and whether children explain how the parent will be achieved.

## Core workflow

1. Normalize the input data.
   - If the user provides CSV, JSON, XLSX, or XML, run `scripts/normalize_backlog.py` when useful.
   - If the input is pasted text or already structured JSON, normalize it directly in context.
   - Preserve extra fields as evidence; do not discard objectives, observations, comments, acceptance criteria, risks, dependencies, status, or attachment text.

2. Reconstruct the hierarchy.
   - Use `parent` or equivalent field to link child to parent.
   - Process parent links bottom-up because parent IDs usually live on children.
   - Present and report top-down: initiative > epic > feature > user story.
   - Flag missing parents, orphan items, duplicate IDs, cycles, unsupported type jumps, and multiple roots.

3. Audit each artifact intrinsically.
   - Evaluate whether the item answers the question required by its type.
   - Evaluate clarity, minimum executable information, validation/testability, risks/dependencies/premises, and usefulness.
   - Do not use status as a direct score input or quality criterion.
   - Use status only as contextual maturity evidence when it combines with missing information, decomposition, or execution signals.
   - Do not score creation date, bugs, blockers, or workflow hygiene unless the user explicitly asks for process audit.

4. Audit parent-child coherence.
   - For each child, check whether it contributes to the parent.
   - For each parent, check whether children cover the parent promise without severe gaps, duplicates, or scope drift.
   - Separate empty-or-weak parent, empty-or-weak child, and broken relation. Do not collapse all empty-field cases into one diagnosis.
   - A well-written child in the wrong parent is structurally risky and must receive a capped final score.

5. Score using severity, traceability, and caps.
   - Assign 0-100 scores using `references/scoring-model.md`.
   - Always produce `score_trace` for every scored item.
   - Never let nice wording hide a structural defect.
   - Never let a parent item be `reference` or `healthy` when direct children are empty, critical, or unrelated unless `score_trace.cap_not_applied_reason` explicitly explains why the cap does not apply.
   - Always separate artifact quality, relationship quality, and maturity risk.

6. Validate conformance before final delivery.
   - Run `scripts/validate_audit_conformance.py` on the audit JSON whenever a JSON file is generated or can be saved.
   - Fix violations before presenting a final result.
   - If the user only wants a quick in-chat review and no file is produced, manually apply the same conformance checks.

7. Generate outputs.
   - Always produce structured JSON as the durable source of truth.
   - Produce Markdown for human review when the result is small or when a narrative report is needed.
   - For large sets of 100-300+ artifacts, prefer JSON plus HTML dashboard or CSV/spreadsheet-ready output.
   - Use `scripts/make_audit_dashboard.py` when the audit JSON already exists and the user wants a collapsible visual dashboard.

## Required report fields per artifact

For every scored initiative, epic, feature, and user story, include:

- `id`
- `type`
- `title`
- `parent_id`
- `score`
- `rating_label`
- `artifact_quality_score`
- `relationship_quality_score`
- `maturity_risk`
- `score_trace`
- `intrinsic_assessment`
- `relational_assessment`
- `pitch`
- `evidence_bullets`
- `impact_bullets`
- `recommendation_bullets`
- `confidence`
- `evidence_sources_used`

Use concise, audit-friendly language. Avoid generic advice such as "improve the description" unless the exact missing information is named.

## Executive labels

Use these labels with the 0-100 score:

- `reference` for 90-100
- `healthy` for 75-89
- `adjustable` for 60-74
- `fragile` for 40-59
- `critical` for 0-39

Do not use celebratory labels such as "excellent" or vague labels such as "bad". The labels must sound executive, defensible, and actionable.

## Empty-field and maturity boundary

Do not punish emptiness as an absolute rule. Penalize emptiness according to artifact usage.

- Empty item in intake/new state with no children: incomplete and not ready, usually lower maturity risk.
- Empty item with children: traceability failure because decomposition exists without a clear parent contract.
- Empty item with children in execution or completion: high maturity risk because work is happening without enough written reference.
- Empty story in execution or completion: severe execution/evidence failure.
- Spike is not exempt: a spike must state the question, expected learning, or output.

Status alone must not raise or lower quality score. Status only helps interpret maturity risk when combined with missing information, active children, completed children, or other evidence of real use.

## Story quality boundary

Do not evaluate stories by template compliance. Evaluate organization, categorization when needed, and good practices.

A user story is strong when product, management, and development can understand enough to decide, execute, and validate without guessing. It does not need a fixed format, but it needs clear objective/value, expected behavior, scope boundary, acceptance/testability, and relation to the parent.

## Output navigation

For large reports, do not dump every artifact in full in chat. Provide:

1. Global summary.
2. Initiative-level summaries.
3. Top critical items.
4. False readiness and traceability risks.
5. Recommended next actions.
6. Links to generated JSON/HTML/CSV/XLSX artifacts when available.

## References

Load these files only when needed:

- `references/artifact-questions.md` for the core question each artifact type must answer.
- `references/scoring-model.md` for severity-based scoring, score caps, maturity context, and labels.
- `references/data-contract.md` for expected fields, aliases, and normalized JSON structure.
- `references/reporting-guide.md` for JSON, Markdown, HTML, CSV, and spreadsheet reporting structure.
- `references/manual.md` for the user-facing manual and operating notes.
- `PATCHLOG.md` for version history and change rationale.

## Important constraints

- Do not treat status as a direct score input.
- Do not score bugs, blockers, or creation dates unless explicitly asked to audit process/workflow.
- Do not overvalue agile format. A story does not need "As a / I want / so that" to be good.
- Do not claim dependencies exist unless they are explicit or clearly inferable. Mark inferred dependencies separately.
- Do not average children blindly into the parent score. Use decomposition risk and critical caps.
- Do not fabricate missing fields from silence. If evidence is absent, say so.
- Do not produce a final audit JSON without `score_trace` unless the user explicitly requests a lightweight draft.
