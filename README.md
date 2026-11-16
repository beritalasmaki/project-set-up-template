# project-set-up-template
Base project template featuring my custom Claude skills, artifacts, and structured AI workflows.

## Status

Planning. Nothing is built yet. The research, decisions and open questions are in **[docs/important-notes.md](docs/important-notes.md)**.

## Key decisions so far

- **Small `AGENTS.md` (about 100 lines or less)** acting as an index. Rules that apply rarely live in skills or nested `AGENTS.md` files.
- **Hybrid skills:** install the [product-designers-pack](https://github.com/polar-bear-org/claude-skills/tree/main/packs/product-designers-pack) by 90n from its source (its licence does not allow public redistribution), and write my own skills for public sector and B2B gaps: stakeholder mapping, accessibility and security checks, procurement-ready handoff, NDA-safe case studies.
- **Examples over prohibitions:** annotated good examples guide design quality. Objective rules (design tokens, contrast) are enforced by scripts, and taste is checked in a review step instead of banned up front.
- **Built for accessibility, security and many stakeholders** because that is the kind of work this template supports.
