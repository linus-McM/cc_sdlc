import json
import subprocess
from pathlib import Path

from conftest import PLAN_BODY, REVIEW_OK, SOURCES, build_out, commit_files, fill, load, regraph
from sdlc import project as p


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
    run("build", "red", "1")
    toml_config(commands={"test": "echo ok", "lint": "echo lint"})
    run("build", "green", "1")
    build_out(repo)
    out = run("test", "run")
    assert out["ok"] is True
    report = load(repo / "sdlc/feat/test-report.json")
    assert report["passed"] is True
    assert [r["name"] for r in report["results"]] == ["test", "lint"]
    assert report["results"][0]["tail"].strip() == "ok"


def test_test_run_failure_reported_not_hidden(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "1")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "1")
    toml_config(commands={"test": "echo boom; exit 3"})
    build_out(repo)
    out = run("test", "run")
    assert out["ok"] is False and out["failed"] == ["test"]


def test_test_review_validates_findings_file(run, repo: Path, accepted_plan):
    assert run("test", "review")["ok"] is False
    (repo / "sdlc/feat/review.md").write_text("# Review\n\n## Bugs\n- none\n\n## Security\n- Important: PII in log (src/feat.py:3)\n\n## Compliance\n- R1: met, tests/test_feat.py\n- Nit: name\n")
    review = repo / "sdlc/feat/review.md"
    out = run("test", "review")
    assert not out["ok"] and out["reason"].startswith("1 Important finding(s) still open in review.md;")
    assert out["open"] == ["- Important: PII in log (src/feat.py:3)"]
    for unresolved in ("wontfix:", "fixed:", "accepted: Sam Lee, log is internal"):  # a resolution carries its note; nobody signs a finding off by name
        review.write_text(review.read_text().replace("(src/feat.py:3)", f"(src/feat.py:3) {unresolved}"))
        assert not run("test", "review")["ok"], unresolved
        review.write_text(review.read_text().replace(f" {unresolved}", ""))
    review.write_text(review.read_text().replace("(src/feat.py:3)", "(src/feat.py:3) fixed: a1b2c3d"))
    out = run("test", "review")
    assert out["ok"] is True and "open" not in out
    assert out["important"] == 1 and out["nits"] == 1 and out["wontfix"] == 0
    assert out["complete"] is True and out["next"].startswith("complete") and "/sdlc:deploy is optional" in out["next"]  # the loop ends at the test stage
    review.write_text(review.read_text().replace("fixed: a1b2c3d", "wontfix: log is internal only until v2"))
    out = run("test", "review")
    assert out["ok"] and out["wontfix"] == 1


def test_review_needs_a_verdict_on_every_requirement(run, repo: Path, accepted_plan):
    review = repo / "sdlc/feat/review.md"
    review.write_text("# Review\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- none\n")
    out = run("test", "review")
    assert not out["ok"] and out["missing"] == ["R1"] and "R<n>: met" in out["reason"]
    review.write_text(review.read_text().replace("## Compliance\n- none", "## Compliance\n- Important: R1 not delivered, the endpoint is missing (src/feat.py:1)"))
    out = run("test", "review")
    assert not out["ok"] and out["open"] == ["- Important: R1 not delivered, the endpoint is missing (src/feat.py:1)"]  # an unmet requirement is an open finding
    review.write_text(review.read_text().replace("(src/feat.py:1)", "(src/feat.py:1) fixed: a1b2c3d"))
    assert run("test", "review")["ok"]


def test_build_steps_wait_for_the_approved_plan(run, repo: Path, accepted_spec, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "new")
    out = run("build", "red", "1")
    assert not out["ok"] and "plan.md is not accepted" in out["reason"] and "build accept" in out["reason"]
    fill(repo / "sdlc/feat/plan.md", **PLAN_BODY)
    assert run("build", "accept")["ok"]
    assert run("build", "red", "1")["ok"]


def test_build_check_traces_every_requirement_to_a_numbered_step(run, repo: Path, accepted_intent):
    run("design", "new")
    fill(repo / "sdlc/feat/spec.md", Requirements="1. first\n2. second", Design="d", Concerns="none", **{"Open questions": "none", "Proof": "tests/test_feat.py"})
    assert run("design", "accept")["ok"]
    run("build", "new")
    fill(repo / "sdlc/feat/plan.md", **{**PLAN_BODY, "Order of work": "- failing test, then implement"})
    out = run("build", "check")
    assert not out["ok"] and "Order of work must be numbered steps" in out["reason"] and "R1, R2" in out["reason"]
    fill(repo / "sdlc/feat/plan.md", **{"Order of work": "1. failing test, then implement (R1)\n2. tidy up (R3)"})
    out = run("build", "check")
    assert not out["ok"] and "no Order of work step delivers R2" in out["reason"] and "cites R3, which spec.md does not define" in out["reason"]
    fill(repo / "sdlc/feat/plan.md", **{"Order of work": "1. failing test, then implement (R1)\n2. second failing test (R2)"})
    assert run("build", "check")["ok"]


