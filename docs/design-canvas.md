---
title: Design canvas · five dimensions
part: Design canvas
version: v0.5
status: Proposed
owner: Design authority
---

# Design canvas · five dimensions

Every scenario is described along five dimensions. Each dimension is one decision, taken with the domain during Discovery and written in the scenario dossier. The order is the logic of the decisions (the job comes before the surface), not a sequence in time: the design process says when each one is taken.

This page is also the instruction set the Copilot skills follow. The rules are written so that a skill can apply them and an owner can check them.

## The five dimensions

| Dimension | Question it answers | Decision and output | Catalogue |
|---|---|---|---|
| D1 · Seller job and journey | What job, in which activity, for which persona, measured how? | Job in one sentence · seller activity · persona · primary metric | JM, P1, P10, P11 |
| D2 · Usage pattern | How does the seller interact with it, and what does the seller gain? | Usage pattern · its UI principle · seller benefit | UP, P8, P9 |
| D3 · Surface and build form | Where does the seller use it, in which format, and how is it built? | Surface and level of control · format · build form · justification if it is an agent | SRF, BF, P2, P3, P4 |
| D4 · Architecture and shared layers | What does it rely on, and what does it share with other scenarios? | Shared layers used · signals read or created · what it adds | LY, SC, P5 |
| D5 · Guardrails and safeguards | What must it never do, and how do we check what it did? | Boundary · guardrails and safeguards applied · confirmation and provenance design | GR, SG, P6, P7 |

## When each dimension is decided, and where it is written

| Dimension | Decided at | Drafted in | Reference version in |
|---|---|---|---|
| D1 | Intake (draft); workshop (confirmed) | Intake form; workshop guide A, B, H | Scenario brief 3.1 |
| D2 | Workshop | Workshop guide F | Scenario brief 3.1 (pattern); functional overview 3.2 (UI principle) |
| D3 | Surface in the workshop; build form at the brief | Workshop guide D, F | Functional overview 3.2 (surface, format); scenario brief 3.1 (build form) |
| D4 | Brief, with the architecture lead | Workshop guide E, G | Solution blueprint 3.3 |
| D5 | Boundary in the workshop; rules at the brief | Workshop guide C, G | Scenario brief 3.1 (boundary); 3.2 (confirmation, provenance); 3.3 (rules applied) |

## Rules a skill applies

**D1 · Seller job and journey**

- Write the job as one sentence a seller would say, starting with the outcome, not the tool.
- Pick exactly one seller activity from `catalogues/jm.yaml`; propose a new JM item only if none fits, and flag it as a change (CH).
- Name the persona as the catalogue does; one scenario, one primary persona.
- Propose one primary metric (P11), business not adoption, with its baseline when known. "No baseline" is an acceptable answer; an invented baseline is not.
- Apply P10: the scenario executes what the seller decided; a recommendation needs a method or a plan to compare against.

**D2 · Usage pattern**

- Pick the main usage pattern from `catalogues/up.yaml`; a second one only when the seller uses it differently in-year or on another path.
- Copy the UI principle of the pattern into 3.2 and state how the scenario applies it.
- State the seller benefit in the seller's terms (time, quality, fewer steps), not the system's.
- Apply P8 (every notification leads to an action) and P9 (infer, don't ask).

**D3 · Surface and build form**

- Surface first, then format, then build form (P3). Name the surface with its level of control from `catalogues/srf.yaml`.
- Start from the simplest build form that works (P4): BF-01 prompting, BF-02 configuration, BF-03 skill and tools (MCP) is the default; BF-04 agent only with its own trigger or identity (P2); BF-05 pro-code only for logic low-code cannot express.
- Write the justification for an agent in two lines: its trigger or identity, and what prompts or skills cannot carry.
- Check the surface constraints listed in the catalogue (for example SRF-03: instructions cannot be customised).

**D4 · Architecture and shared layers**

- Place the scenario in the target architecture: what it relies on (data sources, layers, signals, shared components) and what it adds. Anything new is justified against what exists.
- Reuse before building (P5): a new signal needs two committed consumers and an owner.
- Cite layers and components by ID from `catalogues/ly.yaml`. Say explicitly which layers are not used and why.

**D5 · Guardrails and safeguards**

- Write the boundary as a list of "never" statements the domain confirmed.
- Cite every guardrail and safeguard that applies from `catalogues/gr-sg.yaml`, each with how it is applied in this scenario. GR-01, GR-02, GR-05, SG-01, SG-02, SG-03 and SG-04 are checked before every design review.
- Show confirmation, provenance and "I don't know" in the screens (3.2) and in the rules (3.3), never only in prose.

## Before a design review

One status per dimension: Met, Partly, Not met.

- D1: the job is stated in one sentence, with activity, persona and primary metric.
- D2: the usage pattern is named, with its UI principle.
- D3: the surface is named with its level of control, and the build form is justified; an agent has its own trigger or identity.
- D4: the scenario is placed in the target architecture: what it relies on and what it adds; anything new is justified against what exists.
- D5: confirmation, access rights, provenance and "I don't know" behaviour are shown in the design.

This list is the first part of the checklist (template 4) and is maintained here only.

## Writing rules for every template

- One objective per section; three to five points per section; the rest goes to an annex or a linked file.
- Tables have at most four columns; a longer list becomes a second table or bullets.
- Decisions live in section 3.1 of the scenario dossier and are cited by ID in 3.2 and 3.3, never restated.
- Every value proposed by a skill carries its source in brackets: (intake), (intro call, 29 Sep), (workshop), (deck: Strategic Ambition.pptx). A value with no source is a question to the owner, not a fact.
- Status words: Validated, Proposed, Open, To confirm, Planned. Checks: Met, Partly, Not met.
- Names: the person's first name and role on first mention; the role afterwards.
