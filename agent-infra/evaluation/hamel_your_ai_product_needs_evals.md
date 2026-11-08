# Hamel Husain — *Your AI Product Needs Evals* (study notes)

Notes on [*Your AI Product Needs Evals*](https://hamel.dev/blog/posts/evals/) (March 29, 2024), the post behind the "three levels of evals" framing. Part of the [evaluation section](./README.md). The Level 1 tests applied to the DoorDash support bot have their own doc: [level1_unit_tests.md](./level1_unit_tests.md).

---

**Core claim:** "Unsuccessful products almost always share a common root cause: a failure to create robust evaluation systems." Teams spend their time changing prompts and skip measuring, so they get stuck at the demo stage.

**The virtuous cycle:** (1) evaluate quality → (2) debug issues → (3) change behavior → back to 1. "If you streamline your evaluation process, all other activities become easy."

**Case study — Lucy at Rechat** (real-estate SaaS assistant): prompt engineering stalled with whack-a-mole fixes, no visibility beyond vibes, and a bloated prompt. The fix was putting eval and curation at the center.

**Three levels:**

| Level | What | Cost | Run when |
| --- | --- | --- | --- |
| **1. Unit tests (assertions)** | Code checks on outputs, scoped by feature × scenario, LLM-generated inputs, tracked in CI | Very cheap | Every change |
| **2. Human & model eval** | Log traces, read them in a friction-free custom viewer, label pass/fail, align an LLM judge to a human expert (50 at a time; **precision and recall, not raw agreement**) | Medium | Regular cadence |
| **3. A/B testing** | Real users, real outcomes | Expensive | Mature product |

**Key lines:**
- "One signal you are writing good tests and assertions is when the model struggles to pass them."
- "You must remove all friction from the process of looking at data."
- "You can never stop looking at data — no free lunch exists."
- "99% of the labor involved with fine-tuning is assembling high-quality data" — eval infrastructure gives you that data and your debugging tools for free.

**How his thinking evolved:** later work puts **error analysis first** (open coding → axial coding → failure taxonomy) and uses **Critique Shadowing** (one principal domain expert writes pass/fail plus a critique that becomes the judge's few-shot examples). The 2024 post has nothing agent-specific — pair it with Anthropic's agent-evals post and Sierra's τ-bench for trajectories and pass^k ([reading list](./reading_list.md)).

---

## Self-check

1. Why binary labels over a 1–5 scale?
2. Why is raw agreement a bad metric for judge alignment?
3. Your judge agrees with humans 95% of the time; 5% of outputs are bad. What could be wrong?
4. Why does good eval infrastructure make fine-tuning easier?

<details><summary>Answers</summary>

1. Faster, more agreement between people, easier to act on and track.
2. With imbalanced classes, a judge that always says "good" scores high; measure precision and recall on the failure class.
3. It may pass nearly everything — at a 5% failure rate, always-pass gets 95% agreement. Check recall on bad outputs.
4. The same synthetic-data generator, assertions and judge that power evals also generate and filter training data — "99% of the labor involved with fine-tuning is assembling high-quality data."
</details>
