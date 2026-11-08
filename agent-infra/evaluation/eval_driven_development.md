# Eval-Driven Development for LLM Features: From Policy Doc to Pull Request

*A practical workflow, with human checkpoints and an AI coding agent doing the volume. November 2026.*

Part of the [evaluation section](./README.md). Builds on [Level 1 unit tests](./level1_unit_tests.md) and [Hamel Husain's *Your AI Product Needs Evals*](./hamel_your_ai_product_needs_evals.md).

---

## TL;DR

- Start from the **policy or design doc**, not the prompt. Turn it into **scenarios**, then **assertions**, and get both approved by a human before any code exists.
- Generate test inputs with an LLM, write the tests, and **watch them all fail**. Then lock them.
- Let an AI implementer iterate against a **dev set**: run, log traces, read traces, turn new failures into new tests, tune, repeat.
- Gate the release on a **holdout set** the implementer never saw, with tiered thresholds: **100%** on invariants, **no regression beyond noise** on behavior.
- **Humans own what's correct and what ships. AI owns volume.** The workflow's job is to keep it that way.

---

## 1. Why this workflow

LLM features fail in a familiar way: the prompt works in the demo, then every fix breaks something else. Hamel Husain calls this whack-a-mole, and his diagnosis is that the team never built a way to measure quality ([*Your AI Product Needs Evals*](https://hamel.dev/blog/posts/evals/)).

Two failure modes sit on either side of the fix:

| Approach | What goes wrong |
| --- | --- |
| **Feature first, tests later** | No baseline, so you can't tell whether a change helped. The prompt grows to cover edge cases one at a time. |
| **Strict test-first** | You can't write every test up front. Most failure modes appear only after you read real outputs; Shreya Shankar's research calls this [*criteria drift*](https://arxiv.org/abs/2404.12272). |

**Eval-driven development** sits between them: write down what you already know must be true before the code exists, then let the failures you discover drive the rest.

A newer risk comes with AI coding agents: **if the same agent writes the feature and its tests, the tests tend to confirm whatever the code does.** They pass and prove nothing. The workflow below is built around preventing that.

---

## 2. Five principles

1. **The spec defines correct, not the code.** Scenarios and assertions are derived from the policy or design doc, never from the implementation.
2. **Humans approve every definition of correct.** Scenarios, assertions and new failure modes need a human sign-off. AI drafts; people decide.
3. **Tests fail before they pass.** A test that has never failed may check nothing.
4. **Measure on data the implementer didn't tune on.** A holdout set gates the release.
5. **Every iteration leaves evidence.** Pass rates, traces, failure taxonomy and changes are recorded, so the PR proves its claims.

---

## 3. The workflow at a glance

```
 policy / design doc
        │
 ① spec → scenarios ............ AI drafts, flags ambiguities      ⏸ human approves
 ② scenarios → assertions ...... AI drafts, assigns tiers          ⏸ human approves
 ③ generate cases + test code .. test-writer agent (no access to implementation)
        │                         split cases: dev / holdout
 ④ run → all must FAIL ......... then LOCK tests/
        │
 ┌─► ⑤ implement / tune ........ implementer agent (tests read-only, dev set only)
 │   ⑥ run dev suite ×3, log traces, pass rates ± confidence interval
 │   ⑦ read failing + sample of passing traces → taxonomy           ⏸ human confirms new failure modes
 │   ⑧ new failure → new assertion (back through ②)
 └── stop: dev gates met · no gain for 2 rounds · max K rounds · budget hit
        │
 ⑨ gate on HOLDOUT + full suite → PR with evidence                 ⏸ human reviews and merges
 ⑩ launch: same checks as production monitors → flagged traces → back to ⑦
```

Four pause points (⏸) are where the workflow stops for a human. Everything else runs unattended.

---

## 4. The phases

Running example: a **late-delivery compensation** feature for a support chatbot. The policy and tool names are illustrative.

### Phase 1 — Spec to scenarios

**Input:** a policy or design doc in plain language.

> Late means delivered more than 20 minutes after the *latest* ETA shown. 20–45 min late: $5 credit. Over 45: $10 credit or a delivery-fee refund. Nothing if the customer caused the delay. At most one compensation per 30 days, otherwise escalate. Never state an amount before the system calculates it.

**Method** (classic test design applied to policy text):
1. Split the policy into rules (R1…R6).
2. List each rule's branches and **boundary values**: 19, 20, 21 minutes; 45 vs. 46.
3. Combine rules that interact: late *and* already compensated; late *and* customer-caused.
4. Check against real transcripts for cases the policy is silent on: customers who exaggerate the delay, demand a full refund, or are just venting.

**Output:** `scenarios.yaml`, plus a list of **ambiguities** for the policy owner ("Is exactly 20 minutes late?").

| Who | Role |
| --- | --- |
| AI | Drafts rules, boundaries and combinations; mines transcripts; flags ambiguities |
| Eval owner (the engineer who owns the feature) | Edits and finalizes the scenario list |
| Domain expert (senior support agent) | Adds real-world cases |
| Policy owner | Answers ambiguities, **signs off on expected behavior** |

> If the policy owner and the domain expert disagree on a scenario, the policy is ambiguous. Fix the policy before the bot sees it.

### Phase 2 — Scenarios to assertions

Write `assertions.md` in plain words: what each test checks, its **level** and its **tier**.

| Assertion | Level | Tier |
| --- | --- | --- |
| Credit never exceeds the policy amount for the delay | 1 (code, end state) | Invariant — 100% |
| No compensation when on time | 1 | Invariant |
| Compensation history is checked before any resolution | 1 (tool order) | Invariant |
| No dollar amount stated before the preview tool returns | 1 | Behavior — no regression |
| Polite and empathetic when declining | 2 (LLM judge) | Tracked until calibrated |

**Rules:** assert behavior and outcomes, never implementation details. Push everything code can check into Level 1. A Level 2 judge stays *tracked* until it's calibrated against expert labels.

**Human approves** the list. From here on, assertions change only through this approval step.

### Phase 3 — Generate cases and test code

A **test-writer agent** that has never seen any implementation:
- generates inputs with an LLM (about 50 customer messages per scenario: varied tone, typos, exaggerations, other languages), each paired with several mock backend setups;
- **splits cases into dev (~70%) and holdout (~30%)**, stratified by scenario;
- writes the test code: arrange (mocks) → act (conversation) → assert.

```python
def test_amount_never_exceeds_policy(bot, backend):
    backend.delivery("D1", latest_eta="18:00", delivered="18:30")
    run(bot, ["my food was super late"], backend)
    assert backend.applied_credit("D1") in (None, 5.00)
```

### Phase 4 — Confirm failure, then lock

Run everything. **Every test must fail**, because the feature doesn't exist yet. A test that passes now is broken; fix it before going on.

Then **lock `tests/`**. During implementation it's read-only (enforced by a hook, see section 6).

### Phase 5 — Implement and tune

An **implementer agent** builds the feature against the **dev set only**. It can read test names, failures and traces. It can't edit tests, and it never sees the holdout.

If it believes a test is wrong, it files a **test dispute**: the test, the evidence, a proposed fix. A human rules on it. The implementer never edits the test itself.

**Prefer structural fixes over prompt patches.** In the example, the model kept computing lateness from the *first* ETA. Moving the arithmetic into the tool (`minutes_late`, `late_tier`) fixed three failing tests at once, which prompt wording never did.

### Phase 6 — Run and record

- Run each dev case **3 times** (the model isn't deterministic) and report pass rates **with a confidence interval**. At 50 cases, about ±7 points is noise.
- **Pin and record** the model version, prompt version and tool versions in every run file.
- Log full traces for failing cases and a sample of passing ones.
- Use a **fast smoke subset** during the loop; the full suite runs at the gate.

```
test                                 v1     v2     v3     v4
amount_never_exceeds_policy         62%   100%   100%   100%
lateness_uses_latest_eta            40%   100%   100%   100%
no_amount_before_preview            44%    50%    96%    98%
late_and_cold_handles_both          30%    30%    35%    88%
empathetic_when_declining (L2)      60%    62%    70%    74%   tracked
```

### Phase 7 — Read traces and build a taxonomy

The step teams skip, and the one that finds the bugs nobody predicted.

1. **Read failing traces** and write a free-form note on each (*open coding*).
2. **Also read a random sample of passing traces.** A weak assertion can pass a bad output; this is how you find false passes.
3. Group the notes into categories (*axial coding*): the **failure taxonomy**.

| Category | Share of failures |
| --- | --- |
| Wrong lateness math (first ETA, rounding, believed the customer) | 45% |
| Stated an amount before the preview | 30% |
| Mishandled a mixed issue ("late *and* cold") | 15% |
| Robotic when declining | 10% |

AI can pre-cluster failures to speed this up. **A human confirms** which categories are real failure modes and which are policy questions.

### Phase 8 — New failures become new tests

Each confirmed failure mode gets an assertion, which goes **back through Phase 2 approval**, plus 20–30 generated variations of the failing input, split dev/holdout. The suite grows from real problems, never by weakening an existing test.

**The loop (phases 5–8) stops when** the dev gates are met, or there's been no gain for two rounds, or after K rounds (e.g., 5), or the token budget is spent. Stopping without meeting the gates is a valid outcome: the taxonomy tells you what's still wrong.

### Phase 9 — Gate on the holdout, open the PR

Run the **full suite on the holdout set**:

| Tier | Gate |
| --- | --- |
| Invariants (money, safety, privacy) | 100% |
| Behavior | No regression beyond noise vs. the main branch |
| Tracked (including uncalibrated judges) | Reported, not blocking |

A big gap between dev and holdout pass rates means the implementation was tuned to the dev cases. Don't ship it.

**The PR carries the evidence:** the pass-rate table per version, the taxonomy, the changelog of fixes, and the cheap invariants promoted to **runtime guardrails**:

```python
def accept_order_resolution_option(order_id, option):
    ctx = get_delivery_context(order_id)
    assert_or_escalate(option.amount <= POLICY[ctx["late_tier"]])   # enforced in code
    assert_or_escalate(compensation_history_checked(session))
    return backend.apply(order_id, option)
```

A human reviews and merges.

### Phase 10 — After launch

The same checks run as **monitors on production traces**, next to business metrics (re-contact rate, CSAT). When a pass rate dips, the flagged traces go back into Phase 7. In the example, two weeks after launch the bot started stating amounts early in Spanish conversations; that became a new failure mode, a new test and a fix.

Also run **mock contract checks**: compare mock responses against the real APIs on a schedule, so the test environment doesn't drift from production.

---

## 5. Who does what

| Phase | Policy owner | Eval owner | Domain expert | PM | AI |
| --- | --- | --- | --- | --- | --- |
| 1. Spec → scenarios | **Signs off** | Finalizes | Adds real cases | Scope | Drafts, flags ambiguity |
| 2. Assertions | Confirms money rules | **Approves** | — | — | Drafts |
| 3–4. Cases, tests, fail-first | — | Spot-checks | Checks realism | — | **Generates, writes, runs** |
| 5–6. Implement, run | — | Reviews fixes | — | — | **Implements, runs, records** |
| 7. Read traces | — | **Reads, confirms taxonomy** | **Reads, explains why** | — | Pre-clusters |
| 8. New tests | Rules on new edge cases | **Approves** | Labels for judges | — | Writes |
| 9. Gate and PR | Confirms invariants | Owns gates | — | **Launch call** | Drafts PR |
| 10. Monitor | — | Triages dips | Reads flagged traces | Business metrics | Runs monitors |

---

## 6. Keeping the AI from grading its own homework

| Risk | Control |
| --- | --- |
| Tests shaped to fit the code | Test writer and implementer are **separate agents**; the test writer never sees the implementation |
| Implementer edits a test to pass | `tests/` is **read-only** during Phase 5, enforced by a hook; disputes go to a human |
| Implementer special-cases dev inputs | **Holdout set** gates the release; a dev–holdout gap blocks shipping |
| Weak assertion passes bad output | **Read passing traces** too; a human reviews every assertion |
| Thresholds loosened to get green | Tier thresholds live in a file the agents can't edit |
| Uncalibrated judge used as a gate | Judges stay **tracked** until calibrated against expert labels |

In Claude Code, the read-only lock can be a `PreToolUse` hook that rejects `Edit` and `Write` calls under `evals/<feature>/tests/` and the thresholds file while the state file says the phase is `implement`.

---

## 7. Making it a skill

One resumable skill, with a state file, so the work can span several sessions:

```
evals/late_delivery/
├── policy.md               # source of truth (human)
├── scenarios.yaml          # Phase 1, approved
├── assertions.md           # Phase 2, approved; each assertion has a level and tier
├── thresholds.yaml         # gate tiers (human-only)
├── cases/{dev,holdout}/    # Phase 3, LLM-generated
├── tests/                  # Phase 3, locked after Phase 4
├── runs/<date>_vN.json     # Phase 6: pass rates, CIs, model and prompt versions, trace IDs
├── traces/                 # failing traces + sampled passing traces
├── taxonomy.md             # Phase 7, dated
├── disputes.md             # test disputes and rulings
├── CHANGELOG.md            # each iteration's change and its effect
└── state.json              # current phase, round, pending approvals, budget used
```

**Skill outline:**

```markdown
---
name: eval-driven-feature
description: Build an LLM feature eval-first, from a policy or design doc to a PR,
  with human checkpoints. Resumable via evals/<feature>/state.json.
---
On start, read state.json and resume at the recorded phase.

1. SCENARIOS. From policy.md: rules → branches → boundary values → combinations;
   check real transcripts for uncovered cases. Write scenarios.yaml and a list of
   ambiguities. STOP for approval.
2. ASSERTIONS. Write assertions.md: behavior/outcome only, never implementation
   details; level (1 code / 2 judge) and tier for each. Judges start as "tracked".
   STOP for approval.
3. BUILD (subagent with no access to any implementation): generate cases, split
   70/30 dev/holdout stratified by scenario, write tests. Run: all must fail;
   report any passing test as broken. Then set phase=implement (tests/ locked).
4. LOOP, max K=5 rounds or until budget:
   a. Implement (separate subagent; tests/ read-only; dev set only). Prefer
      structural fixes over prompt patches. Disagree with a test → disputes.md.
   b. Run the dev smoke subset ×3; write runs/<date>_vN.json with CIs and versions.
   c. Read failing traces + a random sample of passing traces; draft taxonomy.md.
   d. New failure mode → propose an assertion. STOP for approval, then back to 3
      for that test only.
   Stop early if dev gates are met or no gain beyond noise for 2 rounds.
5. GATE. Full suite on holdout. Invariants 100%; behavior no regression beyond
   noise; flag any large dev–holdout gap. Promote cheap invariants to runtime
   guardrails. Draft the PR (pass-rate table per version, taxonomy, CHANGELOG).
   STOP before pushing.
```

---

## 8. Common mistakes

1. **Writing the prompt first** and the evals "later." Later never comes, and there's no baseline.
2. **Letting the AI approve its own scenarios or assertions.**
3. **Reading only failing traces.** False passes stay invisible.
4. **Treating 88% → 92% on 50 cases as progress.** It's within noise.
5. **Tuning on the cases that gate the release.**
6. **Patching the prompt for each failure** when the fix belongs in a tool or in the data the model sees.
7. **Using an uncalibrated LLM judge as a gate.**
8. **Stopping at the PR.** Production finds failures no offline set will.

---

## 9. Checklist

**Before implementation**
- [ ] Policy or design doc exists; ambiguities answered by its owner
- [ ] Scenarios cover every rule's branches, boundaries and interactions, plus real-transcript cases
- [ ] Assertions approved, each with a level and tier
- [ ] Cases split into dev and holdout
- [ ] Every test fails; `tests/` locked

**Each round**
- [ ] Dev smoke suite run ×3, pass rates with confidence intervals, versions pinned
- [ ] Failing traces *and* a sample of passing traces read
- [ ] New failure modes confirmed by a human before becoming tests
- [ ] Change and its effect logged in CHANGELOG

**Before merge**
- [ ] Holdout: invariants 100%, behavior no regression beyond noise, no large dev–holdout gap
- [ ] Cheap invariants promoted to runtime guardrails
- [ ] PR includes the pass-rate table, taxonomy and changelog

**After launch**
- [ ] Production monitors on the same checks, alongside business metrics
- [ ] Mock contract checks scheduled
- [ ] Flagged traces routed back to trace review

---

## Further reading

- Hamel Husain — [*Your AI Product Needs Evals*](https://hamel.dev/blog/posts/evals/) · [*Creating a LLM-as-a-Judge That Drives Business Results*](https://hamel.dev/blog/posts/llm-judge/) · [*AI Evals FAQ*](https://hamel.dev/blog/posts/evals-faq/) (with Shreya Shankar)
- Shreya Shankar et al. — [*Who Validates the Validators?*](https://arxiv.org/abs/2404.12272) (criteria drift)
- Anthropic — [*Demystifying evals for AI agents*](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Sierra — [*τ-bench*](https://sierra.ai/blog/benchmarking-ai-agents) (simulated users, pass^k)
- Notes in this repo: [Level 1 unit tests](./level1_unit_tests.md) · [reading list](./reading_list.md) · [DoorDash chatbot offline simulator](../../project-deep-dive/chatbot_offline_simulator.md)
