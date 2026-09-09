---
type: Module
title: docs.py
description: "Graphify community 87: scripts/sdlc/deploy.py, scripts/sdlc/docs.py, scripts/sdlc/project.py, scripts/sdlc/stages.py, scripts/sdlc/testing.py"
resource: scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T03:17:42Z" }
stale_after: "2026-09-23T03:17:42Z"
source_commit: 218a4937bbfd93cc3d6ae744243e90dacb2bf072
sources:
  - { id: deploy, resource: scripts/sdlc/deploy.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 13fece25897d5a38 }
  - { id: docs, resource: scripts/sdlc/docs.py, last_modified: "2026-09-09T13:02:29+10:00", digest: 10270177466cde0a }
  - { id: project, resource: scripts/sdlc/project.py, last_modified: "2026-09-09T13:02:29+10:00", digest: cf02479288a1aba5 }
  - { id: stages, resource: scripts/sdlc/stages.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 79822cdce593996c }
  - { id: testing, resource: scripts/sdlc/testing.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 6ae5daae0d475089 }
---

# Files
- `scripts/sdlc/deploy.py`
- `scripts/sdlc/docs.py`
- `scripts/sdlc/project.py`
- `scripts/sdlc/stages.py`
- `scripts/sdlc/testing.py`

# Symbols
- deploy.py (scripts/sdlc/deploy.py:L1)
- Deploy-stage mechanics: per-environment tiers, rollback rehearsal, release… (scripts/sdlc/deploy.py:L1)
- record() (scripts/sdlc/deploy.py:L102)
- knowledge_diff() (scripts/sdlc/deploy.py:L121)
- `git diff --stat main...HEAD` for the OKF bundle, so reviewers see what the… (scripts/sdlc/deploy.py:L122)
- pr_body() (scripts/sdlc/deploy.py:L133)
- state() (scripts/sdlc/deploy.py:L17)
- released() (scripts/sdlc/deploy.py:L21)
- readiness() (scripts/sdlc/deploy.py:L25)
- Reasons the feature is not ready for any environment; empty when ready. (scripts/sdlc/deploy.py:L26)
- approver() (scripts/sdlc/deploy.py:L40)
- The named release manager from RELEASE_APPROVAL, or empty. (scripts/sdlc/deploy.py:L41)
- check() (scripts/sdlc/deploy.py:L50)
- rehearse() (scripts/sdlc/deploy.py:L76)
- Run deploy.rollback in a throwaway detached worktree of HEAD; the checkout… (scripts/sdlc/deploy.py:L77)
- docs.py (scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (scripts/sdlc/docs.py:L1)
- archify_present() (scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (scripts/sdlc/docs.py:L108)
- install_archify() (scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (scripts/sdlc/docs.py:L119)
- docs_dir() (scripts/sdlc/docs.py:L147)
- sources() (scripts/sdlc/docs.py:L151)
- sha256() (scripts/sdlc/docs.py:L155)
- source_bytes() (scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (scripts/sdlc/docs.py:L164)
- digests() (scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (scripts/sdlc/docs.py:L176)
- receipt_of() (scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (scripts/sdlc/docs.py:L188)
- validation() (scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (scripts/sdlc/docs.py:L200)
- render() (scripts/sdlc/docs.py:L212)
- check() (scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (scripts/sdlc/docs.py:L246)
- open() (scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (scripts/sdlc/docs.py:L265)
- documents() (scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (scripts/sdlc/docs.py:L280)
- cfg() (scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (scripts/sdlc/docs.py:L39)
- enabled() (scripts/sdlc/docs.py:L47)
- skill_dir() (scripts/sdlc/docs.py:L57)
- installed() (scripts/sdlc/docs.py:L61)
- version() (scripts/sdlc/docs.py:L65)
- version_tuple() (scripts/sdlc/docs.py:L73)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (scripts/sdlc/docs.py:L74)
- node_version() (scripts/sdlc/docs.py:L79)
- Major version of the `node` on PATH, or None when absent or unparseable. (scripts/sdlc/docs.py:L80)
- node_problem() (scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (scripts/sdlc/docs.py:L89)
- tooling() (scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (scripts/sdlc/docs.py:L98)
- rel() (scripts/sdlc/project.py:L119)
- read_json() (scripts/sdlc/project.py:L237)
- Blocked (scripts/sdlc/project.py:L73)
- A gate refused; `.verdict` is the JSON dict the CLI prints. (scripts/sdlc/project.py:L74)
- .__init__() (scripts/sdlc/project.py:L76)
- fail() (scripts/sdlc/project.py:L81)
- StepSkipped (scripts/sdlc/project.py:L89)
- This step does not apply here; later steps still run. (scripts/sdlc/project.py:L90)
- next_for() (scripts/sdlc/stages.py:L95)
- The one /sdlc command to run next; the deploy gates decide when test and deploy… (scripts/sdlc/stages.py:L96)
- testing.py (scripts/sdlc/testing.py:L1)
- Test-stage mechanics: run the feedback loop, write test-report.json, validate… (scripts/sdlc/testing.py:L1)
- report() (scripts/sdlc/testing.py:L14)
- run() (scripts/sdlc/testing.py:L18)
- knowledge_result() (scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (scripts/sdlc/testing.py:L43)
- count() (scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (scripts/sdlc/testing.py:L51)
- findings() (scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (scripts/sdlc/testing.py:L56)
- review() (scripts/sdlc/testing.py:L66)
- The test stage's exit: valid findings plus a fresh stage document. (scripts/sdlc/testing.py:L67)

# Depends on
- [hooks.py](/modules/hooks-py.md)
- [__init__.py](/modules/init-py.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Path](/modules/path.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [status](/modules/status.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Dogfood fixes round two](/features/dogfood-fixes-round-two.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
- [Rehearsal and band nits](/features/rehearsal-and-band-nits.md)
- [Release hook hardening](/features/release-hook-hardening.md)
- [Status next pointer](/features/status-next-pointer.md)
