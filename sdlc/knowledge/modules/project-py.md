---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:15:57Z" }
stale_after: "2026-09-23T02:15:57Z"
source_commit: 6ea21e5e3cd13550f8e86b9940edfc0da2010101
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
---

# Files
- `scripts/sdlc/project.py`

# Symbols
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- config() (scripts/sdlc/project.py:L102)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (scripts/sdlc/project.py:L103)
- ensure_config() (scripts/sdlc/project.py:L116)
- home() (scripts/sdlc/project.py:L122)
- features() (scripts/sdlc/project.py:L129)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L130)
- feature() (scripts/sdlc/project.py:L135)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L136)
- run_cmd() (scripts/sdlc/project.py:L146)
- Run an external tool without a shell; never raises on a non-zero exit. None… (scripts/sdlc/project.py:L147)
- run_git() (scripts/sdlc/project.py:L155)
- git() (scripts/sdlc/project.py:L159)
- head_commit() (scripts/sdlc/project.py:L163)
- author() (scripts/sdlc/project.py:L167)
- changed_files() (scripts/sdlc/project.py:L171)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L172)
- read_jsonl() (scripts/sdlc/project.py:L181)
- append_jsonl() (scripts/sdlc/project.py:L185)
- merge() (scripts/sdlc/project.py:L92)

# Depends on
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [maintain.py](/modules/maintain-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
