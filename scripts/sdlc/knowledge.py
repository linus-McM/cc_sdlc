"""Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle (sdlc/knowledge/).

Public mechanics: bootstrap, status, refresh, check, publish, unhook. Every one is a no-op verdict
when the layer is off (`[knowledge] enabled = false` or SDLC_KNOWLEDGE=off). Graphify and uv are
subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import functools
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
from collections import Counter
from datetime import UTC, datetime, timedelta
from pathlib import Path

from . import artifacts as a
from . import build, deploy, docs, testing
from . import project as p
from .project import Blocked, fail

TEMPLATES = p.TEMPLATES / "knowledge"
POINTER_START = "<!-- sdlc-knowledge-start -->"

SKIPPED = {"ok": True, "skipped": "knowledge disabled"}
FENCE = "---"
BAD = re.compile(r"[:#\[\]{}\",']|^\s|\s$|^[-?&*!|>%@`]")
NUMBERISH = re.compile(r"^[-+]?(\d[\d_]*\.?\d*([eE][-+]?\d+)?|\.\d+)$")


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


def when_enabled(default=SKIPPED):
    """Gate a public mechanic on the layer being on; `default` is the verdict (or value) when it is off."""

    def wrap(fn):
        @functools.wraps(fn)
        def inner(root: Path, *args, **kwargs):
            return fn(root, *args, **kwargs) if enabled(root) else default

        return inner

    return wrap


# --- paths and small helpers ---


BUNDLE_OK = re.compile(r"^[A-Za-z0-9._][A-Za-z0-9._/-]*$")


def cfg(root: Path) -> dict:
    """The [knowledge] table; `bundle` is validated here because it becomes a path, a grep pattern and CLAUDE.md text."""
    conf = p.config(root)["knowledge"]
    bundle = str(conf["bundle"])
    if not BUNDLE_OK.match(bundle) or ".." in Path(bundle).parts or bundle.endswith("/"):
        fail(f"[knowledge] bundle {bundle!r} must be a relative path made of letters, digits, `.`, `_`, `-` and `/`, without `..`")
    return conf


def shell_word(text: str) -> str:
    """`text` as one double-quoted POSIX shell word: backslash, double quote, dollar and backtick escaped."""
    return '"' + re.sub(r'([\\"$`])', r"\\\1", text) + '"'


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
    """`.state.json`, or `{"_error": reason}` when it exists but cannot be read (a merge conflict, say): never a traceback in a hook."""
    try:
        return p.read_json(state_path(root), {})
    except Blocked as blocked:
        return {"_error": blocked.verdict["reason"]}


def write_state(root: Path, **fields) -> dict:
    state = {**{k: v for k, v in read_state(root).items() if k != "_error"}, **fields}
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


# --- git post-commit block, appended after Graphify's own ---

BLOCK_START, BLOCK_END = "# sdlc-knowledge-start", "# sdlc-knowledge-end"
GRAPHIFY_MARKER = "# graphify-hook-start"
WORKTREE_HOOK = "linked worktree: the shared post-commit hook is owned by the primary checkout; run `sdlc knowledge bootstrap` there"
BLOCK_RE = re.compile(rf"\n?{BLOCK_START}.*?{BLOCK_END}\n", re.DOTALL)


def hook_block(root: Path) -> str:
    text = (TEMPLATES / "post-commit.sh").read_text()
    return text.replace("__SDLC_PY__", shell_word(str(p.PLUGIN_ROOT / "scripts" / "sdlc.py"))).replace("__BUNDLE__", cfg(root)["bundle"])


def our_block_present(root: Path) -> bool:
    hook = post_commit_path(root)
    return hook.exists() and hook_block(root) in hook.read_text()


def linked_worktree(root: Path) -> bool:
    """A `git worktree` checkout: `.git` is a file pointing at the primary's git dir, whose hooks are shared."""
    return (root / ".git").is_file()


def install_hook(root: Path) -> dict:
    """Idempotent: replaces an existing sdlc block, otherwise appends after everything else. Never from a linked worktree."""
    if linked_worktree(root):
        fail(WORKTREE_HOOK)
    hook = post_commit_path(root)
    hook.parent.mkdir(parents=True, exist_ok=True)
    text = BLOCK_RE.sub("\n", hook.read_text()) if hook.exists() else "#!/bin/sh\n"
    text = text.rstrip("\n") + "\n" + hook_block(root)
    hook.write_text(text)
    hook.chmod(hook.stat().st_mode | 0o755)
    return {"ok": True, "path": str(hook)}


@when_enabled()
def unhook(root: Path) -> dict:
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


class StepSkipped(Exception):
    """This step does not apply here; later steps still run."""


def ran(root: Path, argv: list[str], ok) -> str:
    """Run an install command; StepFailed with its stderr tail when it exits non-zero or `ok()` is false afterwards."""
    result = tool(root, *argv)
    if result.returncode != 0 or not ok():
        raise StepFailed(f"{' '.join(argv)} exited {result.returncode}: {result.stderr.strip()[-200:] or 'expected result missing'}")
    return " ".join(argv)


