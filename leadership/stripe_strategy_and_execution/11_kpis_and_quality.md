# Q11. How do you determine KPIs and assess the quality of your team's work?

[← Round 2 index](README.md)

This is the metric-reasoning question, and Stripe pushes on it harder than most. The highest-scoring move is showing you know how metrics **fail**.

**The script:**

> I start from the outcome someone outside the team cares about, then work back to what we can actually move. For an ML or platform team the honest version is usually two layers: the business metric we're trying to influence, and the metric we actually control. Keeping both visible matters, because optimizing the controllable one while the real one stays flat is the classic failure.
>
> For each metric I ask three questions: can we move it, will we see it move within a cycle we can learn from, and what would someone do to game it? If a metric has an obvious gaming path, I pair it with a guardrail — so model precision travels with a latency and cost ceiling, and throughput travels with a quality measure.
>
> Quality is partly not a dashboard, though. The things I watch that aren't metrics: how often we break something and how fast we notice, how much rework we do, whether estimates are getting more accurate, and whether partner teams come to us early or only when they're stuck. That last one tells me more about how the team is perceived than any survey.

**Have ready: a metric you got wrong.** Something you optimized that turned out to be the wrong target, or a proxy that decoupled from the real outcome. This is the single most useful thing you can bring to this question — it demonstrates metric judgment rather than metric vocabulary.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Two layers | Separates the business metric from the one the team controls | Only output metrics (tickets, launches) |
| Gaming awareness | Pairs each metric with a guardrail | Single metric, no counterweight |
| Learning cycle | Picks metrics that move within a cycle you can learn from | Metrics that only move yearly, or never |
| Beyond dashboards | Watches rework, incident rate, estimate accuracy, how early partners come | Quality equals the dashboard |
| Metric humility | A metric they got wrong and what changed | Every metric worked as intended |

**Follow-ups to prepare:**

- "What's a metric you stopped tracking, and why?"
- "How do you measure quality for work where the payoff is a year out?" (Infrastructure and platform work — answer with leading indicators: adoption, time-to-build for the next use case, how many teams stopped building their own. Full answer in "Measuring work whose payoff is a year out" below.)
- "How do you assess an individual's quality versus the team's output?" (Full answer in "Assessing individuals versus the team" below.)
- "What if your metric is moving but your stakeholders are unhappy?"

## Measuring work whose payoff is a year out

The real problem for platform and infra teams: the payoff — lower fraud losses, faster launches across the company — may not show up for a year. So how do you know before then whether the work is good, and how do you keep leadership funding it? **Define the eventual payoff up front, track a chain of earlier signals that predict it, and set checkpoints where you'd change course if those signals don't show up.**

**1. Name the payoff a year out.** Be explicit even though you can't measure it yet: *"A year from now, any team can ship a new risk model in 2 weeks instead of 8."* Without this, the early signals have nothing to predict, and platform work becomes building for its own sake.

**2. Build a chain of leading indicators.** Platform value shows up in stages; each predicts the next, and the earliest are visible within weeks:

| Stage | When it shows up | What to measure | What it tells you |
| --- | --- | --- | --- |
| 1. Delivery | Weeks | Milestones hit, first version shipped | We're building what we said |
| 2. First real use | 1–3 months | First team runs a real production model on it | It works for a real use case |
| 3. Adoption | 3–6 months | Active weekly usage (not sign-ups); teams that **stopped building their own** | People choose it over the alternative |
| 4. Efficiency | 6–9 months | Time-to-build for the *next* use case; engineer-hours saved; duplicate pipelines retired | It's making others faster |
| 5. Business outcome | 9–12+ months | Fraud losses, launch speed, cost | The original payoff |

*Teams that stopped building their own* is the strongest single signal — building your own is always the fallback, so abandoning it for yours is a vote with their own time. *Time-to-build for the next use case* is the clearest efficiency signal: the first model on a new platform is always slow, but if the second takes half the time and the third half again, it's paying off.

**3. Measure quality, not just usage.** Adoption can mislead if teams are pushed onto the platform, so pair it with guardrails (the same idea as above):

- *Reliability* — uptime, incidents, how often the platform causes a production issue for a user team
- *Developer experience* — time from "I want to use this" to "running in production," support tickets per team, a short quarterly survey of user teams
- *Retention* — do adopting teams stay, or quietly drift back to their own tools?

**4. Set checkpoints with decision rules.** Before starting, write down what you expect by when, and what you'll do if you don't see it: *"By end of Q1, one team runs a production model on it. By end of Q2, three teams, and the second model takes less than half the time of the first. If we're not at two teams by mid-Q2, I stop and find out why before building more."* This gives leadership the confidence to fund delayed-payoff work, and protects you from sunk cost — you find out at month four, not month twelve.

**5. Shrink the delay.** Build the platform underneath one real use case, so a real team gets value in the first quarter — the sequencing detail from Q13. A platform with a happy first customer at month three is far easier to defend than one that's "almost ready."

**Weak metrics to avoid:**

| Weak metric | Why it misleads |
| --- | --- |
| Features shipped | Your output, not anyone's benefit |
| Teams "onboarded" | One test call counts as onboarded |
| Lines of code or pipelines built | Activity, not value |
| "Positive feedback" | Anecdotes, not evidence |

**The spoken answer:**

> For platform work, I write down the payoff a year out first — for us, it was "any team ships a risk model in two weeks instead of eight." Then I track a chain of earlier signals that predict it. First, does a real team run a real production model on it? Then adoption — measured as active usage, and especially how many teams stopped building their own, because that's teams voting with their own time. Then efficiency: does the second model take half as long as the first, and the third half again?
>
> I pair adoption with quality — reliability, and how long it takes a new team to get to production — so I'm not fooled by teams being pushed onto it. And I set checkpoints up front: if we don't have two teams by mid-Q2, I stop and find out why before building more. That's what lets leadership fund something with a delayed payoff — they can see it working at every step, not just at the end.

