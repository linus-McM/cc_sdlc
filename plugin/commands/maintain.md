---
description: Stage 6 Maintain (optional) — deterministic control bands watch production and write the next intent.md on a breach
argument-hint: watch [metric] | propose <metric> | ingest <metric> --value <v> | lesson "<text>"
allowed-tools: Bash(uv run *), Bash(git *), Bash(gh *), Read, Write, Grep, Glob, Agent, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Do not read `sdlc/knowledge/index.md` for these mechanics; the pack and `sdlc/lessons.md` carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc maintain watch` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

This stage is a secondary flow outside the plan, design, build, test loop: run it only when the user asks.

Readings are in `sdlc/metrics.jsonl` (fed by `sdlc maintain ingest`), bands in `sdlc/bands.toml` (template: `/templates/bands.toml`; formats in README, "Readings and bands"). Detection is pure Python: no model decides whether a band was breached.

## watch
`sdlc maintain watch` reports a tier and action per metric:
- `log` (1σ): note it, do nothing.
- `diagnose` (2σ): read-only diagnosis. Run `sdlc knowledge pack maintain --slug <last released feature>` (advisory: the files changed since its production deploy) and then `sdlc:diagnose` with `{metric, pack}` (`pack` omitted when skipped): lessons, deploys, CI runs and the metric trend are swept in parallel, two skeptics try to refute each hypothesis, and it returns a three-line `sitrep`. Without workflows, read `sdlc/lessons.md` first for prior hypotheses, then logs and recent deploys (`gh run list`, `git log`) and write the SITREP yourself. Change nothing.
- `propose` (3σ): run `propose <metric>`.

## docs  (the bands document; never gates a watch)
`sdlc docs draft maintain` writes the Archify source from `sdlc/bands.toml`; then `sdlc docs render maintain`. Only when the draft is refused, follow the `recipe` in `sdlc docs check maintain`'s verdict. `sdlc maintain watch` carries `docs` with the reason while the document is missing or behind `sdlc/bands.toml`; regenerate it when bands change.

## propose <metric>
`sdlc maintain propose <metric>` writes `sdlc/<slug>/intent.md` with the evidence, commits it as `maintain(<slug>): propose — intent.md`, and returns to `/sdlc:plan`. Complete the remaining sections from the diagnosis, then either take it through the loop from `/sdlc:plan check` or, when a deployment sits in the breach window, ask the user before triggering the rehearsed rollback (`deploy.rollback`). Never act beyond a PR or a pre-approved runbook; the user decides: fix now, schedule, or dismiss (dismissals tune `bands.toml`).

## lesson "<text>"
`sdlc maintain lesson "<root cause; fix; gotcha>"` appends to `sdlc/lessons.md` and commits it as `maintain: lesson — lessons.md`. Write one after every incident, add an eval under `evals/` for the incident class, and when a lesson recurs promote it into CLAUDE.md.
