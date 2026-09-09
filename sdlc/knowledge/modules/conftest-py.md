---
type: Module
title: conftest.py
description: "Graphify community 2: tests/conftest.py"
resource: tests
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.2.2, at: "2026-09-09T03:17:42Z" }
stale_after: "2026-09-23T03:17:42Z"
source_commit: 218a4937bbfd93cc3d6ae744243e90dacb2bf072
sources:
  - { id: conftest, resource: tests/conftest.py, last_modified: "2026-09-09T12:22:23+10:00", digest: 083136847a7b1198 }
---

# Files
- `tests/conftest.py`

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
- docs_tools() (tests/conftest.py:L214)
- Stage documents on, with fake `node` and `npx` in the sandbox and a fake… (tests/conftest.py:L215)
- fill() (tests/conftest.py:L37)
- Replace placeholder bodies under named sections with real text. (tests/conftest.py:L38)
- accepted_intent() (tests/conftest.py:L60)
- accepted_spec() (tests/conftest.py:L68)
- accepted_plan() (tests/conftest.py:L76)

# Depends on
- [__init__.py](/modules/init-py.md)
- [run](/modules/run.md)
- [test_docs.py](/modules/test-docs-py.md)
- [toml_config](/modules/toml-config.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [Archify stage documentation](/features/archify-stage-documentation.md)
- [Graphify and OKF knowledge base integration](/features/graphify-and-okf-knowledge-base-integration.md)
