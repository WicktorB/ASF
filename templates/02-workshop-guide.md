---
template: 2 · Workshop guide
title: "Workshop guide · [scenario name]"
scenario: [scenario-slug]
doc_status: Prefilled      # Prefilled | Validated with the domain | Superseded by the dossier
track: To confirm
filled_by: Product team (framing lead)
validated_by: Domain owner, in the workshop
discovery_steps: [2 · Intro call, 3 · Prefill, 4 · Workshop]
dimensions: [D1, D2, D3, D4, D5]
version: 0.1
date: YYYY-MM-DD
---

::: {.readme}
**In 30 seconds.** The working record of Discovery steps 2 to 4. The product team prefills every line as a sourced hypothesis (from the intake, the intro call transcript and the domain's material); the domain confirms, corrects or removes each line in the workshop. The guide drafts; the scenario dossier holds the reference version. Statuses: ✔ confirmed · ✎ corrected · ? open · ☐ to validate. **Must** lines are needed before the Roadmap gate; **Later** lines can wait for the brief.
:::

## Before the workshop

| Item | Content |
|---|---|
| Intro call | _Date, about 30 minutes; transcript filed as `inputs/intro-call-YYYY-MM-DD.md`_ |
| Material read for the prefill | _Decks, notes, screenshots; never the team's own outputs_ |
| Participants | _Domain: names and roles · Product team: framing lead, PO, UX, architecture_ |
| Agenda, 60 to 90 minutes | A need and value (10) · B frictions (10) · C boundary (10) · D scope and overlap (15) · E content and data (10) · F what AI could do (15) · G flags (5) · H success (5) · I wrap-up (5) |

## A · Need and value · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Need in one sentence | _… (intake)_ | ☐ | |
| Must · Who asks, who uses | _Asks: … Uses: … Size: … (intro call)_ | ☐ | |
| Must · Expected value | _… (intake)_ | ☐ | |
| Later · Why now | _… (intake)_ | ☐ | |

## B · Current work and frictions · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Moment of use | _When in the seller's day or year (intro call)_ | ☐ | |
| Must · Current steps | _1 … 2 … 3 … (material)_ | ☐ | |
| Must · User frictions | _Where time or quality is lost (intro call)_ | ☐ | |
| Must · Management frictions | _What leadership cannot see or do (intro call)_ | ☐ | |
| Later · Workarounds | _What sellers do today instead (intro call)_ | ☐ | |

## C · Boundary · D5

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Decisions the seller keeps | _… (intro call)_ | ☐ | |
| Must · Never | _What the solution must never do (intro call)_ | ☐ | |
| Must · Stays declarative | _Values that are entered by people, never derived_ | ☐ | |
| Later · Confirmation before writing | _Where confirmation happens (GR-01)_ | ☐ | |
| Later · Visible to whom | _Who sees outputs; leadership self-service yes or no_ | ☐ | |

## D · Scope and overlap check · D1, D3

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Scope | _In: … Option: … Later: … Out: …_ | ☐ | |
| Must · Overlap check | _For each neighbour (intake D): extend / consume / route / new; verdict proposed: new scenario, extend an existing solution, group, stop_ | ☐ | Design authority |
| Later · First release | _What ships first_ | ☐ | |
| Later · First population | _Pilot population and accounts_ | ☐ | |

## E · Content and data · D4

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · Content relied on | _Templates, rules, previous outputs, knowledge; exists or to collect_ | ☐ | |
| Must · Sources | _Systems and files; access known or to clear_ | ☐ | |
| Later · Data quality | _Typed figures, disconnected versions, reference per measure_ | ☐ | |

## F · What AI could do · D2, D3

::: {.guide}
Options come from the prefill: one line per option, a verdict and a reason from the domain. The recommendation closes the section and feeds the Roadmap gate.
:::

| # | Option | Pattern, surface, build form proposed | Verdict and reason |
|---|---|---|---|
| 0 | _Prompts on existing agents now_ | _UP-nn · SRF-nn · BF-01_ | _Keep / option / later / out (who)_ |
| 1 | _…_ | _…_ | _…_ |
| 2 | _…_ | _…_ | _…_ |

**Recommendation:** _release order, what stays out, what the brief must settle._

## G · Complexity flags · D4, D5

| Flag | Answer | Note |
|---|---|---|
| Personal data | _Yes / No / Unknown_ | _Where_ |
| Confidential content | | |
| Disconnected sources | | |
| Legal, privacy, works council | | |
| Countries and languages | | |
| Licensing | | |
| Dependencies (environment, stack ID, other teams) | | |

## H · Success · D1

| Item | Hypothesis (source) | Status | Owner / due |
|---|---|---|---|
| Must · What success looks like | _For this cycle, for the first release, for the next cycle_ | ☐ | |
| Must · Primary metric candidate | _One business metric (P11)_ | ☐ | |
| Later · Baseline | _Value today, or "none"_ | ☐ | |

## I · Wrap-up

| Decision | Agreed by, date |
|---|---|
| _…_ | _…_ |

| Open item | Owner | Due |
|---|---|---|
| _…_ | _…_ | _…_ |

| Gate | Input from this guide |
|---|---|
| Overlap check (design authority) | _Verdict proposed in D_ |
| ◆ Roadmap (steering) | _Recommendation in F; track to confirm at the brief_ |
| Next step | _Brief: scenario dossier 3.1, 3.2, 3.3; date; owners_ |

::: {.guide}
Within 48 hours of the workshop the product team (or the skill `update-workshop-guide` from the session transcript) sets each status, logs the decisions and open items, and sets `doc_status: Validated with the domain`.
:::
