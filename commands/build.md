---
description: Stage 3 Build — plan mode against spec.md, commit plan.md, then implement red→green with plan sync enforced
argument-hint: new | check | accept | red <step> | green <step> | sync | fix on|off  [--slug <slug>]
allowed-tools: Bash(python3 *), Bash(git *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Agent, Skill
---
Run every `sdlc` call as `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Arguments: $ARGUMENTS

## new  (plan mode play)
1. `sdlc build new` (blocked until spec.md is accepted) writes `sdlc/<slug>/plan.md`.
2. Read intent.md, spec.md, CLAUDE.md and the files the spec names. Fill plan.md: Files that change (one path per line, mark (new)); Order of work where every step names the failing test written first; Risks (what could break, the riskiest step, options rejected); Proof (commands and expected output).
3. Interrogate your own plan: what could this break, which step is riskiest, what did you choose not to do. Iterate until an engineer who never saw this conversation could implement from plan.md alone.
4. `sdlc build check` until `ok`. Ask the engineer to accept (tech lead for `Risk: high`); on yes `sdlc build accept` and commit plan.md as `build(<slug>): accept plan`.

## implement  (after accept; TDD is mandatory)
For each step in Order of work:
1. Write or extend the test named by the step. Do not touch production code yet.
2. `sdlc build red <step>` must report `ok` (tests fail). If they pass, the test is wrong or the behaviour already exists; stop and say so.
3. Implement the smallest change that makes it pass.
4. `sdlc build green <step>` must report `ok`.
5. `sdlc build sync`: any `unplanned` file goes into plan.md "Files that change" in the same commit, or is reverted.
6. Commit: `build(<slug>): <step>`.
When all steps are green run `/simplify`, then `sdlc build sync` once more. Next: `/sdlc:test`.

## fix on | fix off
Bug-fix mode. `sdlc build fix on` locks test files (the pre-edit hook denies edits to them): reproduce the bug as a failing test first, commit it, then `fix on`, make it pass without touching tests, `fix off`.

## red / green / sync
Run the named mechanic directly and report the verdict.
