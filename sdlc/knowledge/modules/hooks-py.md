---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:57:33Z" }
stale_after: "2026-09-23T00:57:33Z"
source_commit: a432e14e93d9df64b84d79b6e6d30b2233332f6e
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-09T10:28:52+10:00", digest: e0aa4bc15a604e1d }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 25657fb47810c34d }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 430205b1a1e854c2 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (scripts/hook.py:L2)
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
- Blocked (scripts/sdlc/project.py:L57)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (scripts/sdlc/project.py:L58)
- .__init__() (scripts/sdlc/project.py:L60)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cfg](/modules/cfg.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
