"""Stage documents: one Archify HTML diagram per stage, delivered from a Claude-authored JSON source.
Public mechanics: render, check, open (plus the `archify` bootstrap step used by knowledge.STEPS).
Every one is a no-op verdict when the layer is off (`[docs] enabled = false` or SDLC_DOCS=off), so the
stages that gate on `check` pass through untouched. Node and Archify are subprocesses; nothing here
imports them or calls an LLM.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
from pathlib import Path

from . import project as p
from .project import Blocked, StepSkipped, fail, ran

SKIPPED = {"ok": True, "skipped": "docs disabled"}
INSTALL = ["npx", "-y", "skills", "add", "tt-a1i/archify", "--skill", "archify", "--agent", "claude-code", "--global", "--copy", "--yes"]
INSTALL_CMD = " ".join(INSTALL)
NO_NETWORK = {"ARCHIFY_UPDATE_CHECK_DISABLED": "1"}
# stage -> the files the document describes, relative to the owner directory (the feature; `sdlc/` for maintain)
SOURCES = {
    "plan": ["intent.md"],
    "design": ["spec.md"],
    "build": ["plan.md"],
    "test": ["review.md", "test-report.json"],
    "deploy": ["pr-body.md"],
    "maintain": ["bands.toml"],
}


DIR_OK = re.compile(r"^[A-Za-z0-9._][A-Za-z0-9._/-]*$")


def cfg(root: Path) -> dict:
    """The [docs] table; `dir` is validated here because it becomes a path under the feature directory."""
    conf = p.config(root)["docs"]
    folder = str(conf["dir"])
    if not DIR_OK.match(folder) or ".." in Path(folder).parts or folder.endswith("/"):
        fail(f"[docs] dir {folder!r} must be a relative path made of letters, digits, `.`, `_`, `-` and `/`, without `..`")
    return conf


def enabled(root: Path) -> bool:
    return os.environ.get("SDLC_DOCS") != "off" and bool(cfg(root)["enabled"])


when_enabled = p.when_enabled(enabled, SKIPPED)


# --- the installed skill and Node ---


def skill_dir() -> Path:
    return p.claude_dir() / "skills" / "archify"


def installed() -> bool:
    return (skill_dir() / "bin" / "archify.mjs").exists()


def version() -> str | None:
    try:
        found = p.read_json(skill_dir() / "skill-release.json", {})
    except Blocked:
        return None
    return str(found["version"]) if isinstance(found, dict) and found.get("version") else None


def version_tuple(text: str | None) -> tuple[int, ...]:
    """Leading dotted integers of a version string; `2.17.0-dev.1` -> (2, 17, 0)."""
    match = re.match(r"\d+(?:\.\d+)*", text or "")
    return tuple(int(n) for n in match.group().split(".")) if match else ()


def node_version(root: Path) -> int | None:
    """Major version of the `node` on PATH, or None when absent or unparseable."""
    if not shutil.which("node"):
        return None
    out = p.run_cmd(root, ["node", "--version"])
    match = re.match(r"v?(\d+)", out.stdout.strip())
    return int(match.group(1)) if out.returncode == 0 and match else None


def node_problem(root: Path) -> str | None:
    """Why Node cannot run Archify here, or None."""
    least, major = cfg(root)["min_node"], node_version(root)
    if major is not None and major >= least:
        return None
    found = "not found" if major is None else f"v{major}"
    return f"node >= {least} required for Archify stage documents (node {found}); install Node, then `{INSTALL_CMD}`"


def tooling(root: Path) -> str | None:
    """Why Archify cannot run here, or None when it can."""
    if why := node_problem(root):
        return why
    return None if installed() else f"Archify skill missing at {skill_dir()}; install it with `{INSTALL_CMD}` (or `sdlc knowledge bootstrap`)"


# --- the `archify` bootstrap step, called from knowledge.STEPS ---


def archify_present(root: Path, conf: dict) -> str | bool:
    """The installed version as the step's detail (no subprocess); StepSkipped when docs are off or Node is unusable."""
    if not enabled(root):
        raise StepSkipped("docs disabled")
    if installed():
        return f"Archify skill {version() or 'unknown'}"
    if why := node_problem(root):
        raise StepSkipped(why)
    return False


