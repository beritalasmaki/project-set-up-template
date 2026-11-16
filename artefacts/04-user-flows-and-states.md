# 04 User flows and states

**Status:** draft · **Last updated:** [date] · **Owner (role):** [role]

One task as a flow, then every screen against its states. Use one copy of this file per task, or one section per task.

## Task: [name]

**User group:** [from `00-product-context.md`] · **Goal:** [what the user achieves]

**Entry points:** [where users arrive from]

## Steps

| # | User does | System responds | Screen |
|---|---|---|---|
| 1 | | | |

## Decision points

| ID | Where | Condition | Leads to | Assumption behind it |
|---|---|---|---|---|
| A | step [n] | | step [n] | evidence: [source] / gap |

## Errors and recovery

| What goes wrong | What the user sees | How they recover | Where they land |
|---|---|---|---|
| | | | |

## Exits

- [where the flow can end: success, abandon, hand-off to another channel]

## Screens against states

Mark each cell `designed`, `missing` or `not needed` (with the reason).

| Screen | Empty | Loading | Partial data | Error | No permission | Success | Long or extreme content | First use |
|---|---|---|---|---|---|---|---|---|
| [screen] | | | | | | | | |

## Edge cases

| Screen | Edge case | Status |
|---|---|---|
| | [for example very long name, no access to the form, session times out] | |

## Gaps in order of what blocks the build first

1. [gap]

## Done when

- [ ] The flow covers errors and recovery, not only the happy path
- [ ] Every decision point has an assumption and a source or `gap`
- [ ] Every screen has every state marked
- [ ] Gaps are ordered by what blocks the build
