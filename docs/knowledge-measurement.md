# Knowledge layer token measurement

Spec requirement 16 (`sdlc/graphify-and-okf-knowledge-base-integration/spec.md`): the five questions in `templates/evals/knowledge-questions.json`, each answered by `claude -p` (Claude Code 2.1.265, default model, `--max-turns 14`) in two modes on the same commit, then again after a rename and a deletion. Raw JSON results and the runner script are in `sdlc/graphify-and-okf-knowledge-base-integration/references/measurement/`.

- **raw**: `--allowedTools Read,Grep,Glob`; the prompt forbids `sdlc/knowledge/` and `graphify`.
- **knowledge**: `--allowedTools Read,Grep,Glob,Bash(graphify *)`; the prompt says read `sdlc/knowledge/index.md` first, use `graphify query` for call-graph facts, open source only when the bundle and graph cannot answer.
- Tokens = `input_tokens + cache_creation_input_tokens + cache_read_input_tokens` from the result's `usage` block, summed over every turn of the run; almost all of it is prompt-cache reads of the growing context.

## Same commit (this repo at 6398504: 159 files, 46 concepts, 697 graph nodes)

| # | Question | raw tokens | raw turns | knowledge tokens | knowledge turns | knowledge / raw |
|---|---|---|---|---|---|---|
| 1 | Which module owns the release gate that needs RELEASE_APPROVAL, and whic | 106,982 | 4 | 110,560 | 4 | 1.03 |
| 2 | What calls project.fail, and what does the CLI do with the Blocked it ra | 107,364 | 5 | 230,452 | 8 | 2.15 |
| 3 | Which files change when a feature is accepted at the plan stage, and wha | 144,589 | 6 | 156,718 | 6 | 1.08 |
| 4 | Which functions read sdlc/metrics.jsonl and which write it? | 220,346 | 9 | 197,616 | 6 | 0.90 |
| 5 | What breaks if artifacts.list_items changes its bullet handling? | 177,638 | 7 | 106,532 | 4 | 0.60 |
| | **total** | **756,919** | 31 | **801,878** | 28 | **1.06** |

## After a rename and a deletion

Worktree at the same commit: `scripts/sdlc/artifacts.py` renamed to `documents.py` with imports updated, `tests/test_evals.py` deleted, committed, graph rebuilt, bundle refreshed (`modules/artifacts-py.md` became a `status: deprecated` tombstone, `modules/documents-py.md` appeared).

| # | raw tokens | raw turns | knowledge tokens | knowledge turns | knowledge / raw | Q5 names documents.py |
|---|---|---|---|---|---|---|
| 1 | 107,413 | 3 | 112,513 | 4 | 1.05 | n/a |
| 2 | 189,934 | 7 | 159,110 | 7 | 0.84 | n/a |
| 3 | 109,196 | 4 | 201,204 | 8 | 1.84 | n/a |
| 4 | 221,342 | 8 | 232,522 | 7 | 1.05 | n/a |
| 5 | 107,395 | 6 | 112,322 | 5 | 1.05 | both |
| **total** | **735,280** | 28 | **817,671** | 31 | **1.11** | |

## What the numbers say

- On this repository the knowledge mode cost +6% tokens on the same commit and +11% after the rename. There is no token saving here. Articles 4 and 5 (`references/article-notes.md`) put the break-even near 500 files; this repo has 159, and every question was already answerable in 3 to 9 tool turns from raw reads. The intent's constraint anticipated this: the tooling tax on a small repo must stay a few seconds per commit, and `knowledge status` must be honest about what it measured.
- Answer quality was equal: both modes gave correct owners, callers and file paths on every question. After the rename both modes reported `documents.py` for question 5; the knowledge mode cited the rename commit from the graph.
- The layer's value in this run was freshness and provenance, not tokens: `knowledge status` reported both indexes at HEAD ten seconds after each commit, `knowledge check` was conformance-clean over 46 concepts, and every concept carries `generated`, `sources` with content digests and `source_commit`.
- Re-measure on a repository above roughly 500 files before quoting any saving; `references/measurement/measure.py <mode> <repo root> <out.json>` reproduces a run.
