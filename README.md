# project-set-up-template
Base project template featuring my custom Claude skills, artifacts, and structured AI workflows.

## Status

Planning. Nothing is built yet. The research, decisions and open questions are in **[docs/important-notes.md](docs/important-notes.md)**.

## Best suited for

This set-up is built for projects where getting it wrong is expensive and many people have a say:

- **Public sector services** where accessibility is a legal duty and decisions must be traceable.
- **B2B and enterprise products** with several user roles, permissions and sensitive data.
- **Multi-stakeholder and multi-vendor projects** where design, engineering, security, procurement and business owners all need to agree, and handoffs cross organisations.
- **Complex expert tools and platforms** (data, industrial, AI-assisted tools) where flows have many states and edge cases.
- **Projects that start from a vague request** and need the problem framed before anyone designs.

It is less suited to quick throwaway prototypes, solo experiments or visual-only concept work. For those, use a few artefacts, not the whole set.

## What the artefact templates are for

Each template is a blank, structured document in your project workspace that you fill in. Each one answers a question that has to be answered before or during design work. They do two jobs.

**1. They are the AI's working memory.** Claude starts every session knowing nothing about the project. Without written context it fills the gaps with generic guesses, which is where bland, "could be any product" output comes from. A filled-in template gives it the facts in a form it can read: who the users are, which constraints are real, which tokens and components exist. Claude then designs against the project's facts, not its own defaults. The skills read and write these files, so each skill and template work as a pair.

**2. They are the paper trail for people.** In public sector and B2B work, many people need to agree, and someone will later ask "why is it like this?" or "who approved that?". The stakeholder map shows who decides. The feedback and decision logs show what was asked, what was decided, by whom and why. The handoff spec tells engineering and other vendors what is final. The security and privacy brief shows that data and permissions were considered early.

**Example.** For a municipality's citizen portal, you fill in `project.config.md`, then the product context and problem framing from the client's brief, with Claude drafting and you correcting. When you ask Claude to design the application form flow, it reads those files first and produces a flow with error paths and states that fit the users, constraints and stakeholders. Months later, when someone asks why a step was removed, the answer is in the decision log, with the date, the decider and the reason.

**Why not let the AI work it out each time?** That is fine for small tasks. On larger projects the AI forgets between sessions, different people get different answers and nothing is traceable. The templates make the context persistent, shared and checkable.

**Watch out for paperwork.** Filling in every template for a one-week experiment costs more than it gives. Start with the core five and add others only when the project needs them.

## How to use this repo

> This describes the intended workflow. The files it mentions are not built yet (see Status).

### Where this repo fits

This is **your own project workspace**, not the client's codebase. For each client project you create a new, **private** repo from this template. The client's repo is never touched. Your deliverables still go where the client expects them (Figma, Jira, Confluence, their repo). The workspace is where you and Claude think, draft and keep the record of decisions.

If the client wants something from it, such as design system rules or a decision log, you export that file and hand it over. Nothing moves into their repo unless they ask.

### Before you start

Check the client's rules on AI tools and data. In public sector and B2B work you may not be allowed to paste confidential or personal data into an AI tool. If in doubt, ask. Use placeholders for names and figures until you know.

### Step 1: Create the project workspace

1. On GitHub, open this repo and click **Use this template**, then **Create a new repository**.
2. Name it after the project (for example `citizen-portal-workspace`) and set it to **Private**.
3. Clone it and open the folder in Claude Code.
4. If Claude needs to read the client's code, open that checkout as an additional folder. Do not commit workspace files into it.

### Step 2: Fill in `project.config.md`

Tell Claude: *"Ask me the questions in project.config.md one at a time and fill it in."* It covers the project name, client type, accessibility level (ask the client, default AA), regulatory basis, data classes handled, languages, stakeholder roles and tools. It takes about ten minutes, and every other template and skill reads it.

### Step 3: Fill in the five core artefacts, in this order

For each one, you paste in your raw material, Claude drafts, and you correct. Anything Claude cannot find in your material stays marked as a **gap**. Do not let it guess.

| Artefact | What you give Claude | What you do afterwards | Done when |
|---|---|---|---|
| `00 Product context` | The client brief, kick-off notes, existing docs | Answer the gaps, delete anything wrong | Users, constraints and "never does" are written, each with a source |
| `01 Problem framing` | The request as it was handed to you, any user data | Rewrite the problem as a user situation with no solution in it | The problem has no fix hidden in it, and evidence and gaps are listed |
| `02 Stakeholder map` | Names and roles from kick-off, org chart | Mark who decides and where interests conflict | Every stakeholder has a role, a need and a "decides / informed" label |
| `03 Requirements spec` | The brief, workshop notes, legal or policy documents | Confirm each requirement's owner and source | Accessibility, security and privacy sections are filled in, not skipped |
| `10 Decision log` | Nothing yet | Add an entry every time something significant is decided | At least the decisions already made at kick-off are recorded |

### Step 4: Do design work against that context

For any task, ask Claude to use the matching skill, for example: *"Run the user flow skill for the application form. Read the product context and requirements first."* Claude produces a draft. You review it, correct it and keep or discard it. Claude proposes, you decide.

### Step 5: Add other artefacts when the project needs them

| When this happens | Add |
|---|---|
| You start designing screens and flows | `04 User flows and states` |
| Designs are ready to check | `05 Accessibility checklist` |
| The product handles personal or sensitive data, or has several user roles | `06 Security and privacy brief` |
| You or Claude are producing UI | `07 Design system rules` |
| Designs go to engineering or other vendors | `08 Handoff spec` |
| Reviews bring comments from several stakeholders | `09 Stakeholder feedback log` |
| The project is coming to a close | `11 Case study notes` |

### Step 6: Keep the record as you go

After every meeting or review where something was decided, tell Claude: *"Add a decision record: [what was decided], decided by [role], because [reason]."* Review the entry before you save it.

### Step 7: Check before you share

Before a design goes to a stakeholder or to engineering, ask Claude to run the accessibility check and the sameness check on it. Fix what they find. Neither one is an audit. Say so when you share the result.

### Step 8: Keep sessions tidy

Clear the session between unrelated tasks and commit after each subtask. More in `docs/ai-workflow.md` once it exists.

### At the end of the project

Use `11 Case study notes` and the decision log to write the portfolio case study. Remove confidential details and check what you may publish before anything goes online.

## Key decisions so far

- **Small `AGENTS.md` (about 100 lines or less)** acting as an index. Rules that apply rarely live in skills or nested `AGENTS.md` files.
- **My own skills, inspired by the structure of** the [product-designers-pack](https://github.com/polar-bear-org/claude-skills/tree/main/packs/product-designers-pack) by 90n. Their licence does not allow public redistribution, so nothing is copied or installed. The skills are written from my own practice and public sources (WCAG 2.2, GOV.UK Service Manual, W3C WAI), with a focus on public sector and B2B gaps: stakeholder mapping, accessibility and security checks, procurement-ready handoff, NDA-safe case studies.
- **Examples over prohibitions:** annotated good examples guide design quality. Objective rules (design tokens, contrast) are enforced by scripts, and taste is checked in a review step instead of banned up front.
- **Built for accessibility, security and many stakeholders** because that is the kind of work this template supports.
