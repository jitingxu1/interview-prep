# Level 1 Tests (Code Assertions) for a Support Bot

Hamel Husain's **Level 1** evals — cheap, deterministic code assertions — applied to the DoorDash support bot: how they differ from traditional unit tests, where their inputs come from, four test types with code, how they gate releases and run in production, the order of work between tests and features, and a full worked example with who does what. Part of the [evaluation section](./README.md); background on the source post: [Hamel's *Your AI Product Needs Evals*](./hamel_your_ai_product_needs_evals.md).

> **What's from where.** The three-level framing comes from [Hamel's post](https://hamel.dev/blog/posts/evals/). The tool names (`get_delivery_context`, `accept_order_resolution_option`, `transfer_to_agent`, …), mock routing and scripted mode come from DoorDash's simulator posts ([notes](../../project-deep-dive/chatbot_offline_simulator.md)). The test harness, field names, thresholds and the late-delivery policy are **illustrative**, not DoorDash's real code.

---

## 1. Level 1 vs. traditional unit tests

**Same checker, different system under test.** The checks are still deterministic code in CI; the thing being tested is non-deterministic.

**What's the same:**

| | Traditional unit test | Level 1 |
| --- | --- | --- |
| The check | Deterministic `assert` | Deterministic code — no LLM judge at this level |
| Organization | Function × case | **Feature × scenario** (listing finder: one, many, no matches) |
| Speed, where it runs | Fast, CI | Fast, CI |
| Purpose | Catch regressions | Catch regressions from prompt, model or code changes |
| Growth | New bug → new test | New failure in the data → new test |

**What's different:**

| | Traditional unit test | Level 1 |
| --- | --- | --- |
| System under test | Deterministic | **Non-deterministic** |
| What you assert | Exact values: `add(2, 3) == 5` | **Properties**: `len(listings) == 1`, valid JSON, no UUID |
| Expected result | 100% green | **Pass rate tracked over time**; some tiers never reach 100% |
| A failing test means | A bug to fix now | Often a known weakness being worked on |
| Flakiness | A test bug | **Expected** — run cases several times, report a rate |
| Inputs | A few, hand-written | **Dozens to hundreds, LLM-generated** |
| Where tests come from | The spec | **Reading traces** — failures actually observed |
| Coverage | Full correctness | Only checkable properties; tone and helpfulness go to Level 2 |
| Where it lives | Test suite only | **Also reused at runtime** as guardrails and retry triggers |

---

## 2. "Generate inputs with an LLM, grow tests from traces"

**Generate inputs:** an LLM writes the test *inputs*; you write the *assertions*, so the LLM never defines correctness.

```
Write 50 messages a DoorDash customer might send when items are missing from
their order. Vary tone (polite, angry, confused), detail (names items vs. not),
and include typos, multiple issues in one message, and a few in Spanish.
```

Benefits: no need to wait for production data, more variety than you'd write, scale, and you can ask for hard cases on purpose.

**Grow from traces:** read real or simulated conversations; every failure becomes a permanent test.

```
   read traces ──► spot a failure ──► write an assertion ──► LLM generates
        ▲                                                    variations of
        │                                                    the failing input
        │                                                          │
        └── next change is tested ◄── fix, re-run ◄── add to suite, measure baseline
            against every past failure     (60% → 97%)
```

Why grow instead of writing everything up front: real failures surprise you (nobody predicts "UUIDs leak into replies" from a spec), every test maps to a real problem, and criteria drift (Shreya Shankar) means "good" is discovered by looking at outputs. Rechat's hundreds of tests were almost all added this way.

**Same pattern at DoorDash:** human review found hallucinations → binary "no hallucination" eval → scenarios from the failure cases → iterate on the case state (−90%) → eval stays in the 50+ guardrail suite.

---

## 3. Four kinds of Level 1 tests for a support bot

All plain code, arrange (mocks) → act (conversation) → assert:

| Type | Checks | Example |
| --- | --- | --- |
| **1. Output format** | The reply itself | No internal IDs, length cap, no raw JSON, no "fraud" |
| **2. Tool trajectory** | Which tools, what order, what args | Fraud check happens **before** any resolution |
| **3. End state** | What the mock backend recorded | Refund amount equals the preview amount |
| **4. Scripted flows** | A fixed sequence of customer messages | "I want a human" ×3 → escalate |

---

## 4. The tests

### Harness

```python
# conftest.py — arrange: mock every tool the bot can call
@pytest.fixture
def mock_backend():
    m = MockBackend()          # records every tool call and final state
    m.delivery("D123", status="delivered", items=["3 cookies", "pulled pork", "fries"],
               subtotal=55.00, dasher_photo=True)
    m.fraud_status("C9", flagged=False)
    m.resolution_preview("D123", options=[
        {"type": "credit", "amount": 55.00},
        {"type": "refund", "amount": 55.00},
        {"type": "redelivery", "credit": 10.00},
    ])
    return m

def run(bot, messages, backend):
    """act: send customer messages, return transcript + tool trace + final state"""
    return bot.converse(messages, tools=backend, headers={"x-simulation": "true"})
```

The simulation header routes tool calls to the mock — the same mock-aware routing DoorDash describes.

### Type 1 — output format

```python
UUID_RE   = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b")
TOOL_NAME = re.compile("|".join(map(re.escape, bot.tool_names)), re.IGNORECASE)

@pytest.mark.parametrize("msg", load_cases("missing_item/opening"))  # LLM-generated
def test_reply_format(bot, mock_backend, msg):
    r = run(bot, [msg], mock_backend)
    for reply in r.bot_messages:
        assert not UUID_RE.search(reply)               # no internal IDs
        assert not TOOL_NAME.search(reply)             # no tool names
        assert not reply.strip().startswith("{")       # no raw JSON
        assert len(reply.split()) <= 120               # length cap
        assert "fraud" not in reply.lower()            # never tell a customer they're flagged
```

**Input:** one opening message per run. `load_cases` reads ~50 LLM-generated messages saved once to a file; `parametrize` turns them into 50 tests. Each run is a one-turn conversation; the bot may send several messages (greeting + reply), so every message is checked. The mock gives the bot realistic order data it *could* leak.

| Assertion | Fails on | Why it matters |
| --- | --- | --- |
| No UUID | "Your order **7f3a9c2e-…** is…" | Internal IDs leaked from tool output |
| No tool name | "Let me call **get_delivery_context**" | Exposed internals |
| Not raw JSON | `{"status": "delivered", …}` | Dumped tool output instead of a sentence |
| ≤ 120 words | A 300-word wall of text | Chat replies must be short |
| No "fraud" | "Your account is under **fraud** review" | Policy and legal risk |

**Not tested here:** whether the reply is correct, understood the issue, or was empathetic — that's types 2–3 and Level 2. Release gate: **100%** (safety and format).

> Building `TOOL_NAME` from the bot's tool registry (case-insensitive) covers new tools automatically; keep "fraud" in its own assertion so each check has one cause.

### Type 2 — tool trajectory

```python
def test_fraud_check_before_any_resolution(bot, mock_backend):
    r = run(bot, ["My cookies and pulled pork were missing"], mock_backend)
    calls = r.tool_names
    assert "get_order_resolution_and_fraud_status" in calls
    if "accept_order_resolution_option" in calls:
        assert calls.index("get_order_resolution_and_fraud_status") \
             < calls.index("accept_order_resolution_option")

def test_delivery_context_fetched_first(bot, mock_backend):
    r = run(bot, ["where is my order"], mock_backend)
    assert r.tool_names[0] == "get_delivery_context"

def test_no_resolution_without_customer_choice(bot, mock_backend):
    r = run(bot, ["Missing items: 3 cookies and pulled pork"], mock_backend)
    assert "accept_order_resolution_option" not in r.tool_names

def test_flagged_account_gets_no_auto_refund(bot, mock_backend):
    mock_backend.fraud_status("C9", flagged=True)
    r = run(bot, ["My whole order never came, refund me"], mock_backend)
    assert "accept_order_resolution_option" not in r.tool_names
    assert "transfer_to_agent" in r.tool_names
```

### Type 3 — end state

```python
def test_refund_amount_matches_preview(bot, mock_backend):
    r = run(bot, ["3 cookies and pulled pork were missing",
                  "I'll take the $55 refund"], mock_backend)
    applied = mock_backend.applied_resolution("D123")
    assert applied.type == "refund"
    assert applied.amount == 55.00
    assert applied.amount <= mock_backend.subtotal("D123")

def test_applied_option_matches_customer_choice(bot, mock_backend):
    r = run(bot, ["My order never came", "Refund to my card please"], mock_backend)
    assert mock_backend.applied_resolution("D123").type == "refund"

def test_options_offered_match_preview(bot, mock_backend):
    r = run(bot, ["items missing from my order"], mock_backend)
    offered = extract_dollar_amounts(r.last_bot_message)
    assert set(offered) <= {55.00, 10.00}   # no invented amounts
```

**Why end state matters:** in DoorDash's published never-delivered example, the customer asked for an $18 refund and the bot applied $18 in **credits**. The reply read fine; only the end state shows the bug.

### Type 4 — scripted flows

```python
def test_human_request_deflect_then_resolve(bot, mock_backend):
    r = run(bot, ["I want to speak to a real person.",
                  "Fine, my order never came.",
                  "Yes, nothing arrived.",
                  "Refund please."], mock_backend)
    assert r.tool_names.count("transfer_to_agent") == 0
    assert "never_delivered_fault_determination" in r.tool_names
    assert mock_backend.applied_resolution("D123").type == "refund"

def test_escalates_after_repeated_insistence(bot, mock_backend):
    r = run(bot, ["I want a human."] * 3, mock_backend)
    assert "transfer_to_agent" in r.tool_names

def test_no_repeated_option_list(bot, mock_backend):
    r = run(bot, ["items missing", "how long do refunds take?",
                  "what's the difference between credit and refund?"], mock_backend)
    option_lists = [m for m in r.bot_messages if "$55.00 in credits" in m]
    assert len(option_lists) <= 2
```

### Tests grown from traces

| Failure seen in a trace | New Level 1 test |
| --- | --- |
| Applied credits when the customer chose a refund | `test_applied_option_matches_customer_choice` |
| Offered $60 on a $55 order | `test_options_offered_match_preview` |
| Said "your account is under fraud review" | `"fraud" not in reply` |
| Restated options three times | `test_no_repeated_option_list` |
| Looped on "I want a human" | `test_escalates_after_repeated_insistence` |

### Reporting

```
scenario / test                             pass rate   last week
missing_item / reply_format                 50/50  100%   100%
missing_item / fraud_check_before_resolve   49/50   98%    96%
missing_item / refund_matches_preview       50/50  100%   100%
never_delivered / option_matches_choice     41/50   82%    64%   ← the credit/refund bug
human_request / escalates_after_insisting   47/50   94%    94%
```

### What doesn't belong in Level 1

| Check | Goes to |
| --- | --- |
| Appropriate empathy, not robotic | Level 2 LLM judge |
| Correct escalation in ambiguous cases | Level 2 policy-compliance judge |
| Issue identified correctly (free text) | Level 2, or Level 1 if the bot emits a structured issue type |
| Customer actually satisfied | Level 3: A/B, re-contact rate, CSAT |

**Rule of thumb:** if code can check it — money, order of operations, format, state — it's Level 1.

---

## 5. Using the tests: gates, production, order of work

### Tiered gates — some failures do block

| Tier | Example | Gate |
| --- | --- | --- |
| **Hard invariants** (money, safety, privacy) | Refund ≤ preview, fraud check first, no "fraud", no leaked IDs | **100% or the merge is blocked** |
| **Behavior tests** | Applied option matches choice; escalate after three asks | **Block on regression** vs. main (minus noise) or below a threshold |
| **Known weaknesses** | New test for an open failure (64% → working on it) | **Tracked, not blocking**; promoted once stable |

### Three uses in production

```
            ┌───────────── BEFORE DEPLOY ─────────────┐
 PR ──► CI: run the suite on mocks  ──► gate ──► deploy
            └─────────────────────────────────────────┘
                                          │
            ┌───────────── IN PRODUCTION ─▼───────────┐
 customer ──► bot ──► [inline guardrail] ──► reply / action
                              │
                              └──► log trace ──► [async monitor] ──► dashboards, alerts
            └─────────────────────────────────────────┘
```

| Use | What runs | When | On failure |
| --- | --- | --- | --- |
| **Regression test** | Whole suite on mocks | Every PR, in CI | Block or flag |
| **Guardrail** | Cheap deterministic checks on one response or action | Inline, every live response, before the user sees it or the action runs | Retry, block, escalate |
| **Online monitor** | Same assertions on logged traces | Async, all or sampled traffic | Alert on dips; failing traces become new tests |

| Test | Regression | Guardrail | Monitor |
| --- | --- | --- | --- |
| No UUID / tool name / JSON | ✅ | ✅ regenerate | ✅ |
| No "fraud" | ✅ | ✅ block and regenerate | ✅ |
| Refund ≤ preview / subtotal | ✅ | ✅ check before the tool call runs | ✅ |
| Fraud check before resolution | ✅ | ✅ refuse the resolution tool if unchecked | ✅ |
| Applied option matches choice | ✅ | ⚠️ needs intent parsing | ✅ |
| Scripted flows | ✅ | ❌ needs script and mocks | ❌ |

**Enforce money rules inside the tool**, so the prompt asks and the code guarantees:

```python
def accept_order_resolution_option(order_id, option):
    preview = get_preview(order_id)
    assert_or_escalate(option in preview.options)              # can't invent an option
    assert_or_escalate(option.amount <= order.subtotal)        # can't exceed the order
    assert_or_escalate(fraud_checked(session))                 # order of operations
    return backend.apply(order_id, option)
```

### Order of work — eval-driven, not strict TDD

- **Not strict test-first:** criteria drift means most failure modes appear only after reading outputs.
- **Not feature-first:** with no baseline you can't tell if a change helped (whack-a-mole). Your own support lesson: "build the eval set before writing the first prompt."

| Step | Who | Output |
| --- | --- | --- |
| 1. Define scenarios and success | **Human** (product, ops, policy) | "Offer options from the preview, never exceed the subtotal, check fraud first" |
| 2. Write invariant tests | **Human owns assertions**, AI writes scaffolding | Money, safety, format tests — **before the feature**, failing at first |
| 3. Generate inputs | **AI** | 50 messages per scenario |
| 4. Build the feature | **AI-assisted** | First version |
| 5. Run and read traces | **Human reads**, AI clusters failures | Baselines plus unpredicted failures |
| 6. Turn failures into tests | **Human names the failure**, AI writes test code and variations | Suite grows |
| 7. Iterate | AI-assisted | Pass rates climb |
| 8. Promote and gate | Human | Stable tests block; cheap ones become guardrails |

### When AI writes both feature and tests

**Risk:** the same AI writes tests that confirm whatever its code does — they pass and prove nothing.

| Rule | Why |
| --- | --- |
| Humans own *what* is asserted; AI writes *how* | Correctness comes from policy and product, not the implementation |
| Derive tests from the spec or policy, never the code | Give the test-writer the policy and scenarios, not the implementation |
| Separate contexts | Write tests in a different session or agent from the feature |
| Invariant tests before the feature | They can't be shaped to fit code that doesn't exist |
| Watch each test fail first | A test that never failed may check nothing |
| Review assertions like code | Weak ones ("reply is not empty") are easy to spot |
| Hamel's signal | If everything passes on day one, the tests are too easy |

DoorDash's Ask DoorDash post follows the same rule: a coding agent proposes fixes, validated against a team-owned rubric calibrated to humans — the AI never grades itself.

---

## 6. Worked example: late-delivery compensation, step by step

One feature taken through the eight steps, with who does what at each. The policy numbers and tool names are invented for the example.

### The roles

| Role | Brings | Typical person |
| --- | --- | --- |
| **Policy owner** | The rules and their meaning in edge cases | Support ops / policy team |
| **Eval owner** | Turns rules into scenarios and assertions; owns the test suite and gates | Engineer or DS who owns the feature (often the tech lead) |
| **Domain expert** | Real-world cases the policy doesn't mention; judges good vs. bad on real traces | Senior support agent or QA lead (Hamel's "principal domain expert") |
| **PM** | Scope, launch decision, business metrics | Product manager for support automation |
| **AI** | Drafts, generates, builds, clusters — never decides what's correct | Coding agent / LLM assistant |

