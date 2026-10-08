---
title: "Set-up plan · repository, Word generation and Copilot skills"
part: Deployment
version: 0.1
doc_status: Proposed
owner: "Stream 5 · AI skills and tooling (Victor, interim)"
date: 2026-10-08
horizon: 15 December 2026
---

::: {.readme}
**In 30 seconds.** Six weeks to move the framework's documentation from hand-written files to a GitHub repository that Copilot skills maintain and that publishes Word to SharePoint. Four phases: enable (week 42), seed and pilot on One Plan Segment (weeks 43-44), open to the POs with one new scenario (weeks 45-47), hand over and release v1.0 (weeks 48-51). Three decisions block the start: repo owner, PO access mode, ISD in the same repo or not.
:::

# Target state on 15 December

| Item | Today | On 15 December |
|---|---|---|
| Source of the pack, templates, catalogues | HTML pack and Claude Docs, edited by hand | One GitHub repository, Markdown and YAML, reviewed by pull request |
| What POs and steering receive | HTML pack, Word drafted by hand | Word and HTML generated on every merge, published to the SharePoint library |
| Who fills the templates | Product team, by hand | Copilot skills draft; the named owner validates the PR |
| Scenario dossiers | One, in Claude Docs | Two or more in the repository (One Plan Segment migrated; one new scenario run end to end) |
| Catalogues | Pages in the pack | YAML read by the skills; pages generated from it |
| Change log | Table in the pack | `catalogues/changes.yaml`; `apply-change` applies validated items |
| Ownership | Framing lead | Technical design owns the repo and the build; design authority owns `docs/` and `catalogues/` |

# Prerequisites · to confirm in week 42

| Prerequisite | Who confirms | Fallback if not available |
|---|---|---|
| GitHub Enterprise organisation of Schneider: a private repository can be created under the ASF programme | Victor, with IT | A repository in a team-owned GitHub Enterprise Cloud org; last resort: Azure DevOps Repos with the same structure, without the coding agent |
| Copilot Business or Enterprise licences for the product team (5) and the POs (number to size) | Victor, Fernanda | Product team only in phase 1; POs through issues reviewed by the product team |
| Copilot coding agent enabled on the organisation (policy "Copilot coding agent") | Victor, with the GitHub admin | Agent mode in VS Code run by the product team on behalf of the POs |
| GitHub Actions allowed on the repository, with `pandoc` and Node installable on the runner | Victor | Build run locally by technical design and committed to `dist/` |
| SharePoint library "ASF Design Framework" and a way to write into it (Graph API app registration, or a Power Automate flow triggered by the release) | Victor, with the M365 admin | Manual upload of the generated Word at each release |
| PO access: GitHub accounts for every PO, read-write on `scenarios/` | Fernanda | Issues only; the product team commits |

# Phases

## Phase 1 · Enable · week 42 (12-16 October)

| Task | Owner | Done when |
|---|---|---|
| Create the repository `asf-design-framework` in the Schneider org; push the skeleton (this content) | Technical design | Repo exists; `main` protected; CI green on the first push |
| Set `CODEOWNERS`: `docs/` and `catalogues/` → design authority; `scenarios/<slug>/` → the PO of the scenario; `build/` and `.github/` → technical design | Technical design | A PR on `catalogues/` cannot merge without a design authority review |
| Enable Copilot on the repo; verify `copilot-instructions.md` is picked up (ask Copilot Chat "which rules apply to this repo") | Technical design | Copilot quotes the rules |
| Run the build locally and in CI; attach `dist/` to a test PR | Technical design | Word files open in Word 365 with styles and diagrams |
| Replace the palette and font in `build/make_reference.py` with the Schneider brand values | Technical design, with UX | Reference document validated by UX |
| Decide the three open points (owner, PO mode, ISD) at the task force | Fernanda, Victor | Decisions logged in `catalogues/changes.yaml` as CH-11 |

## Phase 2 · Seed and pilot · weeks 43-44 (19-30 October)

| Task | Owner | Done when |
|---|---|---|
| Migrate the remaining pack pages from HTML to `docs/` (Start here, Why, Design process, Portfolio views, Ways of working, Deployment, Glossary); catalogue pages generated from YAML | Framework owner, with technical design | The HTML pack is retired; `docs/` is the reference |
| Generate the catalogue pages from the YAML (small script in `build/`) so the YAML is the single source | Technical design | A change in `srf.yaml` appears in the catalogue page after rebuild |
| Pilot the skills on One Plan Segment as a retro: run `check-design-review` on the migrated dossier; compare with the hand-made checklist | Technical design, PO | Differences listed; skill or canvas adjusted |
| Pilot `prefill-workshop-guide` on a past scenario with its transcripts (post-meeting or competitor intelligence) | Framing lead | Prefill judged usable by the framing lead; sources present on every line |
| Write the two-page "How to work in the repo" for POs: open an issue, read a PR, approve, where the Word files are | Documentation and training stream | Reviewed by one PO |
| Set up the SharePoint publication (Graph or Power Automate) from the release workflow | Technical design, M365 admin | A merge on `main` updates the library within the hour |

