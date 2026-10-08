# Q1. What are the most important engineering manager skills?

[← Round 1 index](README.md)

My answer leads with **judgment**, then **emotional stability**. That pairing is distinctive — most candidates say communication and hiring — and both are defensible under pressure.

**The script:**

> The one I'd put first is judgment, and it's the one that compounds. Most of my job is deciding under incomplete information: what we work on and what we kill, who works on what, when to go deep into the details myself versus trust a senior engineer, when to escalate versus absorb it. Every other skill routes through it — communication without judgment is just well-delivered bad decisions.
>
> The second is emotional stability, because judgment only works if I can still use it under pressure. A manager is the shock absorber of the team. Pressure arrives from both directions — incidents and bugs from below, shifting priorities and deadlines from above — and the team reads me before it reads the situation. If I'm anxious, they're anxious, and anxious teams make worse decisions. Staying steady is what lets me run the hard conversations — a performance problem, a conflict, a deadline I have to push back on — without becoming reactive, and it's what makes it safe for people to tell me bad news early, when it's still cheap to fix. The two go together: emotional stability without judgment is just calmly doing the wrong thing.

**Why judgment is the honest number one.** It covers: what to build and what to kill; who works on what (matching people to problems is where output multiplies or collapses); when to intervene versus delegate; when to escalate versus shield the team; and every hiring call, each of which is a bet with incomplete data.

Both of your interview rounds are judgment tests in different clothes — People & Leadership asks how good your bets about people are, Strategy & Execution asks how good your bets about work are. That is why the "why not the other approach?" follow-up never stops: they are testing the machinery that produced the decision, not your memory of the event.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Prioritization | Picks one or two and ranks them | Lists six skills with equal weight |
| Specificity | Ties each skill to a moment it mattered | Abstract definitions ("communication is key") |
| Mechanism | Says how the skill shows up in a normal week — 1:1s, escalations, incidents | Virtue words with no behavior attached |
| Self-awareness | Names which one they are still working on | Implies they have mastered all of them |

**The follow-ups that are coming:**

- "Tell me about a judgment call you made with incomplete information." Have one decision where you named the alternatives, picked one, and can say what you'd do differently — your [foundation story](../stripe_strategy_and_execution/13_foundation_story.md) fits.
- "Tell me about a time your emotional stability actually changed an outcome." Have one incident or crisis story where your composure was the variable — see the [story bank](story_bank.md).

## How to answer proof questions

Both follow-ups above are **proof questions**: you just claimed a skill, and now they're checking whether it's real. The same principles apply to any "tell me about a time you showed X."

**The core principle: the skill has to be the reason the outcome changed.** Test: if you hadn't used that skill, would things have turned out differently?

- ❌ "We had a big incident, I stayed calm, and we fixed it." The team would likely have fixed it anyway.
- ✅ "Three people were proposing fixes at once and on-call was about to roll back the wrong service. I stopped the thread, gave one person diagnosis and one communication, and we found the cause in 20 minutes instead of making it worse."

**Seven principles:**

1. **A real moment with real stakes** — money, customers, deadlines, or trust on the line.
2. **Show your thinking, not just your actions** — what you knew, what you didn't, the options, why you chose one.
3. **"I" for your decisions,** "we" for the team's execution.
4. **Name the alternative you rejected** — "I could have X, but I chose Y because…"
5. **Be specific** — the exact moment, what you said, the numbers.
6. **Include the cost or imperfection** — a perfect story sounds rehearsed.
7. **End with reflection** — what you'd do differently, or what you changed afterward.

Keep it to about two minutes, and leave openings for them to dig into.

**One-line test before using any story:** *does this prove the skill, or just mention it?* If you could remove the skill and the outcome stays the same, pick another story.

### Judgment with incomplete information

The key words are **incomplete information** — they want to see how you decide without waiting for certainty.

1. **The decision and the stakes** — what had to be decided, by when.
2. **What you knew, and what you didn't** — name the missing information explicitly.
3. **The options** — at least two real ones.
4. **How you limited the risk of being wrong** — the strongest part: a reversible option, a phased rollout, a kill switch, or evidence you defined in advance that would change your mind.
5. **The call, and why** — the tradeoff you optimized for.
6. **The outcome, with numbers.**
7. **Reflection.**

The point that impresses most is separating **reversible from irreversible** decisions: "Because a phased rollout was easy to reverse, I didn't need certainty — I needed a way to learn fast and pull back if I was wrong."

