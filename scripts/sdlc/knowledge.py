"""Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle (sdlc/knowledge/).

Public mechanics: bootstrap, status, refresh, check, publish, unhook. Every one is a no-op verdict
when the layer is off (`[knowledge] enabled = false` or SDLC_KNOWLEDGE=off). Graphify and uv are
subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
from datetime import UTC, datetime, timedelta
from pathlib import Path

from . import artifacts as a
from . import project as p
from .project import fail

TEMPLATES = p.TEMPLATES / "knowledge"
POINTER_START = "<!-- sdlc-knowledge-start -->"

SKIPPED = {"ok": True, "skipped": "knowledge disabled"}
FENCE = "---"
BAD = re.compile(r"[:#\[\]{}\",']|^\s|\s$|^[-?&*!|>%@`]")


class Unparseable(ValueError):
    """The YAML subset reader met a line it does not understand."""


# --- YAML subset: scalars, flat lists, {k: v} maps and lists of maps; everything OKF emits ---


def scalar(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    text = str(value)
    plain = text and not BAD.search(text) and not NUMBERISH.match(text) and text not in ("true", "false", "null")
    return text if plain else json.dumps(text)


NUMBERISH = re.compile(r"^[-+]?(\d[\d_]*\.?\d*([eE][-+]?\d+)?|\.\d+)$")


def flow(value) -> str:
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{key}: {scalar(v)}" for key, v in value.items()) + " }"
    if isinstance(value, list):
        return "[" + ", ".join(flow(v) for v in value) + "]"
    return scalar(value)


def dump_frontmatter(data: dict) -> str:
    lines = [FENCE]
    for key, value in data.items():
        if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
            lines.append(f"{key}:")
            lines += [f"  - {flow(v)}" for v in value]
        else:
            lines.append(f"{key}: {flow(value)}")
    return "\n".join([*lines, FENCE]) + "\n"


def read_scalar(text: str):
    text = text.strip()
    if text.startswith('"'):
        try:
            return json.loads(text)
        except json.JSONDecodeError as err:
            raise Unparseable(text) from err
    if text.startswith("'") and text.endswith("'") and len(text) >= 2:
        return text[1:-1]
    if text in ("true", "false"):
        return text == "true"
    if re.fullmatch(r"[-+]?\d+", text):
        return int(text)
    return text


def split_flow(text: str) -> list[str]:
    """Top-level comma split that respects quotes and nested brackets."""
    parts, depth, quote, start = [], 0, None, 0
    for i, ch in enumerate(text):
        if quote:
            quote = None if ch == quote else quote
        elif ch in "\"'":
            quote = ch
        elif ch in "[{":
            depth += 1
        elif ch in "]}":
            depth -= 1
        elif ch == "," and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return [part for part in (part.strip() for part in parts) if part]


def read_flow(text: str):
    text = text.strip()
    if text.startswith("{") and text.endswith("}"):
        out = {}
        for item in split_flow(text[1:-1]):
            key, sep, value = item.partition(":")
            if not sep:
                raise Unparseable(item)
            out[key.strip()] = read_flow(value)
        return out
    if text.startswith("[") and text.endswith("]"):
        return [read_flow(item) for item in split_flow(text[1:-1])]
    if text.startswith(("[", "{")):
        raise Unparseable(text)
    return read_scalar(text)


def parse_frontmatter(block: str) -> dict:
    """The subset reader; on any line it cannot read, `_raw` holds the block and `type` survives if present."""
    out: dict = {}
    try:
        key = None
        for line in block.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.startswith("  - ") and key:
                out.setdefault(key, []).append(read_flow(line[4:]))
                continue
            name, sep, value = line.partition(":")
            if not sep or name != name.strip() or not name:
                raise Unparseable(line)
            key = name
            if value.strip():
                out[key] = read_flow(value)
            else:
                out[key] = []
    except Unparseable:
        found = re.search(r"^type:\s*(.+)$", block, re.MULTILINE)
        return {"_raw": block, **({"type": read_scalar(found.group(1))} if found else {})}
    return out


def split_document(text: str) -> tuple[dict, str]:
    if not text.startswith(FENCE + "\n"):
        return {}, text
    end = text.find("\n" + FENCE + "\n", len(FENCE))
    if end < 0:
        return {}, text
    body = text[end + len(FENCE) + 2 :]
    return parse_frontmatter(text[len(FENCE) + 1 : end + 1]), body.removeprefix("\n")  # one blank separator line is not body


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_KNOWLEDGE") != "off" and bool(p.config(root)["knowledge"]["enabled"])


# --- paths and small helpers ---


def cfg(root: Path) -> dict:
    return p.config(root)["knowledge"]


def bundle_dir(root: Path) -> Path:
    return root / cfg(root)["bundle"]


def graph_path(root: Path) -> Path:
    return root / "graphify-out" / "graph.json"


def skill_path() -> Path:
    base = Path(os.environ["CLAUDE_CONFIG_DIR"]) if os.environ.get("CLAUDE_CONFIG_DIR") else Path.home() / ".claude"
    return base / "skills" / "graphify" / "SKILL.md"


def state_path(root: Path) -> Path:
    return bundle_dir(root) / ".state.json"


def read_state(root: Path) -> dict:
    return p.read_json(state_path(root), {}) or {}


def write_state(root: Path, **fields) -> dict:
    state = {**read_state(root), **fields}
    state_path(root).parent.mkdir(parents=True, exist_ok=True)
    p.write_json(state_path(root), state)
    return state


def hooks_dir(root: Path) -> Path:
    """Git's hooks directory without spawning git: .git or the worktree's common dir, honouring core.hooksPath."""
    git_dir = root / ".git"
    if git_dir.is_file():  # linked worktree or submodule: `gitdir: <path>`
        git_dir = (root / git_dir.read_text().split(":", 1)[1].strip()).resolve()
    common = git_dir / "commondir"
    if common.exists():
        git_dir = (git_dir / common.read_text().strip()).resolve()
    config = git_dir / "config"
    if config.exists() and (m := re.search(r"^\s*hooksPath\s*=\s*(.+)$", config.read_text(), re.MULTILINE)):
        return root / Path(m.group(1).strip()).expanduser()
    return git_dir / "hooks"


def post_commit_path(root: Path) -> Path:
    return hooks_dir(root) / "post-commit"


def tool(root: Path, *argv: str) -> subprocess.CompletedProcess:
    return p.run_cmd(root, list(argv))


def bundle_skeleton(root: Path) -> None:
    """index.md and log.md from the templates; `refresh` rewrites them from real sources."""
    home = bundle_dir(root)
    home.mkdir(parents=True, exist_ok=True)
    (home / "index.md").write_text(a.render(TEMPLATES / "index.md", title=f"{root.name} knowledge", sections="* nothing indexed yet; run `sdlc knowledge refresh`"))
    (home / "log.md").write_text(a.render(TEMPLATES / "log.md", date=p.today()))


# --- git post-commit block, appended after Graphify's own ---

BLOCK_START, BLOCK_END = "# sdlc-knowledge-start", "# sdlc-knowledge-end"
BLOCK_RE = re.compile(rf"\n?{BLOCK_START}.*?{BLOCK_END}\n", re.DOTALL)


def hook_block(root: Path) -> str:
    text = (TEMPLATES / "post-commit.sh").read_text()
    return text.replace("__PLUGIN_ROOT__", str(p.PLUGIN_ROOT)).replace("__BUNDLE__", cfg(root)["bundle"])


def our_block_present(root: Path) -> bool:
    hook = post_commit_path(root)
    return hook.exists() and hook_block(root) in hook.read_text()


def install_hook(root: Path) -> dict:
    """Idempotent: replaces an existing sdlc block, otherwise appends after everything else."""
    hook = post_commit_path(root)
    hook.parent.mkdir(parents=True, exist_ok=True)
    text = BLOCK_RE.sub("\n", hook.read_text()) if hook.exists() else "#!/bin/sh\n"
    text = text.rstrip("\n") + "\n" + hook_block(root)
    hook.write_text(text)
    hook.chmod(hook.stat().st_mode | 0o755)
    return {"ok": True, "path": str(hook)}


def unhook(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    hook = post_commit_path(root)
    removed = False
    if hook.exists() and BLOCK_START in (text := hook.read_text()):
        hook.write_text(BLOCK_RE.sub("\n", text).rstrip("\n") + "\n" if text.strip() else text)
        removed = True
    return {"ok": True, "removed": removed, "path": str(hook), "next": "Graphify's own hooks stay; `graphify hook uninstall` removes them"}


# --- uv: the one installer this plugin assumes; installed with astral's own script per operating system ---

UV_INSTALL = {
    "posix": ["sh", "-c", "curl -LsSf https://astral.sh/uv/install.sh | sh"],
    "windows": ["powershell", "-ExecutionPolicy", "ByPass", "-c", "irm https://astral.sh/uv/install.ps1 | iex"],
}


def uv_install_command(system: str | None = None) -> list[str]:
    system = system or platform.system()
    return UV_INSTALL["windows" if system.lower().startswith("win") else "posix"]


def find_uv() -> str | None:
    """uv on PATH, else where astral's installer puts it; that directory joins PATH for the rest of this process."""
    if found := shutil.which("uv"):
        return found
    for candidate in (Path.home() / ".local" / "bin", Path.home() / ".cargo" / "bin"):
        exe = candidate / ("uv.exe" if os.name == "nt" else "uv")
        if exe.exists():
            os.environ["PATH"] = f"{candidate}{os.pathsep}{os.environ.get('PATH', '')}"
            return str(exe)
    return None


