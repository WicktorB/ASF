---
name: new-scenario
description: Open a new scenario folder from the four templates and an intake note. Use when a domain need arrives (Discovery step 1).
---
# new-scenario

Inputs: the scenario name, a slug, the intake note or email (pasted or in `scenarios/<slug>/inputs/`).

Steps:
1. Create `scenarios/<slug>/` and copy the four templates from `templates/`, keeping their structure.
2. Fill `01-intake-form.md`: sections A and B verbatim from the note or from the text version produced with the intake assistant (never reformulated); section C as a D1 draft with sources; section D from `docs/portfolio.md` and the other `scenarios/*/03-scenario-dossier.md` (same job, persona, data or surface).
3. Propose a track in E against the light-track criteria in the template; state the reason.
4. Set front-matter: `doc_status: Draft`, `version: 0.1`, today's date. Leave the other three files as templates with the scenario name filled.
5. Open a PR titled `scenario: <name> · intake`.