def install_archify(root: Path, conf: dict) -> str:
    """Third-party npm code runs only when the project opted in ([knowledge] auto_install); otherwise the command is reported."""
    if not conf["auto_install"]:
        raise StepSkipped(f"Archify skill missing; install it with `{INSTALL_CMD}`, or set [knowledge] auto_install = true and rerun `sdlc knowledge bootstrap`")
    ran(root, INSTALL, installed)
    return f"Archify skill {version() or 'unknown'}"


# --- documents ---


def mechanic(action: str):
    """CLI handler for `docs <action> <stage>`: the skipped verdict comes before any feature lookup or stage validation."""

    def handler(root: Path, feature, stage: str | None, ns) -> dict:
        if not enabled(root):
            return SKIPPED
        return globals()[action](root, target(root, stage, ns.slug), stage)

    return handler


def target(root: Path, stage: str | None, slug: str | None) -> Path:
    """The directory that owns the stage document: the feature, or `sdlc/` for the project-wide maintain document."""
    if stage not in SOURCES:
        fail(f"unknown stage {stage!r}; one of {', '.join(SOURCES)}")
    return p.home(root) if stage == "maintain" else p.feature(root, slug)


def docs_dir(root: Path, owner: Path) -> Path:
    return owner / cfg(root)["dir"]


def sources(owner: Path, stage: str) -> list[Path]:
    return [owner / name for name in SOURCES[stage]]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


STATUS_LINE = re.compile(rb"\bStatus:\s*[A-Za-z-]+")


def source_bytes(path: Path) -> bytes:
    """The bytes a document describes: a missing source is empty, and an artifact's `Status:` field (the one thing
    `accept` rewrites after the document was delivered) is masked so accepting never makes its own document stale."""
    data = path.read_bytes() if path.exists() else b""
    return STATUS_LINE.sub(b"Status: -", data, count=1) if path.suffix == ".md" else data


def digests(root: Path, paths: list[Path]) -> tuple[list[dict], str]:
    """Per-source sha256 plus one digest over `<path>\n<bytes>` for every source, in order."""
    whole = hashlib.sha256()
    entries = []
    for path in paths:
        data = source_bytes(path)
        entries.append({"resource": p.rel(root, path), "digest": sha256(data)})
        whole.update(f"{p.rel(root, path)}\n".encode())
        whole.update(data)
    return entries, whole.hexdigest()


def receipt_of(output: str) -> dict | None:
    """The JSON object `deliver --json` prints (pretty-printed over many lines, after any progress text)."""
    for match in re.finditer(r"^\{", output, re.MULTILINE):
        try:
            found = json.loads(output[match.start() :])
        except ValueError:
            continue
        if isinstance(found, dict):
            return found
    return None


def validation(receipt: dict, quality: str) -> str:
    """One line from the receipt's `validation` block, `9/9 showcase, 0 errors, 0 warnings`; only integers are copied
    from the tool's output (the line lands in pr-body.md and the feature concept), the profile is the one we asked for."""
    v = receipt.get("validation") if isinstance(receipt.get("validation"), dict) else {}

    def count(key: str) -> str:
        value = v.get(key)
        return str(value) if isinstance(value, int) and not isinstance(value, bool) else "?"

    return f"{count('checksPassed')}/{count('checkCount')} {quality}, {count('errors')} errors, {count('warnings')} warnings"


