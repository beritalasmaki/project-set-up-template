# Workflow map

Three diagrams that explain how the package works. GitHub draws them from the text below.

## 1. The whole process

From the public template to a finished case study. The six stages are the same ones in [skills.md](skills.md). Dashed lines show what runs alongside.

```mermaid
flowchart TD
    T["Public template repo<br/>(this repo)"] -->|"Use this template"| W["Private project workspace<br/>one per client project"]
    W --> C["Fill in project.config.md<br/>accessibility level, data classes,<br/>stakeholders, client rules on AI tools"]
    C --> STAGES

    subgraph STAGES["Six stages. The skill drafts, I decide."]
        direction TB
        S1["1. Frame the problem<br/>skill: problem-framing<br/>artefacts: 00, 01"]
        S2["2. Understand the people<br/>skill: stakeholder-map<br/>artefacts: 02, 03"]
        S3["3. Design<br/>skill: user-flow-and-states<br/>artefacts: 04, 07"]
        S4["4. Check<br/>skills: a11y-gate, security-privacy-brief, sameness-check<br/>artefacts: 05, 06"]
        RP["Real people<br/>user testing, testing with assistive technology and users with access needs,<br/>security review, legal advice. AI never stands in for these."]
        S5["5. Hand off<br/>skill: procurement-ready-handoff<br/>artefacts: 08, 09"]
        S6["6. Record and reflect<br/>skill: nda-safe-case-study<br/>artefact: 11"]
        S1 --> S2 --> S3 --> S4 --> RP --> S5 --> S6
    end

    STAGES -.- D["Always: decision log<br/>skill: decision-log, artefact 10<br/>after every meeting or review"]
    STAGES -.- G["Always: guardrails<br/>no claims without evidence, no client data,<br/>no secrets, roles not names"]
```

## 2. What happens in one task

The same loop repeats for every artefact. Claude proposes, the designer decides.

```mermaid
sequenceDiagram
    actor D as Designer
    participant C as Claude
    participant F as Files<br/>(config, artefacts, skills)

    D->>C: Raw material, which skill, which files to read, what I want back
    C->>F: Read project.config.md and only the artefacts the task needs
    Note over C,F: The skill loads when the task matches its description
    C->>D: Draft with evidence and gaps marked, and up to three questions
    D->>C: Corrections and answers
    C->>F: Update the artefact, status draft
    D->>F: Review it, set status reviewed
    D->>C: A meeting decided something
    C->>F: Decision record, decider as a role, reason from the notes or marked as a gap
    D->>C: /clear and start the next task
    Note over D,C: Claude never calls a design accessible, compliant or tested
```

## 3. How the repo keeps its own rules

Why a rule written in a file stays true.

```mermaid
flowchart LR
    E["A change<br/>by me or by Claude"] --> P["git push"]
    P --> A["GitHub Action runs<br/>scripts/validate-template.py"]
    A --> Q{"All checks pass?"}
    Q -->|"Yes"| G["Green mark on the commit"]
    Q -->|"No"| R["Red mark and a message<br/>naming the broken rule"]
    R --> X["Fix the cause,<br/>do not skip the check"]
    X --> E
```

What the check covers: `AGENTS.md` length, skill frontmatter and length, a "do not use for" line in every skill description, no stray README in skill folders, a "Done when" section in every artefact, working links, valid stage names, an up-to-date skill catalogue, and contrast of every token colour pair. Run it yourself with `python3 scripts/validate-template.py`.
