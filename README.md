# Project set-up template

A set-up for UX and product design projects where AI is used with clear roles, written context and checks. Built for public sector and B2B work, where accessibility and security are requirements and many stakeholders have a say.

**The idea in one line:** Claude drafts, I decide, and real people test.

## Status

The template is built and validated by its own checks. It has **not yet been used on a real project**, the skill trigger tests in `evals/` are written but not yet run, and the annotations on the design examples are drafts for me to confirm. Planning notes, decisions and open questions are in **[docs/important-notes.md](docs/important-notes.md)**.

## Best suited for

Projects where getting it wrong is expensive and many people have a say:

- **Public sector services** where accessibility is a legal duty and decisions must be traceable.
- **B2B and enterprise products** with several user roles, permissions and sensitive data.
- **Multi-stakeholder and multi-vendor projects** where design, engineering, security, procurement and business owners all need to agree, and handoffs cross organisations.
- **Complex expert tools and platforms** (data, industrial, AI-assisted tools) where flows have many states and edge cases.
- **Projects that start from a vague request** and need the problem framed before anyone designs.

It is less suited to quick throwaway prototypes, solo experiments or visual-only concept work. For those, use a few artefacts, not the whole set.

## How the workflow fits together

Six stages. Each has a question it answers, skills that help, and artefacts that hold the result. Claude reads the earlier artefacts before it helps with the next one.

| Stage | The question | Skills | Artefacts |
|---|---|---|---|
| 1. Frame the problem | What problem are we solving, and for whom? | `problem-framing` | 00 product context, 01 problem framing |
| 2. Understand the people | Who has a stake, who decides, what must it do? | `stakeholder-map` | 02 stakeholder map, 03 requirements spec |
| 3. Design | What happens step by step, including when it goes wrong? | `user-flow-and-states` | 04 user flows and states, 07 design system rules |
| 4. Check | Is it accessible, safe, and more than defaults? | `a11y-gate`, `security-privacy-brief`, `sameness-check` | 05 accessibility checklist, 06 security and privacy brief |
| 5. Hand off | Can others build it without guessing? | `procurement-ready-handoff` | 08 handoff spec, 09 stakeholder feedback log |
| 6. Record and reflect | Why is it like this, and what can I show? | `decision-log`, `nda-safe-case-study` | 10 decision log, 11 case study notes |

Artefacts 00, 03, 07 and 09 have no skill of their own. I fill them in with Claude by hand. The full skill list, grouped by stage, is in **[docs/skills.md](docs/skills.md)**.

## What is inside

| Path | What it holds |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | Ground rules for any AI agent. A short index (under 100 lines), not a rulebook |
| `project.config.md` | Per-project facts: accessibility level, data classes, languages, stakeholder roles, the client's rules on AI tools |
| `artefacts/` | Twelve spec templates (00–11) and fictional filled-in examples for the core five |
| `design-system/` | Starter tokens, rules, and five annotated examples from my own projects |
| `.claude/skills/` | Nine skills, each with one job. Detail sits in `references/`, and maths in `scripts/` |
| `.claude/settings.json` | Deny rules, for example secrets and force-push |
| `docs/ai-workflow.md` | How I work with AI: roles, limits, session habits |
| `docs/skills.md` | Skill catalogue by stage, generated from the skills |
| `evals/` | Trigger prompts for checking that each skill loads when it should |
| `scripts/`, `.github/` | The checks that keep this repo to its own rules |

## What the artefact templates are for

Each template is a blank, structured document in your project workspace that you fill in. Each one answers a question that has to be answered before or during design work. They do two jobs.

**1. They are the AI's working memory.** Claude starts every session knowing nothing about the project. Without written context it fills the gaps with generic guesses, which is where bland, "could be any product" output comes from. A filled-in template gives it the facts in a form it can read: who the users are, which constraints are real, which tokens and components exist. Claude then designs against the project's facts, not its own defaults.

**2. They are the paper trail for people.** In public sector and B2B work, many people need to agree, and someone will later ask "why is it like this?" or "who approved that?". The stakeholder map shows who decides. The feedback and decision logs show what was asked, what was decided, by whom and why. The handoff spec tells engineering and other vendors what is final. The security and privacy brief shows that data and permissions were considered early.

