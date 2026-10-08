# Q16. How do you advocate for more resources?

[← Round 2 index](README.md)

What is being tested is whether you argue like someone who understands the whole org's constraints or like someone defending a fiefdom. Headcount is zero-sum, and the managers who win it are the ones who make the case in the org's terms.

**The script:**

> I try to make the ask in the currency my leadership is actually working in, which is rarely "my team is busy." Everyone's team is busy. The case has to be about what the org doesn't get if the resource doesn't exist.
>
> So I bring three things. First, the cost of the status quo in concrete terms — what's being delayed, what risk we're carrying, how much time is going to work that shouldn't need a person. Second, what we've already done to avoid asking: what we automated, what we stopped doing, what we pushed back on. Asking for headcount before exhausting the cheaper options is how you lose credibility for the next ask. Third, a specific proposal — this role, this level, here's what it unlocks, here's how I'll know in six months whether it was the right call.
>
> And I try to name the alternative honestly. If the answer is no, here's what I'll drop — not as a threat, but because an unresourced commitment is a fiction and I'd rather we choose together than discover it in a quarter.
>
> Resources aren't only headcount, though. Often the faster win is borrowing capacity, getting a dependency re-prioritized by another team, or getting permission to stop doing something. I ask for those first, partly because they're cheaper to grant and partly because it shows I'm optimizing for the outcome rather than for team size.

**The strongest version of this answer** includes a time you *didn't* get the resource and what you did instead — cut scope, renegotiated the commitment, or solved it differently. That demonstrates you can operate inside constraints, which matters more to an interviewer than your ability to win budget fights.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Org currency | Frames the ask as what the org loses without it | "My team is overloaded" |
| Cheaper options first | Shows what was automated, cut, or pushed back first | Headcount as the first move |
| Specific proposal | Role, level, what it unlocks, how success is judged | "We need more people" |
| Honest alternative | States what gets dropped if the answer is no | Implies everything still gets done |
| Operating under no | A time they were told no and what they did instead | Every ask was granted |
| Peer awareness | Makes the case without undermining a peer manager | Zero-sum lobbying |

**Follow-ups to prepare:**

- "Tell me about a time you asked and were told no. What happened next?" (Full answer in "When you're told no" below.)
- "How do you decide between asking for headcount and cutting scope?"
- "How do you make that case without undermining a peer manager who's asking for the same headcount?" (Full answer in "Competing with a peer for the same headcount" below.)
- "What did you stop doing last year to free up capacity?"

## When you're told no

Winning resources is only half the skill; interviewers often care more about what you do when you don't get them. Every manager hears no — what's being tested is whether you can **operate inside constraints** without sulking, burning out your team, or quietly missing commitments.

**What they're testing:**

1. **Do you accept the no maturely?** No grudge, no relitigating.
2. **Do you understand why it was no?** Budget, priorities, or a weak case on your side?
3. **Do you adjust the plan explicitly** — rather than pretending everything still fits?
4. **Do you find other ways to get the outcome?** Creativity beyond headcount.
5. **Do you protect your team** — rather than asking everyone to work harder?
6. **Do you come back with a better case later?** Persistence backed by evidence.

**The shape of the answer:**

1. **The ask** — what you asked for and why, briefly.
2. **The no, and the reason** — what you were told, and what you learned when you asked why.
3. **What you changed in the plan** — what you dropped or delayed, and who you told.
4. **How you got the outcome anyway** — alternatives to headcount.
5. **What happened** — results, with numbers.
6. **Later** — did you ask again, with what new evidence, and what happened?

**Step 3 is the most important part.** "An unresourced commitment is a fiction": if you don't get the people, something has to give, and the mature move is to say what, out loud, in writing — to your director and to S&O and Product, since they own the targets and features that might slip:

> Without the extra headcount, we can deliver A and B this half, but not C. I'd suggest C moves to next half. Can we agree on that?

The two failure modes: **the martyr**, who accepts the no, still promises everything, and then burns out the team or quietly misses; and **the sulker**, who accepts the no, then underdelivers while hinting it's leadership's fault.

**Step 4 — ways to get the outcome without headcount:**

| Approach | Example in your domain |
| --- | --- |
| Automate | Automate model retraining and monitoring, freeing ~20% of an engineer's time |
| Stop doing something | Retire a low-value legacy model; hand ad-hoc analysis requests to S&O's analysts |
| Cut or phase scope | Cover the top 2 fraud types first, not all 5 |
| Borrow | An engineer from a partner team for a month, or a DS from another team for one analysis |
| Self-serve | Tooling so S&O can adjust thresholds themselves instead of filing requests |
| Reuse | An existing platform or model instead of building new |

**Step 6 — asking again, the right way.** Don't re-send the same request next quarter. Bring evidence that the no had a cost: *"Last half we couldn't do C. Since then, the fraud type C would have covered caused $X in losses, and we spent Y engineer-weeks firefighting it manually."* That turns the next ask from an opinion into data, and it's often how the second request gets approved.

**An example scenario** (made up — use your real one):

> I asked for two more ML engineers to build real-time fraud detection for a new payment flow. My director said no — there was a hiring freeze, and the org had prioritized another area.
>
> I asked what would change the answer, and learned it was a budget constraint, not a doubt about the value. So I didn't relitigate. I went back to S&O and Product with a revised plan: we'd cover the two highest-loss fraud patterns with a batch model now, and push real-time to next half. They agreed, and I put it in writing.
>
> To make even that fit, we automated model retraining — that freed about a fifth of one engineer's time — and handed ad-hoc analysis requests to S&O's analysts with a self-serve dashboard.
>
> The batch model caught [X]% of the targeted fraud. And because I'd tracked what the delayed real-time work was costing — about [$Y] a month in fraud the batch model missed — I came back next half with that number. That time it was approved.

