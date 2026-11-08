---
description: Stage 2 Design — turn an accepted intent.md into spec.md with flagged concerns; the product owner accepts it
argument-hint: new | check | accept  [--slug <slug>]
allowed-tools: Bash(uv run *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate design`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

Arguments: $ARGUMENTS

## new
1. `sdlc design new` (blocked until intent.md is accepted) writes `sdlc/<slug>/spec.md`.
2. Read intent.md and the codebase (CLAUDE.md, existing modules the change touches). Load every organisation skill relevant to brand, security, compliance and UX and apply them as constraints.
3. `sdlc knowledge pack design` builds an advisory context pack from the intent's systems; state any `skipped` or budget step-down in one line.
4. Run `sdlc:design-panel` with `{slug, pack}` (`pack` = the verdict's `path`, omitted when skipped): three independent designs, four policy-concern lenses and a judge panel return one synthesized draft (`requirements`, `design`, `concerns` with owners, `open_questions`, `proof`, `rejected`). Start spec.md from it and keep `rejected` for the plan's Risks.
5. Fill spec.md: numbered testable Requirements traced to the intent; Design naming components, data flow and interfaces; Concerns listing every policy conflict with its owner (say plainly where two policies contradict); Open questions from intent.md each answered or reassigned; Proof naming the test files and checks.
6. `sdlc design check` until `ok`.

## check
`sdlc design check` and report.

## docs  (the stage document; required before accept)
Read Design: the components it names, the data that moves between them and the interfaces at the edges; Concerns become governance notes on the edges they touch. Follow the `recipe` in `sdlc docs check design`'s verdict, then `sdlc docs render design` and `sdlc docs open design`.

## accept
Run `sdlc docs open design` first (`sdlc design accept` is refused until `docs/design.html` is fresh) and quote the HTML path in the question. Walk the product owner through Concerns first; each must be resolved with its policy owner before engineering sees the spec. Ask the product owner to accept; for `Risk: high` also ask for a tech lead name and record it under Concerns. On yes: `sdlc design accept` (publishes the feature concept and commits `sdlc/<slug>/spec.md`, `sdlc/knowledge/` and the rest of the stage's output as `design(<slug>): accept — spec.md`). Next: the boundary wrote HANDOVER.md; `/clear`, then `/sdlc:build`.
