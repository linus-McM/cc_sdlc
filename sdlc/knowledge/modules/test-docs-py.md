---
type: Module
title: test_docs.py
description: "Graphify community 2: tests/conftest.py, tests/test_docs.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T03:03:44Z" }
stale_after: "2026-09-23T03:03:44Z"
source_commit: d099eabacf6c4a76cce0780a48e58deaaf2926a4
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T13:02:29+10:00", digest: e16eeb63f14bb91e }
---

# Files
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- conftest.py (tests/conftest.py:L1)
- FakeTools (tests/conftest.py:L114)
- Handle on the sandbox: `bin/` holds the fake tools and their call log,… (tests/conftest.py:L115)
- .__init__() (tests/conftest.py:L117)
- .calls() (tests/conftest.py:L120)
- .skill() (tests/conftest.py:L125)
- .skill_dir() (tests/conftest.py:L129)
- repo() (tests/conftest.py:L13)
- .uninstall() (tests/conftest.py:L132)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L14)
- sandbox() (tests/conftest.py:L141)
- A bare PATH (a temp `bin/` plus git and the system dirs), temp HOME and… (tests/conftest.py:L142)
- knowledge() (tests/conftest.py:L154)
- Knowledge layer on, with fake `uv` and `graphify` in the sandbox. (tests/conftest.py:L155)
- install_fake_archify() (tests/conftest.py:L194)
- write_fake_node() (tests/conftest.py:L203)
- sha256() (tests/conftest.py:L209)
- docs_tools() (tests/conftest.py:L214)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L215)
- fill() (tests/conftest.py:L37)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L38)
- load() (tests/conftest.py:L45)
- accepted_intent() (tests/conftest.py:L60)
- accepted_spec() (tests/conftest.py:L68)
- accepted_plan() (tests/conftest.py:L76)
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
- [fail](/modules/fail.md)
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Inferred
- [run](/modules/run.md)
- [toml_config](/modules/toml-config.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
