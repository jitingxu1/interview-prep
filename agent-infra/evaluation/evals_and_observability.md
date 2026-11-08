# Evals and Observability

Part of the [evaluation section](./README.md).

The thing that separates a demo from a platform. If the interviewer only remembers one thing, it should be: **evals are the deploy gate, traces are the debugger.**

---

## What to evaluate

| Level | Question | How |
|---|---|---|
| **Final outcome** | Did the agent solve the task? | Task-specific checks (state of the system after the run), rubric graded by a model or human |
| **Trajectory** | Did it get there sensibly? | Right tools, right args, no unnecessary steps, no policy violations |
| **Single step** | Is each component right? | Router accuracy, retrieval recall@k, tool-arg correctness — classic ML metrics |
| **Safety / policy** | Did it do anything it shouldn't? | Red-team set, policy checks on every write action |
| **Cost / latency** | Is it affordable and fast? | Tokens, model calls, tool calls, p50/p95 per run |

Prefer **outcome checks you can compute** (was the refund issued for the right amount; is the ticket in the right state) over model-graded vibes wherever possible.

## Building the eval set

- **Seed from production:** sample real conversations, stratified by intent and by outcome (escalated, low CSAT, long).
- **Label with humans + models:** a model drafts labels, humans review a sample and all disagreements. Your **offline labeling agent with batch RAG** is exactly this — use it as the anchor.
- **Every incident becomes a test case.** The regression set grows from failures.
- **Hold out a fresh set** periodically so you're not overfitting prompts to a stale set.
- Size: [your eval set size]. Rule of thumb to say: enough per slice that a few-point regression is detectable, and slices for every high-stakes intent.

## Graders

- **Deterministic:** exact match, schema checks, state assertions. Cheap, reliable — use first.
- **Model-as-judge:** rubric-based, one criterion per judge, pairwise comparison for A vs B. **Calibrate against human labels** and report agreement; re-check when you change the judge model.
- **Human review:** for the ambiguous tail and to calibrate judges. Expensive; sample.

## Evals as the deploy gate

