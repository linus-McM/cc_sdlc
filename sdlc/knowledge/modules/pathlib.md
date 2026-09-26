---
type: Module
title: pathlib
description: "Graphify community 6: plugin/scripts/sdlc.py, plugin/scripts/sdlc/__init__.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: sdlc, resource: plugin/scripts/sdlc.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 17708c9e2035a5ee }
  - { id: __init__, resource: plugin/scripts/sdlc/__init__.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 0a6aea3cd6840dbf }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 87213d99f94df3bf }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:06:32+10:00", digest: d2d3493a1ed08434 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-26T15:51:45+10:00", digest: 68b187c7a3220c0b }
---

# Files
- `plugin/scripts/sdlc.py`
- `plugin/scripts/sdlc/__init__.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- sdlc.py (plugin/scripts/sdlc.py:L1)
- Launcher: uv run --no-project scripts/sdlc.py <stage> <action> ... (plugin/scripts/sdlc.py:L2)
- __init__.py (plugin/scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (plugin/scripts/sdlc/__init__.py:L1)
- cli.py (plugin/scripts/sdlc/cli.py:L1)
- One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]`… (plugin/scripts/sdlc/cli.py:L1)
- entry() (plugin/scripts/sdlc/cli.py:L94)
- deploy.py (plugin/scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (plugin/scripts/sdlc/deploy.py:L1)
- testing.py (plugin/scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (plugin/scripts/sdlc/testing.py:L1)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [check](/modules/check.md)
- [checkpoint.py](/modules/checkpoint-py.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [findings](/modules/findings.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [packs.py](/modules/packs-py.md)
- [project.py](/modules/project-py.md)
- [propose](/modules/propose.md)
- [review](/modules/review.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [workflows.py](/modules/workflows-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
