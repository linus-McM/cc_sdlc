---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:03:44Z" }
stale_after: "2026-09-23T03:03:44Z"
source_commit: d099eabacf6c4a76cce0780a48e58deaaf2926a4
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 10270177466cde0a }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
---

# Files
- `scripts/sdlc/docs.py`
- `scripts/sdlc/project.py`

# Symbols
- target() (scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (scripts/sdlc/docs.py:L141)
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- claude_dir() (scripts/sdlc/project.py:L114)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (scripts/sdlc/project.py:L115)
- ensure_config() (scripts/sdlc/project.py:L155)
- home() (scripts/sdlc/project.py:L161)
- features() (scripts/sdlc/project.py:L168)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L169)
- feature() (scripts/sdlc/project.py:L174)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L175)
- run_cmd() (scripts/sdlc/project.py:L185)
- Run an external tool without a shell; never raises on a non-zero exit. A… (scripts/sdlc/project.py:L186)
- run_git() (scripts/sdlc/project.py:L197)
- git() (scripts/sdlc/project.py:L201)
- head_commit() (scripts/sdlc/project.py:L205)
- author() (scripts/sdlc/project.py:L209)
- changed_files() (scripts/sdlc/project.py:L213)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L214)
- append_jsonl() (scripts/sdlc/project.py:L231)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [cfg](/modules/cfg.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [ran](/modules/ran.md)
- [refresh](/modules/refresh.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
