# 02 Stakeholder map (fictional example)

> **Fictional.** An invented example. Do not copy its content into a real project.

**Status:** reviewed · **Last updated:** 2026-03-09 · **Owner (role):** Lead designer

## Stakeholders

| Role | Interest | Needs to see | Influence | Decides? | Source |
|---|---|---|---|---|---|
| Service owner | Fewer returned applications, on time launch | Progress against the launch date | high | yes (scope, release) | evidence: kick-off |
| Case officer lead | Complete applications that are easy to review | Officer view and what is asked of applicants | high | shares | evidence: kick-off |
| Security owner | No personal data leaks, clear roles | Roles and permissions, data shown per screen | high | yes (security) | evidence: conversation 2 Mar |
| Accessibility specialist | Meeting the accessibility duty | Checklist results, test plan | med | shares | gap: not yet met |
| Engineering lead (vendor) | Clear, buildable handoff | Final designs, states, behaviour | high | yes (technical feasibility) | evidence: kick-off |
| Legal advisor | Correct wording of legal texts | Draft copy of legal steps | med | yes (legal wording) | gap: not yet met |

## Decision rights

| Decision area | Decider | Consulted | Informed |
|---|---|---|---|
| Scope | Service owner | Case officer lead, engineering lead | All |
| Design direction | Service owner | Case officer lead, accessibility specialist | Engineering lead |
| Accessibility trade-offs | Service owner | Accessibility specialist | Engineering lead |
| Security and data handling | Security owner | Engineering lead | Service owner |
| Release | Service owner | Security owner, engineering lead | All |

## Tensions and conflicts

| Topic | Raised | Service owner wants | Case officer lead wants | Who decides | Source |
|---|---|---|---|---|---|
| Number of questions on the first screen | At kick-off | Short, to reduce drop-off | All needed details early, to avoid returns | Service owner | evidence: kick-off, 2 Mar |

## Communication rhythm

| Audience | Format | How often | Owner |
|---|---|---|---|
| Service owner and case officer lead | Review of current designs | Every two weeks | Lead designer |
| Engineering lead | Handoff walkthrough | Before each build phase | Lead designer |

## Risks

- The accessibility specialist and legal advisor have not been met yet, so their needs may change scope.

## Done when

- [x] Every stakeholder has a role, an interest and a "decides?" value
- [x] Decision rights exist for scope, accessibility, security and release
- [x] Conflicts raised so far are side by side, each with a named decider
- [x] Gaps (stakeholders not yet met) are listed
