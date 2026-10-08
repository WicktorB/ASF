---
name: check-design-review
description: Pre-check a scenario dossier against the five dimensions and the catalogues, and fill the checklist with evidence, gaps and blockers. Discovery step 6.
---
# check-design-review

Inputs: `03-scenario-dossier.md`, `catalogues/*.yaml`, `docs/design-canvas.md` ("Before a design review").

Steps:
1. For each of the five dimensions: Met / Partly / Not met, the section of the dossier that is the evidence, the gap and its owner. Quote the dossier, do not paraphrase.
2. Catalogue checks: every GR and SG listed in `check_before_design_review` in `catalogues/gr-sg.yaml`, plus P4 and P5.
3. Readiness: open items with owner and date; decision log complete; CH items raised; certification; licences.
4. Blockers: a numbered list, each tied to a decision ID.
5. Write the verdict in one sentence; set `verdict` and `doc_status: Assessed`; open a PR `scenario: <name> · checklist`.
The design authority gives the final verdict; do not set Approved yourself.
