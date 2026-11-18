---
name: problem-framing
description: Builds the problem framing in artefacts/01-problem-framing.md from a request, brief or kick-off notes, quoting the request as handed over, restating the problem as a user situation with no solution inside it, separating evidence on hand from evidence missing, listing what is not being solved, and placing hypotheses by risk and value. Use when handed a feature request or a vague brief, at the start of a project, or when asked to frame or reframe a problem before design. Do not use for choosing between design options, for writing requirements (artefacts/03-requirements-spec.md), or for planning user research.
metadata:
  stage: frame
---

# Problem framing

Separates the request from the problem, so design starts from a user situation and not from a solution someone has already chosen.

## Inputs

- The request as handed over: a brief, email, ticket or kick-off notes
- Any evidence the designer has: analytics, support data, observations, conversations
- `project.config.md` and `artefacts/00-product-context.md` if they exist
- The existing `artefacts/01-problem-framing.md`, if any

## Workflow

1. Read the inputs. Do not load other artefacts.
2. **Quote the request as it was handed over**, with who asked (by role) and when, but replace the client's name and any person's name with a placeholder. Never paraphrase it. It stays in the file even when it is reframed.
3. **Write the problem** as a situation a user is in: who is trying to do what, what gets in the way, and what follows from that. Then run the solution check in `references/problem-statement-checks.md`. If a fix is hiding in the statement, rewrite it.
4. **Evidence on hand:** one row per finding, with its source, date and type (`observation`, `data` or `opinion`). An opinion stays an opinion, however senior the person.
5. **Evidence missing:** what is not known, and who could tell. This list should not be empty. If it is, say why.
6. **Not solving:** what is explicitly out of scope, so the requester can object early.
7. **Hypotheses:** "We believe [X] because [evidence]." Place each by risk if wrong and value if right, and say how it could be tested.
8. **Success:** the signals and measures that would show it worked. If there is no baseline, write `baseline needed`. Never invent a number.
9. Ask at most three questions that would most sharpen the problem, then update the file.

## Rules

- Do not invent users, evidence, quotes or numbers. Missing means `gap`.
- Do not quietly replace the requester's request. Show both: the request as handed over, and the problem behind it.
- Do not propose solutions here. If one appears, move it to a hypothesis or to "not solving".
- Use roles, not personal names.

## Output

Update `artefacts/01-problem-framing.md`. Set `Status: draft` until the designer has reviewed it and the requester has seen "not solving".

## Verify before finishing

- [ ] The request is quoted as handed over, with names replaced by placeholders, and says who (by role) and when
- [ ] The problem statement passes the solution check
- [ ] Every finding has a source and a type, and gaps are listed
- [ ] "Not solving" is filled in
- [ ] Hypotheses are placed by risk and value
- [ ] No number or quote was invented
