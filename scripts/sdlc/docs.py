"""Stage documents: one Archify HTML diagram per stage, delivered from a Claude-authored JSON source.
Public mechanics: render, check, require, open (plus the archify bootstrap step used by knowledge.STEPS).
Every one is a no-op verdict when the layer is off (`[docs] enabled = false` or SDLC_DOCS=off).
Node and Archify are subprocesses; nothing here imports them or calls an LLM.
"""

from __future__ import annotations

import functools
import hashlib
import json
import os
import re
import shutil
from datetime import UTC, datetime
from pathlib import Path

from . import project as p
from .project import fail

INSTALL = ["npx", "-y", "skills", "add", "tt-a1i/archify", "--skill", "archify", "--agent", "claude-code", "--global", "--copy", "--yes"]
NO_NETWORK = {"ARCHIFY_UPDATE_CHECK_DISABLED": "1"}

SKIPPED = {"ok": True, "skipped": "docs disabled"}
# stage -> files the document describes; relative to the feature directory, except maintain (repo-relative, no feature)
SOURCES = {
    "plan": ["intent.md"],
    "design": ["spec.md"],
    "build": ["plan.md"],
    "test": ["review.md", "test-report.json"],
    "deploy": ["pr-body.md"],
    "maintain": ["sdlc/bands.toml"],
}


def cfg(root: Path) -> dict:
    return p.config(root)["docs"]


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_DOCS") != "off" and bool(cfg(root)["enabled"])


def when_enabled(fn):
    @functools.wraps(fn)
    def inner(root: Path, *args, **kwargs):
        return fn(root, *args, **kwargs) if enabled(root) else SKIPPED

    return inner


# --- the installed skill and Node ---


def skill_dir() -> Path:
    base = Path(os.environ["CLAUDE_CONFIG_DIR"]) if os.environ.get("CLAUDE_CONFIG_DIR") else Path.home() / ".claude"
    return base / "skills" / "archify"


def installed() -> bool:
    return (skill_dir() / "bin" / "archify.mjs").exists()


def version() -> str | None:
    try:
        return str(json.loads((skill_dir() / "skill-release.json").read_text())["version"])
    except (OSError, ValueError, KeyError, TypeError):
        return None


def version_tuple(text: str | None) -> tuple[int, ...]:
    """Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0)."""
    return tuple(int(n) for n in re.match(r"(\d+(?:\.\d+)*)", text or "").group(1).split(".")) if re.match(r"\d", text or "") else ()


def node_version(root: Path) -> int | None:
    """Major version of the `node` on PATH, or None when absent or unparseable."""
    if not shutil.which("node"):
        return None
    out = p.run_cmd(root, ["node", "--version"])
    match = re.match(r"v?(\d+)", out.stdout.strip())
    return int(match.group(1)) if out.returncode == 0 and match else None


def tooling(root: Path) -> str | None:
    """Why Archify cannot run here, or None when it can."""
    conf = cfg(root)
    major = node_version(root)
    if major is None or major < conf["min_node"]:
        found = "not found" if major is None else f"v{major}"
        return f"node >= {conf['min_node']} required for Archify stage documents (node {found}); install Node, then `{' '.join(INSTALL)}`"
    if not installed():
        return f"Archify skill missing at {skill_dir()}; install it with `{' '.join(INSTALL)}` (or `sdlc knowledge bootstrap`)"
    return None


# --- the `archify` bootstrap step, called from knowledge.STEPS ---


class Present(str):
    """A truthy present-check result that carries the detail to report (the installed version)."""


def archify_present(root: Path, conf: dict) -> Present | bool:
    """Present when the skill is installed (no subprocess); StepSkipped when docs are off or Node is unusable."""
    from .knowledge import StepSkipped

    if not enabled(root):
        raise StepSkipped("docs disabled")
    if installed():
        return Present(f"Archify skill {version() or 'unknown'}")
    if (why := tooling(root)) and why.startswith("node"):
        raise StepSkipped(why)
    return False


def install_archify(root: Path, conf: dict) -> str:
    from .knowledge import ran

    ran(root, INSTALL, installed)
    return f"Archify skill {version() or 'unknown'}"


# --- documents ---


def stage_of(stage: str | None) -> str:
    if stage not in SOURCES:
        fail(f"unknown stage {stage!r}; one of {', '.join(SOURCES)}")
    return stage


def target(root: Path, stage: str | None, slug: str | None) -> Path | None:
    """The feature the document belongs to; maintain documents belong to the project, not a feature."""
    return None if stage_of(stage) == "maintain" else p.feature(root, slug)


def docs_dir(root: Path, feature: Path | None) -> Path:
    return (feature if feature is not None else p.home(root)) / cfg(root)["dir"]


def sources(root: Path, feature: Path | None, stage: str) -> list[Path]:
    base = root if feature is None else feature
    return [base / name for name in SOURCES[stage]]


def rel(root: Path, path: Path) -> str:
    return str(path.relative_to(root))


def digests(root: Path, paths: list[Path]) -> tuple[list[dict], str]:
    """Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in order; a missing source hashes as empty."""
    whole = hashlib.sha256()
    entries = []
    for path in paths:
        data = path.read_bytes() if path.exists() else b""
        entries.append({"resource": rel(root, path), "digest": hashlib.sha256(data).hexdigest()})
        whole.update(f"{rel(root, path)}\n".encode())
        whole.update(data)
    return entries, whole.hexdigest()


