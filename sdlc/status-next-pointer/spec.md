# Spec: Status next pointer
From: intent.md (2026-09-08). Status: accepted. Risk: low.

## Requirements
1. `sdlc status` returns a `next` key alongside the existing `slug` and `artifacts` keys; no existing key changes shape.
2. `next` is one of the six stage commands `/sdlc:plan`, `/sdlc:design`, `/sdlc:build`, `/sdlc:test`, `/sdlc:deploy`, `/sdlc:maintain`.
3. `next` is the command of the first stage in `stages.ORDER` whose artifact is missing or not `accepted` (intent.md -> `/sdlc:plan`, spec.md -> `/sdlc:design`, plan.md -> `/sdlc:build`).
4. With all three artifacts accepted, `next` is `/sdlc:test` while test-report.json or review.md is missing.
5. With test-report.json and review.md present, `next` is `/sdlc:deploy` until deploy.json lists a deployment with `env == "production"`.
6. After a production deployment is recorded, `next` is `/sdlc:maintain`.
7. The result is deterministic: same files, same answer; no git or subprocess calls.

## Design
- `stages.py`: add `next_for(feature: Path) -> str` computing the pointer from the same
  file checks `status` already makes, reusing `accepted()` and `project.read_json` for deploy.json.
  `status()` gains `"next": next_for(feature)` in its return dict.
- Data flow: filesystem state of `sdlc/<slug>/` only. deploy.json is read through
  `deploy.state()` so the shape stays defined in one place; `stages` importing `deploy` would create
  a cycle (`deploy` imports `testing` imports `build`, none import `stages`, so importing `deploy`
  from `stages` is acyclic; `maintain` imports `stages` and that stays one-directional).
- Interface: JSON verdict of `sdlc status` gains `next`. `commands/plan.md` "status" section tells
  Claude to report `next` verbatim.
- No change to any other stage, template or hook.

## Concerns
none. Read-only mechanic, no auth, PII, payments, migration or infra touched.

## Open questions
none carried from intent.md.

## Proof
- `tests/test_plan_design.py`: the `test_status_next_*` tests assert `next` at each pipeline
  state from `plan new` through a recorded production deployment (requirements 1-6);
  `test_status_reports_stage_progress` asserts membership in `stages.COMMANDS` (requirement 2).
  Requirement 4 is implemented through `deploy.readiness`, so a failed test report also
  points back at `/sdlc:test` (asserted by `test_status_next_agrees_with_deploy_gate_on_failed_report`).
- `uv run pytest` all green; `uv run ruff check scripts tests && uv run ruff format --check scripts tests` clean;
  `claude plugin validate --strict .` passes.
