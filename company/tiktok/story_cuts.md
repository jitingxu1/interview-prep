# Story Cuts — Mapped to ByteStyle

ByteDance scores behavioral answers against its six ByteStyle values. This maps your existing stories to each value, with the angle to lead with. Full stories live in [`../../star_stories/`](../../star_stories/); first-person spoken versions of S2, S8 and S10 are in [`../linkedin/story_cuts.md`](../linkedin/story_cuts.md).

Rules for every cut:
- **First sentence is the conclusion.** "I cut a six-month plan to a one-month pilot and we grew it to $20M." Then the story.
- **Under 2 minutes.** The follow-ups are where you're scored.
- **"I decided", not "we decided".**
- **Every number defensible.** `[bracketed]` = fill in before the loop. Expect "how did you measure that?" on every one.

---

## Value → story map

| ByteStyle value | Primary story | Backup | Lead with |
|---|---|---|---|
| **Always Day 1** | S11 Restaurant lending pilot | Chargeback automation (6–8 wks → 2–3 wks) | Took "one month" seriously instead of defending the six-month plan |
| **Be Candid and Clear** | S8 Right person, wrong seat | S5 Learning & growth | Told a senior engineer the feedback was real, directly, with a plan |
| **Seek Truth and Be Pragmatic** | S2 High-stakes tradeoff | S10 (rebuilding their sim) | Put fraud dollars and blocked users on the same axis; argued about a number, not a principle |
| **Be Courageous, Aim for the Highest** | Foundation-over-firefighting ([13](../../leadership/stripe_strategy_and_execution/13_foundation_story.md)) | S11 | Said no to N one-off models during planning; bet on the shared layer |
| **Champion Diversity & Inclusion** | S6 Conflict resolution | Voltron Data distributed OSS team | Diagnosed that one engineer felt unheard and the other felt dismissed — fixed the process, not just the argument |
| **Grow Together** | S1 Management transition | S7 Engineer leveling, S4 Hiring | Zero attrition through a leaderless transition; built the team from there to 12 |

---

## Cuts for the likely questions

### "Tell me about shipping fast under ambiguity" → S11 (Always Day 1)

> "Leadership asked us to cut a six-month lending plan to a one-month pilot, and I think they were right. My first instinct was that one month was unrealistic. But the six-month plan was built to scale before we'd proven the one thing that mattered: could we pick restaurants that needed the money and would pay it back. So I rebuilt scope around that single question, cut everything that didn't serve it, and built the underwriting model myself in a week because it was the critical path. We launched in a month, and it grew to $20M. [Repayment / loss rate: X.] What I took from it: a plan that's built to scale before the core bet is proven is a plan to be slow."

**Expect:** "What did you cut?" "What broke because you went fast?" "How did you decide you personally should build the model?"

### "Tell me about telling someone something hard" → S8 (Be Candid and Clear)

Use the spoken version in [`../linkedin/story_cuts.md`](../linkedin/story_cuts.md) (Cut 2). Bonus for TikTok: the outcome is **agent execution infrastructure that became a core platform capability** — the exact thing this role builds. Say that plainly.

### "Convince leadership with data" → S2 (Seek Truth and Be Pragmatic)

Use Cut 4 in [`../linkedin/story_cuts.md`](../linkedin/story_cuts.md). Lead with: "We landed at [40%] of fraud caught with under [2%] false positives by turning a yes/no ship decision into a threshold everyone could see."

### "Disagreeing with leadership / taking a risk" → Foundation story (Aim for the Highest)

> "During planning, several product teams each asked my team for their own model. Every request was reasonable. Together they meant a year as a model factory and N systems nobody could maintain. I pushed back on accepting all of it and proposed building the shared foundation first, then delivering their use cases on top. [How you sold it; what you promised the teams who waited.] [Outcome: build time per model went from X to Y; N models share the layer.] It looked slower for a quarter and was much faster after."

**Fill the brackets in [`13_foundation_story.md`](../../leadership/stripe_strategy_and_execution/13_foundation_story.md) first** — this is also your best platform-strategy story for the Head of PGC round.

### "Cross-team collaboration / a partner said no" → S10

Use Cut 3 in [`../linkedin/story_cuts.md`](../linkedin/story_cuts.md). This is your lead for the Head of short video round.

### "Working with a team in another timezone"

You don't have a dedicated story yet. Options:
- Voltron Data: distributed, async-first open-source team (Ibis / Ibis-ML) with global contributors. [Fill: a specific decision or delivery you drove across timezones.]
- Any DoorDash work with offshore ops or vendor teams. [Fill if real.]

Don't invent one. If neither fits, answer with the approach in [`interview_strategy.md`](./interview_strategy.md#cross-timezone--hq-alignment) and say plainly you'd be building that muscle at a new scale.

### "Tell me about a failure" → S5

> "Early as a manager, I gave an engineer performance feedback that blindsided him — because I'd never set the expectation in the first place. That was on me. I went back, told him that directly, and rebuilt the plan with him. Then I changed how I run the team: mid-cycle feedback for everyone, and a simple template — what I saw, why it matters, what good looks like, how I'll help. He stayed, and his performance recovered."

---

## Gaps to close before the loop

1. **Agentic chatbot deep dive** — doesn't exist yet; round 1 will be built on it. See [`interview_strategy.md`](./interview_strategy.md#round-1--hm-deep-dive-agentic-architecture).
2. **Brackets** in S10, S2, S11 and the foundation story.
3. **A real cross-timezone example.**
4. **Scale story** — anything where you influenced or coordinated beyond your 12 (an org-wide initiative, a platform other teams adopted). The Head of PGC will probe whether you can run 30.
