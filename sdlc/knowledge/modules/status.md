---
type: Module
title: status
description: "Graphify community 89: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 41ab4ac9324ee352 }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (scripts/sdlc/knowledge.py:L1005)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1006)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L175)
- state_path() (scripts/sdlc/knowledge.py:L200)
- read_state() (scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L205)
- write_state() (scripts/sdlc/knowledge.py:L212)
- unhook() (scripts/sdlc/knowledge.py:L278)
- bootstrap() (scripts/sdlc/knowledge.py:L399)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L441)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L442)
- status() (scripts/sdlc/knowledge.py:L514)

# Depends on
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [install_hook](/modules/install-hook.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [project.py](/modules/project-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