**Example.** For a municipality's citizen portal, you fill in `project.config.md`, then the product context and problem framing from the client's brief, with Claude drafting and you correcting. When you ask Claude to map the application form flow, it reads those files first and produces a flow with error paths and states that fit the users, constraints and stakeholders. Months later, when someone asks why a step was removed, the answer is in the decision log, with the date, the decider and the reason.

**Why not let the AI work it out each time?** That is fine for small tasks. On larger projects the AI forgets between sessions, different people get different answers and nothing is traceable. The templates make the context persistent, shared and checkable.

**Watch out for paperwork.** Filling in every template for a one-week experiment costs more than it gives. Start with the core five and add others only when the project needs them.

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
| `02 Stakeholder map` | `stakeholder-map` | Names and roles from kick-off, org chart | Mark who decides and where interests conflict | Every stakeholder has a role, a need and a "decides / informed" label |
| `03 Requirements spec` | none | The brief, workshop notes, legal or policy documents | Confirm each requirement's owner and source | Accessibility, security and privacy sections are filled in, not skipped |
| `10 Decision log` | `decision-log` | Nothing yet | Add an entry every time something significant is decided | At least the decisions already made at kick-off are recorded |

### Step 4: Do design work against that context

For any task, tell Claude three things: **which skill or artefact to use**, **which context files to read first**, and **what you want back**. Claude produces a draft. You review it, correct it and keep or discard it. Claude proposes, you decide.

Example prompts in this README show the shape, not fixed wording. Phrase yours to fit the project. Something like: *"Use the stakeholder map skill on these kick-off notes. Read the project config first, and show me who decides what and where the conflicts are."*

### Step 5: Add other artefacts when the project needs them

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

More in [docs/ai-workflow.md](docs/ai-workflow.md).

### At the end of the project

Use `11 Case study notes` and the decision log to write the portfolio case study (the `nda-safe-case-study` skill checks that permission exists first). Remove confidential details and check what you may publish before anything goes online.

## Guardrails

The short version of what Claude is never allowed to do here. The full rules are in [AGENTS.md](AGENTS.md).

- Never calls a design "accessible", "compliant", "secure" or "tested". Checks end as pass, fail or cannot tell.
- Labels every claim as evidence with a source, or as a gap. No invented quotes, research or metrics.
- No client data in prompts or in the repo. Placeholders only.
- No secrets. Deny rules block reading `.env` files and force-pushing.
- Does not replace real people: user testing, testing with disabled users, security review and legal advice.
- Decisions are recorded by role, and Claude proposes while I decide.

## How the repo keeps its own rules

Rules written in a file are easy to break. This repo checks itself.

- `scripts/validate-template.py` fails if `AGENTS.md` goes over 100 lines, a skill has bad frontmatter or no "when not to use", a skill folder gets a stray README, an artefact has no "Done when" section, a link is broken, a skill names an unknown stage, the catalogue is out of date, or any token colour pair falls below its contrast minimum. A GitHub Action runs it on every push.
- `a11y-gate/scripts/contrast.py` does the contrast and target-size maths. Claude does not estimate it. I checked it against known values.
- `scripts/lint-tokens.py` is an optional linter for projects with code. It flags raw colours and off-scale spacing.
- Objective rules are enforced by scripts. Taste is reviewed after a draft, not banned up front.

## Key decisions

- **Small `AGENTS.md`** acting as an index. Rules that apply rarely live in skills or nested `AGENTS.md` files, so they do not cost attention on every turn.
- **My own skills**, written from my own practice and public sources (WCAG 2.2, GOV.UK Service Manual, W3C WAI), with a focus on public sector and B2B needs.
- **Examples over prohibitions.** Annotated good examples from my own work guide design quality, instead of long lists of banned styles. Each shows a decision and what it gave up.
- **Skills in one flat folder, grouped by stage in metadata.** Claude Code documents only the flat layout, so grouping lives in each skill's `metadata.stage` and in the generated catalogue.
- **A private workspace per project,** never the client's repo.

## Limits

- Not yet tried on a real project.
- Skill trigger tests are written, not run.
- The artefact examples are fictional, and the design example annotations are my drafts to confirm.
- The accessibility checks are design-stage reviews. They are not audits, and they never replace testing with assistive technology and disabled users.
