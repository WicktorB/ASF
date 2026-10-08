---
template: 4 · Design review and handover checklist
title: "Checklist · Competitor"
scenario: competitor
doc_status: Draft          # Draft | Assessed | Reviewed
verdict: Not assessed      # Not assessed | Not ready | Ready for design review | Approved | Approved with conditions | Rework
assessed_by: Product team
reviewed_by: Design authority
discovery_step: 6 · Playback
dimensions: [D1, D2, D3, D4, D5]
version: 0.1
date: 2026-10-08
---

::: {.readme}
**In 30 seconds.** One list for the design review and for the handover at ◆ Go build. The product team (or the skill `check-design-review`) pre-checks every item against the dossier and the catalogues; the design authority gives the verdict; steering takes the go / no-go. Statuses: Met · Partly · Not met. A "Partly" or "Not met" needs a gap and an owner.
:::

## Verdict

_One sentence: ready or not, how many checks are met, what blocks. Assessed on DD Mon by …; reviewed by the design authority on …_

## The five dimensions

::: {.guide}
This list is maintained in the design canvas ("Before a design review") and copied here unchanged.
:::

| Check | Status | Evidence | Gap and owner |
|---|---|---|---|
| D1 · Job in one sentence, activity, persona, primary metric | _Met / Partly / Not met_ | _3.1 section_ | _…_ |
| D2 · Usage pattern named, with its UI principle | | _3.1, 3.2_ | |
| D3 · Surface with level of control; build form justified; an agent has its own trigger or identity | | _3.1, 3.2_ | |
| D4 · Placed in the target architecture: what it relies on and what it adds; anything new justified against what exists | | _3.3_ | |
| D5 · Confirmation, access rights, provenance, "I don't know" shown in the design | | _3.2, 3.3, mockup_ | |

## Catalogue checks

| Check | Status | Note |
|---|---|---|
| GR-01 confirmation before any CRM write shown | | |
| GR-02 access model without a technical super-user | | |
| GR-05 personal data: consent and clearance reference | | |
| SG-01, SG-02 provenance and freshness visible in the mockup | | |
| SG-03 evaluation set and method attached | | |
| SG-04 write log defined, with retention | | |
| P4 simpler build forms tried or ruled out | | |
| P5 new signal has two committed consumers and an owner | | |

## Readiness

| Check | Status | Note |
|---|---|---|
| Open items, each with an owner and a date | | |
| Decision log complete; every open decision has an owner | | |
| Changes proposed to the framework logged (CH) | | |
| Certification status: GRCC, AI risk assessment, stack ID | | |
| Licence coverage and run cost checked for the pilot population | | |

## Blockers before the design review

1. _… (decision ID)_
2. _…_

## Handover at ◆ Go build

| Item | Status |
|---|---|
| Dossier approved by the design authority | |
| Owners of 3.1, 3.2 and 3.3 named | |
| Extracts generated: BRD · high-level architecture · backlog · certification inputs · steering one-pager | |
| PO and build team named; handover meeting held | |
