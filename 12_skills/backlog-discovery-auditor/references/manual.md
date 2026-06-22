# Backlog Discovery Auditor Manual

## What this package does

This package helps audit a discovery/backlog hierarchy from initiative to epic to feature to user story.

It evaluates two things:

1. Whether each artifact is clear, useful, validatable, and executable enough for its level.
2. Whether children explain how the parent will be achieved.

It is not a generic agile checklist. It does not reward ceremony by itself. It does not require the user story format "As a / I want / so that".

## Recommended use

Use when you have a project, team, initiative, or planning export with 100-300+ artifacts and need to understand:

- which items are weak
- where decomposition breaks
- which features lack useful stories
- which epics do not cover the initiative
- which artifacts are readable but attached to the wrong parent
- where execution risk is caused by weak documentation

## Input preparation

Provide a CSV, JSON, XLSX, XML, or pasted table with at least:

- id
- title
- type
- description
- parent

Extra fields are useful and should be included when available:

- acceptance criteria
- objectives
- observations
- risks
- dependencies
- comments
- attachment text

Status, creation date, bugs, and blockers may be included as context, but they are not score inputs in version 1.

## Default process

1. Normalize the file.
2. Rebuild the hierarchy through parent IDs.
3. Flag structural problems such as orphan items or missing parents.
4. Score each artifact from 0 to 100.
5. Classify each score into one of five labels.
6. Generate JSON, CSV, Markdown, HTML dashboard, or XLSX depending on the requested output.

## Score labels

- 90-100: reference
- 75-89: healthy
- 60-74: adjustable
- 40-59: fragile
- 0-39: critical

## Important rule

The score is risk-based. It is not a sum of small checklist points. Severe defects cap the score.

Example: a story may be well written, but if it does not belong to the parent feature, it must not receive a high final score.

## Recommended first run

For the first real dataset, generate:

- normalized JSON
- audit JSON
- HTML dashboard
- CSV item table
- short executive summary in chat

Do not generate PDF first. PDF is better after the report structure is stable.

## Calibration

The first scoring version should be treated as a calibration baseline. After reviewing real results, adjust:

- score caps
- severity definitions
- artifact questions
- report fields
- output layout

Do not overfit the model before seeing real examples.