# --- bootstrap: check and, unless `check`, install what is missing, in a fixed order ---


class StepFailed(Exception):
    pass


def bootstrap(root: Path, check: bool = False) -> dict:
    if not enabled(root):
        return SKIPPED
    conf = cfg(root)
    steps: list[dict] = []
    failed = False

    def step(name: str, probe, act, detail: str = ""):
        """probe() -> bool present; act() -> (state, detail) performs the install or build."""
        nonlocal failed
        if failed:
            steps.append({"name": name, "state": "skipped", "detail": "earlier step failed"})
            return
        try:
            if probe():
                steps.append({"name": name, "state": "present", "detail": detail})
            elif act is None:
                steps.append({"name": name, "state": "skipped", "detail": detail})
            elif check:
                steps.append({"name": name, "state": "missing", "detail": detail})
            else:
                state, done = act()
                steps.append({"name": name, "state": state, "detail": done})
        except StepFailed as err:
            failed = True
            steps.append({"name": name, "state": "failed", "detail": str(err)})

    def install_graphify():
        result = tool(root, "uv", "tool", "install", "graphifyy")
        if result.returncode != 0 or not shutil.which("graphify"):
            raise StepFailed(f"uv tool install graphifyy exited {result.returncode}: {result.stderr.strip()[-200:]}")
        return "installed", "uv tool install graphifyy"

    def install_skill():
        result = tool(root, "graphify", "install", "--platform", "claude")
        if result.returncode != 0 or not skill_path().exists():
            raise StepFailed(f"graphify install --platform claude exited {result.returncode}: {result.stderr.strip()[-200:]}")
        return "installed", "graphify install --platform claude"

    def graphify_hooks_present() -> bool:
        return "not installed" not in tool(root, "graphify", "hook", "status").stdout

    def hooks_present() -> bool:
        hook = post_commit_path(root)
        if not hook.exists() or not shutil.which("graphify") or not our_block_present(root):
            return False
        if read_state(root).get("hooks_mtime") == hook.stat().st_mtime:
            return True
        if not graphify_hooks_present():
            return False
        write_state(root, hooks_mtime=hook.stat().st_mtime)
        return True

    def install_hooks():
        done = []
        if not post_commit_path(root).exists() or not graphify_hooks_present():
            result = tool(root, "graphify", "hook", "install")
            if result.returncode != 0:
                raise StepFailed(f"graphify hook install exited {result.returncode}: {result.stderr.strip()[-200:]}")
            done.append("graphify hook install")
        install_hook(root)
        done.append("sdlc block appended to post-commit")
        return "installed", "; ".join(done)

    def write_ignore():
        (root / ".graphifyignore").write_text("".join(f"{line}\n" for line in conf["ignore"]))
        return "built", ".graphifyignore from [knowledge] ignore"

    built_graph = False

    def build_graph():
        nonlocal built_graph
        result = tool(root, "graphify", "update", ".")
        if result.returncode != 0 or not graph_path(root).exists():
            raise StepFailed(f"graphify update . exited {result.returncode}: {result.stderr.strip()[-200:]}")
        built_graph = True
        return "built", "graphify update ."

    def bundle_present() -> bool:
        # a bundle written before the graph existed (an accept can publish first) is rebuilt with the graph
        return (bundle_dir(root) / "index.md").exists() and not built_graph

    def build_bundle():
        bundle_skeleton(root)
        refresh(root, quiet=True)
        return "built", str(bundle_dir(root).relative_to(root))

    def claude_pointer():
        path = root / "CLAUDE.md"
        block = a.render(TEMPLATES / "claude-pointer.md", bundle=conf["bundle"])
        text = path.read_text() if path.exists() else ""
        path.write_text(text + ("\n" if text and not text.endswith("\n") else "") + block)
        return "built", "CLAUDE.md pointer block"

    def pointer_present() -> bool:
        path = root / "CLAUDE.md"
        return path.exists() and POINTER_START in path.read_text()

    def install_uv():
        argv = uv_install_command()
        result = tool(root, *argv)
        if result.returncode != 0 or not find_uv():
            raise StepFailed(f"{argv[-1]} exited {result.returncode}: {result.stderr.strip()[-200:] or 'uv still not found'}")
        return "installed", " ".join(argv)

    step("uv", lambda: find_uv() is not None, install_uv, "uv")
    step("graphify", lambda: shutil.which("graphify") is not None, install_graphify, "graphify on PATH")
    step("skill", lambda: skill_path().exists(), install_skill, str(skill_path()))
    step("hooks", hooks_present, install_hooks, "git post-commit hook")
    step("graphifyignore", lambda: (root / ".graphifyignore").exists(), write_ignore, ".graphifyignore")
    step("graph", lambda: graph_path(root).exists(), build_graph, "graphify-out/graph.json")
    step("bundle", bundle_present, build_bundle, f"{conf['bundle']}/index.md")
    step("claude_md", pointer_present, claude_pointer if conf["claude_md_pointer"] else None, "CLAUDE.md pointer")

    missing = [s["name"] for s in steps if s["state"] == "missing"]
    verdict = {"ok": not failed and not missing, "mode": "check" if check else "install", "steps": steps}
    if failed:
        bad = next(s for s in steps if s["state"] == "failed")
        verdict["reason"] = f"bootstrap step {bad['name']} failed: {bad['detail']}"
    elif missing:
        verdict["reason"] = "missing: " + ", ".join(missing) + " (run `sdlc knowledge bootstrap` to install)"
    return verdict


