## Archify stage documentation

### Why
Every sdlc stage ends with a human accepting a markdown artifact (intent.md, spec.md, plan.md,
review.md, deploy.json). The acceptor reads raw markdown in a terminal or in a PR diff. Nothing
shows the shape of what is being accepted: which systems an intent touches, how the spec's data
moves, which plan steps depend on which, how the deploy tiers and rollback path chain together.
For anything beyond a small change the product owner cannot see the whole picture, so acceptance
is either slow (read everything) or rubber-stamped (read the summary). Reviewers of the PR see
the same wall of text.

The Archify skill (https://github.com/tt-a1i/archify, MIT) already renders validated
architecture, workflow, sequence, dataflow and lifecycle diagrams as standalone HTML from a small
JSON spec. It is installed on this machine by hand under `~/.claude/skills/archify/`, but the
plugin does not know about it: a fresh clone or another developer's machine has Graphify
installed and reported by the SessionStart hook, and Archify absent and silent. Stage commands
cannot rely on a tool the bootstrap does not guarantee.

Affected today: the product owner and tech lead who accept artifacts, the engineer who explains
them, and anyone reviewing the PR that `/sdlc:deploy` opens.

### Artifacts
- sdlc/archify-stage-documentation/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 12
- review: Important: 5, Nit: 11

### Proof
- `uv run pytest` → all green, count rises from 112 by the new tests (10 in `tests/test_docs.py`,
  3 in `tests/test_knowledge.py`, 1 assertion in `tests/test_hooks.py`; the review round added 3 more
  in `tests/test_docs.py`).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests` → no findings.
- `claude plugin validate --strict .` → valid.
- Live: `python3 scripts/sdlc.py knowledge bootstrap` step `archify` `present`, detail
  `Archify skill 2.17.0-dev.1`; `python3 scripts/sdlc.py docs render design` →
  `{"ok": true, "validation": "9/9 showcase, 0 errors, 0 warnings", ...}` and
  `sdlc/archify-stage-documentation/docs/design.html` opens; `python3 scripts/sdlc.py docs check
  design` → `fresh: true`; `SDLC_DOCS=off python3 scripts/sdlc.py docs check design` →
  `skipped`.
- `sdlc build sync` → `unplanned: []`.

### Knowledge
```
sdlc/knowledge/.state.json                         | 121 ++--
 sdlc/knowledge/bands/knowledge-behind.md           |   6 +-
 sdlc/knowledge/bands/knowledge-stale.md            |   6 +-
 sdlc/knowledge/bands/tests-passed.md               |   6 +-
 .../features/archify-stage-documentation.md        | 203 +++++++
 sdlc/knowledge/features/dogfood-fixes-round-two.md |  13 +-
 .../graphify-and-okf-knowledge-base-integration.md |  23 +-
 sdlc/knowledge/features/index.md                   |   1 +
 sdlc/knowledge/features/rehearsal-and-band-nits.md |  15 +-
 sdlc/knowledge/features/release-hook-hardening.md  |  13 +-
 sdlc/knowledge/features/status-next-pointer.md     |  15 +-
 sdlc/knowledge/hubs/docs-py.md                     |  22 +
 sdlc/knowledge/hubs/fail.md                        |  14 +-
 sdlc/knowledge/hubs/hooks-py.md                    |   6 +-
 sdlc/knowledge/hubs/index.md                       |  18 +-
 sdlc/knowledge/hubs/knowledge-py.md                |   8 +-
 sdlc/knowledge/hubs/path-8.md                      |  20 +-
 sdlc/knowledge/hubs/path-9.md                      |  22 +
 sdlc/knowledge/hubs/path.md                        |  12 +-
 sdlc/knowledge/hubs/project-py.md                  |  12 +-
 sdlc/knowledge/hubs/refresh.md                     |  14 +-
 sdlc/knowledge/hubs/run.md                         |  14 +-
 sdlc/knowledge/hubs/test-hooks-py.md               |  18 +-
 sdlc/knowledge/hubs/test-knowledge-py.md           |  14 +-
 sdlc/knowledge/hubs/toml-config.md                 |  18 +-
 sdlc/knowledge/index.md                            |  62 +-
 sdlc/knowledge/lessons/2026-09-07-1.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-07-2.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-07-3.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-07-4.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-1.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-2.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-3.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-4.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-5.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-6.md             |   6 +-
 sdlc/knowledge/lessons/2026-09-08-7.md             |   6 +-
 sdlc/knowledge/log.md                              | 637 +++++++++++++++++++++
 sdlc/knowledge/modules/append-log.md               |  37 ++
 sdlc/knowledge/modules/artifacts-py.md             |  53 +-
 sdlc/knowledge/modules/band-concepts.md            |  45 +-
 sdlc/knowledge/modules/blocked.md                  |  53 ++
 sdlc/knowledge/modules/build-py.md                 |  17 +-
 sdlc/knowledge/modules/bump-version-py.md          |  21 +-
 sdlc/knowledge/modules/cfg.md                      |  44 +-
 sdlc/knowledge/modules/cli-py.md                   |  28 +-
 sdlc/knowledge/modules/communities.md              |  41 ++
 sdlc/knowledge/modules/config.md                   |  52 ++
 sdlc/knowledge/modules/conftest-py.md              |  78 +++
 sdlc/knowledge/modules/deploy-py.md                |  40 +-
 sdlc/knowledge/modules/digests.md                  |  21 +-
 sdlc/knowledge/modules/docs-py.md                  |  83 +++
 sdlc/knowledge/modules/fail.md                     |  49 +-
 sdlc/knowledge/modules/feature-concepts.md         |  49 +-
 sdlc/knowledge/modules/hooks-py.md                 |  47 +-
 sdlc/knowledge/modules/index.md                    |  43 +-
 sdlc/knowledge/modules/init-py.md                  |  47 ++
 sdlc/knowledge/modules/install-hook.md             |  41 +-
 sdlc/knowledge/modules/install-uv.md               |  19 +-
 sdlc/knowledge/modules/knowledge-py.md             |  68 ++-
 sdlc/knowledge/modules/maintain-py.md              |  24 +-
 sdlc/knowledge/modules/parse-frontmatter.md        |   9 +-
 sdlc/knowledge/modules/path.md                     |  66 +--
 sdlc/knowledge/modules/project-py.md               |  63 +-
 sdlc/knowledge/modules/ran.md                      |  37 +-
 sdlc/knowledge/modules/read-json.md                |  28 +-
 sdlc/knowledge/modules/read-state.md               |  31 +-
 sdlc/knowledge/modules/refresh.md                  |  73 +--
 sdlc/knowledge/modules/render.md                   |  19 +-
 sdlc/knowledge/modules/run.md                      | 120 ++--
 sdlc/knowledge/modules/stages-py.md                |  28 +-
 sdlc/knowledge/modules/staleness.md                |  29 +-
 sdlc/knowledge/modules/status.md                   |  52 +-
 sdlc/knowledge/modules/test-artifacts-py.md        |   8 +-
 sdlc/knowledge/modules/test-build-test-py.md       |  46 ++
 sdlc/knowledge/modules/test-deploy-py.md           |  52 ++
 sdlc/knowledge/modules/test-docs-py.md             |  47 ++
 sdlc/knowledge/modules/test-evals-py.md            |   8 +-
 sdlc/knowledge/modules/test-hooks-py.md            |  18 +-
 sdlc/knowledge/modules/test-knowledge-py.md        |  68 ++-
 sdlc/knowledge/modules/test-maintain-py.md         |   8 +-
 sdlc/knowledge/modules/testing-py.md               |  24 +-
 sdlc/knowledge/modules/toml-config.md              |  58 ++
 83 files changed, 2455 insertions(+), 836 deletions(-)
```

### Documents
- build: sdlc/archify-stage-documentation/docs/build.html (9/9 showcase, 0 errors, 0 warnings)
- deploy: sdlc/archify-stage-documentation/docs/deploy.html (9/9 showcase, 0 errors, 0 warnings)
- design: sdlc/archify-stage-documentation/docs/design.html (9/9 showcase, 0 errors, 0 warnings)
- test: sdlc/archify-stage-documentation/docs/test.html (9/9 showcase, 0 errors, 0 warnings)
