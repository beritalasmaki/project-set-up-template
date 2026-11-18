# Using this template

The full guide: how to start a project from this template, what to do at each step, and why the artefacts exist. The short version is in the [README](../README.md). The skills are listed by stage in [skills.md](skills.md), and the process is drawn in [workflow-map.md](workflow-map.md).

## How to use this repo

### Where this repo fits

This is **your own project workspace**, not the client's codebase. For each client project you create a new, **private** repo from this template. The client's repo is never touched. Your deliverables still go where the client expects them (Figma, Jira, Confluence, their repo). The workspace is where you and Claude think, draft and keep the record of decisions.

If the client wants something from it, such as design system rules or a decision log, you export that file and hand it over. Nothing moves into their repo unless they ask.

### Before you start

Check the client's rules on AI tools and data. In public sector and B2B work you may not be allowed to paste confidential or personal data into an AI tool. If in doubt, ask. Use placeholders for names and figures until you know.

### Step 1: Create the project workspace

1. On GitHub, open this repo and click **Use this template**, then **Create a new repository**. (The button appears only if the repo is marked as a template repository in its settings.)
2. Name it after the project (for example `citizen-portal-workspace`) and set it to **Private**.
3. Clone it and open the folder in Claude Code.
4. If Claude needs to read the client's code, open that checkout as an additional folder. Do not commit workspace files into it.

### Step 2: Fill in `project.config.md`

Tell Claude: *"Ask me the questions in project.config.md one at a time and fill it in."* It covers the project name, client type, accessibility level (ask the client, default AA), regulatory basis, data classes handled, languages, stakeholder roles and tools. It takes about ten minutes, and every other template and skill reads it.

### Step 3: Fill in the five core artefacts, in this order

For each one, you paste in your raw material, Claude drafts, and you correct. Anything Claude cannot find in your material stays marked as a **gap**. Do not let it guess.

| Artefact | Skill | What you give Claude | What you do afterwards | Done when |
|---|---|---|---|---|
| `00 Product context` | none | The client brief, kick-off notes, existing docs | Answer the gaps, delete anything wrong | Users, constraints and "never does" are written, each with a source |
| `01 Problem framing` | `problem-framing` | The request as it was handed to you, any user data | Check the problem has no solution hidden in it | Evidence and gaps are listed, and the requester has seen "not solving" |
| `02 Stakeholder map` | `stakeholder-map` | Names and roles from kick-off, org chart | Mark who decides, and who has the final say if they disagree | Every stakeholder has a role, a need and a "decides / informed" label |
| `03 Requirements spec` | none | The brief, workshop notes, legal or policy documents | Confirm each requirement's owner and source | Accessibility, security and privacy sections are filled in, not skipped |
| `10 Decision log` | `decision-log` | Nothing yet | Add an entry every time something significant is decided | At least the decisions already made at kick-off are recorded |

### Step 4: Do design work against that context

For any task, tell Claude three things: **which skill or artefact to use**, **which context files to read first**, and **what you want back**. Claude produces a draft. You review it, correct it and keep or discard it. Claude proposes, you decide.

Example prompts in this README show the shape, not fixed wording. Phrase yours to fit the project. Something like: *"Use the stakeholder map skill on these kick-off notes. Read the project config first, and show me who decides what and where the conflicts are."*

### Step 5: Add other artefacts when the project needs them

Create an artefact only if someone will read it and use it. Who reads each one, and where it goes (Jira, Confluence, Figma), is in [artefact-guide.md](artefact-guide.md).

| When this happens | Add | Skill |
|---|---|---|
| You start designing screens and flows | `04 User flows and states` | `user-flow-and-states` |
| Designs are ready to check | `05 Accessibility checklist` | `a11y-gate` |
| The product handles personal or sensitive data, or has several user roles | `06 Security and privacy brief` | `security-privacy-brief` |
| You or Claude are producing UI | `07 Design system rules` | none (see `design-system/`) |
| Designs go to engineering or other vendors | `08 Handoff spec` | `procurement-ready-handoff` |
| Reviews bring comments from several stakeholders | `09 Stakeholder feedback log` | none |
| The project is coming to a close | `11 Case study notes` | `nda-safe-case-study` |

### Step 6: Record decisions when they are made

**What this means.** During a project, decisions get made in meetings, reviews and chats: "we drop PDF export from the first release", "the form becomes a step-by-step flow". Months later nobody remembers who decided or why, and the decision gets reopened. The decision log (`10`) is one short entry per significant decision, so the answer is always findable.

