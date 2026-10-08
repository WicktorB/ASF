# Copilot instructions · ASF Design Framework repository

You work on the source of the Augmented Salesforce design framework: the pack (`docs/`), the catalogues (`catalogues/*.yaml`), the four templates (`templates/`) and the scenario dossiers (`scenarios/<slug>/`). Word and HTML outputs in `dist/` are generated; never edit them.

## Rules that apply to every change

1. Read `docs/design-canvas.md` first: it holds the five dimensions D1 to D5, the rules a skill applies, the "before a design review" list and the writing rules. Apply them.
2. Cite catalogue items by ID (`JM-06`, `UP-08`, `SRF-11`, `BF-04`, `LY-02`, `SC-03`, `GR-01`, `SG-01`, `P1`–`P11`). Never restate a catalogue definition; never invent an ID. If nothing fits, propose a change in `catalogues/changes.yaml` (next `CH-nn`, status Proposed) and say so.
3. Decisions live in section 3.1 of a scenario dossier and are cited by ID in 3.2 and 3.3.
4. Every value you draft carries its source in brackets: (intake), (intro call, 29 Sep), (workshop), (deck: name). A value with no source is written as a question to the owner, not as a fact.
5. Keep the templates' structure: same headings, same order, same front-matter keys. Tables have at most four columns; three to five points per section.
6. Status words: Validated, Proposed, Open, To confirm, Planned. Check statuses: Met, Partly, Not met.
7. Update the front-matter (`doc_status`, `version`, `date`) of every file you change. Bump the minor version for content changes.
8. Never renumber or reuse an ID. Never delete a decision from a decision log: change its status.
9. You propose; the named owner validates (P6). Open a pull request and list in its description what you changed, what you could not source, and which CH items you raised.
10. Language: English. Tone: short, factual, no superlatives.
11. When you create a branch for scenario work, name it `<scenario>-<update>-<version>`: the scenario slug, the file changed (`intake`, `guide`, `dossier`, `checklist` or `extract`), the version written in its front-matter, for example `one-plan-segment-dossier-v0.2`. Other branches: `docs/<page>`, `catalogue/<id>`.

## Where things are

- Templates: `templates/01-intake-form.md`, `02-workshop-guide.md`, `03-scenario-dossier.md`, `04-checklist.md`.
- A scenario: `scenarios/<slug>/` with the same four files plus `inputs/` (transcripts, decks, notes) and `mockup/`.
- Skills: `.github/skills/<name>/SKILL.md`. Prompts: `.github/prompts/*.prompt.md`.
- Build: `python build/build.py <path>`; outputs in `dist/`.
