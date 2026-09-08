# Spec: Release hook hardening
From: intent.md (2026-09-08). Status: accepted. Risk: high.

## Requirements
1. `.sdlc.toml` gains `deploy.command` (default `""`): the shell command that performs a release, with `{env}` where the environment name goes, e.g. `./deploy.sh {env}`.
2. When `deploy.command` is set, `pre_bash` denies a Bash call only if the command rendered for a gate-tier environment appears in it as a contiguous string, and `RELEASE_APPROVAL` is unset.
3. When `deploy.command` is empty, `pre_bash` falls back to token matching on the first line only: deny iff one token is a deploy program (its basename without extension is `deploy`, e.g. `deploy`, `./deploy.sh`, `bin/deploy`) and another token equals a gate-tier environment name or `prod`, case-insensitive, and `RELEASE_APPROVAL` is unset.
4. Heredoc bodies, later lines, quoted strings (commit messages) and prose never trigger a denial: `git commit -m "deploy(x): ship production"` and a heredoc whose body mentions both words pass.
5. `python3 scripts/sdlc.py deploy record production` is still denied by the fallback (tokens `deploy` and `production`), matching the mechanic's own refusal; with `RELEASE_APPROVAL` set it passes.
6. The denial reason names the matched command or tokens and says the hook is advisory: the mechanic gate in `deploy.check` is what enforces authorization.
7. `agents/verifier.md` and `agents/reviewer.md` instruct: if a hook denies a command, report the denial verbatim and stop; never rewrite, encode, split or relocate the command to get past it.
8. `README.md` Guardrails and `commands/deploy.md` describe the new matching and state that hooks are a second line, not the gate.
9. `deploy.check` and `deploy.record` are unchanged.

## Design
- `project.DEFAULT_CONFIG`: add `command = ""` under `[deploy]` with a comment. Read through `project.config` as today.
- `hooks.py`: replace the body of `pre_bash` with two pure helpers so they are testable without the hook payload:
  - `release_match(cmd: str, template: str, gated: list[str]) -> str | None`: returns the rendered command that appears in `cmd`, or None.
  - `release_tokens(cmd: str, gated: list[str]) -> tuple[str, str] | None`: `shlex.split` the first line (fall back to `str.split` on `ValueError`); return `(program_token, env_token)` when both a deploy program and a gated env / `prod` token are present.
  - `pre_bash`: cheap early exit when `RELEASE_APPROVAL` is set or the lowercase command contains neither `deploy` nor any gated env name; then load config once and apply `release_match` if `command` is set, else `release_tokens`. Deny with a reason built from the match.
- `agents/*.md`: one added sentence each (requirement 7).
- Docs: README Guardrails bullet and `commands/deploy.md` `check <env>` bullet reworded (requirement 8).
- Bypass resistance is out of reach for a text hook; the spec makes the mechanic the guarantee (requirement 6, 9) and the agent prompts the policy (requirement 7).

## Concerns
- Security (owner: release manager, Linus McManamey): the hook now denies less. Accepted because the mechanic gate is unchanged and the old hook was already bypassable; the change removes false confidence and false positives. Tech lead for Risk: high: Linus McManamey.
- Compliance: no conflict between policies found.

## Open questions
none carried from intent.md.

## Proof
- `tests/test_hooks.py`: `test_pre_bash_ignores_prose_and_heredocs`, `test_pre_bash_denies_configured_release_command`, `test_pre_bash_fallback_matches_tokens_not_text` (also asserts the reason names `deploy.check`, requirement 6); existing `test_pre_bash_production_gate` keeps passing.
- `tests/test_deploy.py` unchanged and green (requirement 9).
- `uv run pytest`, `uv run ruff check scripts tests && uv run ruff format --check scripts tests`, `claude plugin validate --strict .` all green.
- Live: the four commands blocked during feature status-next-pointer (heredoc intent, heredoc test, python heredoc implementation, combined commit + lessons) re-run through `hook.py pre-bash` on stdin and print nothing.
