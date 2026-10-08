---
name: update-workshop-guide
description: After the workshop, set each line's status, log decisions and open items from the session transcript. Discovery step 4, within 48 hours.
---
# update-workshop-guide

Inputs: the prefilled guide and `inputs/workshop-<date>.md` (transcript or notes).

Steps:
1. For each line: `✔` confirmed, `✎` corrected (rewrite the hypothesis, keep the source and add "(workshop)"), `?` open with owner and due, `☐` untouched.
2. Section I: one row per decision with who agreed and the date; one row per open item with owner and due; fill the gate inputs (overlap verdict, recommendation, track).
3. Do not add content the domain did not say. Quote the domain's words where the wording matters (boundary, never list).
4. Set `doc_status: Validated with the domain`, bump the version; open a PR `scenario: <name> · guide validated`.
