# 07 — Case Study: DeepSeek Super-agent (Router / Worker)

DeepSeek's Harness team published *Exploring Super-agent Design: Towards a More Autonomous Agent System* on 2026-10-31 (long post, originally in Chinese) and open-sourced a research prototype, [`deepseek-ai/dsh-superagent-prototype`](https://github.com/deepseek-ai/dsh-superagent-prototype) (MIT). It's a proactive coding agent for one GitHub repo that listens to GitHub and, optionally, Feishu. It runs as a bundle on DeepSeek Harness (dsh).

Use it as a fresh, concrete example of multi-agent orchestration. It fits TikTok round 1 on **agentic framework** and **harness engineering**, and it's a good answer to "what have you read recently?"

> All numbers below are DeepSeek's own, from synthetic messages and mocked tools. They call them preliminary. Say that when you quote them.

---

## The problem they're solving

- **Single task → the bottleneck is the model.**
- **Many tasks → the bottleneck is the human.** One person can babysit maybe 3–5 agent sessions at once. Past that, you lose track of which session needs you.

Their move: take session management away from the human and give it to the system.

---

## Architecture

```
  GitHub / Feishu / chat            (external events = "Triggers")
            │
            ▼
   ┌──────────────────┐   two-stage filter: is this worth acting on?
   │      Router      │   persistent, always-on, holds global context
   │  (light model,   │   talks to humans, dispatches work
   │   no Bash)       │   never does the work itself
   └──────┬───────────┘
          │ dispatch                 ▲ results
          ▼                          │
   ┌──────────┐ ┌──────────┐ ┌──────────┐
   │ Worker A │ │ Worker B │ │ Worker C │   one per task, isolated context
   │ (strong  │ │          │ │          │   full tools, run concurrently
   │  model)  │ │          │ │          │   report to Router, not to users
   └──────────┘ └──────────┘ └──────────┘
          ▲
          └── subscription pass-through: follow-ups on a thread a Worker
              has claimed go straight to that Worker, skipping the Router

   Watchdog (external process): detects stuck / dead sessions
```

| Piece | Owns | Design choice worth noting |
|---|---|---|
| **Router** | Intake from all channels, global context, dispatch, the human-facing reply | No execution tools at all, not even Bash. Keeps it fast, cheap, and hard to derail. A light model is enough. |
| **Worker** | One task end to end | Context isolated per task, full toolset. Gets the strongest model, since it decides code quality. |
| **Triggers** | External events (issue opened, comment, chat message) | Two-stage filter before anything reaches the Router, so it isn't woken by noise. |
| **Subscription pass-through** | Follow-ups on a claimed thread | Without it, Router decisions rose ~30%. |
| **Full-duplex interrupts** | Human can redirect mid-task | Agent doesn't have to finish its turn before listening. |
| **Inline & Spill** | Moving results back to the Router | Small results inline; large ones spilled out of the Router's context (I read this as "don't flood the coordinator"). Check the repo docs before stating details. |
| **Watchdog** | Liveness | Runs outside the agents. An agent can't reliably detect that it is itself stuck. |

It looks more and more like a human org: a lead who triages and delegates, and ICs who own tasks.

---

## Results (self-reported, synthetic)

- Load test: ~300 messages containing 20 real requests.
- **p95 completion: 29.5 min (single session) → 15.7 min (Router/Worker)**, roughly 2× faster.
- **Cost: ~3.8× read-cache tokens** (third-party analysis). Each Worker rebuilds context that a single session would have shared.
- Router batching: sources disagree on the numbers (one says 6.4s → 1.6s per decision; another says per-request latency rose 2.5s → 3.9s as event rate rose). **Don't quote these.**

## Open problems they list