DoorDash's one-click platform post says rubrics are "defined by the chatbot production team" per feature: the team that ships a feature owns its definition of correct.

### Step 1 — Define scenarios and success

**The policy** (plain words):
> - Late = delivered **more than 20 min after the latest ETA shown** (not the first ETA).
> - 20–45 min → **$5 credit**. Over 45 min → **$10 credit or delivery-fee refund** (customer chooses).
> - No compensation if the customer caused the delay (wrong address, not answering).
> - At most **one late compensation per 30 days**; after that, escalate to a human.
> - Never state an amount before the system calculates it.

| Who | Does what |
| --- | --- |
| **Policy owner** | Writes or confirms the rules; answers ambiguities ("is exactly 20 minutes late?"); **signs off on expected behavior** |
| **Eval owner** | Splits the policy into rules (R1–R6), lists each rule's branches and **boundary values** (19/20/21 min, 45/46 min), combines interacting rules, writes the scenario table |
| **Domain expert** | Checks the list against real late-delivery transcripts; adds cases the policy is silent on (customer exaggerates the delay, wants a full refund, is just venting) |
| **PM** | Confirms scope (which scenarios are in v1) and the business metrics to watch |
| **AI** | Drafts boundaries and combinations from the policy text; mines transcripts for uncovered cases; **flags where the policy is ambiguous or silent** |

