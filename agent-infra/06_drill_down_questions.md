# 06 — Drill-Down Questions

连环追问 practice. Each answer should fit in under 60 seconds and end with a concrete detail. `[brackets]` = replace with your real example before the interview.

---

## Framework and architecture

**Why not just use an open-source framework (LangGraph, etc.)?**
> Frameworks are fine as the loop. The platform value is everything around it: tool governance, evals, tracing, quotas, safety. I'd let teams use a framework inside the runtime as long as they emit the same traces and pass the same eval gate. What I'd avoid is every team building its own ops on top of a different framework.

**When would you use multiple agents?**
> Only for context isolation, real parallelism, or different permissions. Otherwise one agent with good tools is faster, cheaper, and easier to debug. [Did you split anything into sub-agents at DoorDash? Why?]

**Workflow or agent for customer support?**
> Both. Deterministic workflows for the high-volume, well-understood intents, because they're cheap and testable. An open-ended agent for the long tail. A router decides which. [Your intent split.]

**How do you handle model upgrades?**
> Pin the model per agent version. A new model is just a new version: run the eval suite, compare per slice, shadow, canary. Expect prompts to need retuning. Never upgrade every agent at once.

## Harness and runtime

**What happens if the runtime crashes mid-run?**
> Each step is checkpointed with its model output and tool result. On restart we replay from the log without re-calling the model or re-running side effects, then continue. Write tools take an idempotency key from run id + step, so a retry can't double-refund.

**How do you stop runaway agents?**
> Hard ceilings in the harness on steps, tokens, cost, and wall-clock, plus loop detection on repeated identical tool calls. When a ceiling is hit, the agent escalates to a human instead of failing silently.

**How do you manage context with long conversations?**
> Budget it. Truncate tool results, compact older turns into a structured summary, push noisy sub-tasks to sub-agents, and keep the system prompt and tool schemas stable so prompt caching hits.

**Where does the human come in?**
> As a permission policy, not a prompt instruction. Write and irreversible tools are classed; above a threshold the run parks in a waiting-for-approval state and resumes after review. [Your refund / escalation threshold.]

## Tools

**A tool team changes their API. What breaks and how do you prevent it?**
> Breaking schema changes get a new major version; agents are pinned and migrate deliberately. The subtle one is a description change — that changes model behavior — so the registry runs the eval suites of every agent using that tool before the change ships.

**How do you scale to hundreds of tools?**
> Per-agent allowlists so most agents see 5–20 tools; tool retrieval for broad agents; toolkits; and removing overlapping tools, which are the top cause of wrong-tool picks.

**How do you defend against prompt injection?**
> Treat all tool output and retrieved content as untrusted data. Content can't authorize actions — permissions are enforced in the harness. Delegated, scoped credentials limit the blast radius, secrets never enter the context, and write actions are audited.

## Evals and quality

**How do you evaluate a multi-step agent?**
> Outcome first — check the resulting system state where you can compute it. Then trajectory: right tools, right args, no policy violations. Model-as-judge for the fuzzy parts, calibrated against human labels. [Your eval set and graders.]

**How do you trust an LLM judge?**
> Measure its agreement with human labels on a held-out sample, one criterion per judge, pairwise where possible, and re-calibrate whenever the judge model changes.

**Your containment rate went up 10 points. Is that good?**
> Not by itself. I'd check repeat contacts and CSAT on the same conversations. If the agent stopped escalating cases it should have escalated, containment rises and customers get worse outcomes.

**What was the hardest bug you hit in your agent system?**
> [Real incident: symptom, how you found it (traces?), root cause, fix, what test you added.] Have this one ready — it's the most likely follow-up in a deep dive.

## Platform and org

**How do you get teams to adopt the platform instead of building their own?**
> Make the platform the fastest path, not the mandated one. Start with two or three design-partner teams, embed with them, and make their launch the case study. Measure time-to-first-agent and treat it like a product metric. Mandates come last, if ever.

**Platform team vs product team priorities conflict. What do you do?**
> Separate the goal from the requested solution, show the options with their cost, and agree on the decision in writing. Often the answer is an escape hatch now and a platform feature next quarter. → [10a](../leadership/stripe_strategy_and_execution/10a_saying_no_to_senior.md)

**How would you structure a 30-person agent platform org?**
> Four platform pods — runtime, tools, model and knowledge, quality and safety — plus a small applied pod embedded with customer teams. Each pod has a senior IC or line manager; I'd personally own the roadmap, the platform contract, and the relationships with the top customer teams. → [05](./05_design_walkthrough.md#org-design-if-they-ask)

**What's the first thing you'd do in 90 days?**
> Listen and map: which teams use the platform, what they built around it, where they're blocked. Then pick the one or two metrics the platform will be judged on, and fix the biggest blocker for the top customer team so there's a visible win early.
