---
type: Module
title: Path
description: "Graphify community 9: plugin/scripts/sdlc/packs.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.5.0, at: "2026-09-26T06:33:18Z" }
stale_after: "2026-10-10T06:33:18Z"
source_commit: 5c45a37edd0dc635576e390a1174bea9fad6d10b
sources:
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:31:53+10:00", digest: 976267a001f822d8 }
---

# Files
- `plugin/scripts/sdlc/packs.py`

# Symbols
- secret_rule() (plugin/scripts/sdlc/packs.py:L102)
- The EXCLUDE pattern `path` matches, ignoring case (`SERVER.PEM` is still a key). (plugin/scripts/sdlc/packs.py:L103)
- git_ignored() (plugin/scripts/sdlc/packs.py:L111)
- Files git would ignore, tracked or not (`--no-index`). (plugin/scripts/sdlc/packs.py:L112)
- admit() (plugin/scripts/sdlc/packs.py:L118)
- Split the selection into files Repomix may read and exclusions with the rule… (plugin/scripts/sdlc/packs.py:L119)
- select() (plugin/scripts/sdlc/packs.py:L256)
- ({admitted path: reason}, seeds, unresolved tokens, exclusions); refuses when… (plugin/scripts/sdlc/packs.py:L257)
- tracked() (plugin/scripts/sdlc/packs.py:L34)
- Tracked paths, NUL-separated so git never quotes unusual names. (plugin/scripts/sdlc/packs.py:L35)
- resolve() (plugin/scripts/sdlc/packs.py:L39)
- Tracked `files` a token names (a file, a directory or a glob); tokens naming… (plugin/scripts/sdlc/packs.py:L40)
- review_changes() (plugin/scripts/sdlc/packs.py:L439)
- Files the test pack seeds from and must cover: the branch diff against… (plugin/scripts/sdlc/packs.py:L440)
- covered() (plugin/scripts/sdlc/packs.py:L447)
- section_tokens() (plugin/scripts/sdlc/packs.py:L52)
- plan_seeds() (plugin/scripts/sdlc/packs.py:L64)
- seeds() (plugin/scripts/sdlc/packs.py:L83)
- Seed files for a stage; sdlc-owned paths (artifacts, the bundle) never seed:… (plugin/scripts/sdlc/packs.py:L84)

# Depends on
- [config](/modules/config.md)
- [fail](/modules/fail.md)
- [fresh_graph](/modules/fresh-graph.md)
- [git](/modules/git.md)
- [require](/modules/require.md)
- [review](/modules/review.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
