# Story 11: Restaurant Lending Pilot — Six-Month Plan to One-Month Launch

**Use for:** highest-tempo project, speed over scalability, executing under a tight deadline, simplifying scope, personally unblocking the critical path, ambiguity.

**Situation**: In the second half of 2025, DoorDash offered restaurants loans to help them grow, through a vendor, Parafin. Parafin did the underwriting and funded the loans, and we took a revenue split. We wanted to bring lending in-house: own the underwriting, choose which restaurants to lend to, and keep the economics.

My team wrote a six-month plan covering the full system: the merchant-facing UI, how we'd communicate with restaurants, the risk underwriting models, and loan performance monitoring. Leadership loved the proposal, but asked us to launch a pilot within **one month**.

**Task**: Cut a six-month plan down to a pilot we could ship in a month. The pilot had one goal: prove we could pick restaurants that genuinely needed the money and were willing and able to repay, lend to them, and get the money back. The part that couldn't be faked was the selection: deciding who we could safely lend to.

## Action

### Take the ask seriously, not defensively
- My first instinct was that one month was unrealistic. But when we analyzed it, leadership had a point: the six-month plan was built to scale before we had proven the core bet — that we could pick restaurants that needed the money and would repay, and actually get the money back. A pilot would tell us that much faster.
- So we redefined scope around one question: *what's the minimum we need to lend to a small number of restaurants and prove we can choose the right ones and collect?*
- Once the goal was that clear, every step in the plan sorted itself into one of two buckets: **steps we could skip or simplify**, because they didn't affect whether we picked the right restaurants and got paid back, and **steps we had to strengthen**, because they did. That clarity is what made one month possible.

### Simplify everything that could be simplified
- We grouped the work into two tracks: **backend** (loan flow, disbursement, repayment), and **user experience and communication** (how restaurants find, accept, and understand the offer).
- Both tracks dropped the scalable versions for the simplest thing that worked for a pilot of about 20 restaurants. We **cut the merchant-facing UI and the automated outreach** entirely. Neither affected whether we picked the right restaurants. Instead of restaurants applying through a product flow, we **selected restaurants ourselves using the risk underwriting model** and reached out to them directly.

### Concentrate force on the one thing that couldn't be simplified
- The real blocker was the underwriting risk model. You can't lend money without deciding who's likely to pay it back, and there was no shortcut there.
- I took it on personally. I pulled the data together quickly and built a quick-and-dirty model end to end in **one week**. I validated it against Parafin's historical loans — real repayment outcomes for restaurants that had already borrowed — and its performance was good enough for a small, controlled pilot.
- The model did the selection, with three layers of protection:
  - **Very conservative thresholds:** we only lent to the best of the best restaurants by risk score.
  - **A manual check on every loan** before any money went out. In the end, the manual checks didn't block a single loan: every restaurant the model picked passed.
  - **Small loan amounts:** $20–30K each, so any single mistake was cheap.
- Monitoring was the one thing we deferred, not dropped: we **built a loan performance monitoring dashboard right after launch**, so we were tracking repayment from early on.

## Result
- We launched the pilot within the month: 20 restaurants, each receiving **$20–30K**.
- After six months, **19 of 20 restaurants had fully repaid**. Only one hadn't.
- The pilot proved we could build our own strong underwriting model. On the back of it, this year the program grew from about [$1M — confirm: 20 × $20–30K is $400–600K] to **$20M** in loans.

## Key Takeaway
Under a hard deadline, I first get clear on what we're really trying to prove. Once the main goal is clear, it's obvious which steps can be skipped or simplified and which have to be done better than planned. I put the team's strength on the second group. Everything else gets the simplest version that works. Speed came from refusing to treat every part of the plan as equally important, not from working harder on all of it.

## Short version (~2 minutes, result first)

> In the second half of 2025, leadership asked my team to turn a six-month plan for in-house restaurant lending into a pilot in one month. We launched on time: 20 restaurants, $20 to 30K each, and after six months 19 of 20 had paid back in full. That proved we could pick restaurants that needed the money and would repay, and get it back, and this year the program grew to $20 million.
>
> Before, we used a vendor, Parafin, for underwriting and took a revenue split. We wanted to own it, and our plan covered everything: the merchant UI, communication, underwriting models, and monitoring. Leadership liked it but wanted a pilot in a month. When we looked hard at the ask, they were right: we were building to scale before proving the core bet: that we could pick the right restaurants and get our money back.
>
> Being clear on that goal told us what to skip and what to strengthen. So I split the work. Backend, and UX plus communication, both cut to the simplest version that worked for 20 restaurants. We cut the UI and the automated outreach completely, and picked the restaurants ourselves with the risk model. The one thing we couldn't simplify was the underwriting model, so I took that on myself: I pulled the data and built a quick-and-dirty model end to end in one week, and we contained the risk three ways: very conservative thresholds, so only the best of the best qualified; a manual check on every loan before the money went out; and small loans. The manual checks didn't block a single loan. Right after launch, we built a monitoring dashboard to track repayment.
>
> What I took from it: under a deadline, first get clear on the main goal. Then you know which steps you can skip and which you have to strengthen — put your strength there, and give everything else the simplest version that works.

## Follow-up questions to prepare

- **"How did you know a one-week model was good enough?"** We validated it on Parafin's historical loans: we had real outcomes for restaurants that had already borrowed through Parafin, so we backtested the model on whether those restaurants actually repaid. [Fill in the metric and result, e.g. AUC, or default rate among the top-scored restaurants vs. all Parafin loans.] On top of that, the conservative threshold meant we only lent where the model was most confident.
- **"What did you cut, and what did that cost later?"** The merchant UI and automated outreach — we selected restaurants with the risk model and contacted them directly. Monitoring we deferred to just after launch, not dropped. [Fill in: what you built when scaling to $20M — presumably the UI and outreach came back then.]
- **"Who disagreed with the one-month timeline?"** [Fill in: did anyone on the team push back, and how did you bring them along?]
- **"Why did you build the model yourself instead of assigning it?"** It was the critical path and the riskiest piece; doing it myself meant no hand-off delay, and I [handed it to the team to productionize afterward].
- **"What happened with the one restaurant that didn't repay?"** [Fill in: what you learned and whether it changed the model.]
