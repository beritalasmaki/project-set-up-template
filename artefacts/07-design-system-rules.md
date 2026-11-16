# 07 Design system rules

**Status:** draft · **Last updated:** [date] · **Owner (role):** [role]

The design system written as rules an agent can follow. Claude reads this before it produces any UI, so it does not invent values or components.

If the project has a design system in code or Figma, summarise it here and link to the source. Do not duplicate it.

## Source of truth

- **Design system:** [name and link, or `none yet`]
- **Tokens file:** [path, once it exists]

## Tokens by role

Refer to tokens by name. Do not use raw values where a token exists.

| Role | Token name | Used for |
|---|---|---|
| Surface | [name] | [backgrounds] |
| Text | [name] | [body, headings] |
| Action | [name] | [primary buttons, links] |
| Feedback | [name] | [error, warning, success] |
| Spacing | [scale] | |
| Type | [scale] | |
| Radius and elevation | [scale] | |

## Component rules

| Component | Use when | Do not use when | States that must exist |
|---|---|---|---|
| [button] | | | default, hover, focus, disabled, loading |

## Layout rules

- [grid, breakpoints, maximum text width]

## Do and do not

| Do | Do not |
|---|---|
| [pattern] | [pattern], because [reason] |

## What the system lacks

Components or tokens that do not exist yet. Agents must flag these and not invent them.

- [item]

## Test

Five prompts to check that Claude follows the rules. Write them once the file is filled in, and rerun them when the rules change.

1. [prompt]

## Done when

- [ ] Tokens have names and roles, with a source
- [ ] Every component has its states
- [ ] "What the system lacks" is filled in
- [ ] The five test prompts were run and the results noted
