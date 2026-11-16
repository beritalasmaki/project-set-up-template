---
name: nda-safe-case-study
description: Turns project notes and decision records into portfolio case study notes in artefacts/11-case-study-notes.md that are safe to publish, with permission checked first, confidential details removed or generalised, decisions shown with options and trade-offs, outcomes taken only from real data, and an anonymisation check. Use when asked to write up a project for a portfolio, prepare a case study from client work, or check a draft for confidential details. Do not use to invent outcomes, user quotes or metrics, and do not use for projects where publication has not been approved.
---

# NDA-safe case study

Shows how I worked without exposing the client. Claude drafts, the designer decides what is shared, and the client's approval comes first.

## Inputs

- `project.config.md`: the confidentiality section (NDA, what may be published, who approves)
- `artefacts/10-decision-log.md` and the artefacts the designer chooses to use
- Optional: a list of confidential terms, kept in `.confidential-terms` (one per line, never committed)

## Workflow

1. Read the confidentiality section of the config. **If publication is not approved or unknown, stop** and say so. Offer to prepare notes for the designer's private use only.
2. Choose three to five decisions from the decision log. For each: the situation, the options, what was chosen, what it gave up, and who decided by role.
3. Generalise: replace organisations, products, people and figures with descriptions ("a public body", "a regional service"). Remove screenshots, or mark them for redrawing.
4. **What real users did:** only from actual sessions or data, as n of N and how it was gathered. If there was none, write `no user testing`. Say so in the case study.
5. **Outcomes:** only from real data with a source. Otherwise `not measured`.
6. **How AI was used:** where it helped, where it was not used, and what was checked by hand.
7. Run the confidential-terms scan if a list exists: `python3 .claude/skills/nda-safe-case-study/scripts/scan-confidential.py artefacts/11-case-study-notes.md`.
8. Complete the anonymisation check in the template. Mark anything unchecked.

## Rules

- Never invent a quote, a metric, an outcome or a finding.
- Do not carry over names, figures or internal terms from the inputs, even to illustrate.
- Show trade-offs. A case study with only wins is a claim, not a case.
- Approval from the client is recorded, or the notes are marked private.

## Output

Update `artefacts/11-case-study-notes.md`. The anonymisation check must be complete before the notes become a published case study.

## Verify before finishing

- [ ] Permission is recorded, or the notes are marked private
- [ ] Each decision shows options and what it gave up
- [ ] Every outcome has a source or is `not measured`
- [ ] The scan ran clean, or no list exists and that is stated
- [ ] The anonymisation check is complete
