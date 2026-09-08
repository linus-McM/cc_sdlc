"""Knowledge layer: Graphify graph (graphify-out/) plus an OKF v0.2 bundle (sdlc/knowledge/).

Public mechanics: bootstrap, status, refresh, check, publish, unhook. Every one is a no-op verdict
when the layer is off (`[knowledge] enabled = false` or SDLC_KNOWLEDGE=off). Graphify and uv are
subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

from . import artifacts as a
from . import project as p

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
    return parse_frontmatter(text[len(FENCE) + 1 : end + 1]), text[end + len(FENCE) + 2 :]


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

    def hooks_present() -> bool:
        hook = post_commit_path(root)
        if not hook.exists() or not shutil.which("graphify"):
            return False
        if read_state(root).get("hooks_mtime") == hook.stat().st_mtime:
            return True
        if "not installed" in tool(root, "graphify", "hook", "status").stdout:
            return False
        write_state(root, hooks_mtime=hook.stat().st_mtime)
        return True

    def install_hooks():
        result = tool(root, "graphify", "hook", "install")
        if result.returncode != 0:
            raise StepFailed(f"graphify hook install exited {result.returncode}: {result.stderr.strip()[-200:]}")
        return "installed", "graphify hook install"

    def write_ignore():
        (root / ".graphifyignore").write_text("".join(f"{line}\n" for line in conf["ignore"]))
        return "built", ".graphifyignore from [knowledge] ignore"

    def build_graph():
        result = tool(root, "graphify", "update", ".")
        if result.returncode != 0 or not graph_path(root).exists():
            raise StepFailed(f"graphify update . exited {result.returncode}: {result.stderr.strip()[-200:]}")
        return "built", "graphify update ."

    def build_bundle():
        bundle_skeleton(root)
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

    def need_uv():
        raise StepFailed("uv not on PATH; install uv (https://docs.astral.sh/uv/) and rerun")

    step("uv", lambda: shutil.which("uv") is not None or shutil.which("graphify") is not None, need_uv, "uv")
    step("graphify", lambda: shutil.which("graphify") is not None, install_graphify, "graphify on PATH")
    step("skill", lambda: skill_path().exists(), install_skill, str(skill_path()))
    step("hooks", hooks_present, install_hooks, "git post-commit hook")
    step("graphifyignore", lambda: (root / ".graphifyignore").exists(), write_ignore, ".graphifyignore")
    step("graph", lambda: graph_path(root).exists(), build_graph, "graphify-out/graph.json")
    step("bundle", lambda: (bundle_dir(root) / "index.md").exists(), build_bundle, f"{conf['bundle']}/index.md")
    step("claude_md", pointer_present, claude_pointer if conf["claude_md_pointer"] else None, "CLAUDE.md pointer")

    missing = [s["name"] for s in steps if s["state"] == "missing"]
    verdict = {"ok": not failed and not missing, "mode": "check" if check else "install", "steps": steps}
    if failed:
        bad = next(s for s in steps if s["state"] == "failed")
        verdict["reason"] = f"bootstrap step {bad['name']} failed: {bad['detail']}"
    elif missing:
        verdict["reason"] = "missing: " + ", ".join(missing) + " (run `sdlc knowledge bootstrap` to install)"
    return verdict


def status(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def refresh(root: Path, quiet: bool = False) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def check(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def publish(root: Path, feature: Path, actor: str) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError


def unhook(root: Path) -> dict:
    if not enabled(root):
        return SKIPPED
    raise NotImplementedError
