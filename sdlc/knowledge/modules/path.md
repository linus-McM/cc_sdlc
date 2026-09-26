---
type: Module
title: Path
description: "Graphify community 1: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- docs_dir() (plugin/scripts/sdlc/docs.py:L147)
- open() (plugin/scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (plugin/scripts/sdlc/docs.py:L265)
- documents() (plugin/scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (plugin/scripts/sdlc/docs.py:L280)
- cfg() (plugin/scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (plugin/scripts/sdlc/docs.py:L39)
- skill_dir() (plugin/scripts/sdlc/docs.py:L57)
- installed() (plugin/scripts/sdlc/docs.py:L61)
- node_problem() (plugin/scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (plugin/scripts/sdlc/docs.py:L89)
- tooling() (plugin/scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (plugin/scripts/sdlc/docs.py:L98)
- claude_dir() (plugin/scripts/sdlc/project.py:L124)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (plugin/scripts/sdlc/project.py:L125)

# Depends on
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