**Artifact:** the scenario table, signed off by the policy owner.

| Scenario | Expected behavior |
| --- | --- |
| A. 30 min late | Offer $5 credit |
| B. 60 min late | Offer the choice: $10 credit or fee refund |
| C. Says "late" but on time | Explain politely, no compensation |
| D. Late because of a wrong address | No compensation, explain |
| E. Already compensated this month | Escalate to a human |
| F. Late **and** wants a full refund | Offer the policy options; escalate if they insist |

> If the policy owner and the domain expert disagree on a scenario (e.g., F), **the policy is ambiguous** — fix the policy before the bot sees it.

### Step 2 — Write invariant tests before the feature exists

| Who | Does what |
| --- | --- |
| **Eval owner** | Decides **what** to assert — money, order of operations, trust; reviews every assertion |
| **AI** | Writes the pytest scaffolding and mock setups from the eval owner's spec |
| **Policy owner** | Confirms the money invariants match the policy exactly |

```python
def test_amount_never_exceeds_policy(bot, backend):           # money
    backend.delivery("D1", latest_eta="18:00", delivered="18:30")
    run(bot, ["my food was super late"], backend)
    assert backend.applied_credit("D1") in (None, 5.00)

def test_no_compensation_when_on_time(bot, backend):          # money
    backend.delivery("D1", latest_eta="18:00", delivered="18:10")
    run(bot, ["this took forever, I want credit"], backend)
    assert backend.applied_credit("D1") is None

def test_history_checked_before_compensating(bot, backend):   # order of operations
    r = run(bot, ["order was an hour late"], backend)
    if "accept_order_resolution_option" in r.tool_names:
        assert r.tool_names.index("get_compensation_history") \
             < r.tool_names.index("accept_order_resolution_option")

def test_no_amount_promised_before_preview(bot, backend):     # trust
    r = run(bot, ["it was late"], backend)
    first_amount_turn = turn_with_dollar_amount(r)
    assert first_amount_turn is None or \
           first_amount_turn > turn_of_tool(r, "create_late_compensation_preview")
```