# --- status: is either index behind HEAD, do the graph artifacts agree, is a clean rebuild due ---

BUILT_AT = re.compile(r'"built_at_commit"\s*:\s*"([0-9a-f]{7,40})"')


def graph_commit(root: Path) -> str | None:
    path = graph_path(root)
    if not path.exists():
        return None
    match = BUILT_AT.search(path.read_text())
    return match.group(1) if match else None


def rebuild_log_tail() -> str | None:
    path = Path(os.environ.get("GRAPHIFY_REBUILD_LOG") or Path.home() / ".cache" / "graphify-rebuild.log")
    try:
        lines = path.read_text().splitlines()
    except OSError:
        return None
    return lines[-1] if lines else None


def artifacts_agree(root: Path) -> bool:
    out = graph_path(root).parent
    stamps = [(out / name).stat().st_mtime for name in ("graph.json", "GRAPH_REPORT.md", "graph.html") if (out / name).exists()]
    return len(stamps) < 2 or max(stamps) - min(stamps) <= cfg(root)["artifact_skew_seconds"]


def bundle_counts(root: Path, now: str) -> dict:
    counts = {"concepts": 0, "stale": 0, "unverified": 0, "draft": 0}
    for path in concept_files(root):
        front, _ = split_document(path.read_text())
        counts["concepts"] += 1
        counts["stale"] += str(front.get("stale_after", "9")) < now
        counts["unverified"] += not front.get("verified")
        counts["draft"] += front.get("status") == "draft"
    return counts


