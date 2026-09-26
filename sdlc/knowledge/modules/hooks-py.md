---
type: Module
title: hooks.py
description: "Graphify community 6: plugin/scripts/hook.py, plugin/scripts/sdlc/hooks.py"
resource: plugin/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: hook, resource: plugin/scripts/hook.py, last_modified: "2026-09-09T15:02:31+10:00", digest: d58f919b42a35f78 }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
---

# Files
- `plugin/scripts/hook.py`
- `plugin/scripts/sdlc/hooks.py`

# Symbols
- hook.py (plugin/scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (plugin/scripts/hook.py:L2)
- hooks.py (plugin/scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (plugin/scripts/sdlc/hooks.py:L1)
- is_commit() (plugin/scripts/sdlc/hooks.py:L143)
- post_bash() (plugin/scripts/sdlc/hooks.py:L148)
- After a commit: say when an index has fallen further behind than the configured… (plugin/scripts/sdlc/hooks.py:L149)
- session_start() (plugin/scripts/sdlc/hooks.py:L159)
- Session report: the workflow env merge, then the knowledge bootstrap (check-… (plugin/scripts/sdlc/hooks.py:L160)
- workflow_note() (plugin/scripts/sdlc/hooks.py:L165)
- main() (plugin/scripts/sdlc/hooks.py:L195)
- context() (plugin/scripts/sdlc/hooks.py:L36)

# Depends on
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [config](/modules/config.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work-45.md)
- [pathlib](/modules/pathlib.md)
- [post_edit](/modules/post-edit.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [post_edit](/modules/post-edit.md)

# Features
- no feature plan names these files
