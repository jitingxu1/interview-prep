# Agent Eval Reading List (Nov 2026)

How big companies and well-known practitioners evaluate LLM agents: blogs, guides and one paper, each with the takeaway that matters for interviews. Researched 2026-11-07. Part of the [evaluation section](./README.md); companion to [Evals and observability](./evals_and_observability.md).

> **Source caveat:** summaries come from web search results and the posts' own descriptions, not a full read of every article. Items marked *(secondary)* are write-ups of a company's talk, not the company's own post. Check the original before quoting a number in an interview.

---

## TL;DR — what everyone agrees on

1. **Error analysis first, metrics second.** Read traces, write notes, group failures into a taxonomy, *then* build evals for the failures you actually have (Hamel & Shreya, Eugene Yan, Anthropic).
2. **One narrow judge per failure mode, usually binary.** Generic "rate it 0–10" judges don't work (Shopify, Airbnb, DoorDash, Hamel).
3. **Calibrate judges against human experts**, and treat human–human agreement as the ceiling (Shopify, Shankar, Eugene Yan, DoorDash).
4. **Agents need trajectory evals, not just final-answer evals:** right tool, right order, right args, policy followed (OpenAI trace grading, Google ADK, Anthropic).
5. **Grade the end state when you can.** Check the database or system state after the run instead of the agent's words (τ-bench, Anthropic).
6. **Measure reliability, not just success:** pass^k — does it succeed on *every* one of k tries? (Sierra τ-bench, Anthropic).
7. **Make evals the default, not an afterthought:** tracing on by default and evals as a deploy gate (Uber, Airbnb, DoorDash).
8. **Verification is easier than generation** — the reason LLM judges and verifier passes work at all (Jason Wei; DoorDash code reviewer).

---

## Big companies

