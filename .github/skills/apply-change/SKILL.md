---
name: apply-change
description: Apply a validated change (CH-nn) to every page, template, catalogue and dossier that cites the affected IDs. Used when the design authority validates a change.
---
# apply-change

Inputs: the CH id in `catalogues/changes.yaml` with status Validated.

Steps:
1. List every file that cites an affected ID (`grep -rn "<ID>" docs templates catalogues scenarios`).
2. Apply the change to the catalogue item first, then to the pages and templates, then flag scenario dossiers: add a line "Affected by CH-nn, owner to review" under their "Where we are" table rather than changing their content.
3. Never renumber IDs; a retired item keeps its ID with `status: Retired`.
4. Add the CH id to the version notes in the PR; bump the pack version only when the design authority releases.
