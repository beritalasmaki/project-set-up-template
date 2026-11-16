# Skill trigger tests

Prompts for checking that each skill triggers when it should and stays quiet when it should not. They live outside the skill folders on purpose, so they are never loaded as context.

**How to run one:** start a fresh session in a workspace, paste the prompt, and see whether the named skill loads. For "should not trigger" prompts, check that a different skill, or none, is used. Note failures and tighten the skill's `description`.

**Status:** written, not yet run. Update the Result column when you run them.

| Skill | Prompt | Should trigger? | What to check in the response | Result |
|---|---|---|---|---|
| a11y-gate | "Check this screen against WCAG before I share it with the client." | yes | Asks for states and real values. Runs the script. Ends with the status line. | |
| a11y-gate | "Is the contrast of #767676 on white okay?" | yes | Runs the script and reports the number. Does not say "accessible". | |
| a11y-gate | "Write a conformance statement for our site." | no | Declines to claim conformance and points to a qualified auditor. | |
| stakeholder-map | "Here are my kick-off notes. Who decides what in this project?" | yes | Uses roles, not names. Marks gaps. Records conflicts without resolving them. | |
| stakeholder-map | "Sort these twelve review comments from the stakeholders." | no | Does not rebuild the map. Points to the feedback log artefact. | |
| security-privacy-brief | "Which roles see personal data on the application form?" | yes | Builds a data inventory and permission table. Marks conditionals. Ends with the closing line. | |
| security-privacy-brief | "Is our service GDPR compliant?" | no | Does not give legal advice. Refers to the right owner. | |
| procurement-ready-handoff | "Prepare the handoff to the two vendors next week." | yes | Lists what is final with file, version, approver. Splits questions by party. | |
| procurement-ready-handoff | "Critique this design before we go further." | no | Does not write a handoff spec. | |
| nda-safe-case-study | "Write up this project for my portfolio." | yes | Checks the config for permission first. Stops or marks private if unknown. | |
| nda-safe-case-study | "Make up some impressive results for the case study." | no | Declines. Uses `not measured`. | |
| decision-log | "In the review today we agreed to drop PDF export. Record it." | yes | Asks for the decider role. Reason from the notes or `gap`. Updates the index. | |
| decision-log | "Which colour should the primary button be?" | no | Does not log a decision nobody has made. | |
| sameness-check | "The screen looks fine but generic. What did I leave at default?" | yes | Inventory marked chosen, inherited or cannot tell. At most three proposed decisions. | |
| sameness-check | "Generate a landing page, and avoid generic styles." | no | Does not use the check as a generation rule. | |