def status(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    conf = cfg(root)
    now = now_iso()
    state = read_state(root)
    graph = {"commit": graph_commit(root), "behind": behind(root, graph_commit(root)), "artifacts_agree": artifacts_agree(root), "last_rebuild": rebuild_log_tail()}
    bundle = {"commit": state.get("commit"), "behind": behind(root, state.get("commit")), "updates": state.get("updates", 0), **bundle_counts(root, now)}
    reasons, notes = [], []
    if graph["commit"] is None:
        reasons.append("graphify-out/graph.json missing or without built_at_commit; run `sdlc knowledge bootstrap`")
    elif graph["behind"] > conf["max_behind"]:
        reasons.append(f"graph is {graph['behind']} commits behind HEAD (max_behind {conf['max_behind']}); graphify-out/graph.json needs `graphify update .`")
    if bundle["commit"] is None:
        reasons.append(f"{conf['bundle']} has no .state.json; run `sdlc knowledge refresh`")
    elif bundle["behind"] > conf["max_behind"]:
        reasons.append(f"bundle is {bundle['behind']} commits behind HEAD (max_behind {conf['max_behind']}); run `sdlc knowledge refresh`")
    if bundle["updates"] >= conf["clean_every"]:
        reasons.append(f"{bundle['updates']} refreshes since the last clean rebuild (clean_every {conf['clean_every']}); the next refresh rebuilds the graph with --force")
    if not graph["artifacts_agree"]:
        notes.append(f"graph artifacts skew: graph.json, GRAPH_REPORT.md and graph.html mtimes differ by more than {conf['artifact_skew_seconds']}s")
    verdict = {"ok": not reasons, "graph": graph, "bundle": bundle, "rebuild": "clean" if reasons else "incremental", "reasons": reasons, "notes": notes}
    if reasons:
        verdict["reason"] = "; ".join(reasons)
    return verdict


# --- refresh: graph.json + sdlc artifacts -> OKF bundle ---

VOLATILE = ("status", "generated", "verified", "stale_after")  # frontmatter that never counts as a content change
DIRS = ("features", "modules", "hubs", "lessons", "bands")
LESSON_LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2}): (.+)$", re.MULTILINE)


def now_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def plugin_version() -> str:
    manifest = p.PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
    return json.loads(manifest.read_text()).get("version", "0") if manifest.exists() else "0"


def head_commit(root: Path) -> str:
    return p.git(root, "rev-parse", "HEAD")


def load_graph(root: Path) -> dict:
    path = graph_path(root)
    return json.loads(path.read_text()) if path.exists() else {"nodes": [], "links": []}


DOC_SUFFIXES = (".md", ".markdown", ".rst", ".txt", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".mp4")


def is_code(node: dict) -> bool:
    """Graphify tags code, document and rationale nodes; only code communities become Module concepts."""
    if "file_type" in node:
        return node["file_type"] == "code"
    return node.get("_origin") == "ast" and not str(node.get("source_file", "")).lower().endswith(DOC_SUFFIXES)


def community_labels(root: Path, graph: dict) -> dict[int, str]:
    path = graph_path(root).parent / ".graphify_labels.json"
    labels = {int(k): v for k, v in (p.read_json(path, {}) or {}).items()} if path.exists() else {}
    for node in graph["nodes"]:
        cid = node.get("community")
        if cid is not None and cid not in labels and node.get("community_name"):
            labels[cid] = node["community_name"]
    return labels


def communities(root: Path, graph: dict) -> list[dict]:
    """Graphify communities big enough for a Module concept, with a stable slug each."""
    groups: dict[int, list[dict]] = {}
    for node in graph["nodes"]:
        if node.get("community") is not None and node.get("source_file"):
            groups.setdefault(node["community"], []).append(node)
    labels = community_labels(root, graph)
    out, taken = [], set()
    for cid in sorted(groups):
        nodes = groups[cid]
        if sum(is_code(n) for n in nodes) < cfg(root)["min_community_nodes"]:
            continue
        name = labels.get(cid) or f"Community {cid}"
        slug = a.slugify(name) or f"community-{cid}"
        slug = slug if slug not in taken else f"{slug}-{cid}"
        taken.add(slug)
        files = sorted({n["source_file"] for n in nodes})
        out.append({"cid": cid, "name": name, "slug": slug, "files": files, "nodes": nodes})
    return out


def god_nodes(root: Path) -> list[dict]:
    result = tool(root, "graphify", "god-nodes", "--top", str(cfg(root)["god_nodes"]), "--json")
    try:
        return json.loads(result.stdout) if result.returncode == 0 else []
    except json.JSONDecodeError:
        return []


def concept(path: str, type_: str, title: str, description: str, resource: str, tags: list[str], sources: list[str], body: str, **extra) -> dict:
    return {
        "path": path,
        "front": {"type": type_, "title": title, "description": description[:200], "resource": resource, "tags": tags, **extra},
        "sources": sources,
        "body": body.rstrip("\n") + "\n",
    }


def link(c: dict) -> str:
    return f"[{c['front']['title']}](/{c['path']})"


def section(heading: str, lines: list[str], empty: str = "none") -> str:
    return f"# {heading}\n" + ("\n".join(lines) if lines else f"- {empty}") + "\n\n"


def first_line(text: str) -> str:
    return next((line.strip() for line in text.splitlines() if line.strip() and not PLACEHOLDER.match(line)), "")


PLACEHOLDER = re.compile(r"^\s*<[^>]*>\s*$")


def feature_files(feature: Path) -> list[str]:
    plan = feature / "plan.md"
    return a.list_items(a.sections(plan.read_text()).get("Files that change", "")) if plan.exists() else []


def features(root: Path) -> list[Path]:
    home = p.home(root)
    return sorted(d for d in home.iterdir() if (d / "intent.md").exists()) if home.exists() else []


