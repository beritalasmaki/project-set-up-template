# Artefact guide: when to use each one, who reads it, and where the truth lives

**The rule:** write an artefact only if someone will read it and do something with it. If you cannot name the reader and the use, skip it. A document nobody uses is cost without benefit.

## Where the truth lives

**By default, the workspace (a private Git repo) is the source of truth for documentation.** The kind of documents that would otherwise sit in Confluence live here as Markdown. Why:

- One source of truth. Each published copy is a numbered, dated version of the workspace file, so it is clear which version the client has.
- History. You can see what changed, when and why.
- Claude reads these files directly, so the context is always the current document.

**Jira stays for ticket work** (status, owner, schedule). Do not move that into Git. A requirements spec can create Jira tickets, and Jira is the master for what happens to those tickets.

**Exception:** if other people must edit a document in their own tool, that tool is the source of truth for it. Record the exception in `project.config.md` (*Source of truth exceptions*).

**Before relying on this,** check two things:

1. **The client allows it.** Public sector and some B2B clients restrict where their material may be stored. Fill in *Where client material may be stored* in `project.config.md` first. If private GitHub is not allowed, keep client material in the client's own systems.
2. **The client keeps their own history.** At the end of the project, deliver the final versions of what they need (typically requirements, the decision log and the handoff spec) in their own systems. They should not depend on your private repo for their project history.

## How other people read it

Most stakeholders do not use Git. Offer the route that fits them:

1. **A versioned copy in their tool** (Confluence, a shared page or a PDF), in the form and place the client requires. Mark it with the version number, the date and "Source: [link]". Deliver a new version whenever the document changes; old versions stay available. Copied by hand for now. Put the link in the artefact's `Published at` field. If the client wants to maintain a document themselves, agree at the start that their version is the original from then on (see *Source of truth exceptions* in `project.config.md`).
2. **Access to the repo,** for people who can use GitHub. It shows Markdown as readable pages.
3. **Asking an AI assistant,** for people whose organisation allows an AI tool and access to the repo: they can ask it to bring up the documents they need. This is a convenience, not the record. The file is the record. It has not been verified for any client, so check it with each one.

Route 1 works everywhere. Routes 2 and 3 depend on the client's accounts, permissions and policies.

## What each artefact is for

| # | Artefact | Use it when | Main reader | How others get it | Worth it when |
|---|---|---|---|---|---|
| 00 | Product context | At the start, and before any design task | Claude, you | Stays in the workspace. It is the AI's context | Always (core) |
| 01 | Problem framing | A request is vague or already contains a solution | You, the requester, stakeholders | Versioned copy. Share "not solving" with the requester | Always (core) |
| 02 | Stakeholder map | After kick-off | You, sometimes the project lead | Usually private, because it holds conflicts and influence. Share only the decision-rights table | Always (core) |
| 03 | Requirements spec | While scoping | Engineering, security, the team | Tickets are created in Jira from it. The spec document stays in the workspace and is shared as a versioned copy | Always (core). If the client already owns requirements elsewhere, keep here only the accessibility, security and privacy sections and the gaps |
| 04 | User flows and states | You design a task with many steps or states | Engineering, QA, you | Flow drawn in Figma and linked. States and edge cases become acceptance criteria in Jira | Complex flows, many states |
| 05 | Accessibility checklist | Before sharing or handing off | You, the accessibility specialist, engineering | Attached to the handoff. Fails become Jira tickets | Accessibility is required (public sector, AA) |
| 06 | Security and privacy brief | The product handles personal data or has several roles | Security and data protection owners | Sent to those owners. Open questions go into their tracker | Personal or sensitive data, or several user roles |
| 07 | Design system rules | Claude or anyone produces UI | Claude, developers, designers | Links to the design system's own documentation. Do not duplicate it | No design system documentation exists yet |
| 08 | Handoff spec | Designs go to engineering or other vendors | Engineering, vendors | Versioned copy, with Figma links, in their tool | The handoff crosses teams or vendors |
| 09 | Stakeholder feedback log | A review brings many conflicting comments | You, the deciders | Stays with you. Decisions go to the decision log | Several stakeholders disagree. Skip it if comments are already tracked in Figma or Jira and nobody conflicts |
| 10 | Decision log | After every meeting where something is decided | The team, stakeholders, you in six months | Versioned copy the team can find. Delivered to the client at the end | Always (core) |
| 11 | Case study notes | The project ends | You only | Stays private, then becomes a portfolio case study | You plan to publish |

## Check before you create one

1. Who reads it?
2. What will they do with it?
3. How will they get it, and who keeps it up to date?

If you cannot answer all three, do not create it yet. At the end of a project, note which artefacts nobody used and leave them out next time.
