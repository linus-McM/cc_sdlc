---
type: Module
title: docs.py
description: "Graphify community 1: docs/knowledge-measurement.md, plugin/scripts/sdlc/docs.py, plugin/scripts/sdlc/project.py, sdlc/archify-stage-documentation/plan.md, sdlc/archify-stage-documentation/review.md,"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: knowledge-measurement, resource: docs/knowledge-measurement.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 873b51012167b471 }
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: project, resource: plugin/scripts/sdlc/project.py, last_modified: "2026-09-26T16:06:32+10:00", digest: 26698ea0d06e1efe }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: review, resource: sdlc/archify-stage-documentation/review.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c333272d4dfcf4c6 }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:23:50+10:00", digest: 44de9d075d1ea218 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 852d6be4f419faaa }
---

# Files
- `docs/knowledge-measurement.md`
- `plugin/scripts/sdlc/docs.py`
- `plugin/scripts/sdlc/project.py`
- `sdlc/archify-stage-documentation/plan.md`
- `sdlc/archify-stage-documentation/review.md`
- `sdlc/archify-stage-documentation/spec.md`
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- knowledge-measurement.md (docs/knowledge-measurement.md:L1)
- Knowledge layer token measurement (docs/knowledge-measurement.md:L1)
- After a rename and a deletion (docs/knowledge-measurement.md:L20)
- What the numbers say (docs/knowledge-measurement.md:L33)
- Same commit (this repo at 6398504: 159 files, 46 concepts, 697 graph nodes) (docs/knowledge-measurement.md:L9)
- docs.py (plugin/scripts/sdlc/docs.py:L1)
- Stage documents: one Archify HTML diagram per stage, delivered from a Claude-… (plugin/scripts/sdlc/docs.py:L1)
- archify_present() (plugin/scripts/sdlc/docs.py:L107)
- The installed version as the step's detail (no subprocess); StepSkipped when… (plugin/scripts/sdlc/docs.py:L108)
- install_archify() (plugin/scripts/sdlc/docs.py:L118)
- Third-party npm code runs only when the project opted in ([knowledge]… (plugin/scripts/sdlc/docs.py:L119)
- mechanic() (plugin/scripts/sdlc/docs.py:L129)
- CLI handler for `docs <action> <stage>`: the skipped verdict comes before any… (plugin/scripts/sdlc/docs.py:L130)
- handler() (plugin/scripts/sdlc/docs.py:L132)
- docs_dir() (plugin/scripts/sdlc/docs.py:L147)
- sources() (plugin/scripts/sdlc/docs.py:L151)
- sha256() (plugin/scripts/sdlc/docs.py:L155)
- source_bytes() (plugin/scripts/sdlc/docs.py:L163)
- The bytes a document describes, minus what the pipeline itself rewrites after… (plugin/scripts/sdlc/docs.py:L164)
- digests() (plugin/scripts/sdlc/docs.py:L175)
- Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in… (plugin/scripts/sdlc/docs.py:L176)
- receipt_of() (plugin/scripts/sdlc/docs.py:L187)
- The JSON object `deliver --json` prints (pretty-printed over many lines, after… (plugin/scripts/sdlc/docs.py:L188)
- validation() (plugin/scripts/sdlc/docs.py:L199)
- One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0… (plugin/scripts/sdlc/docs.py:L200)
- count() (plugin/scripts/sdlc/docs.py:L204)
- render() (plugin/scripts/sdlc/docs.py:L212)
- check() (plugin/scripts/sdlc/docs.py:L245)
- The stage document exists and was delivered from the sources as they are now… (plugin/scripts/sdlc/docs.py:L246)
- open() (plugin/scripts/sdlc/docs.py:L264)
- Show the acceptor the delivered document; an opener failure is reported, never… (plugin/scripts/sdlc/docs.py:L265)
- documents() (plugin/scripts/sdlc/docs.py:L279)
- One bullet per delivered stage document, with its receipt's validation line;… (plugin/scripts/sdlc/docs.py:L280)
- cfg() (plugin/scripts/sdlc/docs.py:L38)
- The [docs] table; `dir` is validated here because it becomes a path under the… (plugin/scripts/sdlc/docs.py:L39)
- enabled() (plugin/scripts/sdlc/docs.py:L47)
- skill_dir() (plugin/scripts/sdlc/docs.py:L57)
- installed() (plugin/scripts/sdlc/docs.py:L61)
- version() (plugin/scripts/sdlc/docs.py:L65)
- version_tuple() (plugin/scripts/sdlc/docs.py:L73)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (plugin/scripts/sdlc/docs.py:L74)
- node_version() (plugin/scripts/sdlc/docs.py:L79)
- Major version of the `node` on PATH, or None when absent or unparseable. (plugin/scripts/sdlc/docs.py:L80)
- node_problem() (plugin/scripts/sdlc/docs.py:L88)
- Why Node cannot run Archify here, or None. (plugin/scripts/sdlc/docs.py:L89)
- tooling() (plugin/scripts/sdlc/docs.py:L97)
- Why Archify cannot run here, or None when it can. (plugin/scripts/sdlc/docs.py:L98)
- StepSkipped (plugin/scripts/sdlc/project.py:L102)
- This step does not apply here; later steps still run. (plugin/scripts/sdlc/project.py:L103)
- claude_dir() (plugin/scripts/sdlc/project.py:L127)
- Where Claude Code keeps skills: CLAUDE_CONFIG_DIR, else ~/.claude (the same… (plugin/scripts/sdlc/project.py:L128)
- rel() (plugin/scripts/sdlc/project.py:L132)
- StepFailed (plugin/scripts/sdlc/project.py:L98)
- An install step exited non-zero or left its expected result missing. (plugin/scripts/sdlc/project.py:L99)
- archify-stage-documentation/plan.md (sdlc/archify-stage-documentation/plan.md:L1)
- Plan: Archify stage documentation (sdlc/archify-stage-documentation/plan.md:L1)
- Proof (sdlc/archify-stage-documentation/plan.md:L166)
- Order of work (sdlc/archify-stage-documentation/plan.md:L29)
- Files that change (sdlc/archify-stage-documentation/plan.md:L4)
- archify-stage-documentation/review.md (sdlc/archify-stage-documentation/review.md:L1)
- Review: Archify stage documentation (sdlc/archify-stage-documentation/review.md:L1)
- Security (sdlc/archify-stage-documentation/review.md:L11)
- Compliance (sdlc/archify-stage-documentation/review.md:L15)
- Second pass (after review-fixes) (sdlc/archify-stage-documentation/review.md:L22)
- Bugs (sdlc/archify-stage-documentation/review.md:L4)
- archify-stage-documentation/spec.md (sdlc/archify-stage-documentation/spec.md:L1)
- Spec: Archify stage documentation (sdlc/archify-stage-documentation/spec.md:L1)
- Concerns (sdlc/archify-stage-documentation/spec.md:L144)
- Open questions (sdlc/archify-stage-documentation/spec.md:L174)
- Requirements (sdlc/archify-stage-documentation/spec.md:L4)
- Design (sdlc/archify-stage-documentation/spec.md:L96)
- sha256() (tests/conftest.py:L231)
- load() (tests/conftest.py:L57)
- test_docs.py (tests/test_docs.py:L1)
- Archify stage documents: [docs] config, render/check/open mechanics and the… (tests/test_docs.py:L1)
- test_defaults_and_disabled_verdicts() (tests/test_docs.py:L12)
- test_review_and_record_require_documents() (tests/test_docs.py:L123)
- test_open_calls_opener_unless_ci_or_disabled() (tests/test_docs.py:L150)
- test_pr_body_lists_documents() (tests/test_docs.py:L173)
- test_maintain_document_is_ungated_and_reported() (tests/test_docs.py:L187)
- test_stage_commands_carry_the_docs_step() (tests/test_docs.py:L209)
- test_accept_keeps_the_document_fresh_and_stays_idempotent() (tests/test_docs.py:L224)
- test_disabled_verdict_precedes_feature_lookup() (tests/test_docs.py:L234)
- test_docs_dir_is_validated_and_validation_line_is_numbers_only() (tests/test_docs.py:L238)
- test_run_cmd_timeout_and_missing_program_keep_the_completed_process_shape() (tests/test_docs.py:L258)
- source() (tests/test_docs.py:L33)
- test_render_delivers_html_and_receipt() (tests/test_docs.py:L40)
- test_render_failures_are_verbatim() (tests/test_docs.py:L61)
- test_check_reports_fresh_missing_and_stale() (tests/test_docs.py:L75)
- test_accept_requires_fresh_document_per_stage() (tests/test_docs.py:L99)

# Depends on
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [config](/modules/config.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [review](/modules/review.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)

# Inferred
- [Blocked](/modules/blocked.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [conftest.py](/modules/conftest-py.md)
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [knowledge.py](/modules/knowledge-py.md)
- [Order of work](/modules/order-of-work.md)
- [Path](/modules/path-13.md)
- [propose](/modules/propose.md)
- [refresh](/modules/refresh.md)
- [require](/modules/require.md)
- [review](/modules/review.md)
- [status](/modules/status.md)
- [test_plan_design.py](/modules/test-plan-design-py.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
