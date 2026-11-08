---
description: Stage 3 Build — plan mode against spec.md, commit plan.md, then implement red→green with plan sync enforced
argument-hint: new | check | accept | red <step> | green <step> | sync | fix on|off  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Agent, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate build`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

Arguments: $ARGUMENTS

## new  (plan mode play)
1. `sdlc build new` (blocked until spec.md is accepted) writes `sdlc/<slug>/plan.md`.
2. Read intent.md, spec.md, CLAUDE.md and the files the spec names. Fill plan.md: Files that change (one path per line, mark (new)); Order of work where every step names the failing test written first; Risks (what could break, the riskiest step, options rejected); Proof (commands and expected output).
3. `sdlc knowledge pack build` builds an advisory context pack from the planned files; state any `skipped` or budget step-down in one line. Run `sdlc:plan-critic` with `{slug, pack}` (`pack` = the verdict's `path`, omitted when skipped): four critics (blast radius, test-first, ordering, spec coverage) and a skeptic per finding return confirmed `issues`, each with the plan.md edit. Apply or explicitly reject each one. Then interrogate your own plan: what could this break, which step is riskiest, what did you choose not to do. Iterate until an engineer who never saw this conversation could implement from plan.md alone.
4. `sdlc build check` until `ok`, then the docs step below and `sdlc docs open build` (`sdlc build accept` is refused until `docs/build.html` is fresh). Ask the engineer to accept (tech lead for `Risk: high`); on yes `sdlc build accept` (publishes the feature concept and commits plan.md, `sdlc/knowledge/` and the rest of the stage's output as `build(<slug>): accept — plan.md`).

## docs  (the stage document; required before accept)
Read Order of work: one node per step with its failing test as the gate before it, the red/green loop as the main path, `build sync` and the commit as the exit. Follow the `recipe` in `sdlc docs check build`'s verdict, then `sdlc docs render build` and `sdlc docs open build`.

## implement  (after accept; TDD is mandatory)
For each step in Order of work:
1. Write or extend the test named by the step. Do not touch production code yet.
2. `sdlc build red <step>` must report `ok` (tests fail). If they pass, the test is wrong or the behaviour already exists; stop and say so.
3. Implement the smallest change that makes it pass.
4. `sdlc build green <step>` must report `ok`.
5. `sdlc build sync`: any `unplanned` file goes into plan.md "Files that change" in the same commit, or is reverted.
6. Commit: `build(<slug>): <step>`. The post-commit hook refreshes `graphify-out/` and `sdlc/knowledge/` in the background; the post-bash hook says when an index is further behind HEAD than `[knowledge] max_behind`.
When all steps are green offer `/simplify` (do not run it unasked), then `sdlc build sync` once more. Next: `/clear` (HANDOVER.md from `build accept` and the commits carry the context), then `/sdlc:test`.

## fix on | fix off
Bug-fix mode. `sdlc build fix on` locks test files (the pre-edit hook denies edits to them): reproduce the bug as a failing test first, commit it, then `fix on`, make it pass without touching tests, `fix off`.

## red / green / sync
Run the named mechanic directly and report the verdict.
