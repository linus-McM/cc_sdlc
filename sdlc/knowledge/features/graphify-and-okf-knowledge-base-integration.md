---
type: Feature
title: Graphify and OKF knowledge base integration
description: Every sdlc session re-derives the shape of the codebase from raw file reads. Nothing persists
resource: sdlc/graphify-and-okf-knowledge-base-integration
tags: [feature, accepted]
status: draft
generated: { by: sdlc/0.2.1, at: "2026-09-09T02:01:32Z" }
verified:
  - { by: "process:sdlc-test", at: "2026-09-09T00:11:26Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T00:24:57Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T00:27:25Z" }
  - { by: "process:sdlc-test", at: "2026-09-09T00:28:52Z" }
stale_after: "2026-09-23T02:01:32Z"
source_commit: d8d61950c58abafa13a30ef68be4741e547839ef
sources:
  - { id: intent, resource: sdlc/graphify-and-okf-knowledge-base-integration/intent.md, last_modified: "2026-09-09T07:18:20+10:00", digest: 592df33452185091 }
  - { id: spec, resource: sdlc/graphify-and-okf-knowledge-base-integration/spec.md, last_modified: "2026-09-09T10:28:52+10:00", digest: 18ddccb80477e245 }
  - { id: plan, resource: sdlc/graphify-and-okf-knowledge-base-integration/plan.md, last_modified: "2026-09-09T10:28:52+10:00", digest: 31d2c88298eefdb1 }
  - { id: review, resource: sdlc/graphify-and-okf-knowledge-base-integration/review.md, last_modified: "2026-09-09T10:28:52+10:00", digest: b6e15f798eacd1f2 }
---

# Problem
Every sdlc session re-derives the shape of the codebase from raw file reads. Nothing persists
between stages or sessions except the markdown artifacts under `sdlc/<slug>/`, and those are
not indexed, cross-linked or queryable. Concretely, today:

1. Graphify (`graphifyy` 0.9.53, `~/.local/bin/graphify`) is installed on this machine but the
   plugin does not know it exists: no `graphify-out/graph.json` in the project, no Claude skill
   registered (`~/.claude/skills/graphify/` absent), no git hook (`graphify hook status` reports
   nothing). A graph built by hand would drift from the code on the next commit, and a stale
   structural graph gives high-confidence wrong answers with no signal that it is wrong
   (articles 4 and 7: silent hook failures, ghost nodes surviving `--update`, "already clean"
   false negatives).
2. There is no Open Knowledge Format (OKF) bundle. The knowledge the pipeline already produces
   (intent, spec, plan, review, `sdlc/lessons.md`, `sdlc/bands.toml`, `sdlc/metrics.jsonl`) is
   the curated narrative layer OKF exists to hold, but it has no `type` frontmatter, no
   `index.md` for progressive disclosure, no `log.md`, no provenance or freshness fields, so an
   agent cannot load it selectively and cannot tell current from stale or superseded.
3. Nothing bootstraps tooling when the plugin is first used in a project. A user running
   `/sdlc:plan new` in a fresh repo gets `.sdlc.toml` and nothing else; missing tools are
   discovered one at a time, by hand.
4. No mechanic re-indexes after a commit. The build stage commits every red-green step and the
   accept actions commit artifacts, yet none of those commits refresh any index, and nothing
   would tell anyone if a refresh had silently not happened.
5. Tooling gaps found while writing this intent: Graphify's Claude skill and git hooks not
   installed; plugin `hooks/hooks.json` has no `SessionStart` entry; the `graphify export
   --format okf` command article 4 describes does not exist in the installed 0.9.53 (no OKF
   exporter in `graphify/exporters/`; only `--wiki`), so OKF generation has to be ours; the
   superops `okf` Go CLI (`okf lint`, 13 rules) and `kiso` (OKF static publisher) are not
   installed; OpenWiki (Node, LLM-backed) is a possible alternative producer, not installed.

Affected: anyone running `/sdlc:*` in this or any other project (Linus today; whoever installs
the plugin later), and the reviewer and verifier agents that currently grep the tree cold.

