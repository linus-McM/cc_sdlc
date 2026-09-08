---
description: Stage 2 Design — turn an accepted intent.md into spec.md with flagged concerns; the product owner accepts it
argument-hint: new | check | accept  [--slug <slug>]
allowed-tools: Bash(python3 *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Skill
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge first: run `sdlc knowledge bootstrap` (idempotent; on first use installs uv, Graphify, its Claude skill and git hooks, then builds `graphify-out/` and the OKF bundle `sdlc/knowledge/`), then read `sdlc/knowledge/index.md` and follow its links only as deep as the task needs. For call-graph questions (what calls what, blast radius of a change) run `graphify query "<question>"` or `graphify affected "<symbol>"` before grepping; EXTRACTED edges are parsed facts, INFERRED edges are hints. Never write a `human:` entry into a concept's `verified` list: only `accept` publishes. `sdlc knowledge status` says how far each index is behind HEAD.

Arguments: $ARGUMENTS

## new
1. `sdlc design new` (blocked until intent.md is accepted) writes `sdlc/<slug>/spec.md`.
2. Read intent.md and the codebase (CLAUDE.md, existing modules the change touches). Load every organisation skill relevant to brand, security, compliance and UX and apply them as constraints.
3. Fill spec.md: numbered testable Requirements traced to the intent; Design naming components, data flow and interfaces; Concerns listing every policy conflict with its owner (say plainly where two policies contradict); Open questions from intent.md each answered or reassigned; Proof naming the test files and checks.
4. `sdlc design check` until `ok`.

## check
`sdlc design check` and report.

## accept
Walk the product owner through Concerns first; each must be resolved with its policy owner before engineering sees the spec. Ask the product owner to accept; for `Risk: high` also ask for a tech lead name and record it under Concerns. On yes: `sdlc design accept` (publishes the feature concept), commit `sdlc/<slug>/spec.md` and `sdlc/knowledge/` as `design(<slug>): accept spec`. Next: `/sdlc:build`.
