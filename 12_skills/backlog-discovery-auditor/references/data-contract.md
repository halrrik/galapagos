# Data Contract

## Supported inputs

Preferred input formats:

- CSV
- JSON
- XLSX
- XML
- pasted table or structured text

The normalizer accepts common field aliases. If a field is unknown, preserve it under `extra_fields`.

## Minimum fields

Required or strongly expected:

- `id`
- `title`
- `description`
- `type`
- `parent`

`parent` may be empty for root initiatives.

## Common aliases

### id

- id
- work item id
- work_item_id
- item id
- key
- codigo
- code

### title

- title
- titulo
- name
- summary
- subject

### description

- description
- descricao
- descricaoo
- desc
- body
- details

### type

- type
- tipo
- work item type
- item type
- artifact type
- categoria

### parent

- parent
- parent id
- parent_id
- pai
- id pai
- parent work item

### acceptance criteria

- acceptance criteria
- acceptance_criteria
- criterios de aceite
- criterio de aceite
- acceptance
- criterios

### objectives

- objectives
- objetivos
- objective
- goal
- goals
- resultado esperado
- expected outcome

### observations

- observations
- observacoes
- observacao
- notes
- notas

### risks

- risks
- riscos
- risk

### dependencies

- dependencies
- dependencias
- dependency
- blocked by

### comments

- comments
- comentarios
- discussion

### attachments

- attachments
- anexos
- links
- attachment_text

### status

- status
- state
- estado

Status is preserved as context but must not be used as a direct quality score input. It may only support maturity-risk interpretation when combined with missing information, children, or execution evidence.

## Normalized item shape

```json
{
  "id": "123",
  "type": "feature",
  "title": "Enable invoice approval",
  "description": "...",
  "parent_id": "45",
  "status": "optional maturity context only",
  "acceptance_criteria": "...",
  "objectives": "...",
  "observations": "...",
  "risks": "...",
  "dependencies": "...",
  "comments": "...",
  "attachments": "...",
  "extra_fields": {},
  "children_ids": []
}
```

## Canonical type names

Use these canonical names when possible:

- `initiative`
- `epic`
- `feature`
- `user_story`
- `bug`
- `task`
- `unknown`

Only initiative, epic, feature, and user_story are scored by default. Other types may be listed as context or excluded depending on the user's request.

## Hierarchy rules

Expected hierarchy:

initiative > epic > feature > user_story

Allow imperfect real-world data, but flag it:

- user_story under epic: possible missing feature layer
- feature under initiative: possible missing epic layer
- epic under feature: likely hierarchy error
- multiple parents: unsupported unless explicit mapping exists
- no parent: valid for initiative, suspicious for lower types

## Activity and maturity context

Preserve status/state fields and child relationships, but do not score status directly.

Use these normalized signals only to interpret maturity risk:

- `has_children`: true when the item has direct children.
- `active_child_count`: count of direct children whose status suggests active work.
- `closed_child_count`: count of direct children whose status suggests completed/closed work.
- `empty_required_information`: true when description/objective/acceptance evidence is missing for the artifact level.
- `evidence_of_use`: true when the item has children, active/closed children, or is itself active/closed.

If status vocabulary is unknown, preserve the raw status and avoid hard claims. Prefer `maturity_risk: medium` or `confidence: low` instead of inventing a process interpretation.
