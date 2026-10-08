---
name: draft-scenario-dossier
description: Draft the scenario dossier (3.1, 3.2, 3.3 and the at-a-glance page) from the validated workshop guide. Discovery step 5.
---
# draft-scenario-dossier

Inputs: the validated guide, the intake, architecture inputs in `inputs/`, the family AI-fit statement if one exists.

Steps:
1. Fill the scenario canvas first (five rows, one decision each, with IDs), then "Where we are".
2. 3.1: every section from the guide; reframe the ask in the seller's terms; decision log with the scenario prefix, one ID per decision, status and owner. Decisions only here.
3. 3.2: journey as a Mermaid flowchart (LR, one line per path), key moments (three columns), surface capability check, confirmation and provenance table. Cite decision IDs, do not restate them.
4. 3.3: high-level architecture as a Mermaid flowchart (TB), components, shared layers by ID with "not used and why", data sources, guardrails table with "applied as", open technical questions each ending with the decision it settles.
5. Apply the D3 rule: simplest build form first; an agent needs its own trigger or identity (P2), justified in two lines.
6. Anything the guide does not cover is written as an open question to the section owner, never as a plausible value.
7. Set `doc_status: Draft`, owners from the front-matter; open a PR `scenario: <name> · dossier draft`.
