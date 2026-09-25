---
type: Module
title: artifacts.py
description: "Graphify community 20: plugin/scripts/sdlc/artifacts.py, plugin/scripts/sdlc/deploy.py, plugin/scripts/sdlc/testing.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T23:27:53Z" }
stale_after: "2026-10-09T23:27:53Z"
source_commit: 1348ec2a58c87325a8bcaacd936bc4bc9473c870
sources:
  - { id: artifacts, resource: plugin/scripts/sdlc/artifacts.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3e063b545e7dd897 }
  - { id: deploy, resource: plugin/scripts/sdlc/deploy.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 99b508f60ff0691d }
  - { id: testing, resource: plugin/scripts/sdlc/testing.py, last_modified: "2026-09-24T11:36:09+10:00", digest: f854f76e33b9b57e }
---

# Files
- `plugin/scripts/sdlc/artifacts.py`
- `plugin/scripts/sdlc/deploy.py`
- `plugin/scripts/sdlc/testing.py`

# Symbols
- artifacts.py (plugin/scripts/sdlc/artifacts.py:L1)
- Markdown artifact helpers: intent.md, spec.md, plan.md, review.md share one… (plugin/scripts/sdlc/artifacts.py:L1)
- matches() (plugin/scripts/sdlc/artifacts.py:L100)
- title() (plugin/scripts/sdlc/artifacts.py:L34)
- `# Intent: Claims status` -> `Claims status`. (plugin/scripts/sdlc/artifacts.py:L35)
- sections() (plugin/scripts/sdlc/artifacts.py:L39)
- meta() (plugin/scripts/sdlc/artifacts.py:L49)
- status() (plugin/scripts/sdlc/artifacts.py:L58)
- validate() (plugin/scripts/sdlc/artifacts.py:L62)
- Problems with the document; empty when every required section exists and is… (plugin/scripts/sdlc/artifacts.py:L63)
- glob_regex() (plugin/scripts/sdlc/artifacts.py:L92)
- gitignore-style: `**` spans directories, `*` stays in one segment, a bare name… (plugin/scripts/sdlc/artifacts.py:L93)
- pr_body() (plugin/scripts/sdlc/deploy.py:L134)
- report() (plugin/scripts/sdlc/testing.py:L14)
- knowledge_result() (plugin/scripts/sdlc/testing.py:L42)
- The OKF conformance check as one more feedback-loop row; only conformance… (plugin/scripts/sdlc/testing.py:L43)
- count() (plugin/scripts/sdlc/testing.py:L50)
- Findings tagged `- Important:` / `- Nit:` in a review.md body. (plugin/scripts/sdlc/testing.py:L51)
- findings() (plugin/scripts/sdlc/testing.py:L55)
- review.md validated against REVIEW.md's three passes, with its finding counts. (plugin/scripts/sdlc/testing.py:L56)

# Depends on
- [accept](/modules/accept.md)
- [check](/modules/check-86.md)
- [fail](/modules/fail.md)
- [feature_concepts](/modules/feature-concepts.md)
- [fill](/modules/fill.md)
- [propose](/modules/propose.md)
- [read_json](/modules/read-json.md)
- [render](/modules/render.md)
- [Requirements](/modules/requirements.md)
- [StepSkipped](/modules/stepskipped.md)

# Inferred
- [Blocked](/modules/blocked.md)

# Features
- no feature plan names these files
