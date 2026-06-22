# Patchlog

## v0.2.0-hardening-test

Purpose: harden the skill against false-positive audit results where a report looks polished but ignores weak decomposition, empty children, or missing traceability.

Changes:

- Added mandatory `score_trace` for every scored artifact.
- Separated `artifact_quality_score`, `relationship_quality_score`, and `maturity_risk`.
- Clarified that status is not a quality score input.
- Allowed status only as maturity context when combined with missing information, children, or execution evidence.
- Added explicit empty-field severity model.
- Added false-readiness concept for polished parents with weak/empty children.
- Added user story evaluation based on organization, categorization when needed, and good practices, not template compliance.
- Added conformance validator: `scripts/validate_audit_conformance.py`.
- Updated dashboard/CSV generator to expose score trace, maturity risk, and cap information.

Design decisions:

- Do not merge with alternate skill designs blindly.
- Keep the skill portable and domain-neutral.
- Avoid references to specific internal projects or clients.
- Prefer few general severity rules over many tiny case-by-case rules.

Known limits:

- The validator is a safety net, not a full scorer.
- The skill still relies on model judgment to produce the audit JSON.
- Real calibration requires testing against historical outputs and datasets.
