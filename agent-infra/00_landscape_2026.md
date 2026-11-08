# 00 — Agent Infra Landscape (Nov 2026)

What companies are building to run **many** agents, not one. Short survey for interview talking points. Researched 2026-11-01.

> **Source caveat:** most public material is vendor blogs and secondary write-ups. Treat product dates and adoption numbers as directional; the three company case studies (Cloudflare, Starburst, PhonePe) are first-party engineering posts and are the most reliable part.

---

## TL;DR

1. **The problem moved from "build an agent" to "run a fleet."** A prototype is easy; dozens to hundreds of agents owned by different teams is where things break: credentials, cost, safety, quality drift.
2. **The industry converged on one shape: an "agent plane."** The platform owns everything that isn't domain logic (model access, tool credentials, identity, runtime, deploy, telemetry). Agent teams own prompt, tools, and judgment. Starburst's phrase: *"the plane, not the fleet."*
3. **Hyperscalers now sell the same component list:** runtime, gateway, identity, registry, memory, policy, evals, observability. AWS (Bedrock AgentCore), Google (Gemini Enterprise Agent Platform, replacing Vertex AI in April 2026), Microsoft (Foundry + Agent 365 + Entra Agent ID), and OpenAI (Frontier, Feb 2026).
4. **Standards are settling at the protocol layer:** MCP (agent ↔ tool), A2A (agent ↔ agent), and AGENTS.md (repo context), all now under the Linux Foundation's Agentic AI Foundation. Observability conventions (OpenTelemetry GenAI) are still unstable.
5. **The unsolved problems are governance problems:** acting on behalf of the actual user, evals as a deploy-blocking gate, detecting drift, and accurate cost attribution.

---

## The converged stack

| # | Layer | What it does | State of the art in 2026 |
|---|---|---|---|
| 1 | **Front door / routing** | One entry point; route a request to the right agent | Starburst: one Slack app routes by explicit prefix, thread stickiness, then a classifier over agent descriptions, then a default agent |
| 2 | **Runtime / harness** | Runs the agent loop | Managed runtimes: AgentCore Runtime, Gemini Agent Runtime; SDKs: OpenAI Agents SDK, Claude Agent SDK. Common split: always-on agents on containers, short scheduled agents on per-second-billed serverless runtimes (Starburst: ECS Fargate vs AgentCore) |
| 3 | **Durable execution** | Long runs survive crashes; resume, don't restart | Temporal positioning as the durable layer above sandboxes (sandbox lifecycle tied to the workflow); Cloudflare uses Durable Objects + Workflows |
| 4 | **Sandboxes** | Isolated code / shell / browser execution | E2B (Firecracker microVMs), Modal (gVisor), Daytona, GKE Agent Sandbox, AgentCore Code Interpreter/Browser. Consensus: sandbox compute is largely solved; integrating it with orchestration isn't |
| 5 | **Model / AI gateway** | Single proxy for all model calls: keys, routing, caching, cost | Cloudflare: one proxy injects provider keys server-side (no keys on laptops), maps users to anonymous IDs for per-user cost, enforces zero data retention. Pattern everywhere: frontier models for hard reasoning, cheaper open models for routine work |
| 6 | **Tool layer (MCP)** | Agents reach internal systems through tools | MCP is the default. Enterprises put an **MCP gateway** (auth, policy, logging) and a **registry** (owner, tools, who can discover) in front of MCP servers. Cloudflare: one portal, one OAuth flow, 13 servers, 182+ tools |
| 7 | **Identity & authorization** | Who is this agent, and on whose behalf is it acting? | Agents as first-class identities: Entra Agent ID, Okta for AI Agents, Gemini Agent Identity (cryptographic ID per agent). On-behalf-of via OAuth token exchange (RFC 8693). Deterministic policy on every tool call: AgentCore Policy uses Cedar at the gateway |
| 8 | **Registry / control plane** | Inventory of every agent, tool, MCP server; who owns it | Microsoft Agent 365, AWS Agent Registry, Google Agent Registry, CNCF `agentregistry` (Solo.io). Google's design rule: no agent exists without an identity, deploys without a registry entry, or talks without passing a gateway |
| 9 | **Memory & context** | Session state, long-term memory, org knowledge | Memory: Mem0 (fact extraction layer), Zep (temporal knowledge graph), Letta (stateful runtime), plus managed memory in AgentCore. Org context: service catalogs (Backstage) and AGENTS.md files per repo |
| 10 | **Evals** | Quality gate before and after deploy | Managed: AgentCore Evaluations (LLM-as-judge + code evaluators, online and batch). Real-world gap: evals often live inside each agent, not as a platform-wide deploy gate |
| 11 | **Observability** | Traces of model calls, tool calls, tokens, cost | OpenTelemetry GenAI semantic conventions define agent / model / tool spans but are still marked Development; competing schemas (OpenInference, OpenLLMetry). Gateways are the natural place to emit telemetry |
| 12 | **Interop protocols** | Agents and tools from different vendors work together | MCP (tools), A2A v1.0 (agent-to-agent delegation; donated to the Agentic AI Foundation Aug 2026), AGENTS.md (repo instructions) |

