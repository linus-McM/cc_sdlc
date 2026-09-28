---
type: Module
title: docs.py
description: "Graphify community 1: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- docs.py (plugin/scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (plugin/scripts/sdlc/docs.py:L1)
- archify_present() (plugin/scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (plugin/scripts/sdlc/docs.py:L108)
- docs_dir() (plugin/scripts/sdlc/docs.py:L147)
- sources() (plugin/scripts/sdlc/docs.py:L151)
- receipt_of() (plugin/scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (plugin/scripts/sdlc/docs.py:L188)
- render() (plugin/scripts/sdlc/docs.py:L212)
- open() (plugin/scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (plugin/scripts/sdlc/docs.py:L265)
- cfg() (plugin/scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (plugin/scripts/sdlc/docs.py:L39)
- enabled() (plugin/scripts/sdlc/docs.py:L47)
- skill_dir() (plugin/scripts/sdlc/docs.py:L57)
- installed() (plugin/scripts/sdlc/docs.py:L61)
- version() (plugin/scripts/sdlc/docs.py:L65)
- node_version() (plugin/scripts/sdlc/docs.py:L79)
- Major version of the `node` on PATH, or None when absent or unparseable. (plugin/scripts/sdlc/docs.py:L80)
- node_problem() (plugin/scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (plugin/scripts/sdlc/docs.py:L89)
- tooling() (plugin/scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (plugin/scripts/sdlc/docs.py:L98)
- claude_dir() (plugin/scripts/sdlc/project.py:L127)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (plugin/scripts/sdlc/project.py:L128)

# Depends on
- [Blocked](/modules/blocked.md)
- [build](/modules/build.md)
- [check](/modules/check.md)
- [fail](/modules/fail.md)
- [Order of work](/modules/order-of-work-44.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
