# Plan: Release hook hardening
From: spec.md (2026-09-08). Status: accepted. Risk: high.

## Files that change
- scripts/sdlc/hooks.py
- scripts/sdlc/project.py
- tests/test_hooks.py
- agents/verifier.md
- agents/reviewer.md
- commands/deploy.md
- README.md

## Order of work
1. `tests/test_hooks.py` (failing first, step `hook-tokens`): four tests from spec Proof.
   `test_pre_bash_ignores_prose_and_heredocs` feeds a heredoc whose body says deploy and
   production, a commit message quoting both words, and a multi-line command where the
   words sit on line two; all return None. `test_pre_bash_fallback_matches_tokens_not_text`
   asserts `./deploy.sh production`, `bin/deploy prod` and
   `python3 scripts/sdlc.py deploy record production` are denied, `make deploy ENV=production`
   stays denied (an env token also matches the value after `=`), and staging passes.
   `test_pre_bash_denies_configured_release_command` sets `deploy.command = "./release.sh {env}"`
   and asserts `./release.sh production` is denied, `./release.sh staging` and
   `./deploy.sh production` (not the configured command) pass.
   `test_pre_bash_reason_names_mechanic_gate` asserts the reason contains `deploy.check`.
   `sdlc build red hook-tokens` must report ok.
2. `scripts/sdlc/project.py`: `command = ""` under `[deploy]` in DEFAULT_CONFIG.
   `scripts/sdlc/hooks.py`: `release_match`, `release_tokens`, new `pre_bash`; import `shlex`.
   `sdlc build green hook-tokens` must report ok.
3. `agents/verifier.md`, `agents/reviewer.md`: hook-denial sentence. `commands/deploy.md`
   `check <env>` bullet and `README.md` Guardrails pre-bash bullet reworded. No tests; prose.
4. `sdlc build sync`, `/simplify`, `sdlc build sync`. Re-run the four previously blocked
   commands through `python3 scripts/hook.py pre-bash` with a JSON payload on stdin (Proof).

## Risks
- Could break: a project whose release command does not contain a `deploy` program and has
  no `deploy.command` configured gets no hook denial at all. Mitigated by the mechanic gate and
  by documenting `deploy.command` in README and DEFAULT_CONFIG.
- Riskiest step: 2. `shlex.split` raises on unbalanced quotes (common in heredocs with
  apostrophes); the fallback to `str.split` must be covered by the heredoc test.
- Rejected: parsing shell to strip heredoc bodies (rabbit hole); matching every line (the
  false positives came from later lines); keeping a substring match on the configured command
  rendered for `prod` aliases (only the configured environment names are rendered).
- Rejected: trying to make the hook bypass-proof. Text hooks cannot be; the mechanic is.

## Proof
- `uv run pytest -q`: 65 passed (61 existing + 4 new).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- `printf '%s' '{"tool_input": {"command": "cat > x <<EOF\ndeploy to production\nEOF"}}' | python3 scripts/hook.py pre-bash` prints nothing.
- `printf '%s' '{"tool_input": {"command": "./deploy.sh production"}}' | python3 scripts/hook.py pre-bash` prints a deny verdict naming `deploy.check`.