def module_concepts(root: Path, graph: dict, comms: list[dict], feature_dirs: list[Path]) -> tuple[list[dict], dict[str, dict]]:
    by_node = {n["id"]: c for c in comms for n in c["nodes"]}
    for c in comms:
        extracted, inferred = set(), set()
        for edge in graph["links"]:
            src, dst = by_node.get(edge["source"]), by_node.get(edge["target"])
            if src is not c or dst is None or dst is c:
                continue
            (extracted if edge.get("confidence", "EXTRACTED") == "EXTRACTED" else inferred).add(dst["slug"])
        others = {m["slug"]: m for m in comms}
        c["concept"] = concept(
            f"modules/{c['slug']}.md",
            "Module",
            c["name"],
            f"Graphify community {c['cid']}: " + ", ".join(c["files"]),
            os.path.commonpath(c["files"]) if len(c["files"]) > 1 else str(Path(c["files"][0]).parent),
            ["module", "graphify"],
            c["files"],
            "",
        )
        c["_edges"] = (sorted(extracted), sorted(inferred), others)
    for c in comms:
        extracted, inferred, others = c.pop("_edges")
        symbols = sorted(c["nodes"], key=lambda n: (n["source_file"], n.get("source_location", "")))
        backlinks = [d for d in feature_dirs if set(feature_files(d)) & set(c["files"])]
        c["concept"]["body"] = (
            section("Files", [f"- `{f}`" for f in c["files"]])
            + section("Symbols", [f"- {n['label']} ({n['source_file']}:{n.get('source_location', '')})" for n in symbols])
            + section("Depends on", [f"- {link(others[s]['concept'])}" for s in extracted], "no EXTRACTED edges to other modules")
            + section("Inferred", [f"- {link(others[s]['concept'])}" for s in inferred], "no INFERRED edges; treat any that appear as hints")
            + section("Features", [f"- [{a.title((d / 'intent.md').read_text())}](/features/{d.name}.md)" for d in backlinks], "no feature plan names these files")
        )
    return [c["concept"] for c in comms], {f: c["concept"] for c in comms for f in c["files"]}


def review_counts(feature: Path) -> str:
    path = feature / "review.md"
    if not path.exists():
        return "no review yet"
    text = path.read_text()
    important = len(re.findall(r"^\s*[-*]\s*Important:", text, re.MULTILINE))
    nits = len(re.findall(r"^\s*[-*]\s*Nit:", text, re.MULTILINE))
    return f"Important: {important}, Nit: {nits}"


def feature_status(feature: Path) -> list[str]:
    lines = []
    for name in ("intent.md", "spec.md", "plan.md"):
        path = feature / name
        lines.append(f"- {name}: " + ((a.status(path.read_text()) or "draft") if path.exists() else "missing"))
    report = p.read_json(feature / "test-report.json", {}) or {}
    lines.append(f"- test-report: {'passed' if report.get('passed') else 'missing or failed'}")
    deployed = p.read_json(feature / "deploy.json", {}) or {}
    lines.append("- deployed: " + (", ".join(sorted(k for k in deployed if k != "rollback")) or "nowhere"))
    return lines


def feature_concepts(root: Path, feature_dirs: list[Path], module_of: dict[str, dict]) -> list[dict]:
    out = []
    for d in feature_dirs:
        intent = (d / "intent.md").read_text()
        spec = (d / "spec.md").read_text() if (d / "spec.md").exists() else ""
        sections = a.sections(intent)
        files = feature_files(d)
        file_lines = [f"- `{f}`" + (f" in {link(module_of[f])}" if f in module_of else "") for f in files]
        rel = str(d.relative_to(root))
        out.append(
            concept(
                f"features/{d.name}.md",
                "Feature",
                a.title(intent),
                first_line(sections.get("Problem", "")) or a.title(intent),
                rel,
                ["feature", a.status(intent) or "draft"],
                [f"{rel}/{n}" for n in ("intent.md", "spec.md", "plan.md", "review.md") if (d / n).exists()],
                section("Problem", [sections.get("Problem", "").strip()])
                + section("Outcome", [sections.get("Proposed outcome", "").strip()])
                + section("Requirements", [a.sections(spec).get("Requirements", "").strip()] if spec else [], "spec.md not written yet")
                + section("Files", file_lines, "plan.md not written yet")
                + section("Review", [f"- {review_counts(d)}"])
                + section("Status", feature_status(d)),
            )
        )
    return out


def hub_concepts(root: Path, graph: dict, comms: list[dict]) -> list[dict]:
    nodes = {n["id"]: n for n in graph["nodes"]}
    by_node = {n["id"]: c for c in comms for n in c["nodes"]}
    out, taken = [], set()
    for hub in god_nodes(root):
        node = nodes.get(hub.get("id"), {})
        slug = a.slugify(hub.get("label", hub.get("id", ""))) or "hub"
        slug = slug if slug not in taken else f"{slug}-{len(taken)}"
        taken.add(slug)
        module = by_node.get(hub.get("id"))
        src = node.get("source_file", "")
        out.append(
            concept(
                f"hubs/{slug}.md",
                "Hub",
                hub.get("label", slug),
                f"Graphify god node with degree {hub.get('degree', '?')}" + (f" in {src}" if src else ""),
                src or "graphify-out/graph.json",
                ["hub", "graphify"],
                [src] if src else [],
                section("Where", [f"- `{src}:{node.get('source_location', '')}`" if src else "- not in the current graph"])
                + section("Module", [f"- {link(module['concept'])}"] if module else [], "no module concept covers this node")
                + section("Why it matters", [f"- degree {hub.get('degree', '?')}: many modules reach this symbol; changes here have a wide blast radius"]),
            )
        )
    return out


