# Q9. How does your team set its mission and goals, and how do you assess progress?

[← Round 2 index](README.md)

The thing being tested is whether your team's mission is **derived** from something above it or invented locally. A mission that doesn't trace upward is a red flag for an EM. The second thing being tested is whether you can tell **activity** from **progress** — most managers report the first and call it the second.

**The script:**

> I start from the org's goal and work backward: for that goal to happen, what has to be true that only my team can make true? That becomes the mission, and I hold it to one test — someone on another team should be able to read it and know when to come to us and when not to. For my last team it was roughly: "We make it fast and safe for any team to ship risk models. Come to us for features, training, and serving — not for one-off analyses." The second half matters as much as the first, because it's what I point to when I have to say no.
>
> From there, goals for the half: three or four outcomes, not a task list. I write them as changes in the world — a latency number, an adoption number, a capability that didn't exist — not as "ship X." Shipping X is how we might get there, and sometimes partway through we find a better way.
>
> For assessing progress I run three different clocks. Weekly, I look at whether work is moving and where it's stuck — that's leading indicators and blockers, not status theater. Monthly, I look at whether the metrics are actually moving, because activity and progress are different things. At the end of the half, I look at the outcomes honestly, including what we missed and why, and I write that down before the review rather than after.
>
> And every few months I run one gut check: if my team stopped working tomorrow, who would notice, and how fast? If I can name the teams and what breaks — "the fraud teams couldn't ship model updates within a week" — we're working on the right things. If I find myself giving a long, abstract explanation instead, that's the sign we've drifted, and I'd rather catch that myself than have my leadership catch it for me.

**What makes this answer strong:** the distinction between outcomes and output, and the three clocks. Both show mechanism rather than good intentions.

## The vocabulary: vision, mission, goals, roadmap, tasks

Keep these straight before the round. Each layer answers a different question and lasts a different length of time, and everything lower down should trace back to the layer above it. If a project doesn't connect upward, either it shouldn't be done or the layer above is out of date.

| Layer | Question it answers | How long it lasts | Example (ML risk platform team) |
| --- | --- | --- | --- |
| **Vision** | Where are we going? What does the world look like if we succeed? | 3–5+ years; aspirational | "Every product team can stop fraud as fast as fraudsters adapt, without needing ML experts of their own." |
| **Mission** | Why does the team exist? What do we do, and for whom? | Years; rarely changes | "We make it fast and safe for any team to ship risk models. Come to us for features, training, and serving — not one-off analyses." |
| **Goals** | What will be measurably different at the end of this half? | 6 months | "New risk models take 2 weeks to build instead of 8." |
| **Roadmap** | What will we build to get there, in what order? | A quarter to a half; changes often | "Q1: shared feature store. Q2: reusable serving layer." |
| **Tasks** | What is each person doing this week? | Days | "Migrate the fourth pipeline to the feature store." |

**Vision vs. mission.** The vision is the future you're trying to create; the mission is what your team does every day to help get there. Q9 asks about mission and goals, so lead with the mission — mention a vision only as one sentence of context ("The long-term picture was X; the part my team owned was Y"). The common mistake is a team mission that sounds like a vision — "revolutionize fraud prevention with AI" — inspiring, but it tells nobody what your team actually does or when to come to you. For a team, practical beats inspiring.

**What a good mission does:** it tells other teams when to come to you and when not to; it lets you say no without it being personal; and it lets engineers make good calls without asking you. The test: can you say it in one sentence, and would a PM on another team understand it?

| Mission | Verdict |
| --- | --- |
| "Leverage ML to drive business value." | Too vague — describes any team |
| "Build and maintain the feature store." | Too narrow — a project, not a purpose |
| "Make it fast and safe for any team to ship ML models for fraud and risk." | Specific about who and what, durable for years |

**Goals vs. roadmap.** Goals are the result; the roadmap is the current plan for reaching it. Keeping them separate is what lets you change the plan without missing the goal — if halfway through a two-week caching fix gets latency where a three-month rebuild would have, you switch and still hit the goal. A goal written as "ship X" turns that same smart switch into a miss.

## Going deeper: the four pieces, each with a concrete example

Interviewers rarely let the script stand. They pick one sentence and ask "show me." Have a concrete version of each piece ready. The examples below use an ML platform team; swap in your real ones.

**1. Deriving the mission.** Walk the chain out loud, one level at a time:

- *Org goal:* reduce fraud losses without hurting good-customer conversion.
- *What has to be true:* every product team that faces fraud can ship and iterate a model quickly, on shared, trustworthy features.
- *My team's mission:* "We make it fast and safe for any team to ship risk models — come to us for features, training, and serving; don't come to us for one-off analyses."

