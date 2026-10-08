---
title: "Set-up guide · repository, Word generation and Copilot skills"
part: Ways of working
version: 0.4
doc_status: Proposed
owner: Technical design
date: 2026-10-08
---

::: {.readme}
**In 30 seconds.** Step-by-step instructions to set up the ASF Design Framework repository: create it, protect it, connect Copilot, generate Word, publish to SharePoint, migrate the content, pilot the skills, open it to the POs. Each step says who does it, how, and how to check it worked. Run the steps in order; a step that fails has a fallback.
:::

# Before you start

Four decisions, taken by the task force before step 1.

| Decision | Proposed |
|---|---|
| Owner of the repository and the build | Technical design |
| How POs work in the repository | Through issues and pull request reviews on github.com; no IDE, no Git commands |
| ISD scenarios | In the same repository, one folder per scenario |
| Transcripts and meeting notes | In the repository only if it is private and access-controlled and legal agrees; otherwise in the SharePoint library, referenced by link |

Access you need for the set-up:

- Admin rights on a repository in the Schneider GitHub Enterprise organisation (or a GitHub admin who can act for you).
- A Copilot Business or Enterprise seat for yourself.
- Python 3.12, Node 20, `pandoc` 3.x and VS Code on your machine.
- The repository content: `asf-design-framework-repo.zip`.

# Step 1 · Confirm the platform

Who: technical design, with the GitHub admin and the M365 admin.

1. Ask the GitHub admin to confirm, in writing, four settings on the organisation:
   - Private repositories can be created under the ASF programme.
   - GitHub Copilot is enabled for the organisation, with seats for the product team and the POs.
   - The policy "Copilot coding agent" is enabled (organisation settings → Copilot → Policies).
   - GitHub Actions is allowed, with GitHub-hosted runners or a self-hosted runner that can install `pandoc` and Node.
2. Ask the M365 admin for a SharePoint library "ASF Design Framework" on the ASF programme site, and for one way to write into it from GitHub: an Entra ID app registration with `Sites.Selected` on that site, or a Power Automate flow with an HTTP trigger.
3. Ask Fernanda for the list of POs and their GitHub accounts.

Check: the four GitHub settings and one SharePoint write path are confirmed.

Fallback: no coding agent → the product team runs the skills in VS Code agent mode on behalf of the POs. No Actions → the build is run locally by technical design. No SharePoint write path → the Word files are uploaded by hand at each release.

# Step 2 · Create the repository

Who: technical design.

1. On github.com, in the Schneider organisation: New repository → name `asf-design-framework` → Private → no README (the zip has one).
2. On your machine:

   ```bash
   unzip asf-design-framework-repo.zip
   cd asf-design-framework
   git init -b main
   git add .
   git commit -m "Initial content: pack v0.5, templates, catalogues, One Plan Segment"
   git remote add origin https://github.com/<org>/asf-design-framework.git
   git push -u origin main
   ```

3. In the repository settings → General: enable Issues; disable Wiki and Projects (not used); set "Automatically delete head branches".

Check: the repository shows `docs/`, `catalogues/`, `templates/`, `scenarios/`, `build/`, `.github/`.

# Step 3 · Protect `main` and give access

Who: technical design.

1. Settings → Collaborators and teams: give the product team and the POs the Write role on the repository.
2. Settings → Branches → Add a ruleset for `main`:
   - Require a pull request before merging, with 1 approval.
   - Require status checks to pass: `build`.
   - Block force pushes and deletions.

Check: a direct push to `main` is refused; a PR can be merged after one approval and a green build.

Who approves which PR is agreed by convention for now: the design authority for `docs/` and `catalogues/`, the PO for their scenario folder, technical design for `build/` and `.github/`. Enforcing it in GitHub comes later (see "Later").

# Step 4 · Build the Word and HTML outputs

Who: technical design.

1. Install the tools locally:

   ```bash
   pip install python-docx pyyaml
   npm install -g @mermaid-js/mermaid-cli
   ```

2. Apply the Schneider brand: open `build/make_reference.py`, set `FONT` and the `PALETTE` values to the brand's font and colours, then run:

   ```bash
   python build/make_reference.py
   python build/build.py
   ```

3. Open `dist/scenarios/one-plan-segment/03-scenario-dossier.docx` in Word 365. Check the cover lines, the "In 30 seconds" box, the coloured D1 to D5 rows, the two diagrams and the footer.
4. Run `python build/build.py --final templates` and check that the grey guide boxes are gone in `*-final.docx`.
5. Commit the updated `build/reference.docx` through a PR.