**Your stories for this:** Story 2 (phased fraud model rollout — unknown false-positive impact; ship / don't ship / phase; 40% of fraud caught at under 2% false positives) fits best. The foundation story is the second option — judgment about strategy rather than under uncertainty. The ATO escalation below also works, and the merchant onboarding call below is your most direct example.

### Emotional stability

The trap is saying "I stayed calm." Composure is invisible unless you describe **concrete behaviors**.

1. **The pressure moment** — what was happening, and why it was stressful.
2. **What others were doing** — panic, finger-pointing, rushed fixes. This shows the contrast.
3. **What you felt, honestly** — "I was worried too." Composure is managing stress, not lacking it.
4. **What you did, specifically** — paused before reacting; brought structure (who owns what, what's next); set a communication rhythm; absorbed pressure from above so the team could focus; the exact words you said.
5. **How the outcome changed** — what would have happened otherwise.
6. **Reflection** — what you learned or changed.

## Your story: the ATO escalation

This is a strong story for **both** follow-ups — composure (CEO-level escalation, partners panicking) and judgment with incomplete information (whether to ship the quick model). Use it as the composure story by default.

### What happened (your facts)

- A Dasher's account was taken over (ATO). The Dasher tagged the CEO on Twitter.
- The CEO escalated to the VP, then to your director and you: what happened, and how do we handle this in the future?
- The system gaps were real: no well-designed account-hack blocking, no SMS verification, no working ATO recovery channel.
- S&O and Product panicked.
- You had the option to push a quick ATO model straight to production. You paused instead, worked out what happened in this case and how big the ATO problem was across the platform, shielded your engineers, and delivered a report to your manager: current situation and risk, short-term mitigation, long-term plan.
- Afterward, you advocated for a monitoring dashboard covering every kind of fraud, including ATO, and shared it with leadership.
- You also reset expectations with leaders: fraud is caught by a group of teams working together, and no system catches every single fraud or ATO case.

### Check: are these actions reasonable?

Mostly yes, and the core call is strong. But a few gaps would get probed hard.

**What's strong:**

- **Not deploying the quick model blind was the right call — and you have a better reason than "I wanted to understand first."** Without SMS verification or a recovery channel, a false positive locks a real Dasher out of their income with no way back. A blocking model with unknown precision could have created many more angry Dashers than the one ATO. Say that reason explicitly; it turns "I paused" from hesitation into judgment.
- **Sizing the problem before acting.** Was this one case or a pattern? How many ATOs, what attack vector? That decides whether the answer is a fix or a program.
- **The three-part report** — situation and risk, short-term mitigation, long-term plan — is exactly how a CEO-level escalation should be answered.
- **Shielding the engineers** from the panic so they could do the analysis.

**What to check or add — the interviewer will probe these:**

1. **The affected Dasher.** The first question will be "what happened to the Dasher?" Someone must have restored the account and any lost earnings. Say who did it and how fast. If it wasn't handled well, own that in the reflection.
2. **The pause has to be short and time-boxed.** With a CEO escalation, "I paused" can sound like inaction. Have the number: "I asked for [24/48] hours," and an interim update to your director within [hours] while the full report was being written.
3. **Short-term mitigation can't be "nothing."** If you didn't ship the model, what protected Dashers in the meantime? Strong middle options: run the quick model in **shadow mode** or route its flags to **manual review** instead of auto-blocking; a rule on the highest-risk pattern (e.g. new device + payout-account change); an alert or hold on payout changes after a suspicious login. If you did one of these, it's the strongest part of the story — "I didn't choose between shipping and not shipping; I shipped it in a way that couldn't hurt real Dashers."
4. **Calming S&O and Product is the composure part — make it concrete.** What did you actually do? One shared doc, a short daily sync, clear owners, an update cadence. Panic usually comes from not knowing what's happening, so a clear rhythm is the fix.
5. **Shield, but don't isolate.** Say who did the analysis — e.g. one engineer working with you while the rest stayed on the roadmap. "I shielded them" shouldn't mean you did everything alone.
6. **The long-term plan needs owners outside your team.** SMS verification and account recovery are probably Product or another team's systems. Say who owned what — e.g. you owned the ATO model and detection, Product owned verification and recovery — and whether it got funded.
7. **Numbers.** ATO volume found, time from escalation to report, what was approved, and ATO rate or Dasher impact afterward.
8. **Reflection.** The honest one is probably: "We knew ATO protections were thin before this — I should have flagged the gap proactively, with a risk estimate, instead of it surfacing through a CEO tweet." That's a mature, credible line.

### The follow-up actions: dashboard and expectation-setting

These are the strongest part of the story. They turn a reactive incident into a lasting change, and they're the mechanism that answers the reflection ("I should have raised the gap before a tweet did"). Two things to get right:

**The dashboard — make it about early warning, not reporting.** The point isn't that leadership can see charts; it's that the next ATO spike shows up on your dashboard before it shows up on Twitter. Be ready for:

- **What's on it:** e.g. fraud and ATO rates by type, losses, model catch rate and false positives, time to detect, time to restore an affected account.
- **Who looks at it, and how often:** e.g. a weekly review with S&O, a monthly view for leadership.
- **What it changed:** did it catch anything early afterward? Did leadership use it to fund the long-term plan? One concrete example makes the dashboard real.

**"We can't catch every fraud" — say it as a tradeoff, not a defense.** Said badly, it sounds like an excuse after an escalation. Said well, it's one of the most senior things in the story, because it resets leadership from "zero fraud" to "managed risk." Three things make it land:

1. **Name the tradeoff.** Catching every case means blocking far more real Dashers and customers. The real choice is how much fraud versus how much friction, and leadership should make that choice with data.
2. **Say what you *do* commit to.** Not zero fraud, but: rates within an agreed target, detection within [X hours], and an affected user made whole within [Y hours]. That gives leaders something to hold you to.
3. **Explain "as a group" concretely.** Fraud defense is layers owned by different teams: detection models (your team), verification and recovery flows (Product), policy and targets (S&O), and response (support or ops). No single layer catches everything; together they cover each other's gaps. This also makes clear that fixing ATO wasn't only your team's job — without sounding like you're passing blame.

The line to say:

> We'll never catch every single fraud case — and if we tried, we'd block thousands of real Dashers. What I can commit to is that we'll see a spike before it reaches Twitter, that losses stay within the target we agree with S&O, and that when someone is hit, we make them whole within a day. Fraud defense is a set of layers owned by several teams, and the dashboard is how all of us see the same picture.

### The adjusted story

Fill the brackets with the real facts; drop anything that didn't happen.

> A Dasher had their account taken over and tagged our CEO on Twitter. It came down the chain within hours — CEO to VP to my director to me — with two questions: what happened, and how do we stop it happening again?
>
> The honest situation was bad. We had no strong ATO blocking, no SMS verification, and no working recovery channel. S&O and Product were understandably alarmed, and the fastest-looking option on the table was to push our quick ATO model straight into production.
>
> I paused that — for a specific reason. With no verification and no recovery channel, every false positive would lock a real Dasher out of their income with no way back. Shipping a blocking model with unknown precision could have turned one angry Dasher into [hundreds]. So I asked for [48 hours] to understand the problem before we acted on it.
>
> First, [S&O/support] restored the affected Dasher's account and [earnings]. Then I had [one engineer] work with me on the analysis while the rest of the team stayed on the roadmap — I didn't want the whole team pulled into the panic. We found [N ATO cases in the last X weeks, mostly via Y].
>
> To calm things down, I set up [one shared doc and a daily 15-minute sync with S&O and Product], so everyone knew what we knew and what was next. Within [a day] I sent my director an interim update, and then a short report in three parts: the current situation and risk, short-term mitigation, and the long-term plan.
>
> Short term, we [ran the quick model in shadow mode / routed its flags to manual review / added a hold on payout-account changes after new-device logins], so we were protecting Dashers without blocking anyone automatically. Long term, we proposed [SMS verification and a recovery flow, owned by Product, plus a production ATO model, owned by my team].
>
> [OUTCOME: what leadership approved, what shipped, and ATO numbers afterward.]
>
> The bigger change came after. I pushed for a monitoring dashboard covering every kind of fraud we see — ATO included — with rates, losses, catch rate, false positives, and time to recover an affected account, and we started reviewing it [weekly with S&O and monthly with leadership]. I also reset expectations with our leaders: we'll never catch every single fraud case, and trying would mean blocking huge numbers of real Dashers. What we commit to is seeing spikes early, keeping losses within an agreed target, and making affected users whole fast — and fraud defense is a set of layers across several teams, not one model. [EXAMPLE: something the dashboard caught early, or a decision leadership made with it.]
>
> What I'd do differently: we knew our ATO protections were thin before this happened. I should have raised that gap proactively, with a risk estimate, instead of it surfacing through a tweet to our CEO. The dashboard is what I did about that — the next gap should show up in our review, not on Twitter.

### Skills this story shows

**The two headline skills — for Q1, name these two and rank them.** The ATO story proves both:

| Skill | The moment in the story that proves it |
| --- | --- |
| **1. Judgment** | Not shipping the quick model blind: with no SMS verification or recovery channel, false positives would lock real Dashers out with no way back. You weighed the cost of acting fast against the cost of a wrong block. |
| **2. Emotional stability** | CEO escalation, S&O and Product panicking — you paused, brought structure, and shielded the team instead of reacting to the pressure. |

**Supporting skills.** Use these when a question asks for them specifically — don't list them in your Q1 answer; that's the "six skills with equal weight" red flag.

| Skill | Where it shows up | Questions it answers |
| --- | --- | --- |
| Problem framing / dive deep | Sizing it first — one case or a pattern? How many ATOs? | Q11 (KPIs), "when do you go deep?" |
| Communicating up | The three-part report: situation and risk, short-term fix, long-term plan | Q12, "how do you handle an escalation?" |
| Shielding the team | Engineers kept on the roadmap; one engineer on the analysis | Q14 (churn vs. context), Q6 |
| Cross-functional leadership | Calming S&O and Product; long-term plan split across teams | Q14, Q7 |
| Risk management | A mitigation that couldn't hurt real Dashers (shadow mode or manual review, if true) | Q10a, Story 2's phased-rollout pattern |
| Building mechanisms, not heroics | The fraud dashboard — the next spike shows up in review, not on Twitter | Q9, Q15, the Strategy & Execution round theme |
| Setting expectations with leadership | "We can't catch every fraud; here's what we commit to" | Q11, Q12, Q16 |
| Self-awareness | "I should have raised the gap before a tweet did" | "What would you do differently?" |

**How to use it:**

- **Q1:** say judgment, then emotional stability. When asked for an example, tell the ATO story and stress only those two.
- **Other questions:** same story, different angle — Q14 leads with calming S&O and Product; Q15 leads with the dashboard; "tell me about an escalation" leads with the three-part report.
- **Don't retell it in full.** If you've already told it in a round, say "Going back to the ATO incident…" and jump straight to the part that answers the new question.

### Facts to pin down before you use it

- How fast the affected Dasher was made whole, and by whom
- How long the pause was, and when the first update went up
- The ATO numbers you found (volume, time window, attack pattern)
- What the short-term mitigation actually was
- What the long-term plan was, who owned each part, and whether it got funded
- What changed afterward, with a number
- What the dashboard tracks, who reviews it, how often — and one thing it caught early or one decision it drove
- Whether leadership agreed an explicit fraud target or risk tolerance after the "we can't catch everything" conversation

## Your story: the merchant onboarding model call (judgment with incomplete information)

Your most direct answer to *"Tell me about a judgment call you made with incomplete information."* It also works for Q10 (roadmap — moving a project below the line) and as a judgment archetype in Round 2.

### What happened (your facts)

- During planning, several projects were competing for the same people, and one had to move below the line.
- The choice: build a **merchant (Mx) onboarding fraud model** — protection that didn't exist yet — or **improve the performance of an existing model**.
- The key information was missing: nobody had measured how big the onboarding fraud problem was.
- The list had to be final by the planning deadline, so waiting for data wasn't an option.
- Your call: the onboarding model this quarter; defer the improvement. The onboarding model takes the platform from **0 to 1** on new-merchant protection; the improvement takes an existing protection from good to better.
- You also argued that problem size shouldn't be the only criterion in planning.

### Check: is the call reasonable?

Yes — it's a sound call, and the reasoning is the part interviewers want. Two things will be probed:

1. **"How did you know the improvement wasn't worth more?"** Have the comparison ready: the existing model was already catching [X%] of its fraud, so improving it was worth a few points at the margin; the onboarding gap was unprotected entirely. Even a rough estimate beats "it felt right."
2. **"What if you were wrong?"** This is where the story is strongest — *if* you built in a checkpoint. If you did, lead with it. If you didn't, say so in the reflection.

### Criteria beyond size — completing "we need to consider…"

When the size of a problem can't be measured yet, size can't be the only way to rank it. The criteria you can argue for:

| Criterion | The question it asks | How it applied here |
| --- | --- | --- |
| **Coverage gap (0→1 vs. 1→N)** | Do we have *any* protection today? | Onboarding had none; the other model already worked. Going from nothing to something usually beats going from good to better. |
| **Downside risk** | If we're wrong about the size, how bad could it be? | An unprotected door has no ceiling — fraudsters move to the weakest entry point. Deferring an improvement has a bounded cost: the existing model keeps working. |
| **Cost of delay** | What does waiting a quarter cost? | Deferring the improvement costs a few points of performance for one quarter. Deferring onboarding leaves the door open as merchants keep signing up. |
| **Upstream vs. downstream** | Where in the lifecycle does this act? | Onboarding is the front door — a fraudulent merchant stopped at sign-up never creates fraud downstream. |
| **Value of information** | Will doing it teach us what we don't know? | Building even a simple onboarding model produces labels and a baseline — the very data that was missing. Delaying it keeps us blind. |
| **Reversibility** | How easy is it to change course? | The improvement could come back next quarter with no harm done; the plan could be swapped at a checkpoint. |

The line to say: *"Size is the right first question when you can measure it. When you can't, I ask what the downside is if we're wrong, what waiting costs, and whether doing the work will tell us what we don't know."*

### The story, in the seven-step shape

Fill the brackets with real facts; drop anything that didn't happen.

1. **The decision and the stakes.** In [Q_ planning], [three] projects were competing for [N engineers]. One had to move below the line, and the list was due by [date].
2. **What I knew, and what I didn't.** We knew the existing [model name] was catching [X%] of its fraud and could gain maybe [a few points]. We did *not* know how big merchant onboarding fraud was — no one had measured it, because without a model we had no labels.
3. **The options.** (a) Improve the existing model — measurable, safe, incremental. (b) Build the onboarding model — unmeasured, but the platform had zero protection there. (c) Wait for data — not possible before the deadline.
4. **How I limited the risk of being wrong.** [IF TRUE — the strongest part:] I scoped a thin first version — [rules plus a simple model] — to ship in [N weeks], instrumented so we'd get a measured problem size within [the first month]. I set a checkpoint: if by [week 6] the measured fraud was below [$Y / Z cases], we'd swap back to the model improvement. And I kept the existing model's monitoring in place so deferring its improvement couldn't quietly degrade it.
5. **The call, and why.** I chose the onboarding model: going from no protection to some protection beats going from good to better, the downside of an open door is unbounded while the cost of deferring an improvement is small and bounded, and building it was the only way to find out how big the problem was.
6. **The outcome.** [Measured onboarding fraud: $_ / _ cases in the first month. The model caught _% at _% false positives. The improvement shipped in [next quarter].] Then the process change: I proposed that our planning criteria go beyond size — coverage gap, downside risk, cost of delay, and value of information — and [it was adopted for the next planning cycle].
7. **Reflection.** [Choose the honest one:] "I'd push to get a rough size estimate earlier, even from manual review, so the decision rests on more than reasoning." Or: "The checkpoint was what made the bet safe — I'd set one on every unmeasured bet now."

### The spoken version (about two minutes)

> During planning we had [three] projects competing for the same engineers, and one had to move below the line. The choice came down to building a merchant onboarding fraud model — protection we didn't have at all — or improving an existing model that was already working. The problem was that nobody knew how big onboarding fraud was. We'd never measured it, because without a model we had no labels. And the list was due by [date].
>
> I chose the onboarding model, for three reasons. First, going from no protection to some protection is worth more than going from good to better — the existing model kept protecting us either way. Second, the downside wasn't symmetric: deferring the improvement had a small, bounded cost, but an unprotected front door has no ceiling, because fraudsters move to the weakest entry point. Third, building it was the only way to learn the size of the problem.
>
> To limit the risk of being wrong, I [scoped a thin first version for N weeks, with a checkpoint at week 6: if the measured fraud was below a threshold, we'd swap back]. It turned out [result with numbers].
>
> Afterward I suggested we stop using size as the only planning criterion — when you can't measure size, you also have to weigh downside risk, cost of delay, and what the work teaches you. [It became part of how we plan.]

### Likely follow-ups

- **"How did you know the improvement wasn't worth more?"** — the margin vs. zero-coverage comparison, with whatever rough numbers you had.
- **"Who disagreed, and what did you tell them?"** — whoever owned or wanted the improvement (S&O, Product, or the model's owner). Have the sentence you used and how you kept them on side — e.g. a committed slot next quarter.
- **"What would have made you change your mind?"** — the checkpoint threshold, stated as a number.
- **"Isn't 'unmeasured' just an excuse to do the more interesting project?"** — the discipline answer: a thin first version, a hard checkpoint, and a commitment to swap back if the data said so.
- **"What did you do to measure it afterward?"** — the labels and baseline the first version produced.

### Facts to pin down before you use it

- How many projects, how many engineers, and the planning deadline
- The existing model's name, current performance, and the expected gain from improving it
- Whether you had any rough signal on onboarding fraud size (manual reviews, S&O anecdotes, a pattern)
- Whether there was a thin first version and a checkpoint — and the actual threshold
- The measured result once the model was live
- Who disagreed, and what you told them
- Whether "beyond size" criteria were adopted in later planning
