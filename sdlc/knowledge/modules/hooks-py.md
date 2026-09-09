---
type: Module
title: hooks.py
description: "Graphify community 4: scripts/hook.py, scripts/sdlc.py, scripts/sdlc/__init__.py, scripts/sdlc/cli.py, scripts/sdlc/deploy.py, scripts/sdlc/hooks.py, scripts/sdlc/knowledge.py, scripts/sdlc/project.py"
resource: scripts
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T01:59:02Z" }
stale_after: "2026-09-23T01:59:02Z"
source_commit: e0523eb3d807827869c761a89aea8117eb781e36
sources:
  - { id: hook, resource: scripts/hook.py, last_modified: "2026-09-09T10:28:52+10:00", digest: e0aa4bc15a604e1d }
  - { id: sdlc, resource: scripts/sdlc.py, last_modified: "2026-09-07T12:20:58+10:00", digest: cdf9f0d1c1e68580 }
  - { id: __init__, resource: scripts/sdlc/__init__.py, last_modified: "2026-09-07T12:20:58+10:00", digest: 0a6aea3cd6840dbf }
  - { id: cli, resource: scripts/sdlc/cli.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 954bd60b902e59ea }
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 25657fb47810c34d }
  - { id: hooks, resource: scripts/sdlc/hooks.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 430205b1a1e854c2 }
  - { id: knowledge, resource: scripts/sdlc/knowledge.py, last_modified: "2026-09-09T10:28:52+10:00", digest: 8da5a1d01eeb439c }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T11:55:13+10:00", digest: 83c9a9a7fba6ace5 }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T08:32:17+10:00", digest: b3939b3fb17f6e1d }
---

# Files
- `scripts/hook.py`
- `scripts/sdlc.py`
- `scripts/sdlc/__init__.py`
- `scripts/sdlc/cli.py`
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/hooks.py`
- `scripts/sdlc/knowledge.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/testing.py`

# Symbols
- hook.py (scripts/hook.py:L1)
- Hook launcher: hook.py <pre-edit|pre-bash|post-edit|post-bash|session-start>… (scripts/hook.py:L2)
- sdlc.py (scripts/sdlc.py:L1)
- Launcher: python3 scripts/sdlc.py <stage> <action> ... (scripts/sdlc.py:L2)
- __init__.py (scripts/sdlc/__init__.py:L1)
- sdlc — deterministic gates for the six-stage AI-native SDLC. Stdlib only. (scripts/sdlc/__init__.py:L1)
- cli.py (scripts/sdlc/cli.py:L1)
- One entry point: `python3 scripts/sdlc.py <stage> <action> [arg]` prints a JSON… (scripts/sdlc/cli.py:L1)
- lifecycle() (scripts/sdlc/cli.py:L18)
- new/check/accept for an artifact stage; only `plan new` takes the positional… (scripts/sdlc/cli.py:L19)
- parser() (scripts/sdlc/cli.py:L54)
- main() (scripts/sdlc/cli.py:L69)
- entry() (scripts/sdlc/cli.py:L80)
- deploy.py (scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (scripts/sdlc/deploy.py:L1)
- record() (scripts/sdlc/deploy.py:L102)
- knowledge_diff() (scripts/sdlc/deploy.py:L120)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (scripts/sdlc/deploy.py:L121)
- pr_body() (scripts/sdlc/deploy.py:L132)
- state() (scripts/sdlc/deploy.py:L17)
- released() (scripts/sdlc/deploy.py:L21)
- readiness() (scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (scripts/sdlc/deploy.py:L26)
- approver() (scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (scripts/sdlc/deploy.py:L41)
- gated() (scripts/sdlc/deploy.py:L45)
- Environments at the `gate` tier in a `[deploy]` config table. (scripts/sdlc/deploy.py:L46)
- check() (scripts/sdlc/deploy.py:L50)
- hooks.py (scripts/sdlc/hooks.py:L1)
- Deterministic guardrails. Invoked by hooks/hooks.json: `hook.py <event>` with… (scripts/sdlc/hooks.py:L1)
- release_hit() (scripts/sdlc/hooks.py:L101)
- What in `cmd` looks like a release to a gated environment, or None. Always: a… (scripts/sdlc/hooks.py:L102)
- pre_bash() (scripts/sdlc/hooks.py:L120)
- post_edit() (scripts/sdlc/hooks.py:L129)
- is_commit() (scripts/sdlc/hooks.py:L142)
- post_bash() (scripts/sdlc/hooks.py:L147)
- After a commit: say when an index has fallen further behind than the configured… (scripts/sdlc/hooks.py:L148)
- session_start() (scripts/sdlc/hooks.py:L158)
- Bootstrap report for the session: check-only unless [knowledge] auto_install is… (scripts/sdlc/hooks.py:L159)
- main() (scripts/sdlc/hooks.py:L181)
- deny() (scripts/sdlc/hooks.py:L25)
- context() (scripts/sdlc/hooks.py:L35)
- rel_path() (scripts/sdlc/hooks.py:L39)
- active_feature() (scripts/sdlc/hooks.py:L52)
- pre_edit() (scripts/sdlc/hooks.py:L59)
- command_lines() (scripts/sdlc/hooks.py:L77)
- Logical command lines: backslash continuations joined, heredoc bodies dropped. (scripts/sdlc/hooks.py:L78)
- tokens() (scripts/sdlc/hooks.py:L90)
- Shell tokens of every command line; quoted prose stays one token, unbalanced… (scripts/sdlc/hooks.py:L91)
- enabled() (scripts/sdlc/knowledge.py:L159)
- Blocked (scripts/sdlc/project.py:L72)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (scripts/sdlc/project.py:L73)
- .__init__() (scripts/sdlc/project.py:L75)
- testing.py (scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (scripts/sdlc/testing.py:L1)
- report() (scripts/sdlc/testing.py:L14)
- knowledge_result() (scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (scripts/sdlc/testing.py:L43)
- count() (scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (scripts/sdlc/testing.py:L51)
- review() (scripts/sdlc/testing.py:L55)

# Depends on
- [docs.py](/modules/docs-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [project.py](/modules/project-py.md)
- [read_state](/modules/read-state.md)
- [refresh](/modules/refresh.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
