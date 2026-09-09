---
type: Feature
title: Status next pointer
description: "`sdlc status` lists artifact states (accepted, draft, present, missing) but never says which"
resource: sdlc/status-next-pointer
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T01:00:09Z" }
stale_after: "2026-09-23T01:00:09Z"
source_commit: f4b7a7e7c7ca48d51fac20696ba496746da179e6
sources:
  - { id: intent, resource: sdlc/status-next-pointer/intent.md, last_modified: "2026-09-08T09:14:02+10:00", digest: 160116081cdd23ba }
  - { id: spec, resource: sdlc/status-next-pointer/spec.md, last_modified: "2026-09-08T09:28:14+10:00", digest: 21a434a2e5ea4acf }
  - { id: plan, resource: sdlc/status-next-pointer/plan.md, last_modified: "2026-09-08T09:29:42+10:00", digest: 0d63041e55ae8191 }
  - { id: review, resource: sdlc/status-next-pointer/review.md, last_modified: "2026-09-08T09:28:14+10:00", digest: f6fa7c95be7b4059 }
---

# Problem
`sdlc status` lists artifact states (accepted, draft, present, missing) but never says which
command comes next. Claude and the engineer have to reason about the pipeline order themselves
each time they resume a feature, and every other verdict in the plugin already carries a `next`
field, so `status` is the odd one out.

# Outcome
`sdlc status` returns a `next` field naming the single command to run next, derived from the
artifact states: the first unaccepted stage artifact, then `/sdlc:test` until test-report.json
and review.md exist, then `/sdlc:deploy` until deploy.json records a production release, then
`/sdlc:maintain`. Resuming a feature becomes "run status, follow next".

# Requirements
1. `sdlc status` returns a `next` key alongside the existing `slug` and `artifacts` keys; no existing key changes shape.
2. `next` is one of the six stage commands `/sdlc:plan`, `/sdlc:design`, `/sdlc:build`, `/sdlc:test`, `/sdlc:deploy`, `/sdlc:maintain`.
3. `next` is the command of the first stage in `stages.ORDER` whose artifact is missing or not `accepted` (intent.md -> `/sdlc:plan`, spec.md -> `/sdlc:design`, plan.md -> `/sdlc:build`).
4. With all three artifacts accepted, `next` is `/sdlc:test` while test-report.json or review.md is missing.
5. With test-report.json and review.md present, `next` is `/sdlc:deploy` until deploy.json lists a deployment with `env == "production"`.
6. After a production deployment is recorded, `next` is `/sdlc:maintain`.
7. The result is deterministic: same files, same answer; no git or subprocess calls.

# Files
- `Note: `build sync` reported `cripts/sdlc/stages.py` because `project.git` stripped the leading`
- `commands/plan.md`
- `parentheses; `artifacts.list_items` splits on them.`
- `scripts/sdlc/deploy.py` in [deploy.py](/modules/deploy-py.md)
- `scripts/sdlc/project.py` in [Path](/modules/path.md)
- `scripts/sdlc/stages.py` in [stages.py](/modules/stages-py.md)
- `space off the first porcelain line. Annotations in this list must avoid commas and nested`
- `tests/test_build_test.py` in [run](/modules/run.md)
- `tests/test_plan_design.py` in [run](/modules/run.md)

# Review
- Important: 1, Nit: 4

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev, staging
