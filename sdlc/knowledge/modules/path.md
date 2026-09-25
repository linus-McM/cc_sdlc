---
type: Module
title: Path
description: "Graphify community 12: plugin/scripts/sdlc/knowledge.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: knowledge, resource: plugin/scripts/sdlc/knowledge.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 9f4a8d0ccc4c7375 }
---

# Files
- `plugin/scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (plugin/scripts/sdlc/knowledge.py:L1005)
- concepts_for() (plugin/scripts/sdlc/knowledge.py:L1011)
- Project-relative module concept paths describing `rel`, from the file map the… (plugin/scripts/sdlc/knowledge.py:L1012)
- cfg() (plugin/scripts/sdlc/knowledge.py:L174)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (plugin/scripts/sdlc/knowledge.py:L175)
- bundle_dir() (plugin/scripts/sdlc/knowledge.py:L188)
- graph_path() (plugin/scripts/sdlc/knowledge.py:L192)
- state_path() (plugin/scripts/sdlc/knowledge.py:L200)
- read_state() (plugin/scripts/sdlc/knowledge.py:L204)
- `.state.json`, or `{"_error": reason}` when it exists but cannot be read (a… (plugin/scripts/sdlc/knowledge.py:L205)
- write_state() (plugin/scripts/sdlc/knowledge.py:L212)
- build_graph() (plugin/scripts/sdlc/knowledge.py:L354)
- bundle_present() (plugin/scripts/sdlc/knowledge.py:L358)
- A bundle counts only when it was built from the graph that exists now (an… (plugin/scripts/sdlc/knowledge.py:L359)
- graph_commit() (plugin/scripts/sdlc/knowledge.py:L439)
- artifacts_agree() (plugin/scripts/sdlc/knowledge.py:L459)
- staleness() (plugin/scripts/sdlc/knowledge.py:L483)
- The cheap part of status: how far each index is behind HEAD and why a clean… (plugin/scripts/sdlc/knowledge.py:L484)
- status() (plugin/scripts/sdlc/knowledge.py:L520)
- community_labels() (plugin/scripts/sdlc/knowledge.py:L566)

# Depends on
- [check](/modules/check-86.md)
- [config](/modules/config.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [read_json](/modules/read-json.md)
- [refresh](/modules/refresh.md)
- [Requirements](/modules/requirements.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- no feature plan names these files
