---
description: Stage 5 Deploy — open the PR, tier the environments, rehearse rollback, hold the production gate
argument-hint: pr | readiness <env> | check <env> | rehearse | record <env>  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Bash(gh *), Read, AskUserQuestion, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Do not read `sdlc/knowledge/index.md` for these mechanics; the artifacts carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc deploy pr` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

## pr
`sdlc deploy pr` writes `sdlc/<slug>/pr-body.md` from the artifacts, including a Knowledge section with the `sdlc/knowledge/` diff against main. Push the branch and `gh pr create --body-file sdlc/<slug>/pr-body.md`. The agent never pushes to main; branch protection and a code-owner approval close the PR. Babysit it: sweep unresolved review comments and failing checks, fix through red→green, push, until green and waiting only on approval.

## readiness <env>
Before `check` for staging or production, run `sdlc:release-readiness` with `{slug, env}`: PR reviews and CI, rollback scope, PR body against the diff and rollout ordering are checked in parallel. Fix every `blockers` entry (through red→green when it is code) and list `warnings` in the approval question. `ready: true` is advice only; `sdlc deploy check` is the gate.

## check <env>
`sdlc deploy check <env>` returns `decision`:
- `allow` (dev, or production with every gate satisfied): proceed with the deploy command.
- `ask` (staging): AskUserQuestion before running the deploy.
- `blocked`: quote every entry in `reasons` and stop. Never work around the gate. The Bash hook is a second line (matching rule in README "Guardrails"): while `RELEASE_APPROVAL` is unset it denies the release command for a gated environment; a hook denial is reported, never rewritten around.

## rehearse
`sdlc deploy rehearse` runs `deploy.rollback` from `.sdlc.toml` inside a throwaway detached git worktree of HEAD and records the result. Only the checked-out files, index and current branch are isolated: pushes, tags, other branches and anything outside git (`kubectl`, `gh`) run for real (README, "Rollback rehearsal"), so rehearse in staging with a rollback command scoped to what a rehearsal may touch. Production is blocked until this has passed; the maintain stage calls the same rollback on a 3σ breach.

## docs  (the stage document; required before `deploy record`)
`sdlc docs draft deploy` writes the Archify source from pr-body.md and the `[deploy]` table; then `sdlc docs render deploy` and `sdlc docs open deploy`. Only when the draft is refused, follow the `recipe` in `sdlc docs check deploy`'s verdict.

## record <env>
After the deploy command succeeds (and `sdlc docs open deploy` has shown the document; `record` is refused until `docs/deploy.html` is fresh), `sdlc deploy record <env>` appends env, sha and approver to `sdlc/<slug>/deploy.json` and commits it as `deploy(<slug>): record <env> — deploy.json`. Production: the boundary wrote HANDOVER.md; `/clear`, then `/sdlc:maintain`.
