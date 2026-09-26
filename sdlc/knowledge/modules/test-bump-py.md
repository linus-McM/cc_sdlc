---
type: Module
title: test_bump.py
description: "Graphify community 41: plugin/scripts/hook.py, tests/test_bump.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: hook, resource: plugin/scripts/hook.py, last_modified: "2026-09-09T15:02:31+10:00", digest: d58f919b42a35f78 }
  - { id: test_bump, resource: tests/test_bump.py, last_modified: "2026-09-09T15:02:31+10:00", digest: b17b9763b42ddb1d }
---

# Files
- `plugin/scripts/hook.py`
- `tests/test_bump.py`

# Symbols
- hook.py (plugin/scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (plugin/scripts/hook.py:L2)
- test_bump.py (tests/test_bump.py:L1)
- tree() (tests/test_bump.py:L12)
- test_bump_parts() (tests/test_bump.py:L21)
- test_write_syncs_every_version_file() (tests/test_bump.py:L29)
- test_main_bumps_only_when_head_equals_base() (tests/test_bump.py:L39)
- test_part_from_labels() (tests/test_bump.py:L49)

# Depends on
- [bump_version.py](/modules/bump-version-py.md)
- [hooks.py](/modules/hooks-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- no feature plan names these files