**All four fail** — the feature doesn't exist yet. A test you've watched fail can detect something, and tests written before the code can't be bent to fit it.

### Step 3 — Generate test inputs

| Who | Does what |
| --- | --- |
| **AI** | Generates ~50 customer messages from a prompt; pairs them with mock orders |
| **Eval owner** | Writes the generation prompt (asks for hard cases on purpose); spot-checks the output |
| **Domain expert** | Skims a sample: "do real customers talk like this?" |

```
Write 50 messages a DoorDash customer might send about a late delivery.
Mix tones (polite, furious, sarcastic), include some that exaggerate
("3 hours late!" when it was 25 min), some that also mention cold food,
some that demand a full refund, some in Spanish, and some with typos.
```

Sample output: `"THREE HOURS. unacceptable. refund everything."` (really 25 min) · `"why did it say 6:00 then 6:20 then 6:45??"` (ETA changed twice) · `"llegó tardísimo mi pedido"`. Each message runs against several mock orders (on time, 30 min, 60 min, wrong address, already compensated), so one message becomes many cases.

### Step 4 — Build the feature

| Who | Does what |
| --- | --- |
| **AI** | Writes the prompt instructions and tool wiring (`get_delivery_context`, `get_compensation_history`, `create_late_compensation_preview`, `accept_order_resolution_option`) |
| **Eval owner** | Reviews the code; runs the suite |
| **PM** | Nothing yet — no demo-driven decisions before the numbers exist |

