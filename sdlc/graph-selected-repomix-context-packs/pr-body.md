## graph-selected repomix context packs

### Why
Each stage's parallel Workflow agents (intent-scout, design-panel, plan-critic, review,
release-readiness, diagnose) work out their own view of the codebase at run time: each one reads
`sdlc/knowledge/index.md`, runs `graphify query`, then greps and reads files on its own
(`plugin/commands/*.md:8`, `plugin/workflows/*.js`). The same files are re-read by every agent in a
panel, and the agents of one stage are not guaranteed to judge the same code. The graph already
knows which files a change touches, but nothing turns that into a file set, and nothing packs those
files so a panel can share them. Repomix is used only by hand, to pack external reference repos
(`sdlc/archify-stage-documentation/references/README.md`). An earlier measurement found the
knowledge bundle plus `graphify query` cost 1.06x the tokens of raw reads
(`docs/knowledge-measurement.md`), so the map alone has not yet paid for itself.

### Artifacts
- sdlc/graph-selected-repomix-context-packs/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 19
- review: Important: 3, Nit: 5

### Proof
- `uv run pytest` all green, including the new `tests/test_packs.py` and the gate tests in
  `test_plan_design.py`, `test_build_test.py`, `test_knowledge.py`, `test_workflows.py`.
- `uv run ruff check plugin/scripts scripts tests && uv run ruff format --check plugin/scripts scripts
  tests`: zero findings.
- `claude plugin validate --strict plugin && claude plugin validate --strict .`: both pass.
- Manual on this repo: `sdlc knowledge pack build --slug graph-selected-repomix-context-packs` returns
  `ok: true` with a path under `graphify-out/packs/` and `git status --porcelain` shows no pack file.

