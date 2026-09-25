---
type: Module
title: knowledge.py
description: "Graphify community 9: plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- knowledge.py (plugin/scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (plugin/scripts/sdlc/knowledge.py:L1)
- graph_path() (plugin/scripts/sdlc/knowledge.py:L192)
- skill_path() (plugin/scripts/sdlc/knowledge.py:L196)
- uv_install_command() (plugin/scripts/sdlc/knowledge.py:L295)
- find_uv() (plugin/scripts/sdlc/knowledge.py:L300)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (plugin/scripts/sdlc/knowledge.py:L301)
- install_uv() (plugin/scripts/sdlc/knowledge.py:L315)
- install_graphify() (plugin/scripts/sdlc/knowledge.py:L319)
- install_skill() (plugin/scripts/sdlc/knowledge.py:L323)
- write_ignore() (plugin/scripts/sdlc/knowledge.py:L349)
- build_graph() (plugin/scripts/sdlc/knowledge.py:L354)
- pointer_present() (plugin/scripts/sdlc/knowledge.py:L368)
- scalar() (plugin/scripts/sdlc/knowledge.py:L43)
- flow() (plugin/scripts/sdlc/knowledge.py:L53)
- dump_frontmatter() (plugin/scripts/sdlc/knowledge.py:L61)
- link() (plugin/scripts/sdlc/knowledge.py:L615)
- head_first() (plugin/scripts/sdlc/knowledge.py:L623)
- `front` with the recommended keys first, then `overrides` in order, then… (plugin/scripts/sdlc/knowledge.py:L624)
- render_concept() (plugin/scripts/sdlc/knowledge.py:L841)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (plugin/scripts/sdlc/knowledge.py:L842)
- reconcile() (plugin/scripts/sdlc/knowledge.py:L890)
- Concept files nothing generated any more: tombstone when every source is… (plugin/scripts/sdlc/knowledge.py:L891)
- ran() (plugin/scripts/sdlc/project.py:L103)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (plugin/scripts/sdlc/project.py:L104)
- StepFailed (plugin/scripts/sdlc/project.py:L95)
- An install step exited non-zero or left its expected result missing. (plugin/scripts/sdlc/project.py:L96)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [Components](/modules/components.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- [append_log](/modules/append-log.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)

# Features
- no feature plan names these files
