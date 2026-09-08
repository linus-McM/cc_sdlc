## Rehearsal and band nits

### Why
Five nits left open by the review of dogfood-fixes-round-two:
1. `deploy.rehearse` discards the exit status of `git worktree add` and `git worktree remove`, so a
   failed add reports a guessed reason and a failed remove leaves a stale `.git/worktrees` entry
   plus a full checkout in the temp dir with no signal.
2. The rehearsal runs the rollback at the worktree top level; when the project root is a
   subdirectory of the repository the command gets a different cwd than a real rollback would.
3. Rehearsal commits stay in the object store as dangling objects until git gc.
4. `maintain.tier` raises a bare `KeyError` for an unknown `bad` when called by anything other
   than `watch`.
5. The pre-bash hook treats `prod` as a gated environment alias, but `deploy.check` rejects
   `prod` as unknown, so hook and mechanic disagree on what gated means.

### Artifacts
- sdlc/rehearsal-and-band-nits/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 5
- review: Important: 1, Nit: 5

### Proof
- `uv run pytest -q`: 76 passed (72 existing + 4 new; the pyproject `-q` plus `-q` hides the summary line, use `uv run pytest` alone to see it).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `python3 scripts/sdlc.py deploy rehearse` on this branch: ok, HEAD unchanged, one worktree listed.
