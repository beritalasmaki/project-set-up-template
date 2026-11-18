# Example 2: A decision record that corrects itself

**Source:** `docs/DECISIONS.md`, entry 0134, in [demo-t-example](https://github.com/beritalasmaki/demo-t-example) (my own portfolio project).
**Use as an example of:** recording a decision honestly, including the moment the first assumption turned out to be wrong.
**Annotation status:** draft by Claude from reading the source. Owner to confirm.

## Extract (my words, heavily trimmed)

> **Context.** A request for a drifting blurred shape behind the logo, so the logo reads better in light and dark mode. An earlier entry had removed every form of backing behind the logo.
>
> **Choice, why a separate element is safe here.** Earlier attempts at a page-wide ambient shape as a separate element broke the accessibility suite's contrast rule. This one is a separate element again, on purpose: it is scoped to the logo's small footprint, which an earlier flat version had already passed many times.
>
> **Finding.** That assumption held for one page but not for the other. There the logo sits next to the breadcrumb, and at the peak of the animation the shape's box overlapped the link by up to 24px. Axe read the overlap as a real background and failed contrast with a measured ratio. It was only caught by sampling the position across the whole animation cycle, not one frame.
>
> **Choice, the fix.** Centre the shape on the logo, keep it inside the logo's footprint, and use a smaller-amplitude animation for the tight placement. Verified the way the bug was found.
>
> **Consequence.** "A small element in this slot is always safe" is no longer true without qualification. A future placement needs the same per-neighbour check, not an assumption carried over from last time.

## What it decides

- A decision record has room for a **Finding**: what was learned after the first choice, and that it changed the choice.
- The consequence says what is *no longer true*, so the next person does not reuse the old assumption.
- Verification uses the same method that found the problem.

## What it gives up

- Brevity. The real entries are long. For a template, trim to the decision, the finding and the consequence.

## Why it works as an example

It shows a record that is honest about being wrong and useful to someone reading it months later. It also links the decision to evidence (a measured contrast ratio), not to opinion.

## How to use it

Read it when recording a design decision, particularly one that changed after testing or review. Note that our decision log template (`artefacts/10-decision-log.md`) has no *Finding* field. If a decision changes after the first choice, add a *Finding* line and, if needed, a new entry that supersedes the old one.
