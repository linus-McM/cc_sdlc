---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc/artifacts.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-09T10:28:52+10:00", digest: e0aa4bc15a604e1d }
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 13fece25897d5a38 }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: ba620d207f00af60 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (scripts/hook.py:L2)
- matches() (scripts/sdlc/artifacts.py:L100)
- glob_regex() (scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (scripts/sdlc/artifacts.py:L93)
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
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- main() (scripts/sdlc/hooks.py:L181)
- deny() (scripts/sdlc/hooks.py:L25)
- context() (scripts/sdlc/hooks.py:L35)
- rel_path() (scripts/sdlc/hooks.py:L39)
- active_feature() (scripts/sdlc/hooks.py:L52)
- pre_edit() (scripts/sdlc/hooks.py:L59)
- command_lines() (scripts/sdlc/hooks.py:L77)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (scripts/sdlc/hooks.py:L78)
- tokens() (scripts/sdlc/hooks.py:L90)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (scripts/sdlc/hooks.py:L91)
- enabled() (scripts/sdlc/knowledge.py:L159)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [status](/modules/status.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
