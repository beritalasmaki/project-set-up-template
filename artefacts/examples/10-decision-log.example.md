# 10 Decision log (fictional example)

> **Fictional.** An invented example. Do not copy its content into a real project.

**Status:** draft · **Last updated:** 2026-03-18 · **Owner (role):** Lead designer

## Index

| ID | Title | Status | Date | Decider |
|---|---|---|---|---|
| D-001 | Application form becomes a step-by-step flow | accepted | 2026-03-16 | Service owner |
| D-002 | Contractor access model deferred to second release | accepted | 2026-03-18 | Service owner |

### D-001: Application form becomes a step-by-step flow

- **Date:** 2026-03-16
- **Status:** accepted
- **Decided by (role):** Service owner
- **Context:** The current form is one long page. Reviewers disagreed on whether to keep it or split it.
- **Options considered:** Single page with sections. Step-by-step flow with a summary at the end.
- **Decision:** Step-by-step flow with save on every step.
- **Why:** The save requirement (FR-02) is simpler to meet per step. Evidence on abandonment: gap, no data yet.
- **Gives up:** Faster completion for contractors who know the form.
- **Consequences:** A summary screen is needed. Contractor shortcuts are revisited in D-002.
- **Revisit if:** Contractor feedback shows the flow is too slow.
- **Related:** FR-02, FR-03

### D-002: Contractor access model deferred to second release

- **Date:** 2026-03-18
- **Status:** accepted
- **Decided by (role):** Service owner
- **Context:** How contractors get access to client applications is not decided (SR-02), and the security owner has not answered.
- **Options considered:** Build a provisional model now. Defer until the security owner decides.
- **Decision:** Defer. The first release serves home owners only.
- **Why:** A provisional model risks a security rework (evidence: security owner, open question of 12 Mar).
- **Gives up:** Contractors cannot use the portal at launch.
- **Consequences:** FR-03 moves to the second release.
- **Revisit if:** The security owner answers before build starts.
- **Related:** SR-02, FR-03

## Done when

- [x] Every entry has a decider role, a reason and a revisit trigger
- [x] The reason is evidence or an honest `gap`, never invented
- [x] The index is up to date
- [x] Superseded decisions point to what replaced them
