---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:24:57Z" }
stale_after: "2026-09-23T00:24:57Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-07T12:20:58+10:00", digest: e0aa4bc15a604e1d }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 25657fb47810c34d }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T08:04:31+10:00", digest: 430205b1a1e854c2 }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: python3 scripts/hook.py <pre-edit|pre-bash|post-edit> (hook JSON… (scripts/hook.py:L2)
- gated() (scripts/sdlc/deploy.py:L45)
- Environments at the `gate` tier in a `[deploy]` config table. (scripts/sdlc/deploy.py:L46)
- hooks.py (scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (scripts/sdlc/hooks.py:L1)
- release_hit() (scripts/sdlc/hooks.py:L101)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (scripts/sdlc/hooks.py:L102)
- pre_bash() (scripts/sdlc/hooks.py:L120)
- post_edit() (scripts/sdlc/hooks.py:L129)
- is_commit() (scripts/sdlc/hooks.py:L142)
- post_bash() (scripts/sdlc/hooks.py:L147)
- After a commit: say when an index has fallen further behind than the configured… (scripts/sdlc/hooks.py:L148)
- main() (scripts/sdlc/hooks.py:L183)
- deny() (scripts/sdlc/hooks.py:L25)
- context() (scripts/sdlc/hooks.py:L35)
- rel_path() (scripts/sdlc/hooks.py:L39)
- active_feature() (scripts/sdlc/hooks.py:L52)
- pre_edit() (scripts/sdlc/hooks.py:L59)
- command_lines() (scripts/sdlc/hooks.py:L77)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (scripts/sdlc/hooks.py:L78)
- tokens() (scripts/sdlc/hooks.py:L90)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (scripts/sdlc/hooks.py:L91)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)

# Inferred
- [cli.py](/modules/cli-py.md)
- [status](/modules/status.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
