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
| Ownership | A problem you spotted unprompted that drove a business result | **Never-delivered abuse: reactive → proactive** — backup: driver time abuse | The ask was a better model; you saw the model sat too late in the flow, and moved detection to order time with a verification code |
| Technical standards | A speed vs. scalability trade-off | **Fraud model pipeline** (chargeback automation) — backup: foundation over firefighting | You chose to build the pipeline (scalability) over shipping models faster by hand (speed). Taylor said to pick scalability, because the next question covers speed |
| Relentless execution | Your highest-tempo project; how you personally unblocked the team | **Story 11: restaurant lending pilot** — backup: Story 10 | Six-month plan cut to a one-month pilot; you personally built the underwriting model in a week; 19 of 20 loans repaid, program grew to $20M |
| AI-first questionnaire | ~12 min of quick questions in four tiers | Your agentic AI pod, Story 10's AI use, your own setup | See the questionnaire section |

Each area now has its own story, so Gio hears three different projects: never-delivered abuse (ownership), the model pipeline (scalability), and the lending pilot (speed). The pipeline and the lending pilot land on opposite sides of the trade-off — see [`leadership/speed_vs_scalability.md`](../../leadership/speed_vs_scalability.md).

## 1. Ownership: a problem you spotted unprompted

**What he's looking for:** you saw the stakeholders' problem before anyone handed it to you, and you drove a real business result — not just a technical improvement.

**The principle behind your answer — this is your daily work:** stakeholders bring an *ask*; you turn it into the *real solution*. They know the surface of the problem very well — the symptoms and the cost — but not the underlying cause, or what the technology can do about it. That gap is our value. Not just doing what they asked, but (1) finding the problem behind the ask, (2) designing what actually solves it, and (3) explaining the why and the what in terms they understand. Say this out loud in the close — it turns one fraud example into how you operate every day.

**Story: never-delivered abuse — moving fraud detection from reactive to proactive.** One insight: our model was accurate, but it sat too late in the flow to stop the loss. About 2 minutes, result first:

*Result first*

> At DoorDash, I moved one of our biggest abuse problems, false "never delivered" claims, from reactive to proactive: instead of judging the claim after the loss, we stopped it before it happened. Never-delivered refund requests dropped [X%], [saving $Z]. Nobody asked for this. The ask was a more accurate model. What I saw was that accuracy wasn't the bottleneck; where the model sat in the flow was.

*Situation*

> Some customers falsely claim an order never arrived, to get a refund, a credit, or a chargeback. Our model scored the claim when the customer asked for the refund.

*What I saw*

> But by then, the damage was already done either way. If we wrongly denied a real customer, we lost a customer. If we approved an abuser, we lost money. The model was stuck choosing between two bad outcomes, and no amount of accuracy would get it out of that.

*Action*

> So I proposed moving it upstream, to when the order is placed. If the model flags a user as likely to file a false never-delivered claim, we ask them to enter a verification code when they receive the order. Honest customers barely notice, and once you've entered the code, you can't claim the order never arrived.

*The hard moment*

> [Fill in. Likely: product worried a verification code would add friction for good customers. You answered it by only applying it to high-risk users with a conservative threshold, and testing the impact on conversion and satisfaction before rolling out.]

*Result*

> Never-delivered refund requests dropped [X%], [saving $Z], with [no measurable impact on conversion / good-customer complaints]. And support no longer had to make as many no-win calls on refunds.

*Close*

> The request was "make the model better." The real fix was moving the decision earlier, from reacting after the loss to preventing it.
>
> And that's really my day-to-day job. Business partners know the surface of the problem better than anyone: where it hurts, and how much it costs. What they usually can't see is the underlying cause, and what the technology could do about it. That's what I bring. So my job isn't to just build what they asked for. It's to find the real problem behind the ask, turn it into a solution that actually solves it, and explain the why and the what in their terms, so they can see it's better than what they asked for. Here, that meant telling the business and product teams: fewer good customers wrongly denied, and less money lost.

**Why it works:**

- **Unprompted:** the ask was a better model; you saw the problem was *where* the model sat. Spotting the question behind the question is the ownership signal.
- **Ask → real solution, explained in their terms:** the close generalizes it to your daily job.
- **Stakeholder empathy:** you name the cost on both sides — losing good customers vs. losing money — not just fraud loss.
- **Crosses team boundaries:** the delivery flow belonged to product. You drove change in a system you didn't own.
- **Checkr link:** a reactive decision about a person, made after the fact, is costly whichever way you get it wrong. Better to design the flow so fewer hard calls are needed.

