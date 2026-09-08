## Dogfood fixes round two

### Why
Three rough edges surfaced while the first two features went through the pipeline:
1. `maintain watch` uses two-sided Western Electric rules, so a metric that improves
   (`tests_passed` rising from 61 to 66) trips a tier 3 breach and would propose an incident.
2. `deploy rehearse` runs `deploy.rollback` in the working checkout. On this repo the command is
   `git revert --no-edit HEAD`, so the rehearsal really reverted the last commit twice and had to be
   undone by hand with `git reset --hard HEAD~1`.
3. The post-edit plan-sync hook flags files outside the repository (a scratchpad script) because
   `rel_path` falls back to the absolute path when the file is not under the project root.

### Artifacts
- sdlc/dogfood-fixes-round-two/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 4
- review: Important: 2, Nit: 5

### Proof
- `uv run pytest -q`: 72 passed (66 existing + 6 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py maintain watch tests_passed` prints `"tier": 0`.
- `python3 scripts/sdlc.py deploy rehearse` on this branch leaves `git log --oneline -1` unchanged.