def cycle(run, toml_config, step: str) -> None:
    toml_config(commands={"test": "exit 1"})
    assert run("build", "red", step)["ok"]
    toml_config(commands={"test": "exit 0"})
    assert run("build", "green", step)["ok"]


def test_test_run_needs_a_cycle_for_every_plan_step(run, repo: Path, accepted_spec, toml_config):
    run("build", "new")
    fill(repo / "sdlc/feat/plan.md", **{**PLAN_BODY, "Order of work": "1. failing test (R1)\n2. second failing test (R1)\n3. third (R1)"})
    assert run("build", "accept")["ok"]
    build_out(repo)
    cycle(run, toml_config, "1")
    cycle(run, toml_config, "bugfix")  # a cycle outside the plan counts for no step
    out = run("test", "run")
    assert not out["ok"] and out["missing"] == ["2", "3"] and "build red <n>" in out["reason"]
    cycle(run, toml_config, "step 2: second failing test")
    cycle(run, toml_config, "3")
    assert run("test", "run")["ok"]
    toml_config(commands={"test": "exit 0"}, build={"require_tdd": False})
    (repo / "sdlc/feat/tdd.jsonl").unlink()
    assert run("test", "run")["ok"]  # the switch that drops the cycle rule drops this one too


def test_test_run_refuses_planned_files_the_build_never_changed(run, repo: Path, accepted_plan, toml_config):
    cycle(run, toml_config, "1")
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x\n")
    out = run("test", "run")
    assert not out["ok"] and out["untouched"] == ["tests/test_feat.py"] and "never changed" in out["reason"]
    commit_files(repo, **{"tests__test_feat.py": "def test(): pass\n"})  # committed since the approval counts as changed
    assert run("test", "run")["ok"]


def test_deviations_from_the_approved_plan_are_reported_not_refused(run, repo: Path, accepted_plan, toml_config):
    approved = load(repo / "sdlc/feat/approved.json")
    assert approved["files"] == ["src/feat.py", "tests/test_feat.py"] and approved["steps"] == {"1": "failing test, then implement (R1)"} and len(approved["base"]) == 40
    cycle(run, toml_config, "1")
    build_out(repo)
    assert "deviations" not in run("test", "run")
    fill(repo / "sdlc/feat/plan.md", **{"Files that change": "- src/feat.py (new)\n- src/extra.py (new)", "Order of work": "1. failing test, then implement differently (R1)"})
    (repo / "src/extra.py").write_text("x\n")
    out = run("test", "run")
    assert out["ok"] and out["deviations"] == {"files_added": ["src/extra.py"], "files_removed": ["tests/test_feat.py"], "steps_changed": ["1"]}
    assert load(repo / "sdlc/feat/test-report.json")["deviations"] == out["deviations"]
    commit_files(repo)
    assert run("build", "accept")["ok"]  # approving the changed plan clears them and keeps the first base commit
    assert "deviations" not in run("test", "run") and load(repo / "sdlc/feat/approved.json")["base"] == approved["base"]


def test_run_adds_knowledge_result_and_process_verified(run, repo: Path, knowledge, accepted_plan, toml_config):
    from sdlc import knowledge as k

    toml_config(commands={"test": "exit 1"})
    run("build", "red", "1")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "1")
    build_out(repo)
    out = run("test", "run")
    assert out["ok"], out
    assert [r["name"] for r in out["results"]] == ["test", "knowledge"]
    assert out["results"][-1] == {"name": "knowledge", "exit": 0}  # a passing verdict carries no tails; the report keeps them
    assert "conformance" in load(repo / "sdlc/feat/test-report.json")["results"][-1]["tail"]
    front, _ = k.split_document((repo / "sdlc/knowledge/features/feat.md").read_text())
    assert any(v["by"] == "process:sdlc-test" for v in front["verified"])
    assert front["status"] == "stable"  # accepted by a human earlier in the fixture


