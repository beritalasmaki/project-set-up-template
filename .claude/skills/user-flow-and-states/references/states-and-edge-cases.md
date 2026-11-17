# States and edge cases

Prompts for the screens-against-states table and the edge-case sweep. Ask each as a question about the screen. Mark the answer, and do not skip a state because it is awkward.

## States (the columns of the table)

| State | Ask |
|---|---|
| Empty | What does the user see when there is nothing yet? What can they do next? |
| Loading | What shows while data loads? What if it takes longer than expected? |
| Partial data | What if only some of the data arrives, or some fields are missing? |
| Error | What does the user see when it fails, in words, and what can they do about it? |
| No permission | What does a user without the right role see? Do they learn why? |
| Success | How does the user know it worked, and what happens next? |
| Long or extreme content | Very long names, many items, very large numbers, long translations? |
| First use | What does a new user see before they have any history? |

## Edge cases (the sweep)

- Session times out in the middle of the task. What happens to unsaved input?
- The user presses back, refreshes, or opens the page in a second tab.
- The user submits twice, or double-clicks the main button.
- Something changes elsewhere while the user is working (another user, another system).
- The connection is slow or drops.
- Required information is not available yet, and the user needs to come back later.
- The user's role changes, or access is removed, mid-task.
- Special characters, very long text, or text in another language.
- The user leaves and returns days later. Is progress kept?
- A task is started on one device and continued on another.
- The user uses only a keyboard, or a screen reader, at this step. (Check this in `a11y-gate`.)

## Marking rules

- Every cell is `designed`, `missing` or `not needed`.
- Start every cell as `missing`. Only the designer can mark `designed`.
- `not needed` must have a reason, for example "this screen shows no user data".
- Order the `missing` cells by what blocks the build first: states that change what must be built (no permission, error, partial data) before states that only change the look (long content).
