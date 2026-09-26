import json
import subprocess
from pathlib import Path

from conftest import SOURCES, commit_files, load, regraph


def test_build_new_gated_on_accepted_spec(run, accepted_intent):
    assert run("build", "new")["ok"] is False


def test_build_new_then_accept(run, repo: Path, accepted_plan):
    assert "Status: accepted" in (repo / "sdlc/feat/plan.md").read_text()


def test_build_red_records_failing_run_and_rejects_passing(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    out = run("build", "red", "step1")
    assert out["ok"] and out["phase"] == "red"
    toml_config(commands={"test": "exit 0"})
    out = run("build", "red", "step1")
    assert out["ok"] is False and "passed" in out["reason"]
    log = [json.loads(line) for line in (repo / "sdlc/feat/tdd.jsonl").read_text().splitlines()]
    assert [e["phase"] for e in log] == ["red"]


def test_build_green_requires_prior_red_and_passing_tests(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 0"})
    assert run("build", "green", "step1")["ok"] is False  # no red first
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "step1")
    assert run("build", "green", "step1")["ok"] is False  # still failing
    toml_config(commands={"test": "exit 0"})
    out = run("build", "green", "step1")
    assert out["ok"] and out["cycles"] == 1


def test_build_sync_flags_unplanned_files(run, repo: Path, accepted_plan):
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x")
    (repo / "rogue.py").write_text("x")
    out = run("build", "sync")
    assert out["ok"] is False
    assert out["unplanned"] == ["rogue.py"]
    (repo / "rogue.py").unlink()
    assert run("build", "sync")["ok"] is True


def test_build_sync_ignores_sdlc_artifacts_and_config(run, repo: Path, accepted_plan):
    assert run("build", "sync")["ok"] is True


def test_build_sync_keeps_unstaged_first_line_path_intact(run, repo: Path, accepted_plan):
    """` M path` is the first porcelain line; stripping its leading space mangled the path."""
    (repo / "README.md").write_text("changed\n")
    out = run("build", "sync")
    assert out["ok"] is False
    assert out["unplanned"] == ["README.md"]


def test_build_fix_toggles_lock(run, repo: Path, accepted_plan):
    assert run("build", "fix", "on")["ok"]
    assert (repo / "sdlc/feat/.fix-lock").exists()
    assert run("build", "fix", "off")["ok"]
    assert not (repo / "sdlc/feat/.fix-lock").exists()


def test_test_run_gated_on_accepted_plan(run, accepted_spec):
    assert run("test", "run")["ok"] is False


def test_test_run_requires_tdd_cycle(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 0"})
    out = run("test", "run")
    assert out["ok"] is False and "red" in out["reason"]


def test_test_run_writes_report(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "s")
    toml_config(commands={"test": "echo ok", "lint": "echo lint"})
    run("build", "green", "s")
    out = run("test", "run")
    assert out["ok"] is True
    report = load(repo / "sdlc/feat/test-report.json")
    assert report["passed"] is True
    assert [r["name"] for r in report["results"]] == ["test", "lint"]
    assert report["results"][0]["tail"].strip() == "ok"


def test_test_run_failure_reported_not_hidden(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "s")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "s")
    toml_config(commands={"test": "echo boom; exit 3"})
    out = run("test", "run")
    assert out["ok"] is False and out["failed"] == ["test"]


def test_test_review_validates_findings_file(run, repo: Path, accepted_plan):
    assert run("test", "review")["ok"] is False
    (repo / "sdlc/feat/review.md").write_text("# Review\n\n## Bugs\n- none\n\n## Security\n- Important: PII in log (src/feat.py:3)\n\n## Compliance\n- Nit: name\n")
    out = run("test", "review")
    assert out["ok"] is True
    assert out["important"] == 1 and out["nits"] == 1
    assert out["next"] == "/sdlc:deploy"


def test_run_adds_knowledge_result_and_process_verified(run, repo: Path, knowledge, accepted_plan, toml_config):
    from sdlc import knowledge as k

    toml_config(commands={"test": "exit 1"})
    run("build", "red", "s1")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "s1")
    out = run("test", "run")
    assert out["ok"], out
    assert [r["name"] for r in out["results"]] == ["test", "knowledge"]
    assert out["results"][-1]["exit"] == 0 and "conformance" in out["results"][-1]["tail"]
    front, _ = k.split_document((repo / "sdlc/knowledge/features/feat.md").read_text())
    assert any(v["by"] == "process:sdlc-test" for v in front["verified"])
    assert front["status"] == "stable"  # accepted by a human earlier in the fixture


REVIEW = "# Review\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- none\n"