**Numbers to fill in:** the drop in never-delivered refund requests (and dollars saved); share of users who got the verification step; any impact on conversion or good-customer complaints.

**Likely follow-ups:**

- "How did you spot it?" — [Fill in: e.g. you looked at the cost of both wrong answers at refund time, and saw that no model accuracy could remove it.]
- "Who did you have to convince, and how?" — [Product, for the verification code; the business team.] Frame it in their terms: fewer good customers wrongly denied, less money lost, fewer no-win refund calls.
- "Didn't the verification code hurt good customers?" — Only high-risk users saw it, with a conservative threshold, and [what you measured].
- "Why hadn't anyone done this before?" — Each team optimized its own piece: support the refund decision, us the model. Nobody owned the whole flow end to end.

**Backup — driver time abuse** (same reactive → proactive pattern, if he wants a second example): a low-recall "late" filter sat in front of an accurate attribution model, so most deliberately late orders never reached the model — "a perfect model can't catch what it never sees." You proposed to the business team that owned the filter that we consolidate the two: every order later than our ETA estimate goes straight to the attribution model. [Result: e.g. caught Y% more abusive late deliveries.]

## 2. Technical standards: the speed vs. scalability trade-off

**What he's looking for:** a real decision-making framework — how you justified the call to the team and stakeholders, what you optimized for, and the downstream consequences.

**Story: unifying and automating the fraud model pipeline** (chargeback automation + foundation over firefighting). About 2 minutes; the model answer from Mock 1:

