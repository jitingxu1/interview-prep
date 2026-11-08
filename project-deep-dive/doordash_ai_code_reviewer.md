# DoorDash AI code reviewer (study notes)

[← Project deep dives](README.md)

How DoorDash built an AI code review agent engineers actually act on: a lead scout that notices, deep reviewers that verify, and a "disprove-it" pass before anything is posted. Study material for agent system design questions (multi-agent decomposition, precision vs. recall, verification), not a project of yours.

**Original post:** [How DoorDash built an AI code reviewer engineers actually listen to](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/) — DoorDash Engineering blog.

> **Source caveat.** The original post was blocked when these notes were written (the site's bot check plus archive.org rate limits). The content comes from two secondary summaries that quote the original: the [ZenML LLMOps Database](https://www.zenml.io/llmops-database/building-a-production-ai-code-review-agent-with-high-engineer-acceptance) and [daily.dev](https://daily.dev/posts/how-doordash-built-an-ai-code-reviewer-engineers-actually-listen-to-psc8auyls). Numbers are quoted from those summaries; check the original before citing details in an interview. **[confirm]**

---

## Summary (one page)

**Core idea:** separate **noticing** from **verifying**. A lead scout flags suspicious areas without checking them; two deep reviewers dig into only those leads; every finding must survive an attempt to disprove it before it's posted.

**Key numbers:**

| Metric | Value |
| --- | --- |
| Acceptance rate, high and critical findings | **60.2%** across 10,000+ weekly PR reviews |
| Webhook acceptance (real, non-cherry-picked PRs) | 59.0% |
| Previous third-party agent | 46% |
| Latency | ~**7 minutes** after the PR opens, usually before the first human reviewer |
| Cost | ~**$3** per review |
| Scale | 56 repositories |

**Success metric:** not "how many issues found," but **do engineers change their code when the agent comments**, and **do teams keep it enabled voluntarily instead of muting it**.

---

## 1. The architecture: lead scout + deep reviewers

```
 PR opened
   │
   ▼
┌──────────────────────────────┐
│ Lead Scout (1)               │  only "noticing what feels suspicious"
│ no verification, just marks  │  e.g. dangerous deletions, unhandled
│ areas worth a closer look    │       enum cases, silently swallowed errors
└──────────────┬───────────────┘
               │ curated leads
       ┌───────┴───────┐
       ▼               ▼
┌─────────────┐ ┌─────────────┐
│Deep Reviewer│ │Deep Reviewer│  in parallel, dig into the leads
│     A       │ │     B       │  full monorepo access to trace dependencies
└──────┬──────┘ └──────┬──────┘
       └───────┬───────┘
               ▼
┌──────────────────────────────┐
│ "Disprove-it" verification   │  try to falsify each finding first
│ only survivors get posted    │  anything that can't hold up is dropped
└──────────────┬───────────────┘
               ▼
   PR comment: anchored to changed files and lines, explains the concrete
   behavior at risk, tells the author where to start
```

**It mirrors how senior engineers review:** they don't exhaustively verify every line. They notice hunches, then dig deeply into the areas that warrant it.

| Role | Optimizes for | Analogy |
| --- | --- | --- |
| **Lead scout** | Recall — find candidate problems cheaply | A senior engineer's first skim |
| **Deep reviewers** | Depth — investigate each lead across the repo | Pulling the thread on a hunch |
| **Disprove-it pass** | Precision — kill false positives before anyone sees them | "Am I sure enough to block someone's PR on this?" |

---

## 2. Why it's built this way: three versions

| Version | Design | Problem |
| --- | --- | --- |
| **V1** | Multiple specialist agents (security, testing, performance), each with a narrow checklist | Caught mechanical bugs but **consistently missed architectural issues**: no specialist could see how a change affected its dependencies |
| **V2** | Two parallel general-purpose reviewers, each with full change context | Better at architecture, but **each reviewer had too much responsibility**; attention spread thin and critical issues got lost |
| **V3 (current)** | Added the lead scout layer | **Noticing and verifying are separate**: depth goes to the concerns that matter, without wasting attention on routine changes |

**The lesson:** V1 had focus without context; V2 had context without focus. V3 gets both by letting one agent decide *where to look* and others decide *what's true*.

---

## 3. Domain-specific review profiles

AGENTS.md and CLAUDE.md are written for engineers **authoring** code, not **reviewing** it. So DoorDash built a separate layer: per-domain review profiles holding only what a reviewer needs to know.

**Mined from four sources:**

| Source | What it contributes |
| --- | --- |
| AGENTS.md files | Invariants (setup instructions filtered out) |
| Historical PR reviews | Things senior engineers flagged repeatedly |
| Slack decisions | Design decisions, incident discussions |
| Incident history | Patterns that caused production outages |

**Two filters on every candidate rule:**
- If **CI would already catch it** → dropped.
- If **the LLM would know it from general training data** → dropped.

**Dynamic routing:** profiles load based on which code the PR touches. A fraud-detection PR gets different rules than a pricing change.

---

## 4. Lessons

1. **Precision over recall.** They deliberately gave up comprehensive coverage. Noisy reviews get muted, and a muted reviewer catches nothing.
2. **The cheapest model is not always the cheapest review.** Weaker models produced invalid output that needed retries; stronger models succeeded on the first attempt, so total cost was lower.
3. **Guard against stuck agents.** Soft timeouts interrupt an agent that's stuck; hard timeouts act as a kill switch against expensive infinite loops.
4. **Give it the whole repo.** Full monorepo clones let reviewers trace dependencies and find sibling implementations. Most bugs "don't live in the diff itself — they live in how the diff interacts with its dependencies."
5. **Timing matters.** Posting ~7 minutes after the PR opens means the author sees the comment while the change is still fresh, usually before human review.

---

## 5. Connections to other notes

- **Generator–verifier gap** ([chatbot_offline_simulator.md](chatbot_offline_simulator.md)): the scout generates candidates; reviewers and the disprove-it pass verify. Verification is easier than generation, so it gets its own dedicated step.
- **Super-agent Router / Worker:** the scout is like the Router (light, decides where to send attention); deep reviewers are like Workers (focused tasks, deep execution).
- **Context overload** ([doordash_assistant_memory.md](doordash_assistant_memory.md)): V2's failure is the same lesson as Ask DoorDash memory — too much in one agent's context and it drops what matters.
- **Binary, narrow judgments:** the disprove-it pass asks one question per finding ("can this be falsified?"), like the support simulator's one-judge-per-rubric design.

---

## Likely interview questions

| Question | Answer |
| --- | --- |
| "Why not one big reviewer agent?" | V2 tried that: with full context and full responsibility, attention spread thin and critical issues got lost. Splitting noticing from verifying gives depth where it matters. |
| "Why not specialist agents?" | V1 tried that: specialists catch mechanical bugs but miss architectural issues, because none of them sees how the change affects dependencies. |
| "How do you keep false positives down?" | A disprove-it pass that tries to falsify each finding, comments anchored to specific lines with concrete risk, and a deliberate precision-over-recall stance. |
| "How do you measure success?" | Acceptance rate — whether engineers change code in response — and whether teams keep it enabled voluntarily. Not the number of findings. |
| "How do you give it team-specific knowledge?" | Review profiles mined from AGENTS.md invariants, past PR reviews, Slack decisions and incidents, filtered to drop anything CI catches or the model already knows, loaded by which code the PR touches. |
| "How do you control cost?" | Measure cost per successful review, not per token: stronger models avoid retries. Timeouts stop runaway loops. ~$3 per review. |

## How to say it (about 45 seconds)

> "DoorDash's reviewer separates noticing from verifying. A lead scout skims the PR and flags suspicious areas without checking them — dangerous deletions, unhandled enum cases, swallowed errors. Two deep reviewers then dig into only those leads with full monorepo access, and every finding goes through a disprove-it pass before it's posted. They got there after specialists missed architectural issues and general reviewers spread their attention too thin. It hits 60% acceptance on high-severity findings across 10,000-plus PRs a week, about seven minutes after the PR opens, for around three dollars a review. The metric that matters is whether engineers act on the comments and keep it turned on."
