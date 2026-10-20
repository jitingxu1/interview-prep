# Speed vs. Scalability: a decision framework

For any question shaped like "tell me about a speed vs. scalability trade-off," "how do you balance moving fast with building it right," or "when do you take on tech debt."

## The principle

**Match the investment to what you already know.**

- **Speed buys learning.** When the bet is unproven, or the window is closing, the most valuable thing is an answer, fast. Build the smallest thing that gets it.
- **Scalability compounds.** When the bet is proven and you'll pay the same cost again and again, every hour invested in the system pays back on every future iteration.

The mistake in both directions is the same: investing as if you know more, or less, than you actually do. Scaling an unproven idea wastes the investment if the idea is wrong. Staying scrappy on a proven, repeated workflow taxes the team forever.

## The four questions

Ask these in order. They usually agree; when they don't, the first one wins.

| # | Question | Points to **speed** | Points to **scalability** |
| --- | --- | --- | --- |
| 1 | **Have we proven the bet?** | No: we're still learning whether it works or what we need | Yes: we know it works and we'll keep doing it |
| 2 | **Does the cost repeat?** | One-off, or rare | We pay it on every iteration |
| 3 | **What does waiting cost?** | The window is closing: an incident, a deadline, losses every day | The delay is bounded, and the drag of staying manual isn't |
| 4 | **Can we reverse it?** | Two-way door: cheap to redo later | One-way door: data models, public APIs, money, decisions about people — get it right up front |

**In one line for the room:**

> *"I choose speed when we're still proving the bet, the cost is one-off, or the window is closing. I choose scalability when the bet is proven, the cost repeats, and the delay is bounded. Either way, I never cut corners on the one thing that decides success."*

## Two rules that apply either way

**1. Be clear on the goal, then never cut the core.**
Speed doesn't mean everything is quick-and-dirty. Once you know exactly what you're trying to prove, every step sorts into *skip or simplify* and *must strengthen*. Simplify the first group hard; put your best people, and yourself, on the second.

**2. Name the cost of the path you didn't take, and manage it.**
- Choosing **speed**: say what debt you're taking on and when you'll pay it down. Keep the blast radius small (a small pilot, a kill switch, limited exposure).
- Choosing **scalability**: keep something shipping while you build, so stakeholders aren't asked to accept zero output on faith, and keep an escape hatch so the bet doesn't lock you in.

## Your stories, mapped

| Story | Choice | Why, by the four questions |
| --- | --- | --- |
| **Chargeback / fraud model pipeline** (`project-deep-dive/chargeback_model_automation.md`) | **Scalability** | Bet proven: we retrain fraud models constantly. Cost repeats every iteration (6–8 weeks of plumbing per model). Delay bounded: about a quarter of fewer new models. Reversible: we could still ship a model the old way. Managed the cost: kept one high-priority model shipping; escape hatches for the ~20% of models that didn't fit. |
| **Restaurant lending pilot** (`star_stories/story_11_restaurant_lending_pilot.md`) | **Speed** | Bet unproven: could we pick restaurants that need the money and will repay, and collect? Window: leadership wanted a pilot in a month. Exposure small and contained: 20 loans of $20–30K. Never cut the core: simplified the UI, communication, and backend, but put full strength on the underwriting model — I built it myself in a week. Paid the debt later: scaled to $20M once the bet was proven. |
| **ATO escalation** | **Speed first, then scalability** | Window closing: an active escalation with real users locked out. Fast, contained fix first; the long-term system went through planning afterward. |

The strongest answer uses **two stories that land on opposite sides**. It proves you have a framework rather than a preference.

## How to structure a ~2-minute answer

1. **Name both options** in a sentence each, and what each would have bought.
2. **State your choice and the questions that decided it** — usually two or three of the four, not all of them.
3. **Justify it in the stakeholder's terms**, not engineering terms. ("Slow iteration means we're fighting this month's fraud with last quarter's model.")
4. **Give the consequences, good and bad**, and how you handled the bad.
5. **Close with the other side**: "I don't always pick [X]. When [opposite conditions], I pick [Y] — for example [second story, one sentence]."

## Likely follow-ups

- **"What would have made you choose the other way?"** — Flip the four questions: "If we hadn't proven the bet yet, or the window had been closing, I'd have gone for speed — like the lending pilot."
- **"How do you stop speed from turning into permanent tech debt?"** — Name the debt when you take it on, and tie paying it down to a trigger: the bet is proven, or the volume crosses a threshold. In the lending pilot, the trigger was 19 of 20 loans repaid.
- **"How did you get stakeholders to accept slower delivery?"** — Show them where the time actually goes, frame it in their loss, and keep something shipping in parallel.
- **"Isn't a quick-and-dirty model risky when money is involved?"** — Yes, which is why the exposure was capped: 20 hand-picked restaurants and small loans. Speed with a small blast radius, not speed everywhere.
