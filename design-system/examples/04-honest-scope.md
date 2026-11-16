# Example 4: Saying what was not checked

**Sources:** `STORY.md`, `AGENTS.md` (non-negotiables) and `docs/DECISIONS.md` entry 0059 in [demo-t-example](https://github.com/beritalasmaki/demo-t-example) (my own portfolio project).
**Use as an example of:** reporting what was done and what was not, without overstating.
**Annotation status:** draft by Claude from reading the sources. Owner to confirm.

## Extract (my words, trimmed)

> **Skipped: user testing.** User testing is normally part of my process. Here, there were no real reviewers to test with, so I made the changes based on my own understanding of the problem instead. What "success" means in each scenario is my own assumption, written down and marked as one. It is not a finding from real people, and I want that to stay visible rather than hidden.

> **No claim without a source.** Every number, status and confidence value on screen must come from data in the model, and must link to the evidence it came from. If a value is unknown, the UI says "unknown": it never guesses or hides it.

> **0059: The final accessibility review is a lighter, time-boxed pass, not the full audit.** This entry records what that covers and what it does not, so nobody reads "reviewed" as "audited".
> *Not checked:* screen readers by hand; zoom to 200% and 400%, reflow and text spacing; browsers other than Chromium; forced colours; non-text contrast, which the automated tool does not measure; states the tool cannot see; a plain-language content review.

## What it decides

- What was skipped is named, with the reason, and an assumption is labelled as an assumption.
- A word like "reviewed" is defined by listing what it does *not* include.
- The same rule applies to the product's screen (unknown is shown as unknown) and to the project's own reporting.

## What it gives up

- A stronger-sounding claim. "Accessibility review: done" is shorter and more impressive than the honest version.

## Why it works as an example

It is the stance behind the pass, fail, cannot-tell rule in this template. It shows that an honest "not checked" list builds more trust than a clean "passed".

## How to use it

Read it when writing a status line, an accessibility report, a case study or any statement about what was checked. Copy the moves: name what was skipped, label assumptions, list what the check cannot show. Do not copy the content of the lists. Each project has its own.
