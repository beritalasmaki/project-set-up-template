---
name: user-flow-and-states
description: Builds artefacts/04-user-flows-and-states.md for one task, with entry points, numbered steps pairing what the user does with how the system responds, decision points with the assumption behind each, error and recovery paths, exits, a table of screens against states, an edge-case sweep, and gaps ordered by what blocks the build first. Use when asked to map a flow, work out what happens when something goes wrong, list screen states, or before designing or handing off a task. Do not use for visual design, for writing requirements, or to mark a state as designed when no design exists.
metadata:
  stage: design
---

# User flow and states

One task as a flow, then every screen against its states. It shows what has not been designed, so engineering does not find out on day three of the build.

## Inputs

- One task and the user group doing it
- `artefacts/00-product-context.md` and `artefacts/03-requirements-spec.md` if they exist
- `artefacts/06-security-privacy-brief.md` for roles and sessions, if it exists
- The existing `artefacts/04-user-flows-and-states.md`, if any

## Workflow

1. Take **one task** per run. If the designer names several, do them one by one.
2. Read the inputs. Read `references/states-and-edge-cases.md` for the state and edge-case prompts.
3. **Entry points:** where users arrive from, including links and notifications.
4. **Steps:** a table of numbered steps. Each pairs what the user does with how the system responds, and names the screen. Do not write steps with no system response.
5. **Decision points:** each with an ID, the condition, where it leads, and the **assumption** behind it. Cite a source or mark `gap`.
6. **Errors and recovery:** for each step that can fail, what goes wrong, what the user sees, how they recover and where they land. Include no permission, timeout and lost connection.
   Then ask, for each step, **who might find it challenging and why** (for example little digital experience, assistive technology, a phone in a hurry, an interruption) and what the design does about it. The same path can be smooth for one user and unbearable for another. Record it under *Challenging paths for some users*. Ask the designer. If there is no evidence, write `gap`. Never claim how a group experiences a step.
7. **Exits:** success, abandon and hand-off to another channel.
8. **Screens against states:** list each screen. Mark each cell `designed`, `missing` or `not needed` (with the reason). **Default every cell to `missing`.** Mark `designed` only when the designer says a design exists.
9. **Edge cases:** sweep each screen using the prompts. List those that matter.
10. **Gaps:** order the `missing` cells by what blocks the build first.
11. Ask at most three questions that would settle the biggest unknowns, then update the file.

## Rules

- Never mark a state `designed` yourself. A flow on paper is not a design.
- `not needed` needs a reason written beside it.
- Do not invent business rules. If a decision point has no source, write the assumption and mark it `gap`.
- Use roles, not personal names. Use made-up values in any example data.

## Output

Update `artefacts/04-user-flows-and-states.md`. Set `Status: draft` until the designer has reviewed it.

## Verify before finishing

- [ ] The flow covers errors and recovery, not only the happy path
- [ ] Every step has a system response
- [ ] For each step, who might find it challenging is asked, and the answer or a `gap` is written
- [ ] Every decision point has an assumption and a source or `gap`
- [ ] Every screen has every state marked, and `designed` was set only by the designer
- [ ] Gaps are ordered by what blocks the build first
