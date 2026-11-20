# 08 — How Companies Build Their Agents (Nov 2026)

How companies design **the agent itself**: single vs multi-agent, orchestration, context, model tiering, coding agents. [00](./00_landscape_2026.md) covers the platform layer underneath (gateway, identity, registry). [07](./07_case_deepseek_superagent.md) is the DeepSeek deep dive. Researched 2026-11-02.

> **Source caveat:** each card is marked **[1P]** (I read the company's own post or talk page) or **[2P]** (secondary write-ups of a company post I couldn't open). Quote numbers from [2P] cards only after checking the original.

---

## TL;DR — the patterns

1. **Start with one agent and many tools; split only when you must.** Shopify Sidekick is deliberately one agent. Anthropic says multi-agent fits only breadth-first, parallelizable work, at ~15× the tokens of chat.
2. **When you split, use one coordinator and isolated workers.** Anthropic (lead + subagents), DeepSeek (Router + Workers), LinkedIn (supervisor + sub-agents), DoorDash (Orchestrator + domain agents), Meituan, Kimi. Nobody serious runs a free-form "swarm."
3. **Many agents may read and think; only one writes.** This is Cognition's 2026 rule. Reviewers, verifiers, and researchers can run in parallel, but parallel *writers* still conflict.
4. **Pin follow-ups to the agent that owns the thread.** The same trick shows up three times: DeepSeek's subscription pass-through, DoorDash's pinned turns, Starburst's thread stickiness. It cuts router cost and keeps context coherent.
5. **Mix deterministic steps with agentic ones.** Stripe Blueprints (lint and CI are code, not model calls), Meituan's 手脑分离, Shopify's deterministic reward gates. The model handles judgment; code handles everything that has a right answer.
6. **Tier models by role.** A cheap model routes or does routine work; a strong one plans or writes. Examples: DeepSeek (light Router), Anthropic (Opus lead, Sonnet workers), Cognition's "Smart Friend" escalation.
7. **Context engineering is the real work.** Manus: KV-cache hit rate is the #1 metric, and the file system serves as memory. Shopify: just-in-time instructions inside tool results. Cloudflare: collapse 182 tools into search + execute.
8. **Coding agents went background and unattended.** Stripe, Ramp, Uber, DoorDash, Cursor, and Codex all share the same shape: Slack or a ticket in, a sandboxed VM, a PR out, human review.

---

## The core debate: one agent or many?

| | Single agent + tools | Orchestrator + workers |
|---|---|---|
| **Who** | Shopify Sidekick, Cognition (2025 stance), most coding agents in their main loop | Anthropic Research, DeepSeek Super-agent, LinkedIn Hiring Assistant, DoorDash Assistant, Meituan CatPaw, Kimi Swarm, Devin manager mode |
| **Wins when** | Tasks are sequential and share context; you need easy debugging and low cost | Work is parallel or breadth-first, exceeds one context window, or spans domains owned by different teams |
| **Costs** | Context bloat as tools grow; one slow task blocks everything | ~4–15× tokens (Anthropic), ~3.8× cache reads (DeepSeek); context loss at handoffs; coordination bugs |
| **Key quote** | Cognition: subagents that get only a summary miss the upstream decisions | Cognition 2026: "writes stay single-threaded and the additional agents contribute intelligence rather than actions" |

**Two different reasons to split** (say this in interviews, it shows judgment):
- **For throughput / parallelism:** Anthropic, DeepSeek, Kimi. One task fans out, or many tasks run at once.
- **For org ownership:** DoorDash, LinkedIn, Meituan. Each domain team ships its own agent on its own release cycle. This is Conway's law, not a model limitation.

---

## Company cards

### Agent architecture

**Anthropic — Research (multi-agent)** [1P, Jun 2025]
- Lead agent plans and spawns 3–5 subagents in parallel; each subagent uses 3+ tools in parallel. Effort scales with the query, from 1 agent and 3–10 calls up to 10+ subagents.
- Opus lead + Sonnet subagents beat single-agent Opus by 90.2% on their internal research eval, and cut time by up to 90% on complex queries.
- Cost: agents use ~4× the tokens of chat, multi-agent ~15×. Bad fit when all agents need the same context or have many dependencies.
- Lessons: prompts are the main lever; early versions spawned too many subagents for simple queries; they needed resume-from-checkpoint and custom tracing.

**DeepSeek — Super-agent** [1P repo, Oct 2026]
- Always-on Router (light model, no tools) plus isolated Workers (strong model, full tools). p95 29.5 → 15.7 min. Full notes in [07](./07_case_deepseek_superagent.md).