**v1 results:**
```
amount_never_exceeds_policy            31/50   62%
no_compensation_when_on_time           38/50   76%
history_checked_before_compensating    50/50  100%
no_amount_promised_before_preview      22/50   44%   ← bad
reply_format                           50/50  100%
```

### Step 5 — Run it and read the traces

| Who | Does what |
| --- | --- |
| **Eval owner** | Reads ~40 failing traces; writes a free-form note on each (**open coding**); groups notes into a failure taxonomy (**axial coding**) |
| **Domain expert** | Reads alongside, says *why* a reply is bad from the customer's side; their critiques later become judge examples |
| **AI** | Pre-clusters failures to speed up reading — **suggests** groups, doesn't replace reading |

**Open coding notes:**
```
trace 07: said "$10" in first reply — preview hadn't run yet
trace 12: ETA changed 6:00→6:45, delivered 6:50; bot said "50 min late" → used FIRST ETA
trace 19: customer said "3 hours" — bot believed them, didn't check timestamps
trace 23: customer wanted full refund, bot refused 3 times in a row, sounded robotic
trace 31: delivered 18:19, ETA 18:00 → 19 min, bot rounded to "about 20" and gave $5
trace 38: bot apologized for "cold food" and offered a food-quality refund — not this flow
```

**Failure taxonomy:**

