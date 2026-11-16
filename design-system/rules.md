# Design system rules (starter)

Generic rules for any project built from this template. Adapted from my own design system work. In a real project, `artefacts/07-design-system-rules.md` holds the project's own rules and takes precedence.

## Tokens

- `tokens.json` is the single source of truth. Values change there first.
- Two layers. **Primitives** are raw values (`primitive.color.neutral.900`). **Semantic tokens** say what a value is for (`semantic.color.content.primary`). Build against the semantic layer only.
- Never write a raw colour, radius, shadow or font size where a token exists. If you repeat a value that has a name, that is a bug.
- Spacing uses only the scale in `tokens.json` (4, 8, 12, 16, 24, 32, 48, 64 px). If a layout needs something in between, use the nearer value. Do not add a new one.
- A token that does not exist is a gap in the system. Flag it. Do not work around it with a raw value.

## Components

- If a component exists for the job, use it. Do not rebuild its styles by hand.
- If it cannot do what is needed, say so. That is a system gap and is worth fixing properly.
- Every component has its states designed: default, hover, focus, disabled, loading, error where relevant.

## Accessibility baseline

Part of every component, not a final check.

- Semantic HTML. A button is a `button`, a link is an `a`.
- Everything interactive works with a keyboard, in a logical order.
- A visible focus indicator is always present. Never remove it.
- Target size: at least the `size.target.min` token, and `size.target.comfortable` for primary touch actions.
- Colour is never the only way meaning is shown. Pair it with text or an icon.
- Text and non-text contrast are checked with `.claude/skills/a11y-gate/scripts/contrast.py`, from real values, never estimated.
- Respect reduced motion. Do not override the global rule.
- Use ARIA to communicate state (for example `aria-busy`, `aria-expanded`). Mark decorative elements `aria-hidden`.

## Language

- Say what is happening and what to do next. Plain words first. Where an expert term is standard, show it next to the plain one.
- One date and time format across the product.
- Button labels say what happens next, exactly as they appear in the spec.

## Enforcement

Objective rules are checked by scripts, not by prompting.

- `scripts/lint-tokens.py` flags raw hex colours and off-scale pixel values in code. Optional: copy it into a project with code.
- To run it after every edit in Claude Code, add a `PostToolUse` hook for `Edit|Write` to that project's `.claude/settings.json` that runs the script on the changed file.
- Taste (does it look generic?) is not enforced. It is reviewed after a draft with the `sameness-check` skill.
