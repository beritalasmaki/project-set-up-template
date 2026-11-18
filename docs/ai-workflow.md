# How I work with AI

This page explains how AI is used in my design work, where it is not used, and why. It is written for people (clients, colleagues, anyone evaluating this repo). Agents do not load it by default; `AGENTS.md` holds their rules.

**Status:** some of the artefacts and skills named here are still being built. See the README.

## The principle

**Claude drafts, checks and explains. I make the design decisions. Real people test the work.**

AI speeds up the parts of design work that are about structure and writing things down. It does not replace judgement, user research, specialist review or accountability.

## Roles

| | I decide | Claude drafts and checks | Real people only |
|---|---|---|---|
| Problem and scope | What problem we solve, what is out of scope | A first problem statement from my notes, gaps listed | Talking to users and stakeholders |
| Design direction | Which option, which trade-offs to accept | Options laid out side by side, consequences in words | Final design judgement |
| Accessibility | Whether a fix is made, what level we commit to | Design-stage checks, marked pass, fail or cannot tell | Testing with assistive technology and users with access needs; formal audits |
| Security and privacy | What data is shown to whom | A first data and roles overview, open questions | Security review, legal and data protection advice |
| Stakeholders | Who decides, how to respond to conflicts | Merging and sorting feedback, drafting replies | Negotiation and sign-off |
| Decisions | What was decided and why | Drafting log entries from my notes | Approval by the named decider |

## The workflow

Each stage has an artefact that holds its result. Claude reads the earlier artefacts before it helps with the next.

1. **Frame the problem:** product context, problem framing
2. **Understand the people:** stakeholder map, requirements
3. **Design:** user flows and states, design system rules
4. **Check:** accessibility checklist, security and privacy brief, sameness review
5. **Hand off:** handoff spec, stakeholder feedback log
6. **Record and reflect:** decision log throughout, case study notes at the end

Not every project needs every artefact. Small projects use the core five (product context, problem framing, stakeholder map, requirements, decision log).

## Where I do not use AI

- **No client data in prompts** unless the client's rules allow it. Until I know, I use placeholders.
- **No invented research.** Claude does not write user quotes, interview findings, metrics or testimonials.
- **No stand-ins for users.** I do not ask AI how a user with access needs or a particular user group "would" experience something.
- **No final calls.** Accessibility conformance, legal compliance and security sign-off belong to qualified people.
- **No unreviewed output leaves my hands.** Everything Claude drafts is read and corrected by me first.

## How claims are handled

- Every statement about the project or its users is labelled **evidence** (with a source) or **gap**.
- Every check has one of three answers: **pass**, **fail**, **cannot tell from a design**. A table with no "cannot tell" rows was probably filled in by guessing.
- Reviews are reported as "no fails found in what was shown", never "accessible" or "compliant".
- Anything shared outside my own working session carries the line: *design-stage review, not an audit.*

## Reviewing AI output

After a draft, I run two reviews:

1. **Accessibility check:** does the design hold up against the agreed WCAG level where a design file can show it?
2. **Sameness check:** which choices were left at default, and was that a decision? Three of them should become a real decision.

These are reviews of a finished draft, not rules that restrict Claude while it works. Quality comes from good written context and good examples, not from long lists of prohibitions.

## Session habits

Everything important lives in files, so sessions can be short and disposable.

- **New task, new session.** Type `/clear` when switching tasks. Claude starts empty and re-reads the files it needs.
- **Long session, same task.** Type `/compact` once it feels slow or forgetful.
- **Check what is loaded.** Type `/context` to see what takes up space.
- **Point to files.** Name the path instead of asking Claude to search the repo.
- **Commit after each finished subtask** with a message that says what changed.
- **Do not edit `AGENTS.md` mid-session.** Changing it breaks the cache and costs more.

## Keeping instructions lean

- `AGENTS.md` is an index of about 100 lines or less. It loads on every turn.
- Rules that only apply to some tasks live in skills or in nested `AGENTS.md` files inside a folder.
- Skills do one job each, and their details sit in a `references/` folder that is only read when needed.
- Project facts live in `project.config.md`, not in skill instructions, so the same skills work across projects.
