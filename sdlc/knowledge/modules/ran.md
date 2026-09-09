---
type: Module
title: ran
description: "Graphify community 9: scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:02:33Z" }
stale_after: "2026-09-23T03:02:33Z"
source_commit: 7a6549e2e0a57fe6fe0b1257011d2e78bce58136
sources:
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 9f4a8d0ccc4c7375 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
---

# Files
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`

# Symbols
- skill_path() (scripts/sdlc/knowledge.py:L196)
- uv_install_command() (scripts/sdlc/knowledge.py:L295)
- find_uv() (scripts/sdlc/knowledge.py:L300)
- uv on PATH, else where astral's installer puts it; that directory joins PATH… (scripts/sdlc/knowledge.py:L301)
- install_uv() (scripts/sdlc/knowledge.py:L315)
- install_graphify() (scripts/sdlc/knowledge.py:L319)
- install_skill() (scripts/sdlc/knowledge.py:L323)
- ran() (scripts/sdlc/project.py:L93)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/project.py:L94)

# Depends on
- [cfg](/modules/cfg.md)
- [project.py](/modules/project-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
