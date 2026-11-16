# Important notes

Planning notes for this template, captured before building anything. They record what was researched, what was decided, what is still open, and why. Update this file when a decision changes.

**Status:** planning. Nothing from the structure below is built yet.

## 1. Purpose

A project set-up template for every new project, and a public example of how I handle AI workflows as a UI/UX designer.

It should contain:

- **Artefacts:** spec templates and `AGENTS.md` guidance.
- **Skills:** relevant to design work, especially public sector and B2B projects where **security and accessibility** matter and **several stakeholders** have to be managed.

## 2. What the research found

### My portfolio repo ([berit-portfolio](https://github.com/beritalasmaki/berit-portfolio))

- `design-system-use-case` already has the pattern to reuse: a detailed `AGENTS.md` and a one-line `CLAUDE.md` containing `@AGENTS.md`.
- The working style recorded there: explain changes in plain language, offer options instead of choosing silently, keep boundaries clean.
- Stack: React/Next.js, TypeScript, Tailwind, shadcn/ui, Vercel, Supabase.
- Case studies exist in English and Finnish, so i18n belongs in the template.
- Good sources of example work: `design-system-use-case`, the agent run review dashboard, deliberate choices in `portfolio-homepage`.

### The product-designers-pack ([polar-bear-org/claude-skills](https://github.com/polar-bear-org/claude-skills/tree/main/packs/product-designers-pack))

- 32 skills (`pdes-*`) across eight stages, from framing the problem to the portfolio case study.
- Every skill holds one line: Claude drafts, checks and explains; the designer decides; nothing is called tested, accessible or ready that was not.
- General-purpose. It has no public sector content: no EU accessibility directive, GDPR, procurement or multi-vendor handoff, and little on stakeholder mapping.

### Licence (binding constraint)

The pack is free to use **inside your company and for your own client work, not for resale**. It must not be redistributed publicly or presented as your own.

**Decision:** do **not** copy the pdes skills into this repo if it is public. Install the pack from its source (`/plugin marketplace add polar-bear-org/claude-skills`, then `/plugin install product-designers-pack@90n-skills`), credit 90n, and write my own skills for the gaps.

## 3. Principles for agent files and skills

From the guidance reviewed in the planning session.

- **Progressive disclosure.** Only a skill's frontmatter loads at startup. The body loads when a task matches.
- **`AGENTS.md` / `CLAUDE.md`:** target 50–100 lines, maximum about 200. It loads on every turn, so it should be an index (stack, commands, core boundaries, pointers), not a rulebook.
- **`SKILL.md`:** under 500 lines. Move detail into `references/`, one level deep.
- **One job per skill.** The `description` carries most of the triggering: third person, action verbs, trigger phrases and an explicit "do not use for…".
- **Validation at the end of every skill:** a verify-and-fix checklist.
- **Rules that apply rarely belong in a skill**, not in `AGENTS.md`.
- **Nested `AGENTS.md`** files load only when working in that folder.
- **Config separate from instructions.** Per-project facts live in a manifest so skills stay reusable.
- **Author skills with `skill-creator`** so trigger accuracy is tested, not guessed.
- **Session hygiene:** `/clear` between unrelated tasks, `/compact` at about 40–50% context, `/context` to inspect what is loaded, commit after each subtask, check named paths before broad searches.

### Claims to verify before documenting as fact

- **`.claudeignore`:** unconfirmed as a Claude Code feature. Plan: use `permissions.deny` rules in `.claude/settings.json` (lockfiles, `dist/`, `.next/`, `.env*`), and check the current docs first.
- **`/design-sync`:** needs a React repo and a Team or Enterprise plan. Treat it as optional and check what it does before documenting it.
- **Hard numbers** (4 MiB, 32 KiB, "40–60% token savings") came from secondary sources. Use the 100/200/500 line figures as targets and do not quote the rest.

## 4. Design quality: examples over prohibitions

