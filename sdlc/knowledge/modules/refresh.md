---
type: Module
title: refresh
description: "Graphify community 35: plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- publish() (plugin/scripts/sdlc/knowledge.py:L1081)
- Append a verification event to the feature's concept; only a human: actor… (plugin/scripts/sdlc/knowledge.py:L1082)
- split_document() (plugin/scripts/sdlc/knowledge.py:L149)
- tool() (plugin/scripts/sdlc/knowledge.py:L237)
- build_bundle() (plugin/scripts/sdlc/knowledge.py:L373)
- plugin_version() (plugin/scripts/sdlc/knowledge.py:L565)
- dump_frontmatter() (plugin/scripts/sdlc/knowledge.py:L61)
- link() (plugin/scripts/sdlc/knowledge.py:L629)
- head_first() (plugin/scripts/sdlc/knowledge.py:L637)
- `front` with the recommended keys first, then `overrides` in order, then… (plugin/scripts/sdlc/knowledge.py:L638)
- content_keys() (plugin/scripts/sdlc/knowledge.py:L812)
- last_modified() (plugin/scripts/sdlc/knowledge.py:L824)
- Last commit date per source path from one `git log --name-only` over all of… (plugin/scripts/sdlc/knowledge.py:L825)
- render_concept() (plugin/scripts/sdlc/knowledge.py:L855)
- Frontmatter plus body; `reset` (a source changed) drops the concept back to… (plugin/scripts/sdlc/knowledge.py:L856)
- reconcile() (plugin/scripts/sdlc/knowledge.py:L904)
- Concept files nothing generated any more: tombstone when every source is… (plugin/scripts/sdlc/knowledge.py:L905)
- refresh() (plugin/scripts/sdlc/knowledge.py:L936)
- now_iso() (plugin/scripts/sdlc/project.py:L232)

# Depends on
- [bootstrap](/modules/bootstrap.md)
- [build](/modules/build.md)
- [cfg](/modules/cfg.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [Digests](/modules/digests.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [install_hook](/modules/install-hook.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [parse_frontmatter](/modules/parse-frontmatter.md)
- [Path](/modules/path.md)
- [read_json](/modules/read-json.md)
- [watch](/modules/watch.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
