# 00 Product context (fictional example)

> **Fictional.** An invented "Permit portal" for a made-up municipality. It shows the level of detail and tone. Do not copy its content into a real project.

**Status:** reviewed · **Last updated:** 2026-03-04 · **Owner (role):** Lead designer

## Who it is for

| User group | What they need to get done | Context and constraints | Source |
|---|---|---|---|
| Home owners | Apply for a building permit and know where the application stands | Infrequent users, often on a phone, some use screen magnification | evidence: kick-off notes, 2 Mar |
| Contractors | Submit several applications for clients and track them together | Daily users, desktop, need to reuse data between applications | evidence: kick-off notes, 2 Mar |
| Case officers | Review applications and request missing information | Desktop, many applications a day, long documents | gap: not yet interviewed |

## Jobs the product does

1. A home owner submits a complete application the first time.
2. A contractor manages many applications without re-entering details.
3. A case officer sees what is missing and asks for it in one step.

## Voice and terms

- **Tone:** plain, calm, direct. No legal wording unless the law requires it.
- **Reading level:** plain language for all citizen-facing text.

| Term we use | Meaning | Do not use |
|---|---|---|
| Application | A request for a permit | Case, ticket |
| Missing information | Something the officer needs from the applicant | Deficiency, defect |

## Principles

1. **Say what happens next.** Gives up: shorter screens.
2. **Ask once.** Gives up: the freedom to add questions late.
3. **Plain over precise.** Gives up: some legal exactness, which moves to a linked detail page.

## Constraints

See `project.config.md`. Also: applications must be saved at every step because sessions time out (evidence: security owner, 2 Mar).

## What the product never does

- Never asks for information the municipality already holds.
- Never shows one applicant's data to another.
- Never loses an unsaved application without warning.

## Sources

Kick-off notes, 2 Mar 2026. Security owner conversation, 2 Mar 2026.

## Done when

- [x] Every user group has a need and a source, or is marked as a gap
- [x] "Never does" has at least three entries
- [x] Terms the team argues about are in the glossary
- [x] The owner has reviewed it and status is `reviewed`
