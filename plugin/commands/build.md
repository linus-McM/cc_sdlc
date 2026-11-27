---
description: Stage 3 Build — write plan.md against spec.md, get the one approval, then implement red→green exactly as planned
argument-hint: new | check | accept | red <step> | green <step> | sync | simplify | fix on|off  [--slug <slug>]
allowed-tools: Bash(uv run *), Bash(git *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Agent, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc build new` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

## new  (plan mode play)
1. `sdlc build new` (blocked until spec.md is accepted) writes `sdlc/<slug>/plan.md`.
2. Read intent.md, spec.md, CLAUDE.md and the files the spec names. Fill plan.md: Files that change (one path per line, mark (new)); Order of work as numbered steps (`1.`, `2.`, ...), each naming the failing test written first and citing the requirement it delivers, e.g. `1. tests/test_x.py::test_parse fails, then add parse() (R1)`; Risks (what could break, the riskiest step, options rejected); Proof (commands and expected output). Every spec.md requirement is cited by at least one step, and no step cites a requirement the spec does not have.
3. `sdlc knowledge pack build` builds an advisory context pack from the planned files; state any `skipped` or budget step-down in one line. When `workflow.run` is true, run `sdlc:plan-critic` with `{slug, pack}` (`pack` = the verdict's `path`, omitted when skipped): four critics (blast radius, test-first, ordering, spec coverage) and a skeptic per finding return confirmed `issues`, each with the plan.md edit. Apply or explicitly reject each one. Then interrogate your own plan: what could this break, which step is riskiest, what did you choose not to do. Iterate until an engineer who never saw this conversation could implement from plan.md alone.
4. `sdlc build check` until `ok`: it refuses steps that are not numbered, a requirement no step delivers, and a citation of a requirement that does not exist.
5. `accept` (below).

## accept  (the one approval)
This is the only point where the user signs anything off. Show them, in the reply itself, what they are approving: the outcome from intent.md, the numbered requirements, Files that change, Order of work and Risks, with the three file paths. Ask (AskUserQuestion) whether to build exactly this. On changes, edit the artifacts, re-run the checks and ask again. On yes, `sdlc build accept`: it marks plan.md accepted, pins the approved files and steps with the current commit in `sdlc/<slug>/approved.json`, publishes the feature concept with a `human:<author>` verification event and `status: stable`, and commits the stage's output as `build(<slug>): accept — plan.md`. `sdlc build red|green|sync|simplify|fix` are refused until then.

After approval the plan is the contract. Build it as written. When the code proves a step or a file wrong, edit plan.md and carry on: `sdlc test run`, `sdlc test review` and the PR body report every difference from `approved.json` as `deviations` (files added, files removed, steps changed). When the difference changes what the user gets (a requirement dropped or altered, a new behaviour), stop and ask, then re-run `sdlc build accept`, which pins the new plan and keeps the original base commit.

## docs  (the stage document; on demand)
Only when the user asks for the build document. `sdlc docs draft build` writes the Archify source from Order of work; then `sdlc docs render build` and `sdlc docs open build`. Only when the draft is refused, follow the `recipe` in `sdlc docs check build`'s verdict.

## implement  (after accept; TDD is mandatory)
For each step `<n>` in Order of work, in order:
1. Write or extend the test named by the step. Do not touch production code yet.
2. `sdlc build red "<n>: <label>" --only <test id>` must report `ok` (the test fails; `--only` runs just that test when `[commands] test_one` is set, otherwise the suite). If it passes, the test is wrong or the behaviour already exists; stop and say so. The step name starts with the step's number in plan.md (`3`, `step 3` and `3: add parse()` all name step 3) and red and green use the same name: `sdlc test run` is refused while a step has no red→green cycle under its number.
3. Implement the smallest change that makes it pass. How is yours to decide.
4. `sdlc build green "<n>: <label>" --only <test id>` must report `ok` (that test, then the full suite once). It also runs plan sync and commits the step as `build(<slug>): <n>: <label>`. When `sync.ok` is false, put each `unplanned` file into plan.md "Files that change" or revert it, then `sdlc build sync` and commit by hand; commit by hand too when `commit.committed` is false. The post-commit hook refreshes `graphify-out/` and `sdlc/knowledge/` in the background.
When all steps are green, run `/simplify` without asking (`Skill({skill: "simplify"})`) over the branch diff. If it renamed or removed a public name, grep spec.md, plan.md, README.md, CLAUDE.md and commands/ for the old name. Then `sdlc build simplify`: it runs the test and lint commands and plan sync, commits the result as `build(<slug>): simplify` and records the pass; `sdlc test run` is refused without one since the last green. When it fails, fix the simplification or revert it, never the tests. Then continue with `/sdlc:test run` (`Skill({skill: "sdlc:test", args: "run"})`) in the same session; HANDOVER.md from `build accept` and the step commits carry the context if a fresh session takes over.

## fix on | fix off
Bug-fix mode. `sdlc build fix on` locks test files (the pre-edit hook denies edits to them): reproduce the bug as a failing test first, commit it, then `fix on`, make it pass without touching tests, `fix off`.

## red / green / sync / simplify
Run the named mechanic directly and report the verdict.