REVIEW = "# Review\n\n## Bugs\n- none\n\n## Security\n- none\n\n## Compliance\n- R1: met, tests/test_feat.py\n"


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
    review = run("test", "review")  # no pack yet: the review builds it at HEAD
    assert review["ok"] and review["pack"]["path"].endswith(".xml") and review["pack"]["rebuilt"] is True
    again = run("test", "review")
    assert again["ok"] and "rebuilt" not in again["pack"] and again["pack"]["path"] == review["pack"]["path"]


def test_review_reports_a_changed_file_missing_from_the_pack(run, repo: Path, accepted_plan, packs, toml_config):
    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    assert run("knowledge", "pack", "test")["ok"]
    first = subprocess.run(["git", "rev-list", "--max-parents=0", "HEAD"], cwd=repo, capture_output=True, text=True).stdout.strip()
    toml_config(knowledge={"pack_base": first})  # a wider base after the pack: README.md and the sources are now changes too
    review = run("test", "review")  # a pack that is behind is reported beside the verdict, never a refusal
    assert review["ok"] and not review["pack"]["ok"] and "src/app/util.py" in review["pack"]["missing"]


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


def test_review_reports_a_change_excluded_only_by_uncommitted_state(run, repo: Path, accepted_plan, packs, tmp_path_factory):
    import shutil

    branch_with_change(run, repo, **{"src__web__api.py": "a = 2\n"})
    elsewhere = tmp_path_factory.mktemp("elsewhere") / "web"  # outside the repository
    shutil.move(repo / "src/web", elsewhere)  # uncommitted: the directory swapped for a symlink out of the repo
    (repo / "src/web").symlink_to(elsewhere)
    built = run("knowledge", "pack", "test")
    assert built["ok"] and {"path": "src/web/api.py", "rule": "outside root"} in built["excluded"], built
    review = run("test", "review")
    assert review["ok"] and not review["pack"]["ok"] and review["pack"]["missing"] == ["src/web/api.py"]


def test_red_and_green_run_one_test_when_test_one_is_configured(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "echo full >> runs.log", "test_one": "echo one {selector} >> runs.log; test -f pass"})
    red = run("build", "red", "s", "--only", "tests/test_x.py::test a")
    assert red["ok"] and red["scoped"] is True and "tail" in red
    assert (repo / "runs.log").read_text() == "one tests/test_x.py::test a\n"  # the selector reaches the shell as one quoted word
    (repo / "pass").write_text("")
    green = run("build", "green", "s", "--only", "tests/test_x.py::test a")
    assert green["ok"] and green["scoped"] is True and "tail" not in green  # a passing green carries no output
    assert (repo / "runs.log").read_text().splitlines()[1:] == ["one tests/test_x.py::test a", "full"]  # the one test, then the suite once


def test_scoped_green_still_needs_the_full_suite(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1", "test_one": "test -f pass # {selector}"})
    assert run("build", "red", "s", "--only", "x")["ok"]
    (repo / "pass").write_text("")
    out = run("build", "green", "s", "--only", "x")
    assert not out["ok"] and "full suite fails" in out["reason"]


def test_only_without_test_one_runs_the_full_suite(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    out = run("build", "red", "s", "--only", "tests/test_x.py")
    assert out["ok"] and out["scoped"] is False


def test_green_runs_plan_sync_and_reports_unplanned_files(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "test -f rogue.py"})
    run("build", "red", "1")
    (repo / "rogue.py").write_text("x")
    out = run("build", "green", "1")
    assert out["ok"] and out["cycles"] == 1  # the green is recorded; the sync finding is reported beside it
    assert out["sync"]["ok"] is False and out["sync"]["unplanned"] == ["rogue.py"]
    assert "commit" not in out and "plan.md" in out["next"]


def test_green_commits_the_step_once_sync_passes(checkpoint_on, run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "test -f src/feat.py"})
    run("build", "red", "first step")
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x\n")
    out = run("build", "green", "first step")
    assert out["ok"] and out["sync"] == {"ok": True, "unplanned": []}
    assert out["commit"]["committed"] is True and out["commit"]["message"] == "build(feat): first step"
    assert subprocess.run(["git", "log", "-1", "--format=%s"], cwd=repo, capture_output=True, text=True).stdout.strip() == "build(feat): first step"
    assert subprocess.run(["git", "status", "--porcelain"], cwd=repo, capture_output=True, text=True).stdout == ""


