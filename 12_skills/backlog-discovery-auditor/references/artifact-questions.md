# Artifact Questions

Use these questions as the core of the audit. The goal is not to check whether the artifact follows a template. The goal is to check whether it answers the question it exists to answer.

## Initiative

Primary question:

> Why should this investment exist, what outcome is expected, and do the epics form a coherent path toward that outcome?

Look for:

- problem or opportunity
- objective or desired outcome
- business/user value
- scope boundaries
- impacted stakeholders or areas
- success signals or acceptance of the initiative
- epics that cover the path to the outcome

Common failures:

- initiative is only a theme or label
- objective is vague or generic
- expected result is absent
- epics are administrative buckets, not solution paths
- important outcome has no epic covering it

## Epic

Primary question:

> What large solution front, capability, or change must exist so the initiative can happen, and do the features explain how it will be achieved?

Look for:

- coherent solution front
- clear contribution to the initiative
- scope that is larger than a feature but not just a vague bucket
- features that cover the main parts of the epic
- absence of major gaps, duplication, or scope drift

Common failures:

- epic repeats the initiative without narrowing it
- epic is just an administrative grouping
- features do not cover the epic promise
- epic mixes unrelated concerns

## Feature

Primary question:

> What functional capability, behavior, or product outcome will be delivered, and do the stories explain how it will be built, validated, or delivered?

Look for:

- functional capability or behavior
- value or reason for the capability
- clear relation to the epic
- stories that build the feature in executable increments
- visible validation path
- known risks, dependencies, or premises when relevant

Reality adjustment:

Features may be cancelled or discarded in real product work. In this first version, status is not scored. Evaluate the artifact as it exists. If cancellation evidence appears, mention it as context but do not reward or punish automatically.

Common failures:

- feature is only a title
- feature is actually a task list
- feature describes solution detail without the capability or outcome
- stories cover only part of the feature
- stories belong to another feature

## User story

Primary question:

> Does this story provide enough clear and validatable information for the team to execute an increment that contributes to the parent feature?

Look for:

- clear expected behavior, outcome, or change
- minimum information needed to execute
- intuitive wording that does not require permanent oral explanation
- validation criteria or acceptance criteria
- risks, dependencies, premises, or external constraints when relevant
- clear contribution to the parent feature

A story may be good without the format "As a / I want / so that". Do not score that format as inherently valuable. Only score whether the story explains who or what is affected, what must change, why it matters, and how it can be validated.

Common failures:

- title-only or vague description
- no acceptance or validation signal
- technical task with no behavior or value connection
- mixed scope that should be split
- dependency hidden in comments or external knowledge
- story is well-written but attached to the wrong feature
