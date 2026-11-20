# Agent Eval Playbook: Start Small, Find the Broken Component, Iterate

[Evals and observability](./evals_and_observability.md) covers *what* to measure. This file covers *how to run the process*: how to judge an agent, how to tell which component to fix, and how to grow from 20 test cases to a real eval system. Researched 2026-11-02.

Main sources: Anthropic's *Demystifying evals for AI agents* (Jan 2026), Hamel Husain & Shreya Shankar's evals FAQ, Meituan's 《Agent 评测漫谈》 (Aug 2026) and 《Agent 评测白皮书 01》 (Sep 2026), and LangChain's run/trace/thread guide. All first-party, all read.

---

## TL;DR

1. **Read traces before you write evals.** Error analysis (Hamel): annotate ~30 real traces, note the *first upstream* failure in each, group the notes into a failure taxonomy, count. The taxonomy tells you which evals to build.
2. **Start with 20–50 tasks from real failures** (Anthropic). Don't wait for a big benchmark.
3. **Two layers answer two questions.** End-to-end evals ask *did it work?* Process / component evals ask *where did it break?* (LangChain: "Full-turn and multi-turn evals show us whether the agent broke, while single-step evals show us where it broke.")
4. **Grade outcomes, not paths.** Check the database state, not the agent's claim. Use strict trajectory matching only where order matters for safety.
5. **Agents are random: run k trials.** pass@k = at least one success; pass^k = all succeed. Customer-facing agents need pass^k (75% per trial → ~42% for 3/3).
6. **Two suites with different jobs.** Capability evals start at a low pass rate and show progress. Regression evals sit near 100% and catch breakage. Capability tasks "graduate" into regression.
7. **Every failure needs triage: is it the agent, a coverage gap, or a bad grader?** (Meituan.) If you only ever fix the agent, you end up optimizing it to please the grader.
8. **The judge is a model too, so calibrate it.** Binary yes/no rubric items; human–human and human–model agreement at ~85–90% before you trust it (Meituan; Shopify got κ 0.02 → 0.61 vs a 0.69 human baseline).

---

## Part 1 — Is the agent good? (end-to-end)

Treat the agent as a black box first.

| Agent type | Primary grader | Add |
|---|---|---|
| **Support / conversational** | Final state check (refund issued, ticket resolved, right amount) | Simulated user (a second LLM); turn-count limits; rubric for tone; thread-level resolution |
| **Coding** | Tests pass (deterministic) | Static analysis; LLM rubric for code quality |
| **Research / RAG** | Groundedness + coverage checks | Source-quality rubric calibrated to experts |
| **Computer-use** | Backend state in a sandbox | — |

**Rules that save you pain (Anthropic):**
- A good task is one where **two experts would give the same pass/fail**. Every task needs a reference solution, which proves it's solvable.
- Include **should-do and should-not-do** cases, e.g. both over-searching and under-searching. Otherwise you optimize one direction.
- Run every trial in a **clean, isolated environment**. Shared state creates correlated failures.
- **A task at 0% across many trials is usually a broken task, not a weak agent.** Their CORE-Bench example: 42% became 95% after fixing rigid grading and ambiguous specs.
- **Read the transcripts.** A score alone can't tell an agent mistake from a grader rejecting a valid answer.

**Multi-turn:** single-turn metrics often don't correlate with user success (LangChain). Use **N−1 testing**: replay a real conversation prefix and let the agent generate only the next turn. It's cheap and realistic.

---

## Part 2 — Which component is broken? (attribution)

This is the hard part. Nobody has a fully automatic answer; the arXiv literature still calls causal attribution open. What practitioners actually do:

### Step 1: Find the first upstream failure in each trace

Downstream errors are usually caused by an upstream one. A wrong route produces bad retrieval, which produces a wrong answer. Fix the first one. (Hamel; Meituan.)

### Step 2: Transition failure matrix (Hamel)

Define the agent's states. For a support agent: `intent → route → retrieve → tool call → policy check → respond`. For each failed trace, record the **last state that succeeded** and the **state where it first failed**:

```
                     first failure at →
last success ↓   route   retrieve   tool_args   policy   respond
start              12        -          -          -        -
route               -       31          4          -        -
retrieve            -        -         18          2        9
tool_args           -        -          -          6        3
```

The hot cells tell you where to spend effort. Here, retrieval after a correct route (31) is the biggest bucket. The matrix gets coarse for very long runs; for those, use goal checkpoints instead, each milestone pass/fail.

### Step 3: Component evals for the hot cells

