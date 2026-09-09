---
type: Module
title: knowledge.py
description: "Graphify community 72: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:05:41Z" }
stale_after: "2026-09-23T01:05:41Z"
source_commit: 84e34c7e5ba9bdec7e2f26ef69f1f509c15b7046
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- knowledge.py (scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (scripts/sdlc/knowledge.py:L1)
- policy_findings() (scripts/sdlc/knowledge.py:L1058)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1059)
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
- is_stale() (scripts/sdlc/knowledge.py:L487)
- flow() (scripts/sdlc/knowledge.py:L53)
- dump_frontmatter() (scripts/sdlc/knowledge.py:L61)
- head_first() (scripts/sdlc/knowledge.py:L636)
- `front` with the recommended keys first, then `overrides` in order, then… (scripts/sdlc/knowledge.py:L637)
- render_concept() (scripts/sdlc/knowledge.py:L853)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (scripts/sdlc/knowledge.py:L854)
- index_lines() (scripts/sdlc/knowledge.py:L868)
- `* [Title](link) - description` per concept, sorted by title; sub-indexes link… (scripts/sdlc/knowledge.py:L869)
- write_indexes() (scripts/sdlc/knowledge.py:L875)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [bump_version.py](/modules/bump-version-py.md)
- [cfg](/modules/cfg.md)
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [feature_concepts](/modules/feature-concepts.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [testing.py](/modules/testing-py.md)

# Inferred
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
