---
name: generate-extract
description: Generate an extract (BRD, high-level architecture, backlog, certification inputs, steering one-pager) from an approved scenario dossier. Extracts are never edited.
---
# generate-extract

Inputs: an approved `03-scenario-dossier.md`; the extract type.

| Extract | Built from | Output |
|---|---|---|
| BRD | 3.1 and 3.2 | `extracts/brd.md` |
| High-level architecture | 3.3 and its diagram | `extracts/hla.md` |
| Backlog | 3.2 key moments and 3.3 components, one item per row with release | `extracts/backlog.md` |
| Certification inputs | 3.3 guardrails, legal and privacy tables; 3.1 boundary | `extracts/certification.md` |
| Steering one-pager | At-a-glance page and checklist verdict | `extracts/steering.md` |

Rules: copy, do not rewrite; keep every ID; add a header line "Generated from <file> v<version> on <date>; change the dossier, not this file". Build the Word output with `python build/build.py scenarios/<slug>/extracts`.
