---
template: 2 · Workshop guide
title: "Workshop guide · Competitor Capture"
scenario: competitor-capture
doc_status: Prefilled
track: To confirm
filled_by: Product team (framing lead)
validated_by: Domain owner, in the workshop
discovery_steps: [2 · Intro call, 3 · Prefill, 4 · Workshop]
dimensions: [D1, D2, D3, D4, D5]
version: 0.3
date: 2026-10-14
---

::: {.readme}
**In 30 seconds.** The working record of Discovery steps 2 to 4. All entries remain sourced hypotheses for domain validation, including points discussed during the guide read-through on 30 Sep. Main proposal: capture as part of the post-meeting experience, with a separate early-stage suggestion path to investigate; not a dedicated competitor agent. Statuses: ✔ confirmed · ✎ corrected · ? open · ☐ to validate. **Must** lines are needed before the Roadmap gate; **Later** lines can wait for the brief. This guide and its transcript-derived evidence summary are published in a public repository with the requester's approval; the source transcript itself is not included. (intro call, 30 Sep, 12:07–14:06, 25:27–26:26, 51:02–52:29; requester approval, 14 Oct)
:::

## Before the workshop

| Item | Content |
|---|---|
| Intro call | 30 Sep 2026, 52 min 40 s. The call includes a draft-guide read-through, not validation of this version. The requester-supplied source transcript is held separately and is not included in this repository. (intro call, header, 25:27–26:26) |
| Material read for the prefill | Requester-provided intake and call transcript only for domain facts. The slides and bFO screen shown in the call were not supplied separately; no screenshot or field/API inspection was performed. Catalogues constrain proposals; the existing intake neighbour list and One Plan Segment dossier are used only for the overlap check. (intake; intro call, 1:25–1:47, 15:26–24:56; repository review, 14 Oct) |
| Participants | Samer, CRM Assistant requester; Markus, Victor, Sowmya and Pranav appear in the transcript. Samer: who should attend the workshop from the domain, seller population, bFO data/process team, privacy/legal and product team? Product team: who owns framing, PO, UX and architecture? (intake; intro call, 9:15–12:07, 52:29–52:39) |
| Agenda, 60 to 90 minutes | Proposed: A need and value (10) · B frictions (10) · C boundary (10) · D scope and overlap (15) · E content and data (10) · F what AI could do (15) · G flags (5) · H success (5) · I wrap-up (5). Framing lead: confirm the date and 90-minute slot. (templates/02-workshop-guide.md) |

## A · Need and value · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Need in one sentence | Record the competitors customers mention on the right opportunity line, without sellers re-typing them. Proposed D1: JM-05; keep historical suggestions distinct from captured mentions. (intake; intro call, 26:26–27:18, 29:45–30:13; catalogues/jm.yaml) | ☐ | Samer: confirm the capture job and whether early-stage suggestions are a separate path; at workshop? |
| Must · Who asks, who uses | Request: CRM Assistant domain. Primary persona proposed: Seller; field sellers in EMEA first. Managers read confirmed CRM data; strategy/offer/pricing users were discussed but not established. (intake; intro call, 27:19–28:31, 38:33–40:19; catalogues/jm.yaml) | ☐ | Samer: name sponsor, pilot countries, seller roles and population size; at workshop? |
| Must · Expected value | Better competitor completeness while a deal is active, less retyping, and visibility of who the seller faces. Winning more deals is an ambition, not an evidenced causal result. (intro call, 23:27–24:17, 26:26–27:18, 28:31–29:45) | ☐ | Samer: rank completeness, effort saved and seller usefulness; at workshop? |
| Later · Why now | No seasonal pilot restriction was identified by Samer. This does not establish a deadline or urgency driver. (intro call, 49:39–50:01; intake) | ☐ | Samer: what deadline and business driver apply? Before Roadmap? |

