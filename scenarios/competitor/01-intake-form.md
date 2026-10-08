---
template: 1 · Intake form
title: "Intake form · Competitor"
scenario: competitor
doc_status: Draft
track: Standard
filled_by: Domain owner (intake request from Samer, CRM Assistant, received 8 Oct 2026)
checked_by: Product team (framing lead)
discovery_step: 1 · Need
dimensions: [D1]
version: 0.2
date: 2026-10-08
---

::: {.readme}
**In 30 seconds.** Sections A and B: the intake request of Samer, CRM Assistant (filed in `inputs/intake-request-2026-10-08.md`): competitor information given by customers is not recorded on the opportunity lines in bFO. Sections C to E: the ASF product team's first reading. Outcome proposed: standard track, with the request "an agent that scans Outlook and puts the competitors into bFO automatically" tested against the confirmation and clearance rules before any build form is chosen.
:::

# Stated by the domain

## A · Who asks

| Item | Content |
|---|---|
| Requester | Samer, CRM Assistant |
| Sponsor | Not stated |
| Programme or brick | Not stated; to confirm |
| Users concerned | Field sellers in EMEA, first; number not stated |

## B · The need, in the domain's words

_"Competitor information that customers give on the phone and in emails is not recorded on the opportunity. The competitor list on opportunity lines is almost always empty until closed-lost."_

_"Who is affected: field sellers in EMEA, first"_

_"Today: the competitor list is filled at closed-lost, when it becomes mandatory; some sellers use the "Add Default Opportunity Competitors" action, most don't know it exists"_

| Item | Content |
|---|---|
| Expected value | Competitor information recorded on opportunity lines in bFO, for field sellers in EMEA. Measure: % of opportunity lines with a competitor recorded (no figure stated) |
| Why now | Not stated: date and driver to clarify in the intro call |
| Material available | None attached. Tools named: bFO; Outlook; "Add Default Opportunity Competitors" action in bFO (what is missing in it was not captured) |
| Solution as requested | "an agent that scans Outlook and puts the competitors into bFO automatically" |
| Other needs mentioned | Win/loss dashboard by competitor for managers (secondary) |

# ASF product team analysis

## C · First reading · D1 draft

| Item | Draft | Source |
|---|---|---|
| Job in one sentence | Record the competitors customers mention on the right opportunity line, without sellers re-typing them | (intake request, job draft) |
| Seller activity | JM-05 I debrief and keep the CRM up to date. JM-02 is where the information arises; one activity only, to confirm in the workshop | (catalogue JM; intake request) |
| Persona | Seller: the field seller in EMEA | (intake request; catalogue JM-05) |
| First idea of the value | Fewer steps (no retyping, P9) and quality (the competitor known during the deal, not only at closed-lost). Primary metric proposed: % of opportunity lines with a competitor recorded (P11); no baseline stated. Question to the owner: is it counted before closed-lost, since closed-lost makes the field mandatory, and what business outcome sits behind it | (intake request; P9, P11) |

## D · Neighbours in the portfolio · product team analysis

| Existing or planned item | Same… | First reading |
|---|---|---|
| Competitor capture from emails (JM-02, JM-05; BF-06 example) | Job, data, source | Likely the same item: this scenario would frame it. Overlap check in the workshop (CH-09) |
| "Add Default Opportunity Competitors" action in bFO | Job, data | Existing manual route; what it lacks is unknown. Keep or retire, to decide after the intro call |
| Post-meeting; Meet capture and Voice to CRM (JM-04, JM-05, conditional) | Activity, source | Consume the debrief facts; do not rebuild. Phone calls as a source depend on these |
| Signature detection (JM-02) | Source (mailbox) | Share the mailbox reading and its legal clearance (GR-05) rather than reading twice |
| Update validation hub (SC-01, SRF-12; both not yet confirmed) | Surface, write path | Likely reuse: a change detected without the seller asking cannot be confirmed where it was detected |
| One Plan Segment | Data | Route: competitor signals feed its competitive section later; tag set aligned through CH-02 |

## E · Outcome of the intake · product team analysis

| Check | Result | Status |
|---|---|---|
| Track proposed | Standard. The light track is not met: the agent requested is not BF-01 to BF-03 (P2 and P4 are tested at the brief); detection without the seller asking needs a shared component (SC-01); writing to bFO needs the confirmation pattern (GR-01, SC-02); reading mailboxes and calls needs legal clearance by country (GR-05, pending in the request); competitor quotes with prices fall under GR-06 | Proposed; confirmed at the brief |
| Automatic write | "Automatically" conflicts with GR-01 and P6: the AI proposes, the seller confirms, in one step. To raise with the requester | Open |
| Split or group | The win/loss dashboard by competitor for managers is secondary: left out of release 1, to route in the workshop (nearest existing performance view: Sales Command Center, to confirm) | Proposed |
| To clarify in the intro call | From the request: current figure or target for the metric, date, driver. From the product team: sponsor and brick; what the bFO action lacks; which phone source is meant; how a mention is matched to the right opportunity line when a customer has several | Open |
| Next step | Intro call of about 30 minutes with Samer; its transcript is filed in `inputs/` and feeds the prefill | _Date to set_ |
| Owner on the product team | Framing lead | — |
