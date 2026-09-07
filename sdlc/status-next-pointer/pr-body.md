## Status next pointer

### Why
`sdlc status` lists artifact states (accepted, draft, present, missing) but never says which
command comes next. Claude and the engineer have to reason about the pipeline order themselves
each time they resume a feature, and every other verdict in the plugin already carries a `next`
field, so `status` is the odd one out.

### Artifacts
- sdlc/status-next-pointer/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 3
- review: Important: 1, Nit: 4

### Proof
- `uv run pytest -q`: 60 passed (54 existing + 6 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: "All checks passed!" and "files already formatted".
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py status` on this repo prints `"next": "/sdlc:test"` once plan.md is accepted.