# Outcome
1. Bootstrap on first use. A new mechanic (working name `knowledge bootstrap`, exposed through
   `cli.py` like every other mechanic) runs from a new `SessionStart` hook in `hooks/hooks.json`
   and from the top of every stage command. Idempotent, returns one JSON verdict listing what it
   found, installed or skipped, as separate steps. It checks and, when missing, does: `uv tool
   install graphifyy`; `graphify install --platform claude` (skill registered for Claude Code);
   `graphify hook install` (git post-commit, post-checkout, merge driver); first build `graphify
   update .` when `graphify-out/graph.json` is absent; first OKF bundle generation when the
   bundle is absent. When everything is present it costs one config read and a few `stat` calls,
   no git, no LLM.
2. Re-index after every commit. Graphify's own post-commit hook (installed above) rebuilds
   `graphify-out/` detached, no LLM, logging to `~/.cache/graphify-rebuild.log`. The plugin adds
   its own step on the same trigger so the OKF bundle is regenerated from the fresh `graph.json`
   plus the sdlc artifacts, and `log.md` gets a dated entry. Which trigger the plugin owns (a
   marker-delimited block in the git post-commit hook next to Graphify's, or a `PostToolUse`
   Bash matcher on `git commit`) is a design decision; the outcome is that no commit made by any
   stage leaves either index stale without a visible record.
