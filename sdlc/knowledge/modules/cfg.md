---
type: Module
title: cfg
description: "Graphify community 75: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:56Z" }
stale_after: "2026-09-23T00:28:56Z"
source_commit: e46d381e2f64fa96bbb6eee6115eba30499cfe2e
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concepts_for() (scripts/sdlc/knowledge.py:L1023)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L1024)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L182)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L183)
- state_path() (scripts/sdlc/knowledge.py:L209)
- read_state() (scripts/sdlc/knowledge.py:L213)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (scripts/sdlc/knowledge.py:L214)
- write_state() (scripts/sdlc/knowledge.py:L221)
- unhook() (scripts/sdlc/knowledge.py:L287)
- bootstrap() (scripts/sdlc/knowledge.py:L420)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L463)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L464)
- artifacts_agree() (scripts/sdlc/knowledge.py:L475)
- status() (scripts/sdlc/knowledge.py:L536)

# Depends on
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [maintain.py](/modules/maintain-py.md)
- [project.py](/modules/project-py.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [staleness](/modules/staleness.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
