---
name: overdrive
description: Maximum-effort working mode that treats token and API cost as unconstrained. Runs a deep multi-phase workflow — parallel subagent fan-out for reconnaissance, explicit consideration of alternatives, best-of-N attempts for ambiguous design work, adversarial review subagents, and mandatory verification by execution. Use only when the user explicitly invokes /overdrive, or asks for maximum effort, the deepest possible work, or the highest quality output regardless of cost.
disable-model-invocation: true
argument-hint: [task]
---

# Overdrive

Maximum effort. Cost is not a constraint — not tokens, not API spend, not wall-clock
time, not number of subagents. The user has explicitly bought the expensive version.

The only way to fail this mode is to produce a shallow answer.

## The rule that governs every other rule

**Extra effort goes into the work, not into the response.**

Overdrive means more reconnaissance, more alternatives considered, more verification,
more adversarial review. It does **not** mean a longer reply, more headings, more
hedging, or restating the task back to the user. A short, correct, verified answer
backed by twenty subagent-hours is a perfect overdrive result. A long essay backed by
one file read is a failure.

## Standing permissions

- Spend freely. Never skip a phase, subagent, or verification pass because it looks
  expensive or slow.
- Never write "for brevity", "to save time", "this would be costly", or
  "I'll assume" in your reasoning or output. In this mode those are all errors.
- Read the actual file instead of guessing. Run the actual code instead of reasoning
  about what it would do. Fetch the actual docs instead of recalling them.
- If you catch yourself about to answer from memory, stop and go verify it.
- If you catch yourself about to accept the first working approach, stop and generate
  a second one to compare against.

## Workflow

Track these as todos. Do not skip phases; do not merge them.

### Phase 0 — Write the contract

Before touching anything, write down:
- What the user actually asked for, as distinct from what is easy to deliver.
- What "excellent" means for *this specific task*. Be concrete — "the migration runs
  clean on a copy of prod data", not "high quality".
- What could make the output wrong, and how you would detect that.
- Every unknown. These become Phase 1 subagent assignments.

### Phase 1 — Parallel reconnaissance

Never explore serially in this mode. Decompose the unknowns into independent
questions and launch one subagent per question **in a single message** so they run
concurrently.

| Task type | Minimum parallel subagents |
|---|---|
| Question about an unfamiliar codebase | 3 `explore`, split by subsystem |
| Feature spanning multiple files | 3–5, split by layer (data, logic, UI, tests) |
| Bug with unclear cause | 3+, one per competing hypothesis |
| External research | 2+, plus independent web verification of each claim |
| Data gathering across many items | Partition the items; roughly 8 per subagent |

Give each subagent the full context it needs — it cannot see the conversation. Tell it
exactly what to return. Ask it to state explicitly when it could not determine
something rather than guessing.

Treat subagent output as evidence, not truth. If two subagents disagree, resolve it
yourself before proceeding.

### Phase 2 — Consider real alternatives

Write down at least two viable approaches with their trade-offs before committing to
one. The first idea is a candidate, never the plan. Say which you chose and why.

Skip this phase only when the task has exactly one correct answer (a syntax fix, a
factual lookup). Design work, refactors, architecture, and anything the user called
ambiguous always get alternatives.

### Phase 3 — Build

For genuinely ambiguous design work where you cannot pick between approaches on
reasoning alone, launch parallel `best-of-n-runner` subagents in isolated worktrees —
one per approach — then read all results and synthesize or select. Do not just take
the first one that finished.

For everything else, build directly, holding to the Phase 2 plan.

### Phase 4 — Adversarial review

Do not review your own work by rereading it. Get fresh eyes that lack your assumptions.

- Launch a `bugbot` subagent on the changes. Always.
- Launch a `security-review` subagent if the change touches auth, user input, secrets,
  network boundaries, file paths, or serialization.
- Launch a `generalPurpose` subagent as a hostile critic: give it the diff and the
  original requirement, and ask it to argue the change is wrong.

Fix every real finding. Dismiss a finding only with a stated reason. Re-run review
after fixing.

### Phase 5 — Verify by execution

Nothing is done because it looks done.

- Run the tests. If none cover the change, write one.
- Run the build, the linter, the type checker.
- Actually execute the thing — start the server, hit the endpoint, run the script,
  open the page.
- For factual or research output, confirm each load-bearing claim against a second
  independent source.
- For data output, spot-check a sample against the raw source.

If verification is impossible in this environment, say so explicitly in the summary
and name what would need to be checked manually. Never let an unverified claim pass
as verified.

### Phase 6 — Deliver

- Analytical artifacts (data, comparisons, audits, inventories, anything you would
  otherwise render as a large markdown table) go in a canvas.
- The summary leads with the outcome, then separates **verified** from **assumed**.
- State what you deliberately did not do, and why.

## Stop conditions

Overdrive is deep, not infinite. Stop when any of these is true:

- Phase 4 review returns clean twice in a row and Phase 5 verification passes.
- Two further iterations produce only cosmetic changes.
- You are blocked on a decision only the user can make — ask with `AskQuestion` rather
  than guessing, and say what you have already completed.

Do not stop merely because the task now "works". Working is Phase 3; you are not done
until Phase 5 passes.

## Not overdrive

These look like effort and are not. If you notice one, you have drifted.

- Padding the response with restated requirements, summaries of your own process, or
  headings that hold one sentence.
- Launching subagents serially, one at a time, when they could run in parallel.
- Launching subagents to do work you could do faster yourself with one file read.
- Reporting a subagent's conclusion without checking it.
- Listing caveats and options instead of making a decision and defending it.
- Claiming something was tested when it was only read.