## Phase 3 · Open to the POs · weeks 45-47 (2-20 November)

| Task | Owner | Done when |
|---|---|---|
| PO session: the repo, the PR review, the issue templates; hands-on on One Plan Segment | Documentation and training stream | Every PO has opened one issue and approved one PR |
| Run one new scenario end to end in the repo: intake (with the intake assistant), prefill, workshop, dossier, checklist | Framing lead, the PO of the scenario | Dossier reaches the design review with every file in the repo |
| Issue templates for the coding agent: "new scenario", "prefill guide", "update guide", "draft dossier", "check dossier" | Technical design | An issue created from a template produces a PR without manual prompting |
| Measure: time from transcript to prefilled guide; time from validated guide to dossier draft; review comments per PR | Technical design | Baseline recorded for the retro |
| ISD: share the repo structure and the extracts (`generate-extract`); agree whether ISD scenarios live in the same repo | Victor, ISD counterpart | Decision recorded; first ISD scenario folder created if yes |

## Phase 4 · Hand over and release · weeks 48-51 (23 November - 15 December)

| Task | Owner | Done when |
|---|---|---|
| Apply the validated CH items with `apply-change`; release the pack as v1.0 (Git tag, Word and HTML published) | Design authority, technical design | v1.0 tag; SharePoint library updated |
| Retro of the two pilots; adjust skills and templates; log changes as CH | Framework owner | CH items proposed, reviewed at the design authority session |
| Ownership confirmed: repo and build (technical design), `docs/` and `catalogues/` (design authority), each scenario (its PO) | Fernanda | Written in Ways of working |
| Portfolio view generated weekly from the dossiers (`weekly-portfolio-view` prompt) | Product team | First generated view reviewed |
| Training material frozen: the two-pager, a 20-minute recording of the PO session | Documentation and training stream | Available in the SharePoint library |

# Timeline

| Week | Dates | Milestone |
|---|---|---|
| 42 | 12-16 Oct | Repo live, CI green, three decisions taken |
| 43 | 19-23 Oct | Pack pages migrated; catalogue pages generated |
| 44 | 26-30 Oct | Skills piloted on One Plan Segment and one past scenario; SharePoint publication working |
| 45 | 2-6 Nov | PO session; issue templates live |
| 46-47 | 9-20 Nov | New scenario run end to end; ISD decision |
| 48-49 | 23 Nov - 4 Dec | Retro; CH applied |
| 50-51 | 7-15 Dec | v1.0 released; ownership confirmed |

# Working rules from day one

- `main` is protected: no direct push; one review from the code owner; CI must pass.
- One branch per scenario and step (`scenario/<slug>/<step>`); one PR per step; the PR description lists what was drafted, what could not be sourced, which CH were raised.
- Inputs (transcripts, decks, notes) go to `scenarios/<slug>/inputs/` before any skill runs; a skill never works from the team's own outputs.
- `dist/` is never committed by hand; it is built by CI.
- Conversations with Copilot are not archived; the PR is the record.
- Personal data in transcripts: keep transcripts in the repo only if the repository is private and access-controlled; otherwise store them in the SharePoint library and reference them. To confirm with legal in week 42.

# Risks

| Risk | Signal | Mitigation |
|---|---|---|
| Coding agent not enabled on the org by week 43 | No answer from the GitHub admin | Phase 2 runs in agent mode in VS Code by the product team; POs work through issues anyway |
| POs do not open issues or review PRs | No PO activity in week 45 | The framing lead opens issues for them; review done in the PO session; revisit the access mode at the retro |
| Skills produce unsourced content | Lines without a source in a prefill | Rule in `copilot-instructions.md`; the reviewer rejects the PR; the skill is adjusted |
| Transcripts hold personal or confidential content | Legal objection | Transcripts outside the repo, referenced by link; anonymised extracts only |
| Two sources of truth during migration | HTML pack and `docs/` edited in parallel | Freeze the HTML pack at the start of week 43; every change goes to `docs/` |
| ISD keeps its own format | Extracts not reused | Agree the extract formats with ISD in week 46; the dossier remains the source |

# Decisions needed at the task force of week 42

1. Owner of the repository and the build: technical design (proposed).
2. PO access mode for phase 3: issues and PR review only, no IDE (proposed).
3. ISD scenarios in the same repository (proposed) or a mirror.
4. Transcripts in the repository or in SharePoint only (legal input needed).
