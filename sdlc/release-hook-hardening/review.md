# Review: Release hook hardening
Reviewer: sdlc:reviewer agent. Status: done. Scope: git diff main...HEAD, three passes per REVIEW.md. Probed `sudo ./deploy.sh production`, `ENV=production make deploy`, `npm run deploy -- --env production` (all denied) and `kubectl apply -f prod/` (allowed, as before).

## Bugs
- Important: scripts/sdlc/hooks.py:88 `shlex.split` of the rendered `deploy.command` was unguarded, so a template with an unbalanced quote raised `ValueError: No closing quotation` on every Bash call and the hook crashed instead of gating. Addressed in step `hook-lines`: templates go through the same `tokens()` fallback (`test_pre_bash_survives_bad_release_command_config`).
- Nit: scripts/sdlc/hooks.py:86 a whitespace-only `deploy.command` matched every command with an empty token run and returned `""`. Addressed: blank templates are ignored (same test).
- Nit: scripts/sdlc/hooks.py:3 module docstring still called pre-bash the "production gate". Addressed: reworded to advisory.

## Security
- Important: scripts/sdlc/hooks.py:86 configuring `deploy.command` skipped the token fallback, so following the README made the hook weaker (`./deploy.sh --force production` passed). Addressed: the fallback always runs; the configured command adds a second match (`test_pre_bash_denies_configured_release_command`).
- Important: scripts/sdlc/hooks.py:71 only the first non-empty line was tokenised, so `./deploy.sh \` + newline + `production` and `set -e` + newline + `./deploy.sh production` passed. Addressed: `command_lines` joins continuations and scans every line outside heredoc bodies (`test_pre_bash_scans_every_command_line_outside_heredocs`).
- Nit: scripts/sdlc/hooks.py:94 env tokens with attached punctuation (`production;`, `prod/`) evaded. Addressed: trailing `;,/` stripped (same test).

## Compliance
- Important: scripts/sdlc/hooks.py:102 spec Design asked for a string prefilter before the config read; the shipped hook reads `.sdlc.toml` on every Bash call. Addressed by amending the spec, not the code: the configured command need not contain `deploy`, so no sound prefilter exists, and the read costs about 56 µs against a 34 ms interpreter start (measured during `/simplify`). Spec Design now records this.
- Nit: sdlc/release-hook-hardening/spec.md Design and Proof named `release_match`/`release_tokens` and four tests; shipped as `release_hit`/`tokens`/`command_lines`. Addressed: spec re-synced in this commit.

Nits: 5 of 5 reported. Requirements 5, 7, 8, 9 confirmed by the reviewer; verifier confirmed 1-9 and the live hook launcher behaviour.
