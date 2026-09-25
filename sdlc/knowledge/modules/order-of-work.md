---
type: Module
title: Order of work
description: "Graphify community 0: CLAUDE.md, plugin/scripts/sdlc/docs.py, sdlc/archify-stage-documentation/plan.md, sdlc/archify-stage-documentation/spec.md, tests/conftest.py, tests/test_docs.py"
resource: ""
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-25T07:29:30Z" }
stale_after: "2026-10-09T07:29:30Z"
source_commit: dc32a5b78bc303376f02bfe7d43360ae82fa4a82
sources:
  - { id: CLAUDE, resource: CLAUDE.md, last_modified: "2026-09-24T11:36:09+10:00", digest: 04730a8763c1f30b }
  - { id: docs, resource: plugin/scripts/sdlc/docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 10270177466cde0a }
  - { id: plan, resource: sdlc/archify-stage-documentation/plan.md, last_modified: "2026-09-09T15:03:27+10:00", digest: c94b9c651a152ddc }
  - { id: spec, resource: sdlc/archify-stage-documentation/spec.md, last_modified: "2026-09-09T15:03:27+10:00", digest: 6c2e2d1606d0fe5e }
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-24T11:36:09+10:00", digest: 808a9c4cb9a6aeab }
  - { id: test_docs, resource: tests/test_docs.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 852d6be4f419faaa }
---

# Files
- `CLAUDE.md`
- `plugin/scripts/sdlc/docs.py`
- `sdlc/archify-stage-documentation/plan.md`
- `sdlc/archify-stage-documentation/spec.md`
- `tests/conftest.py`
- `tests/test_docs.py`

# Symbols
- CLAUDE.md (CLAUDE.md:L1)
- sdlc plugin (CLAUDE.md:L1)
- Architecture (CLAUDE.md:L12)
- Conventions (CLAUDE.md:L18)
- Things Claude gets wrong (CLAUDE.md:L24)
- Commands (CLAUDE.md:L5)
- version_tuple() (plugin/scripts/sdlc/docs.py:L73)
- Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0). (plugin/scripts/sdlc/docs.py:L74)
- archify-stage-documentation/plan.md (sdlc/archify-stage-documentation/plan.md:L1)
- Plan: Archify stage documentation (sdlc/archify-stage-documentation/plan.md:L1)
- Proof (sdlc/archify-stage-documentation/plan.md:L166)
- Order of work (sdlc/archify-stage-documentation/plan.md:L29)
- Files that change (sdlc/archify-stage-documentation/plan.md:L4)
- archify-stage-documentation/spec.md (sdlc/archify-stage-documentation/spec.md:L1)
- Spec: Archify stage documentation (sdlc/archify-stage-documentation/spec.md:L1)
- Concerns (sdlc/archify-stage-documentation/spec.md:L144)
- Open questions (sdlc/archify-stage-documentation/spec.md:L174)
- Proof (sdlc/archify-stage-documentation/spec.md:L187)
- conftest.py (tests/conftest.py:L1)
- toml_config() (tests/conftest.py:L103)
- _write() (tests/conftest.py:L104)
- repo() (tests/conftest.py:L13)
- FakeTools (tests/conftest.py:L133)
- Handle on the sandbox: `bin/` holds the fake tools and their call log,… (tests/conftest.py:L134)
- .__init__() (tests/conftest.py:L136)
- .calls() (tests/conftest.py:L139)
- Fresh git repo with one commit; cwd and SDLC root point at it. (tests/conftest.py:L14)
- .skill() (tests/conftest.py:L144)
- .skill_dir() (tests/conftest.py:L148)
- .uninstall() (tests/conftest.py:L151)
- sandbox() (tests/conftest.py:L160)
- A bare PATH (a temp `bin/` plus git and the system dirs), temp HOME and… (tests/conftest.py:L161)
- knowledge() (tests/conftest.py:L173)
- Knowledge layer on, with fake `uv` and `graphify` in the sandbox. (tests/conftest.py:L174)
- install_fake_archify() (tests/conftest.py:L213)
- write_fake_node() (tests/conftest.py:L222)
- sha256() (tests/conftest.py:L228)
- docs_tools() (tests/conftest.py:L233)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L234)
- checkpoint_on() (tests/conftest.py:L31)
- Stage-boundary checkpoints on; list it before any `accepted_*` fixture so their… (tests/conftest.py:L32)
- run() (tests/conftest.py:L38)
- Invoke the CLI in-process; return its JSON result dict. (tests/conftest.py:L39)
- _run() (tests/conftest.py:L41)
- load() (tests/conftest.py:L55)
- accepted_intent() (tests/conftest.py:L79)
- accepted_spec() (tests/conftest.py:L87)
- accepted_plan() (tests/conftest.py:L95)
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
- [docs.py](/modules/docs-py.md)
- [fill](/modules/fill.md)
- [__init__.py](/modules/init-py.md)
- [test_hooks.py](/modules/test-hooks-py.md)
- [test_maintain.py](/modules/test-maintain-py.md)

# Inferred
- [artifacts.py](/modules/artifacts-py.md)
- [Blocked](/modules/blocked.md)
- [Components](/modules/components.md)
- [deploy.py](/modules/deploy-py.md)
- [docs.py](/modules/docs-py.md)
- [fail](/modules/fail.md)
- [fill](/modules/fill.md)
- [maintain.py](/modules/maintain-py.md)
- [Order of work](/modules/order-of-work-5.md)
- [pathlib](/modules/pathlib.md)
- [project.py](/modules/project-py.md)
- [refresh](/modules/refresh.md)
- [stages.py](/modules/stages-py.md)
- [status](/modules/status.md)
- [watch](/modules/watch.md)

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