## B · Current work and frictions · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Moment of use | After physical/remote customer meetings or selected emails, at deal review/loss, and at opportunity creation or early stage. Stage two is mentioned as a KPI; stage two or three is mentioned for creation. Do not treat the trigger as settled. (intro call, 6:18–7:09, 28:31–30:13, 31:07–32:08) | ☐ | Samer and bFO process owner: what exact event and stage should each path use? At workshop? |
| Must · Current steps | Seller hears/reads a competitor, notes or remembers it, then enters it in bFO late or not at all. A loss reason is captured at loss. Samer accepted this outline; exact closed-lost fields were not verified on screen. (intro call, 22:50–25:05, 30:13–31:05) | ☐ | Samer: provide one anonymised active deal and one lost line showing the actual steps; before workshop? |
| Must · User frictions | Re-entry adds work; sellers see limited immediate value in maintaining competitor data; mandatory closure capture can encourage low-quality entries. These are discussion findings, not measured time savings. (intro call, 23:27–24:17, 30:13–31:05) | ☐ | Samer and seller representative: validate with examples and typical frequency; at workshop? |
| Must · Management frictions | Missing historical competitor data limits competitive analysis and understanding of who won and why. The secondary win/loss dashboard is a separate consumption need. (intake; intro call, 2:28–3:46, 28:31–29:45) | ☐ | Samer: identify the reporting owner and existing reports; before Roadmap? |
| Later · Workarounds | Some sellers use "Add Default Opportunity Competitors"; most do not know it exists. The action was seen during the call, but its rules and shortcomings were not established. (intake; intro call, 17:41–18:43) | ☐ | bFO process owner, to nominate: demonstrate the action and its rules before a new build is proposed. |

## C · Boundary · D5

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Decisions the seller keeps | Seller retains close date, forecast, win-probability judgement and deal actions. Capture and suggestions support the seller; they do not decide strategy. (intro call, 37:54–38:31; P10, GR-03) | ☐ | Samer: reconfirm this boundary for both capture and historical suggestions; at workshop? |
| Must · Never | Never write without seller confirmation; never change forecast/date or judge win probability; never turn an inferred likely competitor into a customer-confirmed fact. The last boundary is proposed from the distinction between historical suggestions and meeting evidence, not an agreed historical-inference design. (intro call, 3:16–4:38, 36:17–38:31; P6, P7, GR-01, GR-03, GR-04) | ☐ | Samer and architecture lead, to nominate: agree missing/ambiguous-name and opportunity-line behaviour; at workshop? |
| Must · Stays declarative | Competitor positioning and loss reason remain seller-owned assessments; competitor prices are sourced claims, not verified market facts. Capture may draft from supplied evidence, but may not infer these assessments from history alone. (intro call, 7:50–8:47, 38:33; intake; GR-06, P10) | ☐ | Samer and legal owner, to nominate: identify permitted fields, claim labels and sensitive-data restrictions; at workshop? |
| Later · Confirmation before writing | Read back the proposed competitor and target opportunity/line; seller accepts, edits or rejects; only then use the shared writer. Acceptance was explicit in the call, but this guide remains to validate. Surface and reversibility are not designed yet. (intro call, 36:17–36:56, 41:32–43:02; UP-07, SC-02, SC-04, GR-01, SG-04) | ☐ | UX and architecture leads, to nominate: show confirmation, provenance, unknown/missing-data handling and write log in the mockup; before design review? |
| Later · Visible to whom | Working suggestions stay with the seller; managers see confirmed bFO data subject to CRM access. No access model or leadership self-service design was supplied. (intro call, 38:33–40:19; GR-02) | ☐ | Samer and bFO access owner, to nominate: confirm visibility and retention for proposals, source excerpts and committed data; before design review? |

## D · Scope and overlap check · D1, D3

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Scope | Proposed in: capture from debrief/meeting notes and seller-selected emails, with confirmation against an opportunity line. Option: early-stage likely competitors from existing defaults/history, separately labelled. Later: automatic mailbox analysis and reuse of approved positioning material. Out of first release: team-chat mining, strategy recommendations and a manager dashboard build. (intake; intro call, 3:16–4:38, 34:39–36:07, 38:33–43:02, 46:36–48:20) | ☐ | Samer: prioritise capture versus creation-time suggestion; resolve the brief interjection at 40:17 rather than treating the scope read-through as final approval; at workshop? |
| Must · Overlap check | Proposed verdict: extend/group capture with the CRM Assistant post-meeting experience, not a standalone competitor agent; assess bFO creation-time suggestions as a distinct path. Extend existing competitor/email capture and the default-competitor action where possible; consume shared CRM editing, Teams capture and reference data; route material/distribution to Sales Chat, Sales Digest, Meeting Prep or pitch-agent owners. One Plan Segment is a possible downstream consumer, not a commitment. (intro call, 12:07–14:06, 17:41–18:43, 34:39–36:07, 40:19–43:02, 46:10–48:20, 51:02–52:29; intake D; portfolio references only: catalogues/jm.yaml and One Plan Segment dossier, 3.1) | ☐ | Design authority: confirm extend/consume/route/new for each neighbour and identify owners. Framing lead: supply missing portfolio reference; before Roadmap? |
| Later · First release | Proposed: validate a seller-initiated capture path on existing surfaces and the shared confirmed write path first; compare the existing default action for early-stage coverage in parallel. No autonomous mailbox scan or unconfirmed write. This is a release proposal, not a dated commitment. (intro call, 36:17–36:56, 38:33–43:02; P3, P4, P6) | ☐ | Samer and product owner, to nominate: select first scope and date after feasibility and overlap checks; at workshop? |
| Later · First population | EMEA field sellers first in the intake; market/country users discussed on the call without a pilot selection. (intake; intro call, 27:19–28:31, 49:39–50:01) | ☐ | Samer: which countries, languages, sellers and accounts can join an authorised pilot? Before Roadmap? |