*Set the context (one or two sentences — he hasn't heard this story yet)*

> At DoorDash, every stakeholder request had become its own fraud model, built by hand in notebooks, so each new model took six to eight weeks, and most of that was plumbing. Even updating a model we already had took about two months, because every iteration was done by hand: pulling the data, training, and evaluation were the same steps every time, but someone did them manually. Counting the release, a full cycle from starting an iteration to having it live in production took several months. I had to decide whether to keep shipping models that way, or slow down to unify and automate.

*Name both options*

> It was a real trade-off, and I didn't take it lightly. The fast option was to keep going the way we were: take each stakeholder request, build a model, ship it. Stakeholders would have seen new models sooner. The scalable option was to build every model in a more standard, more automated way, so that each next iteration would take less time, and step by step, automate the whole model pipeline.

*The framework: three questions*

> I chose scalability, and I used three questions to decide.
>
> **First, is this cost one-time or repeating?** Fraud drifts constantly, so we retrain all the time. Every manual step and every duplicate model wasn't a one-time cost; we paid it again on every iteration. Repeating costs are where infrastructure pays off.
>
> **Second, what does waiting actually cost?** Pausing cost us a few model releases for one quarter. Staying manual cost us six to eight weeks on every model, indefinitely. One cost is bounded, the other isn't.
>
> **Third, can we reverse it if I'm wrong?** I made sure we could still push a model out the old way in an emergency, so the bet didn't lock us in.

*Justifying it to stakeholders*

> That was the hard part, because they wanted models, not infrastructure. I didn't argue engineering excellence; I argued their problem. I showed them where the six to eight weeks actually went, and most of it was plumbing, not modeling. Then I framed it as: slow iteration means we're fighting this month's fraud with last quarter's model. And I didn't ask them to accept zero output on faith: I kept [one high-priority model] shipping in parallel, and gave them a date when the new pipeline would start paying back.

*Justifying it to the team*

> That was easier. The pipeline removed exactly the work they hated most. But I was explicit that the next quarter would feel slower before it felt faster, so nobody was surprised.

*Consequences, good and bad*

> The good: iteration went from six to eight weeks to two to three, experiments from two to three months to four to six weeks, and we freed two to three engineers to work on new fraud areas.
>
> The cost: standardizing reduced flexibility. About 20% of our models didn't fit the standard path, so we built escape hatches where engineers could plug in custom steps instead of forcing everything through one pipeline. And for that first quarter, [one stakeholder team] had to wait longer than they wanted, and I owned that conversation with them directly.

*Close: you don't always pick scalability*

> I don't always pick scalability, though. When the cost is one-off, the window is closing, or we're still learning what we need, I pick speed. During an account takeover escalation, for example, the right call was a fast, contained fix first, with the long-term system going through planning afterward.

**Why it works:** it names both options up front; the three questions are the "decision-making framework" Gio asked for; the stakeholder pitch is in business terms, with something still shipping during the build; it gives good *and* bad consequences and how you handled the bad; and it ends by showing you don't always choose scalability, which sets up the speed question that comes next.

**The framework, in one line for the room:** *"I choose speed when we're still proving the bet, the cost is one-off, or the window is closing. I choose scalability when the bet is proven, the cost repeats, and the delay is bounded. Either way, I never cut corners on the one thing that decides success."* Full framework, with the four questions and your stories mapped: [`leadership/speed_vs_scalability.md`](../../leadership/speed_vs_scalability.md).

**Show you don't always pick scalability.** Have one sentence ready: the restaurant lending pilot (Story 11), where the bet was unproven and leadership wanted a pilot in a month, so we simplified everything except the underwriting model. Or the ATO escalation, where the right call was a fast, contained fix first. Judgment means knowing which situation you're in.

**Backup story: foundation over firefighting** (several teams wanted bespoke models; you built shared features and serving first). Use it if he wants a second example or a roadmap-level trade-off. See `leadership/stripe_strategy_and_execution/13_foundation_story.md` — its blanks need filling first.

**Likely follow-ups:**

- "What would have made you choose speed instead?" — The one-line framework above, reversed.
- "What did the team think?" — [Fill in: who pushed back, and what you said.]
- "What broke afterward?" — The flexibility cost, and the escape hatches you built.

**Full STAR version, if he wants the whole story** (moved from the Ownership section):

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


## 3. Relentless execution: the highest-tempo project

**What he's looking for:** what speed actually looked like — told with energy and specifics — and a concrete moment where **you personally** unblocked the team, technically, organizationally, or cross-functionally. Taylor's warnings: don't pick a "fast project" that was really normal pace, and **never blame slowdowns on other teams.**

**Story 11: restaurant lending pilot** (full story: `star_stories/story_11_restaurant_lending_pilot.md`). About 2 minutes, result first:

*Result first*

> In the second half of 2025, leadership asked my team to turn a six-month plan for in-house restaurant lending into a pilot in one month. We launched on time: 20 restaurants, $20 to 30K each, and after six months 19 of 20 had paid back in full. That proved we could pick restaurants that needed the money and would repay, and get it back, and this year the program grew to $20 million.

*Situation*

> Before, we used a vendor, Parafin, to underwrite and fund loans to restaurants, and we took a revenue split. We wanted to own it. Our plan covered everything: the merchant UI, how we communicate with restaurants, the underwriting models, and loan performance monitoring.

*The ask, taken seriously*

> Leadership loved the plan but wanted a pilot in one month. My first instinct was that it wasn't realistic. But when we analyzed the ask, they had a point: we were building to scale before we'd proven the core bet: that we could pick restaurants that needed the money and would repay, and actually get the money back. A pilot would tell us that much faster.

*Simplify everything that can be simplified*

> So I re-scoped around one question: what's the minimum we need to lend to about 20 restaurants and prove we can choose the right ones and collect? Once the goal was that clear, we knew which steps we could skip or simplify and which we had to strengthen. I split the work into two tracks, backend, and UX plus communication, and both took the simplest version that worked for a pilot. We cut the merchant-facing UI and the automated outreach completely: neither affected whether we picked the right restaurants. Instead, we selected restaurants ourselves with the risk underwriting model.

*Concentrate force on what can't be simplified — personally unblocking*

> The one thing we couldn't simplify was the underwriting risk model. You can't lend money without deciding who'll pay it back. That was the critical path, so I took it on myself: I pulled the data together and built a quick-and-dirty model end to end in one week. I validated it against Parafin's historical loans, where we already knew which restaurants had repaid, and it was good enough for a small, controlled pilot, and the model chose the 20 restaurants. I contained the risk three ways: very conservative thresholds, so only the best of the best qualified; a manual check on every loan before any money went out; and small loans, $20 to 30K. The manual checks didn't block a single loan. Right after launch we built a monitoring dashboard to track repayment.

*Close*

> What I took from it: under a hard deadline, first get clear on the main goal. Then you know which steps can be skipped and which have to be strengthened — put your strength there, and give everything else the simplest version that works. Speed came from not treating every part of the plan as equally important.

**Why it scores on every warning:**

- **Real tempo with specifics:** six months → one month; the model in one week; 20 loans; 6-month repayment; $20M a year later.
- **Personally unblocking:** you built the critical-path model yourself, and you re-scoped the whole plan.
- **No blame:** you treat leadership's aggressive ask as right once you analyzed it, rather than pushing back on it.
- **Bonus:** it's your *speed over scalability* example — the counterpart to the chargeback pipeline in section 2, which shows the framework cuts both ways.

**Likely follow-ups:**

- "How did you know a one-week model was good enough?" — We validated it on Parafin's historical loans: we had real outcomes for restaurants that had already borrowed through Parafin, so we backtested the model on whether those restaurants actually repaid. [Fill in the metric and result, e.g. AUC, or default rate among the top-scored restaurants vs. all Parafin loans.] On top of that, the conservative threshold meant we only lent where the model was most confident.
- "What did you cut, and what did it cost later?" — The merchant UI and automated outreach; we picked restaurants with the risk model instead. Monitoring was deferred to just after launch, not dropped. [What you built when scaling to $20M.]
- "Isn't a one-week model risky when money is involved?" — Yes, so I capped the risk three ways: very conservative thresholds (best of the best only), a manual check on every loan before disbursement, and small loan sizes. The manual checks never blocked a loan — the model's picks all held up.
- "Why build the model yourself instead of assigning it?" — It was the critical path and the riskiest piece; doing it myself removed a hand-off, and [the team productionized it afterward].
- "What about the one restaurant that didn't repay?" — [What you learned.]

**Backup — Story 10: embedding the risk score into assignment.** Use it if he wants a cross-team unblocking example.

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
| **Your AI dev setup** | Three layers — **build, operate, grow**. Script below the table. |
| **Last thing you shipped with meaningful AI involvement** | **The restaurant lending pilot** — AI built the model in a week; the model made the picks; a human checked every loan. Backup: the agentic support system. Script below the table. |
| **How AI changed your own work** | Three shifts — **the bottleneck moved to design and checking, overhead time went to people, decisions got better and faster**. Script below the table. |
| **Helping your team adopt AI** | A playbook, not a mandate — **lead by example → prove it on painful work → peer demos → team conventions + harness → ownership rule**. Script below the table. |
| **Opportunities beyond code generation** | Three layers you've built — **AI as the product, AI for data, AI for how the team operates** — then the Checkr angle. Script below the table. |
| **When *not* to use AI** | Three cases — **a simpler tool works, the constraints rule it out, or the decision belongs to a human**. Script below the table. |
| **What most people get wrong about AI** | Two things — **treating a demo as a system**, and **thinking AI removes judgment** (it moves it). Script below the table. (Added from the Taylor call transcript.) |

### Tier 1 — your setup

**"What's your AI dev setup?"** (~45 seconds)

> I think of it in three layers. **Building:** a coding agent is my daily driver — it writes code, does a first-pass code review, and helps me study an unfamiliar codebase fast. I also use it to organize knowledge: turning design discussions and docs into something the team can find later. **Operating:** an AI notetaker runs in every meeting and summarizes it, so I'm in the conversation instead of typing. And at the end of each day I use AI to go through my Slack and email and give me a summary: what I finished, what I missed, and what I need to do tomorrow. **Growing:** I use it as a coach. Before a hard conversation — a conflict, difficult feedback, a cross-team disagreement — I talk it through and rehearse it. And when I'm under a lot of pressure, I use it to step back and sort out what's really bothering me before I react.

Notes on delivery:
- Lead with the build layer; that's what the question literally asks. The other two layers are what make the answer memorable — most candidates stop at code.
- On the stress point, keep the framing as *stepping back before I react*. It shows self-awareness and judgment; no need to go further than that in an interview.

**"When did you last ship something where AI was meaningfully involved?"** (~45–60 seconds; model answer — fill the brackets)

> The restaurant lending pilot, late last year. Leadership wanted a one-month launch, and the critical path was the underwriting model: deciding which restaurants we could safely lend to.
>
> **AI is how I built it in one week instead of a month or more.** I used a coding agent to [pull and join the restaurant data, build the feature pipeline, and write the backtest against Parafin's historical loans]. That's the work that usually eats the time. It left me free to focus on the parts that needed judgment: which signals actually predict repayment, where to set a very conservative threshold, and whether the backtest results held up.
>
> **And I kept the human in the loop where it mattered.** The model picked the 20 restaurants, but a person checked every loan before any money went out.
>
> **The result:** 19 of 20 restaurants repaid in full. That proved we could pick the right restaurants and collect, and this year the program grew to $20 million.

Why it works: leads with the business outcome, with AI as the reason for the speed; shows AI on the plumbing and you on the judgment calls; "a person checked every loan" echoes your when-not-to-use answer and is Checkr's world. It's the same story as your tempo answer from a different angle — if Gio says "you mentioned that," switch to the backup.

**Backup:** the agentic support system, where AI *is* the product — an agent handles customer order issues end to end, with real-time RAG over past support cases. [Add a result: resolution rate, cost per ticket, or tickets handled without a human.]

To fill in: the real AI role in the one-week build (the bracket is a guess); a result for the support system if you want the backup ready.

### Tier 2 — your own work

**"How has AI changed the way you work?"** (~45–60 seconds; model answer — fill the bracket)

> It changed where my time goes, in three ways.
>
> **First, the bottleneck moved from writing code to deciding what to build and checking it.** My team writes nearly all its code with AI now, so implementation isn't the slow part anymore. I write fewer PRs, and I spend that time on design, specs and reviews. A clear spec is now the highest-leverage thing I write, because it's effectively the prompt for the engineers and their agents. And I put more into what we call the harness: tests, evals and guardrails that tell us whether the output is actually right.
>
> **Second, I spend less time on overhead and more time on people.** AI takes my meeting notes, and every evening it summarizes my Slack and email: what I finished, what I missed, what's next. That gives me back [an hour or so] a day, and most of it goes to one-on-ones, unblocking people, and cross-team work.
>
> **Third, I make better decisions, faster.** Before a big call, I give AI a clear, scoped question and have it pull together the evidence and the trade-offs. I read it, learn from it, and make the decision myself. I also rehearse hard conversations with it before I have them. So I walk in better prepared, but the judgment is still mine.

Why it works: about impact, not tools; shows AI used at a manager's level (specs, reviews, decisions, people); consistent with your other answers — the harness (adoption), "clear, scoped questions, and I make the call" (when not to use AI), rehearsing hard conversations (setup).

Watch the overlap with the setup answer: if Gio asks both back to back, keep this one to the *change* — the first two sentences of each shift.

To fill in: roughly how much time AI saves you a day; use a number only if it's real, otherwise "a meaningful chunk of every day."

### Tier 3 — your team and products

**"How have you helped your team adopt AI?"** (~60 seconds; model answer — fill the brackets)

> My team now writes nearly all its code with AI, but it didn't start that way, and I didn't get there by mandating tools.
>
> **I started by using it myself, visibly.** I used a coding agent for my own prototypes and design docs, and shared what worked and what didn't. That made it safe to try, because people could see their manager learning too.
>
> **Then I picked the work people hated most and proved it there,** [e.g. writing data pipelines, test cases, boilerplate]. Once a couple of engineers got real wins, I had them demo their workflow to the team. Engineers trust other engineers more than they trust a mandate.
>
> **Then we made it a team practice, not an individual habit.** We wrote shared conventions: instruction files in each repo, how to scope a task for an agent, and how we review AI-written code. And we invested in what I call the harness: tests, evals and guardrails, so we could trust the output at volume.
>
> **The one rule I held firm on was ownership.** If your name is on the PR, you own every line, generated or not.
>
> **The hard part was [e.g. a senior engineer who didn't trust the output].** I didn't push. I paired them with [someone] on a task where AI clearly helped, and kept the review bar high, which is what they actually cared about.
>
> **The result:** [we went from X% to nearly all code AI-written in N months], and [cycle time / PRs per engineer went from A to B]. More importantly, the team's time moved from typing code to design, research and evaluation, which is where the real problems are.

Why it works: it's a concrete playbook; it has a hard moment; it ends on business impact; and the ownership rule echoes the Checkr ML EM posting almost word for word ("Keep ownership of every output. As generated code becomes cheaper, raise the bar on judgment").

To fill in: the first workflow you proved it on; who resisted or what the real friction was (trust in quality, review load, cost); one before/after number; and confirm the lead-by-example and demo steps match what actually happened.

**"Where do you see AI improving products or engineering systems, beyond code generation?"** (~60 seconds; model answer)

> Code generation is the most visible part, but in my experience the bigger wins are in three other places, and I've built all three.
>
> **First, AI as the product itself.** My team built an agentic support system: when a customer has a problem with an order, like a missing item or a spilled drink, an agent handles the case end to end, with real-time RAG over past support cases. That changes the cost of support, not just the speed of engineering.
>
> **Second, AI for data, which is the most underrated one.** In fraud, our slowest input was always labels. We built an LLM labeling agent with batch RAG that creates training labels for our fraud models. Better labels, faster, means every downstream model gets better. That's leverage code generation can't give you.
>
> **Third, AI for how the team operates.** Summarizing investigations so analysts spend their time deciding, not reading. Turning meetings, docs and decisions into knowledge the team can actually find. Triaging incidents with runbooks. Each one removes reading and searching time from expensive people.
>
> At Checkr I'd expect the same shape. AI can do the heavy reading: parsing messy records, matching them to the right person, summarizing a case for a reviewer. Then people make the decision, because it affects someone's job.

Why it works: every example is something you built; each layer is framed by business impact (support cost, model quality, expensive people's time); "AI for data" is a distinctive point that shows ML depth; the Checkr close ties back to your when-not-to-use answer — AI reads, humans decide.

To check: what the labeling agent labels and any result (volume, cost, model lift); whether your team actually did investigation summaries or incident triage — if not, swap in your meeting summaries and daily Slack/email digest; the Checkr close is deliberately general — name a specific Checkr AI product if you know one.

### Tier 4 — judgment

**"When would you *not* use AI?"** (~60 seconds)

> Three cases. **First, when a simpler tool solves it.** If heuristic rules or traditional ML can handle the problem, I don't reach for an LLM or an agent. Most of fraud detection is tabular data, and gradient-boosted models find those patterns better and cheaper than an LLM.
>
> **Second, when the engineering or cost constraints rule it out.** If I need a real-time decision in under a second, like scoring a transaction at checkout, or I need a deterministic answer that's the same every time, an LLM is the wrong tool.
>
> **Third, the big decisions — direction, strategy, a high-stakes call about a person — stay with humans.** AI is great at analyzing the trade-offs, but the decision itself is ours. The way I use it there is as a research tool: I give it a clear, well-scoped question, and it finds me the material, the evidence, and the explanation. Then I read it, learn from it, and make the call myself. In the lending pilot, the model picked the restaurants, but a person checked every loan before any money went out.

Why it works: it shows you use AI with judgment, not by default; the examples come from your own domain (sub-second fraud scoring, tabular data, lending); and the third case — humans own consequential decisions about people — is exactly Checkr's world, where a background check affects someone's job.

**"What do most people get wrong about AI today?"** (~45–60 seconds; model answer — fill the bracket)

> Two things.
>
> **The biggest one is treating a demo as a system.** It works on ten examples, so people ship it, with no evals, no monitoring, and no idea how it fails. I've seen this myself: [e.g. our support agent looked great in testing, then in production it confidently gave wrong answers on an edge case we hadn't covered]. What fixed it wasn't a better prompt. It was building an eval set from real cases and monitoring live outputs. With AI, building it is the easy part; knowing whether it's right is the real work.
>
> **The second is thinking AI removes the need for judgment.** It actually moves the judgment somewhere else. Generating code or analysis is now cheap, so the value is in asking the right question and checking the answer. AI does best with a clear, well-scoped question. Give it a vague one and you get a confident, vague answer. And the teams that get burned are the ones that lower their review bar as output goes up, when they should be raising it.
>
> So the way I'd put it: AI makes output cheap, which makes judgment more valuable, not less.

Why it works: practical, not hype or doom — a heavy but careful user; the personal example shows you learned it firsthand; "clear, well-scoped questions" ties to your when-not-to-use answer and "raise the review bar" to your adoption answer's ownership rule; the closing line echoes the Checkr posting ("As generated code becomes cheaper, raise the bar on judgment").

To fill in: one real case where an AI system looked right but failed — support chatbot, RAG, or the labeling agent — what broke and what you did.

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

### Mock 1 — speed vs. scalability follow-up

**Question:** "Walk me through that decision. How did you decide that was the right call, and how did you justify it to your team and your stakeholders? What were you optimizing for, and what were the downstream consequences, good and bad?"

You asked for a model answer instead of answering live. It's now the script in the Technical standards section. Next time: answer it out loud yourself first, then compare against the script.
