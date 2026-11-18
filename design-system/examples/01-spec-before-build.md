# Example 1: Spec before build

**Source:** `docs/spec-review-screen.md` in [demo-t-example](https://github.com/beritalasmaki/demo-t-example) (my own portfolio project, all data fictional).
**Use as an example of:** designing from a person's decision, in the order they need to make it.
**Annotation status:** draft by Claude from reading the source. Owner to confirm.

## Extract (my words, trimmed)

> **The question the screen answers:** *Can I release this, and what am I signing?*
>
> **Reviewer questions, in order**
> 1. What was asked for, and by whom?
> 2. What did the agent actually do?
> 3. What checked it, and what did those checks say?
> 4. Where is it uncertain, and why?
> 5. What happens if I approve, and can this be undone?
>
> The layout should follow that order. Anything that does not answer one of these questions is a candidate for removal.

> ### S4 · Check did not run
> **Succeeds when** "not checked" is visibly different from "checked and fine"…
> **Fails when** missing data is shown as a neutral dash, rendered in the same style as a pass, or left out of the screen entirely.

> **These are assumptions, not research.** No reviewers were interviewed for this project. They are written as testable claims so that a real user session could confirm or break them.

## What it decides

- The screen starts from one question a person must answer, not from a list of components.
- The reviewer's questions are ordered, and the order becomes the layout.
- Each scenario has a success test and a failure test, so it can become a story and a test.
- Hard cases (a check did not run, a decision made by someone else mid-review) are specified, not just the clean path.

## What it gives up

- Speed to visuals: a lot of reading and deciding comes before any screen exists.
- Certainty: the scenarios are assumptions, and the spec says so.

## Why it works as an example

It shows what "design against written context" means in practice. A model that reads this knows what a good brief for a decision screen contains, and that missing data needs its own visible state.

## How to use it

Read it when writing a spec, brief or flow for a screen where someone must decide something. Copy the *moves*: the one question, the ordered questions, success and failure tests, assumptions labelled as assumptions. Do not copy the regions, the wording or the review-screen layout into an unrelated project.
