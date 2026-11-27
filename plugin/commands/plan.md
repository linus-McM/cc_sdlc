---
description: Stage 1 Plan — capture an idea, ticket or incident as intent.md
argument-hint: new "<title>" | check | accept | status  [--slug <slug>]
allowed-tools: Bash(uv run *), Read, Edit, Write, Glob, Grep, AskUserQuestion, Skill, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control. The gates check outcomes, not method: between them, choose tools, subagents and reading order freely.

Knowledge: when a verdict carries `knowledge`, run `sdlc knowledge bootstrap` (ask before installing `uv`). Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: the `sdlc plan new` verdict carries `workflow`; when its `run` is true and the Workflow tool is available, run `Workflow({name: workflow.name, args: {...}})`, otherwise do that step inline. `[workflows.run]` in `.sdlc.toml` switches each stage's workflow on or off. Workflows are read-only and advisory: the Python gate decides.

Arguments: $ARGUMENTS

The loop is plan, design, build, test: it is complete when `sdlc test review` passes. The user approves once, at `sdlc build accept`, with intent.md, spec.md and plan.md in front of them. `/sdlc:deploy` and `/sdlc:maintain` are optional and run only when the user asks.

## new "<title>"
1. `sdlc plan new "<title>"` creates `sdlc/<slug>/intent.md` from the template and `.sdlc.toml` if missing.
2. When `workflow.run` is true, run `sdlc:intent-scout` with `{slug, title}`: it scouts affected systems, users, constraints and prior art in parallel and returns section drafts plus an `interview` list. Otherwise read the code the idea touches yourself. Either way, treat what you find as hypotheses to confirm, not answers.
3. Ask the user only what the idea and the code do not already answer: what cannot be done today, who is affected, what better looks like, what is out of scope, constraints, success measure. Plain words; no formal language required. Skip the interview when nothing is open.
4. Write the answers into every section of intent.md.
5. `sdlc plan check`. Fix every listed problem and re-run until `ok`.
6. `sdlc knowledge pack plan` builds the plan context pack from the systems intent.md names; state any `skipped` or budget step-down in one line. Pass its `path` as `pack` whenever `sdlc:intent-scout` runs again.
7. `accept` (below), then carry on with the design stage in the same session.

## check
`sdlc plan check` and report the verdict.

## docs  (the stage document; on demand)
Only when the user asks for the plan document. Read Problem and Affected users and systems: the people, services and systems the change touches and the boundary between what changes and what stays. Follow the `recipe` in `sdlc docs check plan`'s verdict, then `sdlc docs render plan` and `sdlc docs open plan`.

## accept
Once the check passes, run `sdlc plan accept` yourself: no sign-off is asked for here, because the user reads intent.md again when they approve the plan. It marks intent.md accepted, adds a `process:sdlc-plan` verification event to `sdlc/knowledge/features/<slug>.md`, reports the context pack under `pack` (a pack that could not be built is reported, never a refusal) and commits `sdlc/<slug>/intent.md`, `sdlc/knowledge/` and the rest of the stage's output as `plan(<slug>): accept — intent.md`; commit it by hand only when the checkpoint layer is off. Give the user a three-line summary of the intent, then continue with `/sdlc:design new` (`Skill({skill: "sdlc:design", args: "new"})`) unless they asked for the intent alone. The boundary wrote HANDOVER.md, so a fresh session can pick the feature up from there.

## status
`sdlc status` and summarise which artifacts are accepted, present or missing; report `next` verbatim as the command to run. `next: complete` means the loop is done; `optional` then names the secondary command the user may run.
