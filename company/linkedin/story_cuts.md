# Story Cuts — First Person, 2 Minutes

Your STAR files are written in second person ("You called a team meeting"). Spoken aloud that sounds rehearsed. These are the four you're most likely to need tomorrow, rewritten the way you'd actually say them.

`[bracketed]` = fill in a real number before tomorrow. Don't say a story with a hole in it.

---

## Cut 1 — Building the team (Theme 1) ~2:00

> "My manager left the Risk ML team without much warning. Ten engineers, no interim, and I was the tech lead. So I stepped into both roles at once, and I'd never managed before.
>
> The first thing I did — within a day — was get everyone in a room and be straight with them. I said: I'm taking this on, I've never done it, we'll figure it out together. Here's what doesn't change: your 1:1s, your career conversations, the support you were getting. Here's what we'll build together: the process and the clarity that were missing.
>
> Then I did three things deliberately. I started weekly 1:1s with every person and made them non-negotiable — and I used them to ask two questions: where do you actually want to go, and what was missing with the last manager. I stayed hands-on technically, because I knew if people thought they'd lost technical direction along with their manager, they'd leave. And I went to every cross-functional partner individually and asked what they were waiting on from us, so our commitments didn't quietly drop while we were reorganizing.
>
> The outcome: zero attrition through the transition. Delivery stayed on track. Within six months I'd hired [2] engineers, promoted one to senior IC, and the team grew from there to [12] across two pods.
>
> What I'd do differently — I under-invested in written feedback early on. I was having good conversations but not documenting expectations, and that caught up with me later. I'll come back to that if it's useful."

*That last line is bait for the S5 follow-up. Use it if you want to steer toward a growth question.*

---

## Cut 2 — Right person, wrong seat (Theme 1) ~2:00

**Your best people story. Lead with this when he asks about someone struggling.**

> "I had a senior engineer with about eight years of backend experience who'd moved into ML. Smart, motivated, worked hard. But I kept getting the same feedback from peers and cross-functional partners: he's making ML calls without the ML depth, the designs feel over-engineered from a backend instinct. It happened repeatedly, and I could see his confidence dropping.
>
> The easy read is a performance problem. I didn't think it was. He was strong — just in the wrong domain. And 'get better at ML faster' isn't a plan.
>
> At the same time, my team was scaling out agentic systems and we needed someone to build the execution infrastructure for them. That's a backend problem, not an ML problem. And it was exactly what he was excellent at.
>
> So I was direct with him. I said: the feedback you're getting is real, and it's because ML is new territory for you — that's not a character flaw. But I have work where you'd be the strongest person in the room, and it's the agent infrastructure. I framed it as an expansion, not a step down, because that's what it actually was.
>
> He took it and ran. Within a few months he'd built the infrastructure that became a core capability for the whole platform — it unblocked other teams, not just mine. He got his confidence back. No attrition, no bitterness.
>
> The lesson I took: 'this person isn't working out' and 'this person is in the wrong seat' look identical from the outside. It's worth the effort to tell them apart, because the second one is usually recoverable and you get a great engineer out of it."

---

## Cut 3 — Cross-org influence (Theme 3) ~2:15

**Your strongest story overall. This is your answer for influence, for Product partnership, and for cross-functional conflict.**

> "I'd built a delivery-level risk score that worked well for catching fraud *after* an assignment happened. I wanted to move from reactive to proactive — put the risk score into the assignment algorithm itself, so we'd never assign a fraudulent delivery in the first place. That meant working with the logistics team, and it was the first time our two orgs had built anything together.
>
> I had their buy-in in principle. But when the model was ready and I asked for an online experiment, they stopped me. Two reasons. First, the engineers who built their offline simulation had just left the company, so they literally couldn't evaluate a new input — they'd lost the knowledge. Second, they were worried my model would slow assignments down and hurt their assignment rate and time-to-assign.
>
> Both concerns were completely legitimate, and I think that's the thing — I didn't argue with either one.
>
> What I did instead: I committed my own time and resources to rebuilding their simulation system. Not my project, their system. We made it more automated and self-serve, so they weren't dependent on knowledge that had walked out the door. That took [X weeks], and it was the thing that actually earned the yes.
>
> Then we redefined success together. I proposed that *their* assignment metrics be the primary objective — those have to stay flat — and fraud loss be the guardrail we're trying to move. That's the inversion that mattered. I wasn't asking them to take risk for my metric; I was asking them to help prove we could win without hurting theirs. And I built shared real-time dashboards so both sides were visible to both teams.
>
> They greenlit it, committed engineers, and we launched it as a joint experiment. [Result: fraud loss moved X, assignment metrics stayed within Y.]
>
> The general lesson: when a partner team says no, the reason is almost always their metric or their capacity. Find out which, and then absorb some of that cost yourself. Arguing about whose model is better doesn't move anyone."

---

## Cut 4 — Tradeoff under uncertainty (Theme 2) ~1:45

> "We had a fraud model with good precision on the fraud we caught, but the false positive rate meant we were blocking legitimate customers. The business wanted it shipped — the fraud losses were real. I was worried about the user experience cost, and there was no threshold that made both problems go away.
>
> So I stopped treating it as a yes/no ship decision. I got product, ops, legal, and the business side in a room and made the tradeoff explicit: here's fraud dollars prevented at each threshold, here's the estimated legitimate users we block and the support tickets that generates. Put both on the same axis so people were arguing about a number instead of a principle.
>
> What we agreed to was a phased rollout — start only on the highest-confidence signals, instrument the false positive rate with alerting on a threshold we'd agreed in advance, and review weekly with the business to move the threshold as we learned. I personally went through the edge cases, because I wanted to understand where it was failing rather than just watch the aggregate.
>
> We landed at catching [40%] of fraud with under [2%] false positives, and it held for three months. Then we got more aggressive as we understood the failure modes. [$X in prevented loss.]
>
> The thing that outlasted the project was the pattern: model the tradeoff for the stakeholders, ship phased, agree the abort threshold *before* you launch. We used that for every model deployment after."

---

## Before you say any of these

Fill in the brackets. At a leadership screen, "we reduced fraud significantly" gets an immediate "by how much?" — and not having the number costs you more than the number would have gained you.
