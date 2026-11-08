# Agent Infra — Technical Prep

Agent platform infrastructure: the framework, the harness, the tool ecosystem, and the eval and ops layer that lets many teams ship agents safely. This is the technical depth behind the "agentic AI" line on the resume.

## Which interviews this serves

| Interview | Date | How this folder helps |
|---|---|---|
| [TikTok](../company/tiktok/) — Sr Manager, Agentic AI Platform | HM call 2026-11-02, loop after | Round 1 HM deep dive is scored on exactly three areas: **agentic framework, harness engineering infra, tool ecosystem** |
| [Snorkel](../company/snorkel/) — Sr / Staff SWE, AI Platform | 2026-11-05 | "Building with AI" round; platform framing and eval vocabulary |
| [Cresta](../company/cresta/) — Senior MLE | 2026-11-03, 2026-11-05 | Agentic and platform-infra teams; RAG to agent system design |
| Rillet — Applied AI Engineer | 2026-11-02 | Pair programming on an AI-native product; tool-calling loop and eval basics |

## Contents

0. **[Landscape (Nov 2026)](./00_landscape_2026.md)** — what companies are building to run many agents: the converged stack, vendor platforms, Cloudflare / Starburst / PhonePe case studies, open problems
1. **[Reference architecture](./01_reference_architecture.md)** — the layers of an agent platform and what each one owns
2. **[Harness and runtime](./02_harness_and_runtime.md)** — the agent loop, context management, durable execution, sandboxing
3. **[Tool ecosystem](./03_tool_ecosystem.md)** — registry, MCP, schemas, versioning, auth, governance when many teams contribute
4. **[Evaluation](./evaluation/)** (section) — all eval material in one folder:
   - [Evals and observability](./evaluation/evals_and_observability.md) — the framework: offline evals, trajectory grading, online monitoring, cost; how DoorDash does it
   - [Level 1 unit tests](./evaluation/level1_unit_tests.md) — code-assertion tests for the support bot, gates, production use, order of work, worked example with who does what
   - [Eval-driven development (blog)](./evaluation/eval_driven_development.md) — the workflow from policy doc to PR: human checkpoints, dev/holdout split, locked tests, trace reading, tiered gates, and the skill design
   - [Hamel — *Your AI Product Needs Evals*](./evaluation/hamel_your_ai_product_needs_evals.md) — study notes on the three-level framing
   - [Reading list](./evaluation/reading_list.md) — how big companies and well-known practitioners evaluate agents
5. **[System design walkthrough](./05_design_walkthrough.md)** — "Design an agent platform for internal teams," paced for 45 minutes
6. **[Drill-down questions](./06_drill_down_questions.md)** — 连环追问 practice: likely follow-ups with short answers

**Related study notes** (in `project-deep-dive/`):

- **[Chatbot offline simulator](../project-deep-dive/chatbot_offline_simulator.md)** — DoorDash's simulation and evaluation flywheel for support chatbots: LLM customer simulator, binary calibrated judges, release gate
- **[Ask DoorDash agent memory](../project-deep-dive/doordash_assistant_memory.md)** — how agents fetch, use and write consumer memory, with flowcharts and worked examples
- **[DoorDash AI code reviewer](../project-deep-dive/doordash_ai_code_reviewer.md)** — lead scout notices, deep reviewers verify, disprove-it pass before posting

## Your anchors

Tie every abstract point back to something you built. What the repo already records:

- **DoorDash support chatbot** — production agentic system for customer support automation ([Cresta notes](../company/cresta/README.md))
- **Real-time RAG** for live support cases, plus a smaller **batch RAG** feeding an **offline labeling agent**
- **Agent execution infra** built by the S8 engineer that became a core platform capability ([S8](../star_stories/story_8_right_person_wrong_seat.md))
- **AI-native team workflow** — team code is almost entirely AI-generated; you own design, review, milestones
- **Platform instinct** — Ibis / Ibis-ML ("write once, run on 20+ engines") and the foundation-over-firefighting story ([13](../leadership/stripe_strategy_and_execution/13_foundation_story.md))

Still missing, and round 1 at TikTok will go here first:

- [ ] **Chatbot deep dive** in [`project-deep-dive/`](../project-deep-dive/): architecture diagram, how routing and tool calls work, eval setup, guardrails, rollout. Use the reference architecture in this folder as the checklist.
- [ ] **Numbers** — `[containment / automation rate]`, `[CSAT delta]`, `[p50 / p95 latency]`, `[cost per conversation]`, `[eval set size]`, `[# tools]`. Every one needs a baseline and a source.
- [ ] **One failure** — a production incident or a bad design call in the agent stack, and what changed afterward.

## How to use

- Read 01 first; it's the map. 02–04 are depth for follow-ups.
- Rehearse 05 out loud against a timer. Draw the diagram from memory.
- Use 06 as flashcards. If an answer runs past 60 seconds, cut it.
