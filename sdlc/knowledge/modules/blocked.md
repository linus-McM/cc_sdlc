---
type: Module
title: Blocked
description: "Graphify community 14: plugin/scripts/sdlc.py, plugin/scripts/sdlc/cli.py, plugin/scripts/sdlc/project.py, sdlc/graphify-and-okf-knowledge-base-integration/spec.md"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: sdlc, resource: plugin/scripts/sdlc.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 17708c9e2035a5ee }
  - { id: cli, resource: plugin/scripts/sdlc/cli.py, last_modified: "2026-09-29T08:42:51+10:00", digest: 08531c81958e1bbe }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-29T08:42:51+10:00", digest: f89b1e9a47bc69d8 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 18ddccb80477e245 }
---

# Files
- `plugin/scripts/sdlc.py`
- `plugin/scripts/sdlc/cli.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/graphify-and-okf-knowledge-base-integration/spec.md`

# Symbols
- sdlc.py (plugin/scripts/sdlc.py:L1)
- Launcher: uv run --no-project scripts/sdlc.py <stage> <action> ... (plugin/scripts/sdlc.py:L2)
- cli.py (plugin/scripts/sdlc/cli.py:L1)
- One entry point: `uv run --no-project scripts/sdlc.py <stage> <action> [arg]`… (plugin/scripts/sdlc/cli.py:L1)
- parser() (plugin/scripts/sdlc/cli.py:L66)
- main() (plugin/scripts/sdlc/cli.py:L82)
- entry() (plugin/scripts/sdlc/cli.py:L96)
- Blocked (plugin/scripts/sdlc/project.py:L86)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (plugin/scripts/sdlc/project.py:L87)
- .__init__() (plugin/scripts/sdlc/project.py:L89)
- Changes to existing behaviour (sdlc/graphify-and-okf-knowledge-base-integration/spec.md:L270)

# Depends on
- [build.py](/modules/build-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [maintain.py](/modules/maintain-py.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [workflows.py](/modules/workflows-py.md)

# Inferred
- [accept](/modules/accept.md)
- [build.py](/modules/build-py.md)
- [hooks.py](/modules/hooks-py.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
