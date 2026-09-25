---
type: Module
title: hooks.py
description: "Graphify community 19: plugin/scripts/hook.py, plugin/scripts/sdlc.py, plugin/scripts/sdlc/__init__.py, plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/deploy.py, plugin/"
resource: plugin/scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: hook, resource: plugin/scripts/hook.py, last_modified: "2026-09-09T15:02:31+10:00", digest: d58f919b42a35f78 }
  - { id: sdlc, resource: plugin/scripts/sdlc.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 17708c9e2035a5ee }
  - { id: __init__, resource: plugin/scripts/sdlc/__init__.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 0a6aea3cd6840dbf }
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 6cee45ef1d7a0ebb }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: evals, resource: plugin/scripts/sdlc/evals.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 6019b83ce814d4df }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
  - { id: workflows, resource: plugin/scripts/sdlc/workflows.py, last_modified: "2026-09-19T23:30:10+10:00", digest: e4eefc8f967a3373 }
---

# Files
- `plugin/scripts/hook.py`
- `plugin/scripts/sdlc.py`
- `plugin/scripts/sdlc/__init__.py`
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/evals.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/testing.py`
- `plugin/scripts/sdlc/workflows.py`

# Symbols
- hook.py (plugin/scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (plugin/scripts/hook.py:L2)
- sdlc.py (plugin/scripts/sdlc.py:L1)
- Launcher: uv run --no-project scripts/sdlc.py <stage> <action> ... (plugin/scripts/sdlc.py:L2)
- __init__.py (plugin/scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (plugin/scripts/sdlc/__init__.py:L1)
- build.py (plugin/scripts/sdlc/build.py:L1)
- Build-stage mechanics: red/green TDD log, plan sync, fix lock. (plugin/scripts/sdlc/build.py:L1)
- cli.py (plugin/scripts/sdlc/cli.py:L1)
- One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]`… (plugin/scripts/sdlc/cli.py:L1)
- entry() (plugin/scripts/sdlc/cli.py:L92)
- deploy.py (plugin/scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (plugin/scripts/sdlc/deploy.py:L1)
- evals.py (plugin/scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (plugin/scripts/sdlc/evals.py:L1)
- hooks.py (plugin/scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (plugin/scripts/sdlc/hooks.py:L1)
- testing.py (plugin/scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (plugin/scripts/sdlc/testing.py:L1)
- workflows.py (plugin/scripts/sdlc/workflows.py:L1)
- Stage workflows: the catalog of plugin Workflow scripts and the env that turns… (plugin/scripts/sdlc/workflows.py:L1)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [checkpoint.py](/modules/checkpoint-py.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [post_edit](/modules/post-edit.md)
- [pre_bash](/modules/pre-bash.md)
- [project.py](/modules/project-py.md)
- [propose](/modules/propose.md)
- [read_json](/modules/read-json.md)
- [rel_path](/modules/rel-path.md)
- [Requirements](/modules/requirements.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [watch](/modules/watch.md)

# Inferred
- [post_edit](/modules/post-edit.md)
- [pre_bash](/modules/pre-bash.md)
- [rel_path](/modules/rel-path.md)
- [Requirements](/modules/requirements.md)

# Features
- no feature plan names these files
