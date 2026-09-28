---
type: Module
title: knowledge.py
description: "Graphify community 15: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- render() (plugin/scripts/sdlc/artifacts.py:L88)
- knowledge.py (plugin/scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (plugin/scripts/sdlc/knowledge.py:L1)
- policy_findings() (plugin/scripts/sdlc/knowledge.py:L1061)
- Organisational rules, stricter than the spec and reported apart from it. (plugin/scripts/sdlc/knowledge.py:L1062)
- skill_path() (plugin/scripts/sdlc/knowledge.py:L196)
- uv_install_command() (plugin/scripts/sdlc/knowledge.py:L305)
- find_uv() (plugin/scripts/sdlc/knowledge.py:L310)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (plugin/scripts/sdlc/knowledge.py:L311)
- install_uv() (plugin/scripts/sdlc/knowledge.py:L325)
- install_graphify() (plugin/scripts/sdlc/knowledge.py:L329)
- install_skill() (plugin/scripts/sdlc/knowledge.py:L333)
- write_ignore() (plugin/scripts/sdlc/knowledge.py:L359)
- pointer_present() (plugin/scripts/sdlc/knowledge.py:L378)
- write_pointer() (plugin/scripts/sdlc/knowledge.py:L385)
- scalar() (plugin/scripts/sdlc/knowledge.py:L43)
- rebuild_log_tail() (plugin/scripts/sdlc/knowledge.py:L461)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (plugin/scripts/sdlc/knowledge.py:L462)
- is_stale() (plugin/scripts/sdlc/knowledge.py:L485)
- flow() (plugin/scripts/sdlc/knowledge.py:L53)
- index_lines() (plugin/scripts/sdlc/knowledge.py:L870)
- `* [Title](link) - description` per concept, sorted by title; sub-indexes link… (plugin/scripts/sdlc/knowledge.py:L871)
- write_indexes() (plugin/scripts/sdlc/knowledge.py:L877)
- append_log() (plugin/scripts/sdlc/knowledge.py:L888)

# Depends on
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cfg](/modules/cfg.md)
- [Components](/modules/components.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [packs.py](/modules/packs-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
