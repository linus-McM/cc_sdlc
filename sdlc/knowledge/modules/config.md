---
type: Module
title: config
description: "Graphify community 87: plugin/scripts/sdlc/project.py, plugin/scripts/sdlc/workflows.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/scripts/sdlc/project.py`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- merge() (plugin/scripts/sdlc/project.py:L141)
- config() (plugin/scripts/sdlc/project.py:L151)
- DEFAULT_CONFIG deep-merged with .sdlc.toml, so every key is always present;… (plugin/scripts/sdlc/project.py:L152)
- enabled() (plugin/scripts/sdlc/workflows.py:L32)
- catalog() (plugin/scripts/sdlc/workflows.py:L43)
- env() (plugin/scripts/sdlc/workflows.py:L47)
- Merge `[workflows.env]` into the local settings; report which keys were written… (plugin/scripts/sdlc/workflows.py:L48)

# Depends on
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [read_json](/modules/read-json.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
