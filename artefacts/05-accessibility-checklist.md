# 05 Accessibility checklist

**Status:** draft · **Last updated:** [date] · **Owner (role):** [role] · **Published at:** [link, or `not shared`]

A design-stage check, not an audit. It shows what can be judged from a design file. Level and legal basis: see `project.config.md`.

Criteria are from WCAG 2.2. Read the criterion on the W3C site for exact requirements: https://www.w3.org/WAI/WCAG22/Understanding/

## Scope

- **Reviewed:** [screens and states]
- **Not reviewed:** [screens and states]. These read as "not reviewed", never "pass".

## Checks

Each answer is `pass`, `fail` or `cannot tell from a design`. Contrast and size answers need real values. Without them the answer is `cannot tell`.

| Criterion | Where | Answer | What was seen or given | Fix (a design change) |
|---|---|---|---|---|
| 1.1.1 Non-text Content | | | | |
| 1.3.1 Info and Relationships | | | | |
| 1.4.1 Use of Color | | | | |
| 1.4.3 Contrast (Minimum) | | | | |
| 1.4.4 Resize Text | | | | |
| 1.4.10 Reflow | | | | |
| 1.4.11 Non-text Contrast | | | | |
| 1.4.12 Text Spacing | | | | |
| 2.4.3 Focus Order | | | | |
| 2.4.6 Headings and Labels | | | | |
| 2.4.7 Focus Visible | | | | |
| 2.4.11 Focus Not Obscured (Minimum) | | | | |
| 2.5.7 Dragging Movements | | | | |
| 2.5.8 Target Size (Minimum) | | | | |
| 3.2.6 Consistent Help | | | | |
| 3.3.1 Error Identification | | | | |
| 3.3.2 Labels or Instructions | | | | |
| 3.3.3 Error Suggestion | | | | |
| 3.3.7 Redundant Entry | | | | |
| 3.3.8 Accessible Authentication (Minimum) | | | | |

## What a design file cannot show

- Screen reader output: to test in code
- Real focus behaviour, zoom in a browser, timing: to test in code
- How users with access needs get through the task: sessions [planned / not yet planned]

## Status line to use when sharing

"Design-stage review of [scope] on [date]. Not an audit. Not a conformance statement."

## Decision

[Designer role] makes or declines each fix by [date]. [Owner role] decides by [date] when the coded build is tested with assistive technology and users with access needs.

## Done when

- [ ] Scope names what was and was not reviewed
- [ ] Every row has one of the three answers, and every fail has a fix
- [ ] Contrast and size answers come from given values
- [ ] The closing list and the status line are present