**How they grade the delayed-payoff answer:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Clear end state | Names the payoff a year out, concretely | "It'll help a lot of teams" |
| Leading indicators | A chain of signals, each predicting the next | Waits a year to judge |
| Revealed preference | Tracks teams that dropped their own tools | Counts sign-ups or onboarding |
| Quality guardrails | Reliability and developer experience alongside adoption | Usage only |
| Checkpoints | Predefined milestones with a "stop and rethink" rule | Keeps building regardless |
| Early value | Ships under a real first use case | Big-bang platform delivered at the end |

This plugs straight into the foundation story (Q13): with real numbers attached — how many teams adopted, how much faster the second and third models were — that story becomes your answer to this follow-up too.

## Assessing individuals versus the team

The question: when the team delivers (or misses), how do you tell what each person actually contributed, and judge each one fairly? It's harder than it sounds — team output is shared, individual metrics like commits or tickets get gamed, some of the most valuable work (mentoring, reviews, unblocking, on-call fixes) never shows up as output, and the person who presents the demo isn't always the one who made it work.

The short answer: **measure the team by outcomes; measure individuals by impact and behavior against their level, from several sources of evidence.**

| | Team output | Individual quality |
| --- | --- | --- |
| The question | Did we deliver what we committed to? | How well did this person perform for their level? |
| What you measure | Goals and KPIs (Q9, Q11) — latency, adoption, fraud caught | Impact, scope, quality of work, how they make others better |
| Evidence | Dashboards, goal reviews | Your observations, work artifacts, peer and partner feedback |
| Time frame | Quarter or half | Continuous, summarized at review time |

Keep them separate: a strong engineer on a team that missed is still strong, and a weak one on a team that hit everything may have been carried.

**1. Start from the level expectations.** Judge against what the level requires, not against each other or raw output:

| Dimension | What you're asking | Example at senior level |
| --- | --- | --- |
| Impact | What changed because of their work? | Led the serving-layer redesign that cut latency 60% |
| Scope and ambiguity | How big and fuzzy a problem can they own? | Turned a vague ask into a plan |
| Technical quality | Well designed, reliable, maintainable? | Low incident rate; others build easily on their code |
| Multiplier effect | Do they make others better? | Design reviews, mentoring, unblocking teammates |
| Collaboration | How do they work with other teams? | Partner teams ask for them by name |

**2. Gather evidence from several sources.** Work artifacts (design docs, code reviews given and received, incident write-ups — these show thinking, not just output); your own observations of how they handle a hard problem, a disagreement, a deadline; peer feedback, since teammates often know who really did the hard part; partner-team feedback; and running notes through the half, so the review doesn't rest on the last three weeks.

**3. Ask "what was their part?" for each team outcome.** Who made the key design decision, who unblocked the critical path, who did the unglamorous work that made the launch possible — and what would have happened without them. It's the same "I vs. we" question Stripe asks you.

**4. Make invisible work visible.** Actively credit reviews and mentoring, on-call improvements and runbooks, cross-team coordination, interviewing and onboarding. If you only reward visible launches, people stop doing the work that keeps the team healthy — the same glue-work signal you test for in candidates in Round 1.

**5. Calibrate.** Compare with other managers so your bar matches theirs, and watch your own biases: favoring people like you, people who are loud in meetings, or whoever had the most visible project.

**The tricky cases:**

| Situation | How to handle it |
| --- | --- |
| Strong individual, team missed | Rate their own contribution — was their part strong, did they flag risks early? The miss may be the plan, which is on you. |
| Weak individual, team hit its goals | Look at who carried their part. Team success doesn't mean everyone met their level. |
| High output, low quality | Ships fast but creates incidents or rework — part of their output is a cost to the team. |
| Low output, high multiplier | A senior spending half their time unblocking others — lower personal output, higher team output because of them. |
| Visible vs. real contributor | Peer feedback and work artifacts usually reveal who did the hard part. |

**The spoken answer:**

> I keep the two separate. Team output I measure with our goals and KPIs — did we deliver what we committed to. Individual quality I measure against what their level requires: the impact they had, how much ambiguity they could own, the quality of their work, and how much they made others better.
>
> For the individual side I use several sources — design docs and code reviews, my own notes through the half, and feedback from peers and partner teams — because peers usually know who really did the hard part. For each big team result I ask: what was this person's part, and what would have happened without them?
>
> And I deliberately look for invisible work — mentoring, reviews, on-call fixes, cross-team coordination — because if I only reward visible launches, people stop doing the work that keeps the team healthy. A senior engineer who spends half their time unblocking others may have less output of their own, but the team's output is higher because of them.

**How they grade the individual-vs-team answer:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Separation | Distinguishes team outcomes from individual performance | Rates people by whether the team hit its goals |
| Level-based | Judges against level expectations | Ranks people by raw output |
| Multiple sources | Artifacts, notes, peer and partner feedback | Only the manager's impression |
| No vanity metrics | Avoids commits and tickets as performance measures | "I look at how many tickets they close" |
| Glue work | Actively credits invisible contributions | Only rewards visible launches |
| Bias awareness | Running notes, calibration, checks own biases | Relies on memory and gut |

**The example to have ready:** someone whose real contribution was larger or smaller than it looked, and how you found out — for instance, an engineer whose mentoring and reviews were why a launch succeeded, whom you made sure got credit in their review or promotion case. That also fills the "glue work you recognized and rewarded" slot in the Round 1 story bank.