def install_uv(root: Path, conf: dict) -> str:
    return ran(root, uv_install_command(), lambda: find_uv() is not None)


def install_graphify(root: Path, conf: dict) -> str:
    return ran(root, ["uv", "tool", "install", "graphifyy"], lambda: shutil.which("graphify") is not None)


def install_skill(root: Path, conf: dict) -> str:
    return ran(root, ["graphify", "install", "--platform", "claude"], skill_path().exists)


def hooks_present(root: Path, conf: dict) -> bool:
    """Both blocks in the post-commit file, read from the file (no subprocess). A linked worktree shares the primary's
    hook and accepts any sdlc block there; the primary insists on a block naming its own plugin path."""
    hook = post_commit_path(root)
    if not hook.exists():
        return False
    text = hook.read_text()
    ours = BLOCK_START in text if linked_worktree(root) else hook_block(root) in text
    return GRAPHIFY_MARKER in text and ours


def install_hooks(root: Path, conf: dict) -> str:
    if linked_worktree(root):
        raise StepSkipped(WORKTREE_HOOK)
    hook = post_commit_path(root)
    done = []
    if not hook.exists() or GRAPHIFY_MARKER not in hook.read_text():
        done.append(ran(root, ["graphify", "hook", "install"], lambda: True))
    install_hook(root)
    return "; ".join([*done, "sdlc block appended to post-commit"])


def write_ignore(root: Path, conf: dict) -> str:
    (root / ".graphifyignore").write_text("".join(f"{line}\n" for line in conf["ignore"]))
    return ".graphifyignore from [knowledge] ignore"


def build_graph(root: Path, conf: dict) -> str:
    return ran(root, ["graphify", "update", "."], graph_path(root).exists)


def bundle_present(root: Path, conf: dict) -> bool:
    """A bundle counts only when it was built from the graph that exists now (an accept can publish before any graph)."""
    return (bundle_dir(root) / "index.md").exists() and read_state(root).get("graph_commit") == graph_commit(root)


def build_bundle(root: Path, conf: dict) -> str:
    refresh(root)
    return conf["bundle"]


def pointer_present(root: Path, conf: dict) -> bool:
    path = root / "CLAUDE.md"
    return path.exists() and POINTER_START in path.read_text()


def write_pointer(root: Path, conf: dict) -> str:
    path = root / "CLAUDE.md"
    block = a.render(TEMPLATES / "claude-pointer.md", bundle=conf["bundle"])
    text = path.read_text() if path.exists() else ""
    path.write_text(text + ("\n" if text and not text.endswith("\n") else "") + block)
    return "CLAUDE.md pointer block"


# (name, present?(root, conf), install(root, conf) -> detail, state after installing, detail when present)
STEPS = (
    ("uv", lambda r, c: find_uv() is not None, install_uv, "installed", "uv"),
    ("graphify", lambda r, c: shutil.which("graphify") is not None, install_graphify, "installed", "graphify on PATH"),
    ("skill", lambda r, c: skill_path().exists(), install_skill, "installed", "Claude skill"),
    ("archify", docs.archify_present, docs.install_archify, "installed", f"Archify skill; install: {' '.join(docs.INSTALL)}"),
    ("hooks", hooks_present, install_hooks, "installed", "git post-commit hook"),
    ("graphifyignore", lambda r, c: (r / ".graphifyignore").exists(), write_ignore, "built", ".graphifyignore"),
    ("graph", lambda r, c: graph_path(r).exists(), build_graph, "built", "graphify-out/graph.json"),
    ("bundle", bundle_present, build_bundle, "built", "OKF bundle"),
    ("claude_md", pointer_present, write_pointer, "built", "CLAUDE.md pointer"),
)


@when_enabled()
def bootstrap(root: Path, check: bool = False) -> dict:
    conf = cfg(root)
    steps: list[dict] = []
    failed = None
    for name, present, install, done_state, detail in STEPS:
        try:
            found = None if failed else present(root, conf)
        except StepSkipped as why:
            found, state, detail = None, "skipped", str(why)
            steps.append({"name": name, "state": state, "detail": detail})
            continue
        if failed:
            state, detail = "skipped", "earlier step failed"
        elif found:
            state, detail = "present", (str(found) if isinstance(found, docs.Present) else detail)
        elif name == "claude_md" and not conf["claude_md_pointer"]:
            state = "skipped"
        elif check:
            state = "missing"
        else:
            try:
                state, detail = done_state, install(root, conf)
            except StepSkipped as why:
                state, detail = "skipped", str(why)
            except StepFailed as err:
                state, detail, failed = "failed", str(err), name
        steps.append({"name": name, "state": state, "detail": detail})
    missing = [s["name"] for s in steps if s["state"] == "missing"]
    verdict = {"ok": not failed and not missing, "mode": "check" if check else "install", "steps": steps}
    if failed:
        verdict["reason"] = f"bootstrap step {failed} failed: " + next(s["detail"] for s in steps if s["name"] == failed)
    elif missing:
        verdict["reason"] = "missing: " + ", ".join(missing) + " (run `sdlc knowledge bootstrap` to install)"
    return verdict