Check: UX validates the look of the dossier in Word.

If `mmdc` fails: set the browser path with `export MMDC_CHROME=/path/to/chrome`. Without it, diagrams stay as code blocks in Word; the build does not fail.

# Step 5 · Turn on the CI build

Who: technical design.

1. The workflow is in `.github/workflows/build-docs.yml`. It runs on every pull request and on every push to `main`, builds `dist/`, and attaches it to the run as an artifact named `dist`.
2. Open a PR that changes one line in `templates/01-intake-form.md`. In the PR → Checks → `build` → Summary → download `dist`. Open the intake Word.
3. Add the job name `build` to the required checks of the ruleset (step 3) if not already there.

Check: every PR shows a green `build` check and a downloadable `dist`.

# Step 6 · Publish to SharePoint

Who: technical design, with the M365 admin.

Option A · app registration (preferred):

1. The M365 admin creates an Entra ID app registration, grants `Sites.Selected`, and grants the app write access to the ASF programme site only.
2. Store three repository secrets (Settings → Secrets and variables → Actions): `SP_TENANT_ID`, `SP_CLIENT_ID`, `SP_CLIENT_SECRET`; and two variables: `SP_SITE` (site URL), `SP_LIBRARY` (`ASF Design Framework`).
3. Add `build/publish_sharepoint.py` (to write: it uploads every file of `dist/` to the library, keeping the folder structure, using the Microsoft Graph upload API) and uncomment the publish step in the workflow, restricted to pushes on `main`.

Option B · Power Automate:

1. Create a flow "When an HTTP request is received" → for each file in the request → "Create file" in the library, overwrite on.
2. Store the flow URL as the secret `SP_FLOW_URL`; add a workflow step that zips `dist/` and posts it to the flow.

Check: merge a small change on `main`; within the hour the Word file in the SharePoint library shows the new version, with version history.

# Step 7 · Connect Copilot to the repository

Who: technical design.

1. Open the repository in VS Code with the GitHub Copilot extension signed in with the Schneider account.
2. In Copilot Chat, ask: "Which rules apply to this repository?" Copilot must quote the rules of `.github/copilot-instructions.md` (IDs never invented, sources in brackets, decisions in 3.1).
3. Ask: "List the skills available in this repository." Copilot must list the seven skills of `.github/skills/`.
4. On github.com, open the repository → Settings → Copilot → coding agent: check the agent is allowed on this repository. Add `pandoc` and the Python packages to the agent's set-up steps (file `.github/workflows/copilot-setup-steps.yml`) so it can run the build itself.

Check: Copilot quotes the rules and lists the skills; the coding agent appears as an assignee on issues.

# Step 8 · Add issue templates

Who: technical design.

Issue templates turn each Discovery step into a form a PO fills on github.com; assigning the issue to Copilot starts the matching skill.

1. Check the five templates in `.github/ISSUE_TEMPLATE/`: `new-scenario.yml`, `prefill-guide.yml`, `update-guide.yml`, `draft-dossier.yml`, `check-dossier.yml`. Each asks for the scenario slug and the inputs, and names the skill to run.
2. On github.com → New issue: the five forms appear.
3. Test: create a "check dossier" issue for `one-plan-segment`, assign it to Copilot. Copilot opens a PR that updates `scenarios/one-plan-segment/04-checklist.md`.

Check: the PR arrives without any prompt typed by hand, and its description lists what was checked and what could not be sourced.

# Step 9 · Migrate the rest of the pack

Who: framework owner, with technical design.

1. Freeze the HTML pack: announce that from now on every change goes to the repository. Put a banner on the HTML pack pointing to the SharePoint library.
2. For each page still in HTML (Start here, Why, Design process, Portfolio views, Ways of working, Deployment, Glossary), create `docs/<page>.md` with front-matter (`title`, `part`, `version`, `status`, `owner`). One PR per page; the design authority reviews.
3. Catalogue pages: do not rewrite them by hand. Add a small script `build/catalogues_to_md.py` that renders each `catalogues/*.yaml` into `docs/catalogues/<id>.md` before the build, so the YAML stays the only source.
4. Diagrams of the pack: rewrite them as Mermaid where they show a flow; keep the canvas drawing as an SVG file in `docs/img/`.

Check: the HTML pack is no longer edited; every page has a Word and HTML version in `dist/docs/`.

# Step 10 · Pilot the skills on known material

Who: framing lead and technical design.

