---
type: Module
title: Path
description: "Graphify community 79: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:01:32Z" }
stale_after: "2026-09-23T02:01:32Z"
source_commit: d8d61950c58abafa13a30ef68be4741e547839ef
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- graph_path() (scripts/sdlc/knowledge.py:L200)
- skill_path() (scripts/sdlc/knowledge.py:L204)
- tool() (scripts/sdlc/knowledge.py:L246)
- uv_install_command() (scripts/sdlc/knowledge.py:L304)
- find_uv() (scripts/sdlc/knowledge.py:L309)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (scripts/sdlc/knowledge.py:L310)
- ran() (scripts/sdlc/knowledge.py:L332)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/knowledge.py:L333)
- install_uv() (scripts/sdlc/knowledge.py:L340)
- install_graphify() (scripts/sdlc/knowledge.py:L344)
- install_skill() (scripts/sdlc/knowledge.py:L348)
- write_ignore() (scripts/sdlc/knowledge.py:L374)
- build_graph() (scripts/sdlc/knowledge.py:L379)
- build_bundle() (scripts/sdlc/knowledge.py:L388)
- pointer_present() (scripts/sdlc/knowledge.py:L393)
- rebuild_log_tail() (scripts/sdlc/knowledge.py:L463)
- Last line of Graphify's rebuild log, read from its tail only (the log is… (scripts/sdlc/knowledge.py:L464)
- artifacts_agree() (scripts/sdlc/knowledge.py:L475)
- plugin_version() (scripts/sdlc/knowledge.py:L564)
- load_graph() (scripts/sdlc/knowledge.py:L568)
- community_labels() (scripts/sdlc/knowledge.py:L579)
- read_json() (scripts/sdlc/project.py:L188)

# Depends on
- [fail](/modules/fail.md)
- [install_hook](/modules/install-hook.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
