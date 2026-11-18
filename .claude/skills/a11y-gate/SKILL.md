---
name: a11y-gate
description: Runs a design-stage accessibility check of one screen or flow against WCAG 2.2 at the level set in project.config.md, answering each check pass, fail or cannot tell from a design, writing each fix as a design change, and listing what only code, assistive technology and disabled users can show. Uses a script for contrast and target-size maths. Use when asked to check accessibility of a design, review contrast, focus order or target size, fill in artefacts/05-accessibility-checklist.md, or before sharing or handing off a design. Do not use to claim conformance, to audit built code, or to replace testing with disabled users.
metadata:
  stage: check
---

# Accessibility gate

A design-stage check. It finds what a design file can show, and says plainly what it cannot.

## When not to use

- Someone wants a conformance statement or audit: that needs a qualified auditor and the built product.
- The design is ready for disabled users to try: plan sessions with them. A file review never stands in.
- A quick contrast number is all that is needed: run the script directly.

## Inputs

- The screen or flow, with each state named (default, error, empty, loading, focus)
- Real colour values or token names with values, and target sizes. Without values, contrast answers are `cannot tell from a design`.
- The WCAG level, from `project.config.md`
- Optional: the intended focus order

## Workflow

1. Read `project.config.md` for the level and regulatory basis. Read `artefacts/05-accessibility-checklist.md`.
2. Ask: which screen or flow and which states, and can you give real colour values and sizes? Do not proceed on guesses.
3. Fix the scope in writing: what was reviewed, and what was not. Anything not shown reads `not reviewed`, never `pass`.
4. Contrast and sizes: run the script, never estimate.
   - `python3 .claude/skills/a11y-gate/scripts/contrast.py FG BG --kind text|large-text|non-text`
   - `python3 .claude/skills/a11y-gate/scripts/contrast.py --target 44x44`
   - `python3 .claude/skills/a11y-gate/scripts/contrast.py --tokens design-system/tokens.json`
5. Go through the criteria in `references/design-stage-checks.md`, group by group. Answer each: `pass`, `fail` or `cannot tell from a design`.
6. For every `fail`, write the fix as a design change: which token, label, size or spacing. The designer decides whether to make it.
7. Close with what a design file cannot show (screen reader output, real focus behaviour, zoom in a browser, timing, how disabled people complete the task) and with the status line.

## Output

Fill in `artefacts/05-accessibility-checklist.md`. End with the status line exactly:

"Design-stage review of [scope] on [date]. Not an audit. Not a conformance statement."

## Rules

- Never write "accessible", "compliant" or "passes WCAG". A clean table is "no fails found in what was shown".
- Quote no threshold from memory. Use the script output and link the W3C criterion.
- Never describe how a disabled person "would" experience the design.
- Legal duties vary: check with a qualified adviser.

## Verify before finishing

- [ ] Scope lists what was and was not reviewed
- [ ] Every row has a criterion number and one of the three answers
- [ ] Every contrast and size answer comes from script output or is `cannot tell`
- [ ] Every fail has a design-change fix
- [ ] The closing list and the status line are in the output