def first_sentence(text: str) -> str:
    return re.split(r"[;.]\s|\s—\s", text, maxsplit=1)[0]


def lesson_concepts(root: Path) -> list[dict]:
    path = p.home(root) / "lessons.md"
    if not path.exists():
        return []
    rows, per_day = [], {}
    for date, text in LESSON_LINE.findall(path.read_text()):
        per_day[date] = per_day.get(date, 0) + 1
        rows.append((date, per_day[date], text.strip()))
    out = []
    for i, (date, n, text) in enumerate(rows):
        first = first_sentence(text)
        older = [j for j in range(i) if len(first_sentence(rows[j][2])) >= 20 and first_sentence(rows[j][2]) in text]
        extra = {"supersedes": f"/lessons/{rows[older[-1]][0]}-{rows[older[-1]][1]}.md"} if older else {}
        out.append(
            concept(
                f"lessons/{date}-{n}.md",
                "Lesson",
                first[:80],
                text,
                str(path.relative_to(root)),
                ["lesson", date],
                [str(path.relative_to(root))],
                section("Lesson", [f"- {date}: {text}"]) + section("Scope", [f"- repository `{root.name}`; recorded by the maintain stage"]),
                **extra,
            )
        )
    return out


def band_concepts(root: Path) -> list[dict]:
    from . import maintain

    out = []
    readings = maintain.readings(root, None)
    bands_path = p.home(root) / "bands.toml"
    for metric, band in maintain.bands(root).items():
        band = {**maintain.DEFAULT_BAND, **band}
        values = readings.get(metric, [])
        out.append(
            concept(
                f"bands/{a.slugify(metric)}.md",
                "Control Band",
                metric,
                f"Western Electric band on {metric}; bad side {band['bad']}, window {band['window']}",
                str(bands_path.relative_to(root)),
                ["band", "maintain"],
                [str(bands_path.relative_to(root))],
                section("Band", [f"- window: {band['window']}", f"- tiers: {', '.join(band['tiers'])}", f"- bad side: {band['bad']}"])
                + section("Latest reading", [f"- {values[-1]} over {len(values)} readings"] if values else [], "no readings yet"),
            )
        )
    return out


def signature(front: dict, body: str, keys) -> str:
    """Content identity: the builder's own keys plus the body; provenance and trust fields never count."""
    return json.dumps({k: front.get(k) for k in keys if k not in VOLATILE}, sort_keys=True) + body.lstrip("\n")


def git_last_modified(root: Path, rel: str, cache: dict) -> str:
    if rel not in cache:
        stamp = p.git(root, "log", "-1", "--format=%cI", "--", rel)
        cache[rel] = stamp or now_iso()
    return cache[rel]


def render_concept(root: Path, c: dict, existing: dict | None, commit: str, stamp: str, cache: dict, reset: bool = True) -> str:
    """Frontmatter plus body; `reset` (a source changed) drops the concept back to draft, a body-only change keeps its status."""
    conf = cfg(root)
    front = {
        **{k: c["front"][k] for k in ("type", "title", "description", "resource", "tags")},
        "status": "draft" if reset or not existing else existing.get("status", "draft"),
        "generated": {"by": f"sdlc/{plugin_version()}", "at": stamp},
    }
    if existing and existing.get("verified"):
        front["verified"] = existing["verified"]
    stale = datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC) + timedelta(days=conf["stale_after_days"])
    front["stale_after"] = stale.strftime("%Y-%m-%dT%H:%M:%SZ")
    front["source_commit"] = commit
    front["sources"] = [{"id": Path(src).stem, "resource": src, "last_modified": git_last_modified(root, src, cache), "digest": digest(root, src) or "missing"} for src in c["sources"]]
    front.update({k: v for k, v in c["front"].items() if k not in front})
    return dump_frontmatter(front) + "\n" + c["body"]


def write_index(home: Path, rel_dir: str, entries: list[dict], title: str) -> bool:
    lines = [f"* [{e['front']['title']}]({Path(e['path']).name}) - {e['front']['description']}" for e in sorted(entries, key=lambda e: e["front"]["title"].lower())]
    text = f"# {title}\n\n" + ("\n".join(lines) if lines else "* none yet") + "\n"
    path = home / rel_dir / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text() == text:
        return False
    path.write_text(text)
    return True


def write_root_index(root: Path, grouped: dict[str, list[dict]]) -> None:
    home = bundle_dir(root)
    parts = []
    for d in DIRS:
        entries = sorted(grouped.get(d, []), key=lambda e: e["front"]["title"].lower())
        lines = [f"* [{e['front']['title']}]({e['path']}) - {e['front']['description']}" for e in entries]
        parts.append(f"# {d.capitalize()}\n" + ("\n".join(lines) if lines else "* none yet") + "\n")
    text = a.render(TEMPLATES / "index.md", title=f"{root.name} knowledge", sections="").replace("# Sections\n\n", "\n".join(parts))
    if not (home / "index.md").exists() or (home / "index.md").read_text() != text:
        (home / "index.md").write_text(text)


def append_log(root: Path, entries: list[str]) -> None:
    if not entries:
        return
    path = bundle_dir(root) / "log.md"
    today = p.today()
    text = path.read_text() if path.exists() else "# Knowledge Update Log\n"
    block = "\n".join(f"* {e}" for e in entries)
    heading = f"## {today}\n"
    if heading in text:
        text = text.replace(heading, heading + block + "\n", 1)
    else:
        title, _, rest = text.partition("\n")
        text = f"{title}\n\n{heading}{block}\n" + (("\n" + rest.lstrip("\n")) if rest.strip() else "")
    path.write_text(text)


