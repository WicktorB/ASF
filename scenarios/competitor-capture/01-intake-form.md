---
template: 1 · Intake form
title: "Intake form · Competitor Capture"
scenario: competitor-capture
doc_status: Draft          # Draft | Checked | Validated
track: To propose          # Standard | Light | To propose
filled_by: Domain owner
checked_by: Product team (framing lead)
discovery_step: 1 · Need
dimensions: [D1]
version: 0.1
date: 2026-10-14
---

::: {.readme}
**In 30 seconds.** Two parts, two authors. Sections A and B are the domain's: the need in its own words, captured with the intake assistant. Sections C to E are the ASF product team's analysis: a first reading of D1, the neighbours in the portfolio, the track proposed. One page, filled at Discovery step 1, before the intro call.
:::

# Stated by the domain

::: {.guide}
Captured with the intake assistant: the domain shares its documents and transcripts, the assistant reads them, asks for what is missing, challenges the need and keeps the guardrails; the domain validates a text version, which the product team pastes here. MVP without document generation.
:::

## A · Who asks

| Item | Content |
|---|---|
| Requester | Samer, CRM Assistant (intake) |
| Sponsor | Samer: who is the sponsor? (intake: sponsor not stated) |
| Programme or brick | not stated (intake) |
| Users concerned | field sellers in EMEA, first (intake) |

## B · The need, in the domain's words

::: {.guide}
Three to six lines as received. Do not reformulate here: the reframing happens in the workshop and lands in the scenario brief. Quote the request if there is one.
:::

> Competitor information that customers give on the phone and in emails is not recorded
> on the opportunity. The competitor list on opportunity lines is almost always empty
> until closed-lost.
>
> Today: the competitor list is filled at closed-lost, when it becomes mandatory; some sellers use the "Add Default Opportunity Competitors" action, most don't know it exists

(intake; [original brief](inputs/intake-brief-2026-10-14.md))

| Item | Content |
|---|---|
| Expected value | Result: competitor information recorded on opportunity lines in bFO<br>For whom: field sellers in EMEA<br>Measure: % of opportunity lines with a competitor recorded (no figure stated) (intake) |
| Why now | By not stated. Driver: not stated (intake) |
| Material available | [INTAKE REQUEST — draft for the ASF intake review](inputs/intake-brief-2026-10-14.md) (intake) |

> JOB IN ONE SENTENCE (draft for the product team)
>
> Record the competitors customers mention on the right opportunity line, without sellers re-typing them.
>
> NOTES FOR THE REVIEWER
> - Solution as requested: "an agent that scans Outlook and puts the competitors into bFO automatically"
> - Other needs mentioned: win/loss dashboard by competitor for managers (secondary)
> - Existing tools named: bFO; Outlook; "Add Default Opportunity Competitors" action in bFO (what is missing in it was not captured)
> - Complexity: mailbox analysis; write into bFO; phone calls as a source; competitor quotes with prices; legal check on reading mailboxes pending
>
> TO CLARIFY IN THE INTRO CALL
> - expected_value.measure (current figure or target for % of opportunity lines with a competitor)
> - urgency.date
> - urgency.driver

(intake)

# ASF product team analysis

## C · First reading · D1 draft

::: {.guide}
Drafted by the ASF product team (or the skill `new-scenario`) from section B, not by the domain. Each line carries its source in brackets. These are hypotheses; the workshop confirms them.
:::

| Item | Draft | Source |
|---|---|---|
| Job in one sentence | Record the competitors customers mention on the right opportunity line, without sellers re-typing them. | (intake) |
| Seller activity | Proposed: JM-05 | (intake; catalogues/jm.yaml) |
| Persona | Proposed: Seller; field sellers in EMEA first. Samer: how many sellers are concerned? | (intake; catalogues/jm.yaml) |
| First idea of the value | Competitor information recorded on opportunity lines in bFO, without re-typing. Primary metric proposed (P11): % of opportunity lines with a competitor recorded. Samer: what are the baseline, target, measurement period and eligible lines? | (intake; catalogues/principles.yaml) |

## D · Neighbours in the portfolio · product team analysis

::: {.guide}
Written by the ASF product team, which knows the portfolio; the domain is not expected to fill it. A first look, not the overlap check: the overlap check is taken in the workshop at scenario level (CH-09). List what already exists or is planned on the same job, the same persona or the same data.
:::

| Existing or planned item | Same… | First reading |
|---|---|---|
| Competitor capture; Competitor capture from emails | Job and customer-interaction data; JM-05 and JM-02 | Framing lead: does this extend the existing catalogue entries, and who owns them? (catalogues/jm.yaml; intake) |
| "Add Default Opportunity Competitors" action in bFO | Competitor data on opportunity lines | Framing lead: can this action address the need through configuration or awareness, and what is missing? (intake) |
| Post-meeting experience | Customer-interaction capture; JM-05 | Framing lead: can phone-call capture reuse this path rather than create a separate one? (catalogues/jm.yaml; scenarios/one-plan-segment/03-scenario-dossier.md, 3.1) |
| One Plan Segment; competitor intelligence | Competitor signals, not the primary capture job | Framing lead: is competitor intelligence a downstream consumer? No consumer commitment is evidenced. (scenarios/one-plan-segment/03-scenario-dossier.md, 3.1; intake) |

Framing lead: where is the portfolio reference? `docs/portfolio.md` is absent; this first reading uses the catalogue and the available scenario dossier. The design authority's overlap verdict remains Open. (repository review, 14 Oct 2026)

## E · Outcome of the intake · product team analysis

| Check | Result | Status |
|---|---|---|
| Track proposed | Standard: mailbox analysis has a pending legal check (GR-05); bFO write-back has no evidenced existing confirmation pattern (P6, GR-01). Light-track criteria are not all met. (intake; template light-track criteria; catalogues/gr-sg.yaml) | Proposed |
| Next step | Intro call of about 30 minutes. Samer: when can it take place? Confirm the metric baseline/target, urgency date/driver, phone-call source, mailbox clearance and access, handling of competitor prices (GR-06), and seller confirmation before any bFO write (P6, GR-01). The requested automatic write is not an approved design. (intake; templates/01-intake-form.md; catalogues/gr-sg.yaml; catalogues/principles.yaml) | Planned |
| Owner on the product team | Product team: who is the framing lead? (intake: owner not stated) | To confirm |

::: {.guide}
Light track entry criteria, all must hold: build form BF-01, BF-02 or BF-03 on an existing agent; no new surface; no new signal or shared component; no write outside an existing confirmation pattern; no new data source needing a legal or privacy review.
:::
