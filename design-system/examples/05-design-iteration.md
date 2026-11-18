# Example 5: An iteration with a reason

**Source:** `design/README.md` and the design images (`early-design-v1.png`, `iteration2-design-v3.png`) in [demo-t-example](https://github.com/beritalasmaki/demo-t-example) (my own portfolio project, all data fictional). The images are not copied here. Open them at the source.
**Use as an example of:** explaining a design change as a problem and a fix, and showing the cost.
**Annotation status:** draft by Claude from reading the text and viewing both images. Owner to confirm.

## Extract (my words, trimmed)

> I sketched the first version by hand to quickly map out all the necessary pieces. However, it lacked visual hierarchy: it had six equally sized cards, the main decision was buried down the page, and the audit log was just a heavy wall of text.

Under the later design, a three-part note in my own words:

> **What this page is for.** … **What is different.** In the first design, every part of the page looked equally important, and the buttons were at the very bottom. Here the most important things come first: what the change is, and what is still open. … **Why it helps.** *Risks sit next to the buttons. One clear path. Fewer mistakes. A clear record.* **The cost.** The page is long. A reviewer in a hurry can still skip the middle part.

## What changed (from the images)

- **Before:** a single column of equal-weight sections (summary, policy gates, audit log, confidence, decision). The decision came last.
- **After:** three columns. Facts on the left, a story of what happened in the middle, and on the right the open items and the decision. The only dark button is the one that approves, and each other action says what it will do.

## What it decides

- The change is explained as a problem in the first version (equal weight, buried decision) and a response in the next.
- A short note under the design says what the page is for, what is different, why it helps, **and what it costs**.
- Open items appear next to the decision, so risk and action meet at the same moment.

## What it gives up

- Length: the story view is longer than the first design, and says so.

## Why it works as an example

It is a clear "this, not that" pair with a stated reason and an honest cost. A model that reads it learns how to explain a design change, not only how to produce one.

## How to use it

Read it when explaining or critiquing a change between two versions. Copy the moves: name the problem in the old version, state what is different, say what it helps with and what it costs. Do not copy the layout. A three-column story page suits this decision. It will not suit every product.
