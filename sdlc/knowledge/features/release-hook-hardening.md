---
type: Feature
title: Release hook hardening
description: "The pre-bash hook denies any Bash call whose text contains the word \"deploy\" together with a"
resource: sdlc/release-hook-hardening
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: intent, resource: sdlc/release-hook-hardening/intent.md, last_modified: "2026-09-08T12:50:36+10:00", digest: ed3ebb9b592952e4 }
  - { id: spec, resource: sdlc/release-hook-hardening/spec.md, last_modified: "2026-09-08T13:02:03+10:00", digest: ceec7eaa899c3151 }
  - { id: plan, resource: sdlc/release-hook-hardening/plan.md, last_modified: "2026-09-08T13:02:03+10:00", digest: 27db3b2d8bc6d184 }
  - { id: review, resource: sdlc/release-hook-hardening/review.md, last_modified: "2026-09-08T13:02:03+10:00", digest: ed3f8ea859e0a2fd }
---

# Problem
The pre-bash hook denies any Bash call whose text contains the word "deploy" together with a
gate-tier environment name or "prod". During the first dogfooded feature it blocked four
harmless commands: three heredocs writing prose or tests, and one git commit. Meanwhile the
sdlc:verifier subagent got past it by base64-decoding the environment name inside a Python
heredoc, so the hook is both noisy and trivially bypassed. Neither the agent prompts nor the
docs say that hooks are advisory and the mechanic (`deploy.check`) is the real gate.

# Outcome
The hook denies only real release commands: the configured `deploy.command` rendered for a
gate-tier environment, or, when no command is configured, a first-line command whose tokens
(not prose) are a deploy program plus a gated environment name. Prose, heredoc bodies, commit
messages and `sdlc deploy check` verdict calls pass. The verifier and reviewer agents are told
never to rewrite, encode or split a command to get past a hook, and to report the denial
instead. README and the deploy command describe the hook as a second line, not the gate.

# Requirements
1. `.sdlc.toml` gains `deploy.command` (default `""`): the shell command that performs a release, with `{env}` where the environment name goes, e.g. `./deploy.sh {env}`.
2. `pre_bash` tokenises the command lines of a Bash call (backslash continuations joined, heredoc bodies dropped, quoted strings kept as one token) and, while `RELEASE_APPROVAL` is unset, denies iff one token is a deploy program (its basename without extension is `deploy`, e.g. `deploy`, `./deploy.sh`, `bin/deploy`) and another token equals a gate-tier environment name or `prod`, case-insensitive, also matching the value after `=` and ignoring trailing `;,/`.
3. When `deploy.command` is set, `pre_bash` additionally denies when the command rendered for a gate-tier environment appears as a contiguous token run. A malformed template (unbalanced quote, whitespace only) never crashes the hook.
4. Heredoc bodies, quoted strings (commit messages) and prose never trigger a denial: `git commit -m "deploy(x): ship production"` and a heredoc whose body mentions both words pass. Every command line outside a heredoc is examined, so `set -e` followed by `./deploy.sh production` on the next line is denied.
5. `python3 scripts/sdlc.py deploy record production` is still denied by the fallback (tokens `deploy` and `production`), matching the mechanic's own refusal; with `RELEASE_APPROVAL` set it passes.
6. The denial reason names the matched command or tokens and says the hook is advisory: the mechanic gate in `deploy.check` is what enforces authorization.
7. `agents/verifier.md` and `agents/reviewer.md` instruct: if a hook denies a command, report the denial verbatim and stop; never rewrite, encode, split or relocate the command to get past it.
8. `README.md` Guardrails and `commands/deploy.md` describe the new matching and state that hooks are a second line, not the gate.
9. `deploy.check` and `deploy.record` are unchanged.

# Files
- `README.md`
- `agents/reviewer.md`
- `agents/verifier.md`
- `commands/deploy.md`
- `scripts/sdlc/deploy.py` in [deploy.py](/modules/deploy-py.md)
- `scripts/sdlc/hooks.py` in [hooks.py](/modules/hooks-py.md)
- `scripts/sdlc/project.py` in [docs.py](/modules/docs-py.md)
- `tests/test_hooks.py` in [toml_config](/modules/toml-config.md)

# Review
- Important: 4, Nit: 4

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev, staging

# Documents
- none
