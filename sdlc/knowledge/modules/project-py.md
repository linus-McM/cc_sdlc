---
type: Module
title: project.py
description: "Graphify community 3: scripts/sdlc.py, scripts/sdlc/artifacts.py, scripts/sdlc/cli.py, scripts/sdlc/docs.py, scripts/sdlc/evals.py, scripts/sdlc/maintain.py, scripts/sdlc/project.py, scripts/sdlc/stag"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:45:02Z" }
stale_after: "2026-09-23T02:45:02Z"
source_commit: 16ce44221e592819936583be6bb11207ce568f21
sources:
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: artifacts, resource: scripts/sdlc/artifacts.py, last_modified: "2026-09-09T08:32:17+10:00", digest: 3e063b545e7dd897 }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T12:44:58+10:00", digest: f71285ffa536f9ea }
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d7a57e7ce569fd72 }
  - { id: evals, resource: scripts/sdlc/evals.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 6019b83ce814d4df }
  - { id: maintain, resource: scripts/sdlc/maintain.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 3aba25cd9e242550 }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T12:44:58+10:00", digest: d046c71e8661e436 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 79822cdce593996c }
---

# Files
- `scripts/sdlc.py`
- `scripts/sdlc/artifacts.py`
- `scripts/sdlc/cli.py`
- `scripts/sdlc/docs.py`
- `scripts/sdlc/evals.py`
- `scripts/sdlc/maintain.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`

# Symbols
- sdlc.py (scripts/sdlc.py:L1)
- Launcher: python3 scripts/sdlc.py <stage> <action> ... (scripts/sdlc.py:L2)
- meta() (scripts/sdlc/artifacts.py:L49)
- status() (scripts/sdlc/artifacts.py:L58)
- cli.py (scripts/sdlc/cli.py:L1)
- One entry point: `python3 scripts/sdlc.py <stage> <action> [arg]` prints a JSON… (scripts/sdlc/cli.py:L1)
- lifecycle() (scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (scripts/sdlc/cli.py:L19)
- parser() (scripts/sdlc/cli.py:L52)
- main() (scripts/sdlc/cli.py:L67)
- entry() (scripts/sdlc/cli.py:L78)
- target() (scripts/sdlc/docs.py:L140)
- The directory that owns the stage document: the feature, or `sdlc/` for the… (scripts/sdlc/docs.py:L141)
- evals.py (scripts/sdlc/evals.py:L1)
- Continuous evals: run each evals/*.json prompt non-interactively, then its… (scripts/sdlc/evals.py:L1)
- run_eval() (scripts/sdlc/evals.py:L15)
- run() (scripts/sdlc/evals.py:L32)
- maintain.py (scripts/sdlc/maintain.py:L1)
- Maintain-stage mechanics: deterministic control bands that close the loop back… (scripts/sdlc/maintain.py:L1)
- ingest() (scripts/sdlc/maintain.py:L113)
- lesson() (scripts/sdlc/maintain.py:L121)
- tier() (scripts/sdlc/maintain.py:L24)
- Western Electric rules on the trailing points against a rolling baseline. 3:… (scripts/sdlc/maintain.py:L25)
- bands() (scripts/sdlc/maintain.py:L54)
- Per-metric bands from sdlc/bands.toml, validated at the config boundary. (scripts/sdlc/maintain.py:L55)
- readings() (scripts/sdlc/maintain.py:L64)
- watch() (scripts/sdlc/maintain.py:L72)
- propose() (scripts/sdlc/maintain.py:L99)
- project.py (scripts/sdlc/project.py:L1)
- Project-level state: config schema, artifact home, git and JSONL helpers, the… (scripts/sdlc/project.py:L1)
- claude_dir() (scripts/sdlc/project.py:L114)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (scripts/sdlc/project.py:L115)
- attempt() (scripts/sdlc/project.py:L123)
- Run a side mechanic without letting it decide the caller's verdict: a Blocked… (scripts/sdlc/project.py:L124)
- merge() (scripts/sdlc/project.py:L131)
- ensure_config() (scripts/sdlc/project.py:L155)
- home() (scripts/sdlc/project.py:L161)
- features() (scripts/sdlc/project.py:L168)
- Every feature directory (one holding an intent.md), sorted by name. (scripts/sdlc/project.py:L169)
- feature() (scripts/sdlc/project.py:L174)
- The named feature directory, or the most recently modified one; Blocked when… (scripts/sdlc/project.py:L175)
- run_cmd() (scripts/sdlc/project.py:L185)
- Run an external tool without a shell; never raises on a non-zero exit. A… (scripts/sdlc/project.py:L186)
- run_git() (scripts/sdlc/project.py:L196)
- git() (scripts/sdlc/project.py:L200)
- head_commit() (scripts/sdlc/project.py:L204)
- author() (scripts/sdlc/project.py:L208)
- changed_files() (scripts/sdlc/project.py:L212)
- Staged, unstaged and untracked paths in one git call. (scripts/sdlc/project.py:L213)
- today() (scripts/sdlc/project.py:L222)
- read_jsonl() (scripts/sdlc/project.py:L226)
- append_jsonl() (scripts/sdlc/project.py:L230)
- fail() (scripts/sdlc/project.py:L81)
- StepFailed (scripts/sdlc/project.py:L85)
- An install step exited non-zero or left its expected result missing. (scripts/sdlc/project.py:L86)
- ran() (scripts/sdlc/project.py:L93)
- Run an install command; StepFailed with its stderr tail when it exits non-zero… (scripts/sdlc/project.py:L94)
- stages.py (scripts/sdlc/stages.py:L1)
- The ordered stage table, and the new/check/accept lifecycle shared by… (scripts/sdlc/stages.py:L1)
- status() (scripts/sdlc/stages.py:L105)
- prerequisite() (scripts/sdlc/stages.py:L18)
- next_command() (scripts/sdlc/stages.py:L23)
- accepted() (scripts/sdlc/stages.py:L27)
- gated() (scripts/sdlc/stages.py:L32)
- The feature directory, provided `artifact` (if any) has been accepted by a… (scripts/sdlc/stages.py:L33)
- create_feature() (scripts/sdlc/stages.py:L42)
- new() (scripts/sdlc/stages.py:L53)
- check() (scripts/sdlc/stages.py:L75)
- accept() (scripts/sdlc/stages.py:L86)
- next_for() (scripts/sdlc/stages.py:L95)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L96)

# Depends on
- [artifacts.py](/modules/artifacts-py.md)
- [band_concepts](/modules/band-concepts.md)
- [build.py](/modules/build-py.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [refresh](/modules/refresh.md)

# Inferred
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