# --- staleness and status: is either index behind HEAD, do the graph artifacts agree, is a clean rebuild due ---

BUILT_AT = re.compile(r'"built_at_commit"\s*:\s*"([0-9a-f]{7,40})"')


def graph_commit(root: Path) -> str | None:
    path = graph_path(root)
    if not path.exists():
        return None
    match = BUILT_AT.search(path.read_text())
    return match.group(1) if match else None


def rebuild_log_tail() -> str | None:
    """Last line of Graphify's rebuild log, read from its tail only (the log is append-only and never truncated)."""
    path = Path(os.environ.get("GRAPHIFY_REBUILD_LOG") or Path.home() / ".cache" / "graphify-rebuild.log")
    try:
        with path.open("rb") as fh:
            fh.seek(max(0, path.stat().st_size - 4096))
            lines = fh.read().decode("utf-8", "replace").splitlines()
    except OSError:
        return None
    return next((line for line in reversed(lines) if line.strip()), None)


def artifacts_agree(root: Path, conf: dict) -> bool:
    out = graph_path(root).parent
    stamps = [(out / name).stat().st_mtime for name in ("graph.json", "GRAPH_REPORT.md", "graph.html") if (out / name).exists()]
    return len(stamps) < 2 or max(stamps) - min(stamps) <= conf["artifact_skew_seconds"]


def verified_events(front: dict) -> list[dict]:
    """`verified` as a list: the spec lets a single event be written as a bare mapping."""
    events = front.get("verified", [])
    return [events] if isinstance(events, dict) else [e for e in events if isinstance(e, dict)]


def is_stale(front: dict, now: str) -> bool:
    return str(front.get("stale_after", "9")) < now


def behind(root: Path, since: str | None) -> int | None:
    """Commits from `since` to HEAD; None when git cannot resolve `since` (shallow clone, rebase, foreign history)."""
    if not since:
        return 0
    result = p.run_git(root, "rev-list", "--count", f"{since}..HEAD")
    return int(result.stdout.strip() or 0) if result.returncode == 0 else None


def staleness(root: Path, conf: dict, state: dict) -> dict:
    """The cheap part of status: how far each index is behind HEAD and why a clean rebuild would be due."""
    gcommit = graph_commit(root)
    st = {"graph_commit": gcommit, "graph_behind": behind(root, gcommit), "bundle_commit": state.get("commit"), "bundle_behind": behind(root, state.get("commit")), "updates": state.get("updates", 0)}
    reasons = []
    unknown = "recorded commit {commit} is not in this repository's history (shallow clone, rebase or a {what} from another history); run `{fix}`"
    if gcommit is None:
        reasons.append("graphify-out/graph.json missing or without built_at_commit; run `sdlc knowledge bootstrap`")
    elif st["graph_behind"] is None:
        reasons.append(unknown.format(commit=gcommit[:12], what="graph", fix="graphify update . --force"))
    elif st["graph_behind"] > conf["max_behind"]:
        reasons.append(f"graph is {st['graph_behind']} commits behind HEAD (max_behind {conf['max_behind']}); graphify-out/graph.json needs `graphify update .`")
    if "_error" in state:
        reasons.append(f"{conf['bundle']}/.state.json unreadable ({state['_error']}); run `sdlc knowledge refresh` to rewrite it")
    elif st["bundle_commit"] is None:
        reasons.append(f"{conf['bundle']} has no .state.json; run `sdlc knowledge refresh`")
    elif st["bundle_behind"] is None:
        reasons.append(unknown.format(commit=st["bundle_commit"][:12], what="bundle", fix="sdlc knowledge refresh"))
    elif st["bundle_behind"] > conf["max_behind"]:
        reasons.append(f"bundle is {st['bundle_behind']} commits behind HEAD (max_behind {conf['max_behind']}); run `sdlc knowledge refresh`")
    if st["updates"] >= conf["clean_every"]:
        reasons.append(f"{st['updates']} refreshes since the last clean rebuild (clean_every {conf['clean_every']}); the next refresh rebuilds the graph with --force")
    return {**st, "reasons": reasons}


def bundle_counts(files: list[Path], now: str) -> dict:
    counts = {"concepts": 0, "stale": 0, "unverified": 0, "draft": 0}
    for path in files:
        front, _ = split_document(path.read_text())
        counts["concepts"] += 1
        counts["stale"] += is_stale(front, now)
        counts["unverified"] += not verified_events(front)
        counts["draft"] += front.get("status") == "draft"
    return counts


@when_enabled()
def status(root: Path) -> dict:
    conf = cfg(root)
    st = staleness(root, conf, read_state(root))
    graph = {"commit": st["graph_commit"], "behind": st["graph_behind"], "artifacts_agree": artifacts_agree(root, conf), "last_rebuild": rebuild_log_tail()}
    bundle = {"commit": st["bundle_commit"], "behind": st["bundle_behind"], "updates": st["updates"], **bundle_counts(concept_files(root), now_iso())}
    notes = [] if graph["artifacts_agree"] else [f"graph artifacts skew: graph.json, GRAPH_REPORT.md and graph.html mtimes differ by more than {conf['artifact_skew_seconds']}s"]
    verdict = {"ok": not st["reasons"], "graph": graph, "bundle": bundle, "rebuild": "clean" if st["reasons"] else "incremental", "reasons": st["reasons"], "notes": notes}
    if st["reasons"]:
        verdict["reason"] = "; ".join(st["reasons"])
    return verdict