def test_step_commits_can_be_switched_off(checkpoint_on, run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "test -f src/feat.py"}, build={"commit_steps": False})
    run("build", "red", "1")
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x\n")
    out = run("build", "green", "1")
    assert out["ok"] and out["commit"] == {"ok": True, "committed": False, "skipped": "step commits disabled"}


def test_test_run_copies_the_review_template_once(run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "1")
    toml_config(commands={"test": "exit 0"})
    run("build", "green", "1")
    build_out(repo)
    first = run("test", "run")
    assert first["ok"] and "REVIEW.md" in first["review_md"] and "## Passes" in (repo / "REVIEW.md").read_text()
    assert first["results"] == [{"name": "test", "exit": 0}]
    assert "review_md" not in run("test", "run")
    assert run("build", "sync")["ok"]  # REVIEW.md is SDLC-owned: never an unplanned file


def test_test_run_waits_for_a_simplify_pass_after_the_last_green(run, repo: Path, accepted_plan, toml_config, monkeypatch):
    monkeypatch.delenv("SDLC_SIMPLIFY")
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "1")
    toml_config(commands={"test": "exit 0", "lint": "test ! -f lint-broken"})
    run("build", "green", "1")
    build_out(repo)
    out = run("test", "run")
    assert not out["ok"] and out["reason"].startswith("/simplify has not run since the last green step;") and out["next"] == "sdlc build simplify"
    (repo / "lint-broken").write_text("x")
    out = run("build", "simplify")
    assert not out["ok"] and out["failed"] == ["lint"] and "never the tests" in out["reason"]
    assert not run("test", "run")["ok"]  # a failed pass records nothing
    (repo / "lint-broken").unlink()
    out = run("build", "simplify")
    assert out["ok"] and out["phase"] == "simplify" and out["commit"]["committed"] is False
    assert run("test", "run")["ok"]
    toml_config(commands={"test": "exit 1"})
    run("build", "red", "t")
    toml_config(commands={"test": "exit 0"})
    assert run("build", "green", "t")["cycles"] == 2  # the simplify row is not a cycle
    assert not run("test", "run")["ok"]  # a later green needs a new pass
    toml_config(commands={"test": "exit 0"}, build={"require_simplify": False})
    assert run("test", "run")["ok"]


def test_simplify_commits_its_changes_and_refuses_unplanned_files(checkpoint_on, run, repo: Path, accepted_plan, toml_config):
    toml_config(commands={"test": "test -f src/feat.py"})
    run("build", "red", "1")
    (repo / "src").mkdir()
    (repo / "src/feat.py").write_text("x\n")
    run("build", "green", "1")
    (repo / "rogue.py").write_text("x")
    out = run("build", "simplify")
    assert not out["ok"] and out["unplanned"] == ["rogue.py"]
    (repo / "rogue.py").unlink()
    (repo / "src/feat.py").write_text("simpler\n")
    out = run("build", "simplify")
    assert out["ok"] and out["commit"]["message"] == "build(feat): simplify"
    assert subprocess.run(["git", "log", "-1", "--format=%s"], cwd=repo, capture_output=True, text=True).stdout.strip() == "build(feat): simplify"


def test_review_waits_for_the_builtin_review_record(run, repo: Path, accepted_plan, toml_config, monkeypatch):
    monkeypatch.delenv("SDLC_BUILTIN_REVIEW")
    review = repo / "sdlc/feat/review.md"
    review.write_text(REVIEW_OK)
    out = run("test", "review")
    assert not out["ok"] and out["missing"] == ["/code-review", "/security-review"] and "## Built-in review" in out["reason"]
    review.write_text(REVIEW_OK + "\n## Built-in review\n- /code-review high: 2 findings, merged into Bugs\n")
    out = run("test", "review")
    assert not out["ok"] and out["missing"] == ["/security-review"]
    review.write_text(review.read_text() + "- /security-review: none\n")
    assert run("test", "review")["ok"]
    review.write_text(REVIEW_OK)
    toml_config(test={"builtin_review": []})
    assert run("test", "review")["ok"]


def test_stage_commands_carry_the_builtin_passes():
    commands = p.PLUGIN_ROOT / "commands"
    build, test, deploy = ((commands / f"{s}.md").read_text() for s in ("build", "test", "deploy"))
    assert 'Skill({skill: "simplify"})' in build
    assert 'Skill({skill: "code-review"' in test and 'Skill({skill: "security-review"})' in test and "## Built-in review" in test
    assert "/steward" in deploy and "/ship" in deploy and "/code-review ultra" in deploy
