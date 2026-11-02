# 01 — Reference Architecture

What a production agent platform is made of. Use this as the map for any "walk me through the architecture" question, and as the checklist when you write the chatbot deep dive.

---

## The one-sentence version

> "An agent platform is a runtime that runs a model in a loop with tools, plus everything you need so that many teams can do that safely: a shared tool layer, state and memory, evals, observability, and guardrails — so a product team writes the prompt, the tools, and the eval set, and the platform owns the rest."

## Layers

```
            ┌──────────────────────────────────────────────┐
 Clients    │  Product surfaces · internal apps · APIs     │
            └───────────────┬──────────────────────────────┘
                            │
            ┌───────────────▼──────────────────────────────┐
 Gateway    │  AuthN/Z · tenant quotas · rate limits ·     │
            │  routing to agent version · streaming        │
            └───────────────┬──────────────────────────────┘
                            │
            ┌───────────────▼──────────────────────────────┐
 Runtime /  │  Agent loop · planner/router · context mgmt  │
 Harness    │  durable state · retries · HITL · sub-agents │
            └───┬───────────────┬───────────────┬──────────┘
                │               │               │
     ┌──────────▼───┐   ┌───────▼───────┐  ┌────▼─────────────┐
     │ Model gateway│   │ Tool layer    │  │ Memory / knowledge│
     │ multi-model, │   │ registry, MCP,│  │ session state,    │
     │ fallback,    │   │ auth, sandbox │  │ long-term memory, │
     │ caching, cost│   │ rate limits   │  │ RAG / retrieval   │
     └──────────────┘   └───────────────┘  └───────────────────┘

 Cross-cutting:  Evals · Tracing/observability · Guardrails/policy · Cost
```

| Layer | Owns | Key design questions |
|---|---|---|
| **Gateway** | Identity, tenancy, quotas, versioned routing, streaming | Per-tenant budgets? How do canaries and A/B of agent versions route? |
| **Runtime / harness** | The loop: call model, dispatch tools, update context, decide when to stop | Stateless vs durable? How long can a run last? Where does a human approve? |
| **Model gateway** | One interface over many models; fallback, retries, prompt caching, token accounting | Who picks the model — platform or product team? How do you fail over without changing behavior? |
| **Tool layer** | Tool registry, schemas, execution, auth delegation, sandboxing | Who owns a tool? How is it versioned? Whose credentials does it run with? |
| **Memory / knowledge** | Conversation state, user memory, retrieval over documents | What is persisted vs recomputed? Freshness? PII retention? |
| **Evals** | Offline test sets, graders, regression gates, online quality metrics | What blocks a deploy? How do you grade multi-step trajectories? |
| **Observability** | Traces of every step, tool call, token, latency, cost | Can an on-call engineer replay a bad conversation in five minutes? |
| **Guardrails / policy** | Input/output filtering, tool permissions, PII, action limits | Which actions need a human? What's the blast radius of a bad tool call? |

---

## Design choices worth having an opinion on

### 1. Framework vs platform
- **Framework** (a library teams import): fast to start, but every team reinvents ops, evals, and safety. Upgrades are N migrations.
- **Platform** (a hosted runtime): central ops, consistent guardrails and evals, one place to upgrade models. Costs more upfront and risks becoming a bottleneck.
- **Position to take:** thin SDK + hosted runtime. Teams declare agents (prompt, tools, model policy, eval set) as config plus code; the platform runs them. Leave an escape hatch for teams that need custom loops, but they still emit traces and pass the same eval gate.
- **Anchor:** Ibis — one interface, many backends. Same idea: one agent contract, many models and tools.

### 2. Single agent vs multi-agent
- Default to **one agent with good tools**. Multi-agent adds latency, cost, and debugging pain.
- Split into sub-agents when you need **context isolation** (a research step that would blow up the main context), **parallelism** (independent sub-tasks), or **different permissions** (a read-only planner and a write-capable executor).
- Routing pattern for support: a lightweight **router/classifier** in front, then specialized agents or workflows per intent. Deterministic workflows for high-volume, well-understood intents; open-ended agent for the long tail.

### 3. Workflow vs agent
- **Workflow:** code decides the steps, the model fills in each one. Predictable, testable, cheap.
- **Agent:** the model decides the steps. Flexible, harder to bound.
- Most production systems are a **mix**: deterministic skeleton, agentic steps where flexibility pays. Say this — it signals production experience.

### 4. Synchronous vs durable execution
- Chat turns: synchronous, streaming, seconds.
- Long tasks (research, back-office automation, multi-hour coding agents): **durable execution** with checkpointed state so a crash or deploy resumes rather than restarts. See [02](./02_harness_and_runtime.md#durable-execution).

### 5. Who owns what (the platform contract)

| Product team owns | Platform owns |
|---|---|
| Prompt / instructions, domain tools, eval set, success metric | Runtime, model access, tool hosting standards, tracing, eval infra, guardrails, quotas, on-call for the platform |

Getting this contract explicit is half of running an agent platform org. It also tells you how to split a 30-person team — see [05](./05_design_walkthrough.md#org-design-if-they-ask).

---

## Map to your DoorDash system

Fill these in — they're the backbone of the chatbot deep dive.

| Layer | What you built / used |
|---|---|
| Gateway / entry | [support channel(s), how a conversation enters] |
| Router | [intent classification? model or rules?] |
| Agent loop | [framework or in-house; who built the execution infra (S8 engineer)] |
| Tools | [refund, order lookup, account actions... how many, who owns them] |
| Retrieval | Real-time RAG for live cases; batch RAG for the offline labeling agent. [index, chunking, freshness] |
| Evals | [offline set, labeling agent output, human review] |
| Guardrails | [action limits, refund caps, escalation to human] |
| Rollout | [shadow → % traffic → full? metric that gated it] |
