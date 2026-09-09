## Graphify and OKF knowledge base integration

### Why
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

### Artifacts
- sdlc/graphify-and-okf-knowledge-base-integration/intent.md, spec.md, plan.md (accepted)
- test-report: passed, tdd cycles: 19
- review: Important: 7, Nit: 5

### Proof
- `uv run pytest`: existing 76 plus roughly 20 new tests pass; no test needs `graphify` or
  `uv` on PATH (the `fake_tools` fixture proves it by running with `PATH` set to the temp
  `bin/` only, plus the system `git`).
- `uv run ruff check scripts tests && uv run ruff format --check scripts tests`: clean.
- `claude plugin validate --strict .`: "Validation passed".
- Live on this repo (step 13): `python3 scripts/sdlc.py knowledge bootstrap` ok with steps
  `installed`/`built`; `graphify hook status` shows `post-commit: installed`; `grep -c
  sdlc-knowledge-start .git/hooks/post-commit` is 1; after a commit `python3 scripts/sdlc.py
  knowledge status` shows `graph.behind: 0`, `bundle.behind: 0`; `python3 scripts/sdlc.py
  knowledge check` has an empty `conformance` list; `docs/knowledge-measurement.md` holds the
  measured token counts.

### Knowledge
no knowledge changes under sdlc/knowledge against main
