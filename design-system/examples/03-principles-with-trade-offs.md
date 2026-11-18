# Example 3: Principles with trade-offs

**Source:** the Principles page of [design-system-use-case](https://github.com/beritalasmaki/berit-portfolio/tree/main/design-system-use-case) in my portfolio repo.
**Use as an example of:** principles that tell designers and developers what to do, with a concrete case.
**Annotation status:** draft by Claude from reading the source. Owner to confirm, especially the "gives up" lines, which are my reading.

## Extract (my words, two of the five principles, trimmed)

> **Lean system: Keep it small.** A small set of well-explained parts is easier to use than a large set of similar ones. Each new colour, token or component has to be really needed before it is added, because every addition has to be learned, documented and maintained.
> *Design:* before adding something new, check whether an existing part already does the job. *Code:* build with what exists; when something is missing, add it to the system with its documentation instead of solving it once inside a single screen.
> *Example:* the palette was reduced to two oranges and three dark greys, and the gradients to four, after it became unclear which shade to use where.

> **Semantic tokens: Colours are named by their job.** A colour is chosen by what it is used for, such as text or primary button, and not by how it looks.
> *Example:* dark mode works by pointing the same named roles at different values, so no component carries its own dark colours.

## What it decides

- Each principle has a **design** side and a **code** side, so it governs both disciplines.
- Each principle has a concrete **example** from the real system, so it can be checked.
- Principles are about choices (what to add, how to name), not about taste.

## What it gives up

- Lean system gave up palette variety: shades were removed, so some expressive range is gone.
- Semantic naming gave up the convenience of reaching for "the orange". It adds a layer of names to learn.

## Why it works as an example

A principle that cannot be checked against a real case is decoration. These can. A model reading this learns that a principle needs an owner on each side and an example, and that applying it costs something.

## How to use it

Read it when writing or applying design principles. Add what each principle *gives up*, as `artefacts/00-product-context.md` asks. Do not reuse these five principles for another product. Write principles from that product's own constraints.