---

## Vendor platforms at a glance

| Vendor | Product | Notable pieces |
|---|---|---|
| AWS | Bedrock AgentCore | Runtime, Memory, Gateway, Identity (token vault for OAuth to Slack/GitHub/Salesforce), Code Interpreter, Browser, Observability, Policy (Cedar), Evaluations, Agent Registry |
| Google | Gemini Enterprise Agent Platform (Apr 2026, successor to Vertex AI) | Agent Runtime, Agent Identity, Agent Gateway, Agent Registry |
| Microsoft | Azure AI Foundry + Agent 365 + Entra Agent ID | Agent 365 is a control plane with an agent registry and risk signals from Defender / Entra / Purview; agents managed in Entra much like employees |
| OpenAI | Frontier (Feb 2026), Agents SDK | Build and manage agents, including ones built outside OpenAI; enterprise IAM for agent permissions. Agents SDK added sandbox support (Modal, Daytona, Docker, E2B) |
| Anthropic | Claude Agent SDK, Managed Agents | Harness-as-SDK approach; details of Managed Agents not verified in this survey — check Anthropic docs |

**Interview angle:** everyone sells the same eight boxes. The differentiation for an internal platform team is **integration with the company's own identity, data, and tools**, and **the developer experience** that makes teams choose the platform.

---

## Case studies (first-party engineering posts)

### Cloudflare — internal AI engineering stack
- **Scale:** 3,683 active AI coding users (60% of company, 93% of R&D), 295 teams, 241B tokens/month through the gateway; weekly merge requests up from ~5,600 to 8,700+.
- **Design:** SSO → one proxy Worker → AI Gateway. One MCP portal (13 servers, 182+ tools). Backstage service catalog + AGENTS.md generated for ~3,900 repos. Risk-tiered AI code reviewer in CI with specialized review agents.
- **Key trick — "Code Mode":** the portal collapses all tool schemas into two tools (search, execute). The GitLab server alone had cost ~15,000 tokens of schema across 34 tools.
- **Lessons:** route everything through one proxy from day one; make context explicit (stale AGENTS.md is worse than none); reduce tool-schema overhead centrally; use open models where cost and latency matter (~9% of traffic).

### Starburst — Nebula ("the plane, not the fleet")
- **Scale:** 82 production agents owned by teams across the company; started by two engineers.
- **Design:** `/nebula new` scaffolds an agent through Claude Code using runbooks in the repo (no CLI). One container image per agent. Tools accessed through **named grants** on a managed MCP gateway that holds the credentials — agents never see secrets. Okta identity, every tool call audited. OIDC deploys, no stored credentials.
- **Lessons:** failing closed looks like silence (test that approvals *can* succeed); separate grant health from liveness so a provider outage doesn't cause restart loops; synthetic-data checks missed failures on real sensitive records; **a shared model proxy went unused because agents owned their own model-call code — the platform must own the call path to get adoption.**
- **Open problems they name:** acting on behalf of the requesting user; cost is estimated from tokens × price table, not reconciled with invoices; evals aren't a platform-wide deploy gate yet; drift between prompts, grants, and models goes undetected.

### PhonePe — Engineering Agent Hub
- **Scale:** 200+ internal agents, 1,600+ daily queries, ~759 weekly active users.
- **Design:** ephemeral Docker containers with no network and PID limits; local MCP servers launched from an internal artifact repo (air-gapped, regulatory-driven); agents, knowledge bases, and tools in one vector index for semantic discovery; bulk fan-out (e.g., 10,000 CSV rows) with parent-child tracking; self-hosted open models for routine work, frontier for hard reasoning.
- **Results they report:** lending reverse-audit from 3–4 days to 2–3 minutes; AI drives 80% of end-to-end fraud investigations; cost per investigation down from ₹50 to ₹5–15. *(Fraud investigation agents — directly relevant to your DoorDash background.)*

---

## Open problems (good "what would you work on" answers)

1. **On-behalf-of identity.** The agent should act with the requesting user's permissions, not a service account's. Token exchange exists; wiring it through every tool and hop is the hard part.
2. **Evals as a platform gate.** Most companies have per-agent evals; few block deploys platform-wide on them, especially when a *tool* or *model* changes underneath many agents.
3. **Drift detection.** Prompts, tool grants, and models change independently; nothing notices when an agent stops matching its description.
4. **Cost attribution.** Per-team and per-agent cost reconciled with actual invoices, and budgets enforced at the gateway.
5. **Tool-context overhead.** Hundreds of tools don't fit in context; search/execute meta-tools and per-agent allowlists are the current answers.
6. **Unstable observability standards.** Instrument to OTel GenAI for portability, but expect attribute names to change.
7. **Adoption.** The platform has to be the easiest path, and has to own the call path (gateway, SDK) or teams route around it.

---

## How to use this in interviews

