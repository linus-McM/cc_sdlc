---
type: Module
title: conftest.py
description: "Graphify community 2: tests/conftest.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:11:11Z" }
stale_after: "2026-09-23T02:11:11Z"
source_commit: b6ac2e811acbc23d7c5c8119fd8dd5532b43ccd0
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T11:57:45+10:00", digest: 48ea2a2a85d58a00 }
---

# Files
- `tests/conftest.py`

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

# Depends on
- [__init__.py](/modules/init-py.md)
- [run](/modules/run.md)
- [test_deploy.py](/modules/test-deploy-py.md)
- [test_docs.py](/modules/test-docs-py.md)
- [toml_config](/modules/toml-config.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
