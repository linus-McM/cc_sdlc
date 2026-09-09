---
type: Module
title: project.py
description: "Graphify community 67: scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:35:57Z" }
stale_after: "2026-09-22T22:35:57Z"
source_commit: c6f9a22e23b0bee7134aa1e1709c5feef8673f82
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 15fdd6685d1225c1 }
---

# Files
- `scripts/sdlc/project.py`

# Symbols
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- ensure_config() (scripts/sdlc/project.py:L101)
- home() (scripts/sdlc/project.py:L107)
- features() (scripts/sdlc/project.py:L114)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L115)
- feature() (scripts/sdlc/project.py:L120)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L121)
- run_cmd() (scripts/sdlc/project.py:L131)
- Run an external tool without a shell; never raises on a non-zero exit. (scripts/sdlc/project.py:L132)
- run_git() (scripts/sdlc/project.py:L137)
- git() (scripts/sdlc/project.py:L141)
- head_commit() (scripts/sdlc/project.py:L145)
- author() (scripts/sdlc/project.py:L149)
- changed_files() (scripts/sdlc/project.py:L153)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L154)
- read_jsonl() (scripts/sdlc/project.py:L163)
- append_jsonl() (scripts/sdlc/project.py:L167)
- merge() (scripts/sdlc/project.py:L77)

# Depends on
- [cli.py](/modules/cli-py.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
