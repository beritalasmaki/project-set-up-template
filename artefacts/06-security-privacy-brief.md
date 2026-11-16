# 06 Security and privacy brief

**Status:** draft · **Last updated:** [date] · **Owner (role):** [role]

What data the design shows, to whom, and what questions the security and data protection owners must answer. A design-stage brief, not a security review or legal advice.

## Data inventory

Data classes: see `project.config.md`.

| Data item | Class | Shown where | Who can see it | Stored / exported? | Source |
|---|---|---|---|---|---|
| [item] | | [screens] | [roles] | | evidence: [source] / gap |

## Roles and permissions

| Action or screen | [Role A] | [Role B] | [Role C] |
|---|---|---|---|
| [action] | allow / deny / conditional | | |

Mark every `conditional` and say on what.

## Sign-in and sessions (user experience)

- How users sign in, and what happens when it fails: [description]
- Session timeout: what the user sees and what happens to unsaved work: [description]
- Error messages: do they avoid revealing whether an account exists? [yes / no / gap]

## Consent, retention and deletion

| Question | Answer | Source |
|---|---|---|
| What does the user consent to, and where is it shown? | | |
| How long is the data kept? | | |
| How can a user see, correct or delete their data? | | |

## Audit and traceability

- Actions that must be logged: [list]
- Who can see the log: [role]

## AI in the product

Only if the product uses AI. Otherwise write `not applicable`.

- What data reaches the model: [list]
- What the user is told: [description]
- What happens when the AI is wrong or unavailable: [description]

## Questions for the security and data protection owners

| Question | Owner (role) | Needed by | Answer |
|---|---|---|---|
| | | | |

## Done when

- [ ] Every data item has a class, a place and the roles that see it
- [ ] The permissions table has no empty cells
- [ ] Open questions have an owner and a date
- [ ] Closing line is present: "Design-stage brief. Not a security review. Check legal duties with a qualified adviser."
