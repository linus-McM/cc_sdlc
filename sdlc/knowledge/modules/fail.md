---
type: Module
title: fail
description: "Graphify community 14: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/evals.py, plugin/scripts/sdlc/maintain.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: maintain, resource: plugin/scripts/sdlc/maintain.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/evals.py`
- `plugin/scripts/sdlc/maintain.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- target() (plugin/scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (plugin/scripts/sdlc/docs.py:L141)
- run() (plugin/scripts/sdlc/evals.py:L32)
- maintain.py (plugin/scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (plugin/scripts/sdlc/maintain.py:L1)
- ingest() (plugin/scripts/sdlc/maintain.py:L113)
- lesson() (plugin/scripts/sdlc/maintain.py:L121)
- bands() (plugin/scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (plugin/scripts/sdlc/maintain.py:L55)
- readings() (plugin/scripts/sdlc/maintain.py:L64)
- watch() (plugin/scripts/sdlc/maintain.py:L72)
- propose() (plugin/scripts/sdlc/maintain.py:L99)
- home() (plugin/scripts/sdlc/project.py:L171)
- features() (plugin/scripts/sdlc/project.py:L178)
- Every feature directory (one holding an intent.md), sorted by name. (plugin/scripts/sdlc/project.py:L179)
- feature() (plugin/scripts/sdlc/project.py:L184)
- The named feature directory, or the most recently modified one; Blocked when… (plugin/scripts/sdlc/project.py:L185)
- today() (plugin/scripts/sdlc/project.py:L233)
- fail() (plugin/scripts/sdlc/project.py:L91)

# Depends on
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fill](/modules/fill.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
