# Checkr: hiring manager interview with Gio

[← Checkr index](README.md)

Built from the recruiter prep call with Taylor (2026-10-12) and your existing stories. Gio is the hiring manager and the key decision maker. Everything after this round depends on it.

## The thread through the whole hour

Taylor's one-line advice: **show a business-minded engineering leader.** In every answer:

1. **Lead with impact** — the business result in the first two sentences, not at the end.
2. **Show ownership** — what *you* saw, decided, and did. "I," not "we," for decisions.
3. **Include the hard or ambiguous moment** — the part where it could have gone wrong.

## What's public about Checkr manager interviews (checked 2026-10-15)

No verbatim Checkr EM questions are posted publicly. What's available:

**一亩三分地 (1point3acres):** no Checkr manager or hiring-manager posts. Its Checkr list has about nine software engineer posts from 2021 to May 2026 — coding (name matching), API design ("MVR Rules"), and a refactoring challenge — with no behavioral questions. A multi-company EM thread there notes EM interview posts are rare on the forum in general.

**Interview structure from a March 2026 EM report (Glassdoor, San Francisco):** recruiter screen → hiring manager round → product manager round on collaboration → two rounds with engineering managers on **hiring, team management, and project retros**. A 2023 report describes a similar all-behavioral loop: management, product, conflict resolution, mentoring, plus a technical execution screen. Candidates said to be ready to discuss **processes you've implemented, how you motivate your team, and how you communicate up and down**.

**Checkr's five official values** (from its careers page). Interviewers reportedly ask behavioral questions based on these:

| Value | Checkr's wording | Your story |
| --- | --- | --- |
| Grit | "We are passionate and hustle to raise the bar. We persevere through our challenges and grow from our failures." | Story 10 (no → yes in two weeks); ATO escalation |
| Ownership | "We strive for thoughtful impact and hold ourselves accountable." | Chargeback automation |
| Transparency | "We trust each other to communicate the good and the bad… receptive to feedback." | ATO report and dashboard; "we can't catch every fraud" |
| Humility | "We are respectful and free from arrogance… excited to learn from each other." | Story 8 (right person, wrong seat); a mistake you owned |
| Connection | "We genuinely care about each other and understand that our people are our power." | Story 1 (management transition, zero attrition) |

The careers page also says Checkr hires for an **"AI Native"** edge — "If you're an AI skeptic, this isn't for you" — which explains the required AI questionnaire.