Build an eval set *only* for components that the matrix says are failing. Use classic metrics:

| Component | Metric | Eval set |
|---|---|---|
| **Router / intent** | Accuracy, confusion matrix per intent | Labeled turns. Evaluate separately: a router error contaminates every downstream metric (Mastra) |
| **Retrieval** | recall@k, MRR, "answer is in the retrieved chunks" | Query → gold document |
| **Tool selection / args** | Right tool, args valid and correct | Single-step: freeze the agent at the decision and assert (LangChain `interrupt_before`) |
| **Planner** | Plan covers required steps; no unnecessary ones | Reference plans; LLM judge |
| **Skill / sub-agent** | Skill call success rate; skill output correctness | Per-skill set, owned by that skill's team (Meituan aligns eval sets with org ownership so a failure has an owner) |
| **Generation** | Faithfulness to context, policy compliance, tone | Rubric judge, one criterion per judge |

### Step 4: Confirm with a counterfactual

Before you blame a component, **swap in the gold version and rerun**: oracle retrieval, a correct route, a perfect tool result. If the end-to-end pass rate jumps, that component is the bottleneck. If it doesn't, the problem is downstream. This is the cleanest way to rank components by headroom.

### Step 5: Read the online signals together (Meituan's example)

| End-to-end | Process metric | Diagnosis |
|---|---|---|
| Delivery rate 68% → 55% | "Ads data" skill success 95% → 70% | That skill broke. Engineering fix |
| Completion −5 pts | One skill's failure rate 2% → 15% | Engineering / dependency issue |
| Completion −5 pts | Process metrics normal, but "data comparison" tasks 10% → 35% of traffic | User mix shifted toward something the agent is weak at. Capability gap: add cases, improve the agent |
| Drops | All process metrics normal | **Unknown failure.** Mine new cases; your eval set has a blind spot |

---

## Part 3 — Start small, then iterate

### Stage 0 → 1: Cold start (week 1–2)

