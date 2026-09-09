---
type: Module
title: cfg
description: "Graphify community 74: scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:06:51Z" }
stale_after: "2026-09-23T02:06:51Z"
source_commit: 7470298f4fecfcb461736faefdc6244e8983e4de
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:06:46+10:00", digest: 7fce16edc7c795cc }
---

# Files
- `scripts/sdlc/knowledge.py`

# Symbols
- concept_files() (scripts/sdlc/knowledge.py:L1024)
- check() (scripts/sdlc/knowledge.py:L1037)
- Three separate lists: official OKF v0.2 conformance (the only one that fails),… (scripts/sdlc/knowledge.py:L1038)
- policy_findings() (scripts/sdlc/knowledge.py:L1065)
- Organisational rules, stricter than the spec and reported apart from it. (scripts/sdlc/knowledge.py:L1066)
- as_actor() (scripts/sdlc/knowledge.py:L1079)
- OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare… (scripts/sdlc/knowledge.py:L1080)
- publish() (scripts/sdlc/knowledge.py:L1085)
- Append a verification event to the feature's concept; only a human: actor… (scripts/sdlc/knowledge.py:L1086)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L182)
- The [knowledge] table; `bundle` is validated here because it becomes a path, a… (scripts/sdlc/knowledge.py:L183)
- bundle_dir() (scripts/sdlc/knowledge.py:L196)
- unhook() (scripts/sdlc/knowledge.py:L287)
- bootstrap() (scripts/sdlc/knowledge.py:L421)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L470)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L471)
- verified_events() (scripts/sdlc/knowledge.py:L488)
- `verified` as a list: the spec lets a single event be written as a bare mapping. (scripts/sdlc/knowledge.py:L489)
- is_stale() (scripts/sdlc/knowledge.py:L494)
- bundle_counts() (scripts/sdlc/knowledge.py:L531)
- status() (scripts/sdlc/knowledge.py:L543)
- now_iso() (scripts/sdlc/knowledge.py:L566)
- last_modified() (scripts/sdlc/knowledge.py:L829)
- Last commit date per source path from one `git log --name-only` over all of… (scripts/sdlc/knowledge.py:L830)

# Depends on
- [append_log](/modules/append-log.md)
- [fail](/modules/fail.md)
- [hooks.py](/modules/hooks-py.md)
- [install_hook](/modules/install-hook.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
