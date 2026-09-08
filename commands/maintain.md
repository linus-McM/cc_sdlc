---
description: Stage 6 Maintain — deterministic control bands watch production and close the loop by writing the next intent.md
argument-hint: watch [metric] | propose <metric> | ingest <metric> --value <v> | lesson "<text>"
allowed-tools: Bash(python3 *), Bash(git *), Bash(gh *), Read, Write, Grep, Glob, Agent
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Arguments: $ARGUMENTS

Readings live in `sdlc/metrics.jsonl` (one `{"metric","value","ts"}` per line, fed by `sdlc maintain ingest` from CI or a webhook). Bands live in `sdlc/bands.toml` (template: `/templates/bands.toml`); set `bad = "high"` or `"low"` per metric so an improvement never counts as a breach. Detection is pure Python (Western Electric rules on a rolling baseline); no model decides whether a band was breached.

## watch
`sdlc maintain watch` reports a tier and action per metric:
- `log` (1σ): note it, do nothing.
- `diagnose` (2σ): read-only diagnosis. Read `sdlc/lessons.md` first for prior hypotheses, then logs and recent deploys (`gh run list`, `git log`). Write a three-line SITREP. Change nothing.
- `propose` (3σ): run `propose <metric>`.

## propose <metric>
`sdlc maintain propose <metric>` writes `sdlc/<slug>/intent.md` (Risk: high) with the evidence and returns to `/sdlc:plan`. Complete the remaining sections from the diagnosis, then either open a PR through `/sdlc:build` or trigger the rehearsed rollback (`deploy.rollback`) when a deployment sits in the breach window. Never act beyond a PR or a pre-approved runbook; the on-call engineer triages: fix now, schedule, or dismiss (dismissals tune `bands.toml`).

## lesson "<text>"
`sdlc maintain lesson "<root cause; fix; gotcha>"` appends to `sdlc/lessons.md`. Write one after every incident, add an eval under `evals/` for the incident class, and when a lesson recurs promote it into CLAUDE.md.