**Decision:** guide the AI with a lot of good, annotated examples. Do not rely on a standing "AI slop" ban list.

Why:

- Ban lists prime what they name, go out of date, and cannot describe what *good* looks like.
- They add to the always-on context cost.

Cautions:

- **Examples can anchor.** One example gets cloned. Use several that differ from each other, and annotate each with *what was decided, what was given up, and who it was for*. Include "this, not that" pairs.
- **Objective constraints are not taste rules and stay enforced:** token use (no raw hex, no arbitrary pixel values) and contrast. These are checked by a lint script or hook, not left to prompting.

| Layer | What goes there | How it is used |
|---|---|---|
| Generation (positive) | `design-system/examples/`: 4–6 annotated good examples | Claude reads them before designing |
| Hard constraints (objective) | Tokens, hex/px lint, contrast script | Enforced by hook |
| Review (negative, after the fact) | A short sameness check: which defaults were accepted without a decision? | Run once on a finished draft, never in the generation prompt |

Example sources are my own work. For client and public sector work under NDA, use anonymised decision notes, not screenshots.

## 5. Proposed structure

```
AGENTS.md (≤100 lines)   CLAUDE.md (@AGENTS.md)   project.config.md   README.md
docs/            important-notes.md · ai-workflow.md · workflow-map.md · decisions/
artefacts/       AGENTS.md + spec templates
                   00 product context · 01 problem framing · 02 stakeholder map
                   03 requirements spec (accessibility + security) · 04 user flow and states
                   05 accessibility checklist (WCAG 2.2 AA) · 06 security and privacy brief
                   07 design system rules · 08 handoff spec · 09 stakeholder feedback log
                   10 case study notes (NDA-safe)
design-system/   AGENTS.md · tokens.json · rules.md · examples/
.claude/
  settings.json  (deny rules, PostToolUse hook)
  skills/        stakeholder-map · a11y-gate (+ scripts/) · security-privacy-brief
                 · procurement-ready-handoff · nda-safe-case-study
scripts/         lint-tokens · validate-template
.github/         workflow running validate-template
```

**Own skills (the gaps in the pack):**

- `stakeholder-map`: roles, interests, who decides, conflicts side by side.
- `a11y-gate`: design-stage WCAG 2.2 AA check with the answers pass, fail, or cannot tell from a design. Contrast and target-size maths done by a script.
- `security-privacy-brief`: data classes, roles and permissions, GDPR notes.
- `procurement-ready-handoff`: handoff for multi-vendor teams.
- `nda-safe-case-study`: project notes to portfolio case study with confidential details removed.

**The template validates itself:** a check confirms every `SKILL.md` has valid frontmatter and is under 500 lines, and that `AGENTS.md` is at most 100 lines.

## 6. Guardrails for `AGENTS.md`

- Claude never claims "accessible", "compliant" or "tested". It reports pass, fail or cannot tell.
- No client data, names or screenshots in prompts or in the repo. Use placeholders for anything under NDA.
- No secrets in the repo (`.env.example` only, plus a deny rule).
- Decisions are logged by role. Claude proposes, I decide.
- Every design claim links to evidence or is marked as a gap.

## 7. Open decisions

1. **Public or private repo?** Assumed public, which makes the licence constraint binding.
2. **Skills approach:** install the pack and add my own skills (recommended).
3. **Code scaffold?** Recommended: docs, skills and tokens only, with an optional `scaffold/` later.
4. **Language:** English only, or also Finnish versions of the templates?
5. **Standards focus:** name Finnish and EU requirements explicitly (EU accessibility directive, EN 301 549, GDPR) or keep generic?
6. **Example work:** which 4–6 pieces of my work show what good looks like?

## 8. Next steps

1. Answer the open decisions above.
2. Verify the `.claudeignore` and `/design-sync` claims against current docs.
3. Build in this order: `AGENTS.md` and README, `project.config.md`, artefact templates, tokens and examples, skills, validation scripts.
