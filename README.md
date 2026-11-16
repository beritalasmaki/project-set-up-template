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

## Key decisions so far

- **Small `AGENTS.md` (about 100 lines or less)** acting as an index. Rules that apply rarely live in skills or nested `AGENTS.md` files.
- **Hybrid skills:** install the [product-designers-pack](https://github.com/polar-bear-org/claude-skills/tree/main/packs/product-designers-pack) by 90n from its source (its licence does not allow public redistribution), and write my own skills for public sector and B2B gaps: stakeholder mapping, accessibility and security checks, procurement-ready handoff, NDA-safe case studies.
- **Examples over prohibitions:** annotated good examples guide design quality. Objective rules (design tokens, contrast) are enforced by scripts, and taste is checked in a review step instead of banned up front.
- **Built for accessibility, security and many stakeholders** because that is the kind of work this template supports.
