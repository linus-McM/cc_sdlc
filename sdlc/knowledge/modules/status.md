---
type: Module
title: status
description: "Graphify community 1: scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T04:39:18Z" }
stale_after: "2026-09-23T04:39:18Z"
source_commit: fa36f67b2362d73bcbf588271a14e115f96d2a3d
sources:
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T12:06:46+10:00", digest: ba620d207f00af60 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
---

# Files
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- concepts_for() (scripts/sdlc/knowledge.py:L1011)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1012)
- enabled() (scripts/sdlc/knowledge.py:L159)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L175)
- unhook() (scripts/sdlc/knowledge.py:L278)
- bootstrap() (scripts/sdlc/knowledge.py:L403)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L447)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L448)
- status() (scripts/sdlc/knowledge.py:L520)
- StepFailed (scripts/sdlc/project.py:L85)
- An install step exited non-zero or left its expected result missing. (scripts/sdlc/project.py:L86)

# Depends on
- [docs.py](/modules/docs-py.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [docs.py](/modules/docs-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
