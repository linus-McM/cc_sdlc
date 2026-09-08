---
description: Stage 1 Plan — capture an idea, ticket or incident as intent.md; the product owner accepts it
argument-hint: new "<title>" | check | accept | status  [--slug <slug>]
allowed-tools: Bash(python3 *), Read, Edit, Write, AskUserQuestion
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge first: run `sdlc knowledge bootstrap` (idempotent; on first use installs uv, Graphify, its Claude skill and git hooks, then builds `graphify-out/` and the OKF bundle `sdlc/knowledge/`), then read `sdlc/knowledge/index.md` and follow its links only as deep as the task needs. For call-graph questions (what calls what, blast radius of a change) run `graphify query "<question>"` or `graphify affected "<symbol>"` before grepping; EXTRACTED edges are parsed facts, INFERRED edges are hints. Never write a `human:` entry into a concept's `verified` list: only `accept` publishes. `sdlc knowledge status` says how far each index is behind HEAD.

Arguments: $ARGUMENTS

## new "<title>"
1. `sdlc plan new "<title>"` creates `sdlc/<slug>/intent.md` from the template and `.sdlc.toml` if missing.
2. Interview the originator until concrete: what cannot be done today, who is affected, what better looks like, what is out of scope, constraints, success measure. Plain words; no formal language required.
3. Write the answers into every section of intent.md. Set `Risk: high` when the change touches auth, PII, payments, migrations or infra.
4. `sdlc plan check`. Fix every listed problem, re-run until `ok`.
5. Show the originator the file and ask them to correct anything misunderstood.

## check
`sdlc plan check` and report the verdict.

## accept
Only a human accepts. Ask (AskUserQuestion) the product owner to confirm the intent is correct and in scope; on yes run `sdlc plan accept` (it also publishes `sdlc/knowledge/features/<slug>.md` with a `human:<author>` verification event and `status: stable`), then commit `sdlc/<slug>/intent.md` and `sdlc/knowledge/` with message `plan(<slug>): accept intent`. Next: `/sdlc:design`.

## status
`sdlc status` and summarise which artifacts are accepted, present or missing; report `next` verbatim as the command to run.