## E · Content and data · D4

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Content relied on | Competitor reference object and opportunity/line links, selected customer evidence and existing default rules; approved positioning material only if its owner and availability are established. Historical comparison requires an agreed method before recommendations. (intro call, 3:16–5:13, 14:06–15:00, 17:41–18:43, 43:06–46:36; P10) | ☐ | Samer: obtain data/process owner and sample records. Fernanda: does approved positioning material exist and who owns it? Before workshop? |
| Must · Sources | bFO opportunities, lines, competitors and historical outcomes; seller debrief, meeting notes/Teams transcripts and selected Outlook emails. Proposed dependencies: LY-01, LY-03, LY-04 (SC-02, SC-03, SC-04, SC-07), LY-05 (SC-08). LY-02/SC-05 are not proposed for first capture release: no owned shared signal or two committed consumers; SC-01 only if queued detection is selected. Access, endpoints and availability are not verified. (intro call, 12:07–14:06, 18:43–22:05, 31:07–32:08, 41:32–47:48; catalogues/ly.yaml, P5) | ☐ | Architecture lead, to nominate: confirm object/API mappings, permission model, environments and reusable components; before design review? |
| Later · Data quality | The call corrected two assumptions: line-level competitors were found after an initial denial; Sowmya described a reference object/lookup after Samer said no fixed list was known. Reference ownership, create rights, global/local matching, commentary fields and roll-up rules remain unresolved. (intro call, 20:46–22:05, 43:06–45:43) | ☐ | bFO data/process owner, to nominate: verify the schema and aliases, duplicates, unmatched names, line ambiguity and opportunity summary behaviour; before design review? |

## F · What AI could do · D2, D3

::: {.guide}
Options come from the prefill: one line per option, a verdict and a reason from the domain. The recommendation closes the section and feeds the Roadmap gate.
:::

| # | Option | Pattern, surface, build form proposed | Verdict and reason |
|---|---|---|---|
| 0 | Prompts on existing agents now: seller supplies a selected excerpt/debrief and asks for a sourced capture draft; do not assume CRM write tools exist. (intro call, 26:26–27:18, 46:36; P4) | Proposed UP-07 · SRF-03 or SRF-14 · BF-01; fixed Microsoft control. (catalogues/up.yaml, srf.yaml, bf.yaml) | ☐ Proposed comparison baseline, not an endorsed release. Samer: is manual copy/review useful while the shared write path is assessed? (intro call, 11:28–12:13, 41:08–43:02) |
| 1 | Competitor capture as part of the existing/planned post-meeting experience, with reference matching, target-line review and confirmed write; selected-email path if feasible. (intro call, 12:07–14:06, 40:19–43:02, 46:36) | Proposed UP-07, with UP-09 for the wider host process · SRF-03 via BF-03 as the simplest conversational option, not custom instructions inside Sales Chat. SRF-05/BF-02 is an in-context alternative to test; mobile SRF-10 remains Open. (catalogues/up.yaml, srf.yaml, bf.yaml; P2–P4) | ☐ Proposed first build candidate; domain and host owners must confirm feasibility. Seller benefit: no retyping, one change confirmed in one step; no form on conversational surfaces. (intro call, 26:26–27:18, 41:32–43:02; UP-07) |
| 2 | At creation/early stage, reuse the default-competitor action before adding historical/geographic suggestions; distinguish possible competitors from captured customer statements. (intro call, 3:16–5:13, 17:41–18:43, 29:45–30:13, 48:18–48:20) | Proposed UP-03 then UP-07 · SRF-01, controlled CRM surface · BF-07 if agreed rules suffice; BF-06 only if comprehension is needed and the comparison method is agreed. (catalogues/up.yaml, srf.yaml, bf.yaml; P4, P10) | ☐ Proposed parallel feasibility track, not an agreed historical model. bFO owner and Samer: what do existing rules miss, what stage triggers it, and how will the seller validate? (intro call, 17:41–18:43, 29:45–30:13) |
| 3 | Detect email competitors without being asked and queue proposals, never auto-write; optional review on won/lost events. (intro call, 38:33–40:19, 46:36–48:18) | Proposed UP-07 · SRF-12 (controlled UI; host undecided) · BF-06, SC-01; use SC-06 only if actionable notifications are needed. (catalogues/up.yaml, srf.yaml, bf.yaml, ly.yaml; P8) | ☐ Proposed Later: legal clearance, consent, access, queue ownership and hosting are unresolved; compare against selected-email capture first. (intro call, 48:27–49:39; GR-05) |
| 4 | Reuse approved competitor positioning material through existing experiences, not generate a deal strategy or build a separate intelligence agent. (intro call, 33:30–36:07, 46:10–48:18) | Proposed UP-04 · SRF-03 · BF-03 if an existing host can retrieve approved material; distribution to other surfaces is an owner discussion, not committed build. (catalogues/up.yaml, srf.yaml, bf.yaml; P5, P10) | ☐ Proposed route/consume, not first-release scope. Samer/Fernanda and Sales Chat, Sales Digest, Meeting Prep and pitch-agent owners: verify content and non-duplication. (intro call, 14:06–15:00, 34:39–36:07, 46:10) |

