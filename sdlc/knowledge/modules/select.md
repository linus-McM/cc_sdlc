---
type: Module
title: select
description: "Graphify community 9: plugin/scripts/sdlc/build.py, plugin/scripts/sdlc/packs.py"
resource: plugin/scripts/sdlc
tags: [module, graphify]
status: draft
generated: { by: sdlc/0.8.1, at: "2026-09-28T22:57:53Z" }
stale_after: "2026-10-12T22:57:53Z"
source_commit: 0754d821fc594b90c529849cddaca10dc6109921
sources:
  - { id: build, resource: plugin/scripts/sdlc/build.py, last_modified: "2026-09-09T15:02:31+10:00", digest: 3bd6dd8d38860ab6 }
  - { id: packs, resource: plugin/scripts/sdlc/packs.py, last_modified: "2026-09-26T16:35:55+10:00", digest: 976267a001f822d8 }
---

# Files
- `plugin/scripts/sdlc/build.py`
- `plugin/scripts/sdlc/packs.py`

# Symbols
- is_sdlc_owned() (plugin/scripts/sdlc/build.py:L62)
- expand() (plugin/scripts/sdlc/packs.py:L139)
- {path: seed|caller|callee|community}: files `hops` `calls` links from a seed,… (plugin/scripts/sdlc/packs.py:L140)
- exempt() (plugin/scripts/sdlc/packs.py:L212)
- select() (plugin/scripts/sdlc/packs.py:L256)
- ({admitted path: reason}, seeds, unresolved tokens, exclusions); refuses when… (plugin/scripts/sdlc/packs.py:L257)
- tracked() (plugin/scripts/sdlc/packs.py:L34)
- Tracked paths, NUL-separated so git never quotes unusual names. (plugin/scripts/sdlc/packs.py:L35)
- resolve() (plugin/scripts/sdlc/packs.py:L39)
- Tracked `files` a token names (a file, a directory or a glob); tokens naming… (plugin/scripts/sdlc/packs.py:L40)
- seeds() (plugin/scripts/sdlc/packs.py:L83)
- Seed files for a stage; sdlc-owned paths (artifacts, the bundle) never seed:… (plugin/scripts/sdlc/packs.py:L84)

# Depends on
- [fail](/modules/fail.md)
- [git](/modules/git.md)
- [packs.py](/modules/packs-py.md)

# Inferred
- no INFERRED edges; treat any that appear as hints

# Features
- [graph-selected repomix context packs](/features/graph-selected-repomix-context-packs.md)
