# Plan: Status next pointer
From: spec.md (2026-09-08). Status: accepted. Risk: low.

## Files that change
- scripts/sdlc/stages.py
- tests/test_plan_design.py
- commands/plan.md
- scripts/sdlc/project.py (unplanned; found in step 2)
- tests/test_build_test.py

Note: `build sync` reported `cripts/sdlc/stages.py` because `project.git` stripped the leading
space off the first porcelain line. Annotations in this list must avoid commas and nested
parentheses; `artifacts.list_items` splits on them.

## Order of work
1. `tests/test_plan_design.py::test_status_next_walks_the_pipeline` (failing first): start
   from the `accepted_plan` fixture and assert `next` at every state: no feature dir ->
   `plan new` gives `/sdlc:plan`; after `plan accept` `/sdlc:design`; after `design accept`
   `/sdlc:build`; after `build accept` `/sdlc:test`; after writing test-report.json and
   review.md `/sdlc:deploy`; after deploy.json with a production entry `/sdlc:maintain`.
   Also `test_status_next_is_a_stage_command` asserting `next in stages.COMMANDS`.
   `sdlc build red status-next` must report `ok` (KeyError on `next`).
2. `scripts/sdlc/stages.py`: add `next_for(feature)` walking `ARTIFACTS` for the first
   non-accepted artifact, then test-report.json/review.md, then `deploy.state(feature)`
   for a production deployment; `status()` returns `"next": next_for(feature)`.
   `sdlc build green status-next` must report `ok`.
3. `tests/test_build_test.py::test_build_sync_keeps_unstaged_first_line_path_intact`
   (failing first, step `porcelain-strip`): an unstaged edit as the only porcelain line must
   be reported with its full path. Fix `project.git` to strip newlines only.
4. `commands/plan.md` status section: report `next` verbatim. No test; prose only.
5. `sdlc build sync`, then `/simplify`, then `sdlc build sync` again.

## Risks
- Could break: nothing existing; `status` only gains a key. `stages` importing `deploy` is the
  riskiest step because `maintain` imports `stages` and `deploy` imports `testing`/`build`;
  none of those import `stages` or `maintain`, so no cycle. Verified by reading the imports.
- Rejected: computing `next` inside `cli.py` (would split pipeline knowledge across two
  modules); reading deploy.json directly in `stages` (duplicates the deploy.json shape).
- Rejected: a `status --all` listing every feature. Out of scope for this intent.

## Proof
- `uv run pytest -q`: 56 passed (54 existing + 2 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: "All checks passed!" and "files already formatted".
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py status` on this repo prints `"next": "/sdlc:test"` once plan.md is accepted.