@when_enabled
def render(root: Path, owner: Path, stage: str) -> dict:
    conf = cfg(root)
    kind, folder = conf["types"][stage], owner / conf["dir"]
    spec, html, receipt_path = folder / f"{stage}.json", folder / f"{stage}.html", folder / f"{stage}.receipt.json"
    srcs = sources(owner, stage)
    if not spec.exists():
        fail(f"stage document source missing; author {p.rel(root, spec)} from {', '.join(p.rel(root, s) for s in srcs)} (Archify {kind}), then rerun `sdlc docs render {stage}`")
    if why := tooling(root):
        fail(why)
    argv = ["node", str(skill_dir() / "bin" / "archify.mjs"), "deliver", kind, str(spec), str(html), "--quality", conf["quality"], "--json"]
    out = p.run_cmd(root, argv, NO_NETWORK)
    receipt = receipt_of(out.stdout) if out.returncode == 0 else None
    if receipt is None:
        tail = (out.stderr.strip() or out.stdout.strip())[-400:]
        what = f"exited {out.returncode}" if out.returncode else "printed no receipt (exit 0)"
        fail(f"archify deliver {what}: {tail or 'no output'}", argv=argv)
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
        "delivered_at": p.now_iso(),
    }
    p.write_json(receipt_path, record)
    return {"ok": True, "html": str(html), "receipt": str(receipt_path), "validation": record["validation"]}


@when_enabled
def check(root: Path, owner: Path, stage: str) -> dict:
    """The stage document exists and was delivered from the sources as they are now (`artifact_matches` says whether the
    HTML is still the bytes Archify delivered).
    The gates (accept, test review, deploy record) call this; with docs off they get the skipped verdict instead."""
    folder = docs_dir(root, owner)
    html, receipt_path = folder / f"{stage}.html", folder / f"{stage}.receipt.json"
    entries, whole = digests(root, sources(owner, stage))
    if not html.exists() or not receipt_path.exists():
        fail(f"stage document missing; author {stage}.json in {p.rel(root, folder)}, then `sdlc docs render {stage}`", html=str(html), source_digest=whole)
    receipt = p.read_json(receipt_path, {}) or {}
    if receipt.get("source_digest") != whole:
        before = {e["resource"]: e["digest"] for e in receipt.get("sources", [])}
        changed = [e["resource"] for e in entries if before.get(e["resource"]) != e["digest"]] or [e["resource"] for e in entries]
        fail(f"stage document is stale: {', '.join(changed)} changed since {stage}.html was delivered; rerun `sdlc docs render {stage}`", html=str(html), changed=changed, source_digest=whole)
    matches = receipt.get("artifact_sha256") == sha256(html.read_bytes())  # evidence for the acceptor; a formatter or checkout may rewrite HTML, so never a block
    return {"ok": True, "html": str(html), "fresh": True, "artifact_matches": matches, "validation": receipt.get("validation"), "source_digest": whole}


@when_enabled
def open(root: Path, owner: Path, stage: str) -> dict:
    """Show the acceptor the delivered document; an opener failure is reported, never a blocked verdict."""
    verdict = check(root, owner, stage)
    why = "CI set" if os.environ.get("CI") else None if cfg(root)["open"] else "[docs] open = false"
    if why is None and not installed():
        why = tooling(root)
    if why is None:
        out = p.run_cmd(root, ["node", str(skill_dir() / "bin" / "open-artifact.mjs"), verdict["html"]], NO_NETWORK, timeout=10)
        why = None if out.returncode == 0 else (out.stderr.strip() or f"open-artifact.mjs exited {out.returncode}")[-200:]
    return {**verdict, "opened": why is None, **({"reason": why} if why else {})}


def documents(root: Path, owner: Path) -> list[str]:
    """One bullet per delivered stage document, with its receipt's validation line; empty when none."""
    folder = docs_dir(root, owner)
    bullets = []
    for html in sorted(folder.glob("*.html")) if folder.is_dir() else []:
        receipt = p.read_json(html.with_suffix(".receipt.json"), {}) or {}
        bullets.append(f"- {html.stem}: {p.rel(root, html)} ({receipt.get('validation', 'no receipt')})")
    return bullets
