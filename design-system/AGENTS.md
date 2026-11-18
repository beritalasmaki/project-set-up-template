# Rules for working in `design-system/`

Loads when you design or build UI, or edit tokens.

## Before producing UI

1. Read `rules.md` and `tokens.json`. In a real project, also read `artefacts/07-design-system-rules.md`, which overrides the starter values here.
2. If the task is about structure, such as adding a component, organising folders or proposing an architecture, also read `architecture.md`.
3. Read the one or two examples in `examples/` that match the task (see below). Do not read them all.
4. Use token names, never raw values. If a token or component you need is missing, say so. Do not invent one.

## Examples

Annotated examples of good work. **Copy the move, not the content.** Each shows a decision and what it gave up. Do not reproduce its layout, wording or visuals in a different project.

| Read this | When the task is |
|---|---|
| `01-spec-before-build.md` | writing a spec, brief or flow for a screen where a person must decide something |
| `02-decision-record.md` | recording a design decision, especially one that turned out wrong at first |
| `03-principles-with-trade-offs.md` | writing or applying design principles |
| `04-honest-scope.md` | writing a status line, accessibility report, case study or any claim about what was checked |
| `05-design-iteration.md` | explaining or critiquing a change between two versions of a design |

## Review after a draft

List which choices were left at default (type, colour, layout pattern, radius, motion, phrasing) and ask whether each was a decision. This is a review step, not a rule while generating. The `sameness-check` skill does this.

## Do not change without asking

- A token value or name
- A component's props or API
- The folder structure or where a component lives
- The spacing scale
