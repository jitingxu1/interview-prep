# Evaluation

Everything on evaluating LLM agents in one place: the framework, how companies and practitioners do it, and a hands-on doc on Level 1 (code-assertion) tests for the DoorDash support bot. Part of [Agent Infra](../README.md).

**One line to remember:** evals are the deploy gate, traces are the debugger.

## Docs

| Doc | What's in it | Read when |
| --- | --- | --- |
| **[Evals and observability](./evals_and_observability.md)** | The framework: what to evaluate (outcome, trajectory, step, safety, cost), building the eval set, graders, evals as a deploy gate, online metrics, tracing, cost control; plus how DoorDash does it across four systems and a per-stage memory eval design | First — it's the map |
| **[Level 1 unit tests](./level1_unit_tests.md)** | Code-assertion tests for the support bot: vs. traditional unit tests, LLM-generated inputs, tests grown from traces, four test types with code, tiered gates, regression vs. guardrail vs. monitor, order of work with AI, and a worked example (late-delivery compensation) with who does what at each step | Before any hands-on or "how would you test it?" question |
| **[Eval-driven development (blog)](./eval_driven_development.md)** | The end-to-end workflow from a policy or design doc to a PR: ten phases with human checkpoints, dev/holdout split, locked tests and test disputes, trace reading (including passing traces), tiered gates, post-launch monitoring, and how to package it as a resumable Claude Code skill | To explain your dev process, or before building the skill |
| **[Hamel — *Your AI Product Needs Evals*](./hamel_your_ai_product_needs_evals.md)** | Study notes on the post behind the three levels: virtuous cycle, Lucy case study, Level 1/2/3, judge alignment, fine-tuning and debugging payoffs, how his thinking evolved | Background for the Level 1 doc |
| **[Reading list](./reading_list.md)** | How Anthropic, OpenAI, Google, Microsoft, Shopify, Airbnb, Sierra, Uber, Intercom and practitioners (Hamel Husain, Shreya Shankar, Eugene Yan, Jason Wei) evaluate agents, mapped to your DoorDash work | To cite a company or person by name |

## Related notes elsewhere

- [Chatbot offline simulator](../../project-deep-dive/chatbot_offline_simulator.md) — DoorDash's simulation and evaluation flywheel (simulated customer, binary calibrated judges, release gate)
- [Ask DoorDash agent memory](../../project-deep-dive/doordash_assistant_memory.md) — section 8: evaluating a memory pipeline stage by stage
- [DoorDash AI code reviewer](../../project-deep-dive/doordash_ai_code_reviewer.md) — disprove-it verification; acceptance rate as the success metric

## Suggested order

1. [Evals and observability](./evals_and_observability.md) — the framework and the DoorDash patterns
2. [Level 1 unit tests](./level1_unit_tests.md) — rehearse the worked example out loud
3. [Reading list](./reading_list.md) — pick two names to cite (e.g., Shopify's judge correlation 0.66 → 0.75, Sierra's pass^k)
