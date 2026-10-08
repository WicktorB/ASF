---
title: Templates
part: Design process
version: v0.5
status: Proposed
owner: Framework owner
---

# Templates

One scenario, one scenario dossier. The intake form, the workshop guide and the checklist are filed with it. Each template part carries the design dimension it answers.

## Where the templates live

| What | Source | What people receive |
|---|---|---|
| Templates and pack pages | This repository, `templates/` and `docs/`, Markdown | Word and HTML in `dist/`, published to the SharePoint library |
| Catalogues | `catalogues/*.yaml`, one item per ID | Catalogue pages in the pack; read directly by the skills |
| Scenario dossiers | `scenarios/<slug>/`, one folder per scenario | Word per template; extracts at Go build |

A change goes into the source and is reviewed in a pull request; the outputs are rebuilt. Nobody edits a Word file: the Word file is a view.

## The four templates

| # | Template | Filled at | Owner | Holds |
|---|---|---|---|---|
| 1 | Intake form | Discovery step 1 | Domain, checked by the product team | The need, a first reading of D1, the neighbours in the portfolio, the track proposed |
| 2 | Workshop guide | Steps 2 to 4 | Product team, validated with the domain | The working record: sourced hypotheses, statuses, decisions with the domain, the overlap check |
| 3 | Scenario dossier | Step 5 | PO, UX, architecture lead, one section each | The reference: at a glance, decisions and why (3.1), how the seller uses it (3.2), what it is built on (3.3) |
| 4 | Checklist | Step 6 | Product team; reviewed by the design authority | Design review and handover |

Rule: decisions live in 3.1 and are cited by ID in 3.2 and 3.3, never restated.

## What changed in the rework of 8 October (CH-10)

- Every template opens with an "In 30 seconds" box: purpose, who fills it, when, what comes out.
- The scenario dossier gains a one-page "At a glance": summary, the scenario canvas (five dimensions with IDs), and "Where we are" (track, next gate, blockers, CH items raised). A steering reader stops there; the build team reads on.
- Tables have at most four columns; the ownership matrix and long lists are split or moved to the catalogues.
- Grey "guide" boxes explain how to fill each section; `build.py --final` drops them for the reader version.
- Front-matter carries status, track, owners, version and date; the Word cover is generated from it.
- Diagrams (journey, high-level architecture) are Mermaid in the source, rendered to images in Word, editable as text by the skills.
- The overlap check sits in the workshop guide (section D), the intake keeps a first look at the neighbours (CH-09).

## How the templates are produced

Each template is filled by a Copilot skill that follows `docs/design-canvas.md`, reads the catalogues and drafts from the domain's own material; the named owner validates in the pull request. AI proposes, the owner decides: P6 applies to our documents as it does to agents.

| Skill | What it does | Reads | Validated by |
|---|---|---|---|
| Intake assistant (agent, not a repo skill) | Helps the domain state the need for sections A and B: reads what the domain shares, asks for what is missing, challenges, keeps the guardrails; text version validated in the conversation. MVP decided 8 Oct, no document generation | Intake sections A and B, canvas D1 questions | The domain |
| `new-scenario` | Opens the scenario folder; pastes A and B; fills C to E (D1 draft, neighbours, track) | Canvas D1, JM, portfolio | Product team |
| `prefill-workshop-guide` | Prefills A to I as sourced hypotheses; proposes IDs; lists neighbours | Canvas D1 to D5, all catalogues, intake, intro call transcript, decks | The domain, in the workshop |
| `update-workshop-guide` | Sets statuses, logs decisions and open items from the transcript | Canvas writing rules | Product team, within 48 hours |
| `draft-scenario-dossier` | Drafts the at-a-glance page, 3.1, 3.2 and 3.3 from the validated guide; draws the diagrams | Canvas, all catalogues, principles | PO, UX, architecture lead |
| `check-design-review` | Pre-checks the five dimensions and the catalogue rules; fills the checklist | Canvas "Before a design review", GR/SG | Design authority |
| `generate-extract` | BRD, high-level architecture, backlog, certification inputs, steering one-pager | Approved dossier | Owner of each audience |
| `apply-change` | Applies a validated CH to every file that cites the affected IDs | `catalogues/changes.yaml` | Design authority |

Status: skills Planned; the repository, templates, catalogues and build are in place. Until the skills run, each scenario carries the full writing effort; the light track keeps it proportionate.

## Plan of each template

Intake form: stated by the domain — A who asks · B the need in the domain's words; ASF product team analysis — C first reading, D1 draft · D neighbours in the portfolio · E outcome (track, next step).

Workshop guide: Before the workshop · A need and value (D1) · B current work and frictions (D1) · C boundary (D5) · D scope and overlap check (D1, D3) · E content and data (D4) · F what AI could do (D2, D3) · G complexity flags (D4, D5) · H success (D1) · I wrap-up.

Scenario dossier: At a glance (summary, scenario canvas, where we are) · 3.1 Scenario brief: ask and positioning, job and persona, friction and benefit, pattern and surface, AI fit and build form, boundary, success, phasing, decision log · 3.2 Functional overview: journey, key moments, where it appears, UI principle, confirmation and provenance, information shown, scope by release, example prompts, mockup · 3.3 Solution blueprint: architecture, components, AI / deterministic split, shared layers, data sources, triggers, guardrails, certification inputs, open technical questions.

Checklist: verdict · the five dimensions · catalogue checks · readiness · blockers · handover at Go build.

## Extracts

Formats generated from the scenario dossier for a given audience. An extract is never edited: changes go into the dossier, then the extract is generated again. Planned.

| Extract | For | Built from | When |
|---|---|---|---|
| BRD | Teams that still require a BRD | 3.1 and 3.2 | Go build |
| High-level architecture and diagram | Architecture review, IT | 3.3 | Architecture decision |
| Backlog | PO, brick team | 3.2 journey steps and 3.3 components | Handover to the PO |
| Certification inputs | GRCC, AI risk assessment | 3.3 D5 content, 3.1 boundary | Phase 2 |
| Steering one-pager | WPR, SteerCo | At a glance and checklist verdict | Roadmap, Go build |
