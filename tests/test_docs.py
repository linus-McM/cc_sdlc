"""Archify stage documents: [docs] config, render/check/open mechanics and the accept gates."""

import json
from pathlib import Path

from conftest import fill, load, sha256
from sdlc import artifacts, project

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


def test_render_delivers_html_and_receipt(run, repo: Path, accepted_intent, docs_tools):
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


def test_render_failures_are_verbatim(run, repo: Path, accepted_intent, docs_tools):
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


def test_check_reports_fresh_missing_and_stale(run, repo: Path, accepted_intent, docs_tools):
    slug = accepted_intent
    out = run("docs", "check", "plan")
    assert not out["ok"] and out["reason"].startswith("stage document missing; author plan.json")
    assert "sdlc docs render plan" in out["reason"] and len(out["source_digest"]) == 64  # the card quotes it before delivery
    source(repo, slug, "plan")
    assert run("docs", "render", "plan")["ok"]
    out = run("docs", "check", "plan")
    assert out["ok"] and out["fresh"] is True and out["html"].endswith("docs/plan.html")
    assert out["source_digest"] == load(repo / "sdlc" / slug / "docs/plan.receipt.json")["source_digest"]
    intent = repo / "sdlc" / slug / "intent.md"
    intent.write_text(intent.read_text() + "\nmore\n")
    out = run("docs", "check", "plan")
    assert not out["ok"] and out["reason"].startswith(f"stage document is stale: sdlc/{slug}/intent.md changed since plan.html was delivered")
    assert "sdlc docs render plan" in out["reason"]
    out = run("docs", "check", "nope")
    assert not out["ok"] and out["reason"].startswith("unknown stage 'nope'")


def test_accept_requires_fresh_document_per_stage(run, repo: Path, docs_tools):
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **{"Problem": "p", "Proposed outcome": "o", "Affected users and systems": "u", "Constraints": "c", "Open questions": "none"})
    out = run("plan", "accept")
    assert not out["ok"] and out["reason"].startswith("stage document missing; author plan.json")
    assert artifacts.status((repo / "sdlc/feat/intent.md").read_text()) == "draft"
    source(repo, "feat", "plan")
    assert run("docs", "render", "plan")["ok"]
    assert run("plan", "accept")["ok"]
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", Requirements="r", Design="d", Concerns="none", **{"Open questions": "none", "Proof": "t"})
    source(repo, "feat", "design")
    assert run("docs", "render", "design")["ok"]
    (repo / "sdlc/feat/spec.md").write_text((repo / "sdlc/feat/spec.md").read_text() + "\nlater edit\n")
    out = run("design", "accept")
    assert not out["ok"] and out["reason"].startswith("stage document is stale: sdlc/feat/spec.md")
    assert run("docs", "render", "design")["ok"] and run("design", "accept")["ok"]
    run("build", "new")
    fill(repo / "sdlc/feat/plan.md", **{"Files that change": "- a.py", "Order of work": "1. t", "Risks": "none", "Proof": "p"})
    assert not run("build", "accept")["ok"]
    source(repo, "feat", "build")
    assert run("docs", "render", "build")["ok"] and run("build", "accept")["ok"]


def test_review_and_record_require_documents(run, repo: Path, docs_tools, toml_config, monkeypatch):
    monkeypatch.setenv("SDLC_DOCS", "off")  # walk the earlier stages with docs off, then turn them on
    run("plan", "new", "Feat")
    fill(repo / "sdlc/feat/intent.md", **{"Problem": "p", "Proposed outcome": "o", "Affected users and systems": "u", "Constraints": "c", "Open questions": "none"})
    assert run("plan", "accept")["ok"]
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", Requirements="r", Design="d", Concerns="none", **{"Open questions": "none", "Proof": "t"})
    assert run("design", "accept")["ok"]
    run("build", "new")
    fill(repo / "sdlc/feat/plan.md", **{"Files that change": "- a.py", "Order of work": "1. t", "Risks": "none", "Proof": "p"})
    assert run("build", "accept")["ok"]
    toml_config(commands={"test": "exit 1"}, deploy={"rollback": "echo rolled-back"})
    run("build", "red", "s")
    toml_config(commands={"test": "exit 0"}, deploy={"rollback": "echo rolled-back"})
    run("build", "green", "s")
    assert run("test", "run")["ok"]
    (repo / "sdlc/feat/review.md").write_text("# R\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- none\n")
    monkeypatch.delenv("SDLC_DOCS")
    out = run("test", "review")
    assert not out["ok"] and out["reason"].startswith("stage document missing; author test.json")
    source(repo, "feat", "test")
    assert run("docs", "render", "test")["ok"]
    receipt = load(repo / "sdlc/feat/docs/test.receipt.json")
    assert [s["resource"] for s in receipt["sources"]] == ["sdlc/feat/review.md", "sdlc/feat/test-report.json"]
    assert run("test", "review")["ok"]
    assert run("deploy", "pr")["ok"]
    out = run("deploy", "record", "dev")
    assert not out["ok"] and out["reason"].startswith("stage document missing; author deploy.json")
    assert not (repo / "sdlc/feat/deploy.json").exists()
    source(repo, "feat", "deploy")
    assert run("docs", "render", "deploy")["ok"]
    assert load(repo / "sdlc/feat/docs/deploy.receipt.json")["sources"][0]["resource"] == "sdlc/feat/pr-body.md"
    assert run("deploy", "record", "dev")["ok"]