# --- refresh: graph.json + sdlc artifacts -> OKF bundle ---

VOLATILE = ("status", "generated", "verified", "stale_after")  # frontmatter that never counts as a content change
HEAD = ("type", "title", "description", "resource", "tags")  # the recommended keys, written first
DIRS = ("features", "modules", "hubs", "lessons", "bands")
DERIVED = ("hubs",)  # concepts whose existence is a graph property, tombstoned as soon as the graph stops producing them
LESSON_LINE = re.compile(r"^- (\d{4}-\d{2}-\d{2}): (.+)$", re.MULTILINE)
DOC_SUFFIXES = (".md", ".markdown", ".rst", ".txt", ".pdf", ".png", ".jpg", ".jpeg", ".svg", ".mp4")
GRAPH_JSON = "graphify-out/graph.json"


def now_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


@functools.cache
def plugin_version() -> str:
    return p.read_json(p.PLUGIN_ROOT / ".claude-plugin" / "plugin.json", {}).get("version", "0")


def load_graph(root: Path) -> dict:
    return p.read_json(graph_path(root), {"nodes": [], "links": []})


def is_code(node: dict) -> bool:
    """Graphify tags code, document and rationale nodes; only code communities become Module concepts."""
    if "file_type" in node:
        return node["file_type"] == "code"
    return node.get("_origin") == "ast" and not str(node.get("source_file", "")).lower().endswith(DOC_SUFFIXES)


def community_labels(root: Path, graph: dict) -> dict[int, str]:
    labels = {int(k): v for k, v in p.read_json(graph_path(root).parent / ".graphify_labels.json", {}).items()}
    for node in graph["nodes"]:
        cid = node.get("community")
        if cid is not None and cid not in labels and node.get("community_name"):
            labels[cid] = node["community_name"]
    return labels


def communities(root: Path, graph: dict, conf: dict) -> list[dict]:
    """Graphify code communities big enough for a Module concept, with a stable slug each."""
    groups: dict[int, list[dict]] = {}
    for node in graph["nodes"]:
        if node.get("community") is not None and node.get("source_file"):
            groups.setdefault(node["community"], []).append(node)
    labels = community_labels(root, graph)
    out, taken = [], set()
    for cid in sorted(groups):
        nodes = groups[cid]
        if sum(is_code(n) for n in nodes) < conf["min_community_nodes"]:
            continue
        name = labels.get(cid) or f"Community {cid}"
        slug = a.slugify(name) or f"community-{cid}"
        slug = slug if slug not in taken else f"{slug}-{cid}"
        taken.add(slug)
        out.append({"cid": cid, "name": name, "slug": slug, "files": sorted({n["source_file"] for n in nodes}), "nodes": nodes})
    return out


def god_nodes(graph: dict, top: int) -> list[dict]:
    """The most connected code nodes by degree, from the graph already in memory (what `graphify god-nodes` ranks)."""
    degree: Counter = Counter()
    for edge in graph["links"]:
        degree[edge["source"]] += 1
        degree[edge["target"]] += 1
    code = {n["id"]: n.get("label", n["id"]) for n in graph["nodes"] if is_code(n)}
    ranked = sorted(((d, i) for i, d in degree.items() if d > 1 and i in code), key=lambda x: (-x[0], x[1]))
    return [{"id": i, "label": code[i], "degree": d} for d, i in ranked[:top]]


def concept(path: str, type_: str, title: str, description: str, resource: str, tags: list[str], sources: list[str], body: str, **extra) -> dict:
    return {
        "path": path,
        "front": {"type": type_, "title": title.rstrip(), "description": description[:200].rstrip(), "resource": resource, "tags": tags, **extra},
        "sources": sources,
        "body": "\n".join(line.rstrip() for line in body.rstrip("\n").splitlines()) + "\n",  # no trailing whitespace: pre-commit would rewrite the file
    }


def link(c: dict) -> str:
    return f"[{c['front']['title']}](/{c['path']})"


def section(heading: str, lines: list[str], empty: str = "none") -> str:
    return f"# {heading}\n" + ("\n".join(lines) if lines else f"- {empty}") + "\n\n"


def head_first(front: dict, **overrides) -> dict:
    """`front` with the recommended keys first, then `overrides` in order, then everything else."""
    rest = {k: v for k, v in front.items() if k not in HEAD and k not in overrides}
    return {**{k: front[k] for k in HEAD if k in front}, **overrides, **rest}


