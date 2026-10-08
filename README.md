# ASF Design Framework · source repository

The single source of truth for the Augmented Salesforce (ASF) design framework: the design canvas, the Discovery process, the four templates, the catalogues and the scenario dossiers.

Word, HTML and PDF versions are **generated** from this repository. Nobody edits a generated file: a change goes into the Markdown or YAML source, is reviewed in a pull request, and the outputs are rebuilt. This is the same rule the framework applies to agents (P6: AI proposes, the owner confirms) and to extracts (never edited directly).

## What is where

| Folder | Holds | Edited by | Format |
|---|---|---|---|
| `docs/` | The pack, one page per file: design canvas, design process, templates, ways of working | Framework owner, via PR | Markdown |
| `catalogues/` | JM, UP, SRF, BF, LY/SC, GR/SG catalogues and the change log (CH) | Design authority, via PR | YAML, one item per ID |
| `templates/` | The four templates: intake form, workshop guide, scenario dossier, checklist | Framework owner, via PR | Markdown with front-matter |
| `scenarios/<scenario>/` | One folder per scenario: the filled templates (the scenario dossier and what is filed with it) | PO, framing lead, UX, architecture lead | Markdown with front-matter |
| `build/` | The Word reference styles and the build script | Technical design | Python, .docx |
| `.github/` | Copilot instructions, skills and prompts; the build workflow | Technical design | Markdown, YAML |
| `dist/` | Generated outputs (.docx, .html). Never edited, not reviewed | The build | Generated |

## Working on a scenario

1. Copy the four templates into `scenarios/<scenario-slug>/`, or ask Copilot: *"Open the One Plan End User scenario from the intake note attached"* (skill `new-scenario`).
2. Fill the templates in order: intake → workshop guide → scenario dossier → checklist. Each file's front-matter carries the status and the owner of each section.
3. Ask Copilot to prefill, draft or check (skills `prefill-workshop-guide`, `draft-scenario-dossier`, `check-design-review`). The skills read `docs/design-canvas.md` and the catalogues; you validate.
4. Open a pull request. The design authority reviews what changes; the build attaches the generated Word files to the PR.
5. At Go build, generate the extracts (skill `generate-extract`: BRD, high-level architecture, backlog, certification inputs, steering one-pager). An extract is never edited: change the dossier and generate again.

## Building the Word and HTML outputs

```bash
pip install python-docx pyyaml
python build/build.py                 # everything into dist/
python build/build.py scenarios/one-plan-segment   # one scenario
```

Requirements: `pandoc` 3.x on the path; `mmdc` (mermaid-cli) if diagrams must be rendered into Word, otherwise the diagram source is kept as a code block. The GitHub Action in `.github/workflows/build-docs.yml` runs the same script on every pull request and publishes `dist/` as an artifact; a scheduled job can copy it to the SharePoint library.

## Conventions

- One ID, one line: catalogue items (`JM-06`, `UP-08`, `SRF-11`, `BF-04`, `LY-02`, `SC-01`, `GR-01`, `SG-01`), principles (`P1`–`P11`), dimensions (`D1`–`D5`), changes (`CH-nn`) and scenario decisions (`<PREFIX>-nn`) are cited by ID and never restated.
- Decisions live in section 3.1 of the scenario dossier; 3.2 and 3.3 cite them.
- IDs are never renumbered; a retired ID is not reused.
- Status words are the framework's: Validated, Proposed, Open, To confirm, Planned; for checks: Met, Partly, Not met.
- Language: English for the pack and the dossiers.

## Versions

The pack version is the Git tag (`v0.5`, `v0.6`…). The change log is `catalogues/changes.yaml`; a release applies the validated CH items to every page, template and catalogue that cites them (skill `apply-change`).
