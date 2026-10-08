# Q10. What is your process for creating a roadmap?

[← Round 2 index](README.md)

They want the actual mechanics, including the political parts: where input comes from, how you say no, and how you get buy-in.

**The script:**

> Three inputs, and I gather them before I write anything. First, top-down: what the org committed to this half. Second, bottom-up: what my engineers think is broken or slow — they know the real constraints better than I do. Third, demand: what partner teams are asking for, and crucially, *why* — the underlying need, not the feature they've specified.
>
> Then I look for the pattern across requests rather than queueing them. Five teams asking for five similar things usually means one capability is missing, not five projects. That reframing is where most of the leverage is.
>
> I split capacity deliberately. Roughly: committed work for the org's goals, investment work that makes us faster later, and a reserve for the unplanned — incidents, urgent asks, things that break. If I plan to 100%, the first surprise makes me a liar.
>
> Then I write it down with explicit tradeoffs — and critically, a visible "not doing this half" list with the reason. The not-doing list is what makes the roadmap real; without it, everyone assumes their request is in.
>
> Buy-in comes from doing this in the open. I take the draft to the teams whose requests are deferred, before it's published, and I'd rather have the argument then than in a status review two months later. Where they disagree, I either change the plan or explain the tradeoff. What I don't do is publish a roadmap that quietly drops someone's request.

**The sentence that does the work:** the not-doing list. Most candidates describe collecting input and prioritizing; few describe publishing what they declined and defending it in person.

**Protecting the reserve.** This is the political part, and interviewers often probe it:

1. **Make it visible.** Put the reserve on the roadmap as its own line, so it doesn't look like idle people.
2. **Explain it with the history.** "Last half, 22% of our time went to unplanned work. If I don't plan for it, I'll miss commitments, so I plan for it."
3. **Don't let it be spent quietly.** Unplanned work that doesn't truly need to happen now goes through the same prioritization as everything else. The reserve is for urgent work, not for anything someone asks for.
4. **Tie it to credibility.** "If I plan to 100%, the first surprise makes me a liar." Leadership usually accepts this once they see the team hitting its commitments.

**Planning horizons: how far out to plan.** The further out you plan, the less certain you can be — so plan in less detail the further you look.

| Horizon | Level of detail | What it looks like | How often it changes |
| --- | --- | --- | --- |
| **This quarter** (~3 months) | Detailed: projects, owners, milestones, dates | "Feature store v1 ships by Feb 15; Alice owns it; three teams migrate in March." | Rarely — it's a commitment |
| **This half** (~6 months) | Direction: goals and main bets, no exact dates | "By end of June, new risk models take 2 weeks to build — likely via the shared serving layer." | Adjusted at the quarter boundary |
| **Beyond** (1–2 years) | Themes: where we're heading and why | "Long term: every team self-serves ML on our platform." | Revisited a couple of times a year |

*Why:* certainty decays with time. A detailed twelve-month plan is fake precision — other teams plan around your dates and get burned, the plan keeps changing so people stop trusting it, and you waste time maintaining something that will be rewritten anyway. Long-term direction is fine; dressing it up as a schedule is not.

*What each horizon is for:* the quarter is what partner teams can depend on — a date there is a promise. The half is what you're accountable for (your Q9 goals), with room to change the approach. Beyond is what keeps short-term work pointed somewhere, and what justifies investment work that won't pay off this quarter.

*The nuance worth mentioning:* the right horizon depends on the work. A product team shipping fast-moving features may only plan a quarter in detail; a platform or infra team often needs a year of direction because migrations and adoption take multiple quarters — but even then, only the current quarter gets dates.

> A quarter in detail, the half in direction, and beyond that only themes. This quarter has owners, milestones, and dates — that's what partner teams can depend on, so I treat those dates as promises. The half is our goals and the main bets, but I don't put exact dates on the second quarter, because I'll know much more in three months. Beyond the half, I keep a one-page view of where we're heading and why — that's what justifies investment work now — but I'm explicit that it's direction, not a schedule.
>
> The reason is credibility. If I publish a detailed twelve-month plan, it'll be wrong by month four, other teams will have planned around it, and the next plan I publish will be trusted less. I'd rather be precise where I can be right and honest where I can't.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Input breadth | Top-down, bottom-up, and partner demand — gathered before drafting | Roadmap is the loudest stakeholder's list |
| Pattern-finding | Spots one missing capability behind several requests | Queues requests one by one |
| Capacity realism | Explicit split with a reserve for the unplanned | Plans to 100% |
| Saying no | A published not-doing list, with reasons | Everything is "on the backlog" |
| Buy-in | Takes deferrals to affected teams before publishing | Teams find out from the published doc |
| Adaptability | A real mid-quarter replan and what triggered it | The plan never changed, or changed silently |
| Planning horizons | Detail near, direction mid, themes far — and says why | One detailed plan for the whole year, or nothing beyond this quarter |
| Reserve discipline | Reserve sized from data and defended openly | Reserve hidden, guessed, or quietly spent |

**Follow-ups to prepare:**

- "What percentage goes to the reserve, and how did you pick it?" (From data, not instinct: measure the last two quarters of unplanned work, adjust for what's different this half, then track actual usage. Overflow means fix a root cause; unused reserve goes to investment work, not new commitments. See "Protecting the reserve" above.)
- "What do you do when the roadmap breaks mid-quarter?" (Have a real example of a replan.)
- "How do you handle a request from someone senior that you think is wrong?" (Full answer in [Q10a](10a_saying_no_to_senior.md).)
- "How far out do you plan?" (A quarter in detail, the half in direction, nothing beyond that pretending to be certain. See "Planning horizons" above.)