def test_open_calls_opener_unless_ci_or_disabled(run, repo: Path, accepted_intent, docs_tools, toml_config, monkeypatch):
    source(repo, "feat", "plan")
    assert run("docs", "render", "plan")["ok"]
    out = run("docs", "open", "plan")
    html = str(repo / "sdlc/feat/docs/plan.html")
    assert out["ok"] and out["opened"] is True and out["html"] == html
    assert docs_tools.calls()[-1].startswith(f"node open-artifact.mjs {html}")
    monkeypatch.setenv("CI", "1")
    calls = len(docs_tools.calls())
    out = run("docs", "open", "plan")
    assert out["ok"] and out["opened"] is False and out["reason"] == "CI set"
    assert len(docs_tools.calls()) == calls  # no opener under CI
    monkeypatch.delenv("CI")
    toml_config(docs={"open": False})
    out = run("docs", "open", "plan")
    assert out["ok"] and out["opened"] is False and out["reason"] == "[docs] open = false"
    toml_config(docs={"open": True})
    docs_tools.uninstall("node")
    out = run("docs", "open", "plan")
    assert out["ok"] and out["opened"] is False and "node" in out["reason"]
    assert not run("docs", "open", "design")["ok"]  # nothing delivered yet: the acceptor gets the check reason


def test_pr_body_lists_documents(run, repo: Path, accepted_plan, docs_tools):
    from sdlc import deploy

    feature = repo / "sdlc/feat"
    body = deploy.pr_body(repo, feature)
    text = (feature / "pr-body.md").read_text()
    assert body["ok"] and "### Documents\n- none" in text
    source(repo, "feat", "plan")
    assert run("docs", "render", "plan")["ok"]
    deploy.pr_body(repo, feature)
    text = (feature / "pr-body.md").read_text()
    assert "### Documents\n- plan: sdlc/feat/docs/plan.html (9/9 showcase, 0 errors, 0 warnings)" in text


def test_maintain_document_is_ungated_and_reported(run, repo: Path, docs_tools, monkeypatch):
    (repo / "sdlc").mkdir(exist_ok=True)
    (repo / "sdlc/bands.toml").write_text('[metrics.m]\nbad = "high"\n')
    for v in (1.0, 1.0, 1.0):
        run("maintain", "ingest", "m", "--value", v)
    out = run("maintain", "watch")
    assert out["ok"] and out["docs"].startswith("stage document missing; author maintain.json in sdlc/docs")
    src = repo / "sdlc/docs/maintain.json"
    src.parent.mkdir(parents=True)
    src.write_text(json.dumps({"schema_version": 1, "meta": {"title": "bands", "quality_profile": "showcase"}}) + "\n")
    out = run("docs", "render", "maintain")
    assert out["ok"] and out["html"] == str(repo / "sdlc/docs/maintain.html")
    receipt = load(repo / "sdlc/docs/maintain.receipt.json")
    assert receipt["type"] == "lifecycle" and receipt["sources"][0]["resource"] == "sdlc/bands.toml"
    assert "docs" not in run("maintain", "watch")
    (repo / "sdlc/bands.toml").write_text('[metrics.m]\nbad = "low"\n')
    out = run("maintain", "watch")
    assert out["ok"] and out["docs"].startswith("stage document is stale: sdlc/bands.toml changed")
    monkeypatch.setenv("SDLC_DOCS", "off")
    assert "docs" not in run("maintain", "watch")


def test_stage_commands_carry_the_docs_step():
    root = Path(__file__).resolve().parents[1]
    types = project.DEFAULTS["docs"]["types"]
    for stage in ("plan", "design", "build", "test", "deploy", "maintain"):
        text = (root / "commands" / f"{stage}.md").read_text()
        assert f"sdlc docs render {stage}" in text, stage
        assert f"Archify `{types[stage]}`" in text, stage
        assert "Generated by sdlc from" in text and "quality_profile" in text, stage
        if stage != "maintain":
            assert f"sdlc docs open {stage}" in text, stage
    readme = (root / "README.md").read_text()
    assert "[docs]" in readme and "SDLC_DOCS=off" in readme and "npx -y skills add tt-a1i/archify" in readme
    assert "docs.py" in (root / "CLAUDE.md").read_text()
