---
description: Stage 6 Maintain — deterministic control bands watch production and close the loop by writing the next intent.md
argument-hint: watch [metric] | propose <metric> | ingest <metric> --value <v> | lesson "<text>"
allowed-tools: Bash(uv run *), Bash(git *), Bash(gh *), Read, Write, Grep, Glob, Agent, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Do not read `sdlc/knowledge/index.md` for these mechanics; the pack and `sdlc/lessons.md` carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate maintain`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

Arguments: $ARGUMENTS

Readings live in `sdlc/metrics.jsonl` (one `{"metric","value","ts"}` per line, fed by `sdlc maintain ingest` from CI or a webhook). Bands live in `sdlc/bands.toml` (template: `/templates/bands.toml`); set `bad = "high"` or `"low"` per metric so an improvement never counts as a breach. Detection is pure Python (Western Electric rules on a rolling baseline); no model decides whether a band was breached. `sdlc knowledge refresh` appends `knowledge_nodes`, `knowledge_communities`, `knowledge_stale`, `knowledge_unverified` and `knowledge_behind` readings, so the `knowledge_stale` and `knowledge_behind` bands (template) watch index freshness like any production signal.

## watch
`sdlc maintain watch` reports a tier and action per metric:
- `log` (1σ): note it, do nothing.
- `diagnose` (2σ): read-only diagnosis. Run `sdlc knowledge pack maintain --slug <last released feature>` (advisory: the files changed since its production deploy) and then `sdlc:diagnose` with `{metric, pack}` (`pack` omitted when skipped): lessons, deploys, CI runs and the metric trend are swept in parallel, two skeptics try to refute each hypothesis, and it returns a three-line `sitrep`. Without workflows, read `sdlc/lessons.md` first for prior hypotheses, then logs and recent deploys (`gh run list`, `git log`) and write the SITREP yourself. Change nothing.
- `propose` (3σ): run `propose <metric>`.

## docs  (the bands document; never gates a watch)
Read `sdlc/bands.toml`: one state per tier (`log`, `diagnose`, `propose`) and the action each triggers, the rehearsed rollback as the recoverable failure. Follow the `recipe` in `sdlc docs check maintain`'s verdict, then `sdlc docs render maintain`. `sdlc maintain watch` carries `docs` with the reason while the document is missing or behind `sdlc/bands.toml`; regenerate it when bands change.

## propose <metric>
`sdlc maintain propose <metric>` writes `sdlc/<slug>/intent.md` (Risk: high) with the evidence, commits it as `maintain(<slug>): propose — intent.md`, and returns to `/sdlc:plan`. Complete the remaining sections from the diagnosis, then either open a PR through `/sdlc:build` or trigger the rehearsed rollback (`deploy.rollback`) when a deployment sits in the breach window. Never act beyond a PR or a pre-approved runbook; the on-call engineer triages: fix now, schedule, or dismiss (dismissals tune `bands.toml`).

## lesson "<text>"
`sdlc maintain lesson "<root cause; fix; gotcha>"` appends to `sdlc/lessons.md` and commits it as `maintain: lesson — lessons.md`. Write one after every incident, add an eval under `evals/` for the incident class, and when a lesson recurs promote it into CLAUDE.md.
