# Review: Status next pointer
Reviewer: sdlc:reviewer agent. Status: done. Scope: git diff main...HEAD, three passes per REVIEW.md.

## Bugs
- Important: scripts/sdlc/stages.py:95 `status` stopped being total: `deploy.readiness`/`deploy.released` `json.loads` test-report.json and deploy.json, so a truncated file raised an uncaught `JSONDecodeError` and the recovery command printed a traceback instead of a verdict. Addressed in step `corrupt-json`: `project.read_json` now raises a `Blocked` verdict naming the file (`test_status_reports_corrupt_json_as_verdict_not_traceback`).
- Nit: scripts/sdlc/deploy.py:21 and :30 shape assumptions (`["deployments"]`, `d["env"]`, `rep["passed"]`) raise `KeyError` rather than a verdict on hand-edited files.

## Security
- Nit: scripts/sdlc/build.py:16 the bandit `shell=True` justification names only the `.sdlc.toml` commands, but `run_cmd` also executes `checks` strings from `evals/*.json` (evals.py:27).

## Compliance
- Nit: scripts/sdlc/stages.py:95 spec.md requirement 6 reads unconditional, but readiness runs first, so a released feature with a failing test-report points at `/sdlc:test`. Spec Proof now documents this ordering.
- Nit: sdlc/status-next-pointer/spec.md:14 Design described `next_for(feature)` reading deploy.json via `deploy.state()`; shipped signature is `next_for(feature, state)` via `deploy.readiness`/`deploy.released`. Spec Design re-synced in the same commit.

Nits: 4 of 4 reported. Commit 36c9e8e (tooling pass) reviewed for bugs and security only: reformat is behaviour-preserving.
