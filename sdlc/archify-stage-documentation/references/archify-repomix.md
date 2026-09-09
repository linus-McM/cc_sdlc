This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.
The content has been processed where content has been compressed (code blocks are separated by ⋮---- delimiter).

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/SKILL.md, README.md, **/package.json, **/skill-release.json, **/schemas/**, **/examples/*.json, **/recipes/**, **/references/**, **/scripts/check-update.mjs, **/bin/*.mjs, skills.json, .skills/**
- Files matching these patterns are excluded: **/*.html, **/*.png, **/*.svg, **/node_modules/**, **/test/**, **/docs/**
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Content has been compressed - code blocks are separated by ⋮---- delimiter
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
````
archify/
  bin/
    archify.mjs
    open-artifact.mjs
    preview.mjs
    visual-check.mjs
  examples/
    agent-run.lifecycle.json
    agent-tool-call.workflow.json
    async-job-roundtrip.sequence.json
    brand-aware-delivery.architecture.json
    cache-miss-request.sequence.json
    checkout-platform.base.architecture.json
    checkout-platform.head.architecture.json
    deployment-release.lifecycle.json
    event-stream.dataflow.json
    incident-response.workflow.json
    product-analytics.dataflow.json
    production-deployment.architecture.json
    release-delivery.workflow.json
    web-app.architecture.json
  recipes/
    scenarios.mjs
  references/
    authoring-contract.md
    brand-marks.md
    delivery-contract.md
    viewer-runtime.md
  schemas/
    architecture.schema.json
    common.schema.json
    dataflow.schema.json
    lifecycle.schema.json
    README.md
    sequence.schema.json
    workflow.schema.json
  scripts/
    check-update.mjs
  package.json
  skill-release.json
  SKILL.md
examples/
  archify-repo-grid.architecture.json
  archify-repo.architecture.json
  checkout-platform-delta.receipt.json
  maka-architecture.architecture.json
  rag-pipeline.architecture.json
integrations/
  deepseek-harness/
    package.json
README.md
````

# Files

## File: archify/bin/archify.mjs
````javascript
function usage()
⋮----
function fail(message, code = 2)
⋮----
function rejectCliArgument(message, details =
⋮----
function rendererPath(type)
⋮----
function runNode(args, options =
⋮----
function extractQualityArgs(args)
⋮----
function extractRepoRootArgs(args)
⋮----
function rendererEnv(quality, repoRoot, diagnosticJson = false)
⋮----
function diagnostic(
⋮----
function inputDiagnostic(error, inputPath)
⋮----
function rendererFailure(result)
⋮----
// The diagnostic boundary is intentionally fail-closed. Never copy a raw
// Node stack into a machine receipt when a renderer exits unexpectedly.
⋮----
function checkerDiagnostics(checker)
⋮----
function formatDiagnostics(error, diagnostics = [])
⋮----
function assertEvidenceType(type, repoRoot)
⋮----
function exitFrom(result)
⋮----
function reportCompareFailure(
⋮----
function extractCompareOptions(args)
⋮----
function compareReceiptPath(outputPath)
⋮----
function compareCommitError(message, code, details =
⋮----
function commitComparePair(
⋮----
// Preflight the whole pair before moving either trusted target. This avoids
// replacing the HTML and only then discovering that its receipt destination
// cannot be committed (for example, because it is a directory).
⋮----
function renderValidatedArchitecture(inputPath, outputPath, quality, repoRoot)
⋮----
async function commandCompare(args)
⋮----
// Validation must see the exact authored inputs. Only after both sides
// pass do we canonicalize their collection order for deterministic SVG
// geometry and stable artifact bytes.
⋮----
const semanticHash = (diagram)
⋮----
// Raw input hashes and byte counts belong in the sidecar receipt, not the
// artifact. Keeping them out makes formatting-only input rewrites produce
// the exact same canonical review HTML and artifact hash.
⋮----
function commandRender(args)
⋮----
// render takes no options of its own once --quality and --repo-root are
// stripped, so anything left starting with -- is a typo. Without this a
// mistyped flag was taken as the output path: `render architecture spec.json
// --json out.html` wrote a file literally named `--json` and never wrote
// out.html, exiting 0. Every sibling subcommand already guards this.
⋮----
function reportArtifactFailure(
⋮----
function reportDeliveryFailure(options)
⋮----
function reportValidateFailure(options)
⋮----
function reportArtifactArgumentFailure(command, error)
⋮----
function sourceEvidenceFromArtifact(artifact)
⋮----
function engineeringProfileFromArtifact(artifact)
⋮----
async function commandDeliver(args)
⋮----
// Keep the candidate beside the target so the final rename is one
// same-filesystem commit. A render or artifact-check failure never touches
// an existing trusted output.
⋮----
async function commandPreview(args)
⋮----
function commandCheck(args)
⋮----
async function commandVisualCheck(args)
⋮----
function commandExamples()
⋮----
async function commandDoctor()
⋮----
async function commandGuide(args)
⋮----
async function commandBrands(args)
⋮----
function commandDemo(args)
⋮----
function migrationPathDiagnostics(error, sourcePath, destinationPath)
⋮----
function migrationReport({
  ok,
  sourcePath,
  destinationPath,
  sourceBytes,
  destinationBytes,
  fromSchemaVersion,
  preExistingDiagnostics = [],
  migrationDiagnostics = [],
  newSchemaDiagnostics = [],
  changedCoordinates = [],
  oldRequiredViewBox = null,
  newRequiredViewBox = null,
})
⋮----
function extractMigrationOptions(args)
⋮----
async function commandMigrate(args)
⋮----
const reportMigrationFailure = (
⋮----
// Unlike render/validate, migrate has no --quality override. Pin every stage
// to the document's durable policy and scrub any ambient profile from the
// staged renderer by passing this value explicitly.
⋮----
function commandValidate(args)
⋮----
// Layout mode emits JSON without writing HTML; keep its unused target typed.
⋮----
// Fall through to the renderer failure contract when no compiler
// receipt was produced (for example, input JSON could not be read).
````

## File: archify/bin/open-artifact.mjs
````javascript
args: (target)
⋮----
// Keep the command constant and pass the target through PowerShell's
// argument array. Paths are never interpolated into executable source.
⋮----
function launchTarget(target, options =
⋮----
export function openArtifact(target, options =
⋮----
export function openLoopbackUrl(target, options =
````

## File: archify/bin/preview.mjs
````javascript
function sha256(value)
⋮----
function sourceDigest(inputPath)
⋮----
function initialAuthoredOutput(inputPath)
⋮----
// An invalid initial source still gets a status shell. Its output target is
// fixed to the same fallback that `deliver` would use after repair.
⋮----
function previewPage()
⋮----
function compactMessage(value)
⋮----
function redactDiagnostic(value, paths)
⋮----
function safeJson(value)
⋮----
function responseHeaders(contentType)
⋮----
function parseReceipt(stdout)
⋮----
export async function startPreview(options)
⋮----
function publicState()
⋮----
function sendState(res)
⋮----
function broadcast()
⋮----
function finishStop()
⋮----
function signalActiveChild(signal)
⋮----
function closeServer()
⋮----
function startBoundedChildDrain()
⋮----
async function stop(
⋮----
function publishFailure(receipt, stdout, stderr, candidatePath, snapshotPath)
⋮----
function commitCandidate(candidatePath, receipt, generationHash)
⋮----
function beginBuild(digest, epoch)
⋮----
function queueStableBuild(hash, immediate = false)
⋮----
const launch = () =>
⋮----
function observeSource(
⋮----
export async function runPreview(options)
⋮----
const stop = () =>
````

## File: archify/bin/visual-check.mjs
````javascript
function sha256(buffer)
⋮----
function htmlEscape(value)
⋮----
function safeUnlink(file)
⋮----
// A stale optional sidecar must never make the delivered HTML mutable.
⋮----
function writeAtomic(file, contents)
⋮----
function screenshotKey(width, height, theme)
⋮----
export function sidecarPaths(artifactPath)
⋮----
function cleanupCaptureSidecars(paths)
⋮----
function executable(file, platform = process.platform)
⋮----
function findOnPath(command, env, platform)
⋮----
export function findChrome(
⋮----
class PipeCdp
⋮----
failure(stage, error)
⋮----
consume(chunk)
⋮----
send(method, params =
⋮----
waitFor(method, sessionId, timeoutMs = 15000)
⋮----
failAll(error)
⋮----
export function chromeVisualBrowserArgs(profileRoot, {
  env = process.env,
  getuid = typeof process.getuid === 'function' ? () => process.getuid() : null,
} =
⋮----
async function evaluate(cdp, sessionId, expression, awaitPromise = false)
⋮----
export class ChromeVisualBrowser
⋮----
failureDetails: () =>
⋮----
async attach()
⋮----
async inspect(
⋮----
async close()
⋮----
// Chrome may briefly retain profile files on Windows; evidence is done.
⋮----
function observation(
⋮----
function contactSheetHtml(
⋮----
function viewportSubject(artifact, entry)
⋮----
function failureDiagnostic(
⋮----
function observationDiagnostics(
⋮----
function baseReceipt(
⋮----
function persistReceipt(outputs, receipt)
⋮----
export async function runVisualCheck({
  artifactPath,
  chromePath,
  resolveChrome = findChrome,
  browserFactory = async (resolvedChrome) => new ChromeVisualBrowser(resolvedChrome),
} =
````

## File: archify/examples/agent-run.lifecycle.json
````json
{
  "schema_version": 1,
  "diagram_type": "lifecycle",
  "meta": {
    "title": "Agent Run Lifecycle",
    "output": "examples/lifecycle-agent-run.html",
    "viewBox": [1030, 630],
    "animation": "trace",
    "quality_profile": "showcase",
    "views": [
      { "id": "main-lifecycle", "label": "Main lifecycle", "focus": ["queued", "planning", "executing", "reviewing", "completed"], "note": "Follow the ordered phases from accepted request to completed response." },
      { "id": "human-waits", "label": "Human and input waits", "focus": ["executing", "approval", "reviewing", "blocked"], "note": "See where the run pauses without becoming terminal." },
      { "id": "recovery-and-exits", "label": "Recovery and terminal exits", "focus": ["executing", "failed", "blocked", "cancelled", "expired"], "note": "Separate retryable failure from cancellation and expiry." }
    ]
  },
  "lanes": [
    { "id": "main", "label": "Lifecycle phases" },
    { "id": "waiting", "label": "Interruptions" },
    { "id": "exceptions", "label": "Recovery loop" },
    { "id": "terminal", "label": "Terminal exits" }
  ],
  "states": [
    { "id": "queued", "type": "start", "label": "Queued", "sublabel": "request accepted", "lane": "main", "col": 0, "step": "01", "tag": "entry" },
    { "id": "planning", "type": "active", "label": "Planning", "sublabel": "build task graph", "lane": "main", "col": 1, "step": "02", "tag": "model" },
    { "id": "executing", "type": "active", "label": "Executing", "sublabel": "tool calls", "lane": "main", "col": 2, "step": "03", "tag": "work" },
    { "id": "reviewing", "type": "decision", "label": "Reviewing", "sublabel": "quality gate", "lane": "main", "col": 3, "step": "04", "tag": "check" },
    { "id": "completed", "type": "success", "label": "Completed", "sublabel": "final response", "lane": "main", "col": 4, "step": "05", "tag": "done" },
    { "id": "approval", "type": "waiting", "label": "Needs Approval", "sublabel": "human gate", "lane": "waiting", "col": 0, "tag": "pause" },
    { "id": "blocked", "type": "waiting", "label": "Blocked", "sublabel": "missing input", "lane": "waiting", "col": 1, "tag": "wait" },
    { "id": "failed", "type": "failure", "label": "Failed", "sublabel": "recoverable error", "lane": "exceptions", "col": 0, "yOffset": 78, "tag": "retryable" },
    { "id": "cancelled", "type": "failure", "label": "Cancelled", "sublabel": "user stopped", "lane": "terminal", "col": 0, "tag": "terminal" },
    { "id": "expired", "type": "failure", "label": "Expired", "sublabel": "timeout", "lane": "terminal", "col": 1, "tag": "terminal" }
  ],
  "transitions": [
    { "id": "approval-needed", "from": "executing", "to": "approval", "variant": "security", "fromSide": "bottom", "toSide": "top", "route": "straight" },
    { "id": "review-blocked", "from": "reviewing", "to": "blocked", "variant": "default", "route": "drop" },
    { "id": "execution-failed", "from": "executing", "to": "failed", "variant": "security", "fromSide": "left", "toSide": "left", "via": [[320, 157], [320, 385]] },
    { "id": "failed-retry", "from": "failed", "to": "executing", "variant": "emphasis", "fromSide": "left", "toSide": "top", "via": [[20, 385], [20, 80], [402, 80]] },
    { "id": "block-expired", "from": "blocked", "to": "expired", "variant": "security", "fromSide": "bottom", "toSide": "top", "route": "straight" },
    { "id": "approval-cancelled", "from": "approval", "to": "cancelled", "variant": "security", "fromSide": "bottom", "toSide": "top", "via": [[480, 336], [480, 432], [402, 432]] }
  ],
  "cards": [
    {
      "dot": "emerald",
      "title": "Main Path + Waits",
      "items": [
        "The run has five ordered phases from queue to completion",
        "Approval and missing input pause the run without ending it"
      ]
    },
    {
      "dot": "rose",
      "title": "Recovery + Terminal Exits",
      "items": [
        "Failed loops back while retry budget remains",
        "Cancelled and Expired are terminal exits with no return path"
      ]
    }
  ]
}
````

## File: archify/examples/agent-tool-call.workflow.json
````json
{
  "schema_version": 2,
  "diagram_type": "workflow",
  "meta": {
    "title": "Agent Tool Call Workflow",
    "animation": "trace",
    "visual_preset": "signal-flow",
    "quality_profile": "showcase",
    "views": [
      {
        "id": "happy-path",
        "label": "Request to result",
        "focus": ["user", "chat", "planner", "router", "approval", "tool", "external", "final"],
        "note": "Follow the successful request from user intent to the final reply."
      },
      {
        "id": "safety-gate",
        "label": "Policy and recovery",
        "focus": ["router", "approval", "blocked", "retry"],
        "note": "See where risky work stops, waits for consent, or returns for revision."
      },
      {
        "id": "evidence-loop",
        "label": "Evidence and memory",
        "focus": ["external", "store", "trace"],
        "note": "Isolate the durable trace and context path behind the visible answer."
      }
    ],
    "output": "examples/workflow-agent-tool-call-rendered.html"
  },
  "lanes": [
    { "id": "ui", "label": "User Interface" },
    { "id": "agent", "label": "Agent Runtime" },
    { "id": "policy", "label": "Policy & Recovery", "variant": "exception" },
    { "id": "tools", "label": "Tool Execution & Evidence" }
  ],
  "phases": [
    { "id": "intake", "label": "Intake", "fromCol": 0, "toCol": 1 },
    { "id": "reasoning", "label": "Plan + route", "fromCol": 2, "toCol": 3, "variant": "emphasis" },
    { "id": "execution", "label": "Execute + report", "fromCol": 4, "toCol": 5, "variant": "dashed" }
  ],
  "groups": [
    { "id": "agent_loop", "label": "Planning loop", "lane": "agent", "fromCol": 2, "toCol": 3, "variant": "emphasis" },
    { "id": "exception_path", "label": "Human or policy stop", "lane": "policy", "fromCol": 3, "toCol": 5, "variant": "security" },
    { "id": "evidence_path", "label": "Evidence path", "lane": "tools", "fromCol": 1, "toCol": 2, "variant": "dashed" },
    { "id": "tool_work", "label": "Tool work", "lane": "tools", "fromCol": 4, "toCol": 5, "variant": "dashed" }
  ],
  "mainPath": ["user", "chat", "planner", "router", "approval", "tool", "external", "final"],
  "nodes": [
    { "id": "user", "lane": "ui", "col": 0, "type": "external", "label": "User", "sublabel": "asks for work", "width": 132 },
    { "id": "chat", "lane": "ui", "col": 1, "type": "frontend", "label": "Chat Surface", "sublabel": "thread + files", "width": 132 },
    { "id": "final", "lane": "ui", "col": 5, "type": "backend", "label": "Final Reply", "sublabel": "answer + changes", "width": 132 },
    { "id": "planner", "lane": "agent", "col": 2, "type": "backend", "label": "Agent Planner", "sublabel": "plan next step", "tag": "context aware", "width": 132 },
    { "id": "router", "lane": "agent", "col": 3, "type": "backend", "label": "Tool Router", "sublabel": "choose capability", "width": 132 },
    { "id": "approval", "lane": "policy", "col": 3, "type": "security", "label": "Approval Gate", "sublabel": "scope + consent", "tag": "block risky ops", "width": 132 },
    { "id": "blocked", "lane": "policy", "col": 4, "type": "security", "label": "Blocked", "sublabel": "wait or reject", "width": 132 },
    { "id": "retry", "lane": "policy", "col": 5, "type": "messagebus", "label": "Retry Path", "sublabel": "revise request", "width": 132 },
    { "id": "tool", "lane": "tools", "col": 4, "type": "messagebus", "label": "Tool Call", "sublabel": "shell / browser / MCP", "tag": "structured result", "width": 132 },
    { "id": "external", "lane": "tools", "col": 5, "type": "cloud", "label": "External API", "sublabel": "network service", "width": 132 },
    { "id": "store", "lane": "tools", "col": 1, "type": "database", "label": "Context Store", "sublabel": "repo + memory", "width": 132 },
    { "id": "trace", "lane": "tools", "col": 2, "type": "database", "label": "Trace Log", "sublabel": "events + output", "width": 132 }
  ],
  "edges": [
    { "id": "request-chat", "from": "user", "to": "chat", "variant": "default" },
    { "id": "plan-request", "from": "chat", "to": "planner", "label": "plan", "variant": "emphasis" },
    { "id": "planner-route", "from": "planner", "to": "router", "variant": "default" },
    { "id": "approval-check", "from": "router", "to": "approval", "label": "needs approval?", "variant": "security" },
    { "id": "approved-tool", "from": "approval", "to": "tool", "variant": "emphasis" },
    { "id": "approval-denied", "from": "approval", "to": "blocked", "label": "denied", "variant": "security", "role": "error" },
    { "id": "retry-request", "from": "blocked", "to": "retry", "variant": "dashed", "role": "branch" },
    { "id": "tool-external-call", "from": "tool", "to": "external", "variant": "default" },
    { "id": "external-reply", "from": "external", "to": "final", "variant": "emphasis", "role": "return", "fromSide": "right", "toSide": "right", "route": "outside-right", "width": 1.2 },
    { "id": "record-result", "from": "external", "to": "trace", "label": "record result", "variant": "dashed", "fromSide": "bottom", "toSide": "bottom", "route": "bottom-channel", "labelSegment": 1 },
    { "id": "write-trace-memory", "from": "store", "to": "trace", "label": "trace + memory", "variant": "dashed" }
  ],
  "cards": [
    {
      "dot": "cyan",
      "title": "Compiler Contract",
      "items": [
        "Lanes and columns determine node placement",
        "Labels reserve clearance; routes stay orthogonal"
      ]
    },
    {
      "dot": "rose",
      "title": "Runtime Semantics",
      "items": [
        "Approval gates risky work before tool execution",
        "Evidence returns through isolated trace and memory"
      ]
    }
  ]
}
````

## File: archify/examples/async-job-roundtrip.sequence.json
````json
{
  "schema_version": 1,
  "diagram_type": "sequence",
  "meta": {
    "title": "Async Job Roundtrip",
    "output": "examples/async-job-roundtrip.html",
    "viewBox": [820, 920],
    "animation": "trace",
    "visual_preset": "signal-flow",
    "quality_profile": "showcase",
    "views": [
      { "id": "accept-and-enqueue", "label": "Accept without blocking", "focus": ["client", "api", "queue"], "note": "The API acknowledges quickly after durable enqueue." },
      { "id": "work-and-retry", "label": "Background work and retry", "focus": ["queue", "worker", "provider"], "note": "Timeouts re-enter the queue instead of holding the original request open." },
      { "id": "observe-final-state", "label": "Observe final consistency", "focus": ["worker", "store", "notify", "client", "api"], "note": "Webhook delivery is primary; polling remains a bounded fallback." }
    ]
  },
  "participants": [
    { "id": "client", "type": "external", "label": "Client", "sublabel": "mobile app" },
    { "id": "api", "type": "backend", "label": "Jobs API", "sublabel": "request edge" },
    { "id": "queue", "type": "messagebus", "label": "Queue", "sublabel": "durable work" },
    { "id": "worker", "type": "backend", "label": "Worker", "sublabel": "background" },
    { "id": "provider", "type": "cloud", "label": "Provider", "sublabel": "external API" },
    { "id": "store", "type": "database", "label": "Job Store", "sublabel": "source of truth" },
    { "id": "notify", "type": "messagebus", "label": "Notifier", "sublabel": "webhook" }
  ],
  "segments": [
    { "from": 150, "to": 288, "label": "Accept" },
    { "from": 306, "to": 538, "label": "Background work" },
    { "from": 554, "to": 800, "label": "Notify + reconcile" }
  ],
  "messages": [
    { "from": "client", "to": "api", "y": 180, "label": "POST /jobs", "variant": "emphasis" },
    { "from": "api", "to": "queue", "y": 222, "label": "enqueue job", "variant": "emphasis" },
    { "from": "api", "to": "client", "y": 264, "label": "202 + job id", "variant": "return" },
    { "from": "queue", "to": "worker", "y": 326, "label": "deliver", "variant": "emphasis" },
    { "from": "worker", "to": "provider", "y": 368, "label": "perform work", "variant": "default" },
    { "from": "provider", "to": "worker", "y": 410, "label": "result / timeout", "variant": "return" },
    { "from": "worker", "to": "queue", "y": 452, "label": "retry if timeout", "variant": "dashed" },
    { "from": "worker", "to": "store", "y": 494, "label": "persist final state", "variant": "emphasis" },
    { "from": "worker", "to": "notify", "y": 566, "label": "job.completed", "variant": "dashed" },
    { "from": "notify", "to": "client", "y": 608, "label": "signed webhook", "variant": "dashed" },
    { "from": "client", "to": "api", "y": 650, "label": "GET /jobs/:id", "variant": "default" },
    { "from": "api", "to": "store", "y": 692, "label": "read status", "variant": "default" },
    { "from": "store", "to": "api", "y": 734, "label": "completed", "variant": "return" },
    { "from": "api", "to": "client", "y": 776, "label": "200 final result", "variant": "return" }
  ],
  "activations": [
    { "participant": "api", "from": 174, "to": 272, "type": "backend" },
    { "participant": "queue", "from": 216, "to": 334, "type": "messagebus" },
    { "participant": "worker", "from": 320, "to": 574, "type": "backend" },
    { "participant": "provider", "from": 362, "to": 416, "type": "cloud" },
    { "participant": "store", "from": 488, "to": 742, "type": "database" },
    { "participant": "notify", "from": 560, "to": 616, "type": "messagebus" },
    { "participant": "api", "from": 644, "to": 784, "type": "backend" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Fast Acknowledgement", "items": ["The caller receives a durable job id before work begins", "Queue ownership is visible in the acceptance contract", "The original connection does not wait for provider latency"] },
    { "dot": "orange", "title": "Bounded Recovery", "items": ["Timeouts re-enter the queue with a retry policy", "Final state is persisted before notification", "The job store remains the source of truth"] },
    { "dot": "emerald", "title": "Two Observation Paths", "items": ["A signed webhook announces completion", "Status polling is a fallback, not a second workflow", "Both paths converge on the same final state"] }
  ]
}
````

## File: archify/examples/brand-aware-delivery.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Brand-aware AI delivery",
    "quality_profile": "showcase",
    "viewBox": [1120, 640],
    "views": [
      {
        "id": "delivery-path",
        "label": "Delivery path",
        "focus": ["request", "claude", "github", "container", "edge", "customer"],
        "note": "Follow one delivery from the request through the model, repository, container, and edge."
      },
      {
        "id": "business-data",
        "label": "Business and data",
        "focus": ["container", "database", "billing"],
        "note": "Inspect durable state and billing without losing the main delivery path."
      }
    ]
  },
  "components": [
    { "id": "request", "type": "external", "label": "Product request", "sublabel": "Owner brief", "pos": [38, 260], "size": [138, 68] },
    { "id": "claude", "type": "frontend", "label": "Claude", "sublabel": "Plan and author", "brand": "claude", "pos": [220, 260], "size": [138, 68] },
    { "id": "github", "type": "messagebus", "label": "GitHub", "sublabel": "Review and merge", "brand": "github", "pos": [402, 260], "size": [138, 68] },
    { "id": "container", "type": "backend", "label": "Docker service", "sublabel": "Build and run", "brand": "docker", "pos": [584, 260], "size": [138, 68] },
    { "id": "edge", "type": "cloud", "label": "Cloudflare", "sublabel": "Global delivery", "brand": "cloudflare", "pos": [766, 260], "size": [138, 68] },
    { "id": "customer", "type": "external", "label": "Customers", "sublabel": "Web and mobile", "pos": [948, 260], "size": [138, 68] },
    { "id": "database", "type": "database", "label": "PostgreSQL", "sublabel": "Durable state", "brand": "postgresql", "pos": [584, 420], "size": [138, 68] },
    { "id": "billing", "type": "external", "label": "Stripe", "sublabel": "Billing events", "brand": "stripe", "pos": [766, 420], "size": [138, 68] }
  ],
  "connections": [
    { "id": "brief-to-claude", "from": "request", "to": "claude", "label": "brief", "variant": "emphasis" },
    { "id": "claude-to-github", "from": "claude", "to": "github", "label": "change set", "labelDy": -28 },
    { "id": "github-to-container", "from": "github", "to": "container", "label": "approved build", "labelDy": -28 },
    { "id": "container-to-edge", "from": "container", "to": "edge", "label": "deploy" },
    { "id": "edge-to-customer", "from": "edge", "to": "customer", "label": "HTTPS", "variant": "emphasis" },
    { "id": "container-to-database", "from": "container", "to": "database", "label": "SQL", "fromSide": "bottom", "toSide": "top", "labelAt": [625, 370] },
    { "id": "container-to-billing", "from": "container", "to": "billing", "label": "create charge", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "via": [[653, 374], [835, 374]] },
    { "id": "billing-to-database", "from": "billing", "to": "database", "label": "webhook", "variant": "dashed" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Identity at a glance", "items": ["Semantic color still explains technical role", "Brand badges identify the actual products"] },
    { "dot": "amber", "title": "Portable by default", "items": ["Preset marks ship inside Archify", "Every visual export keeps the same badge"] }
  ]
}
````

## File: archify/examples/cache-miss-request.sequence.json
````json
{
  "schema_version": 1,
  "diagram_type": "sequence",
  "meta": {
    "title": "Cache Miss Request Sequence",
    "output": "examples/sequence-cache-miss-request.html",
    "viewBox": [1080, 560],
    "column_fit": "spread",
    "animation": "trace",
    "quality_profile": "showcase",
    "views": [
      { "id": "request-and-auth", "label": "Request and identity", "focus": ["user", "web", "api", "auth"], "note": "Follow the user request through the authentication check." },
      { "id": "cache-fallback", "label": "Cache fallback", "focus": ["api", "redis", "db"], "note": "See the cache miss and the source-of-truth query it triggers." },
      { "id": "return-and-trace", "label": "Return and trace", "focus": ["db", "api", "redis", "trace", "web", "user"], "note": "Separate response latency from the non-blocking observability write." }
    ]
  },
  "participants": [
    { "id": "user", "type": "external", "label": "User", "sublabel": "browser session" },
    { "id": "web", "type": "frontend", "label": "Web App", "sublabel": "React UI" },
    { "id": "api", "type": "backend", "label": "API", "sublabel": "request handler" },
    { "id": "auth", "type": "security", "label": "Auth", "sublabel": "JWT verify" },
    { "id": "redis", "type": "database", "label": "Redis", "sublabel": "cache" },
    { "id": "db", "type": "database", "label": "Postgres", "sublabel": "source of truth" },
    { "id": "trace", "type": "messagebus", "label": "Trace", "sublabel": "async event" }
  ],
  "segments": [
    { "from": 150, "to": 250, "label": "Request" },
    { "from": 260, "to": 370, "label": "Fallback" },
    { "from": 380, "to": 480, "label": "Response + trace" }
  ],
  "messages": [
    { "id": "open-page", "from": "user", "to": "web", "y": 160, "label": "open page", "variant": "default" },
    { "id": "dashboard-request", "from": "web", "to": "api", "y": 185, "label": "GET /dashboard", "variant": "emphasis" },
    { "id": "verify-jwt", "from": "api", "to": "auth", "y": 210, "label": "verify JWT", "variant": "security" },
    { "id": "auth-claims", "from": "auth", "to": "api", "y": 238, "label": "claims ok", "variant": "return" },
    { "id": "cache-read", "from": "api", "to": "redis", "y": 270, "label": "read cache", "variant": "default" },
    { "id": "cache-miss", "from": "redis", "to": "api", "y": 298, "label": "miss", "variant": "return" },
    { "id": "profile-query", "from": "api", "to": "db", "y": 330, "label": "query profile + metrics", "variant": "emphasis" },
    { "id": "profile-rows", "from": "db", "to": "api", "y": 358, "label": "rows", "variant": "return" },
    { "id": "cache-write", "from": "api", "to": "redis", "y": 390, "label": "set cache", "variant": "dashed" },
    { "id": "trace-emit", "from": "api", "to": "trace", "y": 418, "label": "emit trace", "variant": "dashed" },
    { "id": "dashboard-response", "from": "api", "to": "web", "y": 443, "label": "200 JSON", "variant": "return" },
    { "id": "page-render", "from": "web", "to": "user", "y": 468, "label": "render", "variant": "return" }
  ],
  "activations": [
    { "participant": "web", "from": 180, "to": 474, "type": "frontend" },
    { "participant": "api", "from": 185, "to": 450, "type": "backend" },
    { "participant": "auth", "from": 205, "to": 244, "type": "security" },
    { "participant": "redis", "from": 265, "to": 304, "type": "database" },
    { "participant": "db", "from": 325, "to": 364, "type": "database" },
    { "participant": "trace", "from": 413, "to": 449, "type": "messagebus" }
  ],
  "cards": [
    {
      "dot": "emerald",
      "title": "Happy Path",
      "items": [
        "The main request is Web App -> API -> data source -> response",
        "Return messages are quieter than forward calls",
        "Activation bars make ownership duration visible"
      ]
    },
    {
      "dot": "rose",
      "title": "Policy + Fallback",
      "items": [
        "JWT verification is colored as a security interaction",
        "Cache miss is visible without overpowering the main path",
        "Database access only appears after cache fallback"
      ]
    },
    {
      "dot": "orange",
      "title": "Async Trace",
      "items": [
        "Trace emission is dashed and secondary",
        "It does not block the response path",
        "The diagram separates user-facing latency from observability"
      ]
    }
  ]
}
````

## File: archify/examples/checkout-platform.base.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Checkout Platform — Baseline",
    "visual_preset": "signal-flow"
  },
  "components": [
    { "id": "buyers", "type": "external", "label": "Buyers", "sublabel": "Web + mobile", "pos": [40, 250], "size": [120, 60] },
    { "id": "edge", "type": "cloud", "label": "Edge Gateway", "sublabel": "TLS + routing", "pos": [220, 250], "size": [130, 60] },
    { "id": "checkout", "type": "backend", "label": "Checkout API", "sublabel": "v1 service", "pos": [430, 250], "size": [130, 60] },
    { "id": "cache", "type": "database", "label": "Session Cache", "sublabel": "Redis", "pos": [430, 100], "size": [130, 60] },
    { "id": "orders", "type": "database", "label": "Orders", "sublabel": "PostgreSQL", "pos": [640, 250], "size": [130, 60] },
    { "id": "queue", "type": "messagebus", "label": "Order Events", "sublabel": "durable queue", "pos": [430, 400], "size": [130, 60] },
    { "id": "worker", "type": "backend", "label": "Fulfilment", "sublabel": "async worker", "pos": [640, 400], "size": [130, 60] },
    { "id": "payments", "type": "external", "label": "Payment Rail", "sublabel": "external", "pos": [850, 250], "size": [130, 60] }
  ],
  "boundaries": [
    { "kind": "region", "label": "Production region", "wraps": ["edge", "checkout", "cache", "orders", "queue", "worker"] },
    { "kind": "security-group", "label": "Checkout trust zone", "wraps": ["checkout", "orders"] }
  ],
  "connections": [
    { "id": "buyer-request", "from": "buyers", "to": "edge", "label": "HTTPS", "variant": "emphasis" },
    { "id": "edge-checkout", "from": "edge", "to": "checkout" },
    { "id": "session-read", "from": "checkout", "to": "cache", "label": "session", "fromSide": "top", "toSide": "bottom", "labelDy": -66 },
    { "id": "persist-order", "from": "checkout", "to": "orders", "label": "SQL" },
    { "id": "publish-order", "from": "checkout", "to": "queue", "label": "accepted", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "labelDy": 66 },
    { "id": "consume-order", "from": "queue", "to": "worker" },
    { "id": "authorize-payment", "from": "orders", "to": "payments", "label": "authorize", "variant": "security" }
  ]
}
````

## File: archify/examples/checkout-platform.head.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Checkout Platform — Fraud Gate",
    "visual_preset": "signal-flow"
  },
  "components": [
    { "id": "buyers", "type": "external", "label": "Buyers", "sublabel": "Web + mobile", "pos": [40, 250], "size": [120, 60] },
    { "id": "edge", "type": "cloud", "label": "Edge Gateway", "sublabel": "TLS + routing", "pos": [220, 250], "size": [130, 60] },
    { "id": "checkout", "type": "backend", "label": "Checkout API", "sublabel": "v2 idempotent", "pos": [430, 250], "size": [130, 60] },
    { "id": "fraud", "type": "security", "label": "Fraud Gate", "sublabel": "policy scoring", "pos": [640, 100], "size": [130, 60], "tag": "new owner" },
    { "id": "orders", "type": "database", "label": "Orders", "sublabel": "PostgreSQL", "pos": [640, 250], "size": [130, 60] },
    { "id": "queue", "type": "messagebus", "label": "Order Events", "sublabel": "durable queue", "pos": [430, 420], "size": [130, 60] },
    { "id": "worker", "type": "backend", "label": "Fulfilment", "sublabel": "async worker", "pos": [640, 400], "size": [130, 60] },
    { "id": "payments", "type": "external", "label": "Payment Rail", "sublabel": "external", "pos": [850, 250], "size": [130, 60] }
  ],
  "boundaries": [
    { "kind": "region", "label": "Production region", "wraps": ["edge", "checkout", "fraud", "orders", "queue", "worker"] },
    { "kind": "security-group", "label": "Checkout trust zone", "wraps": ["checkout", "fraud", "orders"] }
  ],
  "connections": [
    { "id": "buyer-request", "from": "buyers", "to": "edge", "label": "HTTPS", "variant": "emphasis" },
    { "id": "edge-checkout", "from": "edge", "to": "checkout" },
    { "id": "fraud-check", "from": "checkout", "to": "fraud", "label": "screen", "variant": "security", "fromSide": "top", "toSide": "bottom", "labelDy": -66 },
    { "id": "persist-order", "from": "checkout", "to": "orders", "label": "SQL tx" },
    { "id": "publish-order", "from": "checkout", "to": "queue", "label": "accepted", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "labelDy": 76 },
    { "id": "consume-order", "from": "queue", "to": "worker" },
    { "id": "authorize-payment", "from": "fraud", "to": "payments", "label": "authorize", "variant": "security", "fromSide": "right", "toSide": "top", "via": [[820, 130], [915, 130]] }
  ]
}
````

## File: archify/examples/deployment-release.lifecycle.json
````json
{
  "schema_version": 1,
  "diagram_type": "lifecycle",
  "meta": {
    "title": "Deployment Release Lifecycle",
    "output": "examples/deployment-release.html",
    "viewBox": [980, 680],
    "animation": "trace",
    "visual_preset": "signal-flow",
    "quality_profile": "showcase",
    "views": [
      { "id": "promotion-rail", "label": "Promotion rail", "focus": ["queued", "building", "verifying", "ready", "live"], "note": "Follow the deployment object from accepted change to healthy production." },
      { "id": "approval-gate", "label": "Approval gate", "focus": ["verifying", "approval", "cancelled", "ready"], "note": "Approval pauses promotion and can terminate the release cleanly." },
      { "id": "rollback-outcomes", "label": "Rollback outcomes", "focus": ["ready", "rollback", "failed", "live", "paused", "rolled_back"], "note": "Separate pre-promotion failure from post-promotion health regression." }
    ]
  },
  "lanes": [
    { "id": "main", "label": "Release phases" },
    { "id": "waiting", "label": "Approval + health wait" },
    { "id": "recovery", "label": "Rollback controller" },
    { "id": "terminal", "label": "Terminal exits" }
  ],
  "states": [
    { "id": "queued", "type": "start", "label": "Queued", "sublabel": "change accepted", "lane": "main", "col": 0, "step": "01", "tag": "pending" },
    { "id": "building", "type": "active", "label": "Building", "sublabel": "immutable image", "lane": "main", "col": 1, "step": "02", "tag": "running" },
    { "id": "verifying", "type": "decision", "label": "Verifying", "sublabel": "tests + policy", "lane": "main", "col": 2, "step": "03", "tag": "gate" },
    { "id": "ready", "type": "waiting", "label": "Ready", "sublabel": "promotion pending", "lane": "main", "col": 3, "step": "04", "tag": "approved" },
    { "id": "live", "type": "success", "label": "Live", "sublabel": "production healthy", "lane": "main", "col": 4, "step": "05", "tag": "success" },
    { "id": "approval", "type": "waiting", "label": "Needs Approval", "sublabel": "release owner", "lane": "waiting", "col": 0, "tag": "pause" },
    { "id": "rollback", "type": "active", "label": "Rolling Back", "sublabel": "last good image", "lane": "recovery", "col": 1, "tag": "automatic" },
    { "id": "paused", "type": "waiting", "label": "Health Paused", "sublabel": "SLO regression", "lane": "waiting", "col": 2, "tag": "observe" },
    { "id": "cancelled", "type": "failure", "label": "Cancelled", "sublabel": "approval denied", "lane": "terminal", "col": 0, "tag": "terminal" },
    { "id": "failed", "type": "failure", "label": "Failed", "sublabel": "rollback failed", "lane": "terminal", "col": 1, "tag": "terminal" },
    { "id": "rolled_back", "type": "success", "label": "Rolled Back", "sublabel": "service restored", "lane": "terminal", "col": 2, "tag": "terminal" }
  ],
  "transitions": [
    { "from": "verifying", "to": "approval", "variant": "security", "route": "straight", "fromSide": "bottom", "toSide": "top" },
    { "from": "approval", "to": "cancelled", "variant": "security", "route": "straight", "fromSide": "bottom", "toSide": "top" },
    { "from": "ready", "to": "rollback", "variant": "security", "route": "straight", "fromSide": "bottom", "toSide": "top" },
    { "from": "rollback", "to": "failed", "variant": "security", "route": "straight", "fromSide": "bottom", "toSide": "top" },
    { "from": "live", "to": "paused", "variant": "dashed", "route": "straight", "fromSide": "bottom", "toSide": "top" },
    { "from": "paused", "to": "rolled_back", "variant": "emphasis", "route": "straight", "fromSide": "bottom", "toSide": "top" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Promotion Rail", "items": ["The release object moves through five ordered phases", "Verification and approval remain distinct states", "Live means production health is currently proven"] },
    { "dot": "amber", "title": "Wait States", "items": ["Human approval can pause without consuming a worker", "A health regression pauses further rollout", "Every wait exposes the event required to continue"] },
    { "dot": "rose", "title": "Explicit Endings", "items": ["Denied approval ends as Cancelled", "Rollback controller failure ends as Failed", "Successful rollback is a terminal restored outcome"] }
  ]
}
````

## File: archify/examples/event-stream.dataflow.json
````json
{
  "schema_version": 1,
  "diagram_type": "dataflow",
  "meta": {
    "title": "Order Event-stream Topology",
    "output": "examples/event-stream.html",
    "viewBox": [1080, 780],
    "animation": "trace",
    "visual_preset": "signal-flow",
    "quality_profile": "showcase",
    "views": [
      { "id": "order-transit", "label": "Order event transit", "focus": ["checkout", "orders", "validate", "state", "fulfillment"], "note": "Follow an order from producer through ordered processing to fulfillment." },
      { "id": "payment-transit", "label": "Payment event transit", "focus": ["billing", "payments", "enrich", "state", "analytics"], "note": "Track payment facts into the shared materialized state and analytics." },
      { "id": "failure-and-replay", "label": "Failure and replay", "focus": ["validate", "enrich", "dlq", "replay", "ops"], "note": "Isolate dead letters, operator review, and controlled replay ownership." }
    ]
  },
  "stages": [
    { "label": "Producers" },
    { "label": "Transit" },
    { "label": "Processors" },
    { "label": "State + recovery" },
    { "label": "Consumers" }
  ],
  "nodes": [
    { "id": "checkout", "type": "frontend", "label": "Checkout API", "sublabel": "order producer", "stage": 0, "row": 0, "tag": "team commerce" },
    { "id": "billing", "type": "backend", "label": "Billing API", "sublabel": "payment producer", "stage": 0, "row": 2, "tag": "team money" },
    { "id": "orders", "type": "messagebus", "label": "orders.v1", "sublabel": "12 partitions", "stage": 1, "row": 0, "tag": "key: order_id" },
    { "id": "payments", "type": "messagebus", "label": "payments.v2", "sublabel": "8 partitions", "stage": 1, "row": 2, "tag": "key: order_id" },
    { "id": "validate", "type": "backend", "label": "Order Validate", "sublabel": "group fulfillment", "stage": 2, "row": 0, "tag": "ordered" },
    { "id": "enrich", "type": "backend", "label": "Payment Enrich", "sublabel": "group analytics", "stage": 2, "row": 2, "tag": "at-least-once" },
    { "id": "state", "type": "database", "label": "Order State", "sublabel": "materialized view", "stage": 3, "row": 1, "tag": "idempotent" },
    { "id": "dlq", "type": "messagebus", "label": "events.dlq", "sublabel": "poison events", "stage": 3, "row": 4, "tag": "7-day retention" },
    { "id": "fulfillment", "type": "backend", "label": "Fulfillment", "sublabel": "shipping workflow", "stage": 4, "row": 0, "tag": "consumer" },
    { "id": "analytics", "type": "database", "label": "Analytics", "sublabel": "streaming facts", "stage": 4, "row": 2, "tag": "consumer" },
    { "id": "replay", "type": "security", "label": "Replay Tool", "sublabel": "approved batch", "stage": 4, "row": 4, "tag": "operator gate" },
    { "id": "ops", "type": "external", "label": "On-call", "sublabel": "DLQ owner", "stage": 4, "row": 3, "yOffset": -18, "tag": "SRE" }
  ],
  "flows": [
    { "from": "checkout", "to": "orders", "label": "OrderPlaced", "classification": "schema v1", "variant": "emphasis", "route": "straight" },
    { "from": "billing", "to": "payments", "label": "PaymentCaptured", "classification": "schema v2", "variant": "emphasis", "route": "straight" },
    { "from": "orders", "to": "validate", "label": "ordered orders", "classification": "consumer group", "variant": "emphasis", "route": "straight" },
    { "from": "payments", "to": "enrich", "label": "payment facts", "classification": "at-least-once", "variant": "emphasis", "route": "straight" },
    { "from": "validate", "to": "state", "label": "valid order", "classification": "idempotent", "variant": "emphasis", "route": "vertical-channel" },
    { "from": "enrich", "to": "state", "label": "enriched payment", "classification": "idempotent", "variant": "default", "route": "vertical-channel" },
    { "from": "state", "to": "fulfillment", "label": "ready orders", "classification": "read model", "variant": "emphasis", "route": "vertical-channel" },
    { "from": "state", "to": "analytics", "label": "order facts", "classification": "non-PII", "variant": "default", "route": "vertical-channel" },
    { "from": "validate", "to": "dlq", "label": "invalid event", "classification": "dead letter", "variant": "security", "fromSide": "top", "toSide": "top", "via": [[530, 80], [20, 80], [20, 550], [745, 550]], "labelAt": [300, 550] },
    { "from": "enrich", "to": "dlq", "label": "poison event", "classification": "dead letter", "variant": "security", "route": "bottom-channel", "labelDy": 30 },
    { "from": "dlq", "to": "ops", "label": "failure sample", "classification": "restricted", "variant": "security", "route": "vertical-channel" },
    { "from": "dlq", "to": "replay", "label": "approved replay", "classification": "audited batch", "variant": "dashed", "route": "straight", "labelDy": 30 }
  ],
  "cards": [
    { "dot": "amber", "title": "Transit Contract", "items": ["Every event and topic is named", "Partition keys preserve per-order ordering", "Consumer groups expose processing ownership"] },
    { "dot": "emerald", "title": "State + Delivery", "items": ["Processors write an idempotent materialized view", "Fulfillment and analytics consume distinct assets", "At-least-once delivery never implies duplicate business effects"] },
    { "dot": "rose", "title": "Failure Ownership", "items": ["Poison events land in a retained dead-letter topic", "On-call inspects samples before replay", "Replay is gated, batched, and auditable"] }
  ]
}
````

## File: archify/examples/incident-response.workflow.json
````json
{
  "schema_version": 1,
  "diagram_type": "workflow",
  "meta": {
    "title": "Incident Response Runbook",
    "output": "examples/incident-response.html",
    "animation": "trace",
    "visual_preset": "signal-flow",
    "quality_profile": "showcase",
    "views": [
      { "id": "detect-and-triage", "label": "Detect and establish command", "focus": ["alert", "page", "triage", "declare"], "note": "Follow the first minutes from signal to an owned incident." },
      { "id": "mitigate-and-verify", "label": "Mitigate and prove recovery", "focus": ["triage", "contain", "recover", "verify", "close"], "note": "Keep mitigation separate from the evidence required to close." },
      { "id": "escalate-and-communicate", "label": "Escalation and communication", "focus": ["declare", "escalate", "update", "rollback"], "note": "See who is paged, what stakeholders hear, and when rollback begins." }
    ]
  },
  "lanes": [
    { "id": "signals", "label": "Signals" },
    { "id": "responders", "label": "Incident Command" },
    { "id": "mitigation", "label": "Service Mitigation" },
    { "id": "recovery", "label": "Recovery Evidence" },
    { "id": "communication", "label": "Stakeholder Communication" },
    { "id": "exceptions", "label": "Escalation + Rollback", "variant": "exception" }
  ],
  "phases": [
    { "id": "detect", "label": "Detect", "fromCol": 0, "toCol": 1 },
    { "id": "respond", "label": "Triage + mitigate", "fromCol": 2, "toCol": 3, "variant": "emphasis" },
    { "id": "recover", "label": "Verify + close", "fromCol": 4, "toCol": 5, "variant": "dashed" }
  ],
  "groups": [
    { "id": "command", "label": "Incident command", "lane": "responders", "fromCol": 1, "toCol": 3, "variant": "emphasis" },
    { "id": "exception_actions", "label": "If impact persists", "lane": "exceptions", "fromCol": 3, "toCol": 5, "variant": "security" }
  ],
  "mainPath": ["alert", "page", "triage", "contain", "recover", "verify", "close"],
  "nodes": [
    { "id": "alert", "lane": "signals", "col": 0, "type": "messagebus", "label": "SLO Alert", "sublabel": "burn rate" },
    { "id": "page", "lane": "responders", "col": 1, "width": 76, "type": "external", "label": "Page On-call", "sublabel": "acknowledge" },
    { "id": "triage", "lane": "responders", "col": 2, "width": 64, "type": "backend", "label": "Triage", "sublabel": "scope impact" },
    { "id": "declare", "lane": "responders", "col": 3, "type": "security", "label": "Declare", "sublabel": "assign commander", "tag": "SEV-1/2" },
    { "id": "contain", "lane": "mitigation", "col": 3, "width": 72, "type": "backend", "label": "Contain", "sublabel": "stop growth" },
    { "id": "recover", "lane": "mitigation", "col": 4, "width": 52, "type": "cloud", "label": "Recover", "sublabel": "restore" },
    { "id": "verify", "lane": "recovery", "col": 5, "type": "database", "label": "Verify", "sublabel": "SLO + traces", "tag": "15 min stable" },
    { "id": "close", "lane": "communication", "col": 5, "type": "external", "label": "Resolve", "sublabel": "final update" },
    { "id": "update", "lane": "communication", "col": 3, "type": "frontend", "label": "Status Update", "sublabel": "impact + ETA" },
    { "id": "escalate", "lane": "exceptions", "col": 3, "width": 72, "type": "security", "label": "Escalate", "sublabel": "specialist" },
    { "id": "rollback", "lane": "exceptions", "col": 5, "type": "messagebus", "label": "Rollback", "sublabel": "last good" }
  ],
  "edges": [
    { "from": "alert", "to": "page", "label": "page", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "page", "to": "triage", "route": "bottom-channel", "fromSide": "bottom", "toSide": "bottom" },
    { "from": "triage", "to": "contain", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "contain", "to": "recover", "route": "bottom-channel", "fromSide": "bottom", "toSide": "bottom" },
    { "from": "recover", "to": "verify", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "verify", "to": "close", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "triage", "to": "declare", "variant": "security" },
    { "from": "declare", "to": "update", "variant": "dashed", "fromSide": "top", "toSide": "left", "via": [[430, 16], [20, 16], [20, 615]] },
    { "from": "update", "to": "escalate", "variant": "security", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "verify", "to": "rollback", "variant": "security", "role": "error", "route": "outside-right", "fromSide": "right", "toSide": "right" }
  ],
  "cards": [
    { "dot": "rose", "title": "Ownership First", "items": ["A page is not an incident until someone owns command", "Severity and scope are explicit before mitigation spreads", "Escalation names the missing expertise"] },
    { "dot": "emerald", "title": "Recovery Is Evidence", "items": ["Mitigation can reduce impact without proving recovery", "SLOs and traces must stay healthy for a fixed window", "The final update follows verification, not optimism"] },
    { "dot": "cyan", "title": "Communication Contract", "items": ["Stakeholders receive impact, action, and next update time", "Rollback remains visible as a deliberate response", "Every branch has an owner and observable exit"] }
  ]
}
````

## File: archify/examples/product-analytics.dataflow.json
````json
{
  "schema_version": 1,
  "diagram_type": "dataflow",
  "meta": {
    "title": "Product Analytics Data Flow",
    "output": "examples/dataflow-product-analytics.html",
    "viewBox": [1080, 520],
    "animation": "trace",
    "quality_profile": "showcase",
    "views": [
      { "id": "collection-path", "label": "Collection path", "focus": ["web", "mobile", "edge", "stream"], "note": "Follow product events from clients into the ordered event stream." },
      { "id": "consent-boundary", "label": "Consent and PII", "focus": ["edge", "consent", "pii"], "note": "Isolate the policy gate and restricted identity store." },
      { "id": "analytics-consumers", "label": "Curated consumers", "focus": ["stream", "warehouse", "dashboard", "features", "model"], "note": "See curated facts, dashboards, and the derived feature path." }
    ]
  },
  "stages": [
    { "label": "Sources" },
    { "label": "Ingest" },
    { "label": "Process" },
    { "label": "Store" },
    { "label": "Consume" }
  ],
  "nodes": [
    { "id": "web", "type": "frontend", "label": "Web App", "sublabel": "browser SDK", "stage": 0, "row": 0, "tag": "events" },
    { "id": "mobile", "type": "frontend", "label": "Mobile", "sublabel": "iOS / Android", "stage": 0, "row": 2, "tag": "events" },
    { "id": "edge", "type": "cloud", "label": "Edge API", "sublabel": "collector", "stage": 1, "row": 1, "tag": "TLS" },
    { "id": "consent", "type": "security", "label": "Consent Gate", "sublabel": "policy filter", "stage": 2, "row": 0, "tag": "PII guard" },
    { "id": "stream", "type": "messagebus", "label": "Event Stream", "sublabel": "Kafka topic", "stage": 2, "row": 2, "tag": "ordered" },
    { "id": "pii", "type": "security", "label": "PII Vault", "sublabel": "encrypted", "stage": 3, "row": 0, "tag": "restricted" },
    { "id": "warehouse", "type": "database", "label": "Warehouse", "sublabel": "analytics tables", "stage": 3, "row": 1, "tag": "curated" },
    { "id": "features", "type": "database", "label": "Feature Store", "sublabel": "daily batch", "stage": 3, "row": 2, "tag": "derived" },
    { "id": "dashboard", "type": "backend", "label": "Dashboards", "sublabel": "product metrics", "stage": 4, "row": 0, "tag": "SQL" },
    { "id": "model", "type": "backend", "label": "ML Model", "sublabel": "ranking job", "stage": 4, "row": 2, "tag": "features" }
  ],
  "flows": [
    { "id": "web-clickstream", "from": "web", "to": "edge", "label": "clickstream", "classification": "user events", "variant": "emphasis", "fromSide": "right", "toSide": "left", "via": [[205, 157], [205, 271]], "labelAt": [204, 190] },
    { "id": "mobile-events", "from": "mobile", "to": "edge", "label": "app events", "classification": "device events", "variant": "default", "fromSide": "right", "toSide": "left", "via": [[222, 385], [222, 271]], "labelAt": [220, 342] },
    { "id": "consent-enrichment", "from": "edge", "to": "consent", "label": "identity + consent", "classification": "PII touch", "variant": "security", "fromSide": "top", "toSide": "left", "via": [[315, 112], [450, 112], [450, 157]], "labelAt": [382, 100] },
    { "id": "accepted-events", "from": "edge", "to": "stream", "label": "accepted events", "classification": "append-only", "variant": "emphasis", "fromSide": "right", "toSide": "left", "via": [[420, 271], [420, 385]], "labelAt": [438, 324] },
    { "id": "identity-map", "from": "consent", "to": "pii", "label": "identity map", "classification": "encrypted PII", "variant": "security", "route": "straight", "labelAt": [638, 144] },
    { "id": "normalized-facts", "from": "stream", "to": "warehouse", "label": "normalized facts", "classification": "non-PII", "variant": "emphasis", "fromSide": "right", "toSide": "left", "via": [[638, 385], [638, 271]], "labelAt": [638, 326] },
    { "id": "daily-aggregates", "from": "warehouse", "to": "features", "label": "daily aggregates", "classification": "batch", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "route": "straight", "labelAt": [745, 326] },
    { "id": "metrics-query", "from": "warehouse", "to": "dashboard", "label": "metrics SQL", "classification": "read-only", "variant": "default", "fromSide": "right", "toSide": "bottom", "via": [[852, 271], [960, 271]], "labelAt": [876, 258] },
    { "id": "feature-vectors", "from": "features", "to": "model", "label": "feature vectors", "classification": "derived", "variant": "dashed", "route": "straight", "labelAt": [852, 372] },
    { "id": "restricted-join", "from": "pii", "to": "dashboard", "label": "restricted join", "classification": "approved only", "variant": "security", "route": "straight", "labelAt": [852, 144] }
  ],
  "cards": [
    {
      "dot": "emerald",
      "title": "Primary Data Path",
      "items": [
        "Events move left to right through source, ingest, process, store, and consume stages",
        "The hot path stays visually clear even with secondary batch flows",
        "Labels name data assets instead of generic API verbs"
      ]
    },
    {
      "dot": "rose",
      "title": "Sensitive Boundary",
      "items": [
        "Consent and PII paths are styled as security flows",
        "PII lands in a restricted vault, separate from the analytics warehouse",
        "Restricted joins are visible without implying default access"
      ]
    },
    {
      "dot": "orange",
      "title": "Derived Consumers",
      "items": [
        "Dashboards read curated facts from the warehouse",
        "Feature vectors are derived by batch from analytics tables",
        "Consumption paths stay distinct from collection and consent handling"
      ]
    }
  ]
}
````

## File: archify/examples/production-deployment.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Production Deployment Ownership",
    "output": "examples/production-deployment.html",
    "visual_preset": "blueprint",
    "animation": "trace",
    "quality_profile": "showcase",
    "engineering_profile": "deployment-ownership",
    "views": [
      {
        "id": "request-boundary",
        "label": "Request crosses the edge",
        "focus": ["clients", "edge", "gateway", "api_a", "api_b"],
        "note": "Follow public traffic into the private application network."
      },
      {
        "id": "state-ownership",
        "label": "State and ownership",
        "focus": ["api_a", "api_b", "redis", "postgres", "replica"],
        "note": "Separate stateless platform workloads from data-team-owned state."
      },
      {
        "id": "async-operations",
        "label": "Async and operations",
        "focus": ["api_b", "events", "worker", "audit", "observability"],
        "note": "See the asynchronous work and the evidence it emits."
      }
    ]
  },
  "components": [
    { "id": "clients", "type": "external", "label": "Customers", "sublabel": "web + mobile", "pos": [38, 300], "size": [122, 60] },
    { "id": "edge", "type": "cloud", "label": "Global Edge", "sublabel": "CDN + WAF", "pos": [230, 300], "size": [126, 60], "tag": "edge team" },
    { "id": "gateway", "type": "security", "label": "API Gateway", "sublabel": "public :443", "pos": [430, 300], "size": [128, 60], "tag": "platform" },
    { "id": "api_a", "type": "backend", "label": "API Pods / AZ-a", "sublabel": "private subnet", "pos": [630, 195], "size": [136, 62], "tag": "app team" },
    { "id": "api_b", "type": "backend", "label": "API Pods / AZ-b", "sublabel": "private subnet", "pos": [630, 405], "size": [136, 62], "tag": "app team" },
    { "id": "redis", "type": "database", "label": "Redis", "sublabel": "multi-AZ cache", "pos": [840, 195], "size": [126, 62], "tag": "platform" },
    { "id": "postgres", "type": "database", "label": "PostgreSQL", "sublabel": "primary / encrypted", "pos": [840, 405], "size": [126, 62], "tag": "data team" },
    { "id": "events", "type": "messagebus", "label": "Event Bus", "sublabel": "orders.v1", "pos": [1040, 300], "size": [126, 60], "tag": "platform" },
    { "id": "worker", "type": "backend", "label": "Workers", "sublabel": "private workload", "pos": [1190, 300], "size": [126, 60], "tag": "app team" },
    { "id": "replica", "type": "database", "label": "DR Replica", "sublabel": "eu-west-1", "pos": [1040, 578], "size": [126, 62], "tag": "data team" },
    { "id": "audit", "type": "cloud", "label": "Audit Archive", "sublabel": "immutable objects", "pos": [1190, 450], "size": [126, 62], "tag": "security" },
    { "id": "observability", "type": "external", "label": "Observability", "sublabel": "metrics + traces", "pos": [1190, 85], "size": [126, 62], "tag": "SRE" }
  ],
  "boundaries": [
    { "kind": "region", "label": "AWS us-east-1 / production", "wraps": ["edge", "gateway", "api_a", "api_b", "redis", "postgres", "events", "worker", "audit"], "pad": 20 },
    { "kind": "security-group", "label": "private application network", "wraps": ["api_a", "api_b", "redis", "postgres", "events", "worker"], "pad": 14 },
    { "kind": "region", "label": "AWS eu-west-1 / disaster recovery", "wraps": ["replica"] },
    { "kind": "security-group", "label": "DR private subnet", "wraps": ["replica"], "pad": 14 }
  ],
  "connections": [
    { "from": "clients", "to": "edge", "label": "HTTPS", "variant": "emphasis" },
    { "from": "edge", "to": "gateway", "label": "mTLS", "variant": "security" },
    { "from": "gateway", "to": "api_a", "label": "VPC route", "variant": "emphasis", "route": "orthogonal-h", "labelAt": [594, 275] },
    { "from": "gateway", "to": "api_b", "label": "VPC route", "variant": "emphasis", "route": "orthogonal-h", "labelAt": [594, 385] },
    { "from": "api_a", "to": "redis", "label": "cache", "route": "straight" },
    { "from": "api_b", "to": "postgres", "label": "SQL", "route": "straight" },
    { "from": "api_a", "to": "events", "label": "publish", "variant": "dashed", "fromSide": "top", "toSide": "top", "via": [[698, 170], [1103, 170]] },
    { "from": "api_b", "to": "events", "variant": "dashed", "fromSide": "top", "toSide": "bottom", "via": [[698, 380], [1103, 380]] },
    { "from": "events", "to": "worker", "variant": "emphasis" },
    { "from": "postgres", "to": "replica", "label": "cross-region WAL", "variant": "security", "route": "orthogonal-v", "labelAt": [1003, 529] },
    { "from": "worker", "to": "audit", "label": "evidence", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "labelDy": 58 },
    { "from": "worker", "to": "observability", "label": "OTLP", "variant": "dashed", "route": "orthogonal-v" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Runtime Ownership", "items": ["Platform owns the edge, gateway, cache, and event bus", "Application teams own API pods and workers", "Data owns primary and disaster-recovery state"] },
    { "dot": "rose", "title": "Named Crossings", "items": ["Public HTTPS terminates at the managed edge", "mTLS crosses into the application network", "Cross-region WAL is explicit and encrypted"] },
    { "dot": "emerald", "title": "Operational Evidence", "items": ["Workers emit traces to SRE-owned observability", "Audit evidence lands in immutable storage", "Unknown placement should remain marked, never invented"] }
  ]
}
````

## File: archify/examples/release-delivery.workflow.json
````json
{
  "schema_version": 1,
  "diagram_type": "workflow",
  "meta": {
    "title": "Release Delivery Workflow",
    "output": "examples/release-delivery.html",
    "animation": "trace",
    "quality_profile": "showcase",
    "views": [
      { "id": "commit-to-checks", "label": "Commit to green build", "focus": ["commit", "pull_request", "build", "checks"], "note": "Follow the change through reproducible build and blocking quality gates." },
      { "id": "approval-to-production", "label": "Approve and promote", "focus": ["checks", "approval", "deploy", "verify_prod", "announce"], "note": "See who authorizes production and how success is verified." },
      { "id": "rollback-path", "label": "Failure and rollback", "focus": ["checks", "failed", "verify_prod", "rollback", "deploy"], "note": "Isolate the two places where delivery stops or reverses safely." }
    ]
  },
  "lanes": [
    { "id": "dev", "label": "Developer" },
    { "id": "ci", "label": "Continuous Integration" },
    { "id": "approval", "label": "Release Governance" },
    { "id": "environment", "label": "Production Environment" },
    { "id": "communication", "label": "Release Communication" },
    { "id": "exceptions", "label": "Failure + Rollback", "variant": "exception" }
  ],
  "phases": [
    { "id": "change", "label": "Change", "fromCol": 0, "toCol": 1 },
    { "id": "verify", "label": "Build + verify", "fromCol": 2, "toCol": 3, "variant": "emphasis" },
    { "id": "promote", "label": "Promote + observe", "fromCol": 4, "toCol": 5, "variant": "dashed" }
  ],
  "groups": [
    { "id": "blocking_checks", "label": "Blocking checks", "lane": "ci", "fromCol": 2, "toCol": 3, "variant": "emphasis" },
    { "id": "rollback_work", "label": "Recovery path", "lane": "exceptions", "fromCol": 3, "toCol": 5, "variant": "security" }
  ],
  "mainPath": ["commit", "pull_request", "build", "checks", "approval", "deploy", "verify_prod", "announce"],
  "nodes": [
    { "id": "commit", "lane": "dev", "col": 0, "type": "frontend", "label": "Commit", "sublabel": "signed change" },
    { "id": "pull_request", "lane": "dev", "col": 1, "type": "frontend", "label": "Pull Request", "sublabel": "reviewed diff" },
    { "id": "build", "lane": "ci", "col": 2, "type": "backend", "label": "Build", "sublabel": "locked inputs", "tag": "reproducible" },
    { "id": "checks", "lane": "ci", "col": 3, "type": "security", "label": "Quality Gates", "sublabel": "test + scan", "tag": "blocking" },
    { "id": "approval", "lane": "approval", "col": 4, "type": "security", "label": "Approve", "sublabel": "release owner", "tag": "human gate" },
    { "id": "deploy", "lane": "environment", "col": 4, "type": "cloud", "label": "Deploy", "sublabel": "canary 10%", "tag": "production" },
    { "id": "verify_prod", "lane": "environment", "col": 5, "type": "backend", "label": "Verify", "sublabel": "smoke + SLO" },
    { "id": "announce", "lane": "communication", "col": 5, "type": "external", "label": "Announce", "sublabel": "status + notes" },
    { "id": "failed", "lane": "exceptions", "col": 2, "type": "security", "label": "Stop Release", "sublabel": "gate failed" },
    { "id": "rollback", "lane": "exceptions", "col": 4, "width": 64, "type": "messagebus", "label": "Rollback", "sublabel": "last good image", "tag": "owner: on-call" }
  ],
  "edges": [
    { "from": "commit", "to": "pull_request" },
    { "from": "pull_request", "to": "build", "label": "merge", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "build", "to": "checks" },
    { "from": "checks", "to": "approval", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "approval", "to": "deploy", "variant": "security", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "deploy", "to": "verify_prod" },
    { "from": "verify_prod", "to": "announce", "label": "healthy", "variant": "emphasis", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "checks", "to": "failed", "label": "red", "variant": "security", "role": "error", "route": "drop", "fromSide": "bottom", "toSide": "top" },
    { "from": "verify_prod", "to": "rollback", "variant": "security", "role": "error", "route": "outside-right", "fromSide": "right", "toSide": "right" },
    { "from": "rollback", "to": "deploy", "label": "restore", "variant": "dashed", "role": "return", "route": "return-left", "fromSide": "left", "toSide": "left" }
  ],
  "cards": [
    { "dot": "emerald", "title": "One Happy Path", "items": ["Every change is reviewed before a reproducible build", "Blocking checks must be green before human approval", "Production is complete only after smoke and SLO verification"] },
    { "dot": "rose", "title": "Stop Conditions", "items": ["Test or security failure stops promotion", "Production health can reverse a release", "Rollback ownership is visible before an incident"] },
    { "dot": "cyan", "title": "Release Evidence", "items": ["Approval, immutable image, and check results are retained", "The release announcement follows verification", "The main path remains readable without hiding failure"] }
  ]
}
````

## File: archify/examples/web-app.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Sample Web App",
    "output": "web-app-rendered.html",
    "quality_profile": "showcase",
    "views": [
      { "id": "request-path", "label": "Primary request path", "focus": ["users", "cdn", "lb", "api", "db"], "note": "Follow the primary customer request from the edge to durable state." },
      { "id": "identity-and-cache", "label": "Identity and cache", "focus": ["auth", "api", "cache"], "note": "Isolate authentication and the read-through cache beside the request path." },
      { "id": "async-work", "label": "Static and async work", "focus": ["cdn", "s3", "api", "queue", "worker"], "note": "See the two secondary paths without adding noise to the main request." }
    ]
  },
  "components": [
    { "id": "users", "type": "external", "label": "Users", "sublabel": "Browser / Mobile", "pos": [40, 300], "size": [120, 60] },
    { "id": "auth", "type": "security", "label": "Auth Provider", "sublabel": "OAuth 2.0", "pos": [40, 110], "size": [120, 64], "tag": "JWT + PKCE" },
    { "id": "cdn", "type": "cloud", "label": "CloudFront", "sublabel": "CDN", "pos": [250, 300], "size": [130, 60] },
    { "id": "lb", "type": "cloud", "label": "Load Balancer", "sublabel": "HTTPS :443", "pos": [460, 300], "size": [130, 60] },
    { "id": "api", "type": "backend", "label": "API Server", "sublabel": "FastAPI :8000", "pos": [670, 300], "size": [130, 60] },
    { "id": "cache", "type": "database", "label": "Redis", "sublabel": "cache :6379", "pos": [670, 150], "size": [130, 60] },
    { "id": "db", "type": "database", "label": "PostgreSQL", "sublabel": "primary :5432", "pos": [880, 300], "size": [130, 60] },
    { "id": "s3", "type": "cloud", "label": "S3", "sublabel": "static assets", "pos": [250, 440], "size": [130, 60], "tag": "OAI protected" },
    { "id": "queue", "type": "messagebus", "label": "SQS", "sublabel": "job queue", "pos": [670, 440], "size": [130, 60] },
    { "id": "worker", "type": "backend", "label": "Worker", "sublabel": "async jobs", "pos": [880, 440], "size": [130, 60] }
  ],
  "boundaries": [
    { "kind": "region", "label": "AWS Region: us-west-2", "wraps": ["cdn", "lb", "api", "cache", "db", "s3", "queue", "worker"] },
    { "kind": "security-group", "label": "sg-api :443/:8000", "wraps": ["lb", "api"] }
  ],
  "connections": [
    { "id": "users-to-cdn", "from": "users", "to": "cdn", "label": "HTTPS", "variant": "emphasis" },
    { "id": "jwt-verification", "from": "auth", "to": "api", "label": "verify JWT", "variant": "security", "fromSide": "right", "toSide": "top", "via": [[620, 142], [620, 246], [735, 246]] },
    { "id": "cdn-to-lb", "from": "cdn", "to": "lb" },
    { "id": "static-assets", "from": "cdn", "to": "s3", "label": "static", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "labelDy": 58 },
    { "id": "lb-to-api", "from": "lb", "to": "api" },
    { "id": "cache-read-through", "from": "api", "to": "cache", "label": "read-through", "fromSide": "top", "toSide": "bottom", "labelDy": -68 },
    { "id": "api-sql", "from": "api", "to": "db", "label": "SQL" },
    { "id": "enqueue-job", "from": "api", "to": "queue", "label": "enqueue", "variant": "dashed", "fromSide": "bottom", "toSide": "top", "labelDy": 58 },
    { "id": "queue-to-worker", "from": "queue", "to": "worker" }
  ],
  "cards": [
    { "dot": "cyan", "title": "Edge", "items": ["CloudFront CDN fronts all traffic", "S3 serves static assets via OAI"] },
    { "dot": "emerald", "title": "Application", "items": ["FastAPI behind an HTTPS load balancer", "Redis read-through cache", "Async work drained from SQS by a worker"] },
    { "dot": "rose", "title": "Security", "items": ["OAuth 2.0 with JWT + PKCE", "API + LB isolated in a security group"] }
  ]
}
````

## File: archify/recipes/scenarios.mjs
````javascript
export function detectGuideLanguage(value = '')
⋮----
export function startPromptsFor(recipe, lang = 'en')
⋮----
function normalized(value)
⋮----
function localized(recipe, lang)
⋮----
export function listScenarioRecipes(lang = 'en')
⋮----
function scoreRecipe(recipe, query)
⋮----
export function recommendScenario(query, options =
⋮----
export function formatScenarioList(lang = 'en')
⋮----
export function formatScenarioRecommendation(result)
⋮----
export function publicGuideData()
````

## File: archify/references/authoring-contract.md
````markdown
# Authoring contract

Read this reference only after the Fast authoring path calls for more detail. The schemas and examples remain authoritative.

## Schema lookup

Read both the mode schema and `schemas/common.schema.json`. The mode schemas use `$ref`, so the common file is where shared enums live.

- `componentType`: `frontend`, `backend`, `database`, `cloud`, `security`, `messagebus`, `external`
- `variant`: `default`, `emphasis`, `security`, `dashed`
- Relationship IDs use the shared identifier pattern and must be unique in their collection.

Do not invent fields. Use the nearest matching example for structure, then author fresh IDs, wording, facts, and layout.

## Workflow layout contracts

Use schema v2 for new workflows and keep schema v1 when an existing source must
retain fixed geometry. In both versions, `col` stays in `0..5` and semantic
edge labels are never deleted as a spacing repair. Do not change only
`schema_version` when absolute coordinates exist: follow the canonical
[migration and layout-receipt contract](../renderers/workflow/README.md#migration-and-layout-receipt).
The complete normative invariants live in the workflow renderer's
[layout contracts](../renderers/workflow/README.md#layout-contracts).

## Legend contract

Omit `meta.legend` for the truthful default: `auto` lists only semantic kinds
present in typed IR. Use `mode: "all"` for a renderer reference or
`mode: "hidden"` to remove the full legend. Under `entries`, only keys listed
by the selected mode schema are valid; each key accepts `label`, `visible`, or
both. `visible: true` may show an unused supported convention, while
`visible: false` hides it. `hidden` cannot be overridden.

A label override changes reader wording only. Never infer a kind from prose or
use the legend to compensate for missing nodes, states, messages, or flows.
Long labels are measured and wrap into deterministic rows. Architecture's
implicit automatic viewBox grows from that same measured footprint. For
backwards compatibility, a legacy document with no `meta.legend` may omit an
implicit auto legend that cannot fit its explicit viewBox; this never changes
its typed topology. Adding `meta.legend` makes the presentation intentional and
strict: if its resolved labels cannot fit the authored viewBox, shorten or hide
them, or widen the viewBox using the emitted diagnostic.

## Language consistency

Choose one primary authored language. An explicit user choice wins; otherwise
use the language of the request, or the conversation's dominant language when
the request itself is language-neutral. Separately choose the Viewer locale.
For supported languages, always write the matching `meta.locale`: `"en"` for
English or `"zh-CN"` for Simplified Chinese. The renderer consumes the authored
locale without inferring language from diagram strings. Documents that omit it
remain valid and default to English.

`meta.locale` controls only renderer-owned reader surfaces: `<html lang>`, the
document-title suffix, default SVG description and focus labels, default legend
labels, and fixed Viewer controls, statuses, accessibility names, and errors.
It never translates authored content. Apply the primary language separately to
titles, subtitles, node and relationship copy, boundaries, lanes, groups,
guided views, legend label overrides, and cards. A bilingual diagram still
chooses one primary locale for the Viewer; follow an explicit primary-language
request, then prompt order or conversation dominance.

For a requested language outside `en` and `zh-CN`, do not write an unsupported
locale. Keep every reader-facing authored string in the requested language,
omit `meta.locale` so the renderer safely uses English, and explicitly tell the
user that fixed Viewer UI and `<html lang>` remain English and the artifact is
not fully localized. The fallback applies only to renderer-owned surfaces; it
never permits authored copy to fall back to English. Do not silently substitute
`zh-CN` for another language or Chinese locale.

Keep exact product names, code identifiers, commands, protocols, API paths, and
environment names intact. Those terms may remain English inside localized copy,
but surrounding explanatory prose must still use the selected language.
Renderer-owned default legend labels follow `meta.locale`; author a
`meta.legend.entries.*.label` override only when the diagram needs different
domain wording, and keep that authored override in the primary language.

## Visual preset default

Omit `meta.visual_preset` by default. The renderer then opens the diagram in
`classic` for both light and dark color modes. Color mode and visual preset are
independent viewer state: switching Light / Dark must preserve the current
preset. Author `signal-flow`, `blueprint`, or `editorial` only when the user
explicitly requests that visual style.

## Engineering profile default

Omit `meta.engineering_profile` for an ordinary system architecture. Region,
cluster, and security boundary wording do not by themselves enable an
engineering profile. Enable `deployment-ownership` only when the user
explicitly asks for a production deployment topology, ownership handoff, or
fail-closed deployment review and the source facts are known. Once enabled,
do not remove the engineering profile merely to pass validation; repair the
authored facts or report the diagnostics truthfully.

## Title hierarchy

Use one concise title and let the diagram carry the explanation. Omit
`meta.subtitle` by default, and never use it to restate the title, nodes, edges,
or cards. Include one short supporting line only when the user explicitly asks
for a subtitle; an omitted or blank subtitle must not leave an empty visual row
in the generated viewer.

## Executable geometry rules

- Node anchors start at side midpoints. `left`/`right` change the horizontal endpoint; `top`/`bottom` change the vertical endpoint. For an automatic Architecture relationship, unobstructed facing ports whose axis offset is under 16px may share one horizontal or vertical axis when both endpoints retain the 16px corner gutter. If exactly one endpoint belongs to a spread group, only its unshared counterpart moves; relationships spread at both endpoints keep their distinct ports and outside bridge.
- A side is a direction contract. The first and final route segment must be perpendicular and outward/inward in the named direction.
- Automatic Port Spread is a default renderer behavior for architecture, workflow, data-flow, and lifecycle diagrams. Shared automatic endpoints spread deterministically and symmetrically with a 16px corner gutter. It does not apply to sequence messages, single relationships, or explicit `via`, `channelX`, `channelY`, `labelAt`, or non-`auto` routes.
- Showcase route rhythm: every nonzero segment must be at least 8px; every interior segment must be at least 16px. When spread ports are nearly parallel, the router uses a 24px endpoint stub and a 16px outside bridge instead of manufacturing a tiny dogleg.
- Shared endpoint corridors are allowed only when they remain semantically unambiguous. Unrelated collinear overlap of 8px or more fails showcase.
- Container borders are intentional pass-through geometry, but a long edge running along a structural border is not.
- An edge crossing an unrelated opaque node is always a hard failure, independent of quality profile.

### Spacing and labels

Spacing recommendations mean clear gap between boxes, not center distance. A 200px center distance between 165px-wide nodes leaves only 35px of clear gap.

For a relationship label, require:

```text
clear gap > label mask width + 8px breathing room
label mask width ≈ 6.5px × ASCII units + 13px
CJK characters count as two units
```

Relationship labels are semantic data. If the gap is too small, move the label,
adjust the route or spacing, then shorten the wording while preserving meaning.
Omit only wording already fully implied by both endpoints and carrying no
protocol, action, direction, synchronous/asynchronous behavior, or
cross-boundary mechanism. Preserve every meaningful label.
Deleting it is not a spacing repair. If a relationship starts unlabeled because
its endpoints fully imply it, explain why the wording is redundant; this is a
semantic authoring choice, not a spacing repair. In workflow v2, let the compiler
allocate its measured mask before applying a diagnosed `labelAt`,
`labelDx`/`labelDy`, or `labelSegment`. Apply one diagnosed geometry control at
a time.

### Repair order

1. Fix missing/invalid `meta.quality_profile` and schema errors.
2. Fix node overlap or out-of-range placement.
3. Fix edge-through-node and endpoint-direction errors.
4. Fix crossings, ambiguous corridors, border runs, and route rhythm.
5. Fix label-to-node, label-to-label, then label-to-route clearance.

Run `validate` after every edit. Consume `diagnostics[]` by stable `code`, exact `subject`, measured `evidence`, and `supportedFixes`. If the diagnostic gives `labelAt`, use that point instead of estimating another offset.

## Mode placement

### Architecture

Use one left-to-right spine with short vertical branches. Prefer 6–12 primary components and group only real ownership, trust, process, or deployment boundaries. Boundaries do not replace relationships.

Grid placement is preferred when the schema supports it. Free positions are appropriate for a bounded exception, not for prose-level coordinate planning. Keep external actors outside the system boundary when that is factually true.

### Workflow

Lanes express responsibility or phase. Columns `0..5` express logical
progression. Start new workflows on `readable-v2`; retain `fixed-v1` only for
legacy geometry compatibility. Keep the happy path monotonic, preserve semantic
edge labels, and route retries and exception returns outside the main lane
corridor.

### Sequence

Participants are ordered by conversation role. Messages own their vertical order. Use return/async/security variants for meaning, not decoration; sequence does not use Automatic Port Spread.

### Dataflow

Stages express transformation or custody. Rows separate parallel streams. Label only data contracts, classifications, or cross-boundary movement that is not obvious.

### Lifecycle

Main phases use columns `0..4`; event and terminal bands use columns `0..2`.
Event/terminal column `N` aligns to the same x coordinate as main column
`N + 2`. A recoverable failure needs a real transition back to an active state.
A card or guided view saying “retry” is not topology.

## Repository evidence

When an architecture diagram must reflect real code, inspect repository
entrypoints, runtime boundaries, storage, transports, and deployment
configuration before authoring. Record only evidence you actually verified.
`--repo-root <path>` is architecture-only and is accepted by architecture
`render`, `validate`, `deliver`, `preview`, and `compare`; workflow, sequence,
dataflow, and lifecycle reject it. Never infer runtime causality from file
proximity or naming alone.

Declare `meta.repository.url` and one full 40-character `revision`, then attach
`components[].sources` with repository-relative `path`, optional `line`,
`end_line`, and `label`. Verification reads blobs at that commit, independently
of working-tree edits. A matching local origin, available commit, bounded path,
blob, and valid line range are required in every link mode. Verification is
local and makes no remote requests; it establishes neither public availability
nor the current reader's access rights.

`link_mode` defaults to `web`. GitHub and Gitee HTTPS repository URLs generate
revision-pinned links; their public hosts select the provider automatically.
Optional `provider: "github"` or `"gitee"` must agree with the host. Existing
GitHub declarations and default delivery receipt fields remain compatible.

```json
{
  "url": "https://gitee.com/team/service",
  "revision": "0123456789abcdef0123456789abcdef01234567",
  "provider": "gitee"
}
```

For an internal or unsupported forge, select `link_mode: "local-only"`. The
Viewer retains SRC markers, searchable file paths, line ranges, and revision
labels without repository or source hyperlinks. The evidence receipt adds
`linkMode: "local-only"`. `url` remains required as the expected origin identity;
local-only disables links, not identity verification. A repository without an
origin is not supported.

```json
{
  "url": "http://git.internal:3000/Platform/Services/service",
  "revision": "0123456789abcdef0123456789abcdef01234567",
  "link_mode": "local-only"
}
```

Local-only accepts HTTP(S), `git@host:path`, and `ssh://git@host[:port]/path`
addresses, including nested namespaces. Declare a credential-free address;
HTTP(S) credentials on the checkout's origin are ignored for identity and
redacted from diagnostics. Hostnames compare case-insensitively; repository
paths retain case except for the existing GitHub behavior. A trailing slash
normalizes away. Only GitHub and Gitee normalize a terminal `.git` and match
standard HTTPS/443 with Git SSH/22. For other hosts, use the actual clone address:
transport, port, `.git` suffix, and remote-relative versus absolute paths must
match. For example, `git@host:Team/repo` differs from
`ssh://git@host/Team/repo`; `git@host:/Team/repo` matches the latter. SCP-style
paths preserve literal percent escapes, while URI paths decode them. SSH host
aliases and forge-specific browse/clone prefixes are not guessed.
GitLab/Gitea/Forgejo/Bitbucket web links are not implemented in this version;
use local-only until a tested link provider is available. Unknown web providers
fail with a diagnostic rather than emitting a guessed link.

## Hand-placed fallback

Use only when no renderer can run. Start from `assets/template.html`, keep semantic CSS classes, preserve the inline SVG/accessibility structure, and run the delivery visual checklist. Never introduce inline literal colors that break dark/light parity.
````

## File: archify/references/brand-marks.md
````markdown
# Brand marks

Use a brand mark only when a real product, provider, model family, channel, or
service identity helps the reader. Semantic `type` still explains what the node
does; `brand` explains whose product it is.

## Agent decision path

1. Search the built-in catalogue when the request names a recognizable brand:

   ```bash
   node bin/archify.mjs brands "Claude" --json
   ```

2. Put the returned canonical ID in the node, participant, or state:

   ```json
   {
     "id": "planner",
     "type": "backend",
     "label": "Claude",
     "brand": "claude"
   }
   ```

3. If there is no catalogue match and the user supplied the official website,
   capture its icon explicitly:

   ```bash
   node bin/archify.mjs brands capture "https://partner.example.com" --json
   ```

   Put the command's digest-pinned `brand` value in the authored node:

   ```json
   {
     "id": "partner",
     "type": "external",
     "label": "Partner portal",
     "brand": {
       "url": "https://partner.example.com",
       "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
     }
   }
   ```

4. If there is no match and no user-provided URL, omit `brand`. Do not invent a
   URL or silently assign a visually similar company.

Known-brand URLs resolve to the bundled vector instead of using the network.
Unknown URL capture accepts only bounded raster image formats, blocks
credentials, nonstandard public ports, and private or link-local destinations,
uses bounded concurrency and one total deadline, and returns the captured
content digest. Later render and validate operations require that exact digest;
blocked, unavailable, changed, oversized, or unsafe content fails closed instead
of silently changing the artifact.

The final artifact never fetches a brand asset when opened. Preset vectors and
digest-verified captured site icons remain embedded in SVG, PNG, WebP, JPEG,
Share Card, and WebM exports.

Use `node bin/archify.mjs brands --json` to inspect all canonical IDs, aliases,
categories, domains, and provenance. Current categories cover AI, cloud,
engineering, data, collaboration, business systems, channels, languages, and
frameworks.
````

## File: archify/references/delivery-contract.md
````markdown
# Delivery contract

## Validate and deliver

Use `validate` after every candidate edit. CLI HTML output paths must end in `.html`, including after symbolic-link resolution.
Compare receipt paths must end in `.json`. Explicit CLI paths may be absolute or
outside the current working directory; authored `meta.output` remains confined
to that directory. A type mismatch fails before writing with
`output/cli-extension` or `output/cli-resolved-extension`. These checks prevent
accidental file-type overwrites; they do not sandbox explicit CLI directories
or prevent replacement of an existing artifact of the expected type.

Use final atomic delivery only after the candidate is frozen:

```bash
node bin/archify.mjs deliver <type> <candidate.json> <output.html> --quality showcase --json
```

Deliver reads the specification once, writes those exact bytes to a private same-directory candidate snapshot, renders that snapshot, runs the complete artifact checker, and only replaces the target after all artifact checks pass. The JSON receipt includes SHA-256 and byte counts for both `specification` and `artifact`. Renderer, checker, receipt, or commit failure exits non-zero, removes private state, preserves the previous trusted artifact, and never invokes an opener.

Run `visual-check` only after `deliver` exits zero for the current candidate. If
delivery fails and the output path already exists, that path still names the
previous trusted artifact; running `visual-check` then would measure and capture
stale output, not the rejected candidate. Report the delivery diagnostics and
repair the source before collecting new visual evidence.

The delivery interface exposes three separate claims:

1. `deliver` proves deterministic artifact checks and byte identity.
2. `visual-check` collects automated browser evidence from the exact artifact.
3. Perceptual visual review records a human or image-capable reviewer's judgment.

Passing one claim never implies either of the others. Never claim that the deterministic receipt includes visual review. It does not include browser evidence either.

## Automated browser evidence

After delivery, inspect the exact trusted HTML without rerendering or modifying
it:

```bash
node bin/archify.mjs visual-check <output.html> --json
```

The zero-dependency command uses Chrome/Chromium through the DevTools pipe. It
measures light-theme containment at 1440×900, 1600×1000, 1920×1080, and
2048×1320, then captures light/dark screenshots at 1440×900 and 2048×1320. It
writes four PNG sidecars, one relative-path HTML contact sheet, and one JSON
receipt beside the artifact. The receipt binds the source artifact SHA-256 and
byte count, identifies `evidenceKind: "automated-browser"`, records READ plus
Still runtime state, and always reports `visualReview: "pending"`; automated
browser evidence cannot claim perceptual review.

`browser_evidence` in the handoff records only the outcome of this automated command:

- `passed` maps from exit 0 and receipt `status: "pass"` only after every required measurement and capture completes and passes.
- `failed` maps from exit 1 and receipt `status: "fail"` when the inspection finds a defect, the command fails, or a runtime/capture error leaves the evidence incomplete.
- `skipped` maps only from exit 2 and receipt `status: "skipped"` when Chrome/Chromium is unavailable and the inspection does not run.

Runtime or capture failures leave incomplete evidence and must not be normalized to `skipped`. Failed or skipped capture runs remove stale
image/contact-sheet sidecars rather than presenting prior evidence as current.
They do not invalidate an already successful deterministic delivery, and they
do not turn a perceptual visual review into passed or failed. Retry an
environmental failure through the supported command in a browser-capable
execution context when practical. Keep the packaged transport unchanged unless
the failure reproduces through that seam in a capable environment.

## Optional opening

Add `--open` only when the user wants an immediate local preview. It runs after that atomic commit, uses one argument-array OS opener with a five-second bound, and records `open.status`. Keep it off for CI, unattended agents, and non-interactive environments. Failure or unsupported opening does not invalidate delivery; its status proves only whether the local opener invocation succeeded.

## Last-Good Live Preview

For an active desktop authoring loop only:

```bash
node bin/archify.mjs preview <type> <input>.json <output>.html --quality showcase
```

Preview watches one explicit input on loopback, binds each stable digest to a private snapshot, and advances only after the existing verified delivery pipeline passes. Invalid, half-written, deleted, or superseded input leaves the previous verified revision on screen and on disk. Identical bytes do not rebuild or reload.

The preview runtime ships inside the zero-dependency Skill ZIP and must work without `node_modules`.

Never start it by default. Do not use it for CI, unattended agents, remote sharing, or mobile use. `--no-open` is only for a user who will open the printed local URL or for loop testing. Stop it with Ctrl-C before handoff. Server state, port, source path, diagnostics, error text, and reload tokens must never enter the generated artifact or any export.

## Perceptual delivery gate

Automated validation and browser evidence cannot prove visual polish. After deterministic delivery, inspect the actual HTML in a capable browser or render the evidence screenshots with an image reader. Check both themes when changed, the default READ view, line crossings/corridors, label masks, node/card fit, focus/search/passport closure, and export cleanliness.

For the default standalone desktop viewer, measure 1440×900, 1600×1000, and 1920×1080. When the artifact is intended for a large desktop display, also measure 2048×1320. A first-screen pass requires `document.documentElement.scrollWidth <= window.innerWidth` and `scrollHeight <= window.innerHeight` at every checked size. At the largest checked viewport, inspect the rendered composition for a conspicuous empty lower band: the main panel and necessary conclusion cards should use the available height as a balanced whole, not collapse into a shallow strip. If a desktop viewport overflows, repair the authored composition by removing only genuinely redundant content or compacting spacing before shrinking nodes, labels, or the main panel. Do not hide overflow, clip content, introduce an internal diagram scroller, or reduce node/label typography to make the measurement pass. Narrow/mobile containment may retain vertical page scrolling.

A manual browser record is supplementary to the automated status. Reproducing the same coverage requires all four exact viewport measurements, both endpoint themes, and an artifact-bound record of the inspected SHA-256 and byte count. It never changes `browser_evidence`: when Chrome/Chromium is unavailable, that status remains `skipped` even when the manual browser record is complete and `visual_review: passed`; an automated `failed` result likewise remains `failed`. An unconstrained browser glance can support perceptual review only.

Report exactly one truthful status:

- `visual_review: passed` — only after inspecting the rendered artifact.
- `visual_review: skipped (image reader unavailable)` — when no capable visual surface exists.
- `visual_review: failed` — with the concrete visible defect.

Use `correction_rounds: 0`, `correction_rounds: 1`, or `correction_rounds: 2`; never exceed a maximum of two focused correction rounds. Never report `visual_review: passed` without inspecting the artifact.

If visual review changes the candidate, validation and delivery must run again because the prior frozen specification receipt is no longer current.

## Handoff receipt

Return:

```text
diagram_type: architecture|workflow|sequence|dataflow|lifecycle
output: /absolute/path/to/file.html
specification_sha256: <receipt value>
artifact_sha256: <receipt value>
validation: 9/9 showcase, 0 errors, 0 warnings
browser_evidence: passed|failed|skipped
visual_review: passed|skipped (image reader unavailable)|failed
correction_rounds: 0|1|2
```

Derive `browser_evidence` only from the latest artifact-bound `visual-check` receipt. Record any manual browser work separately with its artifact binding, viewport/theme scope, and observations; never use it or `visual_review` to overwrite the automated status.

Opening, preview status, Share Cards, and other viewer exports are not validation claims.
````

## File: archify/references/viewer-runtime.md
````markdown
# Viewer Runtime reference

Read this only when the user asks for a reader-facing capability. Ordinary generation does not require implementing or re-documenting these features; they are already in the generated HTML.

## Exploration

- Diagram Guide lists current actions and shortcuts.
- Reading Depth starts at READ at the default 100% scale, reveals FULL detail at 175%, and falls back to MAP only below 100%. Focus, story, route, and semantic interactions reveal their exact facts at any scale.
- Semantic Lens summarizes selected node/relationship kinds without changing authored geometry.
- Intent Trace previews a fine-pointer or keyboard target before committed focus.
- Node Finder searches labels and stable IDs.
- Semantic Passport opens on focus, shows authored upstream/downstream facts, supports a copyable deep link, has an explicit close action, closes on true outside activation and Escape, and never enters canonical export.
- Semantic Radar mirrors the visible viewport and authored graph without becoming a second source of truth.
- Direct Relationship Pin makes a unique compiled relationship operable while preserving the authored line and stable relationship identity. It must fail closed on conflicting source/target/label/ID metadata.
- Route Probe resolves exactly two endpoints over authored directed relationships. It never infers a route from geometry.

## Guided views and story

`meta.views` may define at most five curated chapters using stable node IDs. The Named Chapter Rail, Chapter Delta Preview, Story Beat Navigator, Story Follow Camera, Story Director Strip, Story Horizon, and Shareable Story Moment links all derive from that one authored array; none owns parallel topology or layout.

Story transitions classify only the exact relationship between adjacent authored stops: forward, reverse, multiple, or grouped/no direct link. Never infer a transitive edge, verb, causality, or runtime behavior from proximity, kinds, or story order. Playback is reader-started, bounded, stale-safe, and motion-governed.

## Motion and presentation

`meta.animation: "trace"` enables a finite reader-controlled Live/Still trace. Static is the default. Still, reduced motion, page hiding, print, and canonical export preserve complete static meaning. Presentation Stage changes viewer chrome and framing, never authored geometry. This is not a mobile product feature; narrow layouts get containment only.

## Canonical exports

The export menu can copy/download full-diagram PNG, download JPEG/WebP, download a dual-theme SVG, and record a trace-enabled WebM. Viewer state—Guide, Lens, finder, focus, route, story, camera, radar, presentation, motion ownership, and temporary overlays—must be removed from canonical export.

### Share Card

The optional 1200×630 Share Card PNG is for README, release, social, or launch previews. It uses the current theme and visual preset, contains the complete canonical diagram without cropping, and never claims validation. Copy Share Card reuses the same canonical PNG when clipboard image writes are supported.

### Route Share Card

After a real directed Route Probe resolves, the reader may use **Export → Route Share Card**. It reuses the exact ordered route snapshot and the shared Share Card seam: `format=share-card`, `variant=route`. The isolated clone may use only static `data-share-route-*` decoration. It is download-only, fails closed for stale/unreachable/conflicting routes, and never becomes the canonical artifact.

### Reach Share Card

After a non-empty authored reachability query, the reader may use **Export → Reach Share Card**. It consumes the already resolved upstream/downstream node and edge set without rerunning traversal: `format=share-card`, `variant=reach`. The isolated clone may use only static `data-share-reach-*` decoration. It is download-only. Call it authored reachability—not impact, blast radius, breakage, or runtime causality.

## Truth boundary

Viewer exports are communication assets. They do not replace the checked HTML, the deterministic delivery receipt, or a real visual review. Do not add a hosted service, storage surface, dependency, schema branch, or mobile product surface for these viewer-only capabilities.
````

## File: archify/schemas/architecture.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/architecture.schema.json",
  "title": "Archify Architecture Diagram",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "diagram_type", "meta", "components"],
  "properties": {
    "schema_version": { "const": 1 },
    "diagram_type": { "const": "architecture" },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": ["title"],
      "properties": {
        "title": { "type": "string", "minLength": 1 },
        "locale": { "$ref": "common.schema.json#/$defs/locale" },
        "subtitle": { "type": "string" },
        "output": { "type": "string" },
        "animation": { "$ref": "common.schema.json#/$defs/animation" },
        "visual_preset": { "$ref": "common.schema.json#/$defs/visualPreset" },
        "quality_profile": { "$ref": "common.schema.json#/$defs/qualityProfile" },
        "engineering_profile": { "enum": ["deployment-ownership"] },
        "repository": {
          "type": "object",
          "additionalProperties": false,
          "required": ["url", "revision"],
          "properties": {
            "url": {
              "type": "string",
              "minLength": 1
            },
            "provider": { "enum": ["github", "gitee"] },
            "link_mode": { "enum": ["web", "local-only"] },
            "revision": { "type": "string", "pattern": "^[a-fA-F0-9]{40}$" }
          }
        },
        "views": { "$ref": "common.schema.json#/$defs/guidedViews" },
        "legend": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mode": { "$ref": "common.schema.json#/$defs/legendMode" },
            "entries": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "frontend": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "backend": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "database": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "cloud": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "security": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "messagebus": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "external": { "$ref": "common.schema.json#/$defs/legendEntry" }
              }
            }
          }
        },
        "viewBox": {
          "type": "array",
          "prefixItems": [
            { "type": "number", "minimum": 320 },
            { "type": "number", "minimum": 240 }
          ],
          "items": false,
          "minItems": 2,
          "maxItems": 2
        }
      }
    },
    "layout": {
      "type": "object",
      "additionalProperties": false,
      "required": ["mode"],
      "properties": {
        "mode": { "enum": ["grid"] },
        "origin": { "$ref": "common.schema.json#/$defs/point" },
        "cols": { "type": "integer", "minimum": 1, "maximum": 12 },
        "gapX": { "type": "number", "minimum": 0 },
        "gapY": { "type": "number", "minimum": 0 },
        "cellW": { "type": "number", "minimum": 40 },
        "cellH": { "type": "number", "minimum": 24 }
      }
    },
    "components": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "type", "label"],
        "properties": {
          "id": { "$ref": "common.schema.json#/$defs/id" },
          "type": { "$ref": "common.schema.json#/$defs/componentType" },
          "label": { "type": "string", "minLength": 1 },
          "sublabel": { "type": "string" },
          "tag": { "type": "string" },
          "brand": { "$ref": "common.schema.json#/$defs/brandMark" },
          "sources": {
            "type": "array",
            "minItems": 1,
            "maxItems": 3,
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": ["path"],
              "properties": {
                "path": { "type": "string", "minLength": 1, "maxLength": 240 },
                "line": { "type": "integer", "minimum": 1 },
                "end_line": { "type": "integer", "minimum": 1 },
                "label": { "type": "string", "minLength": 1, "maxLength": 48 }
              }
            }
          },
          "row": { "type": "integer", "minimum": 0 },
          "col": { "type": "integer", "minimum": 0 },
          "pos": { "$ref": "common.schema.json#/$defs/point" },
          "size": {
            "type": "array",
            "prefixItems": [
              { "type": "number", "exclusiveMinimum": 0 },
              { "type": "number", "exclusiveMinimum": 0 }
            ],
            "items": false,
            "minItems": 2,
            "maxItems": 2
          }
        }
      }
    },
    "boundaries": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["kind", "label", "wraps"],
        "properties": {
          "kind": { "enum": ["region", "security-group"] },
          "label": { "type": "string", "minLength": 1 },
          "wraps": {
            "type": "array",
            "minItems": 1,
            "items": { "$ref": "common.schema.json#/$defs/id" }
          },
          "pad": { "type": "number", "minimum": 0 }
        }
      }
    },
    "connections": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["from", "to"],
        "properties": {
          "id": { "$ref": "common.schema.json#/$defs/id" },
          "from": { "$ref": "common.schema.json#/$defs/id" },
          "to": { "$ref": "common.schema.json#/$defs/id" },
          "label": { "type": "string" },
          "variant": { "$ref": "common.schema.json#/$defs/variant" },
          "fromSide": { "$ref": "common.schema.json#/$defs/side" },
          "toSide": { "$ref": "common.schema.json#/$defs/side" },
          "route": { "enum": ["auto", "straight", "orthogonal-h", "orthogonal-v"] },
          "via": {
            "type": "array",
            "items": { "$ref": "common.schema.json#/$defs/point" }
          },
          "labelAt": { "$ref": "common.schema.json#/$defs/point" },
          "labelDx": { "type": "number" },
          "labelDy": { "type": "number" },
          "labelSegment": { "type": "integer", "minimum": 0 },
          "width": { "$ref": "common.schema.json#/$defs/relationshipWidth" }
        }
      }
    },
    "cards": { "$ref": "common.schema.json#/$defs/cards" }
  }
}
````

## File: archify/schemas/common.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/common.schema.json",
  "title": "Archify Shared Definitions",
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[a-zA-Z][a-zA-Z0-9_-]*$"
    },
    "locale": {
      "enum": ["en", "zh-CN"]
    },
    "animation": {
      "enum": ["trace", "none"]
    },
    "visualPreset": {
      "enum": ["classic", "signal-flow", "blueprint", "editorial"]
    },
    "qualityProfile": {
      "enum": ["standard", "showcase"]
    },
    "side": {
      "enum": ["left", "right", "top", "bottom"]
    },
    "relationshipWidth": {
      "type": "number",
      "minimum": 0.5
    },
    "point": {
      "type": "array",
      "prefixItems": [
        { "type": "number" },
        { "type": "number" }
      ],
      "items": false,
      "minItems": 2,
      "maxItems": 2
    },
    "componentType": {
      "enum": ["frontend", "backend", "database", "cloud", "security", "messagebus", "external"]
    },
    "brandMark": {
      "oneOf": [
        {
          "type": "string",
          "minLength": 1,
          "maxLength": 2048,
          "anyOf": [
            { "maxLength": 80, "pattern": "^[^\\r\\n]+$" },
            { "pattern": "^https?://" }
          ]
        },
        {
          "type": "object",
          "additionalProperties": false,
          "required": ["url", "sha256"],
          "properties": {
            "url": { "type": "string", "minLength": 8, "maxLength": 2048, "pattern": "^https?://" },
            "sha256": { "type": "string", "pattern": "^[a-f0-9]{64}$" }
          }
        }
      ]
    },
    "variant": {
      "enum": ["default", "emphasis", "security", "dashed"]
    },
    "legendMode": {
      "enum": ["auto", "all", "hidden"]
    },
    "legendEntry": {
      "type": "object",
      "additionalProperties": false,
      "minProperties": 1,
      "properties": {
        "label": { "type": "string", "minLength": 1, "maxLength": 80 },
        "visible": { "type": "boolean" }
      }
    },
    "guidedViews": {
      "type": "array",
      "maxItems": 5,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["id", "label", "focus"],
        "properties": {
          "id": { "$ref": "#/$defs/id" },
          "label": { "type": "string", "minLength": 1, "maxLength": 48 },
          "focus": {
            "type": "array",
            "minItems": 1,
            "items": { "$ref": "#/$defs/id" }
          },
          "note": { "type": "string", "maxLength": 140 }
        }
      }
    },
    "cards": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["dot", "title", "items"],
        "properties": {
          "dot": { "enum": ["cyan", "emerald", "violet", "amber", "rose", "orange", "slate"] },
          "title": { "type": "string", "minLength": 1 },
          "items": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    }
  }
}
````

## File: archify/schemas/dataflow.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/dataflow.schema.json",
  "title": "Archify Data Flow Diagram",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "diagram_type",
    "meta",
    "stages",
    "nodes",
    "flows"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "diagram_type": {
      "const": "dataflow"
    },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title"
      ],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1
        },
        "locale": {
          "$ref": "common.schema.json#/$defs/locale"
        },
        "subtitle": {
          "type": "string"
        },
        "output": {
          "type": "string"
        },
        "animation": {
          "$ref": "common.schema.json#/$defs/animation"
        },
        "visual_preset": {
          "$ref": "common.schema.json#/$defs/visualPreset"
        },
        "quality_profile": {
          "$ref": "common.schema.json#/$defs/qualityProfile"
        },
        "views": {
          "$ref": "common.schema.json#/$defs/guidedViews"
        },
        "legend": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mode": { "$ref": "common.schema.json#/$defs/legendMode" },
            "entries": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "default": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "emphasis": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "security": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "dashed": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "database": { "$ref": "common.schema.json#/$defs/legendEntry" }
              }
            }
          }
        },
        "viewBox": {
          "type": "array",
          "prefixItems": [
            {
              "type": "number",
              "minimum": 360
            },
            {
              "type": "number",
              "minimum": 360
            }
          ],
          "items": false,
          "minItems": 2,
          "maxItems": 2
        }
      }
    },
    "stages": {
      "type": "array",
      "minItems": 2,
      "maxItems": 5,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "label"
        ],
        "properties": {
          "label": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    },
    "nodes": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "type",
          "label",
          "stage",
          "row"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "type": {
            "$ref": "common.schema.json#/$defs/componentType"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "sublabel": {
            "type": "string"
          },
          "tag": {
            "type": "string"
          },
          "brand": {
            "$ref": "common.schema.json#/$defs/brandMark"
          },
          "stage": {
            "type": "integer",
            "minimum": 0
          },
          "row": {
            "type": "integer",
            "minimum": 0
          },
          "width": {
            "type": "number",
            "minimum": 48
          },
          "height": {
            "type": "number",
            "minimum": 36
          },
          "yOffset": {
            "type": "number"
          }
        }
      }
    },
    "flows": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from",
          "to",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "from": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "to": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "classification": {
            "type": "string"
          },
          "variant": {
            "$ref": "common.schema.json#/$defs/variant"
          },
          "route": {
            "enum": [
              "auto",
              "straight",
              "vertical-channel",
              "bottom-channel",
              "top-channel"
            ]
          },
          "fromSide": {
            "$ref": "common.schema.json#/$defs/side"
          },
          "toSide": {
            "$ref": "common.schema.json#/$defs/side"
          },
          "channelX": {
            "type": "number"
          },
          "channelY": {
            "type": "number"
          },
          "labelAt": {
            "$ref": "common.schema.json#/$defs/point"
          },
          "labelDx": {
            "type": "number"
          },
          "labelDy": {
            "type": "number"
          },
          "labelSegment": {
            "type": "integer",
            "minimum": 0
          },
          "via": {
            "type": "array",
            "items": {
              "$ref": "common.schema.json#/$defs/point"
            }
          },
          "width": {
            "$ref": "common.schema.json#/$defs/relationshipWidth"
          }
        }
      }
    },
    "cards": {
      "$ref": "common.schema.json#/$defs/cards"
    }
  }
}
````

## File: archify/schemas/lifecycle.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/lifecycle.schema.json",
  "title": "Archify Lifecycle Diagram",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "diagram_type",
    "meta",
    "lanes",
    "states",
    "transitions"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "diagram_type": {
      "const": "lifecycle"
    },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title"
      ],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1
        },
        "locale": {
          "$ref": "common.schema.json#/$defs/locale"
        },
        "subtitle": {
          "type": "string"
        },
        "output": {
          "type": "string"
        },
        "animation": {
          "$ref": "common.schema.json#/$defs/animation"
        },
        "visual_preset": {
          "$ref": "common.schema.json#/$defs/visualPreset"
        },
        "quality_profile": {
          "$ref": "common.schema.json#/$defs/qualityProfile"
        },
        "views": {
          "$ref": "common.schema.json#/$defs/guidedViews"
        },
        "legend": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mode": { "$ref": "common.schema.json#/$defs/legendMode" },
            "entries": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "start": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "active": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "waiting": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "decision": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "success": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "failure": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "neutral": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "external": { "$ref": "common.schema.json#/$defs/legendEntry" }
              }
            }
          }
        },
        "viewBox": {
          "type": "array",
          "prefixItems": [
            {
              "type": "number",
              "minimum": 420
            },
            {
              "type": "number",
              "minimum": 566
            }
          ],
          "items": false,
          "minItems": 2,
          "maxItems": 2
        }
      }
    },
    "lanes": {
      "type": "array",
      "minItems": 1,
      "maxItems": 4,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    },
    "states": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "type",
          "label",
          "lane",
          "col"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "type": {
            "enum": [
              "start",
              "active",
              "waiting",
              "decision",
              "success",
              "failure",
              "neutral",
              "external"
            ]
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "sublabel": {
            "type": "string"
          },
          "tag": {
            "type": "string"
          },
          "brand": {
            "$ref": "common.schema.json#/$defs/brandMark"
          },
          "step": {
            "type": "string"
          },
          "lane": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "col": {
            "type": "integer",
            "minimum": 0,
            "maximum": 4
          },
          "width": {
            "type": "number",
            "minimum": 48
          },
          "height": {
            "type": "number",
            "minimum": 36
          },
          "yOffset": {
            "type": "number"
          }
        }
      }
    },
    "transitions": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from",
          "to"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "from": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "to": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string"
          },
          "note": {
            "type": "string"
          },
          "variant": {
            "$ref": "common.schema.json#/$defs/variant"
          },
          "route": {
            "enum": [
              "auto",
              "straight",
              "drop",
              "bottom-channel",
              "top-channel",
              "right-channel",
              "left-channel"
            ]
          },
          "fromSide": {
            "$ref": "common.schema.json#/$defs/side"
          },
          "toSide": {
            "$ref": "common.schema.json#/$defs/side"
          },
          "channelX": {
            "type": "number"
          },
          "channelY": {
            "type": "number"
          },
          "cornerRadius": {
            "type": "number",
            "minimum": 0
          },
          "labelAt": {
            "$ref": "common.schema.json#/$defs/point"
          },
          "labelDx": {
            "type": "number"
          },
          "labelDy": {
            "type": "number"
          },
          "labelSegment": {
            "type": "integer",
            "minimum": 0
          },
          "via": {
            "type": "array",
            "items": {
              "$ref": "common.schema.json#/$defs/point"
            }
          },
          "width": {
            "$ref": "common.schema.json#/$defs/relationshipWidth"
          }
        }
      }
    },
    "cards": {
      "$ref": "common.schema.json#/$defs/cards"
    }
  }
}
````

## File: archify/schemas/README.md
````markdown
# Archify JSON IR Schemas

Each typed renderer consumes a JSON intermediate representation (IR) validated
against one of the schemas in this folder before any layout work happens.

## Files

| Schema | Governs | Structural arrays |
|--------|---------|-------------------|
| `workflow.schema.json` | `diagram_type: "workflow"` | `lanes`, `phases`, `groups`, `mainPath`, `nodes`, `edges` |
| `sequence.schema.json` | `diagram_type: "sequence"` | `participants`, `segments`, `messages`, `activations` |
| `dataflow.schema.json` | `diagram_type: "dataflow"` | `stages`, `nodes`, `flows` |
| `lifecycle.schema.json` | `diagram_type: "lifecycle"` | `lanes`, `states`, `transitions` |
| `architecture.schema.json` | `diagram_type: "architecture"` | `components`, `boundaries`, `connections` |
| `common.schema.json` | shared `$defs` only (no top-level document) | — |

Every diagram schema requires `schema_version`, `diagram_type`, `meta` (with
`title`), and its structural arrays — except `segments`, `activations`, and
`cards`, which are optional — and sets `additionalProperties: false` at every
level, so unknown fields are rejected rather than silently ignored.

Every `meta` object also accepts `animation: "trace"` for opt-in SVG/CSS motion
in generated HTML. Omit it, or set `"none"`, for the default static output.
It also accepts `locale: "en" | "zh-CN"`. The field selects the fixed Viewer
UI, renderer-owned default legend and accessibility copy, document-title
suffix, and `<html lang>` value; it does not translate authored strings.
Omitting it preserves legacy behavior and resolves to English. Unsupported
locale values fail schema validation instead of being guessed or silently
rewritten.
`visual_preset` accepts `classic` (the stable default), `signal-flow` (luminous
motion-forward presentation), `blueprint` (high-contrast engineering review),
or `editorial` (warm publication-style design review and documentation).
Presets change only viewer styling; they do not alter semantic IDs or geometry.
Sequence `meta` additionally accepts `column_fit`. The default `fixed` keeps
the historical 108px column gap and 86px participant boxes, so an authored
diagram renders at the same coordinates no matter how wide its viewBox is.
`spread` derives the gap and box width from the viewBox instead, which turns a
wide canvas into column distance and label room rather than empty space on the
right. Lane order, IDs, and message semantics are unchanged either way.

It may also include up to five guided `views`. Each view has a unique `id`, a
reader-facing `label`, a non-empty `focus` list of existing semantic node IDs,
and an optional short `note`.

### Legend presentation contract

Every `meta` object accepts the same optional legend shape without changing
the schema version already selected for that renderer:

```json
"legend": {
  "mode": "auto",
  "entries": {
    "security": { "label": "restricted data", "visible": true }
  }
}
```

`mode` is `auto` (the default), `all`, or `hidden`. `auto` includes only kinds
present in typed IR; `all` includes the renderer's full stable catalog;
`hidden` removes the complete legend and takes precedence over entry overrides.
Architecture documents that omit an explicit `viewBox` size that automatic
viewBox from the same measured resolved legend footprint used for final SVG
layout. Across all renderers, legacy documents that omit `meta.legend` use a
compatibility-safe implicit `auto`: if the resolved legend cannot fit an
explicit authored viewBox without overlap, Archify omits the complete legend
instead of turning a previously valid schema-v1 document into a hard failure.
Once an author adds `meta.legend` (including explicit `mode: "auto"`), the
layout is intentional and unfit labels or bands fail with a path-prefixed
diagnostic. An entry may set a non-empty, bounded `label`, boolean `visible`,
or both.
`visible: false` removes a resolved entry and `visible: true` forces a supported
but unused kind into the visual legend. Unknown kinds and properties fail
strict validation.

Supported keys are renderer-owned:

| Renderer | `meta.legend.entries` keys |
|---|---|
| Architecture | `frontend`, `backend`, `database`, `cloud`, `security`, `messagebus`, `external` |
| Workflow | `frontend`, `backend`, `security`, `messagebus`, `database`, `cloud`, `external` |
| Sequence | `emphasis`, `return`, `security`, `dashed`, `default` |
| Dataflow | `emphasis`, `security`, `dashed`, `database`, `default` |
| Lifecycle | `start`, `active`, `waiting`, `decision`, `success`, `failure`, `neutral`, `external` |

Labels are presentation only: they do not rename the stable kind, change
nodes/relationships, or create Semantic Lens edge facts. Sequence message and
Dataflow flow-variant entries are visual keys. Component/state entries backed
by exact compiled node facts receive the interactive Semantic Legend bridge;
this includes Dataflow `database` when a real `nodes[].type: "database"` fact
exists.

Every relationship collection (`connections`, `edges`, `messages`, `flows`, and
`transitions`) accepts an optional author-controlled `id` using the shared ID
pattern. The renderer keeps its source-order runtime key separately, while the
authored ID enables a stable `#relation=<id>` viewer link that survives array
reordering. ID-less documents remain valid and their relationship pins stay
local to the current page.

Every semantic node collection (`components`, `nodes`, `participants`, and
`states`) also accepts one optional `brand`: either a canonical string returned
by `archify brands --json`, or a digest-pinned `{ "url", "sha256" }` object
returned by `archify brands capture <url> --json`. Known IDs and known-brand
domains use the bundled vector catalogue. Unknown URLs must be captured in that
explicit command before authoring; render and validate never perform an
unpinned network capture. Unsafe, unavailable, changed, or unsupported content
fails closed with a brand diagnostic. Omitted `brand` preserves the prior
output.

## schema_version policy

Workflow supports schema versions 1 and 2. Version 1 remains the fixed-layout
compatibility contract; version 2 opts into the readable workflow compiler and
can be produced explicitly with `archify migrate workflow ... --to-schema 2`.
The other four diagram schemas keep `schema_version` pinned to `1`.

Workflow also accepts optional `semanticChecks`. `allowedRoots` and
`allowedTerminals` close the set of intentional graph sources and sinks;
`requiredEdges` requires exact authored relationships; and `requiredPaths`
requires directed reachability while allowing intermediate nodes. The compiler
evaluates these facts before layout and returns typed `workflow/*` diagnostics.
The field is additive and geometry-neutral: omitting it preserves existing
workflow behavior and including a satisfied contract does not change SVG or
layout-receipt bytes.

A file that validates today must keep validating and rendering within its
declared version throughout the 2.x release line. Additive viewer,
accessibility, and presentation improvements may enhance generated HTML, but
they must not reinterpret authored IR or turn a previously valid profile-less
v1 file into a new hard layout failure. Breaking IR changes require a new
version; additive, backwards-compatible fields do not.

## Shared definitions (common.schema.json)

The five diagram schemas reference `common.schema.json#/$defs/...`:

- `id` — element identifiers, pattern `^[a-zA-Z][a-zA-Z0-9_-]*$`
- `point` — an `[x, y]` pair of numbers (used by `via` and `labelAt`)
- `componentType` — `frontend`, `backend`, `database`, `cloud`, `security`,
  `messagebus`, `external`
- `locale` — the bounded renderer locale, `en` or `zh-CN`
- `brandMark` — one optional built-in brand ID or explicit HTTP(S) site URL
- `variant` — `default`, `emphasis`, `security`, `dashed` (sequence messages
  extend this list locally with `return`)
- `legendMode` and `legendEntry` — the shared strict mode and label/visibility
  override shapes used by each renderer-owned key map
- `guidedViews` — the bounded, read-only reader paths accepted by `meta.views`
- `cards` — the summary-card blocks rendered below the SVG

Lifecycle state `type` is mode-specific (`start`/`active`/`waiting`/...) and
stays in `lifecycle.schema.json`.

## Runtime validation

At development time, `scripts/generate-validators.mjs` compiles all five
schemas with ajv's draft 2020-12 standalone generator using `strict: true` and
`allErrors: true`. The generated `renderers/shared/generated-validators.mjs`
is committed and shipped with the skill, so runtime validation has no npm or
network dependency. `renderers/shared/validator.mjs` applies the matching
standalone validator before the renderer's own layout checks.
The shared loader then checks cross-collection facts that JSON Schema cannot
express cleanly here: duplicate view IDs, duplicate focus IDs, focus IDs that do
not exist in the diagram's semantic collection, and duplicate authored
relationship IDs within the mode's relationship collection.

Architecture additionally supports opt-in, revision-pinned repository evidence.
`meta.repository` names a public GitHub URL and full commit SHA; a component may
carry one to three `sources` with repo-relative POSIX paths, optional line
ranges, and optional labels. Shape is schema-checked, then the renderer requires
`--repo-root`: the local Git origin must match, and Git must prove the commit,
blobs, and requested lines. Verified evidence is embedded outside the canonical
SVG for the Semantic Passport and Node Finder; ordinary documents and visual
exports carry no repository evidence.

## Visual quality and engineering truth

`meta.quality_profile` and `meta.engineering_profile` answer different
questions. `quality_profile` is available in all five modes and controls how
strictly Archify judges composition. `engineering_profile` is an optional
Architecture-only semantic contract; omitting it preserves the ordinary v1
behavior.

The first engineering profile is `deployment-ownership`. Enable it only when
the user wants a fail-closed deployment review and the source facts are known.
It requires every non-external component to name an owner in `tag` and belong
to exactly one `region`; the document must contain both `region` and
`security-group` boundaries; every `database` must be inside a
`security-group`; each security group must contain members from one shared
region; and every connection whose region or security-group membership changes
must name the real crossing mechanism in `label`.

The profile validates only authored IR. It does not discover infrastructure,
infer owners, or prove that a diagram matches a live environment. If a fact is
unknown, leave the profile unset or obtain the fact instead of inventing it.

`npm test` runs the generator in check mode and fails when the committed
validators drift from their schemas.

## Error format

Schema violations exit non-zero. Each ajv error is reported on its own line as
the instance path — annotated with the nearest enclosing element's `id` or
`label` — followed by the message and parameters:

```text
workflow schema validation failed:
  /nodes/3 (id/label: "router") must NOT have additional properties {"additionalProperty":"colour"}
```

Schemas catch shape errors (types, enums, ranges, unknown fields); geometry
problems such as overlaps and label collisions are the renderers' job.
````

## File: archify/schemas/sequence.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/sequence.schema.json",
  "title": "Archify Sequence Diagram",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "diagram_type",
    "meta",
    "participants",
    "messages"
  ],
  "properties": {
    "schema_version": {
      "const": 1
    },
    "diagram_type": {
      "const": "sequence"
    },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title"
      ],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1
        },
        "locale": {
          "$ref": "common.schema.json#/$defs/locale"
        },
        "subtitle": {
          "type": "string"
        },
        "output": {
          "type": "string"
        },
        "animation": {
          "$ref": "common.schema.json#/$defs/animation"
        },
        "visual_preset": {
          "$ref": "common.schema.json#/$defs/visualPreset"
        },
        "quality_profile": {
          "$ref": "common.schema.json#/$defs/qualityProfile"
        },
        "column_fit": {
          "description": "Horizontal participant layout. Omit this field or use fixed for the stable 86px boxes and 108px gap. Use spread when a wide viewBox would leave unused horizontal space or meaningful participant labels do not fit the fixed boxes; spread derives wider boxes and gaps from the viewBox without changing participant order or message semantics.",
          "enum": ["fixed", "spread"]
        },
        "views": {
          "$ref": "common.schema.json#/$defs/guidedViews"
        },
        "legend": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mode": { "$ref": "common.schema.json#/$defs/legendMode" },
            "entries": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "default": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "emphasis": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "security": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "dashed": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "return": { "$ref": "common.schema.json#/$defs/legendEntry" }
              }
            }
          }
        },
        "viewBox": {
          "type": "array",
          "prefixItems": [
            {
              "type": "number",
              "minimum": 480
            },
            {
              "type": "number",
              "minimum": 480
            }
          ],
          "items": false,
          "minItems": 2,
          "maxItems": 2
        }
      }
    },
    "participants": {
      "type": "array",
      "minItems": 2,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "type",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "type": {
            "$ref": "common.schema.json#/$defs/componentType"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "sublabel": {
            "type": "string"
          },
          "brand": {
            "$ref": "common.schema.json#/$defs/brandMark"
          }
        }
      }
    },
    "segments": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from",
          "to",
          "label"
        ],
        "properties": {
          "from": {
            "type": "number"
          },
          "to": {
            "type": "number"
          },
          "label": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    },
    "messages": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from",
          "to",
          "y",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "from": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "to": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "y": {
            "type": "number",
            "minimum": 160
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "variant": {
            "enum": [
              "default",
              "emphasis",
              "security",
              "dashed",
              "return"
            ]
          },
          "note": {
            "type": "string"
          }
        }
      }
    },
    "activations": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "participant",
          "from",
          "to"
        ],
        "properties": {
          "participant": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "from": {
            "type": "number"
          },
          "to": {
            "type": "number"
          },
          "type": {
            "$ref": "common.schema.json#/$defs/componentType"
          }
        }
      }
    },
    "cards": {
      "$ref": "common.schema.json#/$defs/cards"
    }
  }
}
````

## File: archify/schemas/workflow.schema.json
````json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/tt-a1i/archify/schemas/workflow.schema.json",
  "title": "Archify Workflow Diagram",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "diagram_type",
    "meta",
    "lanes",
    "nodes",
    "edges"
  ],
  "properties": {
    "schema_version": {
      "enum": [
        1,
        2
      ]
    },
    "diagram_type": {
      "const": "workflow"
    },
    "meta": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "title"
      ],
      "properties": {
        "title": {
          "type": "string",
          "minLength": 1
        },
        "locale": {
          "$ref": "common.schema.json#/$defs/locale"
        },
        "subtitle": {
          "type": "string"
        },
        "output": {
          "type": "string"
        },
        "animation": {
          "enum": [
            "trace",
            "none"
          ]
        },
        "visual_preset": {
          "enum": [
            "classic",
            "signal-flow",
            "blueprint",
            "editorial"
          ]
        },
        "quality_profile": {
          "enum": [
            "standard",
            "showcase"
          ]
        },
        "views": {
          "$ref": "common.schema.json#/$defs/guidedViews"
        },
        "legend": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "mode": { "$ref": "common.schema.json#/$defs/legendMode" },
            "entries": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "frontend": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "backend": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "database": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "cloud": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "security": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "messagebus": { "$ref": "common.schema.json#/$defs/legendEntry" },
                "external": { "$ref": "common.schema.json#/$defs/legendEntry" }
              }
            }
          }
        },
        "viewBox": {
          "type": "array",
          "prefixItems": [
            {
              "type": "number",
              "minimum": 700
            },
            {
              "type": "number",
              "minimum": 240
            }
          ],
          "items": false,
          "minItems": 2,
          "maxItems": 2
        }
      }
    },
    "lanes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "variant": {
            "enum": [
              "normal",
              "exception"
            ]
          }
        }
      }
    },
    "phases": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "label",
          "fromCol",
          "toCol"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "fromCol": {
            "type": "integer",
            "minimum": 0,
            "maximum": 5
          },
          "toCol": {
            "type": "integer",
            "minimum": 0,
            "maximum": 5
          },
          "variant": {
            "enum": [
              "default",
              "emphasis",
              "security",
              "dashed"
            ]
          }
        }
      }
    },
    "groups": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "label",
          "lane",
          "fromCol",
          "toCol"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "lane": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "fromCol": {
            "type": "integer",
            "minimum": 0,
            "maximum": 5
          },
          "toCol": {
            "type": "integer",
            "minimum": 0,
            "maximum": 5
          },
          "variant": {
            "enum": [
              "default",
              "emphasis",
              "security",
              "dashed"
            ]
          }
        }
      }
    },
    "mainPath": {
      "type": "array",
      "minItems": 2,
      "items": {
        "$ref": "common.schema.json#/$defs/id"
      }
    },
    "semanticChecks": {
      "type": "object",
      "additionalProperties": false,
      "minProperties": 1,
      "properties": {
        "allowedRoots": {
          "type": "array",
          "items": {
            "$ref": "common.schema.json#/$defs/id"
          }
        },
        "allowedTerminals": {
          "type": "array",
          "items": {
            "$ref": "common.schema.json#/$defs/id"
          }
        },
        "requiredEdges": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/semanticRelation"
          }
        },
        "requiredPaths": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/semanticRelation"
          }
        }
      }
    },
    "nodes": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "lane",
          "col",
          "type",
          "label"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "lane": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "col": {
            "type": "integer",
            "minimum": 0,
            "maximum": 5
          },
          "type": {
            "$ref": "common.schema.json#/$defs/componentType"
          },
          "label": {
            "type": "string",
            "minLength": 1
          },
          "sublabel": {
            "type": "string"
          },
          "tag": {
            "type": "string"
          },
          "brand": {
            "$ref": "common.schema.json#/$defs/brandMark"
          },
          "width": {
            "type": "number",
            "minimum": 32
          },
          "height": {
            "type": "number",
            "minimum": 32
          },
          "yOffset": {
            "type": "number"
          }
        }
      }
    },
    "edges": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from",
          "to"
        ],
        "properties": {
          "id": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "from": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "to": {
            "$ref": "common.schema.json#/$defs/id"
          },
          "label": {
            "type": "string"
          },
          "variant": {
            "$ref": "common.schema.json#/$defs/variant"
          },
          "role": {
            "enum": [
              "main",
              "branch",
              "async",
              "return",
              "error"
            ]
          },
          "fromSide": {
            "$ref": "#/$defs/side"
          },
          "toSide": {
            "$ref": "#/$defs/side"
          },
          "route": {
            "enum": [
              "auto",
              "straight",
              "drop",
              "outside-right",
              "return-left",
              "bottom-channel",
              "up-channel"
            ]
          },
          "via": {
            "type": "array",
            "items": {
              "$ref": "common.schema.json#/$defs/point"
            }
          },
          "labelAt": {
            "$ref": "common.schema.json#/$defs/point"
          },
          "labelDx": {
            "type": "number"
          },
          "labelDy": {
            "type": "number"
          },
          "labelSegment": {
            "type": "integer",
            "minimum": 0
          },
          "channelX": {
            "type": "number"
          },
          "channelY": {
            "type": "number"
          },
          "bias": {
            "type": "number",
            "minimum": 0,
            "maximum": 1
          },
          "width": {
            "type": "number",
            "minimum": 0.5
          }
        }
      }
    },
    "cards": {
      "$ref": "common.schema.json#/$defs/cards"
    }
  },
  "$defs": {
    "semanticRelation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "from",
        "to"
      ],
      "properties": {
        "from": {
          "$ref": "common.schema.json#/$defs/id"
        },
        "to": {
          "$ref": "common.schema.json#/$defs/id"
        }
      }
    },
    "side": {
      "enum": [
        "left",
        "right",
        "top",
        "bottom"
      ]
    }
  }
}
````

## File: archify/scripts/check-update.mjs
````javascript
class FileIdentityChangedError extends Error
⋮----
function silent(reason)
⋮----
function isPlainObject(value)
⋮----
function hasOnlyKeys(value, allowed)
⋮----
function validateManifest(value)
⋮----
function validateCachedCandidate(value)
⋮----
function emptyState(installedVersion = null)
⋮----
function encodeBoundedState(state)
⋮----
function stateAfterAcknowledgement(state, targetDigest)
⋮----
function stateWithFailureCheck(state, nextCheckAt, consecutiveFailures, withdrawCandidate = false)
⋮----
function encodeRecoverableState(state)
⋮----
function versionCacheDirectory(cacheDirectory, installedVersion)
⋮----
function normalizeState(value, installedVersion)
⋮----
function isSameFile(left, right)
⋮----
function assertBoundedRegularFile(metadata, maxBytes)
⋮----
async function readJsonFile(target, maxBytes, expectedMetadata = null)
⋮----
function isWithinDirectory(directory, target)
⋮----
async function canonicalizeTrustedDirectoryPrefix(target)
⋮----
// Fall back to validating the absolute path from its filesystem root.
⋮----
function assertSafeDirectory(metadata)
⋮----
class CachePathChangedError extends Error
class CacheOperationRaceError extends Error
class OperationFencedError extends Error
⋮----
function invalidateCacheToken(token, message, cause)
⋮----
async function verifyDirectorySnapshots(token, snapshots, description)
⋮----
async function verifyCacheToken(token)
⋮----
async function guardedCacheRead(token, read)
⋮----
function cacheTokenFor(cacheDirectory)
⋮----
function resolveCacheTarget(token, target)
⋮----
async function captureMutationParentSnapshots(token, targets)
⋮----
async function verifyMutationParentSnapshots(token, snapshots)
⋮----
async function verifyMutationContext(token, parentSnapshots)
⋮----
function assertSafeCacheEntry(metadata)
⋮----
function assertSafeRegularFile(metadata)
⋮----
function assertRenameableCacheEntry(metadata)
⋮----
async function stableCacheEntry(
  token,
  target,
  validate,
  expectedMetadata = null,
  missingIsOperationRace = false,
)
⋮----
async function guardedCacheEntryRead(
  token,
  target,
  validate,
  read,
  expectedMetadata = null,
)
⋮----
async function stablePreparedDirectory(token, target)
⋮----
async function assertCacheTargetAbsent(token, target)
⋮----
async function guardedCacheMutation(token, parentSnapshots, {
  mutate,
  verifyBefore = null,
  verifyAfter,
})
⋮----
async function cacheMkdirWithToken(token, target, options, parentSnapshots = null)
⋮----
mutate: ()
verifyAfter: ()
⋮----
async function cacheMkdir(cacheDirectory, target, options)
⋮----
async function cacheWriteFile(cacheDirectory, target, data, options)
⋮----
mutate: async () =>
verifyAfter: (writtenMetadata) => stableCacheEntry(token, resolved, (metadata) =>
⋮----
async function cacheRename(
  cacheDirectory,
  source,
  destination,
  validate,
  expectedSourceMetadata = null,
)
⋮----
verifyBefore: ()
⋮----
verifyAfter: async () =>
⋮----
async function cacheRm(cacheDirectory, target, options)
⋮----
async function prepareCacheDirectory(cacheDirectory)
⋮----
function operationName(kind, generation)
⋮----
function parseOperationName(name)
⋮----
async function listOperations(cacheDirectory, token = cacheTokenFor(cacheDirectory))
⋮----
async function readState(cacheDirectory, installedVersion = null)
⋮----
// An incomplete or corrupt generation is ignored in favor of the previous commit.
⋮----
async function operationIsActive(
  cacheDirectory,
  operation,
  token = cacheTokenFor(cacheDirectory),
)
⋮----
function validateClaimOwner(value)
⋮----
function metadataIsWithinLease(metadata)
⋮----
function corruptClaimStatus(directory, directoryMetadata, ownerMetadata = directoryMetadata)
⋮----
async function inspectActiveClaim(cacheDirectory)
⋮----
// A malformed claim is recoverable only after the same hard lease as a crashed owner.
⋮----
async function retireActiveClaim(cacheDirectory, claim)
⋮----
async function prepareOperationClaim(cacheDirectory, operation)
⋮----
async function discardPreparedClaim(cacheDirectory, operation)
⋮----
async function promoteOperationClaim(cacheDirectory, operation)
⋮----
async function operationOwnsActiveClaim(cacheDirectory, operation)
⋮----
async function hasActivePendingOperation(cacheDirectory)
⋮----
async function reserveOperation(cacheDirectory)
⋮----
async function operationIsSuperseded(cacheDirectory, operation)
⋮----
async function operationWasFenced(cacheDirectory, operation)
⋮----
async function transitionOperation(cacheDirectory, operation, kind)
⋮----
async function cancelOperation(cacheDirectory, operation)
⋮----
// A higher generation may already have fenced this unique pending directory.
⋮----
async function acquireOperation(cacheDirectory)
⋮----
async function fenceLowerOperations(cacheDirectory, operation)
⋮----
async function commitOperation(cacheDirectory, operation, installedVersion, mutate)
⋮----
function nextSuccessfulCheck(nowMs, random)
⋮----
function nextFailedCheck(nowMs, failures)
⋮----
function stateAfterFailedCheck(state, nowMs, withdrawCandidate = false)
⋮----
function eventKeyForDigest(targetDigest)
⋮----
function digestForEventKey(eventKey)
⋮----
function notification(localRelease, candidate)
⋮----
function resultForCandidate(localRelease, state)
⋮----
async function readBoundedBody(response)
⋮----
async function cancelResponseBody(response)
⋮----
// Network cleanup is best-effort; the original response classification wins.
⋮----
async function fetchCandidate(
⋮----
function defaultCacheDirectory()
⋮----
function freshStateResult(localRelease, state, nowMs)
⋮----
async function resultAfterLosingOperation(cacheDirectory, operation, localRelease)
⋮----
async function waitUntilRetry(deadline, monotonicNow)
⋮----
export async function checkForUpdate({
  releasePath = defaultReleasePath,
  cacheDirectory = defaultCacheDirectory(),
  fetchImpl = globalThis.fetch,
  now = Date.now,
  random = Math.random,
  timeoutMs = DEFAULT_TIMEOUT_MS,
} =
⋮----
export async function acknowledgeUpdate({
  releasePath = defaultReleasePath,
  cacheDirectory = defaultCacheDirectory(),
  eventKey,
  monotonicNow = () => performance.now(),
} =
⋮----
async function runCli()
⋮----
async function isMainModule()
````

## File: archify/package.json
````json
{
  "name": "archify",
  "version": "2.17.0-dev.1",
  "private": true,
  "type": "module",
  "description": "JSON-IR diagram renderers (architecture / workflow / sequence / dataflow / lifecycle).",
  "license": "MIT",
  "bin": {
    "archify": "./bin/archify.mjs"
  },
  "engines": {
    "node": ">=18"
  },
  "scripts": {
    "generate:brand-marks": "node scripts/generate-brand-marks.mjs",
    "check:brand-marks": "node scripts/generate-brand-marks.mjs --check",
    "generate:validators": "node scripts/generate-validators.mjs",
    "check:validators": "node scripts/generate-validators.mjs --check",
    "check:release-identity": "node ../scripts/check-release-identity.mjs",
    "build:gallery": "node ../scripts/build-gallery.mjs ../docs",
    "build:guide": "node ../scripts/build-guide.mjs ../docs/guide.html",
    "build:start": "node ../scripts/build-start.mjs ../docs/start.html",
    "build:readme-showcase": "node ../scripts/build-readme-showcase.mjs",
    "test:webm": "node test/webm-artifact.smoke.mjs && node --test test/site-language-integration.mjs",
    "test": "npm run check:brand-marks && npm run check:validators && npm run check:release-identity && node test/golden.mjs && node ../scripts/run-tests.mjs",
    "render:examples": "node scripts/render-examples.mjs ../examples"
  },
  "devDependencies": {
    "ajv": "^8.17.1",
    "parse5": "7.3.0",
    "saxes": "6.0.0",
    "simple-icons": "16.28.0"
  },
  "overrides": {
    "fast-uri": "3.1.5"
  }
}
````

## File: archify/skill-release.json
````json
{
  "schemaVersion": 1,
  "skillId": "archify",
  "channel": "development",
  "version": "2.17.0-dev.1",
  "source": {
    "repository": "https://github.com/tt-a1i/archify"
  },
  "updateManifestUrl": "https://tt-a1i.github.io/archify/skill-updates/archify/stable.json"
}
````

## File: archify/SKILL.md
````markdown
---
name: archify
description: Create polished, validated architecture, workflow, sequence, data-flow, and lifecycle/state diagrams as explorable standalone HTML with inline SVG, dark/light themes, optional trace motion, and PNG/JPEG/WebP/SVG/WebM export. Accept plain-language requirements or pasted Mermaid flowchart, sequenceDiagram, and stateDiagram input; inspect repository evidence when the diagram must reflect real code. Use when the user asks to visualize system architecture, infrastructure, cloud/security/network topology, technical workflows, API call sequences, request lifecycles, data pipelines, ETL/ELT, data lineage, state machines, or to convert/beautify Mermaid.
license: MIT
metadata:
  version: "2.17"
  author: tt-a1i
  based_on: Cocoon-AI/architecture-diagram-generator (MIT, v1.0)
---

# Archify

Create a self-contained, interactive HTML diagram from a small typed JSON specification. Static output is the default; enable motion only when the user asks for a demo or presentation.

## Fast authoring path

Use this bounded path for ordinary generation. Do not read the optional Viewer Runtime reference unless the user asks about those features.

1. Choose `architecture`, `workflow`, `sequence`, `dataflow`, or `lifecycle` from the question.
2. Read one matching schema in `schemas/`, `schemas/common.schema.json`, and one matching JSON example in `examples/`. Read only those files. Fresh authorship means new stable IDs, domain wording, and layout; use the example for field shape, not facts. New workflow sources use `schema_version: 2` and its readable layout contract; keep `schema_version: 1` only when preserving an existing workflow's fixed geometry. When real product identity matters, query `node bin/archify.mjs brands "<name>" --json`; read `references/brand-marks.md` only for an unknown brand with a user-provided URL.
3. Artifact first: the next tool action must write the candidate. Write the candidate before inspecting renderer internals. Do not plan exact coordinates in prose. Start with one clear main path, short side branches, sparse labels, and at most 12 primary nodes. Set `meta.quality_profile` to `"showcase"` unless the user explicitly requests a dense `standard` map. Start with automatic routes and labels. Do not add `via`, `channelX`, `channelY`, or `labelAt` before a diagnostic calls for one; apply at most one diagnosed geometry control per repair.
4. Validate after every candidate edit and immediately before handoff:

   ```bash
   node bin/archify.mjs validate <type> <candidate.json> --quality showcase --json
   ```

   A receipt with only 4 artifact checks is basic validation, never showcase acceptance. A showcase pass must report all 9 artifact checks with 0 composition errors and 0 warnings. If the candidate omits or misspells the exact `meta.quality_profile` field, fix it before geometry. For a workflow v2 geometry diagnosis, run `node bin/archify.mjs validate workflow <candidate.json> --layout-json` and use the stable compiler receipt; solver internals are not authoring controls. A passing final validation freezes the candidate: never edit it afterward.
5. For a delivered HTML, `deliver` is the final acceptance command:

   ```bash
   node bin/archify.mjs deliver <type> <candidate.json> <output.html> --quality showcase --json
   ```

   A non-zero exit can never be described as success. A failed delivery preserves any previous output, so do not run `visual-check` on that path: it would inspect the stale last-good artifact, not the failed candidate. If validation fails, change only the diagnosed `subject`, verify `evidence`, choose from `supportedFixes`, and rerun. Continue focused correction while the objective error count reaches a new minimum. If two consecutive rounds do not improve that best count, stop and report the unresolved diagnostics truthfully.

## Update awareness

After the first candidate exists, run the packaged checker `scripts/check-update.mjs` once with Node and continue the requested workflow. If the command cannot run, continue without mentioning the check.

- For `silent`, continue without mentioning the update check.
- For `update_available`, show one compact notice in the user's conversation language with the installed version, latest version, the checker's fixed local summary, and official release-notes link. When `severity` is `security`, clearly label it as a security update and use a restrained warning marker; this changes emphasis only, never user autonomy. Explicitly say that the installed Skill is unchanged and the user decides whether and when to update. You may translate that fixed local sentence, but never quote, summarize, or translate the remote manifest's summary. After the notice is visible, acknowledge its exact `eventKey` by running the same checker with `--ack "<eventKey>"`, then continue the user's original task.

The notice is information, not permission. Keep the installed version unchanged; this v0.1 workflow never downloads, installs, or executes an update, and silence is never consent.

Do not read `renderers/shared/geometry.mjs`, renderer source, validator source, tests, or benchmarks before the first candidate. Inspect implementation only for an unsupported internal diagnostic or after two focused repairs fail.

Workflow note: use schema v2 for new workflows; preserve schema v1 when an
existing source needs fixed legacy geometry. Keep semantic edge labels and act
on the compiler diagnostic. The canonical layout, pin, migration, and receipt
contract is in [`renderers/workflow/README.md`](renderers/workflow/README.md#layout-contracts).

Lifecycle note: phase columns `0..4` occupy the main rail; event/terminal column `N` in `0..2` aligns exactly beneath main column `N + 2`. A recoverable state uses `type: "failure"` plus a real transition back to the active state.

## Type router

| Type | Use for |
|---|---|
| `architecture` | Components, services, cloud/security boundaries, infrastructure |
| `workflow` | Processes, approval gates, tool calls, runbooks, CI/CD |
| `sequence` | API call chains, request lifecycles, async traces, returns |
| `dataflow` | Pipelines, ETL/ELT, lineage, governance, consumers |
| `lifecycle` | State/status transitions, retries, waiting and terminal states |

When ambiguous, run `node bin/archify.mjs guide "<scenario>" --json`. Scenario proof examples are structural references, not facts to copy.

## Mermaid input

Read Mermaid for topology and meaning, then author fresh Archify JSON; do not mechanically render Mermaid styling.

- `flowchart` / `graph` → `workflow`, or `architecture` for a component map.
- `sequenceDiagram` → `sequence`; participants become semantic participants and arrows become messages.
- `stateDiagram` → `lifecycle`; states and transitions retain meaning, not Mermaid style.

## Authoring invariants

- One obvious main path; side branches leave the nearest main-path node. Remove low-value edges before adding routing controls.
- Omit `meta.visual_preset` by default so every diagram opens in `classic`, regardless of whether its resolved color mode is light or dark. Color mode and visual preset are independent: switching Light / Dark must preserve the current preset. Set `signal-flow`, `blueprint`, or `editorial` only when the user explicitly requests that visual style.
- Omit `meta.subtitle` by default. Never invent a subtitle that restates the title, nodes, or cards; include one short supporting line only when the user explicitly asks for it.
- Treat the standalone desktop viewer as a first-screen artifact by default, not a shallow strip. Generate one responsive artifact for laptops and external displays—never device-specific HTML or alternate topology. The viewer may adapt only the outer reading width from the live viewport height; it must preserve the authored SVG/viewBox, proportions, semantic geometry, and normal document flow. On a wide or tall desktop, use enough authored vertical rhythm that the diagram panel and its necessary conclusion cards occupy the screen as a balanced whole; runtime scaling cannot repair an over-compressed Y layout or an undersized explicit `meta.viewBox`. Before handoff, open the real HTML at 1440×900, 1600×1000, and 1920×1080; additionally check 2048×1320 whenever the composition is intended for a large desktop display. Require `document.documentElement.scrollWidth <= window.innerWidth` and `scrollHeight <= window.innerHeight` at every checked size, while visually checking that the diagram remains comfortably readable and vertically balanced at the largest checked viewport. Repair overflow by removing only genuinely redundant content or compacting spacing before shrinking nodes, labels, or the main panel. If the largest viewport still has a conspicuous empty lower band at the viewer's width cap, redistribute authored Y positions and increase the viewBox height proportionally; do not add filler copy or decorative cards. Never counterfeit a pass with `overflow: hidden`, clipped content, an internal diagram scroller, stretched SVG height, or smaller typography. Narrow/mobile layouts may scroll vertically when containment requires it.
- Omit `meta.legend` for the truthful `auto` default. When needed, use only `mode: auto|all|hidden` and renderer-supported `entries.<kind>.label|visible`; labels never change semantics.
- Choose one primary authored language from an explicit user choice; otherwise follow the request or conversation's dominant language. `meta.locale` controls only renderer-owned Viewer UI: use `"en"` or `"zh-CN"` for the corresponding supported primary language. For every other language, omit `meta.locale` and explicitly disclose that the fixed Viewer UI and `<html lang>` fall back to English. The renderer never translates authored content. See `references/authoring-contract.md` for details.
- Preserve exact product names, code identifiers, commands, protocols, API paths, and environment names. They may remain English inside localized copy, but never justify leaving the surrounding explanatory prose in another language.
- Brand identity is optional and explicit. Put a canonical built-in ID in `brand` when the node names that real product. If no preset matches and the user supplied the official HTTP(S) URL, first run `node bin/archify.mjs brands capture "<url>" --json`, then author the returned digest-pinned `brand` object. Render and validate never perform an unpinned capture. Otherwise omit `brand`. Never infer a brand from a vague role such as "database", and never let a badge replace the semantic `type`, label, or relationship facts.
- For sequence diagrams, omit `meta.column_fit` for the stable `fixed` layout. Set it to `"spread"` when a wide viewBox would otherwise leave unused horizontal space or when meaningful participant labels do not fit the fixed boxes; do not shorten semantic labels before trying `spread`.
- Component types are `frontend`, `backend`, `database`, `cloud`, `security`, `messagebus`, and `external`; variants are `default`, `emphasis`, `security`, and `dashed`.
- Relationship labels are semantic data. When one collides, move the label, adjust the route or spacing, then shorten the wording while preserving meaning. Omit only wording that is already fully implied by both endpoints and contains no protocol, action, direction, synchronous/asynchronous behavior, or cross-boundary mechanism. Preserve every meaningful label; deleting it is not a geometry repair. If a relationship starts unlabeled because its endpoints fully imply it, explain why the wording is redundant; this is a semantic authoring choice, not a geometry repair.
- Omit `meta.engineering_profile` by default. Region, cluster, and security boundary wording do not by themselves enable it. Enable `deployment-ownership` only when the user explicitly asks for a production deployment topology, ownership handoff, or fail-closed deployment review and the source facts are known. Once enabled, must not remove the engineering profile merely to pass validation; repair the facts or report the diagnostics truthfully.
- Spacing means clear gap, not center distance. For a relationship label, clear gap must exceed its measured mask width; follow the label-preserving repair order.
- Automatic routes own their endpoint sides. A side is a direction contract: the first and final segment must leave/enter perpendicular to that side.
- Automatic Port Spread is a default renderer behavior for architecture, workflow, data-flow, and lifecycle. It skips single relationships and explicit `via`, `channelX`, `channelY`, `labelAt`, or non-`auto` routes. Near parallel ports use an outside bridge so automatic routing cannot create a sub-8px segment or sub-16px interior turn. Architecture separately keeps unobstructed facing automatic ports (`left`/`right` or `top`/`bottom`) on one shared axis when their offset is under 16px and both ports retain corner clearance. If exactly one endpoint was spread, only the unshared endpoint may move onto that axis; if both endpoints were spread, keep the outside bridge so competing ports remain distinct.
- Never accept an edge crossing an unrelated opaque node, an ambiguous shared corridor, or a relationship label masking another route.

Read `references/authoring-contract.md` only when you need field enums, spacing math, geometry repair rules, repository evidence, or mode-specific placement.

## Delivery

Use `validate` during repair and `deliver` once for final acceptance. Delivery freezes the exact specification bytes into a private same-directory snapshot, renders and checks that snapshot, atomically commits the HTML, and reports SHA-256 plus byte counts for both specification and artifact. This is deterministic artifact evidence; it does not exercise the Viewer in a browser.

After delivery, collect bounded desktop evidence without modifying or rerendering the trusted HTML:

```bash
node bin/archify.mjs visual-check <output.html> --json
```

`visual-check` collects automated browser evidence from the exact delivered HTML without modifying or rerendering it. Its machine-readable measurements and screenshots do not approve perceptual polish. Follow `references/delivery-contract.md` for the canonical receipt fields, coverage, sidecars, exit behavior, and supplementary manual-record requirements.

Keep the three claims separate: `deliver` proves deterministic artifact checks, `visual-check` proves bounded behavior in a real browser, and perceptual visual review requires an actual human or image-capable reviewer. Report browser evidence and perceptual review independently. An unconstrained glance can support only perceptual review; use the canonical delivery contract when recording supplementary manual browser work or handling an environmental failure.

Add `--open` only when the user wants an immediate local preview. For an active desktop authoring loop, the optional command is:

```bash
node bin/archify.mjs preview <type> <input>.json <output>.html --quality showcase
```

Never start preview by default. Read `references/delivery-contract.md` when using preview, repository evidence, export receipts, visual review, or post-commit opening.

## Optional viewer capabilities

Generated HTML already contains theme switching, pan/zoom, search, focus, relationship tracing, semantic views, presentation, and truthful exports. These are reader capabilities, not extra authoring work. `meta.animation: "trace"` is opt-in; `meta.views` is optional and should contain at most five curated chapters.

Read `references/viewer-runtime.md` only when the user explicitly asks for Share Cards, Route/Reach cards, motion, guided stories, deep links, presentation, search/focus, or another Viewer Runtime feature.

## Setup and fallback

No install is required inside the skill package. Verify with:

```bash
node bin/archify.mjs doctor
node bin/archify.mjs demo <output-directory>
```

When shell access is unavailable, hand-place architecture SVG into `assets/template.html`, use CSS semantic classes rather than inline colors, and follow the visual review contract in `references/delivery-contract.md`.

## Output

Return the checked HTML path, diagram type, validation summary, specification/artifact receipt, browser-evidence status, and truthful visual-review status. Do not claim success for a non-zero command or claim visual inspection you did not perform.
````

## File: examples/archify-repo-grid.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Archify Pipeline",
    "subtitle": "Grid placement demo — row/col instead of manual pos",
    "output": "examples/archify-repo-grid.html"
  },
  "layout": {
    "mode": "grid",
    "origin": [40, 100],
    "cols": 7,
    "gapX": 24,
    "gapY": 48,
    "cellW": 120,
    "cellH": 60
  },
  "components": [
    { "id": "user", "type": "external", "label": "You", "sublabel": "NL / Mermaid", "row": 1, "col": 0 },
    { "id": "agents", "type": "frontend", "label": "Agent Hosts", "sublabel": "Claude · Codex", "row": 1, "col": 1 },
    { "id": "skill", "type": "frontend", "label": "SKILL.md", "sublabel": "layout rules", "row": 0, "col": 1 },
    { "id": "ir", "type": "messagebus", "label": "JSON IR", "sublabel": "schema v1", "row": 1, "col": 2 },
    { "id": "schemas", "type": "security", "label": "Schema", "sublabel": "ajv", "row": 0, "col": 2 },
    { "id": "renderers", "type": "backend", "label": "Renderers ×5", "row": 1, "col": 3 },
    { "id": "template", "type": "frontend", "label": "template.html", "row": 1, "col": 4 },
    { "id": "checker", "type": "security", "label": "Output Check", "row": 1, "col": 5 },
    { "id": "html", "type": "cloud", "label": "HTML", "sublabel": "artifact", "row": 1, "col": 6 }
  ],
  "boundaries": [
    {
      "kind": "region",
      "label": "archify/ skill package",
      "wraps": ["ir", "schemas", "renderers", "template", "checker"]
    }
  ],
  "connections": [
    { "from": "user", "to": "agents", "variant": "emphasis" },
    { "from": "agents", "to": "skill", "fromSide": "top", "toSide": "bottom" },
    { "from": "agents", "to": "ir", "variant": "emphasis" },
    { "from": "ir", "to": "schemas", "variant": "security", "fromSide": "top", "toSide": "bottom" },
    { "from": "ir", "to": "renderers", "variant": "emphasis" },
    { "from": "renderers", "to": "template", "variant": "emphasis" },
    { "from": "template", "to": "checker", "variant": "emphasis" },
    { "from": "checker", "to": "html", "variant": "emphasis" }
  ],
  "cards": [
    {
      "dot": "cyan",
      "title": "Grid mode",
      "items": [
        "Set layout.mode grid and place components with row/col",
        "pos still overrides a cell when you need fine tuning",
        "Not auto-layout — fixed cell spacing only"
      ]
    }
  ]
}
````

## File: examples/archify-repo.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Archify",
    "subtitle": "Agent skill → JSON IR → typed renderers → standalone HTML",
    "output": "examples/archify-repo.html"
  },
  "components": [
    {
      "id": "user",
      "type": "external",
      "label": "You",
      "sublabel": "NL or Mermaid",
      "pos": [40, 300],
      "size": [120, 60]
    },
    {
      "id": "agents",
      "type": "frontend",
      "label": "Agent Hosts",
      "sublabel": "Claude · Codex · opencode",
      "pos": [200, 300],
      "size": [150, 60]
    },
    {
      "id": "skill",
      "type": "frontend",
      "label": "SKILL.md",
      "sublabel": "layout judgment",
      "pos": [200, 140],
      "size": [150, 60],
      "tag": "prompt dialect"
    },
    {
      "id": "ir",
      "type": "messagebus",
      "label": "JSON IR",
      "sublabel": "schema_version: 1",
      "pos": [400, 300],
      "size": [140, 60]
    },
    {
      "id": "schemas",
      "type": "security",
      "label": "JSON Schema",
      "sublabel": "ajv strict",
      "pos": [400, 140],
      "size": [140, 60],
      "tag": "fail-closed"
    },
    {
      "id": "renderers",
      "type": "backend",
      "label": "Renderers ×5",
      "sublabel": "layout checks",
      "pos": [590, 300],
      "size": [140, 60],
      "tag": "no auto-layout"
    },
    {
      "id": "template",
      "type": "frontend",
      "label": "template.html",
      "sublabel": "theme + export",
      "pos": [780, 300],
      "size": [140, 60]
    },
    {
      "id": "checker",
      "type": "security",
      "label": "Output Check",
      "sublabel": "SVG gates",
      "pos": [970, 300],
      "size": [140, 60]
    },
    {
      "id": "html",
      "type": "cloud",
      "label": "HTML Artifact",
      "sublabel": "single file",
      "pos": [1160, 300],
      "size": [140, 60]
    },
    {
      "id": "zip",
      "type": "cloud",
      "label": "archify.zip",
      "sublabel": "skill package",
      "pos": [1160, 140],
      "size": [140, 60]
    },
    {
      "id": "ci",
      "type": "backend",
      "label": "CI Gates",
      "sublabel": "golden + zip",
      "pos": [590, 440],
      "size": [140, 60]
    }
  ],
  "boundaries": [
    {
      "kind": "region",
      "label": "archify/ skill package",
      "wraps": ["ir", "schemas", "renderers", "template", "checker"]
    }
  ],
  "connections": [
    {
      "from": "user",
      "to": "agents",
      "variant": "emphasis"
    },
    {
      "from": "agents",
      "to": "skill",
      "fromSide": "top",
      "toSide": "bottom"
    },
    {
      "from": "agents",
      "to": "ir",
      "label": "write IR",
      "variant": "emphasis"
    },
    {
      "from": "ir",
      "to": "schemas",
      "variant": "security",
      "fromSide": "top",
      "toSide": "bottom"
    },
    {
      "from": "ir",
      "to": "renderers",
      "variant": "emphasis"
    },
    {
      "from": "renderers",
      "to": "template",
      "variant": "emphasis"
    },
    {
      "from": "template",
      "to": "checker",
      "variant": "emphasis"
    },
    {
      "from": "checker",
      "to": "html",
      "label": "deliver",
      "variant": "emphasis"
    },
    {
      "from": "renderers",
      "to": "ci",
      "variant": "dashed",
      "fromSide": "bottom",
      "toSide": "top"
    },
    {
      "from": "html",
      "to": "zip",
      "variant": "dashed",
      "fromSide": "top",
      "toSide": "bottom"
    }
  ],
  "cards": [
    {
      "dot": "cyan",
      "title": "Agent loop",
      "items": [
        "Claude / Codex / opencode load the skill",
        "SKILL.md teaches layout judgment, not auto-layout",
        "Mermaid is an input dialect via prompt, not a parser"
      ]
    },
    {
      "dot": "emerald",
      "title": "Render path",
      "items": [
        "JSON IR pins schema_version: 1",
        "Five typed renderers: architecture / workflow / sequence / dataflow / lifecycle",
        "template.html owns theme toggle and 4× export"
      ]
    },
    {
      "dot": "rose",
      "title": "Quality gates",
      "items": [
        "ajv schema validation sits on the IR (fail-closed)",
        "Renderer layout checks, then Output Check on the HTML",
        "CI golden tests and zip freshness stay off the main path"
      ]
    }
  ]
}
````

## File: examples/checkout-platform-delta.receipt.json
````json
{
  "schemaVersion": 1,
  "ok": true,
  "command": "compare",
  "type": "architecture",
  "comparatorVersion": 1,
  "canonicalVersion": 1,
  "completeness": "complete",
  "proofLevel": "authored",
  "base": {
    "title": "Checkout Platform — Baseline",
    "rawSha256": "c112195e7285e3e4aedaeab3e1f85f5891d30fccc2c260aebe4e1da12c80cf84",
    "semanticSha256": "5d2f362ed389af82b117a01d36201e27cb83503093b14c50f7cd8dada55f243a",
    "bytes": 2234
  },
  "head": {
    "title": "Checkout Platform — Fraud Gate",
    "rawSha256": "e3aaf47f77afeadafc81c6ce853dc1df68cc1e6932dec972cf478f4008fdda99",
    "semanticSha256": "0b378c8f24d23ec63feecacd7ff84a4944534f4306fc2b7e3266dff9ba258852",
    "bytes": 2368
  },
  "summary": {
    "components": {
      "added": 1,
      "changed": 1,
      "evidenceChanged": 0,
      "removed": 1,
      "moved": 1
    },
    "connections": {
      "added": 1,
      "changed": 2,
      "removed": 1,
      "rerouted": 1
    },
    "boundaries": {
      "added": 0,
      "changed": 2,
      "removed": 0,
      "geometryChanged": 0
    },
    "presentationChanged": true,
    "provenanceChanged": false
  },
  "changes": {
    "components": [
      {
        "id": "cache",
        "baseLabel": "Session Cache",
        "status": "removed",
        "classifications": [
          "semantic"
        ],
        "changedFields": []
      },
      {
        "id": "checkout",
        "baseLabel": "Checkout API",
        "headLabel": "Checkout API",
        "status": "changed",
        "classifications": [
          "semantic"
        ],
        "changedFields": [
          "/sublabel"
        ]
      },
      {
        "id": "fraud",
        "headLabel": "Fraud Gate",
        "status": "added",
        "classifications": [
          "semantic"
        ],
        "changedFields": []
      },
      {
        "id": "queue",
        "baseLabel": "Order Events",
        "headLabel": "Order Events",
        "status": "moved",
        "classifications": [
          "geometry"
        ],
        "changedFields": [
          "/pos"
        ]
      }
    ],
    "connections": [
      {
        "id": "authorize-payment",
        "base": {
          "from": "orders",
          "to": "payments",
          "label": "authorize"
        },
        "head": {
          "from": "fraud",
          "to": "payments",
          "label": "authorize"
        },
        "status": "changed",
        "classifications": [
          "geometry",
          "topology"
        ],
        "changedFields": [
          "/from",
          "/fromSide",
          "/toSide",
          "/via"
        ]
      },
      {
        "id": "fraud-check",
        "head": {
          "from": "checkout",
          "to": "fraud",
          "label": "screen"
        },
        "status": "added",
        "classifications": [
          "topology"
        ],
        "changedFields": []
      },
      {
        "id": "persist-order",
        "base": {
          "from": "checkout",
          "to": "orders",
          "label": "SQL"
        },
        "head": {
          "from": "checkout",
          "to": "orders",
          "label": "SQL tx"
        },
        "status": "changed",
        "classifications": [
          "semantic"
        ],
        "changedFields": [
          "/label"
        ]
      },
      {
        "id": "publish-order",
        "base": {
          "from": "checkout",
          "to": "queue",
          "label": "accepted"
        },
        "head": {
          "from": "checkout",
          "to": "queue",
          "label": "accepted"
        },
        "status": "rerouted",
        "classifications": [
          "geometry"
        ],
        "changedFields": [
          "/labelDy"
        ]
      },
      {
        "id": "session-read",
        "base": {
          "from": "checkout",
          "to": "cache",
          "label": "session"
        },
        "status": "removed",
        "classifications": [
          "topology"
        ],
        "changedFields": []
      }
    ],
    "boundaries": [
      {
        "key": "region:Production region",
        "kind": "region",
        "label": "Production region",
        "status": "changed",
        "classifications": [
          "scope"
        ],
        "changedFields": [
          "/wraps"
        ]
      },
      {
        "key": "security-group:Checkout trust zone",
        "kind": "security-group",
        "label": "Checkout trust zone",
        "status": "changed",
        "classifications": [
          "scope"
        ],
        "changedFields": [
          "/wraps"
        ]
      }
    ]
  },
  "identity": {
    "components": "components[].id",
    "connections": "connections[].id (required)",
    "boundaries": "boundaries[].kind + boundaries[].label (derived)"
  },
  "view": {
    "visualPreset": "signal-flow"
  },
  "limitations": [
    "Authored Architecture IR only; no runtime impact, causality, risk, or mergeability is inferred.",
    "Boundary identity is conservatively derived from kind + label."
  ],
  "artifact": {
    "sha256": "4dfa76443ff644609ff0a4f7e6117a4a5d977a57db63258417d192f9f8072293",
    "bytes": 2213635
  },
  "validation": {
    "checksPassed": 28,
    "checkCount": 28,
    "baseComposition": "pass",
    "headComposition": "pass"
  }
}
````

## File: examples/maka-architecture.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "Maka",
    "subtitle": "Local-first desktop AI workbench — sessions, tools, permissions, recovery",
    "output": "examples/maka-architecture.html"
  },
  "components": [
    {
      "id": "user",
      "type": "external",
      "label": "You",
      "sublabel": "desktop user",
      "pos": [40, 300],
      "size": [120, 60]
    },
    {
      "id": "ui",
      "type": "frontend",
      "label": "Desktop UI",
      "sublabel": "React renderer",
      "pos": [200, 300],
      "size": [140, 60]
    },
    {
      "id": "main",
      "type": "backend",
      "label": "Main Process",
      "sublabel": "Electron IPC",
      "pos": [390, 300],
      "size": [140, 60]
    },
    {
      "id": "session",
      "type": "backend",
      "label": "SessionManager",
      "sublabel": "public runtime API",
      "pos": [580, 300],
      "size": [150, 60]
    },
    {
      "id": "agentrun",
      "type": "backend",
      "label": "AgentRun",
      "sublabel": "turn + recovery",
      "pos": [780, 300],
      "size": [140, 60]
    },
    {
      "id": "model",
      "type": "backend",
      "label": "ModelAdapter",
      "sublabel": "stream + usage",
      "pos": [970, 300],
      "size": [140, 60]
    },
    {
      "id": "providers",
      "type": "cloud",
      "label": "Model Providers",
      "sublabel": "AI SDK / Ollama",
      "pos": [970, 140],
      "size": [140, 60],
      "tag": "API keys local"
    },
    {
      "id": "bots",
      "type": "external",
      "label": "Bots & Gateway",
      "sublabel": "Telegram · Feishu · HTTP",
      "pos": [580, 140],
      "size": [150, 60]
    },
    {
      "id": "permission",
      "type": "security",
      "label": "Permission",
      "sublabel": "policy engine",
      "pos": [780, 140],
      "size": [140, 60],
      "tag": "fail-closed"
    },
    {
      "id": "storage",
      "type": "database",
      "label": "Local Storage",
      "sublabel": "userData JSONL",
      "pos": [580, 440],
      "size": [150, 60]
    },
    {
      "id": "toolrt",
      "type": "messagebus",
      "label": "ToolRuntime",
      "sublabel": "validate · abort",
      "pos": [780, 440],
      "size": [140, 60]
    },
    {
      "id": "tools",
      "type": "frontend",
      "label": "Local Tools",
      "sublabel": "Read · Write · Bash",
      "pos": [970, 440],
      "size": [140, 60]
    }
  ],
  "boundaries": [
    {
      "kind": "region",
      "label": "Electron app + packages/runtime",
      "wraps": ["ui", "main", "session", "agentrun", "model", "toolrt", "storage", "permission"]
    },
    {
      "kind": "security-group",
      "label": "trust boundary",
      "wraps": ["permission", "storage"]
    }
  ],
  "connections": [
    {
      "from": "user",
      "to": "ui",
      "variant": "emphasis"
    },
    {
      "from": "ui",
      "to": "main",
      "label": "IPC",
      "variant": "emphasis"
    },
    {
      "from": "main",
      "to": "session",
      "variant": "emphasis"
    },
    {
      "from": "session",
      "to": "agentrun",
      "label": "turn",
      "variant": "emphasis"
    },
    {
      "from": "agentrun",
      "to": "model",
      "variant": "emphasis"
    },
    {
      "from": "model",
      "to": "providers",
      "label": "stream",
      "variant": "emphasis",
      "fromSide": "top",
      "toSide": "bottom"
    },
    {
      "from": "bots",
      "to": "session",
      "variant": "dashed",
      "fromSide": "bottom",
      "toSide": "top"
    },
    {
      "from": "agentrun",
      "to": "permission",
      "variant": "security",
      "fromSide": "top",
      "toSide": "bottom"
    },
    {
      "from": "session",
      "to": "storage",
      "variant": "dashed",
      "fromSide": "bottom",
      "toSide": "top"
    },
    {
      "from": "agentrun",
      "to": "toolrt",
      "fromSide": "bottom",
      "toSide": "top"
    },
    {
      "from": "toolrt",
      "to": "tools",
      "variant": "emphasis"
    },
    {
      "from": "toolrt",
      "to": "permission",
      "variant": "security",
      "fromSide": "bottom",
      "toSide": "top",
      "via": [[850, 540], [1160, 540], [1160, 100], [850, 100]]
    }
  ],
  "cards": [
    {
      "dot": "cyan",
      "title": "Desktop surfaces",
      "items": [
        "apps/desktop: renderer, preload, main process",
        "Settings for models, bots, search, gateway, permissions",
        "Bots and open gateway share SessionManager as the public API"
      ]
    },
    {
      "dot": "emerald",
      "title": "Runtime kernel",
      "items": [
        "SessionManager → AgentRun → AiSdkBackend",
        "ModelAdapter normalizes provider streams and usage",
        "ToolRuntime owns tool validation, abort, and telemetry"
      ]
    },
    {
      "dot": "rose",
      "title": "Local & privacy",
      "items": [
        "Sessions and credentials live under Electron userData",
        "Write/Bash and risky ops go through the permission engine",
        "Renderer never sees plaintext secrets — only masked status"
      ]
    }
  ]
}
````

## File: examples/rag-pipeline.architecture.json
````json
{
  "schema_version": 1,
  "diagram_type": "architecture",
  "meta": {
    "title": "RAG Pipeline",
    "output": "rag-pipeline.html",
    "quality_profile": "showcase",
    "views": [
      { "id": "query-path", "label": "Query path", "focus": ["user", "guardrail", "orchestrator", "retriever", "vectordb", "reranker", "llm"], "note": "Follow a user question from input through safety filtering, retrieval, and generation to grounded answer." },
      { "id": "ingestion", "label": "Document ingestion", "focus": ["sources", "loader", "chunker", "embedder", "vectordb"], "note": "How raw documents become searchable vector embeddings." },
      { "id": "safety-and-cache", "label": "Safety and cache", "focus": ["user", "guardrail", "orchestrator", "cache", "llm"], "note": "The guardrail intercepts harmful queries before they reach the orchestrator; the semantic cache avoids redundant LLM calls." }
    ]
  },
  "components": [
    { "id": "user", "type": "external", "label": "User", "sublabel": "Chat / API", "pos": [30, 200], "size": [100, 50] },
    { "id": "guardrail", "type": "security", "label": "Guardrail", "sublabel": "Input filter", "pos": [160, 200], "size": [110, 50], "tag": "PII + toxicity" },
    { "id": "orchestrator", "type": "backend", "label": "Orchestrator", "sublabel": "LangGraph agent", "pos": [310, 200], "size": [130, 54] },
    { "id": "cache", "type": "database", "label": "Semantic Cache", "sublabel": "Redis :6379", "pos": [310, 70], "size": [130, 50] },
    { "id": "retriever", "type": "backend", "label": "Retriever", "sublabel": "Hybrid search", "pos": [480, 200], "size": [120, 54] },
    { "id": "vectordb", "type": "database", "label": "Vector Store", "sublabel": "Milvus", "pos": [480, 285], "size": [120, 50], "tag": "HNSW index" },
    { "id": "reranker", "type": "backend", "label": "Reranker", "sublabel": "Cross-encoder", "pos": [640, 200], "size": [120, 54] },
    { "id": "llm", "type": "cloud", "label": "LLM", "sublabel": "Claude API", "pos": [800, 200], "size": [110, 54] },
    { "id": "sources", "type": "external", "label": "Documents", "sublabel": "PDF / Web / DB", "pos": [200, 390], "size": [120, 50] },
    { "id": "loader", "type": "backend", "label": "Loader", "sublabel": "Parse + extract", "pos": [360, 390], "size": [110, 50] },
    { "id": "chunker", "type": "backend", "label": "Chunker", "sublabel": "Semantic split", "pos": [510, 390], "size": [110, 50] },
    { "id": "embedder", "type": "cloud", "label": "Embedding", "sublabel": "text-embedding-3", "pos": [670, 390], "size": [120, 50] }
  ],
  "boundaries": [
    { "kind": "region", "label": "Query Runtime", "wraps": ["guardrail", "orchestrator", "cache", "retriever", "reranker", "llm"] },
    { "kind": "security-group", "label": "Ingestion Pipeline", "wraps": ["loader", "chunker", "embedder"] }
  ],
  "connections": [
    { "id": "user-to-guardrail", "from": "user", "to": "guardrail", "label": "question", "variant": "emphasis", "labelDy": -19 },
    { "id": "guardrail-to-orchestrator", "from": "guardrail", "to": "orchestrator", "label": "validated query", "variant": "security", "labelDy": -19 },
    { "id": "cache-lookup", "from": "orchestrator", "to": "cache", "label": "semantic match", "fromSide": "top", "toSide": "bottom", "labelAt": [450, 155] },
    { "id": "orchestrator-to-retriever", "from": "orchestrator", "to": "retriever", "label": "retrieve", "labelDy": -21 },
    { "id": "retriever-to-vectordb", "from": "retriever", "to": "vectordb", "label": "ANN search", "fromSide": "bottom", "toSide": "top", "labelAt": [570, 265] },
    { "id": "retriever-to-reranker", "from": "retriever", "to": "reranker", "label": "top-k docs", "labelDy": -21 },
    { "id": "reranker-to-llm", "from": "reranker", "to": "llm", "label": "context", "labelDy": -21 },
    { "id": "llm-response", "from": "llm", "to": "orchestrator", "label": "grounded answer", "variant": "dashed", "fromSide": "top", "toSide": "top", "via": [[855, 130], [375, 130]] },
    { "id": "orchestrator-to-user", "from": "orchestrator", "to": "user", "label": "response", "variant": "emphasis", "fromSide": "bottom", "toSide": "bottom", "via": [[375, 285], [80, 285]] },
    { "id": "sources-to-loader", "from": "sources", "to": "loader", "label": "raw docs", "variant": "dashed", "labelAt": [280, 365] },
    { "id": "loader-to-chunker", "from": "loader", "to": "chunker", "label": "parsed text", "labelDy": -19 },
    { "id": "chunker-to-embedder", "from": "chunker", "to": "embedder", "label": "chunks", "labelDy": -19 },
    { "id": "embedder-to-vectordb", "from": "embedder", "to": "vectordb", "label": "vectors", "variant": "dashed", "fromSide": "top", "toSide": "top", "via": [[730, 275], [540, 275]] }
  ],
  "cards": [
    { "dot": "emerald", "title": "Retrieval", "items": ["Hybrid search: dense vectors + sparse BM25", "Cross-encoder reranker for precision", "Top-k context window management"] },
    { "dot": "cyan", "title": "Generation", "items": ["Claude API for grounded generation", "Semantic cache reduces repeat LLM calls", "Streaming response with citations"] },
    { "dot": "rose", "title": "Safety", "items": ["Input guardrail filters PII and toxic content", "Output grounding reduces hallucination risk", "Document-level access control in retriever"] }
  ]
}
````

## File: integrations/deepseek-harness/package.json
````json
{
  "name": "@tt-a1i/archify-dsh",
  "version": "0.2.0",
  "description": "Opt-in DeepSeek Harness Skill-only bundle for the Archify architecture-diagram skill.",
  "license": "MIT",
  "type": "module",
  "main": "./lib/index.js",
  "exports": {
    ".": "./lib/index.js",
    "./package.json": "./package.json"
  },
  "files": [
    "lib",
    "cordis.patch.yml",
    "skills",
    "README.md",
    "LICENSE",
    "release.json"
  ],
  "keywords": [
    "dsh-plugin",
    "deepseek-harness",
    "agent-skill",
    "architecture-diagram"
  ],
  "engines": {
    "node": "^22.19.0 || >=24.0.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/tt-a1i/archify.git",
    "directory": "integrations/deepseek-harness"
  },
  "homepage": "https://github.com/tt-a1i/archify/tree/main/integrations/deepseek-harness",
  "bugs": "https://github.com/tt-a1i/archify/issues",
  "publishConfig": {
    "access": "public"
  },
  "dsh": {
    "bundle": {
      "patch": "./cordis.patch.yml"
    }
  }
}
````

## File: README.md
````markdown
<p align="center">
  <strong>English</strong> · <a href="./README_ZH.md">简体中文</a>
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/31352?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-31352" target="_blank" rel="noopener noreferrer"><img src="https://trendshift.io/api/badge/repositories/31352" alt="Archify on Trendshift" width="250" height="55"/></a>
</p>

![Archify product preview](docs/assets/archify-readme-hero.png)

# Archify

**Turn a codebase or system description into a polished, interactive system map — directly in chat.**

Archify is a Node.js rendering and validation system for Cursor, Claude Code, Codex CLI, and OpenCode. Agents produce typed JSON IR; Archify deterministically compiles it into HTML/SVG.

- **Open it and present** — five diagram types, four presets, dark/light themes, built-in brand marks, and finite motion
- **Review architecture changes before merge** — compare two validated snapshots as Before / Delta / After, with exact added, removed, changed, moved, and rerouted facts
- **Every interaction stays grounded** — search nodes, optionally open revision-verified source, trace upstream/downstream authored reach and exact routes, compare roles, and play guided stories without inventing topology
- **One file, ready to trust and share** — typed JSON IR and deterministic checks produce self-contained HTML plus PNG, SVG, WebM, and 1200×630 share cards

![License](https://img.shields.io/badge/license-MIT-22c55e?style=flat-square)
![Agent Skill](https://img.shields.io/badge/Agent-Skill-7C3AED?style=flat-square)
![Development Version](https://img.shields.io/badge/version-2.17.0--dev.1-0891b2?style=flat-square)

**Current development version:** `v2.17.0-dev.1`. See [Changelog](CHANGELOG.md#unreleased).

**[Project page](https://tt-a1i.github.io/archify/)** · **[Scenario guide](https://tt-a1i.github.io/archify/guide.html)** · **[Proof Lab](https://tt-a1i.github.io/archify/gallery.html)**

```bash
npx skills add tt-a1i/archify -g
```

Using Cursor? Open the [agent-aware quick start](https://tt-a1i.github.io/archify/start.html?agent=cursor&type=architecture) for exact global and project commands.

**No repository is required:** describe the system in any agent chat.

## ❤️ Sponsors

<table>
  <tr><td align="center" width="240"><a href="https://apinebula.ai/ref/wywnaATT"><img src="docs/assets/sponsors/apinebula-archify.jpg" alt="APINEBULA" width="200" /></a><br/><strong><a href="https://apinebula.ai/ref/wywnaATT">APINEBULA</a></strong></td><td>APINEBULA sponsors Archify with one API for Claude, GPT, Gemini, and more. <a href="https://apinebula.ai/ref/wywnaATT">Register through Archify</a> and use <strong><code>Archify</code></strong> for <strong>10% off</strong>.</td></tr>
  <tr><td align="center" width="240"><a href="https://github.com/EverMind-AI/Raven"><img src="docs/assets/sponsors/evermind-archify-raven.png" alt="Archify × Raven" width="200" /></a><br/><strong><a href="https://github.com/EverMind-AI">EverMind</a> · <a href="https://github.com/EverMind-AI/Raven">Raven</a></strong></td><td>EverMind sponsors Archify and builds memory infrastructure for agents. Its <a href="https://github.com/EverMind-AI/Raven"><strong>Raven</strong></a> harness supports Archify as a Skill for verified, interactive system maps.</td></tr>
</table>

> Want to sponsor Archify? [Contact us by email.](mailto:2801884530@qq.com)

## See Archify in action

These are generated Archify artifacts, not product mockups. Click a frame to open its live, shareable state.

<p align="center">
  <a href="https://tt-a1i.github.io/archify/gallery.html"><img src="docs/assets/archify-live-proof.gif" alt="Three verified Archify artifacts moving through Signal Flow, Blueprint, and Classic presets" width="960"/></a>
  <br/>
  <sub><strong>Three real generated artifacts.</strong> Signal Flow · Blueprint · Classic · <a href="https://tt-a1i.github.io/archify/gallery.html">open the interactive Proof Lab ↗</a></sub>
</p>

| Guided story | Route probe | Semantic lens |
|---|---|---|
| [![Agent workflow playing one authored chapter](docs/assets/archify-demo-story.png)](https://tt-a1i.github.io/archify/gallery/artifacts/agent-tool-call.workflow.html?theme=dark&present=1&play=1#view=happy-path) | [![Cache-miss sequence showing the Web App to Postgres route](docs/assets/archify-demo-route.png)](https://tt-a1i.github.io/archify/gallery/artifacts/cache-miss.sequence.html?theme=dark&present=1#route=web~db) | [![Production architecture comparing backend and database roles](docs/assets/archify-demo-lens.png)](https://tt-a1i.github.io/archify/gallery/artifacts/production-deployment.architecture.html?theme=dark&present=1#lens=backend~database) |
| Play one finite named chapter. | Inspect the shortest authored directed path. | Compare real traffic between semantic roles. |

The [Proof Lab](https://tt-a1i.github.io/archify/gallery.html) contains all 11 checked-in scenarios, their JSON sources, named views, and validation receipts.

### A real repository, mapped from source

[![MCO runtime architecture generated from the public mco-org/mco repository](docs/assets/mco-runtime-share-card.png)](https://tt-a1i.github.io/archify/cases/mco-runtime.architecture.html?theme=dark&present=1#view=dispatch-path)

Archify traced [`mco-org/mco`](https://github.com/mco-org/mco) at `9f1a1cf` and produced this checked map. **[Open it ↗](https://tt-a1i.github.io/archify/cases/mco-runtime.architecture.html?theme=dark&present=1#view=dispatch-path)** · [trace reach ↗](https://tt-a1i.github.io/archify/cases/mco-runtime.architecture.html?theme=dark#focus=router&reach=downstream) · [typed source](docs/cases/mco-runtime.architecture.json)

## Preview

Same diagram, two themes, one click to switch:

| Dark | Light |
|---|---|
| ![Dark theme](docs/assets/archify-dark.png) | ![Light theme](docs/assets/archify-light.png) |

The Export menu copies PNG to the clipboard and downloads static or motion formats:

![Export menu](docs/assets/archify-menu.png)

Use **Copy Share Card** when you want a canonical 1200×630 image for a README, release, or social post.

After tracing a route, **Export → Route Share Card** downloads that authored path as a 1200×630 PNG with the full diagram retained for context.

![Route Share Card showing the exact Users to API Server path with the full architecture retained as context](docs/assets/archify-route-share-card.png)

After tracing authored `Upstream` or `Downstream` reach, **Export → Reach Share Card** captures that exact reading without claiming runtime impact.

![MCO downstream Reach Share Card showing authored relationships from Command Router](docs/assets/mco-runtime-reach-share-card.png)

Open [`examples/web-app.html`](examples/web-app.html) locally to try the complete viewer.

## Quick start

### 1. Install

```bash
npx skills add tt-a1i/archify -g
```

For an explicit, non-interactive Cursor install:

```bash
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```

To try without installing:

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

[DSH community opt-in](integrations/deepseek-harness/README.md): `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`

The [agent switcher](https://tt-a1i.github.io/archify/start.html?agent=cursor&type=architecture) covers `cursor`, `codex`, `claude-code`, and `opencode`. For Raven's manual ZIP install, extract [`archify.zip`](archify.zip) into `~/.raven/workspace/skills`; it yields `~/.raven/workspace/skills/archify`. Raven is not a switcher target.

Archify may GET the fixed stable manifest solely to show an optional reminder; it never downloads or installs updates. Successful checks wait about 72 hours (±20%); active use retries failures after 6, then 24 hours. The server sees normal HTTP metadata (IP and time), but receives no version, Agent, project data, prompts, account/device ID, or ETag. You decide whether and when to update. Set `ARCHIFY_UPDATE_CHECK_DISABLED=1` to disable networking and reminder-state writes.

### 2. Start from a description — no repository required

```text
Use Archify to draw: Browser -> API -> Redis cache -> PostgreSQL fallback.
```

For source evidence, open a repository and ask:

```text
Analyze this repository, then use archify to create a high-level runtime architecture diagram.
Show 8–12 core components, one primary path, external dependencies, and trust boundaries.
Put supporting detail in cards instead of adding more edges.
```

### 3. Refine in chat

Continue with focused requests such as `add Redis`, `move auth to the left`, or `highlight the rollback path`. Archify keeps the typed source available for targeted iteration.

## Choose the right diagram

| Type | Best for | Include in your prompt |
|---|---|---|
| **Architecture** | Components, services, storage, boundaries | Scope, core components, primary path |
| **Workflow** | CI/CD, approvals, tool calls, runbooks | Participants, order, branches, exceptions |
| **Sequence** | API calls, cache fallback, auth, async traces | Callers, callees, returns, timing |
| **Data Flow** | Pipelines, lineage, PII, consumers | Sources, transforms, stores, boundaries |
| **Lifecycle** | States, retries, waits, terminal outcomes | States, events, retry and cancellation paths |

Architecture's optional `deployment-ownership` profile fails closed when authored owners, region placement, private database scope, or named crossings are missing; it is never implicit and does not inspect live infrastructure. See the [checked deployment proof](https://tt-a1i.github.io/archify/gallery.html#proof-deployment-ownership).

For design or PR review, Architecture Delta compares validated Before / Delta / After snapshots with a machine receipt. Select an authored change or play one finite, viewer-only Review; it infers no impact, risk, or merge safety.

`node archify/bin/archify.mjs compare architecture base.json head.json architecture-delta.html --json`

[![Architecture Delta showing added, removed, changed, and moved authored facts](docs/assets/architecture-delta-proof.jpg)](examples/checkout-platform-delta.html)

Not sure which one fits? Use the [interactive scenario guide](https://tt-a1i.github.io/archify/guide.html), or ask the zero-dependency CLI:

```bash
node archify/bin/archify.mjs guide "Show an API request with Redis cache miss"
node archify/bin/archify.mjs guide "Map Kafka topics, consumer groups, replay, and DLQ" --json
```

Workflow keeps the happy path clear across lanes:

![Workflow example](docs/assets/archify-workflow.png)

Sequence explains one interaction over time:

![Sequence example](docs/assets/archify-sequence.png)

Data Flow makes movement and sensitivity boundaries explicit:

![Data Flow example](docs/assets/archify-dataflow.png)

Lifecycle separates progress, waits, retries, and terminal outcomes:

![Lifecycle example](docs/assets/archify-lifecycle.png)

Architecture examples: [`web-app`](examples/web-app.html) · [`Archify pipeline`](examples/archify-repo.html) · [`grid placement`](examples/archify-repo-grid.html) · [`desktop agent`](examples/maka-architecture.html)

## Why Archify

- **Layout judgment over generic auto-layout** — the agent chooses hierarchy, spacing, routes, and emphasis; shared automatic endpoints spread deterministically instead of piling arrows on one midpoint.
- **Typed JSON IR** — every renderer-backed mode has a schema and reproducible source.
- **Atomic validation before delivery** — schema, layout, HTML/SVG, route, and label-to-route clearance checks must all pass before a showcase artifact replaces the last known good output.
- **Failures come with a repair receipt** — `validate --json` and `deliver --json` return stable rule codes, the exact subject, measured evidence, and only supported repair controls instead of a Node stack or an unstructured retry guess.
- **Last-good live preview** — an optional desktop loop watches one JSON file, refreshes only after the latest candidate passes every gate, and keeps the previous verified diagram visible when a save is incomplete or invalid.
- **Truthful interaction** — focus, upstream/downstream reach, exact routes, role comparison, and stories reuse authored nodes and relationships instead of inventing topology or claiming runtime impact.
- **Source evidence, only when requested** — Evidence-backed Architecture nodes mark themselves `SRC n` and open Git-verified files and line ranges pinned to one public commit; ordinary artifacts stay source-free.
- **Portable by default** — the result is one HTML file; exports remain full-diagram and free of temporary viewer state.

Archify is not a general-purpose drawing editor or a Mermaid theme. It turns technical intent into a communication artifact.

## How it works

| Step | What happens |
|---|---|
| **Generate** | The agent creates typed JSON IR from your description. |
| **Validate** | Bundled validators and layout rules check the source; failures identify the exact local repair in machine-readable JSON. |
| **Preview (optional)** | A loopback-only desktop session watches one source and reloads only verified revisions; failures keep the last-good artifact. |
| **Deliver** | A same-directory candidate is rendered and checked; only a passing artifact atomically replaces the target, then optional `--open` launches that exact file. |
| **Iterate** | The agent updates the source while unrelated structure stays stable. |

Useful repository commands:

```bash
cd archify
node bin/archify.mjs doctor
node bin/archify.mjs demo /tmp/archify-demo
node bin/archify.mjs guide "Show CI/CD checks, approval, deploy, and rollback"
node bin/archify.mjs validate workflow examples/agent-tool-call.workflow.json --quality showcase --json
node bin/archify.mjs preview workflow examples/agent-tool-call.workflow.json /tmp/workflow.html --quality showcase
node bin/archify.mjs deliver workflow examples/agent-tool-call.workflow.json /tmp/workflow.html --quality showcase --open --json
```

`preview` is an explicit loopback-only desktop mode: it watches one JSON file on a random `127.0.0.1` port, keeps the last verified output through failures, stops with Ctrl-C, and adds no generated-HTML runtime. Use `--no-open` for tests or manual URL opening.

`deliver --open` is an opt-in one-shot handoff after commit. Opener failure preserves success; JSON remains on stdout and the absolute fallback path goes to stderr.

On failure, `validate --json` and `deliver --json` emit one JSON object. Apply only each `diagnostics[]` subject's `supportedFixes`, within the Skill's two correction rounds; visual review remains separate.

Settings:

```json
{
  "meta": {
    "locale": "en",
    "animation": "trace",
    "visual_preset": "signal-flow"
  }
}
```

`meta.locale=en|zh-CN` localizes page title, Legend, states/errors, a11y, HTML/SVG `lang`—never authored content. Otherwise omit; preserve requested-language copy; disclose English fallback. Static omits `animation`; `classic` defaults.

## Explore and share the output

| Action | Control |
|---|---|
| Open the factual Diagram Guide | <kbd>?</kbd> |
| Find and focus a semantic node | <kbd>/</kbd> |
| Trace upstream/downstream authored reach | Focus a node → `Upstream` / `Downstream` |
| Probe a directed route and inspect its journey | <kbd>R</kbd> or `PATH` |
| Compare one or two semantic roles | <kbd>L</kbd> or `LENS` |
| Open the live overview radar | <kbd>M</kbd> or `MAP` |
| Play a guided story / change chapter | <kbd>P</kbd> / <kbd>[</kbd> <kbd>]</kbd> |
| Enter Presentation Stage | <kbd>F</kbd> |
| Choose visual style (`S` cycles) / toggle theme / open Export | <kbd>S</kbd> / <kbd>T</kbd> / <kbd>E</kbd> |
| Zoom or reset | <kbd>+</kbd> / <kbd>-</kbd> / <kbd>0</kbd> |

Stable links can restore `#focus=<id>`, `#focus=<id>&reach=upstream|downstream`, `#relation=<id>`, `#route=<source>~<target>`, `#lens=<kind>~<kind>`, and `#view=<view-id>`. Reader-driven motion is finite, respects `prefers-reduced-motion`, and never enters canonical exports.

The complete generation and viewer contract lives in [`archify/SKILL.md`](archify/SKILL.md).

## Installation options

| Surface | Install location or method | Capability |
|---|---|---|
| **Raven** | Manual ZIP into `~/.raven/workspace/skills` → `~/.raven/workspace/skills/archify` | Full renderer + validation workflow |
| **Claude Code** | `~/.claude/skills/` or `.claude/skills/` | Full renderer + validation workflow |
| **Codex CLI** | `~/.agents/skills/` or `.agents/skills/` | Full renderer + validation workflow |
| **opencode** | `~/.config/opencode/skills/`, `.opencode/skills/`, or `.agents/skills/` | Full renderer + validation workflow |
| **Claude.ai** | Upload `archify.zip` under Settings → Capabilities → Skills | Depends on Node.js access in the sandbox |
| **Project Knowledge** | Upload `archify.zip` to the project | Prompt-driven architecture fallback |
| **DeepSeek Harness** | Opt-in: `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`. Invoke: `Use the archify skill to map this repository's runtime architecture.` Remove: `dsh plugin --profile web remove @tt-a1i/archify-dsh`. | Community integration for developer-preview `@deepseek-ai/dsh@0.1.0-rc.6`; Node `^22.19.0 \|\| >=24.0.0`; not an official DeepSeek product. No telemetry. Shell files need exact workspace paths, not Web Produced Files. [Details](integrations/deepseek-harness/README.md). |

## Reference and scope

- [Schema reference](archify/schemas/README.md) · [Skill](archify/SKILL.md) · [Examples](archify/examples/) · [Agent cookbook](docs/authoring-cookbook.md)
- [Changelog](CHANGELOG.md)
- [Roadmap](ROADMAP.md)
- [Generated Proof Lab](https://tt-a1i.github.io/archify/gallery.html)

Automatic Mermaid parsing, general-purpose auto-layout, hosted sharing, and WYSIWYG editing are intentionally outside the current scope.

## License

[MIT](LICENSE) — free to use, modify, and distribute.

## Contributing

Issues, pull requests, and real-world diagrams are welcome. Start with the [contribution guide](CONTRIBUTING.md), use the reproducible bug form for failures, or submit a validated diagram through the [community showcase form](https://github.com/tt-a1i/archify/issues/new?template=showcase.yml).&nbsp;·&nbsp;[LINUX&nbsp;DO](https://linux.do)

## Star History

<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/tt-a1i/archify/star-history/assets/star-history-dark.svg" /><img alt="Star History" src="https://raw.githubusercontent.com/tt-a1i/archify/star-history/assets/star-history-light.svg" /></picture></p>
````
