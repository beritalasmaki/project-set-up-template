# Artefact guide: when to use each one, and where it goes

**The rule:** write an artefact only if someone will read it and do something with it. If you cannot name the reader and the use, skip it. A document nobody uses is cost without benefit.

## Two kinds of artefact

- **Working memory.** Read mostly by Claude and by you. It stays in the workspace and helps drafts fit the project.
- **Shared.** Read by people outside the workspace. You draft it here, then publish it where the team already works (Jira, Confluence, Figma, a shared drive). The published copy becomes the source of truth.

The workspace never replaces the client's tools. Nobody should have to open it to do their job. Which tools a project uses is recorded under *Tools and systems* in `project.config.md`.

## What each artefact is for

| # | Artefact | Use it when | Main reader | Where it typically goes | Worth it when |
|---|---|---|---|---|---|
| 00 | Product context | At the start, and before any design task | Claude, you | Stays in the workspace. It is the AI's context | Always (core) |
| 01 | Problem framing | A request is vague or already contains a solution | You, the requester, stakeholders | Brief or Confluence page. Share "not solving" with the requester | Always (core) |
| 02 | Stakeholder map | After kick-off | You, sometimes the project lead | Usually stays private, because it holds conflicts and influence. Share only the decision-rights table | Always (core) |
| 03 | Requirements spec | While scoping | Engineering, security, the team | Requirements become Jira epics or stories, or a Confluence page. The Jira or Confluence copy is the source of truth once published | Always (core). If the client already owns requirements in Jira, keep here only the accessibility, security and privacy sections and the gaps |
| 04 | User flows and states | You design a task with many steps or states | Engineering, QA, you | Flow in Figma, linked. States and edge cases become acceptance criteria in Jira | Complex flows, many states |
| 05 | Accessibility checklist | Before sharing or handing off | You, the accessibility specialist, engineering | Attached to the handoff. Fails become Jira tickets | Accessibility is required (public sector, AA) |
| 06 | Security and privacy brief | The product handles personal data or has several roles | Security and data protection owners | Sent to those owners. Open questions go into their tracker | Personal or sensitive data, or several user roles |
| 07 | Design system rules | Claude or anyone produces UI | Claude, developers, designers | The design system's own documentation, linked here. Do not duplicate it | No design system documentation exists yet |
| 08 | Handoff spec | Designs go to engineering or other vendors | Engineering, vendors | Confluence or Jira, with Figma links | The handoff crosses teams or vendors |
| 09 | Stakeholder feedback log | A review brings many conflicting comments | You, the deciders | Stays with you. Decisions go to the decision log | Several stakeholders disagree. Skip it if comments are already tracked in Figma or Jira and nobody conflicts |
| 10 | Decision log | After every meeting where something is decided | The team, stakeholders, you in six months | Shared wiki page, or a Confluence page the team can read | Always (core) |
| 11 | Case study notes | The project ends | You only | Stays private, then becomes a portfolio case study | You plan to publish |

## How to publish an artefact

1. Finish the draft in the workspace and review it. Set `Status: reviewed`.
2. Copy it to the team's tool. For a requirements spec this is Jira tickets or a Confluence page. For a decision log, a shared page.
3. Put the link in the artefact's `Published at` field.
4. From then on, edit the published copy. If the workspace copy stops being updated, mark it stale or update it from the published one. There is no automatic sync, and that is a known cost of this approach.

## Check before you create one

1. Who reads it?
2. What will they do with it?
3. Where will it live, and who keeps it up to date?

If you cannot answer all three, do not create it yet. At the end of a project, note which artefacts nobody used and leave them out next time.
