# Design-stage checks

What can and cannot be judged from a design file, by criterion. Criteria are from WCAG 2.2. Read each one on the W3C site for the exact wording: https://www.w3.org/WAI/WCAG22/Understanding/

## Seeing and reading

| Criterion | Judge from design? | Ask or check |
|---|---|---|
| 1.1.1 Non-text Content | Partly | Which images carry meaning and need a text alternative? Which are decorative? The actual text comes in the build. |
| 1.3.1 Info and Relationships | Partly | Are headings, lists, tables and form groups clear from the layout? Real structure is checked in code. |
| 1.4.1 Use of Color | Yes | Is colour the only way to show an error, selection or state? If yes, fail. |
| 1.4.3 Contrast (Minimum) | Yes, with values | Run the script on each text and background pair, including states. |
| 1.4.4 Resize Text | No | Needs a browser. List it under "cannot show". |
| 1.4.10 Reflow | Partly | Is there a narrow layout? Does it avoid two-way scrolling? Confirm in a browser. |
| 1.4.11 Non-text Contrast | Yes, with values | Borders of inputs, icons that carry meaning, focus indicators. Run the script with `--kind non-text`. |
| 1.4.12 Text Spacing | No | Needs a browser. |

## Pointing and moving

| Criterion | Judge from design? | Ask or check |
|---|---|---|
| 2.4.3 Focus Order | Partly | Ask the designer to number the intended order. Check it against reading order and meaning. |
| 2.4.7 Focus Visible | Yes | Is a focus style drawn for every interactive element and state? Where is it not drawn? |
| 2.4.11 Focus Not Obscured (Minimum) | Partly | Sticky headers, banners and cookie bars can cover a focused element. Where are they? |
| 2.5.7 Dragging Movements | Yes | Does anything need dragging? Is there a single-pointer alternative? |
| 2.5.8 Target Size (Minimum) | Yes, with sizes | Run `--target WxH`. A FAIL needs a human to check the criterion's exceptions. |

## Understanding and input

| Criterion | Judge from design? | Ask or check |
|---|---|---|
| 2.4.6 Headings and Labels | Yes | Do headings and labels describe their topic or purpose? |
| 3.2.6 Consistent Help | Yes | If help is offered on several pages, is it in the same place? |
| 3.3.1 Error Identification | Yes | Is the error identified in text, and the field named? Colour alone fails twice (also 1.4.1). |
| 3.3.2 Labels or Instructions | Yes | Does every input have a visible label or instruction? |
| 3.3.3 Error Suggestion | Yes | Does the message say how to fix it, where that is known? |
| 3.3.7 Redundant Entry | Yes | Does the flow ask for information the user already gave? |
| 3.3.8 Accessible Authentication (Minimum) | Yes | Does sign-in require remembering, transcribing or solving something, with no alternative? |

## What a design file cannot show

Always list these, whatever the table says:

- Screen reader output
- Real focus behaviour and keyboard operation in the built page
- Zoom to 200% and 400%, reflow, text spacing in a browser
- Timing and animation behaviour
- Forced colours and other user settings
- How users with access needs get through the task