The "don't come to us for" clause is the part most candidates leave out, and it is the part that makes the mission useful. It is what you point to when you say no (see Q10 and Q10a).

**2. Writing goals as outcomes, not output.** Show the rewrite — this is the most convincing ten seconds of the answer:

| Output (weak) | Outcome (strong) |
| --- | --- |
| Ship the shared feature store | Time to ship a new risk model drops from 8 weeks to 2 |
| Migrate three teams to the new serving layer | p99 scoring latency under 50 ms for 100% of checkout traffic |
| Build a monitoring dashboard | Model drift detected within 24 hours instead of at the monthly review |

Each outcome needs three properties: a **baseline** (where we are now), a **target** (where we're committing to be), and an **owner** (one person, not "the team"). If you cannot state the baseline, the goal isn't ready yet — and saying "the first goal was to establish the baseline" is a perfectly good answer.

Also name the ratio: roughly **one stretch goal and two or three you expect to hit.** If you hit every goal, they were too easy; if you miss most, nobody believes the next set.

**3. The three clocks, as artifacts.** Saying "I review weekly" is a claim. Naming what the review produces is the evidence:

| Clock | What I look at | The artifact | What triggers action |
| --- | --- | --- | --- |
| Weekly | Leading indicators, blockers, dependencies on other teams | A short written status, red/yellow/green per goal, readable without a meeting | Anything yellow two weeks running gets a conversation, not another week |
| Monthly | Whether the outcome metrics are actually moving | Metric review against the baseline and target | Work shipping but metric flat → question the plan, not the team |
| End of half | What we hit, missed, and why | A written retro, drafted *before* the leadership review | Misses become explicit inputs to next half's goals |

The line worth saying: **"I want to find out a goal is in trouble in week four, not week twelve."** The weekly clock exists to make slippage cheap to see.

**4. Connecting it to the engineers.** The test: could any engineer on the team, asked cold, say which goal their current work moves? Make it mechanical — every project in planning maps to a goal, and work that maps to nothing either gets a goal or gets cut. In 1:1s ask "what goal is this for?" occasionally; if they can't answer, that's your failure to communicate, not theirs.

## When a goal is missed

This is the follow-up that almost always comes, so the answer needs its own shape:

1. **Say it early and plainly.** The miss was visible in the weekly status before the review — no surprises.
2. **Separate the causes.** Wrong target (we picked a metric that didn't matter), wrong plan (right target, wrong approach), or wrong execution (right plan, we didn't deliver). Each has a different fix.
3. **Say what you changed.** The goal-setting process, the plan, or the staffing — one concrete change.
4. **Don't relitigate the target.** Lowering the bar after the fact to call it a hit is the move interviewers look for.

**The story to have ready:** one goal you missed, with the miss in a number, which of the three causes it was, and what you changed in the next half. If you also have a goal you *changed* mid-half because you learned the target was wrong, that's a strong second story — it shows you treat goals as tools, not promises to be defended.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Traceability | Mission walks up to an org goal in one or two steps | Mission invented locally, or a slogan |
| Boundaries | Says what the team is *not* for | Team does whatever is asked |
| Outcomes vs. output | Goals stated as measurable changes with a baseline | A list of things to ship |
| Calibration | Mix of stretch and expected goals; knows the hit rate | Hits 100% every half, or misses most |
| Mechanism | Names the artifact each review produces | "We check in regularly" |
| Early detection | Has an example of catching slippage weeks early | Learned about the miss at the review |
| Honesty on misses | Names the cause and the change that followed | Blames dependencies, or redefines the target |
| Team line of sight | Engineers can map their work to a goal | Goals live only in the manager's head |

**Follow-ups to prepare:**

- "Tell me about a goal you missed. What did you do?" (Use the four-step shape above.)
- "What if your team's mission and the org's priorities pull in different directions?" (That is Q12 — keep the answers consistent.)
- "How do your engineers know how their work connects to the mission?" (Good answer: they can state it themselves in 1:1s; if they can't, that's on you, not them.)
- "Have you ever changed the mission mid-year? Why?"
- "Has that 'would anyone notice' check ever failed for you?" (Have the real example: a project you realized nobody outside the team depended on, and what you cut or redirected. It doubles as the kill-decision story in the judgment archetypes.)
- "How do you set goals for platform work whose payoff is a year out?" (Leading indicators: adoption, time-to-ship for the next use case, number of teams that stopped building their own. Same answer as the Q11 follow-up — keep them consistent.)
- "Who sets the goals — you, or the team?" (Both: I bring the org constraints and a draft; the senior engineers pressure-test the targets and own the plans. Goals the team didn't shape are goals the team doesn't believe.)
