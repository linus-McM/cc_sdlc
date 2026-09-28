---
type: Module
title: hooks.py
description: "Graphify community 19: plugin/scripts/hook.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/plan.md, sdlc/dogfood-fixes-round-two/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: hook, resource: plugin/scripts/hook.py, last_modified: "2026-09-09T15:02:31+10:00", digest: d58f919b42a35f78 }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-26T15:09:04+10:00", digest: ddf52a8e990d343f }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: plan, resource: sdlc/dogfood-fixes-round-two/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 74b29c1ae00f8ef4 }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
---

# Files
- `plugin/scripts/hook.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/plan.md`
- `sdlc/dogfood-fixes-round-two/spec.md`

# Symbols
- hook.py (plugin/scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (plugin/scripts/hook.py:L2)
- hooks.py (plugin/scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (plugin/scripts/sdlc/hooks.py:L1)
- post_edit() (plugin/scripts/sdlc/hooks.py:L130)
- is_commit() (plugin/scripts/sdlc/hooks.py:L143)
- post_bash() (plugin/scripts/sdlc/hooks.py:L148)
- After a commit: say when an index has fallen further behind than the configured… (plugin/scripts/sdlc/hooks.py:L149)
- session_start() (plugin/scripts/sdlc/hooks.py:L159)
- Session report: the workflow env merge, then the knowledge bootstrap (check-… (plugin/scripts/sdlc/hooks.py:L160)
- workflow_note() (plugin/scripts/sdlc/hooks.py:L165)
- knowledge_note() (plugin/scripts/sdlc/hooks.py:L174)
- main() (plugin/scripts/sdlc/hooks.py:L198)
- context() (plugin/scripts/sdlc/hooks.py:L36)
- rel_path() (plugin/scripts/sdlc/hooks.py:L40)
- active_feature() (plugin/scripts/sdlc/hooks.py:L53)
- pre_edit() (plugin/scripts/sdlc/hooks.py:L60)
- attempt() (plugin/scripts/sdlc/project.py:L136)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (plugin/scripts/sdlc/project.py:L137)
- Order of work (sdlc/dogfood-fixes-round-two/plan.md:L16)
- Requirements (sdlc/dogfood-fixes-round-two/spec.md:L4)

# Depends on
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [build.py](/modules/build-py.md)
- [cfg](/modules/cfg.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [install_hook](/modules/install-hook.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [pathlib](/modules/pathlib.md)
- [pre_bash](/modules/pre-bash.md)
- [project.py](/modules/project-py.md)
- [select](/modules/select.md)
- [test_deploy.py](/modules/test-deploy-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [workflows.py](/modules/workflows-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [pre_bash](/modules/pre-bash.md)
- [test_deploy.py](/modules/test-deploy-py.md)
- [watch](/modules/watch.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
