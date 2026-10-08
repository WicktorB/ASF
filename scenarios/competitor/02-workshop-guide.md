---
template: 2 · Workshop guide
title: "Workshop guide · Competitor"
scenario: competitor
doc_status: Validated with the domain      # Prefilled | Validated with the domain | Superseded by the dossier
track: To confirm
filled_by: Product team (framing lead)
validated_by: Samer Baseet, CRM Assistant domain representative
discovery_steps: [2 · Intro call, 3 · Prefill, 4 · Workshop]
dimensions: [D1, D2, D3, D4, D5]
version: 0.2
date: 2026-10-08
---

::: {.readme}
**In 30 seconds.** The working record of Discovery steps 2 to 4. The product team prefills every line as a sourced hypothesis; the domain confirms, corrects or leaves it open in the workshop. This guide records the 30 Sep 2026 discussion with Samer Baseet. The guide drafts; the scenario dossier holds the reference version. Statuses: ✔ confirmed · ✎ corrected · ? open · ☐ to validate. **Must** lines are needed before the Roadmap gate; **Later** lines can wait for the brief.
:::

## Before the workshop

| Item | Content |
|---|---|
| Workshop | 30 Sep 2026, 52 min 40 s; transcript: `2026-09-30_CRM Assistant_Competitor Use Case.docx` (workshop) |
| Material read for the prefill | Slides were reviewed during the call; follow-up design material was to be shared after the call (workshop) |
| Participants | Domain: Samer Baseet (CRM Assistant domain representative) · Product team: Markus Geier, Victor Bauchet, Sowmya Chebolu and Pranav Vinod Kumar (workshop) |
| Topics covered | A need and value · B frictions · C boundary · D scope and overlap · E content and data · F what AI could do · G flags · H success · I wrap-up (workshop) |

## A · Need and value · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Need in one sentence | Capture and suggest competitor information on the relevant opportunity line from CRM history and seller-provided meeting or email context, so sellers can record it without retyping. (workshop) | ✎ | |
| Must · Who asks, who uses | Asks: CRM Assistant domain. Uses: field sellers and their managers on competitive deals. Population size and any additional users in strategy or pricing teams are not confirmed. (workshop) | ? | Samer Baseet · before Roadmap gate; date to agree |
| Must · Expected value | Improve competitor-data completeness in BFO for competitive analytics, and give sellers useful information to help win more deals. (workshop) | ✎ | |
| Later · Why now | Competitor information is mostly missing before closure; the gap limits historical analysis and the competitive strategy that can be built from CRM data. (workshop) | ✎ | |

## B · Current work and frictions · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Moment of use | At opportunity creation, usually around stage 2 and sometimes stage 3/early stages; after a customer meeting; when the seller selects a relevant email; and during deal review or at loss. (workshop) | ✎ | |
| Must · Current steps | The seller hears or reads about a competitor, may note it on paper, a form or a phone, or remember it; later they enter it on the opportunity line in BFO or skip it. Competitor and loss reason are required at closed-lost. (workshop) | ✎ | |
| Must · User frictions | Re-entry takes time and is skipped; mandatory entry at close can produce low-quality data. Sellers need value from the information, not only a capture task. (workshop) | ✎ | |
| Must · Management frictions | Incomplete capture weakens analysis of which competitors appear on deals and why opportunities are lost. Managers see only the information recorded in BFO. (workshop) | ✎ | |
| Later · Workarounds | Sellers may use paper, a form, a phone or memory. BFO already has “Add Default Opportunity Competitors”; its current rules and actual use are not yet understood. (workshop) | ? | Samer Baseet / BFO process owner · next domain follow-up; date to agree |

## C · Boundary · D5

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Decisions the seller keeps | The seller validates proposed competitor updates and remains responsible for the close date, forecast, win probability and what action to take. Competitor positioning and loss reason remain seller judgements. (workshop) | ✔ | |
| Must · Never | Never write a proposed update to BFO before the seller validates it. Never change or decide the seller’s close date, forecast, win probability or action based on a competitor suggestion. (workshop) | ✔ | |
| Must · Stays declarative | Competitor positioning and loss reason are provided or confirmed by the seller; they are not inferred as facts. (workshop) | ✔ | |
| Must · Confirmation before writing | Present the proposed competitor and ask the seller whether to add it; write to BFO only after an explicit yes. (workshop) | ✔ | |
| Must · Visible to whom | Unvalidated suggestions stay with the seller; managers see only information saved in BFO. (workshop) | ✔ | |

