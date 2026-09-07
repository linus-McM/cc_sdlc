---
description: Stage 4 Test — run the feedback loop, write the review against REVIEW.md, run continuous evals
argument-hint: run | review | evals  [--slug <slug>]
allowed-tools: Bash(python3 *), Bash(git *), Read, Write, Edit, Glob, Grep, Agent
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Arguments: $ARGUMENTS

## run
1. `sdlc test run` executes the test, lint and build commands from `.sdlc.toml` and writes `sdlc/<slug>/test-report.json`. It refuses when no red→green cycle was recorded.
2. On failure: fix the code, never the test; rerun. Paste the failing tail in your report.
3. Spawn the `sdlc:verifier` agent for a fresh-context check that the change matches plan.md. Report what it ran and saw.

## review
1. Read `REVIEW.md` at the repo root (copy `/templates/REVIEW.md` if absent) plus intent.md, spec.md, plan.md and `git diff main...HEAD`.
2. Spawn the `sdlc:reviewer` agent and write its findings to `sdlc/<slug>/review.md` with the three passes as headings `## Bugs`, `## Security`, `## Compliance`; each finding a bullet starting `Important:` or `Nit:` with `path:line`.
3. Address every Important finding with a red→green cycle (`/sdlc:build red|green`) and re-review. Cap nits at five.
4. `sdlc test review` validates the file and reports the counts. If a mistake was flagged for the second time, add the correction to CLAUDE.md in this commit.
5. Commit `sdlc/<slug>/test-report.json` and `review.md` as `test(<slug>): green + review`. Next: `/sdlc:deploy`.

## evals
`sdlc test evals` runs every `evals/*.json` (prompt, allowed_tools, checks) through `claude -p` and gates on `[evals] threshold`. Runs in CI on any change to CLAUDE.md, .claude/ or skills (template: `/templates/agent-evals.yml`). Add one eval per production incident.
