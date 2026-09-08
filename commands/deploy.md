---
description: Stage 5 Deploy — open the PR, tier the environments, rehearse rollback, hold the production gate
argument-hint: pr | check <env> | rehearse | record <env>  [--slug <slug>]
allowed-tools: Bash(python3 *), Bash(git *), Bash(gh *), Read, AskUserQuestion
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Arguments: $ARGUMENTS

## pr
`sdlc deploy pr` writes `sdlc/<slug>/pr-body.md` from the artifacts. Push the branch and `gh pr create --body-file sdlc/<slug>/pr-body.md`. The agent never pushes to main; branch protection and a code-owner approval close the PR. Babysit it: sweep unresolved review comments and failing checks, fix through red→green, push, until green and waiting only on approval.

## check <env>
`sdlc deploy check <env>` returns `decision`:
- `allow` (dev, or production with every gate satisfied): proceed with the deploy command.
- `ask` (staging): AskUserQuestion before running the deploy.
- `blocked`: quote every entry in `reasons` and stop. Never work around the gate. The Bash hook is a second line (matching rule in README "Guardrails"): while `RELEASE_APPROVAL` is unset it denies the release command for a gated environment; a hook denial is reported, never rewritten around.

## rehearse
`sdlc deploy rehearse` runs `deploy.rollback` from `.sdlc.toml` inside a throwaway detached git worktree of HEAD (the checkout, index and branch are untouched; a rollback that depends on uncommitted working-tree state will not see it) and records the result. Production is blocked until this has passed. The maintain stage calls the same rollback on a 3σ breach, so it must be proven here.

## record <env>
After the deploy command succeeds, `sdlc deploy record <env>` appends env, sha and approver to `sdlc/<slug>/deploy.json`; commit it as `deploy(<slug>): <env>`. Production → next `/sdlc:maintain`.
