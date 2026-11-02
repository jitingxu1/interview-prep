# 04 — Evals and Observability

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

## Short answer to "How do you know your agent is good?"

> "Three layers. Offline, every change to the prompt, model, or tools runs against an eval set built from real conversations — mostly computable outcome checks, plus model graders that we've calibrated against human labels — and it has to pass per intent, not just on average. Before full rollout, we shadow and then canary with online metrics: resolution rate, but always paired with repeat contact and CSAT so we don't reward the agent for refusing to escalate. And every production failure gets traced, replayed, and added to the eval set, so the set gets harder over time."

**Your anchor:** [how you actually evaluated the DoorDash chatbot; what the labeling agent produced; one regression the evals caught].
