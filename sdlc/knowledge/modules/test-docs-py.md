---
type: Module
title: test_docs.py
description: "Graphify community 91: tests/conftest.py, tests/test_docs.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:17:09Z" }
stale_after: "2026-09-23T02:17:09Z"
source_commit: 5f6707036a44f201af1092fdfdde11b3cdba2f6f
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:15:53+10:00", digest: 0a4917a47b89aec7 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T12:11:08+10:00", digest: 5186a666aee97601 }
---

# Files
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- sha256() (tests/conftest.py:L207)
- load() (tests/conftest.py:L45)
- test_docs.py (tests/test_docs.py:L1)
- Archify stage documents: [docs] config, render/check/open mechanics and the… (tests/test_docs.py:L1)
- test_review_and_record_require_documents() (tests/test_docs.py:L117)
- test_defaults_and_disabled_verdicts() (tests/test_docs.py:L12)
- test_open_calls_opener_unless_ci_or_disabled() (tests/test_docs.py:L152)
- test_pr_body_lists_documents() (tests/test_docs.py:L175)
- test_maintain_document_is_ungated_and_reported() (tests/test_docs.py:L189)
- test_stage_commands_carry_the_docs_step() (tests/test_docs.py:L211)
- source() (tests/test_docs.py:L33)
- test_render_delivers_html_and_receipt() (tests/test_docs.py:L40)
- test_render_failures_are_verbatim() (tests/test_docs.py:L60)
- test_check_reports_fresh_missing_and_stale() (tests/test_docs.py:L74)
- test_accept_requires_fresh_document_per_stage() (tests/test_docs.py:L93)

# Depends on
- [build.py](/modules/build-py.md)
- [conftest.py](/modules/conftest-py.md)

# Inferred
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
