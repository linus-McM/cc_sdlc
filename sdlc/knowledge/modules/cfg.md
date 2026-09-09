---
type: Module
title: cfg
description: "Graphify community 89: scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:22:28Z" }
stale_after: "2026-09-23T02:22:28Z"
source_commit: 596440e8a2a56052df06112cb01e32437adfaa8c
sources:
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: ba620d207f00af60 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 418f9277e7848a02 }
---

# Files
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- concepts_for() (scripts/sdlc/knowledge.py:L1005)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1006)
- enabled() (scripts/sdlc/knowledge.py:L159)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L175)
- unhook() (scripts/sdlc/knowledge.py:L278)
- bootstrap() (scripts/sdlc/knowledge.py:L399)
- when_enabled() (scripts/sdlc/project.py:L101)
- Gate a layer's public mechanics on `enabled(root)`; `default` is the verdict… (scripts/sdlc/project.py:L102)

# Depends on
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)

# Inferred
- [docs.py](/modules/docs-py.md)
- [project.py](/modules/project-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