- **Minimum traceability first** (Meituan's 最小可归因): log the full model input/output and every tool/skill call, and be able to replay a bad case from its trace. Without this, attribution is guesswork.
- **Error analysis on ~30 traces.** One domain expert annotates, without committees. Stop at saturation, when new traces show no new failure modes. (Hamel)
- **20–50 tasks from real failures + the core happy paths.** Mostly code-based checks on outcomes. (Anthropic)
- **One gate:** the suite runs on every prompt, model, or tool change. Meituan's cold-start bar is level 1 on observability, eval set, and regression gate, which is enough for a closed loop.

### Stage 2: Scale up

- **Add LLM judges for the subjective parts**, and calibrate them: break vague criteria into **binary yes/no/unknown rubric items**, use the unknown rate to find bad rubric items, and iterate until human–human and human–model agreement reach ~85–90%. Meituan's example: one judge went from 62% to 92% agreement.
- **Split eval sets by purpose** (Meituan):
  - 黄金集 **golden**: defines the floor of "good"
  - 必过集 **must-pass**: core functions; safety and data-accuracy checks are one-vote veto
  - 错题集 **mistakes**: every past bug, so it never recurs
  - 挑战集 **challenge**: maps the capability frontier; hard to build, ages fast
- **Online evals:** sample ~10% of production traces and run cheap deterministic checks; trigger LLM judges only when those drop (LangChain). Add shadow mode before launch, A/B after, and periodic 巡检 (scheduled re-runs of representative tasks).
- **Component evals for the hot cells only** (Part 2).

### Stage 3: The flywheel (two loops)

From Meituan's white paper. Both loops share the same entry (case mining + triage) and the same asset (the eval sets):

```
       production signals (low CSAT, escalation, retries, complaints, monitors)
                              │
                              ▼
                     case mining → triage
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
   agent is wrong     eval set missed it    grader was wrong
   (prompt, skill     → add case to set     → fix rubric / metric,
   desc, context,                             add to 错题集
   model)
           │
           ▼
   fix → rerun regression + capability suites → shadow → A/B → ship
```

- **Loop A (agent):** fix the agent, backtest, ship.
- **Loop B (eval system):** fix coverage and graders. Teams skip this loop, and that's how the agent ends up optimized to please the eval.
- Positive cases go into golden or challenge sets.

### Keeping the suite alive

- **Saturation:** a suite at 100% only catches regressions. Graduate it to regression and write harder capability tasks. (SWE-bench Verified went ~30% → 80%+ in a year.)
- **Ownership:** a small evals team owns the infra; product and domain teams contribute tasks. (Anthropic, Meituan)
- **Find the shortest plank** (Meituan's L0–L3 maturity check): if graders are automated at scale but case mining still relies on user complaints, fix mining first. The worst shape is an eval set and a dashboard that don't talk to each other.
- **Re-run error analysis periodically.** New features and new user mixes bring new failure modes.
- **Cost:** report cost per *successful* task, and track tokens and steps per task as eval metrics too.

---

## Worked example: DoorDash-style support agent

1. **Week 1:** pull 50 escalated or low-CSAT conversations. Annotate the first failure. Taxonomy, say: wrong intent 20%, missing policy doc 35%, wrong refund amount 15%, tone 10%, other 20%.
2. **Build:** 40 tasks = top failures + happy paths. Graders: refund amount and order state (code), policy-cited-correctly (judge, binary). Run 3 trials each and report pass^3.
3. **Attribute:** the transition matrix shows most failures at *retrieve after correct route*. Swap in oracle retrieval and pass^3 jumps 25 points, so retrieval is the bottleneck. Build a retrieval eval (query → gold policy doc, recall@5) and iterate on chunking and the index *against that set*, which is fast and cheap. Then confirm end-to-end.
4. **Ship:** regression suite in CI → shadow → canary. Online: sample 10% for deterministic checks, plus containment paired with repeat contact and CSAT ([evals and observability](./evals_and_observability.md)).
5. **Flywheel:** weekly case mining from escalations → triage (agent / coverage / grader) → update sets. Re-run error analysis monthly.

**Your anchor:** the offline labeling agent is the Stage-2 machinery (judge-drafted labels, human review of disagreements). Bring a real agreement number if you have one.

---

## Likely follow-ups

**The eval passed but users are unhappy. Why?**
The suite is stale or one-sided, single-turn metrics don't predict thread success, or the grader is wrong. Run error analysis on fresh production traces, add thread-level evals, and audit the judge's agreement.

**How do you know the LLM judge is right?**
Binary rubric items, one criterion per judge, measured agreement with humans (κ or % agreement against a human–human baseline), and re-calibration whenever the judge model or the rubric changes.

**How many test cases is enough?**
To start, 20–50 drawn from failures. Later, enough per slice that the regression you care about (say 3 points on a high-stakes intent) is bigger than run-to-run noise across k trials.

**End-to-end dropped. How do you find what broke?**
Check process metrics first, using Meituan's table. If they're all normal, it's an unknown failure: pull the failing traces, build the transition matrix, and run an oracle swap on the suspect component.

**How do you stop the agent from overfitting to the eval?**
Hold out a fresh set, triage grader errors as their own category, include should-not-do cases, and keep A/B results on real users as the final judge.

---

## Sources

- [Anthropic — Demystifying evals for AI agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Hamel Husain — Why is error analysis so important, and how is it performed?](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html)
- [Hamel Husain — How do I evaluate agentic workflows?](https://hamel.dev/blog/posts/evals-faq/how-do-i-evaluate-agentic-workflows.html) · [Substack version with transition matrix](https://hamelhusain.substack.com/p/how-do-i-evaluate-agentic-workflows)
- [美团技术团队 — Agent 评测漫谈](https://tech.meituan.com/2026/08/07/Agent-Evaluation.html)
- [美团技术团队 — Agent 评测白皮书 01：评测全览](https://tech.meituan.com/2026/09/10/Agent-Evaluation-White-Paper-01.html)
- [LangChain — Evaluating agents at the run, trace, and thread level](https://www.langchain.com/resources/agent-evals)
- Secondary / vendor: [Confident AI — agent evaluation guide](https://www.confident-ai.com/blog/llm-agent-evaluation-complete-guide) · [Mastra — agent evaluation](https://mastra.ai/articles/ai-agent-evaluation) · [Databricks — what is agent evaluation](https://www.databricks.com/blog/what-is-agent-evaluation) · [DeepEval — agent evaluation](https://deepeval.com/guides/guides-ai-agent-evaluation) · [Google — agent quality flywheel](https://developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/) · [Lee Hanchung — hidden debt of agent eval infra](https://leehanchung.github.io/blogs/2026/06/13/hidden-technical-debt-agent-evaluation-infra/) · [腾讯云 — Agent 质量评估](https://cloud.tencent.com/developer/article/2597942) · [AWS 中国 — Agent quality evaluation](https://aws.amazon.com/cn/blogs/china/agent-quality-evaluation)
- Research: [Long-horizon agent trajectory attribution benchmark (arXiv 2608.06909)](https://arxiv.org/pdf/2608.06909)
