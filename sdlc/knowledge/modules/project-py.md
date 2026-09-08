---
type: Module
title: project.py
description: "Graphify community 67: scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-08T22:12:23Z" }
stale_after: "2026-09-22T22:12:23Z"
source_commit: b7fff727fc81eeb9a3aa4e92ba2c81caed3a3a56
sources:
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T07:32:46+10:00", digest: cd1977e43e9bb660 }
---

# Files
- `scripts/sdlc/project.py`

# Symbols
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- run_cmd() (scripts/sdlc/project.py:L108)
- Run an external tool without a shell; never raises on a non-zero exit. (scripts/sdlc/project.py:L109)
- run_git() (scripts/sdlc/project.py:L114)
- git() (scripts/sdlc/project.py:L118)
- author() (scripts/sdlc/project.py:L122)
- changed_files() (scripts/sdlc/project.py:L126)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L127)
- read_jsonl() (scripts/sdlc/project.py:L136)
- append_jsonl() (scripts/sdlc/project.py:L140)
- write_json() (scripts/sdlc/project.py:L155)
- merge() (scripts/sdlc/project.py:L68)
- config() (scripts/sdlc/project.py:L75)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present. (scripts/sdlc/project.py:L76)
- ensure_config() (scripts/sdlc/project.py:L81)

# Depends on
- [cli.py](/modules/cli-py.md)
- [fail](/modules/fail.md)
- [maintain.py](/modules/maintain-py.md)
- [stages.py](/modules/stages-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