**Recommendation:** Proposed Standard track, confirmed at the brief: compare option 0 with option 1, assess option 2 separately with the bFO owner, defer option 3 until legal and shared-queue readiness, and route option 4 to existing owners. Prefer selected evidence and the shared confirmed writer over a dedicated competitor agent. At the brief, settle surface/control before build form, target-line mapping, provenance/freshness (SG-01, SG-02), safe failure, evaluation (SG-03) and reversible write logging (SG-04). A new BF-04 agent is not justified for this scenario by the call; the post-meeting host's identity is a separate decision. (intro call, 17:41–18:43, 34:39–36:56, 40:19–43:02, 48:27–49:39, 51:02–52:29; P2–P7; template light-track criteria)

## G · Complexity flags · D4, D5

| Flag | Answer | Note |
|---|---|---|
| Personal data | Yes | Customer email, contact information and meeting content are candidate inputs, not cleared processing. Legal owner, to nominate: what consent, country permissions and retention apply? ☐ (intro call, 48:27–49:39; GR-02, GR-05) |
| Confidential content | Yes | Competitor quotes/prices and seller positioning assessments may be present. Samer/legal owner: which fields and excerpts can be retained or shared, and under which access rules? ☐ (intake; intro call, 7:50–8:47, 38:33; GR-06) |
| Disconnected sources | Yes | Outlook/meeting content and bFO records must be linked; no connector or permission check was performed. Architecture lead: how will account, opportunity, line and competitor be matched? ☐ (intro call, 12:07–14:06, 18:43–22:05, 46:36–48:18) |
| Legal, privacy, works council | Unknown | Mailbox clearance is pending; the call asks what email analysis is permitted. No consent, legal approval or works-council decision was provided. Legal owner: what review is required, including selected-email and recorded-meeting paths? ☐ (intake; intro call, 48:27–49:39; GR-05) |
| Countries and languages | Unknown | EMEA first is from intake; local/global competitor differences were discussed, not countries/languages for a pilot. Samer: supply the country and language list. ☐ (intake; intro call, 4:38–5:13, 44:58–45:43) |
| Licensing | Unknown | Copilot for Sales and Teams capture were proposed; no entitlement, consumption budget or run-cost evidence was supplied. Platform owner, to nominate: confirm coverage and estimate for the chosen pilot. ☐ (intro call, 31:07–32:08, 40:19–41:08, 48:27–49:39; LY-05) |
| Dependencies (environment, stack ID, other teams) | Yes | Shared CRM editing, post-meeting host, reference ownership and surface extensibility need coordination; environment and stack ID are unknown. Architecture/framing leads: name owners and delivery dependencies; verify SRF-05 preview API and SRF-03 instruction constraints rather than assume capability. ☐ (intro call, 11:28–14:06, 41:08–45:43, 48:27–49:39, 51:02–52:29; catalogues/srf.yaml) |