| Category | Share of failures |
| --- | --- |
| **Wrong lateness math** (first ETA, rounding, believed the customer) | **45%** |
| Promised an amount before the preview | 30% |
| Mishandled a mixed issue ("late *and* cold") | 15% |
| Robotic on refusal | 10% |

**Nobody predicted the first category in step 1.** You only find it by reading.

### Step 6 — Turn each failure into a test

| Who | Does what |
| --- | --- |
| **Eval owner** | Names each failure, decides the check and its level (code vs. judge) |
| **AI** | Writes the test code; generates 20–30 variations of each failing input |
| **Domain expert** | For Level 2 checks: labels examples pass/fail **with a critique**, used to calibrate the judge |
| **Policy owner** | Rules on any new edge case the failures exposed (e.g., boundary rounding) |

| Failure | New test | Level |
| --- | --- | --- |
| Used the first ETA | `test_lateness_uses_latest_eta`: ETA 6:00 → 6:45, delivered 6:50 → no compensation | **Level 1** |
| Believed the customer's number | `test_ignores_customer_claimed_delay`: says "3 hours," real 25 min → $5 | **Level 1** |
| Rounding at the boundary | `test_19_minutes_is_not_late` → no compensation | **Level 1** |
| Mixed issue | `test_late_and_cold_handles_both`: both flows, or a hand-off to food quality | **Level 1** (trajectory) |
| Robotic refusal | Rubric "empathetic when declining" — binary, calibrated to the expert | **Level 2** |