1. Scaling the Router (it's a single point of coordination)
2. Long-term memory
3. Agent-to-agent communication (Workers only talk via the Router today)
4. Prompt injection: the agent reads untrusted GitHub/Feishu content. The repo says its blocked-command list and wrappers are defaults, **not a security boundary**.

---

## How to use it in an interview

**One-liner:** "DeepSeek's Super-agent splits the agent into an always-on Router that only triages and delegates, and isolated Workers that execute. That shifts the bottleneck from the human babysitting sessions to the system, at the price of more tokens."

**Tie to your own work:**

- **DoorDash support chatbot:** the same split shows up as intent routing in front of specialized flows. Compare: your router classifies a customer's intent; theirs dispatches *tasks* and keeps a long-lived global context. Be ready to say where your router lived and which model ran it. (Fill in once the [chatbot deep dive](../project-deep-dive/) exists.)
- **Offline labeling agent:** a natural Worker-style job with isolated context and no user in the loop.
- **Agent execution infra ([S8](../star_stories/story_8_right_person_wrong_seat.md)):** Watchdog, isolation, and concurrency are platform concerns, not prompt concerns. That's the platform-instinct point.

**Map to the reference architecture ([01](./01_reference_architecture.md)):** Router = orchestration layer, Worker = runtime/sandbox ([02](./02_harness_and_runtime.md)), Triggers = event ingestion, Watchdog = ops/observability ([04](./04_evals_and_observability.md)).

---

## Likely follow-ups (连环追问)

**Why can't the Router just do small tasks itself?**
Once it has tools it can get stuck in a long task, and then nobody is answering new messages. A Router with no tools is always available. It's the same reason an on-call lead shouldn't pick up a big ticket.

**Why a light model on the Router and a strong one on Workers?**
The Router makes many short decisions (classify, dispatch, summarize), so latency and cost matter. Workers make few, long, high-stakes decisions, so quality matters. Route model choice by role, not one model everywhere.

**What does isolation buy you, and what does it cost?**
It buys no cross-task context pollution, parallelism, and a clean failure blast radius. It costs re-reading shared context per Worker (the ~3.8× cache tokens) and harder coordination when two tasks touch the same files.

**Two Workers edit the same file. What happens?**
The prototype doesn't solve this well; agent-to-agent communication is listed as open. Options: Router-level locking per resource, git branches per Worker with merge at the end, or the Router serializing conflicting tasks.

**The Router is a single point of failure. How would you scale it?**
Shard by channel or repo, with each shard owning its threads. Keep the global state in a durable store instead of in the context window, so a Router can restart without losing anything. The Watchdog restarts it.

**How would you evaluate this system?**
End-to-end task success and p50/p95 completion on a replayed message stream (their method); Router routing accuracy as its own metric; cost per completed task; how often a human had to step in. See [04](./04_evals_and_observability.md).

**Biggest risk in production?**
Prompt injection. It reads issue comments from anyone and has a Worker with full tools. Treat external content as data, sandbox Workers, gate writes (push, merge, external send) behind policy in the harness, and don't rely on a blocklist.

---

## Sources

- Repo README: [dsh-superagent-prototype](https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/README.md). The design docs are in `docs/` (`000-philosophy.md`, `007-architecture.md` are the most relevant).
- Summaries: [实践哥 Li on X](https://x.com/MinLiBuilds/status/2116871144145875173), [新浪财经](https://finance.sina.com.cn/roll/2026-11-01/doc-inixeyiz3146996.shtml), [知乎](https://zhuanlan.zhihu.com/p/2100019747622602327), [Joye Blog](https://www.joyehuang.me/notes/1126-deepseek-super-agent)
- Cost analysis (~3.8× read-cache tokens): [AIDeepThink](https://aideepthink.cn/news/202611-deepseek-superagent-prototype-router-worker-open-source)
- English write-ups: [CellCog](https://cellcog.ai/blog/deepseek-super-agent/), [Developers Digest](https://www.developersdigest.tech/blog/deepseek-dsh-superagent-router-worker-always-on-agent-2026), [Dataconomy](https://dataconomy.com/2026/11/02/deepseek-releases-open-source-dsh-superagent-coding-agent/)

- [ ] Read `docs/007-architecture.md` in the repo and correct anything above that's off, especially Inline & Spill
- [ ] Find the original slides you saw, if you can, and link them here