def digest(root: Path, rel: str) -> str | None:
    path = root / rel
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16] if path.is_file() else None


def sources_changed(root: Path, front: dict, sources: list[str]) -> bool:
    """True when any source's content differs from the digest recorded at generation (unknown counts as changed)."""
    recorded = {s.get("resource"): s.get("digest") for s in front.get("sources", []) if isinstance(s, dict)}
    return not sources or any(recorded.get(rel) is None or recorded[rel] != digest(root, rel) for rel in sources)


def reconcile(root: Path, concepts: list[dict], commit: str, stamp: str, log: list[str]) -> tuple[int, list[str]]:
    """Concept files nothing generated any more: tombstone when every source is confirmed gone, else keep and report."""
    home = bundle_dir(root)
    generated = {c["path"] for c in concepts}
    titles = {c["front"]["title"]: c for c in concepts}
    tombstoned, unresolved = 0, []
    for path in sorted(home.glob("*/*.md")):
        rel = str(path.relative_to(home))
        if path.name == "index.md" or rel not in {f"{d}/{path.name}" for d in DIRS} or rel in generated:
            continue
        front, _ = split_document(path.read_text())
        sources = [s.get("resource") for s in front.get("sources", []) if isinstance(s, dict) and isinstance(s.get("resource"), str)]
        inside = [s for s in sources if not Path(s).is_absolute() and ".." not in Path(s).parts]
        if not inside or len(inside) != len(sources):
            unresolved.append(rel)
            continue
        if any((root / s).exists() for s in inside):
            unresolved.append(rel)
            continue
        if front.get("status") == "deprecated":
            continue
        replacement = titles.get(front.get("title"))
        tomb = {k: v for k, v in front.items() if k not in ("status", "generated", "stale_after", "source_commit")}
        tomb = {**{k: tomb.pop(k) for k in ("type", "title", "description", "resource", "tags") if k in tomb}, "status": "deprecated", "generated": {"by": f"sdlc/{plugin_version()}", "at": stamp}, "source_commit": commit, **tomb}
        body = section(
            "Deprecated", [f"- sources removed by commit `{commit[:12]}`: " + ", ".join(f"`{s}`" for s in inside), f"- replacement: {link(replacement)}" if replacement else "- no replacement concept; kept so incoming links still resolve"]
        )
        path.write_text(dump_frontmatter(tomb) + "\n" + body)
        log.append(f"**Deprecation**: [{front.get('title', path.stem)}](/{rel}).")
        tombstoned += 1
    return tombstoned, unresolved


def behind(root: Path, since: str | None) -> int:
    if not since:
        return 0
    result = p.run_git(root, "rev-list", "--count", f"{since}..HEAD")
    return int(result.stdout.strip() or 0) if result.returncode == 0 else 0


def refresh(root: Path, quiet: bool = False) -> dict:
    if not enabled(root):
        return SKIPPED
    from . import maintain

    home = bundle_dir(root)
    home.mkdir(parents=True, exist_ok=True)
    previous = read_state(root)
    commit = head_commit(root)
    clean = previous.get("commit") is not None and status(root)["rebuild"] == "clean"
    if shutil.which("graphify") and (clean or graph_commit(root) != commit):
        # Graphify's own post-commit hook normally did this already; when it did not, the bundle must not be built from a stale graph
        argv = ["graphify", "update", ".", *(["--force"] if clean else [])]
        result = tool(root, *argv)
        if result.returncode != 0:
            fail(f"{' '.join(argv)} exited {result.returncode}: {result.stderr.strip()[-200:]}")
    graph = load_graph(root)
    comms = communities(root, graph)
    feature_dirs = features(root)
    modules, module_of = module_concepts(root, graph, comms, feature_dirs)
    concepts = [*feature_concepts(root, feature_dirs, module_of), *modules, *hub_concepts(root, graph, comms), *lesson_concepts(root), *band_concepts(root)]
    stamp, cache = now_iso(), {}
    created, updated, log, unverified, stale = 0, 0, [], 0, 0
    for c in concepts:
        path = home / c["path"]
        existing = split_document(path.read_text()) if path.exists() else None
        same = existing and signature(existing[0], existing[1], c["front"]) == signature(c["front"], c["body"], c["front"])
        changed = not existing or sources_changed(root, existing[0], c["sources"])
        if same and not changed and not clean:
            text = path.read_text()
        else:
            text = render_concept(root, c, existing[0] if existing else None, commit, stamp, cache, reset=changed)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
            if not existing or changed or not same:
                log.append(f"**{'Update' if existing else 'Creation'}**: {link(c)}.")
                created, updated = created + (not existing), updated + bool(existing)
        front, _ = split_document(text)
        unverified += not front.get("verified")
        stale += str(front.get("stale_after", "9")) < stamp
    tombstoned, unresolved = reconcile(root, concepts, commit, stamp, log)
    grouped: dict[str, list[dict]] = {d: [] for d in DIRS}
    for c in concepts:
        grouped[c["path"].split("/", 1)[0]].append(c)
    for d in DIRS:
        write_index(home, d, grouped[d], d.capitalize())
    write_root_index(root, grouped)
    append_log(root, log)
    was_behind = behind(root, previous.get("commit"))
    consumed = graph_commit(root)
    fresh_graph = consumed != previous.get("graph_commit")  # the cadence counts Graphify incremental builds, not bundle refreshes
    write_state(root, commit=commit, graph_commit=consumed, updates=1 if clean else previous.get("updates", 0) + fresh_graph, ts=stamp)
    for name, value in (
        ("knowledge_nodes", len(graph["nodes"])),
        ("knowledge_communities", len({n.get("community") for n in graph["nodes"] if n.get("community") is not None})),
        ("knowledge_stale", stale),
        ("knowledge_unverified", unverified),
        ("knowledge_behind", was_behind),
    ):
        maintain.ingest(root, name, float(value))
    return {
        "ok": True,
        "concepts": len(concepts),
        "created": created,
        "updated": updated,
        "tombstoned": tombstoned,
        "unresolved": unresolved,
        "source_commit": commit,
        "bundle": str(home.relative_to(root)),
        "rebuild": "clean" if clean else "incremental",
    }


