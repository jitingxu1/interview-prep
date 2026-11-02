# 03 — Tool Ecosystem

Tools are where an agent touches the real world, and where a platform either scales or turns into a mess. The interesting questions are organizational as much as technical: **who owns a tool, who can use it, and what happens when it changes.**

---

## What a tool is, contractually

| Field | Why it matters |
|---|---|
| Name + description | The model picks tools from the description. This is prompt engineering, and it's owned by the tool's team. |
| Input / output schema | Validated by the harness; rejects hallucinated args before they hit a backend |
| Side-effect class | `read` / `write` / `irreversible` (money, external messages). Drives the permission policy. |
| Auth mode | Runs as end user (delegated) or as a service identity; required scopes |
| SLOs | Latency, error budget, rate limit |
| Owner + on-call | A team, not a person |
| Version | Semver; breaking schema changes get a new major |

## MCP and standards

- **MCP (Model Context Protocol)** is the de facto open standard for exposing tools (and resources/prompts) to agents: a server advertises tools with JSON schemas, any MCP-capable client can call them.
- Platform position: **adopt the standard at the edge, add governance in the middle.** Teams expose tools as MCP servers (or an internal equivalent); the platform runs a **tool gateway / registry** in front that adds auth, quotas, logging, and policy.
- Benefit: the same tool works in your hosted agents, in internal coding agents, and in third-party clients, with no per-framework adapters.

## Registry and discovery

- Central catalog: every tool with schema, owner, side-effect class, SLOs, version, and **which agents use it**.
- Self-serve onboarding: a team registers a tool, it passes automated checks (schema valid, description quality lint, auth configured, eval cases attached), then it's available.
- Usage analytics per tool: call volume, error rate, latency, how often the model picks it wrongly. Tools with high misuse get their descriptions fixed or get merged.

## Tool selection at scale

With hundreds of tools, you can't put every schema in every context: it costs tokens and makes selection accuracy worse.

- **Scope per agent:** each agent declares an allowlist. Most agents need 5–20 tools.
- **Dynamic retrieval:** for broad agents, retrieve the top-k relevant tools per turn (embedding search over descriptions), or expose a `search_tools` meta-tool.
- **Toolkits:** group related tools (e.g., "order management") so agents attach a bundle.
- **Avoid overlap:** two tools that do nearly the same thing is the top cause of wrong-tool errors. Registry review should catch it.

## Versioning and change management

- Non-breaking changes (new optional field) roll out in place.
- Breaking changes: new major version, both run side by side, agents pinned to a version migrate deliberately.
- **Description changes are behavior changes.** Rewording a description can change which tool the model picks. Run the eval suites of the agents that use the tool before shipping — the registry knows who they are.
- Deprecation: usage dashboard shows who still calls v1; owners get a deadline.

## Auth, permissions, safety

- **Delegated auth:** when the agent acts for a user, it uses the user's scoped token (OAuth-style), so it can never do more than the user could.
- **Least privilege per agent:** an agent's tool allowlist plus per-tool scopes. A support agent can issue refunds up to `[cap]`; above that it routes to a human.
- **Side-effect gates:** `irreversible` tools require confirmation (user or human reviewer) or run in a dry-run/preview mode first.
- **Prompt injection:** tool results and retrieved content are untrusted. Don't let content from a tool result authorize a write. Keep secrets out of the model's context entirely.
- **Audit log:** every write tool call recorded with run id, agent version, user, args, result. Non-negotiable for money-moving tools.

## Quality of tools themselves

Agents are only as good as their tools. Platform-level practices:

- Return **model-friendly** errors ("order 123 not found; check the id") instead of stack traces.
- Return **compact** results; paginate.
- Make tools **idempotent** where possible; accept idempotency keys otherwise.
- Ship each tool with **eval cases**: prompts where it should be chosen, prompts where it shouldn't, and expected args.

---

## The governance question (manager-level)

> "Many teams contribute tools. How do you keep quality up without becoming a bottleneck?"

> "Make the standard cheap and the review automated. The platform publishes the tool contract, a template, and lint checks — schema, description quality, auth, attached eval cases. Passing the checks gets you into the catalog without a meeting. The platform team only reviews tools in the irreversible class, like anything that moves money or messages a customer. Then quality is managed with data: every tool has a dashboard for error rate, latency, and how often the model misuses it, and the owners of the worst ones get a ticket. Central standards, distributed ownership."

**Your anchor:** [how tools were added and owned on the DoorDash support agent; who owned refund / order tools; any time a tool change broke the agent].
