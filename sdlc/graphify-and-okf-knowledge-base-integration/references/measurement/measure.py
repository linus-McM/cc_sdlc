"""Run the five evals questions through `claude -p` in one mode and record token usage per question."""

import json
import subprocess
import sys
import time
from pathlib import Path

mode, root, out = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
questions = json.loads((root / "templates/evals/knowledge-questions.json").read_text())["questions"]
PREFIX = {
    "raw": "Answer from the repository source only, using Read, Grep and Glob. Do not open anything under sdlc/knowledge and do not run graphify. Be concise (under 120 words) and cite file paths. Question: ",
    "knowledge": 'Read sdlc/knowledge/index.md first and follow only the concept links you need; for call-graph facts run `graphify query "<question>"` (graphify-out/ exists). Open raw source files only if the bundle and the graph cannot answer. Be concise (under 120 words) and cite file paths. Question: ',
}[mode]
TOOLS = {"raw": "Read,Grep,Glob", "knowledge": "Read,Grep,Glob,Bash(graphify *)"}[mode]
results = []
for q in questions:
    t0 = time.time()
    proc = subprocess.run(
        ["claude", "-p", PREFIX + q["question"], "--output-format", "json", "--allowedTools", TOOLS, "--max-turns", "14"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        data = {"error": proc.stdout[-500:] + proc.stderr[-500:]}
    usage = data.get("usage", {})
    results.append(
        {
            "question": q["question"],
            "mode": mode,
            "exit": proc.returncode,
            "seconds": round(time.time() - t0, 1),
            "input_tokens": usage.get("input_tokens"),
            "cache_creation": usage.get("cache_creation_input_tokens"),
            "cache_read": usage.get("cache_read_input_tokens"),
            "output_tokens": usage.get("output_tokens"),
            "turns": data.get("num_turns"),
            "cost_usd": data.get("total_cost_usd"),
            "answer": (data.get("result") or "")[:600],
            "error": data.get("error"),
        }
    )
    out.write_text(json.dumps(results, indent=1))
print(json.dumps([{k: r[k] for k in ("mode", "exit", "seconds", "input_tokens", "cache_read", "cache_creation", "turns", "cost_usd")} for r in results], indent=1))