## H · Success · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · What success looks like | This cycle, proposed: settle the capture path and early-stage split. First release, proposed: seller-confirmed competitors on the intended lines from selected evidence without retyping. Next cycle, proposed: expand only after quality, permission and reuse checks; no promised win-rate improvement. (intro call, 26:26–27:18, 28:31–30:13, 36:17–36:56, 51:24–52:29) | ☐ | Samer: confirm outcomes and target dates for each horizon; at workshop? |
| Must · Primary metric candidate | Proposed P11 candidate: % of eligible opportunity lines with a competitor recorded (intake). The call also names % of opportunities with a competitor by stage two and lost opportunities with competitor/loss reason. Keep one primary metric; do not silently switch the denominator or early-stage cutoff. (intake; intro call, 6:18–7:09, 29:45–30:13, 50:01–50:44; P11) | ☐ | Samer and reporting owner, to nominate: choose opportunity versus line, stage/cutoff, eligibility, target and measurement window; classify other measures as secondary. At workshop? |
| Later · Baseline | No measured baseline was supplied. "Almost zero" on example opportunities is qualitative only; report availability was suggested, not verified. (intro call, 22:50–24:17, 50:01–50:44) | ☐ | Reporting owner, to nominate: obtain an extract for the agreed population/metric and capture the baseline before pilot; propose date at workshop. |

## I · Wrap-up

| Decision | Agreed by, date |
|---|---|
| ☐ Proposed: group capture with post-meeting; investigate creation-time recommendations separately, not as a new competitor agent. (intro call, 12:07–14:06, 41:32–43:02, 51:24–52:29) | Discussed by Markus and Samer on 30 Sep; design authority/workshop validation still required. |
| ☐ Proposed: seller confirmation is required for every write; forecast/date/probability decisions stay with the seller. (intro call, 36:17–38:31) | Samer explicitly supported these points on 30 Sep; revalidate against the chosen path and mockup. |
| ☐ Proposed: selected evidence first; automatic mailbox analysis later, subject to clearance. (intro call, 38:33–40:19, 48:27–49:39) | Workshop scope and legal owner confirmation required; do not treat the read-through as a signed release scope. |

| Open item | Owner | Due |
|---|---|---|
| ☐ Choose capture/creation priorities, first population, one metric, target and urgency. (intake; intro call, 6:18, 29:45–30:13, 49:39–50:44) | Samer: confirm accountable domain/reporting owners. | Framing lead: agree date at workshop. |
| ☐ Verify competitor reference owner/create rights, line links, closed-lost fields, default rules and roll-up; obtain anonymised examples. (intro call, 17:41–25:05, 43:06–45:43) | Samer: connect bFO data/process owner; Sowmya: who can verify the schema? | Before design choice; owner to set date. |
| ☐ Decide selected-email/meeting permissions, country clearance, sensitive-data handling and retention. (intro call, 48:27–49:39; intake) | Samer: identify legal/privacy and access owners. | Before any source-data pilot; owner to set date. |
| ☐ Resolve reuse and ownership across capture/defaults, shared CRM editing, post-meeting, Sales Chat/Digest, Meeting Prep/pitch and downstream reporting/One Plan; nominate PO, UX, architecture and surface hosts. (intro call, 11:28–14:06, 34:39–36:07, 41:08–43:02, 46:10, 51:02–52:29; portfolio references only: intake D, One Plan Segment dossier 3.1) | Design authority and framing lead, to nominate: confirm accountable owners and verdicts. | Before Roadmap; owners to set date. |
| ☐ Define source-to-line matching tests, missing/ambiguous-name handling, confirmation mockup, evaluation thresholds, reversible write log, licensing and environment. (intro call, 18:43–22:05, 36:17–36:56, 43:06–45:43, 48:27–49:39; GR-01–GR-06, SG-01–SG-04) | UX, architecture and platform owners, to nominate: agree acceptance criteria. | Before design review; owners to set date. |

| Gate | Input from this guide |
|---|---|
| Overlap check (design authority) | ☐ Proposed verdict in D: extend/group capture with post-meeting; assess the bFO suggestion path separately. Confirm each neighbour in the local evidence notes. No new CH item proposed; CH-01 and CH-02 remain existing Proposed items, not validated capability. (intro call, 51:02–52:29; catalogues/changes.yaml) |
| ◆ Roadmap (steering) | ☐ Recommendation in F, one agreed metric, scope/reuse verdict and named owners. Standard track proposed, not confirmed; legal and platform unknowns remain visible. (intake; intro call, 48:27–50:44; template light-track criteria) |
| Next step | ☐ Review this local prefill with Samer and source owners; validate/correct lines in the workshop, then update within 48 hours. After Roadmap, draft 3.1/3.2/3.3 with PO/UX/architecture owners and prepare design review. No public PR; framing lead: choose an approved restricted home for the guide and transcript. (intro call, 51:02–52:29; templates/02-workshop-guide.md; user storage instruction, 14 Oct) |

::: {.guide}
Within 48 hours of the workshop the product team (or the skill `update-workshop-guide` from the session transcript) sets each status, logs the decisions and open items, and sets `doc_status: Validated with the domain`.
:::