### Step 7 — Iterate on the feature

| Who | Does what |
| --- | --- |
| **AI** | Implements fixes |
| **Eval owner** | Chooses *structural* fixes over prompt patches; re-runs; tracks pass rates per version |
| **Domain expert** | Re-reads a sample after each version to catch new problems the tests don't see |

**Fix 1 (structural): move the math out of the prompt into the tool.**
```python
def get_delivery_context(order_id):
    d = backend.delivery(order_id)
    return {...,
            "minutes_late": max(0, minutes(d.delivered - d.latest_eta)),  # code computes it
            "late_tier": tier(d)}                                          # "none" | "5" | "10"
```
**Fix 2:** prompt rule — never state an amount until the preview returns. **Fix 3:** route "cold food" to the food-quality flow.

| Test | v1 | v2 (math in tool) | v3 (+ prompt rule) | v4 (+ routing) |
| --- | --- | --- | --- | --- |
| amount_never_exceeds_policy | 62% | **100%** | 100% | 100% |
| lateness_uses_latest_eta | 40% | **100%** | 100% | 100% |
| ignores_customer_claimed_delay | 55% | **98%** | 98% | 100% |
| no_amount_before_preview | 44% | 50% | **96%** | 98% |
| late_and_cold_handles_both | 30% | 30% | 35% | **88%** |
| empathetic_when_declining (judge) | 60% | 62% | 70% | 74% |

One structural fix (v2) solved three tests at once — the same lesson as DoorDash's case state.

### Step 8 — Promote tests and gate the release

| Who | Does what |
| --- | --- |
| **Eval owner** | Assigns tests to tiers; moves cheap checks into the tool as guardrails; sets up async monitors |
| **Policy owner** | Confirms the hard invariants (money, history) are the right ones to block on |
| **PM** | Makes the launch call from simulation results; owns the A/B test and business metrics (re-contact, CSAT, cost) |
| **AI** | Implements guardrail code and monitor jobs |

| Tier | Tests | Gate |
| --- | --- | --- |
| **Hard invariant — 100%** | amount ≤ policy, nothing when on time, history first, latest ETA | Blocks merge |
| **Behavior — no regression** | no amount before preview, ignores claimed delay, late + cold | Blocks if below last main-branch run |
| **Tracked** | empathetic when declining (Level 2, 74%) | Dashboard only |

```python
def accept_order_resolution_option(order_id, option):
    ctx = get_delivery_context(order_id)
    assert_or_escalate(option.amount <= POLICY[ctx["late_tier"]])   # money cap in code
    assert_or_escalate(compensation_history_checked(session))
    assert_or_escalate(not compensated_in_last_30_days(customer))
    return backend.apply(order_id, option)
```

Launch: full suite in the simulator → A/B on 5% of traffic → async monitors on production traces plus re-contact and CSAT.

### And the loop restarts

Two weeks later the monitor flags `no_amount_before_preview 98% → 91%`. The eval owner and domain expert read the flagged traces: in Spanish, the bot states "$5" early. New failure → new test with 30 Spanish variations → fix → back to the gate.