**When.** Right after a meeting or review where something was decided. That includes decisions that went against your recommendation. Log only significant ones: hard to reverse, affecting other people, or likely to be questioned later.

**How.** Give Claude your meeting notes and ask it to pull out the decisions and draft entries (the `decision-log` skill does this). You check each one, especially *decided by* and *why*, then save it. Claude must not invent a reason that was not in your notes.

Each entry holds: what was decided, the context, the options that were considered, who decided (by role), the reason, and what would make you reopen it. For example:

> **D-007: Application form becomes a step-by-step flow.** Decided by: service owner, after the stakeholder review. Why: usability sessions showed people abandoning the long single page. Considered: single page with sections. Gives up: faster completion for expert users. Revisit if: completion rates drop after launch.

### Step 7: Check before you share

**Share with whom.** Anyone outside your own working session: stakeholders in a review, the client, engineers or other vendors receiving a handoff, or users in a test. Once it leaves your hands, people treat it as more finished and more reliable than it may be.

**What you check:**

- **Accessibility, at design stage** (`a11y-gate`). Contrast, target sizes, focus order, labels, error messages. Each check is pass, fail or *cannot tell from a design*. Contrast and target sizes are calculated by a script, not estimated.
- **Sameness** (`sameness-check`). Which choices are just defaults that nobody decided on?
- **Claims and confidentiality**, by hand. Does anything say "tested", "accessible" or "compliant" without evidence? Do the screens or prototype contain real personal data, client names or confidential figures?

You get a short list of things to fix. Fix them, then share with one honest line: *"Design-stage review, not an audit."* Claude must never say a design is accessible or compliant.

### Step 8: Keep sessions tidy

A long session fills Claude's memory with old conversation. Answers get worse and slower, and cost more. Because everything important lives in the files, you lose nothing by starting fresh.

- **Switching to a different task**, for example you finished the stakeholder map and move on to user flows: type `/clear`. Claude starts empty and reads the files again.
- **Long session on the same task** that is getting slow or forgetful: type `/compact` to shrink the history.
- **Not sure what is taking up space:** type `/context`.
- **After each finished artefact or task**, make a commit with a clear message, such as "Add stakeholder map first draft". Work is saved and each change stays small.

More in [ai-workflow.md](ai-workflow.md).

### At the end of the project

Use `11 Case study notes` and the decision log to write the portfolio case study (the `nda-safe-case-study` skill checks that permission exists first). Remove confidential details and check what you may publish before anything goes online.

## Artefacts without a skill

Artefacts 00 (product context), 03 (requirements spec), 07 (design system rules) and 09 (stakeholder feedback log) have no skill of their own. Fill them in with Claude by hand: paste your raw material, let Claude draft, and correct it. The same rules apply. Every claim is evidence with a source, or a marked gap.

## What the artefact templates are for

Each template is a blank, structured document in your project workspace that you fill in. Each one answers a question that has to be answered before or during design work. They do two jobs.

**1. They are the AI's working memory.** Claude starts every session knowing nothing about the project. Without written context it fills the gaps with generic guesses, which is where bland, "could be any product" output comes from. A filled-in template gives it the facts in a form it can read: who the users are, which constraints are real, which tokens and components exist. Claude then designs against the project's facts, not its own defaults.

**2. They are the paper trail for people.** In public sector and B2B work, many people need to agree, and someone will later ask "why is it like this?" or "who approved that?". The stakeholder map shows who decides. The feedback and decision logs show what was asked, what was decided, by whom and why. The handoff spec tells engineering and other vendors what is final. The security and privacy brief shows that data and permissions were considered early.

**Example.** For a municipality's citizen portal, you fill in `project.config.md`, then the product context and problem framing from the client's brief, with Claude drafting and you correcting. When you ask Claude to map the application form flow, it reads those files first and produces a flow with error paths and states that fit the users, constraints and stakeholders. Months later, when someone asks why a step was removed, the answer is in the decision log, with the date, the decider and the reason.

**Why not let the AI work it out each time?** That is fine for small tasks. On larger projects the AI forgets between sessions, different people get different answers and nothing is traceable. The templates make the context persistent, shared and checkable.

**Watch out for paperwork.** Filling in every template for a one-week experiment costs more than it gives. Start with the core five and add others only when the project needs them.
