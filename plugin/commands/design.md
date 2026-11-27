---
description: Stage 2 Design — turn an accepted intent.md into spec.md with numbered requirements and flagged concerns
argument-hint: new | check | accept  [--slug <slug>]
allowed-tools: Bash(uv run *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc design new` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

## new
1. `sdlc design new` (blocked until intent.md is accepted) writes `sdlc/<slug>/spec.md`.
2. Read intent.md and the codebase (CLAUDE.md, existing modules the change touches). Load every organisation skill relevant to brand, security, compliance and UX and apply them as constraints.
3. `sdlc knowledge pack design` builds an advisory context pack from the intent's systems; state any `skipped` or budget step-down in one line.
4. When `workflow.run` is true, run `sdlc:design-panel` with `{slug, pack}` (`pack` = the verdict's `path`, omitted when skipped): three independent designs, four policy-concern lenses and a judge panel return one synthesized draft (`requirements`, `design`, `concerns` each with its mitigation, `open_questions`, `proof`, `rejected`). Start spec.md from it and keep `rejected` for the plan's Risks. Otherwise design it yourself.
5. Fill spec.md: Requirements as a numbered list (`1.`, `2.`, ...), one testable requirement per item, traced to the intent; plan.md and review.md cite them as `R1`, `R2`, so the numbers are the contract. Design naming components, data flow and interfaces; Concerns listing every policy or security conflict with how the design handles it (say plainly where two policies contradict); Open questions from intent.md each answered; Proof naming the test files and checks.
6. `sdlc design check` until `ok`: it refuses Requirements that are not a numbered list.
7. `accept` (below), then carry on with the build stage in the same session.

## check
`sdlc design check` and report.

## docs  (the stage document; on demand)
Only when the user asks for the design document. Read Design: the components it names, the data that moves between them and the interfaces at the edges; Concerns become governance notes on the edges they touch. Follow the `recipe` in `sdlc docs check design`'s verdict, then `sdlc docs render design` and `sdlc docs open design`.

## accept
Ask the user (AskUserQuestion) only about a Concern or Open question that the code and the intent cannot settle; write the answer into spec.md. Then run `sdlc design accept` yourself: it marks spec.md accepted, adds a `process:sdlc-design` verification event to the feature concept and commits `sdlc/<slug>/spec.md`, `sdlc/knowledge/` and the rest of the stage's output as `design(<slug>): accept — spec.md`. Continue with `/sdlc:build new` (`Skill({skill: "sdlc:build", args: "new"})`) unless the user asked for the spec alone. The boundary wrote HANDOVER.md, so a fresh session can pick the feature up from there.
