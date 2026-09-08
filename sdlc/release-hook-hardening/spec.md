# Spec: Release hook hardening
From: intent.md (2026-09-08). Status: accepted. Risk: high.

## Requirements
1. `.sdlc.toml` gains `deploy.command` (default `""`): the shell command that performs a release, with `{env}` where the environment name goes, e.g. `./deploy.sh {env}`.
2. `pre_bash` tokenises the command lines of a Bash call (backslash continuations joined, heredoc bodies dropped, quoted strings kept as one token) and, while `RELEASE_APPROVAL` is unset, denies iff one token is a deploy program (its basename without extension is `deploy`, e.g. `deploy`, `./deploy.sh`, `bin/deploy`) and another token equals a gate-tier environment name or `prod`, case-insensitive, also matching the value after `=` and ignoring trailing `;,/`.
3. When `deploy.command` is set, `pre_bash` additionally denies when the command rendered for a gate-tier environment appears as a contiguous token run. A malformed template (unbalanced quote, whitespace only) never crashes the hook.
4. Heredoc bodies, quoted strings (commit messages) and prose never trigger a denial: `git commit -m "deploy(x): ship production"` and a heredoc whose body mentions both words pass. Every command line outside a heredoc is examined, so `set -e` followed by `./deploy.sh production` on the next line is denied.
5. `python3 scripts/sdlc.py deploy record production` is still denied by the fallback (tokens `deploy` and `production`), matching the mechanic's own refusal; with `RELEASE_APPROVAL` set it passes.
6. The denial reason names the matched command or tokens and says the hook is advisory: the mechanic gate in `deploy.check` is what enforces authorization.
7. `agents/verifier.md` and `agents/reviewer.md` instruct: if a hook denies a command, report the denial verbatim and stop; never rewrite, encode, split or relocate the command to get past it.
8. `README.md` Guardrails and `commands/deploy.md` describe the new matching and state that hooks are a second line, not the gate.
9. `deploy.check` and `deploy.record` are unchanged.

## Design
- `project.DEFAULT_CONFIG`: add `command = ""` under `[deploy]` with a comment. Read through `project.config` as today.
- `hooks.py`: pure helpers, testable without the hook payload:
  - `command_lines(cmd) -> list[str]`: joins backslash continuations, drops heredoc bodies (`<<`, `<<-`, quoted or bare terminator), skips blank lines.
  - `tokens(text) -> list[str]`: `shlex.split` each command line, falling back to `str.split` on `ValueError`.
  - `release_hit(cmd, template, gated) -> str | None`: the configured command as a contiguous token run (when `template` is non-blank), else the deploy-program plus gated-env token pair; returns a display string for the denial reason.
  - `pre_bash`: exit when the command is blank or `deploy.approver()` is set; load config once; deny on `release_hit`. No string prefilter before the config read: the configured command need not contain `deploy`, and the read costs about 56 µs against a 34 ms interpreter start per hook call.
- `deploy.py`: `approver()` and `gated(cfg)` helpers shared by the hook and `deploy.check`, so one definition of the gate.
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
