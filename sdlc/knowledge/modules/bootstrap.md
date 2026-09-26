---
type: Module
title: bootstrap
description: "Graphify community 10: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/hooks.py, plugin/scripts/sdlc/knowledge.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T05:22:30Z" }
stale_after: "2026-10-10T05:22:30Z"
source_commit: c5f64f8d3b9b5e3268754f626b7f2e958fd6415e
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: hooks, resource: plugin/scripts/sdlc/hooks.py, last_modified: "2026-09-19T13:08:30+10:00", digest: 40334c1872956197 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/hooks.py`
- `plugin/scripts/sdlc/knowledge.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- title() (plugin/scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (plugin/scripts/sdlc/artifacts.py:L35)
- knowledge_note() (plugin/scripts/sdlc/hooks.py:L174)
- enabled() (plugin/scripts/sdlc/knowledge.py:L159)
- graph_path() (plugin/scripts/sdlc/knowledge.py:L192)
- bundle_present() (plugin/scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (plugin/scripts/sdlc/knowledge.py:L359)
- bootstrap() (plugin/scripts/sdlc/knowledge.py:L403)
- graph_commit() (plugin/scripts/sdlc/knowledge.py:L439)
- artifacts_agree() (plugin/scripts/sdlc/knowledge.py:L459)
- behind() (plugin/scripts/sdlc/knowledge.py:L475)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (plugin/scripts/sdlc/knowledge.py:L476)
- staleness() (plugin/scripts/sdlc/knowledge.py:L483)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L484)
- load_graph() (plugin/scripts/sdlc/knowledge.py:L555)
- graphify-and-okf-knowledge-base-integration/spec.md (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Spec: Graphify and OKF knowledge base integration (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L1)
- Design (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L136)
- Data flow (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L195)
- Interfaces (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L217)
- Concerns (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L279)
- Open questions (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L308)
- Requirements (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L5)

# Depends on
- [Blocked](/modules/blocked.md)
- [Components](/modules/components.md)
- [config](/modules/config.md)
- [fill](/modules/fill.md)
- [Order of work](/modules/order-of-work-5.md)
- [refresh](/modules/refresh.md)
- [rehearse](/modules/rehearse.md)

# Inferred
- [cli.py](/modules/cli-py.md)
- [docs.py](/modules/docs-py.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path.md)
- [post_edit](/modules/post-edit.md)
- [refresh](/modules/refresh.md)
- [StepSkipped](/modules/stepskipped.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
