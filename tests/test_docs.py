"""Archify stage documents: [docs] config, render/check/open mechanics and the accept gates."""

import json
from pathlib import Path

from conftest import load, sha256
from sdlc import project

DISABLED = {"ok": True, "skipped": "docs disabled", "stage": "docs"}


def test_defaults_and_disabled_verdicts(run, repo: Path, toml_config, monkeypatch):
    conf = project.config(repo)["docs"]
    assert conf["enabled"] is True and conf["dir"] == "docs" and conf["quality"] == "showcase"
    assert conf["open"] is True and conf["min_node"] == 18 and conf["min_version"] == "2.17"
    assert conf["types"] == {
        "plan": "architecture",
        "design": "dataflow",
        "build": "workflow",
        "test": "sequence",
        "deploy": "lifecycle",
        "maintain": "lifecycle",
    }
    run("plan", "new", "Feat")
    for action in ("render", "check", "open"):
        assert run("docs", action, "plan") == DISABLED  # SDLC_DOCS=off from the repo fixture
    monkeypatch.delenv("SDLC_DOCS")
    toml_config(docs={"enabled": False})
    for action in ("render", "check", "open"):
        assert run("docs", action, "plan") == DISABLED


def source(repo: Path, slug: str, stage: str, **extra) -> Path:
    path = repo / "sdlc" / slug / "docs" / f"{stage}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"schema_version": 1, "meta": {"title": stage, "quality_profile": "showcase"}, **extra}) + "\n")
    return path


def test_render_delivers_html_and_receipt(run, repo: Path, docs_tools, accepted_intent):
    slug = accepted_intent
    src = source(repo, slug, "plan")
    out = run("docs", "render", "plan")
    assert out["ok"], out
    html = repo / "sdlc" / slug / "docs/plan.html"
    assert html.exists() and out["html"] == str(html)
    receipt = load(repo / "sdlc" / slug / "docs/plan.receipt.json")
    intent = repo / "sdlc" / slug / "intent.md"
    assert receipt["stage"] == "plan" and receipt["type"] == "architecture"
    assert receipt["sources"] == [{"resource": f"sdlc/{slug}/intent.md", "digest": sha256(intent.read_bytes())}]
    assert receipt["source_digest"] == sha256(f"sdlc/{slug}/intent.md\n".encode(), intent.read_bytes())
    assert receipt["specification_sha256"] == sha256(src.read_bytes())
    assert receipt["artifact_sha256"] == sha256(html.read_bytes())
    assert receipt["validation"] == out["validation"] == "9/9 showcase, 0 errors, 0 warnings"
    assert receipt["archify_version"] == "2.17.0-dev.1" and receipt["delivered_at"]
    call = docs_tools.calls()[-1]
    assert call == f"node archify.mjs deliver architecture {src} {html} --quality showcase --json update_check=1"


def test_render_failures_are_verbatim(run, repo: Path, docs_tools, accepted_intent):
    slug = accepted_intent
    out = run("docs", "render", "plan")
    assert not out["ok"] and out["reason"].startswith("stage document source missing; author ")
    assert f"sdlc/{slug}/docs/plan.json" in out["reason"] and "intent.md" in out["reason"] and "architecture" in out["reason"]
    source(repo, slug, "plan", fail=True)
    out = run("docs", "render", "plan")
    assert not out["ok"] and out["reason"] == "archify deliver exited 1: composition error: node budget"
    assert not (repo / "sdlc" / slug / "docs/plan.receipt.json").exists()
    docs_tools.uninstall("node")
    out = run("docs", "render", "plan")
    assert not out["ok"] and "npx -y skills add tt-a1i/archify" in out["reason"]