3. Freshness is observable, not assumed (article 4). A `knowledge status` mechanic compares
   `graph.json`'s `built_at_commit` and the bundle's recorded source commit against `HEAD`, checks
   the three Graphify artifacts agree with each other, reads the rebuild log's last line, and
   reports a staleness verdict in commits and hours. The bundle records an update counter; after
   a configurable number of incremental updates (default 5, article 7's 3-5) or when staleness
   exceeds a configurable age, the next bootstrap forces a clean rebuild instead of an
   incremental one and says so.
4. An OKF v0.2 bundle lives in the target project's repository beside the code, never in the
   plugin checkout and never in `CLAUDE.md`. Root is the project root every `sdlc` call already
   uses (cwd for commands, the hook payload's `cwd` for hooks), so it is the same place whether
   the user or Claude runs the command. Paths: bundle at `<project>/sdlc/knowledge/` (proposed,
   `[knowledge] bundle` in `.sdlc.toml`; see Open questions), committed; Graphify output at
   `<project>/graphify-out/` (Graphify's fixed path), proposed ignored; git hooks in the
   project's `.git/hooks/`; skill and tool under `~/.claude/skills/graphify/` and
   `~/.local/share/uv/tools/graphifyy`; rebuild log `~/.cache/graphify-rebuild.log`. Optionally
   one marker-delimited pointer line in the project's `CLAUDE.md` (OpenWiki's pattern) so
   sessions that never run `/sdlc:*` still find `sdlc/knowledge/index.md`.
   Conformance per SPEC.md §11: every concept has parseable frontmatter with a
   non-empty `type`; `index.md` and `log.md` follow §8 and §9. Concepts:
   - one per sdlc feature (`type: Feature`) synthesised from intent, spec, plan, review;
   - one per Graphify community and god node (`type: Module`, `type: Hub`) from `graph.json`,
     linking to the feature concepts whose `Files that change` touch them;
   - `type: Lesson` per entry of `sdlc/lessons.md`; `type: Control Band` per band in
     `sdlc/bands.toml`.
   Frontmatter: `generated: { by: sdlc/<plugin version>, at }`, `status: draft`, `sources`
   naming the source paths and the source commit (`source_commit` documented as an
   organisational extension), `stale_after` set from the next expected regeneration.
   Bundle-relative links form the graph. Reverse-dependency invalidation (article 7): on
   regeneration, any concept whose `sources` paths changed since its `source_commit` is marked
   `status: draft` again, not silently kept. Concepts for deleted or renamed things become
   `status: deprecated` tombstones with a replacement link; eviction fails closed (a concept is
   only tombstoned when its source path is confirmed absent).
5. Trust boundary (articles 3 and 8). The agent only drafts: it never writes a `verified` event
   with a `human:` actor. A human `accept` (plan, design, build) is the publisher event: the
   accept mechanic derives `verified: { by: human:<git author>, at }` for the matching Feature
   concept and promotes it to `status: stable`. Deterministic checks may add `process:` events.
   Official conformance, organisational policy (title, generated, source_commit required) and
   trust/freshness are reported as three separate lists in one verdict, never conflated.
   Lesson concepts carry scope (repository, feature, source commit) and a `supersedes` link so a
   later lesson demotes an earlier one instead of both being served as current.
6. Every stage consumes the knowledge before it reads raw files: stage commands read
   `index.md` first and prefer `graphify query` / `graphify affected` over grep for "what calls
   what" questions, respecting EXTRACTED versus INFERRED edge tags; the build post-edit hook names
   the concepts a changed file affects; test review runs the OKF conformance check and fails on
   official-conformance violations; deploy's PR body links the knowledge diff; maintain ingests
   graph and bundle metrics (node count, community count, stale-concept count, unverified-concept
   count, staleness in commits) into `metrics.jsonl` so the bands can watch knowledge freshness
   like any other production signal and write the next intent when it drifts.
7. Success measure: after `/sdlc:plan new` in a fresh clone the bootstrap verdict is `ok`, both
   `graphify-out/graph.json` and the bundle exist, `graphify hook status` reports installed, and
   after any stage commit both indexes carry that commit's hash. `knowledge status` reports a
   stale graph within one commit of it going stale. The conformance check passes on the bundle
   this repo generates for its own five features. A fixed set of five codebase questions answered
   from the bundle plus `graphify query` uses fewer input tokens than the same questions answered
   by raw reads, measured on the same commit, then again after a rename and a deletion (articles
   3 and 7's honest-measurement protocol); the result is recorded, not assumed.

# Requirements
Traced to intent.md Proposed outcome items (PO1..PO7). "Verdict" means the one JSON dict `cli.main` returns.

1. (PO1) `sdlc knowledge bootstrap` returns a verdict with `steps: [{name, state, detail}]` where
   `state` is `present`, `installed`, `built`, `skipped` or `failed`, and `ok` is true only when
   no step is `failed`. Steps, in order: `uv` on PATH; `graphify` on PATH (installs with
   `uv tool install graphifyy` when absent and `uv` is present); Claude skill file present
   (`graphify install --platform claude`); git hooks installed (`graphify hook install`, checked
   via `graphify hook status`); `.graphifyignore` present with the plugin's exclusions; graph
   present (`graphify update .` when `graphify-out/graph.json` is absent); bundle present
   (generated when `<bundle>/index.md` is absent); `CLAUDE.md` pointer present (when configured).
2. (PO1) When every step is already satisfied, bootstrap performs no subprocess call other than
   `graphify hook status`, which is skipped when a cached `<bundle>/.state.json` says hooks were
   verified for the current `.git/hooks/post-commit` mtime. Proven by a test that monkeypatches
   `subprocess.run` to raise and asserts a healthy project still returns `ok`.
3. (PO1) `[knowledge] enabled = false` makes every `knowledge` action return
   `{"ok": true, "skipped": "knowledge disabled"}` and makes the `SessionStart` and post-commit
   paths exit silently. When `uv` is absent the bootstrap installs it with astral's own installer
   (`curl -LsSf https://astral.sh/uv/install.sh | sh` on POSIX, `irm https://astral.sh/uv/install.ps1
   | iex` through `powershell` on Windows; the choice is an operating-system gate in
   `knowledge.uv_install_command`); when that fails the step is `failed` with the installer's
   stderr, later steps are `skipped`, and no `pip` call is ever made. (Revised 2026-09-09 during
   build at the product owner's request; the original text stopped at "report and stop".)
4. (PO1) Every install step is reported before it runs: the verdict's step list includes the exact
   command executed in `detail`, and the `SessionStart` hook prints the verdict as
   `additionalContext` so the installs are visible in the session.
5. (PO2) `sdlc knowledge refresh` regenerates the bundle from `graphify-out/graph.json` plus the
   sdlc artifacts, appends one dated entry to `<bundle>/log.md`, records `HEAD` and an
   incremented `updates` counter in `<bundle>/.state.json`, and returns
   `{ok, concepts, created, updated, tombstoned, source_commit}`. Running it twice on the same
   commit changes no file except `.state.json`.
6. (PO2) `graphify hook install` is the only writer of Graphify's git hooks. The plugin appends
   its own marker-delimited block (`# sdlc-knowledge-start` .. `# sdlc-knowledge-end`) to the
   same `post-commit` file, after Graphify's, which runs `python3 <plugin>/scripts/sdlc.py knowledge refresh` detached (the `--quiet` flag was dropped during `/simplify`; the hook redirects output itself), honouring `GRAPHIFY_SKIP_HOOK=1`, skipping when the commit
   touched only `<bundle>/` or `graphify-out/`, and skipping in linked worktrees. The block is
   idempotent (re-install replaces it) and removable (`sdlc knowledge unhook`).
7. (PO2) The plugin's `PostToolUse` Bash handler `post-bash`, on a command whose tokens contain
   `git commit`, calls `knowledge.status` and, when the graph or bundle is behind `HEAD` by more
   than `[knowledge] max_behind` (reconciled during build: right after a commit both indexes are
   one behind while the detached hook runs, so "behind at all" would fire on every commit), emits
   `additionalContext` naming the stale index and the command to run. It never runs the refresh
   itself (the git hook does; this is the visibility path when the hook did not fire).
8. (PO3) `sdlc knowledge status` returns `{ok, graph: {commit, behind, artifacts_agree, last_rebuild}, bundle: {commit, behind, updates, concepts, stale, unverified, draft}, rebuild: "incremental" | "clean", reasons}` where `behind` is the number of commits from the
   recorded commit to `HEAD` (`git rev-list --count`), `artifacts_agree` is false when
   `graph.json`, `GRAPH_REPORT.md` and `graph.html` mtimes differ by more than
   `[knowledge] artifact_skew_seconds` (default 300), and `last_rebuild` is the last line of
   `~/.cache/graphify-rebuild.log` (or `GRAPHIFY_REBUILD_LOG`) when readable. `ok` is false with
   a reason when either index is behind by more than `[knowledge] max_behind` commits (default 1)
   or the bundle's `updates` counter reached `[knowledge] clean_every` (default 5): then
   `rebuild` is `clean` and the next `refresh` runs `graphify update . --force` and a full
   bundle rewrite, resetting the counter. (Reconciled during build: `bootstrap` stays free of
   git calls so a healthy session start spawns nothing; `refresh` owns the rebuild. The counter
   advances only when a refresh consumes a graph built at a new commit, so accept-triggered
   refreshes on the same graph do not count towards the cadence. `refresh` also rebuilds the
   graph incrementally whenever `built_at_commit` is not `HEAD`, so a bundle is never generated
   from a graph Graphify's own hook failed to rebuild.)
9. (PO4) The bundle root is `[knowledge] bundle` (default `sdlc/knowledge`) under the project
   root. `index.md` at the root carries `okf_version: "0.2"` frontmatter and one section per
   concept directory; every subdirectory has its own `index.md`; `log.md` uses `## YYYY-MM-DD`
   headings, newest first, entries `* **Creation**|**Update**|**Deprecation**: ...`.
10. (PO4) Concept documents are generated deterministically, one file per source:
    - `features/<slug>.md` `type: Feature`: title from intent, description from the first line of
      Problem, sections `# Problem`, `# Outcome`, `# Requirements` (spec), `# Files` (plan, each
      as a link to the `modules/` concept owning that file when one exists), `# Review` (review.md
      counts), `# Status` (artifact acceptance and deploy state).
    - `modules/<community-slug>.md` `type: Module`: one per Graphify community whose nodes span at
      least `[knowledge] min_community_nodes` (default 3) code nodes (`file_type: code`; the first
      live run showed markdown-heading communities from docs and the sdlc artifacts, which are
      not modules, and the bundle itself is in the default `.graphifyignore`); description names the files;
      sections `# Files`, `# Symbols` (labels with `source_file:source_location`), `# Depends on`
      (links to other modules reached by EXTRACTED edges; INFERRED edges listed separately under
      `# Inferred`), `# Features` (back-links).
    - `hubs/<label-slug>.md` `type: Hub`: top `[knowledge] god_nodes` (default 10) code nodes by
      degree, computed from the loaded `graph.json` (reconciled during `/simplify`: the same
      ranking `graphify god-nodes` prints, without a subprocess per refresh); links to its
      module. Hubs are derived concepts: one the graph stops ranking is tombstoned even though
      its source file still exists.
    - `lessons/<date>-<n>.md` `type: Lesson`: one per line of `sdlc/lessons.md`; `supersedes`
      set when a later lesson line contains the earlier one's first sentence verbatim.
    - `bands/<metric>.md` `type: Control Band`: one per `[metrics.*]` in `sdlc/bands.toml`,
      with the latest reading from `metrics.jsonl`.
      Every concept's frontmatter: `type`, `title`, `description`, `resource` (repo-relative path),
      `tags`, `generated: {by: "sdlc/<plugin version>", at}`, `status`, `sources: [{id, resource, last_modified}]`, `source_commit` (organisational extension), `stale_after` (generation time
      plus `[knowledge] stale_after_days`, default 14).
11. (PO4) Invalidation: on refresh, a concept whose `sources[].resource` content differs from the
    `digest` (sha256 prefix, an organisational extension recorded per source at generation) is
    regenerated and its `status` reset to `draft` even if it was `stable`, and `log.md` records
    the update. (Reconciled during build from "a commit newer than `source_commit`": an accept
    publishes from a working tree whose artifacts are not yet committed, so a commit-based rule
    reset every freshly published concept on its own accept commit. A body change caused by a
    non-source file, such as test-report.json, rewrites the concept but keeps its status.) A concept whose every source path is confirmed
    absent from the tree (`Path.exists()` false, checked at the repo root) is rewritten as a
    tombstone: `status: deprecated`, body `# Deprecated` with a link to the replacement when a
    concept with the same title exists elsewhere. A concept whose sources cannot be resolved
    (no `sources`, or a path outside the repo) is kept unchanged and listed in the verdict under
    `unresolved`; nothing is deleted.
12. (PO5) Generation never writes a `verified` entry whose `by` starts with `human:`. `sdlc <stage> accept` (plan, design, build) calls `knowledge.publish(feature, actor)` which appends
    `{by: "human:<git user.name slug>", at}` to `verified` on `features/<slug>.md` and sets
    `status: stable`; a refresh that regenerates the concept from unchanged sources preserves
    `verified`; regeneration after a source change keeps the history but resets `status: draft`
    (requirement 11), so `verified` alone never implies current. `sdlc test run` adds
    `{by: "process:sdlc-test", at}` when the report passes.
13. (PO5) `sdlc knowledge check` returns three lists in one verdict: `conformance` (SPEC.md §11:
    unparseable frontmatter, missing or empty `type`, reserved-file structure), `policy`
    (organisational: missing `title`, `generated`, `source_commit`; `verified` with a `human:`
    actor on a `draft` concept; a `stale_after` in the past on a `stable` concept), `trust`
    (per-concept tier: unverified, machine-confirmed, human-reviewed; counts). `ok` is false only
    on `conformance` findings. Broken links, unknown types and unknown keys are never findings.
14. (PO6) `commands/*.md` change: every stage command starts with `sdlc knowledge bootstrap` and
    reads `<bundle>/index.md` before any other file; build.md, test.md and maintain.md name
    `graphify query "<question>"` and `graphify affected "<symbol>"` as the first tool for
    call-graph questions and say INFERRED edges are hints. `hooks.post_edit` adds to its context
    the `modules/` concepts whose `# Files` list the edited path. `sdlc test run` runs
    `knowledge check` after the configured commands and fails on `conformance` findings.
    `deploy.pr_body` adds a `### Knowledge` section with `git diff --stat main...HEAD -- <bundle>`.
    `sdlc maintain ingest` gains no new syntax; `knowledge refresh` appends readings
    `knowledge_nodes`, `knowledge_communities`, `knowledge_stale`, `knowledge_unverified`,
    `knowledge_behind` to `metrics.jsonl`, and `templates/bands.toml` gains bands for
    `knowledge_stale` and `knowledge_behind` with `bad = "high"`.
15. (PO6) Agents: `agents/reviewer.md` and `agents/verifier.md` say to read `<bundle>/index.md`
    first and may run `graphify query`; their `tools` lists are unchanged (`Bash` already covers
    it).
16. (PO7) `evals/knowledge-questions.json` holds five fixed questions about this repo with
    deterministic checks; `docs/knowledge-measurement.md` records the token counts of answering
    them from raw reads versus bundle plus `graphify query`, on one commit, then after a rename
    and a deletion. Numbers are recorded as measured; no target is asserted by a test.
17. (Constraints) All new code is stdlib; `graphify` and `uv` are invoked through
    `project.run_cmd`-style subprocess helpers with `check=False`; no hook path runs
    `graphify label` or any LLM; every current test passes unchanged; `[knowledge] enabled = false` leaves every existing verdict byte-identical.

# Files
- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`
- `.gitattributes`
- `.gitignore`
- `.graphifyignore`
- `.sdlc.toml`
- `CLAUDE.md`
- `README.md`
- `agents/reviewer.md`
- `agents/verifier.md`
- `commands/build.md`
- `commands/deploy.md`
- `commands/design.md`
- `commands/maintain.md`
- `commands/plan.md`
- `commands/test.md`
- `docs/knowledge-measurement.md`
- `hooks/hooks.json`
- `scripts/hook.py` in [hooks.py](/modules/hooks-py.md)
- `scripts/sdlc/artifacts.py` in [artifacts.py](/modules/artifacts-py.md)
- `scripts/sdlc/cli.py` in [cli.py](/modules/cli-py.md)
- `scripts/sdlc/deploy.py` in [deploy.py](/modules/deploy-py.md)
- `scripts/sdlc/hooks.py` in [hooks.py](/modules/hooks-py.md)
- `scripts/sdlc/knowledge.py` in [staleness](/modules/staleness.md)
- `scripts/sdlc/project.py` in [Path](/modules/path.md)
- `scripts/sdlc/stages.py` in [stages.py](/modules/stages-py.md)
- `scripts/sdlc/testing.py` in [testing.py](/modules/testing-py.md)
- `sdlc/bands.toml`
- `sdlc/graphify-and-okf-knowledge-base-integration/references/measurement/`
- `sdlc/knowledge/`
- `templates/bands.toml`
- `templates/evals/knowledge-questions.json`
- `templates/knowledge/claude-pointer.md`
- `templates/knowledge/index.md`
- `templates/knowledge/log.md`
- `templates/knowledge/post-commit.sh`
- `tests/conftest.py` in [conftest.py](/modules/conftest-py.md)
- `tests/fixtures/graph.json`
- `tests/test_artifacts.py` in [test_artifacts.py](/modules/test-artifacts-py.md)
- `tests/test_build_test.py` in [run](/modules/run.md)
- `tests/test_deploy.py` in [run](/modules/run.md)
- `tests/test_hooks.py` in [toml_config](/modules/toml-config.md)
- `tests/test_knowledge.py` in [run](/modules/run.md)
- `tests/test_plan_design.py` in [run](/modules/run.md)

# Review
- Important: 7, Nit: 5

# Status
- intent.md: accepted
- spec.md: accepted
- plan.md: accepted
- test-report: passed
- deployed: dev