def concept_files(root: Path) -> list[Path]:
    home = bundle_dir(root)
    return sorted(f for f in home.rglob("*.md") if f.name not in ("index.md", "log.md")) if home.exists() else []


FILES_LINE = re.compile(r"^- `([^`]+)`", re.MULTILINE)


def concepts_for(root: Path, rel: str) -> list[str]:
    """Bundle-relative module concept paths whose `# Files` section lists `rel`; empty when the layer is off."""
    if not enabled(root):
        return []
    home = bundle_dir(root) / "modules"
    hits = []
    for path in sorted(home.glob("*.md")) if home.exists() else []:
        if path.name == "index.md":
            continue
        _, body = split_document(path.read_text())
        files_section = body.split("# Files", 1)[-1].split("\n# ", 1)[0]
        if rel in FILES_LINE.findall(files_section):
            hits.append(str(path.relative_to(root)))
    return hits


def check(root: Path) -> dict:
    """Three separate lists: official OKF v0.2 conformance (the only one that fails), organisational policy, trust tiers."""
    if not enabled(root):
        return SKIPPED
    home = bundle_dir(root)
    conformance, policy, tiers = [], [], {"unverified": 0, "machine-confirmed": 0, "human-reviewed": 0}
    now = now_iso()
    for path in concept_files(root):
        rel = str(path.relative_to(home))
        text = path.read_text()
        front, _ = split_document(text)
        if not text.startswith(FENCE + "\n") or (not front and text.startswith(FENCE)):
            conformance.append(f"{rel}: no parseable YAML frontmatter block")
            continue
        if "_raw" in front and "type" not in front:
            conformance.append(f"{rel}: frontmatter is not parseable YAML")
            continue
        if not isinstance(front.get("type"), str) or not front["type"].strip():
            conformance.append(f"{rel}: missing or empty `type`")
            continue
        events = front.get("verified", [])
        events = [events] if isinstance(events, dict) else events
        actors = [str(e.get("by", "")) for e in events if isinstance(e, dict)]
        tier = "human-reviewed" if any(x.startswith("human:") for x in actors) else "machine-confirmed" if actors else "unverified"
        tiers[tier] += 1
        policy += [f"{rel}: {finding}" for finding in policy_findings(front, actors, now)]
    verdict = {"ok": not conformance, "conformance": conformance, "policy": policy, "trust": tiers, "concepts": len(concept_files(root))}
    if conformance:
        verdict["reason"] = f"{len(conformance)} conformance finding(s) (OKF v0.2 SPEC.md section 11): " + "; ".join(conformance[:3])
    return verdict


def policy_findings(front: dict, actors: list[str], now: str) -> list[str]:
    """Organisational rules, stricter than the spec and reported apart from it."""
    out = [f"missing `{key}` (policy)" for key in ("title", "generated", "source_commit") if not front.get(key)]
    status = front.get("status", "stable")
    if status == "draft" and any(x.startswith("human:") for x in actors):
        out.append("draft concept carries a human: verified event; only an accept may write one (policy)")
    if status == "stable" and str(front.get("stale_after", "9")) < now:
        out.append(f"stable concept past stale_after {front.get('stale_after')} (policy)")
    for actor in actors:
        if not re.fullmatch(r"(human|process):\S+|\S+/\S+", actor):
            out.append(f"verified.by {actor!r} does not follow the actor convention (policy)")
    return out


def as_actor(name: str) -> str:
    """OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare name is a human."""
    return name if name.startswith(("human:", "process:")) or "/" in name else f"human:{a.slugify(name)}"


def publish(root: Path, feature: Path, actor: str) -> dict:
    """Append a verification event to the feature's concept; only a human: actor promotes it to stable."""
    if not enabled(root):
        return SKIPPED
    rel = f"features/{feature.name}.md"
    path = bundle_dir(root) / rel
    refresh(root, quiet=True)  # the concept must describe the artifact as it is now, then the event is appended
    if not path.exists():
        fail(f"no concept generated for {feature.name}; run `sdlc knowledge refresh`", concept=rel)
    front, body = split_document(path.read_text())
    who = as_actor(actor)
    events = front.get("verified", [])
    events = [events] if isinstance(events, dict) else list(events)
    events.append({"by": who, "at": now_iso()})
    status = "stable" if who.startswith("human:") else front.get("status", "draft")
    ordered = {}
    for key, value in front.items():
        if key == "status":
            ordered[key] = status
        elif key == "generated":
            ordered[key] = value
            ordered["verified"] = events
        elif key != "verified":
            ordered[key] = value
    ordered.setdefault("verified", events)
    ordered.setdefault("status", status)
    path.write_text(dump_frontmatter(ordered) + "\n" + body)
    append_log(root, [f"**Update**: [{front.get('title', feature.name)}](/{rel}) verified by {who}."])
    return {"ok": True, "concept": rel, "actor": who, "status": status}
