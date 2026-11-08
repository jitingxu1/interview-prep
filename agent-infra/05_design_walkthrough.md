# 05 — System Design Walkthrough

**Prompt:** "Design an agent platform that lets many internal teams build and run agents." (Variants: "...for creator tools at TikTok," "...for contact-center automation," "...for an AI-native ERP.")

Paced for a 45-minute round. Rehearse out loud with a timer; draw the diagram from [01](./01_reference_architecture.md#layers) from memory.

---

## 0–5 min: Clarify and scope

Ask, then **state assumptions out loud** and move on.

- Who are the users — platform engineers, product engineers, or non-engineers (ops, creators)? *(Drives SDK vs config vs no-code.)*
- What kinds of agents — chat turns, long-running back-office tasks, coding? *(Drives sync vs durable.)*
- Do agents take **actions** (writes, money, messaging users) or only answer? *(Drives the safety design.)*
- Scale: how many teams, agents, runs per day?
- Constraints: data residency, which models are allowed, latency target.

**Assumptions to state if they don't specify:**
- ~50 teams, a few hundred agents, mix of interactive chat (p95 first token < 2s) and long-running tasks (minutes to hours).
- Agents take real actions on internal systems.
- Multiple model providers plus internal models.
- Back of envelope: 1M runs/day × ~5 model calls × ~4K tokens ≈ 20B tokens/day. **The cost is tokens, not compute** — so the design centers on token efficiency, quotas, and caching.

## 5–10 min: Requirements

| Functional | Non-functional |
|---|---|
| Define, version, deploy an agent | Safe: no action beyond granted permissions |
| Shared tool catalog | Observable: every step traceable and replayable |
| Session state and memory, retrieval | Reliable: long runs survive crashes; no duplicate side effects |
| Evals and gated rollout | Cost-bounded per tenant |
| Human approval for risky actions | Self-serve: a team ships its first agent in [days], not a quarter |

Say the **platform success metric** early: *time for a new team to ship an agent to production*, and *% of agent traffic on the platform*. That's what a platform leader is measured on.

## 10–25 min: High-level design

Draw the layers top-down and walk one request through them:

1. **Gateway** authenticates, applies tenant quota, routes to the pinned agent version (or canary).
2. **Runtime** loads the agent definition (prompt, model policy, tool allowlist, limits) and starts the loop; creates a run record.
3. **Model gateway** calls the chosen model; handles fallback, caching, token accounting.
4. **Tool gateway** validates args, checks permission policy, executes with delegated credentials, logs to audit.
5. **State store** checkpoints each step (for durable runs); **memory / retrieval** serves context.
6. **Tracing** emits spans for every step; **eval service** consumes traces for online metrics.

**Agent definition** — the core abstraction to show:

```yaml
agent: refund-assistant
version: 7
model_policy: {primary: large-model, router: small-model, fallback: alt-provider}
instructions: prompts/refund_v7.md
tools: [order.lookup@2, refund.issue@1, ticket.escalate@3]
limits: {max_steps: 15, max_tokens: 60000, timeout_s: 120}
approvals: {refund.issue: {auto_below_usd: 50, else: human}}
evals: evalsets/refund_v4
rollout: {canary_pct: 5, gate: [resolution_rate, repeat_contact, csat]}
```

Point out: everything a product team owns is in this file; everything else is the platform.

## 25–40 min: Deep dives (let them pick; have all four ready)

1. **Durable execution and side effects** — checkpoint per step, replay without re-calling, idempotency keys, HITL as a parked state. → [02](./02_harness_and_runtime.md#durable-execution)
2. **Tool ecosystem governance** — registry, MCP at the edge, automated onboarding checks, description changes trigger dependent evals. → [03](./03_tool_ecosystem.md)
3. **Evals as deploy gate** — computed outcome checks, calibrated judges, per-slice gates, shadow → canary. → [04](./evaluation/evals_and_observability.md)
4. **Context and cost** — tool retrieval, result truncation, compaction, sub-agents, prompt caching, small models for routing. → [02](./02_harness_and_runtime.md#context-management)

## 40–45 min: Trade-offs, risks, and what you'd build first

- **Build order:** (1) runtime + tracing + model gateway, onboard 2–3 design-partner teams; (2) tool registry and eval gate once patterns repeat; (3) self-serve and no-code only after the abstractions are stable. Don't build the platform before you have two real customers — that's the foundation story told forwards.
- **Biggest risks:** platform becomes a bottleneck (fix: self-serve + escape hatch); safety incident from a write tool (fix: side-effect classes + approvals + audit); cost blow-up (fix: quotas + budgets).
- **What you'd measure:** time-to-first-agent, % agent traffic on platform, eval coverage, incidents per 1M runs, cost per successful outcome.

---

## Org design (if they ask)

For a ~30-person agent platform org, one way to cut it — present as a starting point, not a dogma:

| Pod | Owns |
|---|---|
| Runtime & harness | Agent loop, durable execution, SDK, sandboxing |
| Tools & integrations | Tool gateway, registry, MCP, auth delegation |
| Model & knowledge | Model gateway, retrieval / memory, caching, cost |
| Quality & safety | Eval infra, judges, guardrails, red-teaming |
| Solutions / applied | Embedded with first design-partner teams; turns repeated patterns into platform features |

The applied pod is the one people forget. It keeps the platform honest about what customers need.

---

## Variant hooks

- **TikTok PGC / creators:** agents for creator tools — content ideation, editing assistance, moderation pre-checks, ops automation. Emphasize multi-tenant scale, multilingual, global stakeholders, and cost per creator action.
- **Cresta / contact center:** real-time voice + chat, strict latency (agent assist must land inside the conversation), compliance, per-customer config of the same agent.
- **Rillet / ERP:** actions on financial records — correctness and audit over flexibility; deterministic workflows with agentic steps; every write reviewable and reversible.
- **Snorkel / AI platform:** eval and data are the product — lean into labeling, programmatic graders, and the eval-set lifecycle.