**The spoken answer, short version:**

> When I'm told no, I first ask why — whether it's budget, priority, or my case wasn't strong enough, because each needs a different response. Then I don't pretend everything still fits. I go back to my stakeholders with an explicit tradeoff — here's what we'll deliver, here's what moves — and get agreement in writing. Then I look for other ways to get the outcome: automating, stopping low-value work, phasing the scope, borrowing help. And I track what the no is actually costing, so if I ask again, I'm bringing data, not the same request louder.

**How they grade the "told no" answer:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Maturity | Accepts the no and asks why | Resentful, or blames leadership |
| Explicit tradeoff | Tells stakeholders what moves, in writing | Promises everything anyway |
| Team protection | Changes the plan instead of overloading people | "We just worked harder" |
| Creativity | Automates, cuts, phases, borrows | Headcount was the only option |
| Results | Delivered the most important outcome anyway | Everything slipped |
| Evidence-based persistence | Tracked the cost of the no and came back with data | Re-asked the same way, or never again |

**Pick a real story if you have one** — this is the strongest version of the resources answer, because operating under constraints matters more to interviewers than winning budget fights.

## Competing with a peer for the same headcount

The situation: you and another manager both want the same limited headcount, and the director can fund only one. Headcount is zero-sum, so your director is watching two things — **are you thinking about the whole org or only your team**, and **can you compete without damaging the relationship**? That peer is someone you'll depend on next quarter. Win the headcount and lose the partnership, and you've lost overall.

**1. Talk to your peer first, before the director decides.** Don't let the director be the first to hear both cases side by side: *"I know we're both asking for headcount this half. Can we compare notes? I'd like to understand your case, and I'll share mine."* Often one need is clearly more urgent this half, the role can be **shared** or **sequenced**, or one of you has a cheaper alternative.

**2. Argue for your case, never against theirs.** Make it on its own merits, in org terms — what the org gets, what it loses without the role.

| Undermining (bad) | Advocating (good) |
| --- | --- |
| "Their project isn't as important as ours." | "Here's what this role unlocks for the org's fraud-loss goal." |
| "Their team is already overstaffed." | "Here's what we've already done to avoid asking — automation, things we stopped doing." |
| Quietly lobbying the director in 1:1s | Making the case openly, in the same forum as your peer |
| Inflating urgency to win | Being honest about what happens if you don't get it |

**3. Frame it as the org's choice, not a contest.** The strongest move is a joint view with your peer: *"We both have real needs. Here's a side-by-side — what each role unlocks, the cost of waiting, and options like sequencing or sharing. We're both fine with whatever you decide."* It saves the director time and makes you both look like org-level thinkers.

**4. Offer creative alternatives.** It often isn't really either/or:

- **Sequencing** — one team gets the hire in Q1, the other in Q2, depending on whose deadline is earlier.
- **Shared role** — one person whose work serves both teams, such as a platform engineer on shared infrastructure.
- **Borrowing** — lending engineers between teams to cover a peak.
- **Cutting scope** — one team deprioritizes something instead of hiring.

**5. If you lose, support your peer's success.** Accept it without relitigating, adjust your plan (cut scope, renegotiate commitments), and actively help them — share candidates from your pipeline, help with interviews. Directors remember who handled losing well, and it's what makes your next ask credible.

**An example scenario** (made up — the shape is what matters):

> You manage Risk ML; a peer manages Logistics ML. You both want a senior ML engineer this half, and the director can fund one. You meet your peer first. Their need: a model migration with a hard Q1 deadline. Yours: scaling the fraud platform — important, but more flexible on timing. You propose together that they get the hire in Q1 and you get the next approved role in Q2, and meanwhile one of their engineers who knows the shared feature pipeline pairs with your team for a month. You bring the joint proposal to the director, who accepts it.

**The spoken answer:**

> I make my case on its own merits, never by arguing against theirs. Before it goes to our director, I talk to the peer directly — what's their need, what's mine, what's the cost of waiting for each. Often one of us is more time-sensitive, and we can sequence it, share a role, or one of us solves it another way.
>
> Then ideally we bring the director one joint view: what each role unlocks, the cost of delay, the options. That turns it from a contest into an org decision — which is what it really is. And if it goes to them, I commit to that, adjust my plan, and help them succeed — even sharing candidates from my pipeline. The relationship with that peer matters more than any single headcount decision, and how I lose is what makes my next ask credible.

**How they grade the peer-competition answer:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Org-level thinking | Frames it as the org's choice, in org terms | "My team needs it more" |
| Peer relationship | Talks to the peer first and compares openly | Lobbies the director privately |
| Advocacy style | Argues for own case, not against theirs | Criticizes the peer's project or team |
| Creativity | Offers sequencing, sharing, borrowing | Treats it as strictly win/lose |
| Honesty | States the real cost of waiting | Inflates urgency to win |
| Losing well | Commits, adjusts, and helps the peer succeed | Relitigates or holds a grudge |

**Have a real example if you can:** a time you and a peer competed for the same resource and how you resolved it. Even a small one works — a shared data scientist's time, or an infra team's roadmap slot. Most candidates only have stories where they won, so this stands out.
