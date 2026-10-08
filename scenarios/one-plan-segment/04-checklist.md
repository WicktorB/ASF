---
template: 4 · Design review and handover checklist
title: "Checklist · One Plan Segment"
scenario: one-plan-segment
doc_status: Assessed
verdict: Not ready
assessed_by: Product team, 6 Oct 2026
reviewed_by: Design authority, date to set
discovery_step: 6 · Playback
dimensions: [D1, D2, D3, D4, D5]
version: 1.1
date: 2026-10-08
---

::: {.readme}
**In 30 seconds.** Not ready for the design review: one check met on the five dimensions, four partly met; certification and handover not met. Six blockers below. The write path (SEG-14) blocks release 2, not this review.
:::

## Verdict

Not ready for the design review. Assessed on 6 Oct 2026 by the product team; the design authority reviews once the blockers below have an answer or a date.

## The five dimensions

| Check | Status | Evidence | Gap and owner |
|---|---|---|---|
| D1 · Job in one sentence, activity, persona, primary metric | Partly | 3.1 Job, persona, activity; 3.1 Success | JM-06 assigned; primary metric proposed, no baseline (SEG-16, Tara) |
| D2 · Usage pattern named, with its UI principle | Met | 3.1 Usage pattern; 3.2 UI principle | None: UP-08 named, with its UI principle |
| D3 · Surface with level of control; build form justified; an agent has its own trigger or identity | Partly | 3.1 AI fit and build form; 3.2 Where it appears | Surface open (SEG-12): SRF-11 agent or SRF-03 skills and MCP tools (BF-03); release-1 scope differs between mockup and phasing (SEG-15) |
| D4 · Placed in the target architecture: what it relies on and what it adds; anything new justified against what exists | Partly | 3.3 Shared layers and signals | Shared core gated on skill reuse (SEG-11, Victor); industry insights for CSP unconfirmed |
| D5 · Confirmation, access rights, provenance, "I don't know" shown in the design | Partly | 3.2 Confirmation and provenance; mockup | Cross-account access for the roll-up undecided; confidential marking method open; no evaluation set yet (SG-03) |

## Catalogue checks

| Check | Status | Note |
|---|---|---|
| GR-01 confirmation before any CRM write shown | Met | No write in release 1; refusal message in the mockup |
| GR-02 access model without a technical super-user | Partly | Roll-up access across accounts to decide |
| GR-05 personal data: consent and clearance reference | Not met | Risk assessment scope to confirm |
| SG-01, SG-02 provenance and freshness visible in the mockup | Met | Tag set extends SG-01 (CH-02) |
| SG-03 evaluation set and method attached | Not met | To define before release 1 |
| SG-04 write log defined, with retention | Not applicable | Release 2 |
| P4 simpler build forms tried or ruled out | Met | Release 0 prompts; BF-03 fallback stated |
| P5 new signal has two committed consumers and an owner | Partly | Industry insights: End User consumption to confirm |

## Readiness

| Check | Status | Note |
|---|---|---|
| Open items, each with an owner and a date | Met | Guide wrap-up; 3.1 decision log. One owner still open: project manager on the One Plan side |
| Decision log complete; every open decision has an owner | Met | SEG-01 to SEG-17 |
| Changes proposed to the framework logged (CH) | Met | CH-01, CH-02, CH-03 |
| Certification status: GRCC, AI risk assessment, stack ID | Not met | Risk assessment scope not confirmed; stack ID pending |
| Licence coverage and run cost checked for the pilot population | Not met | Xyra, next session |

## Blockers before the design review

1. Decide the release-1 scope: path A in or out (SEG-15).
2. Confirm the surface and licence coverage (SEG-12).
3. Confirm skill reuse across agents in the new experience (SEG-11).
4. Decide reading across accounts for the roll-up.
5. Assign the UX and architecture owners of sections 3.2 and 3.3.
6. Define the evaluation set required by SG-03 before release 1.

## Handover at ◆ Go build

| Item | Status |
|---|---|
| Dossier approved by the design authority | Not met |
| Owners of 3.1, 3.2 and 3.3 named | Partly: PO named (ASF); UX and architecture to assign |
| Extracts generated | Not met |
| PO and build team named; handover meeting held | Not met |
