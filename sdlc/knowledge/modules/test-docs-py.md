---
type: Module
title: test_docs.py
description: "Graphify community 7: tests/conftest.py, tests/test_docs.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T04:39:18Z" }
stale_after: "2026-09-23T04:39:18Z"
source_commit: fa36f67b2362d73bcbf588271a14e115f96d2a3d
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T13:02:29+10:00", digest: e16eeb63f14bb91e }
---

# Files
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- sha256() (tests/conftest.py:L209)
- load() (tests/conftest.py:L45)
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
- [__init__.py](/modules/init-py.md)

# Inferred
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
