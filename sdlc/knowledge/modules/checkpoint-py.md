---
type: Module
title: checkpoint.py
description: "Graphify community 24: plugin/scripts/sdlc/checkpoint.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: checkpoint, resource: plugin/scripts/sdlc/checkpoint.py, last_modified: "2026-09-24T11:36:09+10:00", digest: caeae3619aaf1c38 }
---

# Files
- `plugin/scripts/sdlc/checkpoint.py`

# Symbols
- checkpoint.py (plugin/scripts/sdlc/checkpoint.py:L1)
- Stage-boundary checkpoints: `cli.main` commits the SDLC home directory and… (plugin/scripts/sdlc/checkpoint.py:L1)
- enabled() (plugin/scripts/sdlc/checkpoint.py:L17)
- pending() (plugin/scripts/sdlc/checkpoint.py:L24)
- Changed files under the SDLC home directory or `[checkpoint] paths`; git-… (plugin/scripts/sdlc/checkpoint.py:L25)
- busy() (plugin/scripts/sdlc/checkpoint.py:L29)
- subject() (plugin/scripts/sdlc/checkpoint.py:L34)
- `<stage>(<slug>): <action> — <file>` for a feature's artifact, `<stage>: ...`… (plugin/scripts/sdlc/checkpoint.py:L35)
- commit() (plugin/scripts/sdlc/checkpoint.py:L43)
- Commit what the boundary produced plus anything generated since the last one.… (plugin/scripts/sdlc/checkpoint.py:L44)

# Depends on
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