## D · Scope and overlap check · D1, D3

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Scope | In: suggest likely competitors in BFO at opportunity creation using CRM history, and capture competitors from meeting notes/transcripts or seller-selected emails for the relevant opportunity line; show the competitive picture on the opportunity. Later: automatic scanning of unselected emails and positioning/strategy recommendations. Out: team chats and a standalone competitor-intelligence agent. (workshop) | ✎ | |
| Must · Overlap check | Proposed: extend the broader CRM Assistant post-meeting flow and assess the existing BFO “Add Default Opportunity Competitors” action; do not create a standalone competitor agent. Check Sales Chat, Sales Digest and Pitch Agent overlap. Verdict: open. (workshop) | ? | Design authority · before Roadmap gate; date to agree |
| Later · First release | Candidate: early-stage BFO suggestions plus post-meeting capture from meeting notes and seller-selected emails, with seller confirmation before write-back. The exact order and technical feasibility remain open. (workshop) | ? | Domain and architecture owners · before brief; date to agree |
| Later · First population | Pilot population, accounts and target are not specified; Samer identified no seasonal restriction for a pilot. (workshop) | ? | Samer Baseet · before Roadmap gate; date to agree |

## E · Content and data · D4

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Content relied on | BFO competitor reference data and CRM history; meeting notes or Teams meeting information; seller-selected email; any existing competitor positioning material. Existence and ownership of the positioning material are not confirmed. (workshop) | ? | Samer Baseet / relevant data and content owners · before brief; date to agree |
| Must · Sources | BFO opportunity and opportunity-line competitor records; CRM history; meeting notes/transcripts and selected Outlook emails. Copilot for Sales may provide Teams meeting detections. Email clearance, BFO write-back and source access remain to confirm. (workshop) | ? | Samer Baseet, privacy and architecture owners · before design review; date to agree |
| Later · Data quality | Competitor information is often absent before closure. Confirm the metric baseline, master-data owner, seller create/update rights, and how global/local competitors map to product lines and geographies. (workshop) | ? | Samer Baseet / BFO data owner · before Roadmap gate; date to agree |

## F · What AI could do · D2, D3

::: {.guide}
Options recorded from the discussion: one line per option, a verdict and a reason from the domain. The recommendation closes the section and feeds the Roadmap gate.
:::

| # | Option | Pattern, surface, build form proposed | Verdict and reason |
|---|---|---|---|
| 0 | Suggest likely competitors in BFO at opportunity creation from CRM history, geography and product context. (workshop) | UP-03 / UP-07 · SRF-01 · BF-05 or BF-06 to assess (workshop) | Keep in scope; supports earlier capture, including when meeting or email evidence is not available. (workshop) |
| 1 | Capture competitors from meeting notes/transcripts and seller-selected emails; ask the seller to validate before BFO write-back. (workshop) | UP-07 / UP-09 · SRF-10 / SRF-12 · BF-03 or BF-05 to assess (workshop) | Keep in scope as part of the broader CRM Assistant post-meeting flow; no dedicated competitor agent. (workshop) |
| 2 | Automatically scan unselected emails for competitor mentions. (workshop) | UP-07 · SRF-05 / SRF-12 · BF-06 to assess (workshop) | Later; email clearance and technical constraints need checking first. (workshop) |
| 3 | Serve competitive positioning or strategy material in context. (workshop) | UP-02 / UP-03 · SRF-03 / SRF-04 / SRF-06 · build form to assess (workshop) | Later; Samer asked to avoid duplication with Sales Chat and Sales Digest; also check Pitch Agent and existing material. (workshop) |

**Recommendation:** Start with early-stage BFO competitor suggestions and post-meeting capture from meeting notes and seller-selected emails, with seller validation before every write. Keep the competitive picture in BFO. Defer unselected-email scanning, team chats and competitive strategy/positioning recommendations pending privacy, overlap and content checks. Treat the implementation as part of the broader CRM Assistant experience, not a standalone competitor agent. (workshop)

## G · Complexity flags · D4, D5

