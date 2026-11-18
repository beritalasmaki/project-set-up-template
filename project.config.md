# Project config

Facts about this project that agents and skills read before any task. Fill this in at the start. Write `unknown` instead of guessing, and update it when something changes.

> Tip: tell Claude *"Ask me the questions in project.config.md one at a time and fill it in."*

Use roles, not personal names, and placeholders such as `[Client]`. This file must contain no confidential or personal data.

## Project

- **Name:** [project name]
- **One-line description:** [what the service or product does, for whom]
- **Organisation type:** [public sector / B2B / other]
- **My role:** [for example lead designer, one of three designers]
- **Phase:** [discovery / design / build / live]
- **Key dates:** [kick-off, milestones, launch]

## Accessibility

- **Target level:** WCAG 2.2 AA (change only if the client specifies otherwise)
- **Regulatory or contractual basis:** [for example "public sector accessibility rules", "client requirement", "none", or `unknown`]
- **Assistive technology the team will test with:** [screen readers, magnification, voice control, or `unknown`]
- **Who will test with disabled users, and when:** [role and date, or `not planned`]

## Data and security

- **Data classes the product handles:** [public / internal / personal / sensitive personal / confidential]
- **User roles and permissions:** [list roles, one line each]
- **Where data is shown or exported:** [screens, reports, downloads]
- **Where client material may be stored:** [for example private GitHub allowed, only the client's own systems, or `unknown`. Fill in before saving client material here]
- **Client rules on AI tools:** [allowed / allowed with limits / not allowed / `unknown`]
- **Approved AI tools and what may be pasted into them:** [details or `unknown`]
- **Security contact (role):** [who reviews security questions]

## Languages

- **Interface languages:** [for example English]
- **Reading level or plain-language requirements:** [or `none stated`]

## Stakeholders (summary)

Full detail goes in `artefacts/02-stakeholder-map.md`.

| Role | Interest in one line | Decides? (yes / no / shares) |
|---|---|---|
| [Service owner] | | |
| [Engineering lead] | | |
| [Legal or compliance] | | |
| [Procurement or vendor manager] | | |

## Tools and systems

- **Design:** [for example Figma]
- **Tickets and planning:** [for example Jira]
- **Documentation:** [for example Confluence]
- **Code and design system:** [stack and design system name, or `none yet`]
- **Where requirements and decisions are shared:** [for example Jira stories, Confluence pages, or `not decided`]
- **Source of truth exceptions:** [artefacts the team edits in its own tool instead of this workspace, for example `03 in Jira`, or `none`]

## Constraints

- **Deadline and budget limits:** [or `unknown`]
- **Technical constraints:** [platforms, browsers, legacy systems]
- **Other vendors involved:** [roles, and what each delivers]

## Confidentiality

- **NDA in place:** [yes / no / `unknown`]
- **What may appear in a portfolio case study:** [nothing / anonymised only / agreed after review / `unknown`]
- **Who approves publication (role):** [role]
