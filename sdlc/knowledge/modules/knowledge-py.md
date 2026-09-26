---
type: Module
title: knowledge.py
description: "Graphify community 15: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- knowledge.py (plugin/scripts/sdlc/knowledge.py:L1)
- Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle… (plugin/scripts/sdlc/knowledge.py:L1)
- policy_findings() (plugin/scripts/sdlc/knowledge.py:L1050)
- Organisational rules, stricter than the spec and reported apart from it. (plugin/scripts/sdlc/knowledge.py:L1051)
- uv_install_command() (plugin/scripts/sdlc/knowledge.py:L295)
- find_uv() (plugin/scripts/sdlc/knowledge.py:L300)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (plugin/scripts/sdlc/knowledge.py:L301)
- install_uv() (plugin/scripts/sdlc/knowledge.py:L315)
- install_graphify() (plugin/scripts/sdlc/knowledge.py:L319)
- write_ignore() (plugin/scripts/sdlc/knowledge.py:L349)
- pointer_present() (plugin/scripts/sdlc/knowledge.py:L368)
- scalar() (plugin/scripts/sdlc/knowledge.py:L43)
- is_stale() (plugin/scripts/sdlc/knowledge.py:L475)
- flow() (plugin/scripts/sdlc/knowledge.py:L53)
- dump_frontmatter() (plugin/scripts/sdlc/knowledge.py:L61)
- head_first() (plugin/scripts/sdlc/knowledge.py:L627)
- `front` with the recommended keys first, then `overrides` in order, then… (plugin/scripts/sdlc/knowledge.py:L628)
- signature() (plugin/scripts/sdlc/knowledge.py:L806)
- Content identity: the builder's keys (present on either side) plus the body;… (plugin/scripts/sdlc/knowledge.py:L807)
- render_concept() (plugin/scripts/sdlc/knowledge.py:L845)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (plugin/scripts/sdlc/knowledge.py:L846)

# Depends on
- [append_log](/modules/append-log.md)
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [Components](/modules/components.md)
- [Digests](/modules/digests.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [Order of work](/modules/order-of-work.md)
- [packs.py](/modules/packs-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path-13.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)

# Inferred
- [append_log](/modules/append-log.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path-13.md)
- [refresh](/modules/refresh.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