def receipt_of(output: str) -> dict | None:
    """The JSON object `deliver --json` prints (pretty-printed over many lines, after any progress text)."""
    for start in [m.start() for m in re.finditer(r"^\{", output, re.MULTILINE)]:
        try:
            found = json.loads(output[start:])
        except ValueError:
            continue
        if isinstance(found, dict):
            return found
    return None


def validation(receipt: dict, quality: str) -> str:
    """One line from the receipt's `validation` block: `9/9 showcase, 0 errors, 0 warnings`."""
    v = receipt.get("validation") or {}
    return f"{v.get('checksPassed', '?')}/{v.get('checkCount', '?')} {v.get('compositionProfile', quality)}, {v.get('errors', '?')} errors, {v.get('warnings', '?')} warnings"


@when_enabled
def render(root: Path, feature: Path | None, stage: str) -> dict:
    conf = cfg(root)
    kind = conf["types"][stage]
    folder = docs_dir(root, feature)
    spec, html, receipt_path = folder / f"{stage}.json", folder / f"{stage}.html", folder / f"{stage}.receipt.json"
    srcs = sources(root, feature, stage)
    if not spec.exists():
        fail(f"stage document source missing; author {rel(root, spec)} from {', '.join(rel(root, s) for s in srcs)} (Archify {kind}), then rerun `sdlc docs render {stage}`")
    if why := tooling(root):
        fail(why)
    argv = ["node", str(skill_dir() / "bin" / "archify.mjs"), "deliver", kind, str(spec), str(html), "--quality", conf["quality"], "--json"]
    out = p.run_cmd(root, argv, NO_NETWORK)
    receipt = receipt_of(out.stdout) if out.returncode == 0 else None
    if out.returncode != 0 or receipt is None:
        tail = (out.stderr.strip() or out.stdout.strip())[-400:]
        fail(f"archify deliver exited {out.returncode}: {tail or 'no receipt printed'}", argv=argv)
    entries, whole = digests(root, srcs)
    record = {
        "stage": stage,
        "type": kind,
        "sources": entries,
        "source_digest": whole,
        "specification_sha256": (receipt.get("specification") or {}).get("sha256"),
        "artifact_sha256": (receipt.get("artifact") or {}).get("sha256"),
        "validation": validation(receipt, conf["quality"]),
        "archify_version": version(),
        "delivered_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    p.write_json(receipt_path, record)
    return {"ok": True, "html": str(html), "receipt": str(receipt_path), "validation": record["validation"]}


@when_enabled
def check(root: Path, feature: Path | None, stage: str) -> dict:
    """The stage document exists and was delivered from the sources as they are now."""
    folder = docs_dir(root, feature)
    html, receipt_path = folder / f"{stage}.html", folder / f"{stage}.receipt.json"
    entries, whole = digests(root, sources(root, feature, stage))
    if not html.exists() or not receipt_path.exists():
        fail(f"stage document missing; author {stage}.json in {rel(root, folder)}, then `sdlc docs render {stage}`", html=str(html), source_digest=whole)
    receipt = p.read_json(receipt_path, {}) or {}
    if receipt.get("source_digest") != whole:
        before = {e["resource"]: e["digest"] for e in receipt.get("sources", [])}
        changed = [e["resource"] for e in entries if before.get(e["resource"]) != e["digest"]] or [e["resource"] for e in entries]
        fail(f"stage document is stale: {', '.join(changed)} changed since {stage}.html was delivered; rerun `sdlc docs render {stage}`", html=str(html), changed=changed, source_digest=whole)
    return {"ok": True, "html": str(html), "fresh": True, "validation": receipt.get("validation"), "source_digest": whole}


require = check  # the gate stages call; the skipped verdict when docs are off


@when_enabled
def open(root: Path, feature: Path | None, stage: str) -> dict:
    """Show the acceptor the delivered document; an opener failure is reported, never a blocked verdict."""
    verdict = check(root, feature, stage)
    html = verdict["html"]
    if os.environ.get("CI"):
        return {**verdict, "opened": False, "reason": "CI set"}
    if not cfg(root)["open"]:
        return {**verdict, "opened": False, "reason": "[docs] open = false"}
    if why := tooling(root):
        return {**verdict, "opened": False, "reason": why}
    try:
        out = p.run_cmd(root, ["node", str(skill_dir() / "bin" / "open-artifact.mjs"), html], NO_NETWORK, timeout=10)
    except OSError as err:
        return {**verdict, "opened": False, "reason": str(err)}
    if out is None or out.returncode != 0:
        return {**verdict, "opened": False, "reason": "opener timed out" if out is None else (out.stderr.strip() or f"open-artifact.mjs exited {out.returncode}")[-200:]}
    return {**verdict, "opened": True}


def documents(root: Path, feature: Path) -> list[str]:
    """PR-body bullets: one per delivered stage document, with its receipt's validation line."""
    folder = feature / cfg(root)["dir"]
    bullets = []
    for html in sorted(folder.glob("*.html")) if folder.is_dir() else []:
        receipt = p.read_json(html.with_suffix(".receipt.json"), {}) or {}
        bullets.append(f"- {html.stem}: {rel(root, html)} ({receipt.get('validation', 'no receipt')})")
    return bullets or ["- none"]
