---
name: security-privacy-brief
description: Builds the design-stage security and privacy brief in artefacts/06-security-privacy-brief.md from screens, flows and requirements, covering data items and classes, who sees what, roles and permissions, sign-in and session behaviour, consent and retention, audit needs, AI in the product, and open questions for the security and data protection owners. Use when asked about data handling, permissions or roles in a design, personal or sensitive data on screens, or before handoff of a product with several user roles. Do not use for a security review, a penetration test, legal advice or a data protection impact assessment.
metadata:
  stage: check
---

# Security and privacy brief

Shows what data a design displays, to whom, and which questions the security and data protection owners must answer. It is a design-stage brief. It is not a review and not legal advice.

## Inputs

- `project.config.md`: data classes, user roles, regulatory basis, client rules on AI tools
- The screens or flows, and `artefacts/03-requirements-spec.md` if it exists
- Any statements from the security or data protection owner

## Workflow

1. Read `project.config.md` and the existing `artefacts/06-security-privacy-brief.md`.
2. **Data inventory:** list each data item shown, entered or exported. Give its class from the config. Name the screens and the roles that see it. Cite a source or mark `gap`.
3. **Roles and permissions:** build the table of actions against roles. Mark every `conditional` and say on what. Leave no empty cell. Ask when a cell is unknown.
4. **Sign-in and sessions:** describe what the user sees at sign-in failure and at timeout, and what happens to unsaved work. Check that error messages do not reveal whether an account exists.
5. **Consent, retention, deletion:** what is the user told, and how can they see, correct or delete data? Mark unknowns as gaps.
6. **Audit:** which actions need a record, and who reads it.
7. **AI in the product:** only if the product uses AI. What data reaches a model, what the user is told, and what happens when it is wrong or unavailable. Otherwise write `not applicable`.
8. **Questions for owners:** turn every gap into a question with an owner role and a date. `references/questions-for-owners.md` has prompts.

## Rules

- Do not state what a law requires. Use the regulatory basis from the config and refer legal questions to the right owner.
- Do not say a design is "secure" or "compliant". Say what was shown and what is open.
- Use roles, not personal names. Use placeholders for real data.
- If a field would show real personal data in an example, use made-up values.

## Output

Update `artefacts/06-security-privacy-brief.md`. End with: "Design-stage brief. Not a security review. Check legal duties with a qualified adviser."

## Verify before finishing

- [ ] Every data item has a class, the screens and the roles that see it
- [ ] The permissions table has no empty cells
- [ ] Every gap has become a question with an owner role and a date
- [ ] The closing line is present
- [ ] No real personal data is in the file