**If this is the Senior EM, Machine Learning role** (posted on Checkr's job boards), its wording lines up with Gio's areas: "Keep ownership of every output. As generated code becomes cheaper, raise the bar on judgment"; "Raise the production engineering bar. Models and agents ship as dependable software"; "a strong bias for action… move with urgency"; "Use AI to increase the team's speed and ambition." It also asks for evaluation and golden sets, training-data provenance, and model and prompt versioning — your chargeback pipeline (dataset versioning, frozen eval harness, model registry with lineage) maps onto that directly. Quote one of these lines back if it fits naturally.

**Likely questions beyond Gio's areas** (from the public reports — prepare for the panels too):

| Question | Your story |
| --- | --- |
| Hiring: a strong hire, or a hire you got wrong | Story 4 (hiring and leveling) |
| Team management: a low performer, or someone struggling | Story 8 (right person, wrong seat) |
| A project retro: what went wrong, what you changed | Chargeback automation, or the merchant onboarding call |
| Working with a PM who disagreed with you | Stripe Q14 notes: S&O and Product |
| Conflict | Story 6 (conflict resolution) |
| Mentoring | Story 9 (unblocking a stuck engineer) |
| Communicating up and down | ATO report to your director; shielding the team |

Sources: [1point3acres Checkr list](https://www.1point3acres.com/interview/company/checkr) · [Glassdoor EM reports](https://www.glassdoor.com.hk/Interview/Checkr-Interview-E985716-RVW78360888.htm) · [Checkr careers](https://checkr.com/company/careers) · [Senior EM, ML posting](https://jobs.accel.com/companies/checkr/jobs/92577974-senior-engineering-manager-machine-learning)

## Story map

| Area | Question to expect | Your story | Why it fits |
| --- | --- | --- | --- |
| Ownership | A problem you spotted unprompted that drove a business result | **Chargeback model automation** | You saw that model iteration took 6–10 weeks, mostly plumbing — nobody asked you to fix it |
| Technical standards | A speed vs. scalability trade-off | **Same story, the trade-off angle** — backup: foundation over firefighting | You chose to build the pipeline (scalability) over shipping models faster by hand (speed). Taylor said to pick scalability, because the next question covers speed |
| Relentless execution | Your highest-tempo project; how you personally unblocked the team | **Story 10: risk score in the assignment algorithm** | From "no" to full buy-in in two weeks, a four-week experiment, and you personally rebuilt the partner team's simulation system with them |
| AI-first questionnaire | ~12 min of quick questions in four tiers | Your agentic AI pod, Story 10's AI use, your own setup | See the questionnaire section |

Using one story for both ownership questions is deliberate: Gio goes deep, and one story told in layers beats two told thinly. If he wants a second example, use the foundation story.

## 1. Ownership: a problem you spotted unprompted

**What he's looking for:** you saw the stakeholders' problem before anyone handed it to you, and you drove a real business result — not just a technical improvement.

**Story: unifying and automating the fraud model pipeline** (combines the chargeback automation and the foundation-over-firefighting work). Told in STAR, result first:

> **[Result first]** At DoorDash, I cut our fraud model iteration time from six to eight weeks down to two to three, and freed up two to three ML engineers to work on new fraud problems instead of plumbing. Nobody asked me to fix it — everyone had accepted the slowness as the cost of doing ML.
>
> **[Situation]** When I joined, we had a small ML team facing a lot of fraud problems. Stakeholders were frustrated: new models took too long, updates were slow, and we kept missing new fraud trends. The engineers were frustrated too — constant deadlines, lots of repetitive work.
>
> **[Task — what I saw]** The complaints were about speed, but when I dug in, the real problem was how we built models. Every stakeholder request became its own model, so we had [N] models that overlapped heavily, each with its own features, labels, and evaluation. And the process was manual: everything lived in separate notebooks, so engineers re-pulled the same data, restarted jobs that failed halfway, and couldn't easily tell what data trained a production model. We weren't slow because people weren't working hard. We were slow because we kept rebuilding the same things by hand.
>
> **[Action]** I proposed two things. First, **unification**: I inventoried every model — what use case it covered, what it protected — and merged overlapping ones onto shared feature pipelines, shared labels, and one evaluation standard. That took us from [N] models to [M]. Second, **automation**: an orchestrated pipeline with versioned data, training that automatically resumes from checkpoints, and a fixed evaluation gate before anything ships.
>
> The hard part was the pitch. This meant fewer new models for [about a quarter] while we built it, and stakeholders wanted output, not infrastructure. So I framed it in their terms: slow iteration means we're fighting this month's fraud with last quarter's model. I [kept one high-priority model shipping in parallel], so they weren't asked to accept nothing on faith. The engineers were easy to win: it removed the work they hated most.
>
> **[Result]** Model development went from six to eight weeks to two to three — one to two for engineers fully on the pipeline. Experiments went from two to three months to four to six weeks. We moved from quarterly model updates to [monthly], and we could respond to new fraud patterns in weeks instead of quarters. [Business number: e.g. fraud loss reduced by X, or a new fraud pattern caught within Y weeks.]
>
> **[Reflection]** What I'd do differently: I'd have measured where the weeks actually went before pitching it. Once I had that breakdown, the argument got much easier.

**Numbers to fill in:** models before and after unification ([N] → [M]); how long new-model delivery slowed during the build; whether one model kept shipping in parallel; the change in update frequency; and one business metric. If there's no business number yet, connect the freed capacity to new coverage: "freed up 2–3 MLEs, and we used that capacity to cover [new fraud area]."

**The hard moment to include:** [Who doubted it? E.g. a quarter where fewer models shipped while the pipeline was being built, or engineers attached to their notebooks.] This is where Gio digs.

**Likely follow-ups:**

- "How did you know it was worth fixing?" — The 6–10 weeks, and that most of it was plumbing, not modeling. You measured where the time went.
- "Who did you have to convince?" — [Fill in.] Frame the pitch in business terms: stale models mean losses.
- "Why didn't anyone fix it before?" — Everyone treated it as the normal cost of ML. Spotting a cost everyone has accepted is the ownership signal.

## 2. Technical standards: the speed vs. scalability trade-off

**What he's looking for:** a real decision-making framework — how you justified the call to the team and stakeholders, what you optimized for, and the downstream consequences.

**Same story, told as the trade-off:**

> The trade-off was real. The fast option was to keep shipping models the old way — a heroic engineer could push one model through in a few weeks, and the business would have seen output sooner. The scalable option was to pause and build the pipeline, which meant fewer model releases for [a quarter] while we built it.
>
> I chose scalability, and here's the framework I used. First, **is this a one-time need or a repeating one?** Chargeback models retrain constantly because fraud drifts, so any manual cost got paid again every cycle. Second, **what's the cost of delay?** Pausing for [N weeks] cost us a few model updates; staying manual cost us six to ten weeks on every update, forever. Third, **is it reversible?** We built it so a model could still go out the old way in an emergency, so the bet didn't trap us.
>
> To justify it to stakeholders, I [kept one model update going in parallel / showed the 6–10-week breakdown], so they weren't asked to accept zero output on faith.
>
> The downstream consequences were mostly good, with one cost: standardizing meant less flexibility for unusual models. About 80% of our work fit the standard pipeline, so we built escape hatches — engineers could plug in custom steps — rather than forcing everything through one path.

**The framework, in one line for the room:** *"I choose scalability when the cost repeats, the delay is bounded, and the decision is reversible. I choose speed when it's a one-off, the window is closing, or we're still learning what we need."*

**Show you don't always pick scalability.** Have one sentence ready: the ATO escalation, where the right call was a fast, contained short-term fix while the long-term plan went through planning. Judgment means knowing which situation you're in.

**Backup story: foundation over firefighting** (several teams wanted bespoke models; you built shared features and serving first). Use it if he wants a second example or a roadmap-level trade-off. See `leadership/stripe_strategy_and_execution/13_foundation_story.md` — its blanks need filling first.

**Likely follow-ups:**

- "What would have made you choose speed instead?" — The one-line framework above, reversed.
- "What did the team think?" — [Fill in: who pushed back, and what you said.]
- "What broke afterward?" — The flexibility cost, and the escape hatches you built.

## 3. Relentless execution: the highest-tempo project

**What he's looking for:** what speed actually looked like — told with energy and specifics — and a concrete moment where **you personally** unblocked the team, technically, organizationally, or cross-functionally. Taylor's warnings: don't pick a "fast project" that was really normal pace, and **never blame slowdowns on other teams.**

**Story 10: embedding the risk score into assignment.**

> I'd built a delivery-level risk score that worked well for catching fraud *after* a delivery was assigned. I wanted to move it upstream — block risky driver-delivery pairings before assignment — which meant working with the logistics assignment team for the first time.
>
> They agreed in principle, but when the model was ready, they hit the brakes, and for good reasons: the engineers who'd built their offline simulation system had just left, so they had neither the bandwidth nor the knowledge to integrate a new input, and they were worried my model would slow assignment, which is their core metric.
>
> Here's where the speed came from. Instead of escalating or waiting for their roadmap, I put my own time in: six to eight hours a week for two weeks, pairing with their senior engineer to rebuild their simulation system — making it more automated and self-serve. I used Claude to document their assignment logic and generate test cases, and their engineer reviewed and owned everything, so they weren't left depending on me.
>
> In parallel I reframed success: their assignment metrics became the primary objective that had to stay flat — under 50 ms p95 — and fraud loss became the guardrail we were trying to move, with a kill switch if assignment time degraded more than 2%.
>
> From their "not now" to full buy-in took two weeks. The experiment ran four weeks. Fraud loss on risky pairings dropped 12%, assignment time stayed within half a millisecond, and they made it a permanent input to the assignment algorithm. We shipped three follow-on projects together over the next year.

**Why it scores on every warning:**

- **Real tempo with specifics:** two weeks to buy-in, a four-week experiment, then permanent integration.
- **Personally unblocking, all three kinds:** technical (rebuilt the simulation), organizational (reframed the metrics), cross-functional (a first-time partnership).
- **No blame:** you describe the assignment team's constraints with empathy — they had lost the people who knew the system, and you absorbed that cost yourself.

**Likely follow-ups:**

- "Why did you do their work?" — It was the fastest path to the outcome, and I built it with their engineer so they owned it afterward. No long-term dependency on me.
- "What did you de-prioritize to find that time?" — [Fill in.]
- "What if the experiment had hurt assignment time?" — The kill switch: pause at a 2% degradation, agreed before launch.

**Backup if he wants a crisis-tempo example:** the ATO escalation — a CEO-level escalation, a situation report within [48 hours], short-term mitigation within [N days]. Its facts aren't pinned down yet (see `leadership/stripe_people_and_leadership/01_em_skills.md`), so only use it if you can fill them.

## 4. AI-first questionnaire (~12 minutes, four tiers)

Required for all manager interviews. Quick questions, so **answer in 30–60 seconds each** — one concrete example per answer, not a philosophy.

| Topic | Your answer, short |
| --- | --- |
| **Your AI dev setup** | [Confirm and fill in.] E.g.: Claude Code in the terminal as a daily driver — for coding, reviewing diffs, and writing docs — plus [IDE assistant]. Say *how* you use it, not just which tools: "I give it the repo and a narrow task, review every diff, and keep a project instructions file so it follows our conventions." |
| **Last thing you shipped with meaningful AI involvement** | Story 10: you used Claude to document the assignment team's algorithm and generate test and edge cases for the rebuilt simulation system — part of why buy-in took two weeks instead of a quarter. Or a more recent one from your agentic AI pod. [Pick the most recent real one.] |
| **Helping your team adopt AI** | [Fill in what you actually did.] Strong shapes: pick one workflow and prove it (e.g. test generation or code review), share what worked in a team demo, write down team conventions for prompts and review, and measure something — review time, cycle time — instead of mandating tools. |
| **Opportunities beyond code generation** | From your own domain: agentic customer-support automation (your agentic AI pod), LLMs as labelers to create training data for fraud models, summarizing fraud investigations for ops, drafting documentation and runbooks, and generating test and edge cases. |
| **When *not* to use AI** | Use your ATO story: you didn't push a model to auto-block accounts when there was no verification or recovery channel, because a wrong call locked a real person out with no way back. The general rule: don't put AI in a high-stakes, irreversible decision without a human or a recovery path; don't use an LLM where a deterministic rule does the job; and be careful where you need auditability or tight latency. Very relevant at Checkr, where a wrong decision affects someone's job. |

**Tier strategy:** questions likely get harder or more strategic as they go. For the first ones (your setup), be crisp and concrete. For the later ones (adoption, when not to use AI), show judgment: what you'd measure, where the risk is.

**One line worth having ready for Checkr specifically:** background checks decide whether someone gets a job, so accuracy, fairness, and auditability matter as much as speed. Your fraud and trust work at DoorDash is the same shape: high-stakes decisions about people, where false positives hurt real users.

## Questions to ask Gio

Prepare three; ask two.

- "What does the team look like today, and what's the biggest gap you're hiring this role to close?"
- "What does success look like in the first six months?"
- "How is the team actually using AI day to day, and where do you want it to be in a year?" (Ties back to the questionnaire and shows you'd drive it.)
- "What's the hardest trade-off the team is facing right now — speed or scale?" (Echoes his own question back; good if the conversation went well.)

## Logistics and process

- **After Gio:** three virtual panel interviews, a prep session, then an onsite project presentation in San Francisco — about an hour, with three people. Your chargeback automation deep dive is a strong candidate for the presentation; it already has the problem, architecture, trade-offs, and results written up.
- **Offices:** San Francisco and Denver only. You confirmed no commute issues.
- **Timeline:** you told Taylor you have no other opportunities or timeline yet.
- **Next step:** Taylor follows up after the Gio interview.

## Before the interview

- [ ] Fill the brackets in all three stories, above all: the business number for the chargeback story, and who pushed back
- [ ] Confirm your AI dev setup and pick your most recent AI-shipped example
- [ ] Rehearse each story out loud in about 2 minutes, impact first
- [ ] Practice the scalability-vs-speed framework line until it sounds natural
- [ ] Prepare 30–60-second answers for all five AI questionnaire topics
- [ ] Find out the fourth value area (see the README)

## Mock log

### Mock 1 — 2026-10-15, Ownership question

**Question:** "Tell me about a time you spotted a problem your stakeholders were living with that nobody had asked you to fix, and you went and drove a real business result."

**What worked:** strong material — you named both sides of the pain (stakeholders: slow models, low coverage, missed fraud trends; engineers: repetitive work and deadline pressure), found the root cause (manual, siloed model building; duplicate firefighting models), and proposed two concrete fixes (unification and automation).

**What to fix:**

1. **The result came last, with no number** ("XXX times faster"). Lead with the result in the first two sentences: 6–8 weeks → 2–3 weeks; 2–3 MLEs freed.
2. **Separate the complaint from your insight.** Everyone could see the complaints; your ownership is that you found the root cause. Say it explicitly: "We weren't slow because people weren't working hard. We were slow because we kept rebuilding the same things by hand."
3. **No hard moment.** Pausing to build meant fewer new models for a while — say who resisted and how you won them over. Gio will dig here.

The rewritten STAR version is in the Ownership section above.
