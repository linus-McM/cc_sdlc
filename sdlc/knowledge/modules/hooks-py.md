---
type: Module
title: hooks.py
description: "Graphify community 19: plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/knowledge.py, plugin/scripts/sdlc/project.py, sdlc/dogfood-fixes-round-two/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 12afb6df19262a3a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: spec, resource: sdlc/dogfood-fixes-round-two/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 79ecdc49d82b1fc2 }
---

# Files
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/knowledge.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/dogfood-fixes-round-two/spec.md`

# Symbols
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
- main() (plugin/scripts/sdlc/hooks.py:L195)
- deny() (plugin/scripts/sdlc/hooks.py:L26)
- context() (plugin/scripts/sdlc/hooks.py:L36)
- rel_path() (plugin/scripts/sdlc/hooks.py:L40)
- active_feature() (plugin/scripts/sdlc/hooks.py:L53)
- pre_edit() (plugin/scripts/sdlc/hooks.py:L60)
- enabled() (plugin/scripts/sdlc/knowledge.py:L159)
- attempt() (plugin/scripts/sdlc/project.py:L136)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (plugin/scripts/sdlc/project.py:L137)
- Requirements (sdlc/dogfood-fixes-round-two/spec.md:L4)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [build.py](/modules/build-py.md)
- [config](/modules/config.md)
- [fresh_graph](/modules/fresh-graph.md)
- [knowledge.py](/modules/knowledge-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [review](/modules/review.md)
- [status](/modules/status.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [workflows.py](/modules/workflows-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [config](/modules/config.md)
- [watch](/modules/watch.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
