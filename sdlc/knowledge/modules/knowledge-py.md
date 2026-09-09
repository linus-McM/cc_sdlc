---
type: Module
title: knowledge.py
description: "Graphify community 79: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 7fce16edc7c795cc }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- skill_path() (scripts/sdlc/knowledge.py:L204)
- tool() (scripts/sdlc/knowledge.py:L246)
- uv_install_command() (scripts/sdlc/knowledge.py:L304)
- find_uv() (scripts/sdlc/knowledge.py:L309)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (scripts/sdlc/knowledge.py:L310)
- StepFailed (scripts/sdlc/knowledge.py:L324)
- ran() (scripts/sdlc/knowledge.py:L332)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/knowledge.py:L333)
- install_uv() (scripts/sdlc/knowledge.py:L340)
- install_graphify() (scripts/sdlc/knowledge.py:L344)
- install_skill() (scripts/sdlc/knowledge.py:L348)
- scalar() (scripts/sdlc/knowledge.py:L43)
- flow() (scripts/sdlc/knowledge.py:L53)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- head_first() (scripts/sdlc/knowledge.py:L643)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L644)
- render_concept() (scripts/sdlc/knowledge.py:L860)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L861)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [cli.py](/modules/cli-py.md)
- [communities](/modules/communities.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [append_log](/modules/append-log.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
