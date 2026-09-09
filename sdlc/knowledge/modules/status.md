---
type: Module
title: status
description: "Graphify community 75: scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.0, at: "2026-09-09T00:28:34Z" }
stale_after: "2026-09-23T00:28:34Z"
source_commit: 614af23c7f6ad2aa72305090f08b8c7fff243ba5
sources:
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T08:04:31+10:00", digest: 430205b1a1e854c2 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:18:34+10:00", digest: 8da5a1d01eeb439c }
---

# Files
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`

# Symbols
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- enabled() (scripts/sdlc/knowledge.py:L159)
- when_enabled() (scripts/sdlc/knowledge.py:L163)
- Gate a public mechanic on the layer being on; `default` is the verdict (or… (scripts/sdlc/knowledge.py:L164)
- cfg() (scripts/sdlc/knowledge.py:L179)
- unhook() (scripts/sdlc/knowledge.py:L269)
- bootstrap() (scripts/sdlc/knowledge.py:L398)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L439)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L440)
- status() (scripts/sdlc/knowledge.py:L504)
- concepts_for() (scripts/sdlc/knowledge.py:L983)
- Project-relative module concept paths describing `rel`, from the file map the… (scripts/sdlc/knowledge.py:L984)

# Depends on
- [hooks.py](/modules/hooks-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Path](/modules/path.md)
- [post_commit_path](/modules/post-commit-path.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
