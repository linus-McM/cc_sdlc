---
type: Module
title: Path
description: "Graphify community 75: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T12:08:42+10:00", digest: 9f7d0b83d716857f }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:06:46+10:00", digest: f517b9ce73f6af08 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L200)
- skill_path() (scripts/sdlc/knowledge.py:L204)
- tool() (scripts/sdlc/knowledge.py:L246)
- ran() (scripts/sdlc/knowledge.py:L332)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/knowledge.py:L333)
- install_graphify() (scripts/sdlc/knowledge.py:L344)
- install_skill() (scripts/sdlc/knowledge.py:L348)
- write_ignore() (scripts/sdlc/knowledge.py:L374)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- bundle_present() (scripts/sdlc/knowledge.py:L383)
- A bundle counts only when it was built from the graph that exists now (an… (scripts/sdlc/knowledge.py:L384)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- pointer_present() (scripts/sdlc/knowledge.py:L393)
- graph_commit() (scripts/sdlc/knowledge.py:L462)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L470)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L471)
- artifacts_agree() (scripts/sdlc/knowledge.py:L482)
- behind() (scripts/sdlc/knowledge.py:L498)
- Commits from `since` to HEAD; None when git cannot resolve `since` (shallow… (scripts/sdlc/knowledge.py:L499)
- staleness() (scripts/sdlc/knowledge.py:L506)
- The cheap part of status: how far each index is behind HEAD and why a clean… (scripts/sdlc/knowledge.py:L507)
- plugin_version() (scripts/sdlc/knowledge.py:L574)
- load_graph() (scripts/sdlc/knowledge.py:L578)
- community_labels() (scripts/sdlc/knowledge.py:L589)
- read_json() (scripts/sdlc/project.py:L191)

# Depends on
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [project.py](/modules/project-py.md)
- [read_state](/modules/read-state.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
