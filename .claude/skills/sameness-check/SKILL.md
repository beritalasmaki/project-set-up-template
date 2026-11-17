---
name: sameness-check
description: Reviews one finished design draft for choices left at default, listing typeface, colour, background, layout pattern, radius and shadow, iconography, motion and phrasing, marking each as chosen or inherited, and proposing up to three places for a real decision. Use after a draft exists, when a screen looks fine but could belong to any product, or before sharing a design. Do not use while generating a design, as a list of banned styles, or for accessibility checks (use a11y-gate).
metadata:
  stage: check
---

# Sameness check

A review of a finished draft. It asks which defaults were accepted without a decision. It does not restrict what is generated.

## Inputs

- One design draft: screens, code or a description
- `artefacts/00-product-context.md` and `artefacts/07-design-system-rules.md` if they exist
- Optional: `design-system/examples/` for the level of decision expected

## Workflow

1. Read the product context and design system rules, if present. They say what was supposed to be decided.
2. Build the inventory. For each of: typeface, colour and gradients, backgrounds, layout pattern, radius and shadow, iconography, motion, phrasing: state what the draft does, then mark it `chosen` (the product context or design system gives a reason) or `inherited` (a default, with no reason).
3. Do not mark something `chosen` unless you can point to the reason. If you cannot tell, write `cannot tell`.
4. Pick up to three inherited choices where a real decision would make this product recognisably itself. For each: the decision to make, two options that differ in a meaningful way, and what each gives up.
5. List what should stay standard on purpose (forms, navigation, anything where familiarity helps people).
6. Hand the decisions to the designer. Do not make them.

## Rules

- This is a review. Never use the inventory as a list of things to avoid when generating.
- Standard is not wrong. Familiar patterns are right where users need them.
- Propose options, not verdicts. The designer decides.
- Do not describe taste as a fact. Say what the draft does and ask if it was a decision.

## Output

A short note in the chat, or appended to the designer's review notes: the inventory table, the up to three proposed decisions, and what stays standard.

## Verify before finishing

- [ ] Every row is marked chosen, inherited or cannot tell, with a reason for chosen
- [ ] At most three decisions are proposed, each with two options and what each gives up
- [ ] Nothing was changed in the design