### Summary: who does what

| Step | Policy owner | Eval owner | Domain expert | PM | AI |
| --- | --- | --- | --- | --- | --- |
| 1. Define scenarios | **Signs off** on rules and expected behavior | **Translates** policy → scenarios | Adds real-world cases | Sets scope | Drafts edge cases, flags ambiguity |
| 2. Invariant tests | Confirms money rules | **Decides what to assert** | — | — | Writes scaffolding |
| 3. Generate inputs | — | Writes prompt, spot-checks | Sanity-checks realism | — | **Generates** |
| 4. Build | — | Reviews, runs suite | — | — | **Builds** |
| 5. Read traces | — | **Reads**, builds taxonomy | **Reads**, explains why | — | Pre-clusters |
| 6. Failures → tests | Rules on new edge cases | Names failures, picks level | Labels and critiques for judges | — | Writes tests and variations |
| 7. Iterate | — | Picks structural fixes, tracks rates | Re-reads samples | — | **Implements** |
| 8. Gate and launch | Confirms hard invariants | Tiers, guardrails, monitors | — | **Launch call**, A/B | Implements guardrails |

**The pattern:** humans own *what's correct* (steps 1, 2, 5, 6) and *what ships* (step 8); AI owns *volume* (generating, building, writing code).

**How to say it (about 45 seconds):**

> "Take a late-delivery compensation feature. The policy owner signs off on the rules, and I as eval owner turn them into scenarios — boundaries like 19, 20 and 21 minutes, combinations like late plus already compensated — with a senior support agent adding real cases the policy missed. I write invariant tests before any code; they all fail. AI generates fifty customer messages and builds v1. Then the support expert and I read forty traces and find something nobody predicted: the model used the first ETA instead of the latest. That becomes a test, and the fix is structural — compute lateness in the tool — which solved three tests at once. I tier the tests, the money cap becomes a guardrail inside the tool, the PM makes the launch call on an A/B, and monitors on production traces keep feeding new failures back in."

---

---

## Self-check

1. Name three ways Level 1 tests differ from traditional unit tests.
2. Why does the LLM generate test inputs but never the assertions?
3. Which Level 1 tests can run as inline guardrails, and which can't?
4. Why must humans own the assertions when AI writes the tests?
5. Who turns the policy into scenarios, and who signs off?

<details><summary>Answers</summary>

1. They assert properties instead of exact values; they track a pass rate instead of requiring all green; inputs are LLM-generated and tests grow from failures seen in traces (also: reused at runtime as guardrails).
2. If the LLM wrote the assertions, it would be defining correctness itself; humans keep that, derived from policy.
3. Cheap, deterministic, single-response or single-action checks (IDs, "fraud", refund cap, fraud-check order) can; scripted multi-turn flows and pass-rate runs need mocks, so they're regression only.
4. Otherwise the tests confirm the implementation instead of the policy — they pass and prove nothing.
5. The eval owner (the engineer or DS who owns the feature) translates, with a domain expert adding real cases; the policy owner signs off on expected behavior. AI drafts edge cases and flags ambiguity.
</details>

---

## How to say it (about 60 seconds)

> "For our support bot, Level 1 is code assertions in four groups: output format — no internal IDs, no mention of fraud, a length cap; tool trajectory — fraud check before any resolution, nothing committed before the customer chooses; end state on the mock backend — refund matches the preview, applied option matches the customer's choice; and scripted flows. Inputs are LLM-generated per scenario, and every failure we find in traces becomes a test — like the bot applying credits when the customer asked for a refund: the reply read fine, but the end-state check failed. Gates are tiered: money and safety at 100%, behavior on no-regression, open problems tracked. The same checks run three ways: regression in CI, inline guardrails — the refund cap is enforced inside the tool — and async monitors on production traces. Order of work is eval-driven: humans define success and write invariant tests first, AI builds and generates inputs, and humans own what's asserted so the AI never grades its own homework."