def branch_with_change(run, repo: Path, **changes: str) -> None:
    """Sources on main, a feat branch committing `changes`, graph.json fresh at HEAD and review.md written."""
    with (repo / ".git/info/exclude").open("a") as exclude:
        exclude.write("graphify-out/\n")  # graph output stays untracked, so the branch diff is only the change
    commit_files(repo, **SOURCES)
    subprocess.run(["git", "checkout", "-qb", "feat"], cwd=repo, check=True)
    commit_files(repo, **changes)
    assert run("knowledge", "bootstrap")["ok"]
    commit_files(repo, "bootstrap output")
    (repo / "sdlc/feat/review.md").write_text(REVIEW)


def test_review_accepts_a_covering_pack(run, repo: Path, accepted_plan, packs):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    refused = run("test", "review")
    assert not refused["ok"] and "sdlc knowledge pack test" in refused["reason"]
    assert run("knowledge", "pack", "test")["ok"]
    review = run("test", "review")
    assert review["ok"] and review["pack"]["path"].endswith(".xml")


def test_review_refused_when_a_changed_file_is_missing_from_the_pack(run, repo: Path, accepted_plan, packs, toml_config):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    assert run("knowledge", "pack", "test")["ok"]
    first = subprocess.run(["git", "rev-list", "--max-parents=0", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    toml_config(knowledge={"pack_base": first})  # a wider base after the pack: README.md and the sources are now changes too
    refused = run("test", "review")
    assert not refused["ok"] and "src/app/util.py" in refused["missing"]


def test_review_accounts_for_excluded_changes(run, repo: Path, accepted_plan, packs):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    (repo / "link.py").symlink_to("src/web/api.py")  # a changed symlink: excluded from the pack, recorded in its manifest
    regraph(repo)
    built = run("knowledge", "pack", "test")
    assert built["ok"] and {"path": "link.py", "rule": "symlink"} in built["excluded"]
    review = run("test", "review")
    assert review["ok"] and review["pack"]["excluded"] == [{"path": "link.py", "rule": "symlink"}]


def test_review_covers_renames_and_lock_files(run, repo: Path, accepted_plan, packs):
    branch_with_change(run, repo, **{"uv.lock": "version = 2\n"})
    subprocess.run(["git", "mv", "src/app/util.py", "src/app/helpers.py"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "rename"], cwd=repo, check=True)
    regraph(repo)
    built = run("knowledge", "pack", "test")
    assert built["ok"] and {"src/app/helpers.py", "uv.lock"} <= set(built["files"]), built
    assert run("test", "review")["ok"]


def test_review_refused_for_a_secret_excluded_change(run, repo: Path, accepted_plan, packs):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n", "deploy.pem": "k\n"})
    assert run("knowledge", "pack", "test")["ok"]
    refused = run("test", "review")
    assert not refused["ok"] and refused["secrets"] == [{"path": "deploy.pem", "rule": "*.pem"}]


def test_review_skips_deleted_binary_and_sdlc_owned_changes(run, repo: Path, accepted_plan, packs):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n", "sdlc__feat__notes.md": "n\n", "CLAUDE.md": "c\n"})
    (repo / "logo.png").write_bytes(b"\x89PNG\x00\x01\x02")
    subprocess.run(["git", "rm", "-q", "src/app/util.py"], cwd=repo, check=True)
    subprocess.run(["git", "add", "logo.png"], cwd=repo, check=True)
    regraph(repo)
    built = run("knowledge", "pack", "test")
    assert built["ok"], built
    review = run("test", "review")
    assert review["ok"], review


def test_review_gate_skipped_visibly_when_off(run, repo: Path, accepted_plan, packs, monkeypatch):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    monkeypatch.setenv("SDLC_PACKS", "off")
    review = run("test", "review")
    assert review["ok"] and review["pack"] == {"ok": True, "skipped": "packs disabled (SDLC_PACKS=off)"}


def test_review_refuses_a_change_excluded_only_by_uncommitted_state(run, repo: Path, accepted_plan, packs, tmp_path_factory):
    import shutil

    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    elsewhere = tmp_path_factory.mktemp("elsewhere") / "web"  # outside the repository
    shutil.move(repo / "src/web", elsewhere)  # uncommitted: the directory swapped for a symlink out of the repo
    (repo / "src/web").symlink_to(elsewhere)
    built = run("knowledge", "pack", "test")
    assert built["ok"] and {"path": "src/web/api.py", "rule": "outside root"} in built["excluded"], built
    refused = run("test", "review")
    assert not refused["ok"] and refused["missing"] == ["src/web/api.py"]
