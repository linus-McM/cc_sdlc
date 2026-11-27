---
description: Stage 4 Test — run the feedback loop, review the diff against the approved plan and REVIEW.md, and close the loop
argument-hint: run | review | evals  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Read, Write, Edit, Glob, Grep, AskUserQuestion, Agent, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Do not read `sdlc/knowledge/index.md` for these mechanics; the artifacts and the pack carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc test run` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

## run
1. `sdlc test run` executes the test, lint and build commands from `.sdlc.toml`, then `knowledge check` (OKF v0.2 conformance of `sdlc/knowledge/`; policy and trust findings are reported, only conformance fails), and writes `sdlc/<slug>/test-report.json`. It refuses when no red→green cycle was recorded, when a plan.md step has no cycle under its number (`missing`), and when a file plan.md lists was never changed since the approval (`untouched`): build the step or the file, or take it out of plan.md. It reports `deviations` from the approved plan and copies the template `REVIEW.md` to the repo root when there is none. On pass it adds a `process:sdlc-test` verification event to the feature concept.
2. On failure: fix the code, never the test; rerun. Paste the failing tail in your report.
3. Spawn the `sdlc:verifier` agent for a fresh-context check that the change matches plan.md. Report what it ran and saw.

## review
1. `sdlc knowledge pack test` packs every file the branch changed plus one graph hop; state any `skipped` or budget step-down in one line.
2. With workflows: run `sdlc:review` with `{slug, base: "main", pack}` (`pack` = the verdict's `path`) and write its `markdown` to `sdlc/<slug>/review.md` as is. Do not read REVIEW.md, the artifacts or the diff yourself: its agents do (three passes in parallel, two skeptics per Important finding and one per Nit, nits capped at five). Without workflows: spawn the `sdlc:reviewer` agent and write its markdown there as is. Either way the Compliance section carries one line per spec.md requirement: `- R<n>: met, <test or path:line that proves it>`, or an `Important:` finding that names the `R<n>` the diff does not deliver.
3. Fix every Important finding with a red→green cycle (`/sdlc:build red|green`), then end its line in review.md with `fixed: <commit>`. A finding the user decides to leave ends with `wontfix: <reason>`: ask them (AskUserQuestion), never decide it for them. `sdlc test review` is refused while an Important line has neither.
4. `sdlc test review` validates the file, refuses while a requirement has no verdict in Compliance (`missing`), and reports the counts, any `deviations` from the approved plan and the context pack under `pack` (it rebuilds the pack when HEAD moved; a pack problem is reported, and only a changed file excluded as a secret refuses the review). If a mistake was flagged for the second time, add the correction to CLAUDE.md in this commit.
5. `review` commits `sdlc/<slug>/review.md`, `test-report.json` and the stage's other output as `test(<slug>): review — review.md` and returns `complete: true`. The loop ends here. Tell the user the feature is complete: the requirement verdicts, the finding counts and every deviation from the approved plan. `/sdlc:deploy` and `/sdlc:maintain` are optional; run them only when the user asks.

## docs  (the stage document; on demand)
Only when the user asks for the test document. Read review.md and test-report.json: the exchange between `test run`, the verifier agent and the reviewer agent, with the finding counts and the red/green fixes as returns. Follow the `recipe` in `sdlc docs check test`'s verdict, then `sdlc docs render test` and `sdlc docs open test`.

## evals
`sdlc test evals` runs every `evals/*.json` (prompt, allowed_tools, checks) through `claude -p` and gates on `[evals] threshold`. Runs in CI on any change to CLAUDE.md, .claude/ or skills (template: `/templates/agent-evals.yml`). Add one eval per production incident.
