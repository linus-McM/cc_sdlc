# Article 1: Standardizing Agent Memory (Estari, Jul 3 2026)
- OKF v0.1 published June 12-13 2026 by Sam McVeety / Amir Hormati (Google Cloud). Formalises Karpathy's "LLM Wiki" pattern.
- Bundle = directory of Markdown files with YAML frontmatter. Only required field: `type`. Recommended: title, description, resource, tags, timestamp.
- File path is identity. Bundle-relative links (/services/x.md) form the graph.
- Reserved files: index.md (progressive disclosure entry point), log.md (knowledge change history, distinct from git log).
- Conformance: consumers must NOT reject on missing optional fields, unknown types, unknown keys, broken links.
- For code: type: Service/Module/API; sections # Responsibilities, # Dependencies, # Citations; resource = repo path.
- Gap: OKF has no opinion on generation. Need enrichment pipeline: commit -> diff-scoped scan -> draft/update concepts (two-pass: schema/interfaces then citations) -> re-link -> lint -> publish.
- Diff-scoping keeps per-commit cost cheap.
- Tooling: superops-team/okf Go CLI (`okf init`, `okf hook install`, `okf search`, `okf lint` 13 rules); oak-invest/kiso static-site publisher (llms.txt).
- Consumption: orchestrator reads index.md first, routes sub-agents to concept files. OKF = compiled cache for stable knowledge; RAG for long tail.
- Limits: no search layer, no type registry, untyped links, doesn't fix stale docs, ecosystem very early.
- Refs: https://github.com/superops-team/okf , https://github.com/oak-invest/kiso , https://okf.md/faq/
# Article 2: Graphify, OKF, or Both? (Estari, Jul 22 2026)
- Graphify BENCHMARKS.md: LongMemEval-S ties vector RAG (76% acc, recall 0.844 vs 0.848). LOCOMO 45.3% at $1.40 ingest vs Supermemory 49.7% at $15.67. Edge = ingest cost (AST, zero LLM) + zero-hallucination structural extraction, not retrieval accuracy.
- Three layers: Vector RAG (unstructured: docs, tickets, Slack) / Graphify (structure: AST call graphs, imports, inherits, mixes_in; EXTRACTED vs INFERRED edges; Leiden communities; god nodes) / OKF (narrative: architecture, schemas, playbooks).
- `/graphify .` outputs: graph.html, GRAPH_REPORT.md, graph.json (in graphify-out/).
- Timeline: Karpathy 2026-04-01; Graphify 2026-04-03 (Safi Shamsi, YC S26); OKF 2026-06-12; Graphify<->OKF hybrid toolkit 2026-07-01 (71.5x token claim, corpus-topology dependent).
- Triggers: multi-hop reasoning failure -> add Graphify; tribal-knowledge sprawl -> add OKF.
- Graphify risks: build-time snapshot staleness (needs pre-commit / CI hook; stale graph worse than none), community noise in monoliths, LLM hallucination in semantic pass for non-code, unreplicated benchmarks.
- OKF risks: no enforcement/validation, silent bundle degradation (tolerant consumers), maintenance overhead unless workflow mandates updates with code changes.
- Combined pipeline: Stage 1 OKF index.md progressive disclosure (~2K tokens) -> Stage 2 graphify structural query (zero LLM) -> Stage 3 vector RAG for long tail.
- Install: `uv tool install graphifyy`; `graphify install`; `/graphify .`; `graphify path "A" "B"`; `graphify query "..."`.
- OKF bundle location suggestion: `.well-known/okf/` or `docs/knowledge/`.
- ERPNext case: baseline 70.8% key-fact coverage vs hybrid 82.0%.
- Decision: add layer only for observed failure mode.
# Article 3: From Self-Updating OKF Wiki to Production Trust System (Estari, Aug 2 2026)
- Core rule: model may DRAFT knowledge; separately controlled system decides what becomes trusted/current/publishable.
- Agent must never write its own `verified: human:...` event. Producer proposes `status: draft` + `generated: {by: <agent>/<version>, at}`.
- OKF v0.2 trust tiers from `verified`: none -> unverified; only process:/tool actors -> machine-confirmed; any human:<id> -> human-reviewed. Advisory, not access control.
- Three separate report categories: official OKF conformance / organisational policy (e.g. superops okf lint requires title) / trust+freshness. Don't conflate.
- Four roles: Producer (agent drafts), Verifier (deterministic checks: symbols exist, contract valid; human for qualitative), Publisher (derives `verified` from authenticated PR review metadata, ties bundle to `source_commit` org-extension), Consumer (trust policy before loading body; unverified consumable but maybe not actionable).
- GitHub enforcement: CODEOWNERS on knowledge dirs + policy code; PR required; stale approval dismissal; required status checks; separate bot/human identities.
- CI validates: OKF conformance; org-required fields; actor syntax; no producer-authored human verified in draft; cited internal sources exist at reviewed revision; changed sources mark dependents stale or regenerate; deprecated concepts keep tombstone + replacement link; stale_after not passed for promoted content.
- Truth maintenance: record source lineage (source_commit, source_paths); invalidate reverse dependencies; keep tombstones (status: deprecated + replacement link); distinguish rename vs replacement; fail closed on uncertainty (mark stale/draft); preserve rollback evidence (code + knowledge state together).
- Attested Computation useful for reproducible ops only (SQL, builds). Not for judgement calls.
- Measure token savings honestly: fixed task set, same revision, then advance repo through deletions/renames and re-run.
- Small repo checklist: bundle in same repo as source; PR + one owner approval for stable; agents create drafts only; full regeneration regularly instead of elaborate incremental invalidation; reject expired stale_after at publication; tombstones; small fixed task set before claims.
- superops okf CLI: `okf hook -type post-commit`.
# Article 4: Production-Grade OKF + Graphify Setup, Not Just a Demo (Estari, Aug 13 2026)
- 71.5x token claim = single favourable case (123k -> 1.7k tokens). Replications: 6.8x (code review) to 49x (daily coding, 500+ files); from-scratch Python repo 7.3x. Plan around 7x-49x.
- Hard floor: graph build/maintenance overhead only pays off above ~500 files. Below: tooling tax.
- Claimed integration command: `graphify export --format okf --out docs/knowledge/` (toolkit shipped 2026-07-01). Verify against installed version.
- Core risk: static index, does NOT self-heal. Stale graph with zero signal = worst case. Documented case: GRAPH_SUMMARY.md two weeks stale on origin/main while handed to agents as truth.
- Silent hook failure mechanisms (graphify issues #1161 etc.):
  1. Windows: hooks use nohup, Git for Windows lacks it -> rebuild never runs, no error.
  2. Hook's hardcoded CODE_EXTS allowlist drifted from graphify/detect.py -> commits touching valid code skip rebuild.
  3. Resource gating (cpu <= 50%, mem >= 2GB) silently skips; "next commit retries" -> unbounded staleness on quiet branches.
  4. MCP server caches graph.json at startup, no hot reload -> fresh on disk, stale in agent memory.
  5. Three artifacts (graph.json, graph.html, GRAPH_REPORT.md) can desync if update refuses overwrite; no cross-check.
- Scale wall: betweenness_centrality O(V*E); 450k-node monorepo rebuild killed at 114 min on 96-core; ~10 min on M3 Pro on other repo. Incremental 0.8s to 10s+, not an SLA.
- Operational trap: graphify-out/ tracked in git -> every regeneration dirties tree, blocks CI/publish. Gitignore it or exclude from triggering commit.
- Production-grade requirements:
  * Treat freshness as observable property: log rebuild success/failure with timestamp somewhere visible, don't trust exit code.
  * CI one-liner: compare graph.json / GRAPH_REPORT.md / graph.html generation timestamps to each other and to `git log -1`.
  * Restart or hot-reload MCP server after regeneration; verify.
  * Resource-gated skip only with explicit retry/alert path: scheduled catch-up job or alert when staleness > threshold.
  * Decide deliberately if repo is above ~500-file threshold; measure first.
  * Graphify = "what calls what"; OKF = narrative + portability; vector index = semantic recall. Complementary layers.
- Definition: production-grade setup = defined by failure-detection story ("will you know within 24h the graph is stale?"), not benchmark story.
# Article 5: Knowledge-Graph Skills for Claude Code and Codex: Graphify and Rivals Compared (Estari, Jul 16 2026)
- Every tool publishes own single-favourable multiple (Graphify 71.5x, codebase-memory-mcp 120x/"99%", code-review-graph 85%, CodeGraph 92% fewer tool calls). Not comparable. Optimise for deployment model matching team constraints, not multiple.
- Shared pipeline: tree-sitter parse (EXTRACTED, deterministic) -> optional LLM pass (INFERRED, probabilistic, tagged) -> queryable graph (JSON/SQLite/graph DB).
- Packaging split: static skill artifact (Graphify: SKILL.md + graph.json + GRAPH_REPORT.md, rebuild manually or via hook) vs live MCP server (CodeGraph, codebase-memory-mcp, code-review-graph; some auto-sync on save).
- Three decision variables: (1) codebase size: <500 files agentic grep usually enough; (2) team size/update frequency: solo/periodic -> static Graphify, commit graph.json so teammates share; fast-moving daily commits -> live MCP; (3) data residency: local-first tools fine, run EXTRACTED-only if no external LLM allowed.
- Anthropic Claude Code team dropped vector RAG for agentic grep; AAAI 2026 "keyword search is all you need".
- ~80% enterprise retrieval queries are simple lookups, 15% multi-hop (graph), 5% agentic planning.
- Rivals: CodeGraph (Rust MCP, codegraph_context/explore, best blast radius); codebase-memory-mcp (static binary, 158 langs, arXiv, 31-repo avg 10x); code-review-graph (`pip install code-review-graph`, SQLite, ~10s for 500 files, incremental on save, PR blast radius); Sourcegraph Cody (enterprise >100 engineers).
- Failure modes: staleness silent killer; INFERRED edges hallucinate, agent must respect tag; ecosystem pre-1.0 API instability; agentic grep may already be enough.
- 15-minute test: score repo size/team/query pattern/residency; baseline one real query with grep (tokens, tool calls); then same with Graphify; adopt only if savings meaningful.
# Article 6: Your Vector DB is Shredding Context. Google OKF is the Fix. (Estari, Jul 2 2026)
- Vector RAG = fuzzy cosine similarity; wrong tool for canonical knowledge (runbooks, policies, API specs, metric definitions). Chunking breaks structure -> "shredded context" -> hallucination on exact-match queries.
- OKF = deterministic retrieval of exact versioned markdown from git; no embeddings, no index sync. Memory lives in git, auditable, portable.
- Minimal CI validation: parse frontmatter, fail if `type` missing (python-frontmatter example). Run on every commit.
- Hybrid stack: router agent sends canonical questions to OKF, open-ended thematic questions to vector DB. Not replacement.
- Use cases: policy audit of PRs, infra migration from canonical specs, incident triage from runbooks.
- Extra references: OKFy GitHub repo, Hermes OKF Python package (unverified names).
# Article 7: The Graph That Lied for Three Weeks: Real Knowledge Lifecycle for Graphify + OKF (Estari, Jul 23 2026)
- Thesis: build problem solved; lifecycle (cache coherence) problem unowned. Incremental `graphify update` = untrusted cache with short TTL.
- Documented Graphify defects: #1007 manifest.json absolute vs graph.json relative paths -> eviction never matches, "already clean" false negative, ghost nodes forever; #1178 destructive fuzzy node-merge during --update corrupts valid graph; #1116 symbol deleted inside surviving file never evicted; #857 update/extract share manifest.json hash -> semantic pass silently skipped; #311 cache keyed on absolute paths, non-portable across machines/CI.
- Maintainers recommend full clean rebuild every 3-5 incremental sessions.
- Realistic cost: initial full build 200k-280k tokens for ~140-file repo (LLM semantic pass); saves 80k-150k tokens/hour orientation tax on ~200-file repo. Not 70x.
- Lifecycle design:
  1. Content hashing + explicit dependency metadata in frontmatter: `content_hash` (sha256 body), `refs: [path#Lx-Ly]`, `status: draft|verified|stale`, `review_by` date (org extensions; v0.2 has status/stale_after/sources natively).
  2. Reverse-dependency invalidation: `git diff --name-only <range>` intersect concept refs -> STALE CONCEPT list; CI fails when verified concept points at changed source or review_by passed.
  3. Fail-closed tombstoning: evict node only when Path(identity).exists() is explicitly False; missing manifest entry -> keep + loud warning; canonical relative paths in manifest.
- CI: cadence counter `.graphify/update_count`; after 3-5 incrementals or weekly cron run clean full rebuild; freshness gate script on every PR.
- Sizing: <100 files: no custom invalidation, just weekly scheduled clean rebuild. 500+ files: full cache-coherence engineering.
# Article 8: Your Agent Memory Is a Dependency, Not a Superpower (Estari, Aug 24 2026)
- Retrieved memory is versioned, scoped, potentially hostile input; must pass lifecycle before influencing consequential action. Interface: retrieved_memory + provenance + scope + conflicts -> candidate evidence, never -> instruction.
- MemTrapBench: faithful relevant memories can still anchor reasoning wrongly. Retrieval precision is incomplete metric; measure downstream utility vs no-memory baseline.
- Separate memory kinds with different authority: transcript / fact / preference / state / episode / procedure. Preference is not policy; episode is not procedure; old observation is not current state.
- Memory contract fields that matter: source ref + trust, observed_or_inferred, scope (tenant/repo/env/task_family), versions (tool_schema, repository_commit), valid_from/valid_until, supersedes, status (candidate|active|quarantined|archived), removal_policy (e.g. repository_commit_changed), evidence_of_success.
- Lifecycle gates: capture (raw evidence beside summary) -> decompose (subskills with interfaces, not whole trajectories) -> qualify -> retrieve (authorization + validity filters BEFORE semantic ranking) -> challenge (preconditions match? superseded? contradicted? how irreversible?) -> measure (causal path telemetry) -> expire (by condition, not only TTL; demote, don't delete audit history).
- Challenge gate: ignore if scope mismatch / superseded / expired / untrusted; verify_live for facts, procedures, consequential requests; use directly only low-impact matching preference.
- Subtask skills transfer better than whole-task replays (cross-task transfer preprint: whole-task -1.2 to -4.1 pts, subtask +0.5 to +1.9).
- Memory poisoning: payloads already in memory attack later sessions; measure write, retrieval, action controls separately.
- Fixtures: strategy switch; policy correction supersedes old record; planted instruction in untrusted doc must not be admitted or resurface; commit/schema upgrade moves affected skills out of active retrieval; repeated unused retrieval demotes.
- Relevance to sdlc: sdlc/lessons.md + maintain lessons are procedural memory; OKF concepts derived from them need scope (repo, commit), status, supersession, and a challenge step before agents act on them.
# Article 9: OpenWiki in 2026: Self-Maintaining Memory Layer (Estari, Aug 17 2026)
- OpenWiki v0.3.3 (Node CLI, `npm install -g openwiki`; `openwiki --init`): Code Brain writes linked markdown wiki under `openwiki/` and adds pointer to AGENTS.md / CLAUDE.md; Personal Brain ingests Gmail/Notion/Slack/git/web via connectors into ~/.openwiki/wiki/.
- Uses LLM provider (OpenRouter etc.) for synthesis; update mode `openwiki code --update --print` diffs since last documented commit (needs full git history, fetch-depth 0).
- CI template: scheduled daily workflow opens docs PR (peter-evans/create-pull-request); PR review is the quality gate.
- Can emit OKF bundles. Positioned as narrative layer alternative/producer; Graphify for graph-native relationship queries; OKF for portability/interchange.
- Files: openwiki/INSTRUCTIONS.md (brief), .openwikiignore (read boundary).
- Evaluation: two-week before/after on 10-20 representative tasks, stable model/harness; measure rather than promise.
- Relevance to sdlc: alternative producer for the narrative layer; requires Node + paid LLM in CI, so out of scope for stdlib plugin, but the pointer-in-CLAUDE.md pattern and PR-as-quality-gate pattern carry over.
