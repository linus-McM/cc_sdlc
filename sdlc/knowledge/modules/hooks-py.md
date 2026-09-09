---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc/build.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T01:00:09Z" }
stale_after: "2026-09-23T01:00:09Z"
source_commit: f4b7a7e7c7ca48d51fac20696ba496746da179e6
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-09T10:28:52+10:00", digest: e0aa4bc15a604e1d }
  - { id: build, resource: scripts/sdlc/build.py, last_modified: "2026-09-08T09:22:42+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 25657fb47810c34d }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 430205b1a1e854c2 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc/build.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (scripts/hook.py:L2)
- build.py (scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (scripts/sdlc/build.py:L1)
- run_cmd() (scripts/sdlc/build.py:L15)
- cycles() (scripts/sdlc/build.py:L23)
- Completed red->green pairs, matched per step name in order. (scripts/sdlc/build.py:L24)
- tdd() (scripts/sdlc/build.py:L35)
- planned_files() (scripts/sdlc/build.py:L57)
- is_sdlc_owned() (scripts/sdlc/build.py:L62)
- sync() (scripts/sdlc/build.py:L66)
- fix() (scripts/sdlc/build.py:L78)
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
- config() (scripts/sdlc/project.py:L87)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (scripts/sdlc/project.py:L88)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [cfg](/modules/cfg.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)

# Inferred
- [cli.py](/modules/cli-py.md)

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
