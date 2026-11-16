---
name: stakeholder-map
description: Builds or updates the stakeholder map in artefacts/02-stakeholder-map.md from kick-off notes, meeting notes and organisation information, with roles (not personal names), interests, decision rights, conflicts set side by side, and gaps for stakeholders not yet met. Use when asked to map stakeholders, work out who decides what, prepare for a multi-stakeholder review, or after a kick-off or a change of people. Do not use for sorting review comments (that is artefacts/09-stakeholder-feedback-log.md), for user personas, or for deciding between stakeholders.
---

# Stakeholder map

Makes visible who has a stake, who decides, and where interests collide. Claude drafts, the designer decides what is true.

## Inputs

- Raw material: kick-off notes, org charts, emails or meeting notes (with personal names allowed in the input, never in the output)
- `project.config.md` for the stakeholder summary and confidentiality rules
- The existing `artefacts/02-stakeholder-map.md`, if any

## Workflow

1. Read the inputs and the existing file. Do not load other artefacts.
2. List each stakeholder as a **role**. Convert personal names to roles. If a role is unclear, mark it `gap` and ask.
3. For each: interest, what they need to see to say yes, influence, and whether they decide, share a decision, or are informed. Cite the source (`evidence: kick-off notes, 2 Mar`) or mark `gap`.
4. Build the decision-rights table for scope, design direction, accessibility trade-offs, security and data handling, and release. Use `references/decision-rights-questions.md` to find who decides when the material is silent. Ask the designer. Do not assume.
5. Record conflicts **side by side**: who wants what, and who decides. Do not resolve them. Do not suggest who is right.
6. List stakeholders mentioned but not yet met as gaps. Note the risk each gap creates.
7. Ask at most three questions that would most improve the map, then update the file.

## Rules

- Roles only. No personal names, no personal details, nothing about a person's character.
- Never infer a position. If a stakeholder's view was not stated in the material, write `gap`.
- Never rank people. Influence is about the decision, not the person.

## Output

Update `artefacts/02-stakeholder-map.md`. Set `Status: draft` until the owner has reviewed it.

## Verify before finishing

- [ ] Every stakeholder has a role, an interest and a decides value
- [ ] Decision rights exist for scope, accessibility, security and release
- [ ] Every conflict names a decider and sits side by side
- [ ] No personal names appear in the file
- [ ] Every claim has a source or is marked `gap`
