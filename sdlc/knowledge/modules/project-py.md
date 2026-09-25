---
type: Module
title: project.py
description: "Graphify community 14: plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- target() (plugin/scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (plugin/scripts/sdlc/docs.py:L141)
- project.py (plugin/scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (plugin/scripts/sdlc/project.py:L1)
- claude_dir() (plugin/scripts/sdlc/project.py:L124)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (plugin/scripts/sdlc/project.py:L125)
- merge() (plugin/scripts/sdlc/project.py:L141)
- config() (plugin/scripts/sdlc/project.py:L151)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (plugin/scripts/sdlc/project.py:L152)
- ensure_config() (plugin/scripts/sdlc/project.py:L165)
- home() (plugin/scripts/sdlc/project.py:L171)
- features() (plugin/scripts/sdlc/project.py:L178)
- Every feature directory (one holding an intent.md), sorted by name. (plugin/scripts/sdlc/project.py:L179)
- feature() (plugin/scripts/sdlc/project.py:L184)
- The named feature directory, or the most recently modified one; Blocked when… (plugin/scripts/sdlc/project.py:L185)
- head_commit() (plugin/scripts/sdlc/project.py:L215)
- changed_files() (plugin/scripts/sdlc/project.py:L223)
- Staged, unstaged and untracked paths in one git call, limited to `paths` when… (plugin/scripts/sdlc/project.py:L224)

# Depends on
- [Blocked](/modules/blocked.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [pathlib](/modules/pathlib.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