| Flag | Answer | Note |
|---|---|---|
| Personal data | Unknown (workshop) | Customer contacts and email content may be involved; confirm scope and handling. (workshop) |
| Confidential content | Unknown (workshop) | Meeting and email content; permitted processing to confirm. (workshop) |
| Disconnected sources | To confirm (workshop) | BFO, meeting notes/Teams information and selected Outlook email are candidate sources; access and integration are not confirmed. (workshop) |
| Legal, privacy, works council | Open (workshop) | Clearance for email access/analysis is pending; identify the privacy/legal owner. (workshop) |
| Countries and languages | To confirm (intake; workshop) | Field sellers are in EMEA; global and local competitors vary by geography. Country and language coverage is open. (workshop) |
| Licensing | Unknown (workshop) | Confirm licences and availability for the relevant BFO, Copilot for Sales and Outlook capabilities. (workshop) |
| Dependencies (environment, stack ID, other teams) | Open (workshop) | BFO write-back and competitor reference data; Copilot for Sales meeting detection; global CRM Assistant post-meeting flow; Sales Chat, Sales Digest and Pitch Agent overlap. (workshop) |

## H · Success · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · What success looks like | More complete competitor information on opportunity lines, less retyping and better data quality; the broader aim is to help sellers win more deals. No target or timeframe was agreed. (workshop) | ? | Samer Baseet · before Roadmap gate; date to agree |
| Must · Primary metric candidate | Candidate (P11): percentage of opportunities with a competitor captured by stage 2. Also monitor competitor completeness on opportunity lines and lost opportunities with a competitor and loss reason. Confirm the primary measure and denominator. (workshop) | ? | Samer Baseet · before Roadmap gate; date to agree |
| Later · Baseline | Current baseline, target and existing reporting were not stated; confirm whether reports already exist. (workshop) | ? | Samer Baseet / BFO reporting owner · before Roadmap gate; date to agree |

## I · Wrap-up

| Decision | Agreed by, date |
|---|---|
| Capture the competitor on the relevant opportunity line; show a competitive overview at opportunity level. | Samer Baseet, CRM Assistant domain representative · 30 Sep 2026 (workshop) |
| Use CRM history for early-stage suggestions and meeting notes/transcripts or seller-selected emails for capture; defer automatic email scanning. | Samer Baseet, CRM Assistant domain representative · 30 Sep 2026 (workshop) |
| Require seller validation before BFO write-back; leave sales actions and declarative competitor/loss assessments with the seller. | Samer Baseet, CRM Assistant domain representative · 30 Sep 2026 (workshop) |
| Keep the capability within the broader CRM Assistant experience rather than create a standalone competitor agent; defer positioning insights pending overlap checks. | Samer Baseet, CRM Assistant domain representative · 30 Sep 2026 (workshop) |
| Use competitor capture by stage 2 as a KPI candidate; no target or baseline was agreed. | Samer Baseet, CRM Assistant domain representative · 30 Sep 2026 (workshop) |

| Open item | Owner | Due |
|---|---|---|
| Confirm user population/size, pilot population, accounts and target. (workshop) | Samer Baseet | Before Roadmap gate; date to agree |
| Confirm competitor master-data owner, seller create/update rights, global/local matching and product-line use; verify current BFO line-level fields and “Add Default Opportunity Competitors” behaviour. (workshop) | Samer Baseet with BFO/data owners | Before brief; date to agree |
| Confirm whether competitor and loss-reason information is captured at opportunity or line level, and validate stage 2/3 trigger and metric definition, baseline and target. (workshop) | Samer Baseet with BFO process/reporting owners | Before Roadmap gate; date to agree |
| Clear legal/privacy and access constraints for selected/unselected email analysis; confirm personal/confidential data handling, Teams detection and BFO write-back feasibility. (workshop) | Samer Baseet to identify privacy and architecture owners | Before design review; date to agree |
| Decide overlap/placement across CRM Assistant post-meeting, Sales Chat, Sales Digest, Pitch Agent and existing positioning material. (workshop) | Design authority with product owners | Before Roadmap gate; date to agree |

| Gate | Input from this guide |
|---|---|
| Overlap check (design authority) | Proposed extension of CRM Assistant post-meeting flow and assessment of the existing BFO action; no standalone competitor agent. Design authority verdict remains open. (workshop) |
| ◆ Roadmap (steering) | Recommendation in F; track remains To confirm. (workshop) |
| Next step | Share the design material for domain review, resolve the open items, then draft scenario dossier 3.1, 3.2 and 3.3; date and owners to agree. (workshop) |

::: {.guide}
Guide updated from the 30 Sep 2026 session transcript; open items remain for follow-up with their owners.
:::
