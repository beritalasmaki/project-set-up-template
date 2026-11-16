# 03 Requirements spec (fictional example)

> **Fictional.** An invented example. Do not copy its content into a real project.

**Status:** draft · **Last updated:** 2026-03-12 · **Owner (role):** Lead designer

## Functional requirements

| ID | Requirement | Owner | Source | Priority | Status |
|---|---|---|---|---|---|
| FR-01 | The applicant sees which documents are required before starting. | Service owner | evidence: kick-off | must | open |
| FR-02 | The applicant can save the application at any step and return later. | Security owner | evidence: conversation 2 Mar | must | open |
| FR-03 | A contractor can reuse applicant details across applications. | Case officer lead | gap: needs confirming | should | open |
| FR-04 | The officer can request missing information in one message. | Case officer lead | evidence: kick-off | must | open |

## Accessibility requirements

Level: see `project.config.md`.

| ID | Requirement | Source |
|---|---|---|
| AR-01 | Every task can be completed with a keyboard alone. | project config |
| AR-02 | Error messages say what is wrong and how to fix it. | project config |

## Security and privacy requirements

| ID | Requirement | Data class | Source |
|---|---|---|---|
| SR-01 | An applicant sees only their own applications. | personal | evidence: conversation 2 Mar |
| SR-02 | Contractors see only applications they were granted access to. | personal | gap: access model not decided |

## Content and language

Plain language for all citizen-facing text. See `00-product-context.md`.

## Devices, browsers and performance

- Current versions of major browsers, desktop and mobile (source: gap, ask engineering lead).

## Out of scope

- Changes to the officers' case management system.

## Open questions

| Question | Who can answer | Needed by |
|---|---|---|
| How do contractors get access to client applications? | Security owner | 20 Mar |

## Done when

- [x] Every requirement has an owner role and a source, or is marked `gap`
- [x] Accessibility, security and privacy sections are filled in, not deleted
- [x] Out of scope matches `01-problem-framing.md`
- [x] Open questions have an owner and a date