### Knowledge
```
sdlc/knowledge/.state.json                         |  291 ++++
 sdlc/knowledge/bands/index.md                      |    5 +
 sdlc/knowledge/bands/knowledge-behind.md           |   21 +
 sdlc/knowledge/bands/knowledge-stale.md            |   21 +
 sdlc/knowledge/bands/tests-passed.md               |   21 +
 .../features/archify-stage-documentation.md        |  204 +++
 sdlc/knowledge/features/dogfood-fixes-round-two.md |   67 +
 .../graph-selected-repomix-context-packs.md        |  219 +++
 .../graphify-and-okf-knowledge-base-integration.md |  317 +++++
 sdlc/knowledge/features/index.md                   |    9 +
 sdlc/knowledge/features/rehearsal-and-band-nits.md |   74 ++
 sdlc/knowledge/features/release-hook-hardening.md  |   66 +
 sdlc/knowledge/features/status-next-pointer.md     |   61 +
 sdlc/knowledge/hubs/accept.md                      |   22 +
 sdlc/knowledge/hubs/blocked.md                     |   17 +
 sdlc/knowledge/hubs/bundle-dir.md                  |   16 +
 sdlc/knowledge/hubs/config.md                      |   16 +
 sdlc/knowledge/hubs/deploy-py.md                   |   16 +
 sdlc/knowledge/hubs/docs-py.md                     |   22 +
 sdlc/knowledge/hubs/enabled.md                     |   16 +
 sdlc/knowledge/hubs/fail.md                        |   22 +
 sdlc/knowledge/hubs/hooks-py.md                    |   17 +
 sdlc/knowledge/hubs/index.md                       |   12 +
 sdlc/knowledge/hubs/knowledge-py.md                |   22 +
 sdlc/knowledge/hubs/packs-py.md                    |   22 +
 sdlc/knowledge/hubs/path-8.md                      |   16 +
 sdlc/knowledge/hubs/path-9.md                      |   17 +
 sdlc/knowledge/hubs/path.md                        |   22 +
 sdlc/knowledge/hubs/plays.md                       |   16 +
 sdlc/knowledge/hubs/project-py.md                  |   22 +
 sdlc/knowledge/hubs/refresh.md                     |   22 +
 sdlc/knowledge/hubs/run.md                         |   17 +
 sdlc/knowledge/hubs/status.md                      |   16 +
 sdlc/knowledge/hubs/test-hooks-py.md               |   16 +
 sdlc/knowledge/hubs/test-knowledge-py.md           |   22 +
 sdlc/knowledge/hubs/test-packs-py.md               |   22 +
 sdlc/knowledge/hubs/toml-config.md                 |   17 +
 sdlc/knowledge/index.md                            |  103 ++
 sdlc/knowledge/lessons/2026-09-07-1.md             |   19 +
 sdlc/knowledge/lessons/2026-09-07-2.md             |   19 +
 sdlc/knowledge/lessons/2026-09-07-3.md             |   19 +
 sdlc/knowledge/lessons/2026-09-07-4.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-1.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-2.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-3.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-4.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-5.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-6.md             |   19 +
 sdlc/knowledge/lessons/2026-09-08-7.md             |   19 +
 sdlc/knowledge/lessons/2026-09-09-1.md             |   19 +
 sdlc/knowledge/lessons/2026-09-09-2.md             |   19 +
 sdlc/knowledge/lessons/2026-09-09-3.md             |   19 +
 sdlc/knowledge/lessons/index.md                    |   16 +
 sdlc/knowledge/log.md                              | 1401 ++++++++++++++++++++
 sdlc/knowledge/modules/accept.md                   |   70 +
 sdlc/knowledge/modules/append-log.md               |   36 +
 sdlc/knowledge/modules/artifacts-py.md             |   41 +
 sdlc/knowledge/modules/band-concepts.md            |   18 +
 sdlc/knowledge/modules/bash.md                     |   47 +
 sdlc/knowledge/modules/blocked.md                  |   65 +
 sdlc/knowledge/modules/bootstrap.md                |   70 +
 sdlc/knowledge/modules/build-py.md                 |   51 +
 sdlc/knowledge/modules/build.md                    |   52 +
 sdlc/knowledge/modules/bump-version-py.md          |   36 +
 sdlc/knowledge/modules/cfg.md                      |   39 +
 sdlc/knowledge/modules/check-86.md                 |   38 +
 sdlc/knowledge/modules/check.md                    |  101 ++
 sdlc/knowledge/modules/checkpoint-py.md            |   42 +
 sdlc/knowledge/modules/cli-py.md                   |   48 +
 sdlc/knowledge/modules/communities.md              |   18 +
 sdlc/knowledge/modules/components.md               |   70 +
 sdlc/knowledge/modules/config.md                   |   55 +
 sdlc/knowledge/modules/conftest-py.md              |  112 ++
 sdlc/knowledge/modules/deploy-py.md                |  104 ++
 sdlc/knowledge/modules/design-panel-js.md          |   38 +
 sdlc/knowledge/modules/diagnose-js.md              |   33 +
 sdlc/knowledge/modules/digests.md                  |   33 +
 sdlc/knowledge/modules/docs-py.md                  |  160 +++
 sdlc/knowledge/modules/fail.md                     |   55 +
 sdlc/knowledge/modules/feature-concepts.md         |   57 +
 sdlc/knowledge/modules/fill.md                     |  131 ++
 sdlc/knowledge/modules/findings.md                 |   36 +
 sdlc/knowledge/modules/fresh-graph.md              |   43 +
 sdlc/knowledge/modules/git.md                      |   39 +
 sdlc/knowledge/modules/hooks-py.md                 |   66 +
 sdlc/knowledge/modules/index.md                    |   53 +
 sdlc/knowledge/modules/init-py.md                  |   38 +
 sdlc/knowledge/modules/install-hook.md             |   48 +
 sdlc/knowledge/modules/install-uv.md               |   31 +
 sdlc/knowledge/modules/intent-scout-js.md          |   32 +
 sdlc/knowledge/modules/json.md                     |   33 +
 sdlc/knowledge/modules/knowledge-py.md             |   68 +
 sdlc/knowledge/modules/maintain-py.md              |   66 +
 sdlc/knowledge/modules/order-of-work-23.md         |   55 +
 sdlc/knowledge/modules/order-of-work-25.md         |   67 +
 sdlc/knowledge/modules/order-of-work-45.md         |   43 +
 sdlc/knowledge/modules/order-of-work-5.md          |  110 ++
 sdlc/knowledge/modules/order-of-work-8.md          |  127 ++
 sdlc/knowledge/modules/order-of-work.md            |  122 ++
 sdlc/knowledge/modules/packs-py.md                 |   56 +
 sdlc/knowledge/modules/parse-frontmatter.md        |   35 +
 sdlc/knowledge/modules/path-13.md                  |   52 +
 sdlc/knowledge/modules/path.md                     |   51 +
 sdlc/knowledge/modules/pathlib.md                  |   62 +
 sdlc/knowledge/modules/plan-critic-js.md           |   33 +
 sdlc/knowledge/modules/post-commit-path.md         |   17 +
 sdlc/knowledge/modules/post-edit.md                |   49 +
 sdlc/knowledge/modules/pre-bash.md                 |   42 +
 sdlc/knowledge/modules/project-py.md               |   60 +
 sdlc/knowledge/modules/propose.md                  |   48 +
 sdlc/knowledge/modules/publish.md                  |   61 +
 sdlc/knowledge/modules/ran.md                      |   18 +
 sdlc/knowledge/modules/read-json.md                |   46 +
 sdlc/knowledge/modules/read-state.md               |   17 +
 sdlc/knowledge/modules/reconcile.md                |   38 +
 sdlc/knowledge/modules/refresh.md                  |   66 +
 sdlc/knowledge/modules/rehearse.md                 |   56 +
 sdlc/knowledge/modules/rel-path.md                 |   63 +
 sdlc/knowledge/modules/release-readiness-js.md     |   34 +
 sdlc/knowledge/modules/render.md                   |   34 +
 sdlc/knowledge/modules/require.md                  |   50 +
 sdlc/knowledge/modules/requirements.md             |   68 +
 sdlc/knowledge/modules/review-js.md                |   37 +
 sdlc/knowledge/modules/review.md                   |   70 +
 sdlc/knowledge/modules/run-repomix.md              |   36 +
 sdlc/knowledge/modules/run.md                      |   67 +
 .../sdlc-ai-native-sdlc-plugin-for-claude-code.md  |   48 +
 sdlc/knowledge/modules/stages-py.md                |   53 +
 sdlc/knowledge/modules/staleness.md                |   17 +
 sdlc/knowledge/modules/status.md                   |   65 +
 sdlc/knowledge/modules/stepskipped.md              |   96 ++
 sdlc/knowledge/modules/test-artifacts-py.md        |   37 +
 sdlc/knowledge/modules/test-build-test-py.md       |   45 +
 sdlc/knowledge/modules/test-bump-py.md             |   38 +
 sdlc/knowledge/modules/test-deploy-py.md           |   47 +
 sdlc/knowledge/modules/test-docs-py.md             |   51 +
 sdlc/knowledge/modules/test-evals-py.md            |   33 +
 sdlc/knowledge/modules/test-hooks-py.md            |   86 ++
 sdlc/knowledge/modules/test-knowledge-py.md        |   64 +
 sdlc/knowledge/modules/test-maintain-py.md         |   58 +
 sdlc/knowledge/modules/test-plan-design-py.md      |   92 ++
 sdlc/knowledge/modules/test-workflows-py.md        |   48 +
 sdlc/knowledge/modules/testing-py.md               |   17 +
 sdlc/knowledge/modules/toml-config.md              |   79 ++
 sdlc/knowledge/modules/watch.md                    |   66 +
 sdlc/knowledge/modules/when-enabled.md             |   31 +
 sdlc/knowledge/modules/workflows-py.md             |   45 +
 147 files changed, 8686 insertions(+)
```

### Documents
- build: sdlc/graph-selected-repomix-context-packs/docs/build.html (9/9 showcase, 0 errors, 0 warnings)
- design: sdlc/graph-selected-repomix-context-packs/docs/design.html (9/9 showcase, 0 errors, 0 warnings)
- plan: sdlc/graph-selected-repomix-context-packs/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)
- test: sdlc/graph-selected-repomix-context-packs/docs/test.html (9/9 showcase, 0 errors, 0 warnings)
