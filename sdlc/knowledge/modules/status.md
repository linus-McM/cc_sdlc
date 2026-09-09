---
type: Module
title: status
description: "Graphify community 89: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:15:57Z" }
stale_after: "2026-09-23T02:15:57Z"
source_commit: 6ea21e5e3cd13550f8e86b9940edfc0da2010101
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (scripts/sdlc/knowledge.py:L1034)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1035)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L182)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L183)
- state_path() (scripts/sdlc/knowledge.py:L209)
- read_state() (scripts/sdlc/knowledge.py:L213)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L214)
- write_state() (scripts/sdlc/knowledge.py:L221)
- unhook() (scripts/sdlc/knowledge.py:L287)
- bootstrap() (scripts/sdlc/knowledge.py:L421)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L470)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L471)
- status() (scripts/sdlc/knowledge.py:L543)

# Depends on
- [communities](/modules/communities.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [staleness](/modules/staleness.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
