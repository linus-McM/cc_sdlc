---
description: Stage 5 Deploy — open the PR, tier the environments, rehearse rollback, hold the production gate
argument-hint: pr | readiness <env> | check <env> | rehearse | record <env>  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Bash(gh *), Read, AskUserQuestion, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Do not read `sdlc/knowledge/index.md` for these mechanics; the artifacts carry the context. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate deploy`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

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
`sdlc deploy rehearse` runs `deploy.rollback` from `.sdlc.toml` inside a throwaway detached git worktree of HEAD, at the project's own path within the repository, and records the result. Isolated: the checked-out files, index and current branch. Not isolated: the shared object store, tags, other branches, remotes (`git push`, `git tag`, `git branch -f`) and anything outside git (`kubectl`, `gh`), which all run for real; commits the rehearsal makes become dangling objects that git's own gc prunes. A worktree that cannot be removed is reported with its path after the result is recorded. Rehearse in staging with a rollback command scoped to what a rehearsal may touch. Production is blocked until this has passed. The maintain stage calls the same rollback on a 3σ breach, so it must be proven here.

## docs  (the stage document; required before `deploy record`)
Read pr-body.md and the `[deploy]` table of `.sdlc.toml`: one state per environment tier (`free`, `ask`, `gate`), the PR and `RELEASE_APPROVAL` as gates, the rehearsed rollback as the recoverable failure back to the previous release. Follow the `recipe` in `sdlc docs check deploy`'s verdict, then `sdlc docs render deploy` and `sdlc docs open deploy`.

## record <env>
After the deploy command succeeds (and `sdlc docs open deploy` has shown the document; `record` is refused until `docs/deploy.html` is fresh), `sdlc deploy record <env>` appends env, sha and approver to `sdlc/<slug>/deploy.json` and commits it as `deploy(<slug>): record <env> — deploy.json`. Production: the boundary wrote HANDOVER.md; `/clear`, then `/sdlc:maintain`.
