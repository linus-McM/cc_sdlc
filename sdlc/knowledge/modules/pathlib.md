---
type: Module
title: pathlib
description: "Graphify community 19: plugin/scripts/hook.py, plugin/scripts/sdlc.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/project.py"
resource: plugin/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: hook, resource: plugin/scripts/hook.py, last_modified: "2026-09-09T15:02:31+10:00", digest: d58f919b42a35f78 }
  - { id: sdlc, resource: plugin/scripts/sdlc.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 17708c9e2035a5ee }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 6cee45ef1d7a0ebb }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-24T11:36:09+10:00", digest: d1e5536892dbd875 }
---

# Files
- `plugin/scripts/hook.py`
- `plugin/scripts/sdlc.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/project.py`

# Symbols
- hook.py (plugin/scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (plugin/scripts/hook.py:L2)
- sdlc.py (plugin/scripts/sdlc.py:L1)
- Launcher: uv run --no-project scripts/sdlc.py <stage> <action> ... (plugin/scripts/sdlc.py:L2)
- cli.py (plugin/scripts/sdlc/cli.py:L1)
- One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]`… (plugin/scripts/sdlc/cli.py:L1)
- parser() (plugin/scripts/sdlc/cli.py:L63)
- main() (plugin/scripts/sdlc/cli.py:L78)
- entry() (plugin/scripts/sdlc/cli.py:L92)
- attempt() (plugin/scripts/sdlc/project.py:L133)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (plugin/scripts/sdlc/project.py:L134)

# Depends on
- [Blocked](/modules/blocked.md)
- [checkpoint.py](/modules/checkpoint-py.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [stages.py](/modules/stages-py.md)
- [test_build_test.py](/modules/test-build-test-py.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- no feature plan names these files