def module_concepts(graph: dict, comms: list[dict], plans: dict[Path, set[str]], titles: dict[Path, str]) -> tuple[list[dict], dict[str, dict]]:
    by_node = {n["id"]: c for c in comms for n in c["nodes"]}
    module_link = {c["slug"]: f"[{c['name']}](/modules/{c['slug']}.md)" for c in comms}
    edges: dict[str, dict[str, set[str]]] = {c["slug"]: {"EXTRACTED": set(), "other": set()} for c in comms}
    for edge in graph["links"]:  # one pass over the edges for every community
        src, dst = by_node.get(edge["source"]), by_node.get(edge["target"])
        if src is not None and dst is not None and src is not dst:
            edges[src["slug"]]["EXTRACTED" if edge.get("confidence", "EXTRACTED") == "EXTRACTED" else "other"].add(dst["slug"])
    out = []
    for c in comms:
        symbols = sorted(c["nodes"], key=lambda n: (n["source_file"], n.get("source_location", "")))
        backlinks = [d for d, files in plans.items() if files & set(c["files"])]
        out.append(
            concept(
                f"modules/{c['slug']}.md",
                "Module",
                c["name"],
                f"Graphify community {c['cid']}: " + ", ".join(c["files"]),
                os.path.commonpath(c["files"]) if len(c["files"]) > 1 else str(Path(c["files"][0]).parent),
                ["module", "graphify"],
                c["files"],
                section("Files", [f"- `{f}`" for f in c["files"]])
                + section("Symbols", [f"- {n['label']} ({n['source_file']}:{n.get('source_location', '')})" for n in symbols])
                + section("Depends on", [f"- {module_link[x]}" for x in sorted(edges[c["slug"]]["EXTRACTED"])], "no EXTRACTED edges to other modules")
                + section("Inferred", [f"- {module_link[x]}" for x in sorted(edges[c["slug"]]["other"])], "no INFERRED edges; treat any that appear as hints")
                + section("Features", [f"- [{titles[d]}](/features/{d.name}.md)" for d in backlinks], "no feature plan names these files"),
            )
        )
    return out, {f: c for m, c in zip(comms, out, strict=True) for f in m["files"]}


def review_counts(feature: Path) -> str:
    path = feature / "review.md"
    if not path.exists():
        return "no review yet"
    text = path.read_text()
    return f"Important: {testing.count(text, 'Important')}, Nit: {testing.count(text, 'Nit')}"


def feature_status(feature: Path) -> list[str]:
    lines = []
    for name in ("intent.md", "spec.md", "plan.md"):
        path = feature / name
        lines.append(f"- {name}: " + ((a.status(path.read_text()) or "draft") if path.exists() else "missing"))
    report = testing.report(feature) or {}
    lines.append(f"- test-report: {'passed' if report.get('passed') else 'missing or failed'}")
    envs = sorted({d["env"] for d in deploy.state(feature)["deployments"]})
    lines.append("- deployed: " + (", ".join(envs) or "nowhere"))
    return lines


