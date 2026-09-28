---
type: Module
title: cfg
description: "Graphify community 30: plugin/README.md, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/knowledge.py"
resource: plugin
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: README, resource: plugin/README.md, last_modified: "2026-09-29T08:42:51+10:00", digest: c7e6b88df8690ad4 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-26T16:35:55+10:00", digest: d2d3493a1ed08434 }
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-29T08:42:51+10:00", digest: d350848efe5d7fe2 }
---

# Files
- `plugin/README.md`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- Knowledge (Graphify + OKF) (plugin/README.md:L36)
- knowledge_diff() (plugin/scripts/sdlc/deploy.py:L127)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (plugin/scripts/sdlc/deploy.py:L128)
- concepts_for() (plugin/scripts/sdlc/knowledge.py:L1026)
- Project-relative module concept paths describing `rel`, from the file map the… (plugin/scripts/sdlc/knowledge.py:L1027)
- enabled() (plugin/scripts/sdlc/knowledge.py:L159)
- when_enabled() (plugin/scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (plugin/scripts/sdlc/knowledge.py:L164)
- cfg() (plugin/scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (plugin/scripts/sdlc/knowledge.py:L175)
- unhook() (plugin/scripts/sdlc/knowledge.py:L288)

# Depends on
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [watch](/modules/watch.md)
- [when_enabled](/modules/when-enabled.md)

# Inferred
- [accept](/modules/accept.md)
- [refresh](/modules/refresh.md)

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
