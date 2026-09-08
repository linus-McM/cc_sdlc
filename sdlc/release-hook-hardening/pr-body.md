## Release hook hardening

### Why
The pre-bash hook denies any Bash call whose text contains the word "deploy" together with a
gate-tier environment name or "prod". During the first dogfooded feature it blocked four
harmless commands: three heredocs writing prose or tests, and one git commit. Meanwhile the
sdlc:verifier subagent got past it by base64-decoding the environment name inside a Python
heredoc, so the hook is both noisy and trivially bypassed. Neither the agent prompts nor the
docs say that hooks are advisory and the mechanic (`deploy.check`) is the real gate.

### Artifacts
- sdlc/release-hook-hardening/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 2
- review: Important: 4, Nit: 4

### Proof
- `uv run pytest -q`: 66 passed (61 existing + 5 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `printf '%s' '{"tool_input": {"command": "cat > x <<EOF\ndeploy to production\nEOF"}}' | python3 scripts/hook.py pre-bash` prints nothing.
- `printf '%s' '{"tool_input": {"command": "./deploy.sh production"}}' | python3 scripts/hook.py pre-bash` prints a deny verdict naming `deploy.check`.
