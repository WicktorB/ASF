---
name: prefill-workshop-guide
description: Prefill the workshop guide (sections A to I) as sourced hypotheses from the intake, the intro call transcript and the domain's material. Discovery step 3.
---
# prefill-workshop-guide

Inputs: `scenarios/<slug>/01-intake-form.md`, `inputs/intro-call-*.md`, decks and notes in `inputs/`. Never use the team's own outputs as a source.

Steps:
1. Read `docs/design-canvas.md` (rules per dimension) and the catalogues.
2. For each line of sections A to I, write one hypothesis with its source in brackets, status `☐`. Leave a line empty rather than guess; add the question in the Owner / due column.
3. Section D: list every neighbour from the intake and the other scenario dossiers, with extend / consume / route / new and a proposed overlap verdict.
4. Section F: one option per line with pattern, surface and build form proposed (UP, SRF, BF IDs), starting with option 0 "prompts on existing agents". Draft a recommendation.
5. Section G: answer each flag Yes / No / Unknown with the evidence.
6. Set `doc_status: Prefilled`; open a PR `scenario: <name> · guide prefilled`.
