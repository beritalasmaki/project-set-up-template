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

Each template is a blank, structured document you copy into a new project and fill in. Each one answers a question that has to be answered before or during design work. They do two jobs.

**1. They are the AI's working memory.** Claude starts every session knowing nothing about the project. Without written context it fills the gaps with generic guesses, which is where bland, "could be any product" output comes from. A filled-in template gives it the facts in a form it can read: who the users are, which constraints are real, which tokens and components exist. Claude then designs against the project's facts, not its own defaults. The skills read and write these files, so each skill and template work as a pair.

**2. They are the paper trail for people.** In public sector and B2B work, many people need to agree, and someone will later ask "why is it like this?" or "who approved that?". The stakeholder map shows who decides. The feedback and decision logs show what was asked, what was decided, by whom and why. The handoff spec tells engineering and other vendors what is final. The security and privacy brief shows that data and permissions were considered early.

**Example.** For a municipality's citizen portal, you fill in `project.config.md`, then the product context and problem framing from the client's brief, with Claude drafting and you correcting. When you ask Claude to design the application form flow, it reads those files first and produces a flow with error paths and states that fit the users, constraints and stakeholders. Months later, when someone asks why a step was removed, the answer is in the decision log, with the date, the decider and the reason.

**Why not let the AI work it out each time?** That is fine for small tasks. On larger projects the AI forgets between sessions, different people get different answers and nothing is traceable. The templates make the context persistent, shared and checkable.

**Watch out for paperwork.** Filling in every template for a one-week experiment costs more than it gives. Start with the core five and add others only when the project needs them.

## How to use this repo

> This describes the intended workflow. The files it mentions are not built yet (see Status).

1. **Copy it into a new project.** Use "Use this template" on GitHub, or copy the folders you need into an existing repo.
2. **Fill in `project.config.md` first.** Set the accessibility level, regulatory basis, data classes, languages and stakeholder roles. The templates and skills read these values, so they stay generic.
3. **Start with the core artefacts.** Product context, problem framing, stakeholder map, requirements and the decision log. Add the others (user flows and states, accessibility checklist, security and privacy brief, design system rules, handoff spec, feedback log, case study notes) only when the project needs them. A small project may need only the core five.
4. **Let Claude draft, and you decide.** Give Claude your raw notes and ask it to fill a template, or run the matching skill. Review every claim, correct it, and mark anything unproven as a gap. Claude never calls work accessible, compliant or tested.
5. **Design against the written context.** Ask Claude for screens, flows or copy only after the context files exist. It reads them first, so the output follows your project's facts, tokens and constraints, not its own defaults.
6. **Log decisions as you go.** Record each significant decision with its context, the decider by role and a revisit trigger, so you can answer "why is it like this?" later.
7. **Review before sharing.** Run the accessibility and sameness checks on drafts, and fix what they find.
8. **Turn it into a case study.** Use the case study notes (kept free of confidential details) to write the portfolio piece.

Keep sessions short and focused: clear between unrelated tasks and commit after each subtask. More in `docs/ai-workflow.md` once it exists.

## Key decisions so far

- **Small `AGENTS.md` (about 100 lines or less)** acting as an index. Rules that apply rarely live in skills or nested `AGENTS.md` files.
- **Hybrid skills:** install the [product-designers-pack](https://github.com/polar-bear-org/claude-skills/tree/main/packs/product-designers-pack) by 90n from its source (its licence does not allow public redistribution), and write my own skills for public sector and B2B gaps: stakeholder mapping, accessibility and security checks, procurement-ready handoff, NDA-safe case studies.
- **Examples over prohibitions:** annotated good examples guide design quality. Objective rules (design tokens, contrast) are enforced by scripts, and taste is checked in a review step instead of banned up front.
- **Built for accessibility, security and many stakeholders** because that is the kind of work this template supports.
