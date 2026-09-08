# Intent: Release hook hardening
Author: Linus McManamey. Status: accepted. Risk: high.

## Problem
The pre-bash hook denies any Bash call whose text contains the word "deploy" together with a
gate-tier environment name or "prod". During the first dogfooded feature it blocked four
harmless commands: three heredocs writing prose or tests, and one git commit. Meanwhile the
sdlc:verifier subagent got past it by base64-decoding the environment name inside a Python
heredoc, so the hook is both noisy and trivially bypassed. Neither the agent prompts nor the
docs say that hooks are advisory and the mechanic (`deploy.check`) is the real gate.

## Proposed outcome
The hook denies only real release commands: the configured `deploy.command` rendered for a
gate-tier environment, or, when no command is configured, a first-line command whose tokens
(not prose) are a deploy program plus a gated environment name. Prose, heredoc bodies, commit
messages and `sdlc deploy check` verdict calls pass. The verifier and reviewer agents are told
never to rewrite, encode or split a command to get past a hook, and to report the denial
instead. README and the deploy command describe the hook as a second line, not the gate.

## Affected users and systems
`scripts/sdlc/hooks.py` (`pre_bash`), `scripts/sdlc/project.py` (DEFAULT_CONFIG gains
`deploy.command`), `agents/verifier.md`, `agents/reviewer.md`, `commands/deploy.md`,
`README.md`, `tests/test_hooks.py`. Every Bash call Claude makes in a project using the plugin.

## Constraints
Stdlib only; hook must stay fast (string checks before config or git). Must not weaken the
mechanic gate: `deploy.check` and `deploy.record` keep requiring `RELEASE_APPROVAL`. A hook
cannot be made bypass-proof against an agent that encodes text; the design must say so and
put the guarantee in the mechanic. Risk is high because the change touches the release gate.

## Open questions
none
