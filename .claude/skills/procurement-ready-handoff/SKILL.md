---
name: procurement-ready-handoff
description: Builds the handoff spec in artefacts/08-handoff-spec.md for engineering and other vendors, stating which file and version is final, putting behaviour rules beside each screen, listing dependencies and what each vendor provides, running a ready check, and listing open questions per party. Use when designs are about to go to engineering or another supplier, when several vendors build parts of one product, or when asked for a handoff spec or ready check. Do not use for design critique, for writing contracts or procurement documents, or for work that is still being explored.
metadata:
  stage: handoff
---

# Procurement-ready handoff

A handoff that survives being read by a vendor who was not in the room. Nothing left to guess, and a clear line between what is final and what is not.

## Inputs

- The final designs or flows, with file location and version
- `artefacts/04-user-flows-and-states.md`, `05-accessibility-checklist.md` and `06-security-privacy-brief.md` where they exist
- `project.config.md` for languages, tools, other vendors and constraints

## Workflow

1. Read `artefacts/08-handoff-spec.md` and the inputs above. Read only what the handoff needs.
2. **What is final:** a table with item, location, version, date and approver (role). If any is missing, ask. Anything not listed is not final.
3. **Scope:** what is included and what is not, and why.
4. **Behaviour per screen:** validation, defaults, limits, permissions and links to states. Write rules in plain statements a vendor can build and test. Avoid "should feel", "intuitive" and "etc.".
5. **Dependencies and vendors:** for each item, who provides it, when it is needed and its status. Make each vendor's part readable on its own, without reading the others' sections.
6. **Ready check:** run it honestly. Tick only what is true. List each unticked item with an owner role.
7. **Open questions:** split by party (engineering, each vendor). Give each a needed-by date.
8. **Walkthrough:** record when it is held, with which roles, and link resulting changes to decision log entries.

## Rules

- Do not mark a screen ready if any state is missing. Say which.
- Do not hide a failed or open accessibility or security item. Name it and its owner.
- Do not invent approvals. If nobody approved, write `not approved`.
- Use roles and vendor names as given in the config, not personal names.

## Output

Update `artefacts/08-handoff-spec.md`. Set `Status: draft` until the walkthrough has happened.

## Verify before finishing

- [ ] "What is final" lists file, version and approver for every item
- [ ] Every screen has its behaviour rules and states, or is marked as not ready
- [ ] Every dependency has a provider and a date
- [ ] The ready check is run and unticked items have owners
- [ ] Open questions are split by party, with dates
