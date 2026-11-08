# Chatbot offline simulator (DoorDash)

[← Project deep dives](README.md)

The infrastructure that lets the support team build, test and ship LLM agents safely: an offline **simulation and evaluation flywheel**. It is the testing and release layer under [Support automation with AI](support_automation_ai.md) — every agent in those milestones is iterated and gated on it.

**Public write-up:** [A simulation and evaluation flywheel to develop LLM chatbots at scale](https://careersatdoordash.com/blog/doordash-simulation-evaluation-flywheel-to-develop-llm-chatbots-at-scale/) — DoorDash Engineering blog, January 26, 2026. Authors: Lewis Warne (Senior Data Scientist, Support Automation), Chenran Gong (SWE, Delex AI — led the simulation platform design), Aditi Bamba (SWE, Conversational AI — simulation and eval platform infra), Matt Gode (SWE, Consumer Engineering).

> **How to read this doc.** Everything in the summary comes from the blog post. Your own role, team size and anything marked **[confirm]** are not in the post — fill them in with what's true before using this in an interview.

---

## Project summary (one page)

**The problem: LLMs broke our testing model.**

- Support used to run on hand-built **decision trees**. Testing was easy: change a node, trace the branch, and the impact was predictable.
- LLM agents resolved cases better (more flexible, conversational, human-like decisions), but they are **non-deterministic**. A prompt change can improve one scenario and quietly break another, and you can't trace the branch any more.
- The only two options were bad: **test in production** (customers and Dashers become the test cases) or **test manually** (slow, a bottleneck, and misses problems).
- Goal: **fast feedback loops with no production risk** — multi-turn conversations run offline, at scale, with quality measured automatically.

**What we built: two connected systems.**

| Component | What it does |
| --- | --- |
| **1. Scenario generation pipeline** | LLMs mine historical support transcripts into structured, parameterized test scenarios: customer **characteristics** ("frustrated, demanding, direct" vs. "confused, polite, patient"), customer **story**, and customer **intent** (e.g. "wants a full refund"). Stored in S3, indexed by test ID. |
| **2. Customer simulator** | An LLM that plays the customer, not a script. Each turn it analyzes the bot's reply (was the issue addressed? progress? more info needed? is it looping?) and writes the next message in character — pushback, clarifying questions, and escalation only after repeated unhelpful or circular answers. Runs on the internal **load-testing infrastructure** for high QPS. |
| **3. Simulation mocking** | Mocks gRPC API responses and MCP tool resources, so the bot's tool calls (delivery status, refund decisions, order details) return controlled results. **Hybrid mocking** blends live test delivery data with historical scenario details (items, addresses, issue traits), shifting timestamps to keep the original timing. Arrange–act–assert, like unit tests. |
| **4. Evaluation framework** | **LLM-as-judge** calibrated against expert human labels. Each eval is a function: inputs (full conversation + tool-call trace, plus the policy) → prompt → **binary pass/fail + reasoning**. |

**Why trust an LLM to judge an LLM: the generator–verifier gap.** Acting as a full support agent is a hard, open-ended task. Verifying one narrow behavior ("did the bot communicate all options?", "did it follow policy?") is a simple binary task that LLMs do reliably, and a binary task is easy to calibrate with precision and recall.

**The flywheel (problem → production):**

1. **Find a problem.** Experts manually review cases from early simulations or live traffic, and pick the issue plus real transcripts to seed scenarios.
2. **Write an eval** that captures the failure mode.
3. **Calibrate it against humans.** Label a sample by hand → run the judge → compute precision, recall and F1 → read the reasoning on mismatches → fix the prompt → repeat until above threshold. An internal tool speeds this up.
4. **Iterate.** Baseline the current system (e.g. 50% pass), change the prompt or tool outputs, re-run the simulator, re-check (e.g. 60%), and repeat until the exit criterion — up to 99.9% for high-stakes behavior, lower for less serious ones.
5. **Guardrails, then ship.** Run the full eval suite (hallucination, tone, issue classification). If nothing regresses, ship through the standard **A/B test**, then monitor live traffic with the same evals.

**Case study — the "case state" (context engineering):**

- Human review of early launches showed the bot getting bogged down in the huge amount of raw data in its context, which led to **hallucinations**: misread fields and invented policies.
- Hypothesis: the context is vital for deciding, but it becomes noise when writing the reply to the customer.
- Fix: a new layer called the **case state** that turns raw tool history into a structured intermediate summary for the bot.
- The first versions were wrong both ways: some dropped critical details, others were still too noisy. The simulator made it possible to try **dozens of context shapes and prompt strategies** in hours instead of weeks of manual trial and error.
- **Result: 90% fewer hallucinations in simulation, and the gain carried over to production.** That offline-to-online correlation is the evidence that the simulator can be trusted.

**Impact**

| Dimension | Before | After |
| --- | --- | --- |
| Iteration cycle | Days (deploy to prod, or test dozens of scenarios by hand) | **Hours** — **200+ simulated conversations in under 5 minutes**, with automated eval results |
| Coverage | Edge cases impossible to test safely | Fraud cases, high-value refunds, extreme delays; **50+ evals** in the suite |
| Hallucinations (case study) | Baseline | **−90%** in simulation, held in production |
| Production stability | Customers as test cases | Gains validated offline hold in live traffic, at a much lower cost per change |

---

## How to say it (about 60 seconds)

> When we moved support from decision trees to LLM agents, we lost the ability to test. With a tree, you change a node and trace the branch. With an LLM, a prompt change can fix one scenario and break another, and the only options were testing on customers or testing by hand. So we built an offline flywheel with two parts. A simulator, where an LLM plays the customer using personas and intents mined from real transcripts, with mocked tools so the bot sees realistic order and refund data. And LLM-as-judge evals, each one narrow and binary and calibrated against expert labels until precision and recall clear a bar. A change goes from days to hours: 200-plus conversations in under five minutes, scored automatically, and the full eval suite as a release gate before the A/B test. The biggest win was context engineering: we added a structured "case state" layer and cut hallucinations by 90%, and that held in production, which is how we know the simulator predicts real traffic.

## Likely follow-ups

| Question | Answer |
| --- | --- |
| "Why trust an LLM judge when an LLM made the mistake?" | The generator–verifier gap: generating a full resolution is hard, but checking one narrow binary behavior is easy and measurable. Each judge is calibrated against human labels on precision, recall and F1 before we trust it. |
| "How do you know the simulator is realistic?" | Scenarios come from real transcripts; the simulator keeps the persona and only escalates after repeated unhelpfulness; and the real test is offline-to-online correlation — the 90% hallucination drop held in production. |
| "Why binary evals instead of a 1–10 score?" | Binary is easier to calibrate, easier to agree on between humans, and a pass rate works directly as a north star and exit criterion. |
| "How do you avoid overfitting to the eval set?" | The full suite runs as a regression guardrail on every change, fixes still go through an A/B test, and production monitoring uses the same evals. [confirm: held-out scenarios, eval refresh cadence] |
| "What's still manual?" | Problem discovery and error analysis — experts read traces. The post says we're exploring tools to speed both up. |
| "How does it scale?" | Simulations run on the existing load-testing infra, scenarios are indexed in S3 by test ID, and tools are mocked, so a run doesn't touch production backends. |
| "What does a run cost?" | [confirm: tokens and dollars per 200-conversation run; judge model vs. bot model] |

## Connections to other material

- **Support automation milestones:** this is the "build the eval set first" lesson from [support_automation_ai.md](support_automation_ai.md) turned into a platform — each new agent gets scenarios and calibrated evals before it ships.
- **People story:** [Story 8](../star_stories/story_8_right_person_wrong_seat.md) — the backend engineer moved onto agent infrastructure. [confirm: whether this is the same infrastructure]
- **Super-agent / context engineering:** the case state is the same idea as "start minimal, inline by locality" — raw context becomes noise.

## Fill in before using

- [ ] Your role: did you lead the team, set the direction, or sponsor the platform? Which decisions were yours?
- [ ] Team size and timeline.
- [ ] Which agents and issue types run through the flywheel today.
- [ ] Calibration threshold (target precision and recall) and how many humans label.
- [ ] One concrete failure the simulator caught before it reached customers.
