---
description: Stage 4 Test — run the feedback loop, write the review against REVIEW.md, run continuous evals
argument-hint: run | review | evals  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Read, Write, Edit, Glob, Grep, Agent, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Do not read `sdlc/knowledge/index.md` for these mechanics; the artifacts and the pack carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate test`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

Arguments: $ARGUMENTS

## run
1. `sdlc test run` executes the test, lint and build commands from `.sdlc.toml`, then `knowledge check` (OKF v0.2 conformance of `sdlc/knowledge/`; policy and trust findings are reported, only conformance fails), and writes `sdlc/<slug>/test-report.json`. It refuses when no red→green cycle was recorded. On pass it adds a `process:sdlc-test` verification event to the feature concept.
2. On failure: fix the code, never the test; rerun. Paste the failing tail in your report.
3. Spawn the `sdlc:verifier` agent for a fresh-context check that the change matches plan.md. Report what it ran and saw.

## review
1. Read `REVIEW.md` at the repo root (copy `/templates/REVIEW.md` if absent) plus intent.md, spec.md, plan.md and `git diff main...HEAD`.
2. `sdlc knowledge pack test` packs every file the branch changed plus one graph hop; state any `skipped` or budget step-down in one line. Run `sdlc:review` with `{slug, base: "main", pack}` (`pack` = the verdict's `path`): three passes in parallel, two skeptics per finding (one refutation downgrades to Nit, two drop it), nits capped at five. Write its `markdown` to `sdlc/<slug>/review.md` as is. Without workflows, spawn the `sdlc:reviewer` agent and write its findings there with the three passes as headings `## Bugs`, `## Security`, `## Compliance`; each finding a bullet starting `Important:` or `Nit:` with `path:line`.
3. Address every Important finding with a red→green cycle (`/sdlc:build red|green`) and re-review. Cap nits at five.
4. The docs step below, then `sdlc docs open test`. Immediately before review, rebuild the pack at HEAD with `sdlc knowledge pack test` (fixes committed in step 3 moved HEAD); `sdlc test review` refuses a pack that is not at HEAD or misses a changed file (`missing`). `sdlc test review` validates the file, requires a fresh `docs/test.html`, and reports the counts. If a mistake was flagged for the second time, add the correction to CLAUDE.md in this commit.
5. `review` commits `sdlc/<slug>/review.md`, `test-report.json` and the stage's other output as `test(<slug>): review — review.md`. Next: the boundary wrote HANDOVER.md; `/clear`, then `/sdlc:deploy`.

## docs  (the stage document; required before `test review`)
Read review.md and test-report.json: the exchange between `test run`, the verifier agent, the reviewer agent and the engineer, with the finding counts and the red/green fixes as returns. Follow the `recipe` in `sdlc docs check test`'s verdict, then `sdlc docs render test` and `sdlc docs open test`.

## evals
`sdlc test evals` runs every `evals/*.json` (prompt, allowed_tools, checks) through `claude -p` and gates on `[evals] threshold`. Runs in CI on any change to CLAUDE.md, .claude/ or skills (template: `/templates/agent-evals.yml`). Add one eval per production incident.