1. Retro on One Plan Segment: create a "check dossier" issue, let Copilot run `check-design-review`, compare its checklist with the hand-made one. List every difference.
2. Prefill on a past scenario: put the intro call transcript and the domain's decks of a scenario already framed (post-meeting or competitor intelligence) in `scenarios/<slug>/inputs/`, run `prefill-workshop-guide`, compare with the guide used at the time.
3. For each difference, decide: fix the skill (procedure), fix the canvas (`docs/design-canvas.md`, the rule), or accept. Log rule changes as CH items in `catalogues/changes.yaml`.
4. Record three measures: time from transcript to prefilled guide; lines without a source; review comments per PR.

Check: the framing lead judges the prefill usable, and every line carries a source.

# Step 11 · Onboard the POs

Who: documentation and training stream, with the framing lead.

1. Write "How to work in the repository" (two pages, in `docs/`): open an issue from a form, follow the PR, read the Word attached by the build, comment on a line, approve. Screenshots from github.com only.
2. Run a one-hour PO session on One Plan Segment: each PO opens one issue and approves one PR.
3. Hold the PO session every two weeks for questions and lessons learned.

Check: every PO has opened one issue and approved one PR.

# Step 12 · Run one new scenario end to end

Who: framing lead and the PO of the scenario.

1. The domain states its need with the intake assistant; the validated text version goes into a "new scenario" issue.
2. Copilot runs `new-scenario`: folder created, intake A and B pasted, C to E drafted. The framing lead reviews the PR.
3. After the intro call, the transcript goes to `inputs/`; "prefill guide" issue → `prefill-workshop-guide`. The framing lead reviews before the workshop.
4. After the workshop, the transcript goes to `inputs/`; "update guide" issue → `update-workshop-guide`. Reviewed within 48 hours.
5. "Draft dossier" issue → `draft-scenario-dossier`. The PO, UX and architecture lead each review their section in the same PR.
6. "Check dossier" issue → `check-design-review`. The design authority reviews and gives the verdict.
7. At Go build: `generate-extract` for the BRD, high-level architecture and backlog.

Check: the scenario reaches the design review with every file in the repository and every Word generated.

# Step 13 · Hand over

Who: Fernanda, technical design, design authority.

1. Write the ownership in the Ways of working page: repository and build (technical design), `docs/` and `catalogues/` (design authority), templates (framework owner), each scenario (its PO).
2. Apply the validated CH items with `apply-change`; tag the release (`git tag v1.0`, `git push --tags`); check the SharePoint library is updated.
3. Schedule the weekly portfolio view: run the prompt `weekly-portfolio-view` each week (by hand, or from a scheduled workflow).
4. Record the PO session (20 minutes) and store it with the two-pager in the SharePoint library.

Check: a person who did not set up the repository can run steps 4, 7 and 12 from this guide alone.

# Rules from the first commit

- No direct push to `main`; one PR per scenario step, approved by the owner agreed for that folder.
- Branch names: `<scenario>-<update>-<version>` for scenario work (for example `one-plan-segment-dossier-v0.2`), `docs/<page>` for the pack, `catalogue/<id>` for a catalogue. Details below.
- Inputs go to `scenarios/<slug>/inputs/` before a skill runs; a skill never works from the team's own outputs.
- `dist/` is built by CI, never committed by hand.
- Copilot conversations are not archived: the PR is the record.
- The PR description lists what was drafted, what could not be sourced, which CH items were raised.

# Branch names

A scenario branch is named `<scenario>-<update>-<version>`: lower case, words separated by hyphens, no slash.

| Part | Is | Example |
|---|---|---|
| `<scenario>` | The scenario slug, as the folder name under `scenarios/` | `one-plan-segment` |
| `<update>` | The file the branch changes: `intake`, `guide`, `dossier`, `checklist` or `extract` | `dossier` |
| `<version>` | The version the file reaches in its front-matter, prefixed with `v` | `v0.2` |

- One branch and one PR per scenario, per update and per version: `one-plan-segment-guide-v0.2`, then `one-plan-segment-dossier-v0.1`.
- The version is the one written in the front-matter of the file when the PR is merged (minor bump for a content change).
- Branches for `docs/` and `catalogues/` keep their own form: `docs/<page>`, `catalogue/<id>`.
- Branches opened by the Copilot coding agent are named by Copilot (`copilot/…`) and are not renamed; the PR title says which scenario and update it covers.

# Later

- **Enforce who approves what (CODEOWNERS).** A file `.github/CODEOWNERS` maps each folder to the GitHub group that must approve its changes (design authority for `docs/` and `catalogues/`, the PO for each scenario), and the ruleset adds "Require review from Code Owners". Set it up once the design authority members are named, with at least two members to avoid a bottleneck.
