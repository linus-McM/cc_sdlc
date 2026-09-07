from sdlc import artifacts as a


def test_slugify_collapses_punctuation_and_case():
    assert a.slugify("Claims status: self-service!") == "claims-status-self-service"


def test_sections_parse_headings_to_bodies():
    md = "# T\nStatus: draft\n\n## Problem\nfoo\nbar\n\n## Outcome\nbaz\n"
    assert a.sections(md) == {"Problem": "foo\nbar", "Outcome": "baz"}


def test_meta_roundtrip():
    md = "# Intent: T\nAuthor: x. Status: draft. Risk: low.\n\n## Problem\nfoo\n"
    assert a.status(md) == "draft" and a.meta(md, "Risk") == "low" and a.title(md) == "T"
    accepted = a.set_meta(md, "Status", "accepted")
    assert a.status(accepted) == "accepted" and "Status: draft" not in accepted


def test_set_section_replaces_only_that_body():
    md = "# T\n\n## A\n<x>\n\n## B\nkeep\n"
    out = a.set_section(md, "A", "new")
    assert a.sections(out) == {"A": "new", "B": "keep"}


def test_glob_semantics():
    assert a.matches("tests/unit/test_a.py", ["tests/**"])
    assert a.matches("pkg/test_a.py", ["test_*.py"])
    assert a.matches("a/b.test.ts", ["*.test.*"])
    assert not a.matches("src/a.py", ["tests/**", "test_*.py"])
    assert not a.matches("src/gen2/a.py", ["src/gen/**"])


def test_validate_reports_missing_and_placeholder_sections():
    md = "# T\nStatus: draft\n\n## Problem\n<describe>\n\n## Outcome\nreal\n"
    problems = a.validate(md, required=["Problem", "Outcome", "Constraints"])
    assert problems == ["unfilled section: Problem", "missing section: Constraints"]


def test_validate_passes_complete_document():
    md = "# T\nStatus: draft\n\n## Problem\nreal\n\n## Outcome\nreal\n"
    assert a.validate(md, required=["Problem", "Outcome"]) == []


def test_list_items_parses_bullets_and_commas():
    body = "- a/b.py (new)\n- c.py, d/e.py\nplain.py"
    assert a.list_items(body) == ["a/b.py", "c.py", "d/e.py", "plain.py"]