- **Opening frame (TikTok HM, Snorkel):** "The hard part of agents in 2026 isn't building one — it's running a fleet. Every serious platform has converged on the same split: the platform owns identity, credentials, model access, runtime, and telemetry; teams own prompt, tools, and judgment. Where platforms still differ is evals as a real deploy gate and acting on behalf of the user — that's where I'd focus."
- **Cite one case study** by name with one number. It signals you track the field. Starburst's "platform must own the call path" lesson pairs well with your foundation-over-firefighting story.
- **For Cresta / contact center:** PhonePe's fraud investigation numbers and your DoorDash support + fraud work are the same domain.
- **For Rillet / ERP:** deterministic policy on every tool call (Cedar-style) and audit logs on every write.

Deeper detail on each layer: [01](./01_reference_architecture.md) · [02](./02_harness_and_runtime.md) · [03](./03_tool_ecosystem.md) · [04](./evaluation/evals_and_observability.md).

---

## Sources

**First-party engineering posts**
- [Cloudflare — The AI engineering stack we built internally](https://blog.cloudflare.com/internal-ai-engineering-stack/)
- [Starburst — The Plane, Not the Fleet (Nebula)](https://www.starburst.io/blog/starburst-nebula-ai-agent-the-plane-not-the-fleet/)
- [PhonePe — Engineering Agent Hub](https://tech.phonepe.com/engineering-agent-hub-how-phonepe-built-a-production-grade-internal-ai-platform/)
- [Gorgias — How we built a company-wide internal AI platform](https://medium.com/gorgias-engineering/how-we-built-a-company-wide-internal-ai-platform-b57947cad08b)

**Vendor platforms**
- [AWS — AgentCore Policy and Evaluations (preview announcement)](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-agentcore-policy-evaluations-preview)
- [AgentCore suite capabilities (secondary)](https://github.com/davidamitchell/Research/wiki/2026-05-17-aws-bedrock-agentcore-suite-capabilities)
- [Google — Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)
- [Google — Agent Registry overview](https://docs.cloud.google.com/agent-registry/overview)
- [ITPro — Google consolidates Vertex AI into Gemini Enterprise](https://www.itpro.com/technology/artificial-intelligence/google-expands-gemini-enterprise-consolidates-vertex-ai-services-to-simplify-agent-deployment)
- [TechCrunch — OpenAI launches Frontier](https://techcrunch.com/2026/02/05/openai-launches-a-way-for-enterprises-to-build-and-manage-ai-agents/)
- [Microsoft Agent 365 control plane (secondary)](https://dev.to/thenexusguard/microsoft-just-built-a-control-plane-for-ai-agents-here-is-what-it-cannot-do-k6i)
- [Google / Microsoft / IBM — the race to build the AI control plane (secondary)](https://www.softwareseni.com/google-microsoft-ibm-the-race-to-build-the-ai-control-plane)

**Runtime, sandboxes, durability**
- [Temporal — Temporal and agentic sandboxes with the OpenAI Agents SDK](https://temporal.io/blog/introducing-temporal-and-agentic-sandboxes-openai-agents-sdk)
- [Temporal — Sandbox orchestration harness](https://temporal.io/blog/temporal-sandbox-orchestration-harness-the-missing-layer-for-running-agents)
- [Modal — Code execution sandboxes for agents](https://modal.com/resources/best-code-execution-sandboxes-tool-calling-ai-agents)

**Tools, identity, registry**
- [Gravitee — MCP gateway](https://www.gravitee.io/blog/mcp-gateway)
- [WitnessAI — MCP gateway](https://witness.ai/blog/mcp-gateway/)
- [MCP in regulated environments (Toronto MCP Dev Summit)](https://datalakehousehub.com/blog/mcp-regulated-environments-toronto-2026/)
- [Bigeye — What is an agent registry](https://www.bigeye.com/blog/what-is-an-agent-registry)
- [Atlan — AWS Agent Registry](https://atlan.com/know/ai-agent/aws/what-is-aws-agent-registry.md)

**Standards**
- [A2A joins MCP at the Linux Foundation (secondary)](https://www.flowhunt.io/blog/agentic-ai-foundation-a2a-mcp-standards/)
- [A2A meets MCP — the protocol stack](https://codex.danielvaughan.com/2026/04/09/a2a-meets-mcp-protocol-stack/)
- [OpenTelemetry — AI agent observability](https://opentelemetry.io/blog/2025/ai-agent-observability/)
- [Greptime — OTel GenAI semantic conventions status](https://www.greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions)

**Memory**
- [Atlan — Agent memory frameworks compared](https://atlan.com/know/best-ai-agent-memory-frameworks-2026/)

**Landscape overviews**
- [Enterprise agentic AI platforms 2026](https://agentic-ai.readthedocs.io/en/latest/AgentPlatforms/enterprise-platforms-2026/)
- [Dataiku — Enterprise agentic AI platforms](https://www.dataiku.com/blog/best-enterprise-agentic-ai-platforms)
