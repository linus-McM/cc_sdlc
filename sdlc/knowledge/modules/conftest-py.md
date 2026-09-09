---
type: Module
title: conftest.py
description: "Graphify community 82: tests/conftest.py, tests/test_docs.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:02:49Z" }
stale_after: "2026-09-23T02:02:49Z"
source_commit: f15b143d1ce08297fc13142247be8dc7f63d478f
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T11:57:45+10:00", digest: 48ea2a2a85d58a00 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T12:02:46+10:00", digest: 62c629bf92c915a8 }
---

# Files
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- conftest.py (tests/conftest.py:L1)
- FakeTools (tests/conftest.py:L127)
- .__init__() (tests/conftest.py:L128)
- repo() (tests/conftest.py:L13)
- .calls() (tests/conftest.py:L131)
- .skill() (tests/conftest.py:L136)
- .uninstall() (tests/conftest.py:L139)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L14)
- knowledge() (tests/conftest.py:L145)
- Knowledge layer on, with fake `uv` and `graphify` on an otherwise bare PATH… (tests/conftest.py:L146)
- install_fake_archify() (tests/conftest.py:L192)
- write_fake_node() (tests/conftest.py:L201)
- sha256() (tests/conftest.py:L207)
- FakeDocs (tests/conftest.py:L211)
- .__init__() (tests/conftest.py:L212)
- .skill_dir() (tests/conftest.py:L216)
- .calls() (tests/conftest.py:L219)
- .uninstall() (tests/conftest.py:L223)
- docs_tools() (tests/conftest.py:L232)
- Stage documents on, with fake `node` and `npx` on an otherwise bare PATH (plus… (tests/conftest.py:L233)
- fill() (tests/conftest.py:L37)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L38)
- accepted_intent() (tests/conftest.py:L50)
- accepted_spec() (tests/conftest.py:L67)
- accepted_plan() (tests/conftest.py:L81)
- test_docs.py (tests/test_docs.py:L1)
- Archify stage documents: [docs] config, render/check/open mechanics and the… (tests/test_docs.py:L1)
- test_review_and_record_require_documents() (tests/test_docs.py:L116)
- test_defaults_and_disabled_verdicts() (tests/test_docs.py:L12)
- test_open_calls_opener_unless_ci_or_disabled() (tests/test_docs.py:L151)
- test_pr_body_lists_documents() (tests/test_docs.py:L174)
- source() (tests/test_docs.py:L33)
- test_render_delivers_html_and_receipt() (tests/test_docs.py:L40)
- test_render_failures_are_verbatim() (tests/test_docs.py:L60)
- test_check_reports_fresh_missing_and_stale() (tests/test_docs.py:L74)
- test_accept_requires_fresh_document_per_stage() (tests/test_docs.py:L92)

# Depends on
- [cli.py](/modules/cli-py.md)
- [fail](/modules/fail.md)
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Inferred
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
