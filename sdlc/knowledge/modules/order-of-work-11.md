---
type: Module
title: Order of work
description: "Graphify community 11: sdlc/archify-stage-documentation/plan.md, tests/conftest.py, tests/test_docs.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 44de9d075d1ea218 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 852d6be4f419faaa }
---

# Files
- `sdlc/archify-stage-documentation/plan.md`
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- Order of work (sdlc/archify-stage-documentation/plan.md:L29)
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
- [conftest.py](/modules/conftest-py.md)
- [pathlib](/modules/pathlib.md)
- [test_hooks.py](/modules/test-hooks-py.md)

# Inferred
- [accept](/modules/accept.md)
- [Blocked](/modules/blocked.md)
- [bootstrap](/modules/bootstrap.md)
- [check](/modules/check.md)
- [Components](/modules/components.md)
- [conftest.py](/modules/conftest-py.md)
- [docs.py](/modules/docs-py.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work.md)
- [packs.py](/modules/packs-py.md)
- [pathlib](/modules/pathlib.md)
- [StepSkipped](/modules/stepskipped.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