- Any change to **prompt, model, tool description, tool version, or retrieval index** triggers the agent's eval suite in CI.
- Gate on per-slice metrics, not just the average — a model upgrade that improves the average can break a small high-stakes intent.
- Agents are non-deterministic: run each case several times or report variance; don't block on single-run noise.
- After offline pass: **shadow** (run on live traffic, don't act) → **canary** (small % of traffic) → full, with online metrics as the gate.

## Online metrics

For a support agent:

- **Resolution / containment rate** — resolved without a human `[your number]`
- **Escalation rate and reason**
- **CSAT** on agent-handled conversations vs human `[delta]`
- **Repeat contact** within N days — catches "resolved" conversations that weren't
- **Policy violations / bad actions** — should be ~zero; any one is an incident
- **Cost per resolved conversation** vs cost of a human-handled one — this is the business case

Watch for **Goodhart:** containment goes up if the agent just refuses to escalate. Pair it with repeat contact and CSAT.

## Observability

- **Trace every run:** one trace per run, spans for each model call, tool call, and retrieval, with inputs, outputs, tokens, latency, cost, model and prompt versions. (OpenTelemetry-style spans; GenAI semantic conventions exist.)
- **Replay:** pull a bad production trace and re-run it against a new prompt or model. This closes the loop between online failures and offline evals.
- **PII:** redact at ingestion; access-controlled traces; retention limits.
- **Dashboards per agent and per tool:** volume, success, latency, cost, error classes.
- **Alerting:** on spikes in escalation, tool errors, loop limits hit, cost per run — not just on 5xx.

## Cost control

- Per-tenant budgets and alerts at the gateway.
- Smaller models for routing, classification, and simple steps; the big model only where it pays.
- Prompt caching for stable prefixes.
- Cap steps and tokens per run.
- Report **cost per successful outcome**, not cost per call.

---

## How DoorDash does it (first-party engineering posts)

Four DoorDash systems, studied 2026-11-02 to 11-06. Full notes: [chatbot offline simulator](../../project-deep-dive/chatbot_offline_simulator.md) · [Ask DoorDash memory](../../project-deep-dive/doordash_assistant_memory.md) · [AI code reviewer](../../project-deep-dive/doordash_ai_code_reviewer.md).

| System | What they evaluate | How | Headline result |
|---|---|---|---|
| **Support chatbot simulator** | Multi-turn support conversations before launch | LLM plays the customer (personas and intents mined from real transcripts); tool calls mocked (gRPC + MCP, routed by a simulation header); binary LLM judges per rubric | Iteration days → hours; 200+ conversations in < 5 min; 50+ evals; hallucinations −90%, held in production |
| **One-click platform** | Same, as self-serve infra | Per-feature rubrics written by each chatbot team, **every rubric binary pass/fail**; results in SQL + dashboards; scripted mode for deterministic flows | Realism check: simulation 302 convos in 5 min, 46% escalation vs. production 175 convos in 7 h, 44% |
| **Ask DoorDash** (shopping agent) | Whole sessions, offline and online | Transcript = inputs, responses, tool calls, outputs, grounding context. **Guardrail evals** (session integrity, safety) vs. **capability evals** (result quality, execution quality). **Offline and online share the same rubric and judge.** Background agents cluster failures and write reports; fixes validated in the simulator | Memory sessions: −33% misunderstood intent, −24% irrelevant results (judge-measured); +24% grocery conversion (A/B) |
| **AI code reviewer** | Review comments | Lead scout flags, deep reviewers verify, **"disprove-it" pass** drops findings that can be falsified. Success = engineers change code and keep it enabled | 60.2% acceptance on high/critical findings, 10,000+ PRs/week, ~7 min, ~$3/review |

**Patterns that repeat across all four:**

1. **Narrow, binary judges, one per failure mode.** Verifying one behavior is much easier than generating a full answer (the **generator–verifier gap**), so a judge can be reliable even when the agent isn't. A generic "rate this 1–10" judge loses that gap.
2. **Calibrate every judge against humans.** Label a sample → run the judge → precision, recall, F1 → read the reasoning on mismatches → fix the prompt → repeat until above threshold.
3. **Judges get the ground truth as input.** Policy-compliance judges get the policy text, looked up by the scenario's issue type — not whatever the bot retrieved, or a retrieval mistake grades itself as correct. Hallucination judges get the tool responses.
4. **Scorecard, not a single score.** Each conversation gets one pass/fail per rubric; the release gate is per-rubric pass rates across the batch vs. baseline — no regressions, stricter bars on policy and hallucination than on tone.
5. **Prove the simulator is realistic.** Match a business metric (escalation rate) between simulation and live traffic, and check that offline gains carry over online.
6. **Same rubric offline and online.** Calibration stays aligned between development and production.
7. **Measure what users do, not what the agent claims.** Acceptance rate for the reviewer, conversion for the shopping agent.

### Component-level evals: the memory / retrieval example

Our own design, not from the posts (DoorDash only reports end-to-end numbers). Treat a memory-backed agent as a **funnel** and give each stage a metric, so an end-to-end failure points to one stage:

```
 fact stored?  → intent asked for it? → plan could reach it? → retrieved? → kept after trim? → used correctly?
 (extraction)    (memory-kind recall)   (plan coverage,         (recall@K,    (critical-fact     (binary judge
                                         0 isolation violations) stale rate)   survival,          rubrics)
                                                                               distractor rate)
```

- **Golden set:** synthetic users with **planted facts**, plus tasks with must-return and must-not-return lists. Relevance labels from a calibrated binary judge ("is fact X relevant to task Y?") and human review of real traces.
- **Usage rubrics:** exclusion honored, constraint respected, parameter applied, no memory hallucination, no over-personalization, live data wins over memory.
- **Write path:** extraction precision and recall, durability classification, health-data saves = 0, over-deletion on "forget" = 0.
- **Fact ablation:** remove a fact and re-run; if the output doesn't change, it wasn't worth its tokens.

Full version with metric tables: [doordash_assistant_memory.md](../../project-deep-dive/doordash_assistant_memory.md).

**Beyond DoorDash:** how Anthropic, OpenAI, Google, Shopify, Airbnb, Sierra, Uber and well-known practitioners do it → [Agent eval reading list](./reading_list.md).

**Hands-on:** what Level 1 (code-assertion) tests look like for the support bot, how they gate releases and run in production, and the order of work between tests and features → [Level 1 tests for a support bot](./level1_unit_tests.md).

---

## Short answer to "How do you know your agent is good?"

> "Three layers. Offline, every change to the prompt, model, or tools runs against an eval set built from real conversations — mostly computable outcome checks, plus model graders that we've calibrated against human labels — and it has to pass per intent, not just on average. Before full rollout, we shadow and then canary with online metrics: resolution rate, but always paired with repeat contact and CSAT so we don't reward the agent for refusing to escalate. And every production failure gets traced, replayed, and added to the eval set, so the set gets harder over time."

**Your anchor:** [how you actually evaluated the DoorDash chatbot; what the labeling agent produced; one regression the evals caught].