### Anthropic — *Demystifying evals for AI agents* (Jan 9, 2026)
[anthropic.com/engineering/demystifying-evals-for-ai-agents](https://anthropic.com/engineering/demystifying-evals-for-ai-agents)
- Gives a vocabulary for an agent eval: **tasks, trials, transcripts, outcomes, graders, and the eval harness**.
- Multi-turn agents compound mistakes, so single-turn tests aren't enough.
- Covers outcome vs. trajectory grading, isolated trials, and **pass@k vs. pass^k**.
- Practical roadmap: start with a **small, representative task set drawn from real failures**, define success before optimizing, and match graders to the task.
- **Interview use:** the cleanest framework to name when asked "how would you evaluate an agent?"

### OpenAI — *Trace grading* and *Evaluate agent workflows* (developer guides)
[Trace grading](https://developers.openai.com/api/docs/guides/trace-grading) · [Agent evals](https://developers.openai.com/api/docs/guides/agent-evals/)
- **Trace grading** scores the whole trace (decisions, tool calls, reasoning steps), not just the final answer.
- Questions it answers: did the agent pick the right tool? did a handoff happen when it should? did it violate a policy? did a routing change help end to end?
- Combines grader types, with **code (Python) graders as the workhorse**: assert on tool-call order, argument correctness and step count.
- Each dataset row carries the input plus the metadata graders need (expected tool args, step budget, ground-truth facts).
- **Interview use:** "white-box" eval — explains *why* an agent failed, not just *that* it failed.

### Google Cloud — *From vibe checks to continuous evaluation* + ADK eval
[Cloud blog](https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents) · [Agent Factory recap](https://cloud.google.com/blog/topics/developers-practitioners/agent-factory-recap-a-deep-dive-into-agent-evaluation-practical-tooling-and-multi-agent-systems) · [Evaluate agents (docs)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents) · [ADK eval codelab](https://codelabs.developers.google.com/adk-eval/instructions)
- Two kinds of agent eval: **final-response evaluation** and **trajectory evaluation** (e.g., did it call `check_inventory` before `place_order`?).
- Built-in rubric metrics for agents: final response quality, tool-use quality, hallucination.
- Continuous evaluation wired into the dev loop with ADK, the GenAI evaluation service and Cloud Run.

### Microsoft — Foundry agent evaluation + ISE framework
[Evaluating AI agents with Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/evaluating-ai-agents-a-practical-guide-with-microsoft-foundry/4500224) · [ISE: Intuitive evaluation framework for agentic chatbots](https://devblogs.microsoft.com/ise/intuitive-evaluation-framework-for-agentic-chatbots/) (Sept 2025)
- Agent evaluation is "a different game" from LLM evaluation: it needs **scenario simulation, observability instrumentation and fine-grained analytics**.
- Non-determinism is the core challenge.
- The ISE post is a field case: an eval framework for line-of-business agentic chatbots in business-critical settings.

### Shopify — *Building production-ready agentic systems* (Sidekick, ICML 2025 talk)
[shopify.engineering/building-production-ready-agentic-systems](https://shopify.engineering/building-production-ready-agentic-systems)
- "Vibe testing" and a "Vibe LLM judge that rates 0–10" don't cut it.
- Replaced curated golden sets with **Ground Truth Sets (GTX)**: sampled from real production conversations, labeled by humans against criteria, and grown continuously. Sidekick's criteria: **safety, goal fulfillment, grounding, merchant sentiment**.
- **Human–human agreement is the ceiling** for a judge. Judge correlation improved **0.66 → 0.75**.
- Judges trained against GTX can then score unlimited production conversations, not just a fixed test set.
- Also covers reward hacking found during GRPO training — evals catch the model gaming the reward.
- **Interview use:** the closest match to your DoorDash support work; cite the 0.66 → 0.75 number.

### Airbnb — *Eval-driven development: lessons from evaluating GenAI at scale*
[airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale](https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/)
- LLM outputs are non-deterministic and "correct" is subjective, so you often need AI to evaluate AI — which brings its own failure modes.
- **Keep the evaluator set small and sharp: 3–5 well-calibrated judges beat 20–30 noisy ones**, each targeting one correctness dimension.
- **Interview use:** a crisp counterweight to "add more metrics."

### Sierra — *τ-bench: benchmarking AI agents for the real world*
[sierra.ai/blog/benchmarking-ai-agents](https://sierra.ai/blog/benchmarking-ai-agents) · [How τ-bench is shaping agent evaluation](https://sierra.ai/blog/tau-bench-shaping-development-evaluation-agents)
- Multi-turn customer-service tasks: an **LLM-simulated user** talks to an agent that has domain API tools and a **written policy**.
- **Grades the goal database state** at the end — fast and faithful, no judge needed.
- Introduced **pass^k**: probability of succeeding on all k repeated runs. Every tested model degraded sharply as k grew; the best (GPT-4o at the time) was under 50% average success.
- **Interview use:** same shape as DoorDash's support simulator (simulated customer + policy + tools). pass^k is the right answer to "is 80% good enough?" — not if it fails one run in five.

### Uber — evaluation-first agent platform *(secondary: Arize write-up of an Uber talk)*
[arize.com/blog/how-uber-evaluates-ai-agents-at-production-scale](https://arize.com/blog/how-uber-evaluates-ai-agents-at-production-scale/) · related: [Uber GenAI Gateway](https://www.uber.com/blog/genai-gateway/)
- Problem: teams shipped agents and deferred evals, then retrofitted and debugged.
- Fix: **tracing on by default** for every agent deployed through the managed platform, in every environment from day one (two lines of config for code-first SDKs); **AI-generated starter eval kits** delivered via Slack; CLI tools to make evals self-serve.
- **Interview use:** the platform answer to "evals aren't a deploy gate yet" (an open problem in [00](../00_landscape_2026.md)).

### Intercom — *AI is approving our pull requests: here's how we made it safe*
[intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe](https://intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe)
- 497 PRs went fully autonomous in the first four weeks of broader rollout (Claude writes, an AI approval system reviews and ships).
- AI-authored backend code had a **0.53% revert rate vs. 5.39% for human-authored** — an outcome metric, not a judge score.
- Pairs with the DoorDash code reviewer below.

### LinkedIn — Hiring Assistant
[LinkedIn AI stack for agents](https://news.linkedin.com/2025/linkedin-s-ai-stack--expanding-to-build-tomorrow-s-agents) · [LeadDev: how LinkedIn built its hiring agent](https://leaddev.com/ai/how-linkedin-built-ai-hiring-agent)
- Plan-and-execute supervisor with sub-agents (intake, sourcing, evaluation, outreach); curated rollout through a **charter beta** with a few enterprise customers.
- Public posts are **thin on eval methodology** — useful for architecture and rollout, not for eval detail.

### DoorDash — four systems (already in your notes)
- Support chatbot: LLM customer simulator + binary calibrated judges; hallucinations −90% → [chatbot_offline_simulator.md](../../project-deep-dive/chatbot_offline_simulator.md)
- Ask DoorDash: guardrail vs. capability evals; same rubric and judge offline and online → [Evals and observability](./evals_and_observability.md#how-doordash-does-it-first-party-engineering-posts)
- Agent memory: proposed per-stage eval funnel → [doordash_assistant_memory.md](../../project-deep-dive/doordash_assistant_memory.md)
- AI code reviewer: disprove-it verification; 60.2% acceptance → [doordash_ai_code_reviewer.md](../../project-deep-dive/doordash_ai_code_reviewer.md)

---

## Well-known practitioners

### Hamel Husain — the most-cited practitioner on product evals
- [*Your AI product needs evals*](https://hamel.dev/blog/posts/evals/) — the original case for evals as the core of AI product iteration. Study notes: [hamel_your_ai_product_needs_evals.md](./hamel_your_ai_product_needs_evals.md); applied to the support bot: [level1_unit_tests.md](./level1_unit_tests.md).
- [*Creating a LLM-as-a-Judge that drives business results*](https://hamel.dev/blog/posts/llm-judge/) — **Critique Shadowing**: find the one or two principal domain experts; have them give a pass/fail plus a detailed critique on real outputs; use those critiques as few-shot examples; iterate the judge until it agrees with the expert. Based on helping 30+ companies. His point: the judge is a "hack" to get people to look at their data carefully — **the process drives results, not the judge**.
- [*AI Evals: Everything you need to know* (FAQ, with Shreya Shankar)](https://hamel.dev/blog/posts/evals-faq/) — includes [why error analysis is the most important activity](https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html).

### Hamel Husain & Shreya Shankar — error analysis method (Maven course *AI Evals for Engineers & PMs*)
[Lenny's Newsletter: Why AI evals are the hottest new skill](https://www.lennysnewsletter.com/p/why-ai-evals-are-the-hottest-new-skill) · [Building eval systems that improve your product](https://www.lennysnewsletter.com/p/building-eval-systems-that-improve) · [Pragmatic Engineer: evals](https://newsletter.pragmaticengineer.com/p/evals)
- **Open coding:** read traces and write free-form notes on what went wrong (borrowed from qualitative research).
- **Axial coding:** group the notes into a **failure taxonomy** — "the most important step."
- Build evals only for the failure categories you found, so metrics reflect real behavior instead of generic scores.
- They've trained 2,000+ engineers and PMs, including teams at OpenAI and Anthropic.

### Shreya Shankar et al. — *Who Validates the Validators?* (UIST 2024, paper)
[arxiv.org/abs/2404.12272](https://arxiv.org/abs/2404.12272)
- **EvalGen:** an interface that helps people generate eval criteria and assertions, then aligns them with human grades.
- Key finding — **criteria drift**: you need criteria to grade outputs, but grading outputs is how you discover the criteria. You can't fully define criteria before looking at data.
- **Interview use:** why the eval set and rubrics must keep evolving, and why calibration is a loop, not a one-time step.

### Eugene Yan — three essays
- [*Evaluating the effectiveness of LLM-evaluators (aka LLM-as-judge)*](https://eugeneyan.com/writing/llm-evaluators/) — survey of judge prompting, alignment methods and benchmarks; documents judge biases and reliability limits.
- [*An LLM-as-judge won't save the product — fixing your process will*](https://eugeneyan.com/writing/eval-process/) — adding tools, metrics or judges sidesteps the real work.
- [*Product evals in three simple steps*](https://eugeneyan.com/writing/product-evals/) — (1) label a small dataset, (2) align LLM evaluators to it, (3) run the experiment + eval harness on every config change.

### Jason Wei — *Asymmetry of verification and verifier's law*
[jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law](https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law)
- Some tasks are much easier to verify than to solve.
- **Verifier's law:** how easy it is to train AI on a task is proportional to how verifiable the task is; anything solvable and easy to verify will be solved.
- **Interview use:** the theory behind the generator–verifier gap — why narrow LLM judges and "disprove-it" passes work.

### Simon Willison — *smevals* (Jul 31, 2026) and his evals tag
[simonwillison.net/2026/Jul/31/smevals](https://simonwillison.net/2026/Jul/31/smevals/) · [all posts tagged evals](https://simonwillison.net/tags/evals/)
- A small eval suite for comparing models, prompts and harnesses. His evals tag is a running digest of the field, including commentary on Hamel's judge post.

### Long-form guides
- [Cameron Wolfe — *Agent evaluation: a detailed guide*](https://cameronrwolfe.substack.com/p/agent-evals)
- [ICLR 2026 blog track — *A hitchhiker's guide to agent evaluation*](https://iclr-blogposts.github.io/2026/blog/2026/agent-evaluation/)
- [awesome-evals (GitHub list)](https://github.com/benchflow-ai/awesome-evals)

---

## How these map to your DoorDash work

| Idea | Where it shows up | Your DoorDash anchor |
| --- | --- | --- |
| Simulated user + tools + policy, grade the outcome | Sierra τ-bench, Microsoft | Support chatbot simulator (LLM customer, mocked tools, policy-compliance judge) |
| Narrow binary judges, calibrated to experts | Hamel, Shopify, Airbnb, Eugene Yan | One judge per failure mode; precision/recall calibration loop |
| Error analysis → failure taxonomy → evals | Hamel & Shreya, Anthropic | "Step 1: identify a customer problem" from expert review of traces |
| Criteria drift | Shankar | New failure modes keep adding evals (suite grew to 50+) |
| Production-sampled ground truth | Shopify GTX | Scenarios mined one-to-one from production transcripts |
| Trajectory / trace grading | OpenAI, Google | White-box simulation: tool calls and context inspected per step |
| pass^k reliability | Sierra, Anthropic | [gap] Did you run each scenario several times? Worth adding |
| Evals by default on the platform | Uber | One-click platform; evals triggered automatically after each run |
| Verification easier than generation | Jason Wei | Generator–verifier gap argument; code reviewer's disprove-it pass |
| Outcome metrics over judge scores | Intercom, DoorDash reviewer | Acceptance rate; offline gains holding in production |

## Suggested reading order (about 2 hours)

1. Anthropic — *Demystifying evals for AI agents* (the framework)
2. Hamel — *LLM-as-a-judge* (how to build a judge people trust)
3. Hamel & Shreya — error analysis FAQ entry (where evals come from)
4. Shopify — Sidekick post (a production case close to yours)
5. Sierra — τ-bench (simulated users and pass^k)
6. Jason Wei — verifier's law (the theory, 5 minutes)

## How to say it (about 45 seconds)

> "The field has converged on a few ideas. Start with error analysis — read traces and build a failure taxonomy, as Hamel Husain and Shreya Shankar teach — and only then write evals, one narrow judge per failure mode, calibrated against a domain expert, with human agreement as the ceiling, which is how Shopify measures its judges. For agents, grade the trajectory and the end state, not just the reply — OpenAI's trace grading and Sierra's τ-bench do that — and measure reliability with pass^k, not one lucky run. And make it the platform default: Uber turned tracing on for every agent from day one. At DoorDash we did the same pattern for support: a simulated customer, mocked tools, binary calibrated judges, and a release gate."

---

## Sources

All links are inline above. Secondary sources used for context: [ZenML LLMOps database — Uber eval-first culture](https://www.zenml.io/llmops-database/building-an-evaluation-first-culture-for-enterprise-agent-platform), [ZenML — Shopify Sidekick](https://www.zenml.io/llmops-database/building-and-evaluating-sidekick-a-production-agent-for-e-commerce-merchants), [ZenML — LinkedIn Hiring Assistant](https://zenml.io/llmops-database/building-linkedin-s-first-production-agent-hiring-assistant-platform-and-architecture).
