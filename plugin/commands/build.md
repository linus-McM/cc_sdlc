---
description: Stage 3 Build — plan mode against spec.md, commit plan.md, then implement red→green with plan sync enforced
argument-hint: new | check | accept | red <step> | green <step> | sync | simplify | fix on|off  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Agent, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc build new` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

## new  (plan mode play)
1. `sdlc build new` (blocked until spec.md is accepted) writes `sdlc/<slug>/plan.md`.
2. Read intent.md, spec.md, CLAUDE.md and the files the spec names. Fill plan.md: Files that change (one path per line, mark (new)); Order of work where every step names the failing test written first; Risks (what could break, the riskiest step, options rejected); Proof (commands and expected output).
3. `sdlc knowledge pack build` builds an advisory context pack from the planned files; state any `skipped` or budget step-down in one line. Run `sdlc:plan-critic` with `{slug, pack}` (`pack` = the verdict's `path`, omitted when skipped): four critics (blast radius, test-first, ordering, spec coverage) and a skeptic per finding return confirmed `issues`, each with the plan.md edit. Apply or explicitly reject each one. Then interrogate your own plan: what could this break, which step is riskiest, what did you choose not to do. Iterate until an engineer who never saw this conversation could implement from plan.md alone.
4. `sdlc build check` until `ok`, then the docs step below and `sdlc docs open build` (`sdlc build accept` is refused until `docs/build.html` is fresh). Ask the engineer to accept (tech lead for `Risk: high`); on yes `sdlc build accept` (publishes the feature concept and commits plan.md, `sdlc/knowledge/` and the rest of the stage's output as `build(<slug>): accept — plan.md`).

## docs  (the stage document; required before accept)
`sdlc docs draft build` writes the Archify source from Order of work; then `sdlc docs render build` and `sdlc docs open build`. Only when the draft is refused, follow the `recipe` in `sdlc docs check build`'s verdict.

## implement  (after accept; TDD is mandatory)
For each step in Order of work:
1. Write or extend the test named by the step. Do not touch production code yet.
2. `sdlc build red <step> --only <test id>` must report `ok` (the test fails; `--only` runs just that test when `[commands] test_one` is set, otherwise the suite). If it passes, the test is wrong or the behaviour already exists; stop and say so.
3. Implement the smallest change that makes it pass.
4. `sdlc build green <step> --only <test id>` must report `ok` (that test, then the full suite once). It also runs plan sync and commits the step as `build(<slug>): <step>`. When `sync.ok` is false, put each `unplanned` file into plan.md "Files that change" or revert it, then `sdlc build sync` and commit by hand; commit by hand too when `commit.committed` is false. The post-commit hook refreshes `graphify-out/` and `sdlc/knowledge/` in the background.
When all steps are green, run `/simplify` without asking (`Skill({skill: "simplify"})`) over the branch diff. If it renamed or removed a public name, grep spec.md, plan.md, README.md, CLAUDE.md and commands/ for the old name. Then `sdlc build simplify`: it runs the test and lint commands and plan sync, commits the result as `build(<slug>): simplify` and records the pass; `sdlc test run` is refused without one since the last green. When it fails, fix the simplification or revert it, never the tests. Next: `/clear` (HANDOVER.md from `build accept` and the commits carry the context), then `/sdlc:test`.

## fix on | fix off
Bug-fix mode. `sdlc build fix on` locks test files (the pre-edit hook denies edits to them): reproduce the bug as a failing test first, commit it, then `fix on`, make it pass without touching tests, `fix off`.

## red / green / sync / simplify
Run the named mechanic directly and report the verdict.
