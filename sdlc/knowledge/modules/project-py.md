---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc/artifacts.py, scripts/sdlc/maintain.py, scripts/sdlc/project.py, scripts/sdlc/stages.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:55:17Z" }
stale_after: "2026-09-23T01:55:17Z"
source_commit: 0972bddc57871b4600edb500118b597e83638fbc
sources:
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: maintain, resource: scripts/sdlc/maintain.py, last_modified: "2026-09-08T15:49:55+10:00", digest: 75052069898694d5 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 54e5024a991ef45d }
---

# Files
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/maintain.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`

# Symbols
- artifacts.py (scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (scripts/sdlc/artifacts.py:L1)
- matches() (scripts/sdlc/artifacts.py:L100)
- title() (scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (scripts/sdlc/artifacts.py:L35)
- sections() (scripts/sdlc/artifacts.py:L39)
- set_section() (scripts/sdlc/artifacts.py:L44)
- meta() (scripts/sdlc/artifacts.py:L49)
- set_meta() (scripts/sdlc/artifacts.py:L54)
- status() (scripts/sdlc/artifacts.py:L58)
- validate() (scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (scripts/sdlc/artifacts.py:L63)
- first_line() (scripts/sdlc/artifacts.py:L74)
- The first filled line of a section body, skipping template placeholders. (scripts/sdlc/artifacts.py:L75)
- glob_regex() (scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (scripts/sdlc/artifacts.py:L93)
- maintain.py (scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (scripts/sdlc/maintain.py:L1)
- ingest() (scripts/sdlc/maintain.py:L109)
- lesson() (scripts/sdlc/maintain.py:L117)
- tier() (scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (scripts/sdlc/maintain.py:L25)
- bands() (scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (scripts/sdlc/maintain.py:L55)
- readings() (scripts/sdlc/maintain.py:L64)
- watch() (scripts/sdlc/maintain.py:L72)
- propose() (scripts/sdlc/maintain.py:L95)
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- ensure_config() (scripts/sdlc/project.py:L116)
- home() (scripts/sdlc/project.py:L122)
- features() (scripts/sdlc/project.py:L129)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L130)
- feature() (scripts/sdlc/project.py:L135)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L136)
- run_cmd() (scripts/sdlc/project.py:L146)
- Run an external tool without a shell; never raises on a non-zero exit. (scripts/sdlc/project.py:L147)
- run_git() (scripts/sdlc/project.py:L152)
- git() (scripts/sdlc/project.py:L156)
- head_commit() (scripts/sdlc/project.py:L160)
- author() (scripts/sdlc/project.py:L164)
- changed_files() (scripts/sdlc/project.py:L168)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L169)
- today() (scripts/sdlc/project.py:L174)
- read_jsonl() (scripts/sdlc/project.py:L178)
- append_jsonl() (scripts/sdlc/project.py:L182)
- attempt() (scripts/sdlc/project.py:L84)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (scripts/sdlc/project.py:L85)
- merge() (scripts/sdlc/project.py:L92)
- stages.py (scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (scripts/sdlc/stages.py:L1)
- status() (scripts/sdlc/stages.py:L104)
- prerequisite() (scripts/sdlc/stages.py:L18)
- next_command() (scripts/sdlc/stages.py:L23)
- accepted() (scripts/sdlc/stages.py:L27)
- gated() (scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (scripts/sdlc/stages.py:L33)
- create_feature() (scripts/sdlc/stages.py:L42)
- new() (scripts/sdlc/stages.py:L53)
- check() (scripts/sdlc/stages.py:L75)
- accept() (scripts/sdlc/stages.py:L86)
- next_for() (scripts/sdlc/stages.py:L94)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L95)

# Depends on
- [append_log](/modules/append-log.md)
- [build.py](/modules/build-py.md)
- [cli.py](/modules/cli-py.md)
- [communities](/modules/communities.md)
- [config](/modules/config.md)
- [deploy.py](/modules/deploy-py.md)
- [fail](/modules/fail.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [run](/modules/run.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
