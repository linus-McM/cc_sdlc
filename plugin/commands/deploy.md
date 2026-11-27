---
description: Stage 5 Deploy (optional, after the loop is complete) — open the PR, tier the environments, rehearse rollback, record releases
argument-hint: pr | readiness <env> | check <env> | rehearse | record <env>  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Bash(gh *), Read, AskUserQuestion, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Do not read `sdlc/knowledge/index.md` for these mechanics; the artifacts carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc deploy pr` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

The loop is complete once `sdlc test review` passes. This stage is a secondary flow: run it only when the user asks for a PR or a release.

## pr
`sdlc deploy pr` writes `sdlc/<slug>/pr-body.md` from the artifacts, including the deviations from the approved plan and a Knowledge section with the `sdlc/knowledge/` diff against main. Push the branch and `gh pr create --body-file sdlc/<slug>/pr-body.md`. The agent never pushes to main; branch protection closes the PR. Babysit it: sweep unresolved review comments and failing checks, fix through red→green, push, until green and waiting only on review.

## readiness <env>
Before `check` for staging or production, when `workflow.run` is true, run `sdlc:release-readiness` with `{slug, env}`: PR reviews and CI, rollback scope, PR body against the diff and rollout ordering are checked in parallel. Fix every `blockers` entry (through red→green when it is code) and list `warnings` in the question you ask before the release. `ready: true` is advice only; `sdlc deploy check` is the gate.

## check <env>
`sdlc deploy check <env>` returns `decision`:
- `allow` (the `free` tier: dev): proceed with the deploy command.
- `ask` (the `ask` tier: staging; and the `gate` tier: production, once the rollback is configured and rehearsed): AskUserQuestion before running the deploy.
- `blocked`: quote every entry in `reasons` and stop. A feature is blocked for every environment until its test report passes and review.md has no open Important finding. Never work around the gate. The Bash hook is a second line (matching rule in README "Guardrails"): it puts a release command for a gated environment to the user as a permission prompt; never rewrite a command to get past it.

## rehearse
`sdlc deploy rehearse` runs `deploy.rollback` from `.sdlc.toml` inside a throwaway detached git worktree of HEAD and records the result. Only the checked-out files, index and current branch are isolated: pushes, tags, other branches and anything outside git (`kubectl`, `gh`) run for real (README, "Rollback rehearsal"), so rehearse in staging with a rollback command scoped to what a rehearsal may touch. Production is blocked until this has passed; the maintain stage calls the same rollback on a 3σ breach.

## docs  (the stage document; on demand)
Only when the user asks for the deploy document. `sdlc docs draft deploy` writes the Archify source from pr-body.md and the `[deploy]` table; then `sdlc docs render deploy` and `sdlc docs open deploy`. Only when the draft is refused, follow the `recipe` in `sdlc docs check deploy`'s verdict.

## record <env>
After the deploy command succeeds, `sdlc deploy record <env>` appends env, date and sha to `sdlc/<slug>/deploy.json` and commits it as `deploy(<slug>): record <env> — deploy.json`. After production, `/sdlc:maintain` is available when the user wants the control bands watched.
