# 02 — Harness and Runtime

"Harness" gets used two ways. **Ask which one the interviewer means** — it shows you know both.

1. **Agent harness:** the code around the model that turns a model into an agent — the loop, tool dispatch, context management, permissions, hooks, stopping rules. (Claude Code, Codex, and similar coding agents are harnesses around a model.)
2. **Eval / test harness:** the infrastructure that runs agents against test sets and grades them. Covered in [04](./04_evals_and_observability.md).

TikTok's "harness engineering infrastructure" most likely means #1, possibly both. This file is #1.

---

## The agent loop

```
while not done:
    response = model(system_prompt, context, tool_schemas)
    if response.has_tool_calls:
        for call in response.tool_calls:          # parallel where independent
            check_permission(call)                # policy / HITL gate
            result = execute(call, timeout, retries)
            context.append(call, truncate(result))
    else:
        done = True                               # model produced a final answer
    enforce_limits(steps, tokens, wall_clock, cost)
    maybe_compact(context)
```

Everything interesting in the harness is in those helper calls.

| Concern | What good looks like |
|---|---|
| **Stopping** | Final answer, max steps, max tokens, max cost, wall-clock timeout, or a human stop. Always a hard ceiling — runaway loops are the classic failure. |
| **Tool errors** | Return the error to the model as a tool result so it can recover; retry transient errors in the harness, not via the model. Idempotency keys on write tools. |
| **Parallel tool calls** | Run independent calls concurrently; serialize writes to the same resource. |
| **Permissions** | Per-tool policy: auto-allow (read), require approval (write / money / external send), deny. Evaluated in the harness, never trusted to the prompt. |
| **Hooks** | Pre/post tool-call hooks for logging, policy, redaction, metrics. This is how a platform adds behavior without every team changing code. |
| **Streaming** | Stream tokens and step events to the client; users tolerate latency much better when they see progress. |

---

## Context management

The context window is the agent's working memory, and it's the main thing the harness manages.

- **Budget it.** System prompt + tool schemas + history + retrieved docs + tool results. Tool schemas alone get large with many tools — see tool selection in [03](./03_tool_ecosystem.md#tool-selection-at-scale).
- **Truncate tool results.** Large API responses are the most common context blow-up. Return summaries or the relevant slice; let the agent request more.
- **Compaction.** When history gets long, summarize older turns into a running state and drop the raw text. Keep decisions, open tasks, and user constraints; drop intermediate reasoning.
- **Sub-agents for isolation.** Hand a noisy sub-task to a sub-agent with a fresh context; get back only the result.
- **Prompt caching.** Keep the stable prefix (system prompt, tool schemas) identical across calls so the provider's cache hits. Big latency and cost lever; breaks if you inject timestamps or per-request data at the top.
- **Structured state vs transcript.** For workflows, keep explicit state (order id, verified identity, refund amount) in a structured object the harness owns, not only in the chat transcript. Easier to test, audit, and resume.

---

## Durable execution

Needed when runs outlive a request: multi-step back-office tasks, long research, waiting on a human approval for hours.

- **Checkpoint after every step** (model call or tool call) to a store keyed by run id. On crash or redeploy, resume from the last checkpoint.
- **Deterministic replay:** record model outputs and tool results so a resume doesn't re-call the model or re-run side effects. Same idea as workflow engines (Temporal-style event histories).
- **Idempotent side effects:** every write tool takes an idempotency key derived from (run id, step). A retried refund must not refund twice.
- **Human-in-the-loop as a first-class pause:** the run parks in a `waiting_for_approval` state, a reviewer acts, the run resumes. No thread held open.
- **Versioning:** a run that started on agent v3 should finish on v3. Pin prompt, tools, and model per run.

---

## Isolation and sandboxing

- **Code execution** (agents that write and run code): ephemeral containers or microVMs, no ambient credentials, egress allowlist, CPU/memory/time limits, filesystem thrown away after the run.
- **Credentials:** tools run with **delegated, scoped** credentials for the end user or the agent's service identity — never a shared god token. Short-lived tokens issued per run.
- **Tenant isolation:** one team's agent can't see another team's tools, memory, or traces unless explicitly shared.

---

## Scaling the runtime

- Agent runs are **I/O-bound** (waiting on models and tools), so the runtime is cheap; model tokens are the cost. Async workers, high concurrency per worker.
- **Backpressure** at the gateway per tenant; model provider rate limits are the real ceiling. Queue and shed load before you hit them.
- **Model gateway** handles provider failover, retries with jitter, and per-tenant token accounting.
- Latency levers in order of impact: fewer sequential model calls (parallel tools, better prompts), smaller/faster model for routing and simple steps, prompt caching, streaming.

---

## Failure modes to name

| Failure | Mitigation |
|---|---|
| Infinite / long loops | Step, token, cost, and time ceilings; loop detection on repeated identical calls |
| Hallucinated tool args | Strict JSON schema validation; reject and return the error to the model |
| Wrong tool chosen | Better tool descriptions, fewer overlapping tools, eval cases targeting tool choice |
| Context blow-up | Result truncation, compaction, sub-agents |
| Prompt injection via tool results / retrieved docs | Treat tool output as data; permission gates on writes; no secrets in context |
| Duplicate side effects on retry | Idempotency keys; durable step log |
| Silent quality regression after a model upgrade | Eval gate in CI; canary with online metrics — see [04](./04_evals_and_observability.md) |

**Your anchor:** [which of these you actually hit at DoorDash, and what you changed]. One real incident beats this whole table.
