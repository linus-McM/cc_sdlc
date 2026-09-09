---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/docs.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:28Z" }
stale_after: "2026-09-23T03:02:28Z"
source_commit: 5f197b911461521ad08675a63cc179623564938a
sources:
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:44:58+10:00", digest: 10270177466cde0a }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: cf02479288a1aba5 }
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
- run_git() (scripts/sdlc/project.py:L196)
- git() (scripts/sdlc/project.py:L200)
- head_commit() (scripts/sdlc/project.py:L204)
- author() (scripts/sdlc/project.py:L208)
- changed_files() (scripts/sdlc/project.py:L212)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L213)
- read_jsonl() (scripts/sdlc/project.py:L226)
- append_jsonl() (scripts/sdlc/project.py:L230)
- StepFailed (scripts/sdlc/project.py:L85)
- An install step exited non-zero or left its expected result missing. (scripts/sdlc/project.py:L86)
- ran() (scripts/sdlc/project.py:L93)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/project.py:L94)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
