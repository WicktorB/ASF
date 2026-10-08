---
mode: agent
description: Rebuild docs/portfolio.md tables from the scenario dossiers' canvas rows
---
Read every `scenarios/*/03-scenario-dossier.md`. For each, take the front-matter (status, track, owners, next gate) and the scenario canvas rows. Rebuild the tables in `docs/portfolio.md` (programme view, usage view, solution view, build view) from these rows only; keep IDs; mark a dossier whose `date` is older than 60 days as "Review". Open a PR titled `portfolio: weekly view`.
