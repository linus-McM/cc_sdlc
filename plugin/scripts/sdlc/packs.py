"""Graph-selected Repomix context packs: one commit-pinned snapshot per stage that its Workflow agents share.

Seeds come from the stage artifact, grow one hop through graphify-out/graph.json, pass a frozen secret
exclude list, Bandit and Repomix's own secret check, and land in graphify-out/packs/ (never committed).
`require` is the plan and test gate: a pack built at HEAD, and at test one covering every changed file.
"""

from __future__ import annotations

from collections import defaultdict


def expand(graph: dict, seeds: list[str], hops: int) -> dict[str, str]:
    """{path: seed|caller|callee|community}: files `hops` `calls` links from a seed, plus each seed's community."""
    files: dict[str, str] = dict.fromkeys(seeds, "seed")
    node_file = {n["id"]: n.get("source_file") for n in graph["nodes"] if n.get("source_file")}
    by_file = defaultdict(set)
    for node_id, path in node_file.items():
        by_file[path].add(node_id)
    calls = [(link["source"], link["target"]) for link in graph["links"] if link.get("relation") == "calls"]
    frontier = {n for s in seeds for n in by_file[s]}
    for _ in range(hops):
        reached = {target: "callee" for source, target in calls if source in frontier} | {source: "caller" for source, target in calls if target in frontier}
        frontier = set()
        for node_id, reason in reached.items():
            if (path := node_file.get(node_id)) and path not in files:
                files[path] = reason
                frontier.add(node_id)
    communities = {n.get("community") for n in graph["nodes"] if n.get("source_file") in seeds} - {None}
    for node in graph["nodes"]:
        if node.get("community") in communities and (path := node.get("source_file")):
            files.setdefault(path, "community")
    return files
