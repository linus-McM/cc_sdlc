---
description: Stage 1 Plan — capture an idea, ticket or incident as intent.md; the product owner accepts it
argument-hint: new "<title>" | check | accept | status  [--slug <slug>]
allowed-tools: Bash(uv run *), Read, Edit, Write, AskUserQuestion, Workflow
---
Run every `sdlc` call as `uv run --no-project "${CLAUDE_PLUGIN_ROOT}/scripts/sdlc.py" ...` from the project root. Each call prints one JSON verdict: act on `ok`, quote `reason` verbatim when false, and follow `next`. Never edit the verdict logic; the gate is the control.

Knowledge: run `sdlc knowledge bootstrap`; if `uv` is missing, ask the user before installing it. Read `sdlc/knowledge/index.md` only during `new`, following its links only as deep as the task needs. For call-graph questions run `graphify query "<question>"` or `graphify affected "<symbol>"` directly (do not load the graphify skill for syntax). Never write a `human:` entry into a concept's `verified` list: only `accept` publishes.

Workflows: run `sdlc workflows gate plan`; when `run` is true and the Workflow tool is available, run the named workflow as `Workflow({name: "sdlc:<name>", args: {...}})`, otherwise do that step inline. Workflows are read-only and advisory: you write the artifact, the Python gate decides.

Arguments: $ARGUMENTS

## new "<title>"
1. `sdlc plan new "<title>"` creates `sdlc/<slug>/intent.md` from the template and `.sdlc.toml` if missing.
2. Run `sdlc:intent-scout` with `{slug, title}`: it scouts affected systems, users, risk triggers and prior art in parallel and returns section drafts plus an `interview` list. Treat the drafts as hypotheses to confirm, not answers.
3. Interview the originator until concrete: what cannot be done today, who is affected, what better looks like, what is out of scope, constraints, success measure. Plain words; no formal language required.
4. Write the answers into every section of intent.md. Set `Risk: high` when the change touches auth, PII, payments, migrations or infra.
5. `sdlc plan check`. Fix every listed problem, re-run until `ok`.
6. `sdlc knowledge pack plan` builds the plan context pack from the systems intent.md names (`sdlc plan accept` is refused without one at HEAD, and with the knowledge layer on a missing Repomix blocks it: `npm i -g repomix`). Pass its `path` as `pack` whenever `sdlc:intent-scout` runs again, and state any `skipped` or budget step-down in one line.
7. Show the originator the file and ask them to correct anything misunderstood.

## check
`sdlc plan check` and report the verdict.

## docs  (the stage document; required before accept)
Read Problem and Affected users and systems: the people, services and systems the change touches and the boundary between what changes and what stays. Follow the `recipe` in `sdlc docs check plan`'s verdict, then `sdlc docs render plan` and `sdlc docs open plan`.

## accept
Only a human accepts. Run `sdlc docs open plan` first (`sdlc plan accept` is refused until `docs/plan.html` is fresh). Ask (AskUserQuestion) the product owner to confirm the intent is correct and in scope, quoting the HTML path; on yes run `sdlc plan accept` (it also publishes `sdlc/knowledge/features/<slug>.md` with a `human:<author>` verification event and `status: stable`), which commits `sdlc/<slug>/intent.md`, `sdlc/knowledge/` and the rest of the stage's output as `plan(<slug>): accept — intent.md`; commit it by hand only when the checkpoint layer is off. Next: the boundary wrote HANDOVER.md; `/clear`, then `/sdlc:design`.

## status
`sdlc status` and summarise which artifacts are accepted, present or missing; report `next` verbatim as the command to run.