**Cognition — Devin / Windsurf** [1P, Apr 2026: "Multi-Agents: What's Actually Working"]
- Revisits their 2025 "Don't Build Multi-Agents." What works now:
  1. **Generator–verifier:** Devin plus Devin Review. ~2 bugs found per PR, ~58% severe. The reviewer works best with *no* shared context, reasoning from the diff alone.
  2. **Smart Friend:** a small primary model escalates hard cases to a big one. It only works if the primary is strong enough to know when to ask (SWE-1.5 wasn't).
  3. **Manager → child Devins:** coordinated over an internal MCP. Problems they hit: managers over-prescribe, children wrongly assume shared state, cross-agent messages don't happen unless designed in.
- Still doesn't work: parallel-writer swarms and unstructured agent negotiation. They prefer map-reduce-and-manage. Every remaining problem is a communication problem.

**LinkedIn — Hiring Assistant** [2P, 2025; QCon London talk]
- Supervisor agent plus specialized sub-agents (intake, sourcing, evaluation, outreach, screening, learning).
- Chose **plan-and-execute over ReAct**: more predictable and cheaper for long recruiter workflows.
- Runs on a **message-driven agent platform** reused across LinkedIn products. Ambient: works in the background and reports back. Experiential memory learns recruiter preferences. Reportedly built on LangGraph.

**DoorDash — Ask DoorDash / DoorDash Assistant** [2P, part 4 dated Jul 2026]
- Orchestrator routes each turn to a **domain agent** (restaurant discovery, grocery, later reservations) over **A2A**. Follow-up turns are **pinned** to the chosen agent.
- Built on Google ADK, plus what ADK lacks: distributed tracing, model access, durable state, rollout controls. A shared gateway handles client streaming.
- Agent memory reportedly raised grocery checkout 24% and cut intent misunderstandings 33%. The 3rd domain agent took ~1 week, ~10× faster than the first ones.
- Deeper notes: [Ask DoorDash agent memory](../project-deep-dive/doordash_assistant_memory.md).
- ⚠️ **This is your company.** Know these posts cold, and know which parts you can talk about beyond what's public.

**Shopify — Sidekick** [2P]
- Deliberately **one agent with a large toolbox**. Subagents were explored but not adopted.
- **Just-in-time instructions:** tool-specific guidance comes back *in the tool response* instead of bloating the system prompt.
- **Calibrate the judge first:** LLM-judge agreement with experts went from Cohen's κ 0.02 → 0.61 (human-to-human baseline 0.69) before they trusted it.
- **Reward hacking:** during RL the model gamed the grader; the fix was cheap deterministic checks gating the reward.

**Moonshot — Kimi Agent Swarm** [2P + Kimi help pages]
- The orchestrator is a **trained policy**, not a prompt: spawning a sub-agent is an action it learns with RL (PARL).
- Reward has three parts. Besides task performance, a parallelism reward fights "serial collapse" (never spawning) and a finish reward fights "spurious parallelism" (spawning for show).
- Scale: K2.5 up to 100 sub-agents; K2.6 up to 300. Swarm now runs on K3; I found no K3 report.

**Meituan — CatPaw / AgentOS** [1P talk abstract, QCon Shanghai Oct 2026; CatPaw launch Jul 2026]
- **手脑分离:** the model does understanding, judgment, and planning (the brain); the harness provides knowledge, tools, state, sandbox, permissions, and verification (the hands). Deterministic logic goes in code.
- AgentOS: stateless agent loop, distributed sessions, short-lived sandboxes, cloud storage, and a registry for agent identity and permissions. Multica handles multi-agent tasks via Issue/Task/Runtime with human approval.
- Evals are a **pre-launch gate**, not after-the-fact scoring. Merchant-level sandboxes; baseline-vs-candidate regression before release.
- Scale: CatPaw covers ~90k employees internally, ~30k agents built.

**Manus (now part of Meta) — context engineering** [1P, Jul 2025]
- **KV-cache hit rate is the #1 production metric.** Cached vs uncached input is ~10× cheaper. Keep the prompt prefix stable (no timestamps up front), make context append-only, and serialize JSON deterministically.
- **Mask tools, don't remove them:** constrain decoding by tool-name prefix instead of changing the tool list mid-task, which would break the cache.
- **File system as memory:** compress reversibly (drop the page, keep the URL or path); the agent reads it back when needed.

**Intercom — Fin** [1P blog + help center]
- Layers: App (training, deployment), AI (RAG-based), Model. Model-agnostic, so it can route per query and swap models without re-engineering. Now on its third major architecture iteration, moving from task-based toward goal-driven with persistent memory.

**Airbnb — support** [1P, older]
- Task-oriented conversational AI for self-service cancellations and refunds in 14 languages. A pre-LLM-agent design; useful only as the "before" picture.

### Coding agents (background / unattended)

| Company | What | Notable design | Reported scale |
|---|---|---|---|
| **Stripe — Minions** [2P] | One-shot ticket → PR, no human mid-run | Fork of Block's Goose with confirmations removed; runs in **pre-warmed EC2 devboxes** (~10s); **Blueprints** mix deterministic nodes (lint before push) with agentic ones; CI retries capped at 2; Toolshed MCP with ~500 internal tools | 1,000 → 1,300+ merged PRs/week |
| **Ramp — Inspect** [2P] | Company-wide background coding agent | Sandboxed VMs on Modal; entry from Slack, web, Chrome extension, voice, mobile | ~30% of merged PRs (Jan 2026) → reportedly over half; sources conflict |
| **Uber** [2P] | Agents across code review, CI fixes, alert triage | "Software factory" framing; Aug 2026 post focuses on **cost efficiency** at scale | 70%+ of PRs from coding agents (per secondary source) |
| **DoorDash — Flux** [2P] | Cloud coding agents | Own the primitives around the agent: orchestration, sandboxes, workflows, permissions, integrations, context | ~130k agent tasks in one month (headline, unverified) |
| **OpenAI — Codex** [1P] | Harness as a product | "Codex core" holds the loop; exposed via CLI, `codex exec`, SDK, App Server. "Harness engineering": engineers design environments, intent, and feedback loops instead of writing code; Codex iterates until agent reviewers pass | — |
| **Cursor** [2P] | Background agents | Each agent in its own cloud VM with a browser and video recording; Agents Window in Cursor 3 | Unverified |
| **ByteDance — Trae Agent** [1P repo + arXiv 2507.23370] | Open-source SWE agent | ReAct loop, modular, CLI | Benchmark claims unverified |

**The shared shape:** Slack/ticket in → sandboxed VM with the real dev environment → agent loop with internal tools via MCP → deterministic gates (lint, tests, CI) → PR → human review. The differentiators are environment startup speed, the internal tool catalog, and how much is deterministic.

---

## How to use this in interviews

**Opening line for "how would you design X agent":**
"I'd start with a single agent and a good toolset, as Shopify does, and split only for parallelism or team ownership. If I split, I'd use one coordinator and isolated workers, keep writes single-threaded, pin follow-ups to the owning worker, and put everything deterministic in code."

**Map to your anchors:**
- **DoorDash support chatbot** ↔ the orchestrator + domain-agent pattern. Explain where your routing sits compared to Ask DoorDash's, and why.
- **Offline labeling agent** ↔ Anthropic-style parallel workers with an LLM judge. Bring up Shopify's judge calibration (κ) as how you'd trust the labels.
- **Agent execution infra (S8)** ↔ Stripe devboxes, Meituan AgentOS, DoorDash Flux: own the primitives around the agent.

**By interview:**
- **TikTok (agentic framework / harness / tools):** lead with the patterns list. Meituan and Kimi show you track Chinese industry, which plays well with a ByteDance panel. Mention Trae Agent if asked about ByteDance's own work.
- **Cresta (contact center):** Intercom Fin, Airbnb, DoorDash Assistant, Shopify's judge calibration.
- **Snorkel (AI platform, data):** Kimi's learned orchestrator and Shopify's reward hacking. Both are data and eval problems.
- **Rillet (pair programming):** Stripe Blueprints, a deterministic + agentic mix, is the right instinct for finance and ERP workflows.

---

## Likely follow-ups

**When would you NOT use multi-agent?**
When subtasks share heavy context or depend on each other, or when the volume doesn't justify ~4–15× tokens. Cite Anthropic's own guidance and Shopify's choice.

**How do two agents avoid stepping on each other?**
Single writer (Cognition). Otherwise use a lock or branch per worker, with a coordinator that serializes conflicting tasks.

**Router mistakes: how do you catch them?**
Measure routing accuracy as its own metric on labeled traffic. Pin follow-ups so a misroute doesn't compound. Allow a worker to hand a turn back to the orchestrator.

**Plan-and-execute or ReAct?**
Plan-and-execute for long, predictable workflows where cost and auditability matter (LinkedIn). ReAct for exploratory work where the next step depends on what you just saw (coding agents).

**How do you keep cost under control?**
Cache-friendly context (Manus), model tiering, deterministic steps instead of model calls (Stripe), effort scaling by query difficulty (Anthropic), and per-agent budgets at the gateway ([00](./00_landscape_2026.md)).

---

## Sources

**First-party, read**
- [Anthropic — How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Cognition — Multi-Agents: What's Actually Working](https://cognition.com/blog/multi-agents-working)
- [Manus — Context Engineering for AI Agents](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [美团企业级 Agent 的平台化应用实践 — QCon 上海 (InfoQ)](https://www.infoq.cn/article/BQJltkL1FJ9AG3cMeUmB) · [QCon 议题页](https://qcon.infoq.cn/2026/shanghai/presentation/7335)
- [美团 CatPaw 发布](https://tech.meituan.com/2026/07/28/CatPaw-LongCat.html)
- [OpenAI — Unrolling the Codex agent loop](https://openai.com/index/unrolling-the-codex-agent-loop/) · [Unlocking the Codex harness](https://openai.com/index/unlocking-the-codex-harness/) · [Harness engineering](https://openai.com/index/harness-engineering/) · [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform)
- [Intercom — Preparing for the Customer Agent future](https://www.intercom.com/blog/preparing-for-the-customer-agent-future/) · [Fin over email](https://www.intercom.com/blog/fin-over-email-how-we-built)
- [Airbnb — Task-oriented conversational AI in customer support](https://medium.com/airbnb-engineering/task-oriented-conversational-ai-in-airbnb-customer-support-5ebf49169eaa)
- [Kimi — Agent Swarm help page](https://www.kimi.com/help/agent/agent-swarm)

**First-party, not opened (blocked or not found); details via secondary sources**
- DoorDash: [Building DoorDash Assistant](https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/) · [Ask DoorDash Part 2](https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/) · [Delegating engineering work to cloud agents](https://careersatdoordash.com/blog/delegating-engineering-work-to-cloud-based-agents/) · [Long-running agents](https://careersatdoordash.com/blog/engineers-journey-long-running-ai-agents/)
- [LinkedIn — GenAI stack extended to agents](https://news.linkedin.com/2025/linkedin-s-ai-stack--expanding-to-build-tomorrow-s-agents) · [QCon London talk](https://qconlondon.com/presentation/apr2025/lessons-learned-building-linkedins-first-agent-hiring-assistant)

**Secondary**
- Stripe Minions: [lilting.ch](https://lilting.ch/en/articles/stripe-minions-agent-architecture) · [MintMCP](https://www.mintmcp.com/blog/stripe-minions-explained) · [Dotzlaw](https://dotzlaw.com/insights/ai-04-stripe-minions-deterministic-rails/) · [Background Agents Summit](https://background-agents.com/summit/sessions/alistair-gray/)
- Ramp Inspect: [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect?from=bd_signal) · [Ramp vs Stripe](https://pkm-wiki.pages.dev/comparisons/ramp-inspect-vs-stripe-minions) · [In-house coding agents](https://rywalker.com/research/in-house-coding-agents)
- Uber: [ShiftMag](https://shiftmag.dev/how-uber-engineers-use-ai-agents-8617/) · [Software factory cost (Aug 2026)](https://explainx.ai/blog/uber-software-factory-agent-cost-optimization-august-2026)
- DoorDash Flux: [explainx](https://explainx.ai/blog/doordash-flux-cloud-agents-platform-august-2026)
- LinkedIn: [ByteByteGo](https://blog.bytebytego.com/p/how-linkedin-built-an-ai-powered) · [LeadDev](https://leaddev.com/ai/how-linkedin-built-ai-hiring-agent) · [ZenML](https://zenml.io/llmops-database/building-linkedin-s-first-production-agent-hiring-assistant-platform-and-architecture)
- Shopify Sidekick: [ZenML](https://www.zenml.io/llmops-database/building-and-evaluating-sidekick-a-production-agent-for-e-commerce-merchants) · [The AI Engineer](https://theaiengineer.substack.com/p/how-shopify-built-sidekick)
- Kimi: [Phil Schmid](https://www.philschmid.de/kimi-composer-context) · [Towards AI](https://pub.towardsai.net/kimi-k2-5-and-the-rise-of-agent-swarms-a-technical-deep-dive-into-parallel-ai-orchestration-d2fb2b8c7c9d)
- Cognition 2025: [jxnl](https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems/) · [LangChain response](https://blog.langchain.com/how-and-when-to-build-multi-agent-systems)
- Cursor: [Morph](https://www.morphllm.com/cursor-background-agents) · [agentmarketcap](https://agentmarketcap.ai/blog/2026/04/05/cursor-april-2026-agent-mode-overhaul-background-agents-ide-convergence)
- ByteDance Trae Agent: [新浪科技](https://finance.sina.com.cn/tech/digi/2025-07-07/doc-infeqytv6508898.shtml)
- 国内大厂格局: [36氪](https://www.36kr.com/p/3929141384953216) · [21财经](https://m.21jingji.com/article/20260730/herald/3d37f1efdf73657378a73614e46c7fca.html)

---

- [ ] Read the DoorDash Assistant / Ask DoorDash series directly (it blocked the fetcher) and fix the DoorDash card
- [ ] Open Stripe's Minions Part 1–2 on stripe.dev and LinkedIn's engineering post to confirm the [2P] numbers
- [ ] Not covered yet: Google/ByteDance Coze internals, Alibaba engineering post-mortems, Notion, Replit, Klarna
