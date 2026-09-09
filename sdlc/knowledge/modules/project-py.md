---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:57:49Z" }
stale_after: "2026-09-23T01:57:49Z"
source_commit: 2297887381a971c1eb7c5a881bc9df5cfba0ea6b
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
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
- Run an external tool without a shell; never raises on a non-zero exit. (scripts/sdlc/project.py:L147)
- run_git() (scripts/sdlc/project.py:L152)
- git() (scripts/sdlc/project.py:L156)
- head_commit() (scripts/sdlc/project.py:L160)
- author() (scripts/sdlc/project.py:L164)
- changed_files() (scripts/sdlc/project.py:L168)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L169)
- read_jsonl() (scripts/sdlc/project.py:L178)
- append_jsonl() (scripts/sdlc/project.py:L182)
- merge() (scripts/sdlc/project.py:L92)

# Depends on
- [cli.py](/modules/cli-py.md)
- [fail](/modules/fail.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [run](/modules/run.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