def feature_concepts(root: Path, plans: dict[Path, set[str]], titles: dict[Path, str], module_of: dict[str, dict]) -> list[dict]:
    out = []
    for d, files in plans.items():
        intent = (d / "intent.md").read_text()
        spec = (d / "spec.md").read_text() if (d / "spec.md").exists() else ""
        sections = a.sections(intent)
        file_lines = [f"- `{f}`" + (f" in {link(module_of[f])}" if f in module_of else "") for f in sorted(files)]
        rel = str(d.relative_to(root))
        out.append(
            concept(
                f"features/{d.name}.md",
                "Feature",
                titles[d],
                a.first_line(sections.get("Problem", "")) or titles[d],
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


def hub_concepts(graph: dict, comms: list[dict], conf: dict) -> list[dict]:
    nodes = {n["id"]: n for n in graph["nodes"]}
    by_node = {n["id"]: c for c in comms for n in c["nodes"]}
    out, taken = [], set()
    for hub in god_nodes(graph, conf["god_nodes"]):
        node = nodes.get(hub["id"], {})
        slug = a.slugify(hub["label"]) or "hub"
        slug = slug if slug not in taken else f"{slug}-{len(taken)}"
        taken.add(slug)
        module = by_node.get(hub["id"])
        src = node.get("source_file", "")
        out.append(
            concept(
                f"hubs/{slug}.md",
                "Hub",
                hub["label"],
                f"Graphify god node with degree {hub['degree']}" + (f" in {src}" if src else ""),
                src or GRAPH_JSON,
                ["hub", "graphify"],
                [src or GRAPH_JSON],
                section("Where", [f"- `{src}:{node.get('source_location', '')}`" if src else "- not in the current graph"])
                + section("Module", [f"- [{module['name']}](/modules/{module['slug']}.md)"] if module else [], "no module concept covers this node")
                + section("Why it matters", [f"- degree {hub['degree']}: many modules reach this symbol; changes here have a wide blast radius"]),
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
    rel = str(path.relative_to(root))
    out, firsts = [], [first_sentence(text) for _, _, text in rows]
    for i, (date, n, text) in enumerate(rows):
        older = [j for j in range(i) if len(firsts[j]) >= 20 and firsts[j] in text]
        extra = {"supersedes": f"/lessons/{rows[older[-1]][0]}-{rows[older[-1]][1]}.md"} if older else {}
        out.append(
            concept(
                f"lessons/{date}-{n}.md",
                "Lesson",
                firsts[i][:80],
                text,
                rel,
                ["lesson", date],
                [rel],
                section("Lesson", [f"- {date}: {text}"]) + section("Scope", [f"- repository `{root.name}`; recorded by the maintain stage"]),
                **extra,
            )
        )
    return out


def band_concepts(root: Path) -> list[dict]:
    from . import maintain

    readings = maintain.readings(root, None)
    rel = str((p.home(root) / "bands.toml").relative_to(root))
    out = []
    for metric, band in maintain.bands(root).items():
        band = {**maintain.DEFAULT_BAND, **band}
        values = readings.get(metric, [])
        out.append(
            concept(
                f"bands/{a.slugify(metric)}.md",
                "Control Band",
                metric,
                f"Western Electric band on {metric}; bad side {band['bad']}, window {band['window']}",
                rel,
                ["band", "maintain"],
                [rel],
                section("Band", [f"- window: {band['window']}", f"- tiers: {', '.join(band['tiers'])}", f"- bad side: {band['bad']}"])
                + section("Latest reading", [f"- {values[-1]}"] if values else [], "no readings yet"),  # no count: refresh itself appends readings
            )
        )
    return out


RUN_KEYS = (*VOLATILE, "source_commit", "sources", "_raw")  # written by the run, never part of a concept's content identity


def content_keys(new_front: dict, existing_front: dict | None) -> list[str]:
    return sorted((set(new_front) | set(existing_front or ())) - set(RUN_KEYS))


def signature(front: dict, body: str, keys) -> str:
    """Content identity: the builder's keys (present on either side) plus the body; run-written fields never count."""
    return json.dumps({k: front.get(k) for k in keys}, sort_keys=True) + body.lstrip("\n")


ISO_LINE = re.compile(r"^\d{4}-\d{2}-\d{2}T[\d:]+[+-Z][\d:]*$")


def last_modified(root: Path, sources: list[str]) -> dict[str, str]:
    """Last commit date per source path from one `git log --name-only` over all of them; uncommitted paths fall back to now."""
    result = p.run_git(root, "log", "--format=%cI", "--name-only", "--", *sorted(sources))
    seen, stamp = {}, now_iso()
    for line in result.stdout.splitlines() if result.returncode == 0 else []:
        if ISO_LINE.match(line.strip()):
            stamp = line.strip()
        elif line.strip():
            seen.setdefault(line.strip(), stamp)
    return {rel: seen.get(rel, now_iso()) for rel in sources}


class Digests(dict):
    """sha256 prefix per repo-relative source path, hashed at most once per refresh; None when the file is gone."""

    def __init__(self, root: Path):
        super().__init__()
        self.root = root

    def __missing__(self, rel: str) -> str | None:
        path = self.root / rel
        self[rel] = hashlib.sha256(path.read_bytes()).hexdigest()[:16] if path.is_file() else None
        return self[rel]


def sources_changed(front: dict, sources: list[str], digests: Digests) -> bool:
    """True when any source's content differs from the digest recorded at generation (no digest counts as changed)."""
    recorded = {s.get("resource"): s.get("digest") for s in front.get("sources", []) if isinstance(s, dict)}
    return any(recorded.get(rel) != digests[rel] for rel in sources)


def render_concept(c: dict, existing: dict | None, run: dict, reset: bool) -> str:
    """Frontmatter plus body; `reset` (a source changed) drops the concept back to draft, a body-only change keeps its status."""
    trust = {"verified": existing["verified"]} if existing and existing.get("verified") else {}
    front = head_first(
        c["front"],
        status="draft" if reset or not existing else existing.get("status", "draft"),
        generated={"by": run["by"], "at": run["stamp"]},
        **trust,
        stale_after=run["stale_after"],
        source_commit=run["commit"],
        sources=[{"id": Path(src).stem, "resource": src, "last_modified": run["modified"][src], "digest": run["digests"][src] or "missing"} for src in c["sources"]],
    )
    return dump_frontmatter(front) + "\n" + c["body"]


def index_lines(entries: list[dict], basename: bool) -> str:
    """`* [Title](link) - description` per concept, sorted by title; sub-indexes link by basename."""
    ordered = sorted(entries, key=lambda e: e["front"]["title"].lower())
    lines = [f"* [{e['front']['title']}]({Path(e['path']).name if basename else e['path']}) - {e['front']['description']}" for e in ordered]
    return "\n".join(lines) if lines else "* none yet"


def write_indexes(root: Path, home: Path, concepts: list[dict]) -> None:
    grouped: dict[str, list[dict]] = {d: [] for d in DIRS}
    for c in concepts:
        grouped[c["path"].split("/", 1)[0]].append(c)
    for d in DIRS:
        (home / d).mkdir(parents=True, exist_ok=True)
        (home / d / "index.md").write_text(f"# {d.capitalize()}\n\n" + index_lines(grouped[d], basename=True) + "\n")
    parts = [f"# {d.capitalize()}\n" + index_lines(grouped[d], basename=False) for d in DIRS]
    (home / "index.md").write_text(a.render(TEMPLATES / "index.md", title=f"{root.name} knowledge", sections="\n\n".join(parts)))


def append_log(root: Path, entries: list[str]) -> None:
    if not entries:
        return
    path = bundle_dir(root) / "log.md"
    today = p.today()
    text = path.read_text() if path.exists() else a.render(TEMPLATES / "log.md", date=today)
    block = "\n".join(f"* {e}" for e in entries)
    heading = f"## {today}\n"
    if heading in text:
        text = text.replace(heading, heading + block + "\n", 1)
    else:
        title, _, rest = text.partition("\n")
        text = f"{title}\n\n{heading}{block}\n" + (("\n" + rest.lstrip("\n")) if rest.strip() else "")
    path.write_text(text)


def reconcile(root: Path, home: Path, concepts: list[dict], run: dict, log: list[str]) -> tuple[int, list[str]]:
    """Concept files nothing generated any more: tombstone when every source is confirmed gone, else keep and report."""
    generated = {c["path"] for c in concepts}
    titles = {c["front"]["title"]: c for c in concepts}
    tombstoned, unresolved = 0, []
    for path in sorted(home.glob("*/*.md")):
        rel = str(path.relative_to(home))
        if path.name == "index.md" or path.parent.name not in DIRS or rel in generated:
            continue
        front, _ = split_document(path.read_text())
        if front.get("status") == "deprecated":
            continue
        sources = [s.get("resource") for s in front.get("sources", []) if isinstance(s, dict) and isinstance(s.get("resource"), str)]
        inside = [s for s in sources if not Path(s).is_absolute() and ".." not in Path(s).parts]
        derived = path.parent.name in DERIVED  # a hub's standing comes from the graph, not from its file
        if not derived and (not inside or len(inside) != len(sources) or any((root / s).exists() for s in inside)):
            unresolved.append(rel)
            continue
        replacement = titles.get(front.get("title"))
        front.pop("stale_after", None)
        tomb = head_first(front, status="deprecated", generated={"by": run["by"], "at": run["stamp"]}, source_commit=run["commit"])
        body = section(
            "Deprecated",
            [f"- sources removed by commit `{run['commit'][:12]}`: " + ", ".join(f"`{s}`" for s in inside), f"- replacement: {link(replacement)}" if replacement else "- no replacement concept; kept so incoming links still resolve"],
        )
        path.write_text(dump_frontmatter(tomb) + "\n" + body)
        log.append(f"**Deprecation**: [{front.get('title', path.stem)}](/{rel}).")
        tombstoned += 1
    return tombstoned, unresolved


@when_enabled()
def refresh(root: Path) -> dict:
    from . import maintain

    conf, home = cfg(root), bundle_dir(root)
    home.mkdir(parents=True, exist_ok=True)
    previous = read_state(root)
    commit = p.head_commit(root)
    st = staleness(root, conf, previous)
    clean = previous.get("commit") is not None and bool(st["reasons"])
    if shutil.which("graphify") and (clean or st["graph_commit"] != commit):
        # Graphify's own post-commit hook normally did this already; when it did not, the bundle must not come from a stale graph
        argv = ["graphify", "update", ".", *(["--force"] if clean else [])]
        result = tool(root, *argv)
        if result.returncode != 0:
            fail(f"{' '.join(argv)} exited {result.returncode}: {result.stderr.strip()[-200:]}")
    graph = load_graph(root)
    comms = communities(root, graph, conf)
    plans = {d: set(build.planned_files(d)) for d in p.features(root)}
    titles = {d: a.title((d / "intent.md").read_text()) for d in plans}
    modules, module_of = module_concepts(graph, comms, plans, titles)
    concepts = [*feature_concepts(root, plans, titles, module_of), *modules, *hub_concepts(graph, comms, conf), *lesson_concepts(root), *band_concepts(root)]
    stamp = now_iso()
    run = {
        "commit": commit,
        "stamp": stamp,
        "by": f"sdlc/{plugin_version()}",
        "stale_after": (datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=UTC) + timedelta(days=conf["stale_after_days"])).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "digests": Digests(root),
        "modified": {},
    }
    todo = []
    for c in concepts:
        path = home / c["path"]
        existing = split_document(path.read_text()) if path.exists() else None
        keys = content_keys(c["front"], existing[0] if existing else None)
        same = existing and "_raw" not in existing[0] and signature(existing[0], existing[1], keys) == signature(c["front"], c["body"], keys)
        changed = not existing or sources_changed(existing[0], c["sources"], run["digests"])
        if not (same and not changed and not clean):
            todo.append((c, existing, changed, not existing or changed or not same))
    run["modified"] = last_modified(root, sorted({s for c, *_ in todo for s in c["sources"]})) if todo else {}
    created, updated, log = 0, 0, []
    for c, existing, changed, noteworthy in todo:
        path = home / c["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_concept(c, existing[0] if existing else None, run, reset=changed))
        if noteworthy:
            log.append(f"**{'Update' if existing else 'Creation'}**: {link(c)}.")
            created, updated = created + (not existing), updated + bool(existing)
    tombstoned, unresolved = reconcile(root, home, concepts, run, log)
    write_indexes(root, home, concepts)
    append_log(root, log)
    counts = bundle_counts(concept_files(root), stamp)
    consumed = graph.get("built_at_commit")
    fresh_graph = consumed != previous.get("graph_commit")  # the cadence counts Graphify builds, not bundle refreshes
    files: dict[str, list[str]] = {}
    for m, c in zip(comms, modules, strict=True):  # every module a file belongs to, not just the last community seen
        for rel in m["files"]:
            files.setdefault(rel, []).append(c["path"])
    write_state(root, commit=commit, graph_commit=consumed, updates=1 if clean else previous.get("updates", 0) + fresh_graph, ts=stamp, files=files)
    for name, value in (
        ("knowledge_nodes", len(graph["nodes"])),
        ("knowledge_communities", len({n.get("community") for n in graph["nodes"] if n.get("community") is not None})),
        ("knowledge_stale", counts["stale"]),
        ("knowledge_unverified", counts["unverified"]),
        ("knowledge_behind", st["bundle_behind"] if st["bundle_behind"] is not None else -1),
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


# --- consumers: concept lookup, conformance check, publish ---


def concept_files(root: Path) -> list[Path]:
    home = bundle_dir(root)
    return sorted(f for f in home.rglob("*.md") if f.name not in ("index.md", "log.md")) if home.exists() else []


@when_enabled(default=[])
def concepts_for(root: Path, rel: str) -> list[str]:
    """Project-relative module concept paths describing `rel`, from the file map the last refresh recorded (one small read)."""
    bundle = cfg(root)["bundle"]
    return [f"{bundle}/{c}" for c in read_state(root).get("files", {}).get(rel, [])]


@when_enabled()
def check(root: Path) -> dict:
    """Three separate lists: official OKF v0.2 conformance (the only one that fails), organisational policy, trust tiers."""
    home = bundle_dir(root)
    files = concept_files(root)
    conformance, policy, tiers = [], [], {"unverified": 0, "machine-confirmed": 0, "human-reviewed": 0}
    now = now_iso()
    for path in files:
        rel = str(path.relative_to(home))
        front, _ = split_document(path.read_text())
        if not front:
            conformance.append(f"{rel}: no parseable YAML frontmatter block")
            continue
        if "_raw" in front and "type" not in front:
            conformance.append(f"{rel}: frontmatter is not parseable YAML")
            continue
        if not isinstance(front.get("type"), str) or not front["type"].strip():
            conformance.append(f"{rel}: missing or empty `type`")
            continue
        actors = [str(e.get("by", "")) for e in verified_events(front)]
        tier = "human-reviewed" if any(x.startswith("human:") for x in actors) else "machine-confirmed" if actors else "unverified"
        tiers[tier] += 1
        policy += [f"{rel}: {finding}" for finding in policy_findings(front, actors, now)]
    verdict = {"ok": not conformance, "conformance": conformance, "policy": policy, "trust": tiers, "concepts": len(files)}
    if conformance:
        verdict["reason"] = f"{len(conformance)} conformance finding(s) (OKF v0.2 SPEC.md section 11): " + "; ".join(conformance[:3])
    return verdict


def policy_findings(front: dict, actors: list[str], now: str) -> list[str]:
    """Organisational rules, stricter than the spec and reported apart from it."""
    out = [f"missing `{key}` (policy)" for key in ("title", "generated", "source_commit") if not front.get(key)]
    status = front.get("status", "stable")
    if status == "draft" and any(x.startswith("human:") for x in actors):
        out.append("draft concept carries a human: verified event; only an accept may write one (policy)")
    if status == "stable" and is_stale(front, now):
        out.append(f"stable concept past stale_after {front.get('stale_after')} (policy)")
    for actor in actors:
        if not re.fullmatch(r"(human|process):\S+|\S+/\S+", actor):
            out.append(f"verified.by {actor!r} does not follow the actor convention (policy)")
    return out


def as_actor(name: str) -> str:
    """OKF actor convention: human:<id>, process:<id> or <producer>/<version>; a bare name is a human."""
    return name if name.startswith(("human:", "process:")) or "/" in name else f"human:{a.slugify(name)}"


@when_enabled()
def publish(root: Path, feature: Path, actor: str) -> dict:
    """Append a verification event to the feature's concept; only a human: actor promotes it to stable."""
    rel = f"features/{feature.name}.md"
    path = bundle_dir(root) / rel
    refresh(root)  # the concept must describe the artifact as it is now, then the event is appended
    if not path.exists():
        fail(f"no concept generated for {feature.name}; run `sdlc knowledge refresh`", concept=rel)
    front, body = split_document(path.read_text())
    who = as_actor(actor)
    events = [*verified_events(front), {"by": who, "at": now_iso()}]
    status = "stable" if who.startswith("human:") else front.get("status", "draft")
    front.update(status=status, verified=events)
    path.write_text(dump_frontmatter(front) + "\n" + body)
    append_log(root, [f"**Update**: [{front.get('title', feature.name)}](/{rel}) verified by {who}."])
    return {"ok": True, "concept": rel, "actor": who, "status": status}
