---
name: decision-log
description: Adds decision records to artefacts/10-decision-log.md from meeting notes, review notes or the designer's description, with the decider as a role, the reason taken from the notes or marked as a gap, options, what was given up, a revisit trigger, and an updated index. Use right after a meeting or review where something was decided, when asked to record a decision, or when a decision is reopened, changed or superseded. Do not use for minor choices nobody will question, for sorting review comments, or to invent a reason that is not in the notes.
metadata:
  stage: record
---

# Decision log

One short, honest entry per significant decision, so "why is it like this?" always has an answer.

## What counts as significant

Hard to reverse, affects other people, or likely to be questioned later. If unsure, ask the designer. Do not log every small choice.

## Inputs

- Meeting or review notes, or the designer's own account
- The existing `artefacts/10-decision-log.md`
- `artefacts/02-stakeholder-map.md` for decider roles, if it exists

## Workflow

1. Read the existing log to find the next ID and avoid duplicates.
2. Pull out only decisions the notes actually state. List them to the designer before writing.
3. For each, fill in: title, date, decider (**role**, not a personal name), context, options considered, decision, why, gives up, consequences, revisit trigger and related items.
4. **Why:** use the reason stated in the notes. If none was stated, write `gap: reason not stated` and ask. Never invent one.
5. If the decision changed after a first choice, or a finding changed it, add a `Finding` line, and write a new entry that supersedes the old one. Update the old entry's status.
6. Update the index. Show the new entries to the designer for review before saving.

## Rules

- No reasons, deciders or options that are not in the material.
- Roles only. Resolve a personal name to a role from the stakeholder map, or ask.
- A decision made against the designer's recommendation is logged like any other. Record the recommendation in *Options considered*.
- Do not edit the substance of an accepted decision. Supersede it.

## Output

Update `artefacts/10-decision-log.md`: new entries and the index.

## Verify before finishing

- [ ] Every entry has a decider role, a reason (or `gap`) and a revisit trigger
- [ ] No reason or option was invented
- [ ] The index is current and superseded entries point to what replaced them
- [ ] The designer has seen the entries before they were saved
