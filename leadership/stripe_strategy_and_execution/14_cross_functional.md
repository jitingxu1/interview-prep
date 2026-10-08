# Q14. How do you work with cross-functional teams?

[← Round 2 index](README.md)

This question comes with a specific second half: *which teams?* They want to hear that you have operated with product, data science, design, legal, compliance, or infra — not only with other engineers. Name the functions concretely.

**The script:**

> The thing I've learned to do first is establish what each side is accountable for, in writing, before the work starts. Most cross-functional friction isn't disagreement — it's two teams assuming someone else owns the same thing, discovered three weeks late.
>
> Concretely, for each partnership I want three things settled early: what we're each delivering, the interface between us, and who decides when we disagree. If we can't name the decider, that's the first problem to solve.
>
> With product specifically, the pattern that works for me is getting involved in problem definition rather than receiving requirements. If the first time my team sees something is a spec, we've already lost the chance to say "there's a much cheaper version of this."
>
> On communication, I over-invest in the boring parts: a shared written status that both sides can read without a meeting, and surfacing slippage the week I see it rather than the week it's due. The fastest way to lose a partner team's trust is for them to find out late.

**Your version is below** — see "Your version: S&O, Product, data science, backend, infra." **Fill in:** which functions you actually worked with and one specific example per function you want to claim. For a data/ML manager the strong set is product, data science or analytics, platform or infra, and whoever owns the risk side — legal, compliance, or ops. Stripe cares about that last one.

**How they grade it:**

| Signal | Strong | Red flag |
| --- | --- | --- |
| Range | Names specific functions — product, DS, infra, legal or compliance | Only other engineering teams |
| Ownership clarity | Settles deliverables, interface, and decider up front | Discovers overlapping ownership late |
| Early involvement | Shapes the problem with product before the spec | Receives requirements and executes |
| Transparency | Surfaces slippage the week it is seen | Partners find out at the deadline |
| Self-ownership | Names their own part in a partnership that went badly | The other function was the problem |

**Follow-ups to prepare:**

- "Tell me about a cross-functional partnership that went badly. What was your part in it?"
- "How do you handle a partner team that keeps missing its commitments to you?" (Mechanism answer: make the dependency visible to both managers early, build a fallback, and escalate jointly rather than complaining upward.)
- "How do you work with a PM you disagree with about priorities?"
- "How much do you shield your engineers from stakeholder noise versus exposing them to it?" (Good answer: shield from churn, never from context — engineers who talk to users make better decisions. Full answer in "Shield from churn, never from context" below.)

## Your version: S&O, Product, data science, backend, infra

Your two most important partners are **S&O (Strategy & Operations)**, who own the business metrics, and **Product**, who own the features. Say "Strategy & Operations — the business team that owns fraud-loss targets" once in the interview; Stripe interviewers may not know the DoorDash term.

### How they'll dig in

Expect this question to go several layers deep. Most candidates handle layers 1–2 and stall at 4–7 — prepare those most.

| Layer | What they ask | What they're testing |
| --- | --- | --- |
| 1. Range | "Which teams do you work with?" | Have you worked beyond engineering? |
| 2. Roles | "What does each one own? What do you own?" | Do you understand how responsibility is divided? |
| 3. Mechanism | "How do you plan together? How often? What gets written down?" | A system, or just good relationships? |
| 4. Conflict | "When S&O and Product want different things, what happens?" | Can you manage tension between partners? |
| 5. Decision rights | "Who makes the final call?" | Is it clear, or do things get stuck? |
| 6. Specific story | "A time it went badly — what was your part?" | Self-awareness, owning your mistakes |
| 7. Exact words | "What did you actually say to the PM?" | Real experience vs. a rehearsed framework |

### How they evaluate you

At Stripe an EM is expected to be a **business partner**, not someone who takes requests. They're judging whether you:

1. **Understand the business, not just the tech** — fraud loss, conversion, and customer friction, in S&O's language.
2. **Shape the work, not just deliver it** — help define the problem, offer cheaper or better options.
3. **Make tradeoffs explicit** — when partners disagree, put the tradeoff on the table with numbers.
4. **Keep decision rights clear** — know who decides what, so nothing gets stuck.
5. **Build trust through reliability** — partners hear about slippage early, from you.
6. **Own your part when it goes wrong** — "here's what I did wrong," without blaming the other team.

### Who owns what

| Partner | What they own | What you own with them | Where the tension usually is |
| --- | --- | --- | --- |
| **S&O** | Business metrics — fraud loss, loss rates, targets; operational policy | Turning metric targets into model goals; showing what's technically possible | They want loss down fast; ML takes time. They may want quick rules where you'd prefer a model |
| **Product (PM)** | Features, user experience, roadmap priorities | Feasibility, cost, cheaper alternatives, sequencing | New features vs. foundation and tech debt; friction for good users |
| **Data science** | Analysis, experiment design, metric definitions | Agreeing how success is measured before launch | Who owns which analysis; metric definitions drifting |
| **Backend** | The systems your models plug into (assignment, checkout) | Integration, latency SLAs, who's on call for what | Their latency and reliability vs. your new model inputs |
| **Infra** | Compute, platform, serving infrastructure | Capacity; getting your needs onto their roadmap | Their priorities aren't yours, and you depend on them |

**The core relationship — you, S&O, and Product.** This is where you actually plan, so describe it in depth:

- **S&O brings the "why" and "how much"** — loss trends, business targets ("reduce fraud loss by X%").
- **Product brings the "what"** — the features and user experience that need to change.
- **You bring the "how" and "what it costs"** — technical options, capacity, timelines, and the cheaper version.

> On my team, planning is a three-way partnership. S&O owns the business metrics and brings the targets, Product owns the features and user experience, and I own the technical approach and what it costs. Roadmap and planning happen with all three of us in the room, so nobody gets handed a plan they didn't shape.

### Decision rights: who decides when we disagree

**It depends on what the disagreement is about.** The rule of thumb: **whoever owns the outcome decides; everyone else gives input.** The point of the script line is that you agree on this *before* the work starts, so when a disagreement comes up, nobody has to argue about who gets the final say.

| What you disagree about | Who decides | Example |
| --- | --- | --- |
| Business target — how much fraud loss to cut, how much is acceptable | **S&O**, with my input on feasibility | S&O wants a 15% reduction; you think 10% is realistic. You bring evidence; S&O sets the target |
| Feature scope and user experience | **Product**, with my input on cost | Product wants a verification step for flagged users; you think it adds friction. You raise it; Product decides |
| Technical approach — model design, architecture, how to build it | **Me** and my team | Product suggests a rules-based quick fix; you think a model is better. You decide, and explain the tradeoff |
| Their system — assignment logic, their latency limits | **The owning team** (e.g. Backend) | The assignment team won't accept more than 50 ms added latency. Their call; you work within it |
| Launch go/no-go | **Joint**, by rules agreed *before* the launch | "Ship if fraud loss drops at least 8% and assignment time degrades no more than 2%." The data decides, not a debate |
| A real conflict nobody can settle | **Shared leadership**, escalated jointly | S&O and Product both own part of it and still disagree. Escalate together with one written tradeoff |

**Three ways to make it work:**

1. **Agree on the decider up front.** At kickoff, ask: "If we disagree on X, who makes the call?" It feels slightly awkward, but far easier than settling it mid-argument. Write it in the project doc.
2. **Turn decisions into pre-agreed rules where you can.** Launch criteria are the best example: when the rule is set before anyone is invested in the result, the data settles it. Story 10 did exactly this — assignment metrics as must-hold guardrails, fraud loss as the metric to improve, and a kill switch.
3. **When it truly can't be settled, escalate together.** Not each to your own boss — one shared doc with both views and the tradeoff, brought to the common manager together. Leadership gets a clear decision to make, not two competing stories.

**Two nuances:**

- **"Decides" doesn't mean "ignores others."** The decider should hear everyone's input, especially from whoever disagrees. Often the best outcome is that your input changes their decision even though the call is theirs.
- **Once it's decided, everyone commits** — including you when it went against you. Same disagree-then-commit idea as Q12.

> Whoever owns the outcome decides: S&O owns the business target, Product owns the feature and the user experience, and I own the technical approach. For launches, we agree the success criteria and guardrails beforehand, so the data decides, not a debate. And if S&O and Product genuinely can't agree, we escalate together with one written tradeoff, not separately.

**Likely follow-up:** "Tell me about a time you disagreed with the decider and lost." Have an example where S&O or Product made a call you disagreed with — how you raised it, how you committed, and ideally what you learned or what the result showed.

### Operating rhythm

Adjust to what you actually do:

| Cadence | What happens | With whom |
| --- | --- | --- |
| Half or quarterly planning | S&O shares targets and loss trends; Product shares priorities; I bring capacity and options. We agree goals and a roadmap, with a not-doing list | S&O + Product, DS input |
| Weekly | Metric review (is fraud loss moving?), roadmap status, risks | S&O + Product |
| Before each launch | Success metrics, guardrails, experiment design, rollback criteria | DS, S&O, Product, Backend |
| Ongoing | Written status anyone can read; slippage flagged the week I see it | Everyone |
| As needed | Dependency check-ins on capacity and integration | Infra, Backend |

### Your stories, mapped to functions

| Function | Story | What it shows |
| --- | --- | --- |
| S&O, Product, legal, business | **Story 2** — phased fraud model rollout: modeled fraud prevented vs. user friction; 40% of fraud caught at under 2% false positives | Making a tradeoff explicit across several functions |
| Backend (assignment team) | **Story 10** — risk score embedded in assignment: built trust, helped rebuild their simulation, primary/guardrail metrics; 12% fraud loss reduction, assignment time unchanged | Winning over a skeptical partner team |
| Product teams | **Foundation story (Q13)** — many one-off model requests turned into a shared platform | Shaping the roadmap with Product |
| Data science | [Fill in — e.g. agreeing experiment design or metric definitions] | Agreeing how to measure success |
| Infra | [Fill in — e.g. getting serving capacity or a platform feature onto their roadmap] | Managing a dependency you don't control |

Have one deep story each for **S&O and Product** above all.

### Hints for the likely follow-ups

- **"When S&O and Product want different things, what do you do?"** — the one most likely for you. Typical case: S&O wants stricter blocking to cut losses; Product worries about good customers being blocked. Don't pick a side: make the tradeoff measurable (fraud dollars saved vs. good orders lost or support tickets), propose a way to test it (phased rollout or experiment with guardrails), and agree the decision rule in advance. If it still doesn't settle, escalate jointly with the tradeoff written up. Story 2 is exactly this shape.
- **"Tell me about a partnership that went badly. What was your part?"** Pick a real one and spend most of the time on *your* mistake — you involved S&O too late and built toward the wrong metric, you never clarified who owned an analysis with DS, you didn't flag a slip early. End with the mechanism you changed.
- **"How do you work with a PM you disagree with about priorities?"** Understand their goal first, then offer options with costs ("your version, a cheaper version, and what each pushes out"). If you still disagree, bring in S&O's metrics: which option moves the business number more? Data settles more than opinions.
- **"How do you handle a partner team that keeps missing commitments?"** (Likely Infra or Backend.) Make the dependency visible to both managers early, understand *why* they're missing — often capacity or priority, as in Story 10 — build a fallback, and escalate jointly rather than complaining upward.
- **"Have you ever said no to S&O?"** Yes, framed as "yes, if" or "here's a better way" — e.g. they wanted a quick rule change, you showed it would block too many good users, and proposed a model-based approach with a fast first version. You respect that they own the metric; you own the technical judgment.
- **"How do you agree on metrics with S&O?"** Separate their business metric (fraud loss) from the model metrics your team controls (precision, recall, false-positive rate), and agree how the two connect *before* launch — the two layers plus guardrails from Q11.
- **"How much do you shield your engineers from stakeholders?"** "Shield them from churn, never from context." Engineers who hear S&O explain fraud patterns directly build better models. See "Shield from churn, never from context" below.

### The opening answer, built from your setup

> My most important partners are S&O and Product. S&O owns our business metrics — fraud loss and loss rates — and Product owns the features and user experience. Planning is a three-way partnership: S&O brings the targets and loss trends, Product brings the priorities, and I bring the technical options and what they cost. We plan the roadmap together, with a not-doing list, so nobody gets handed a plan they didn't shape.
>
> Beyond them, I work closely with data science on experiment design and metric definitions, with backend teams whose systems our models plug into — like the assignment team — and with infra for serving and capacity.
>
> Two things make it work. First, decision rights are clear: S&O owns the target, Product owns scope, I own the technical approach, and launch criteria are agreed before the launch, not during it. Second, I surface problems early — if something's slipping, my partners hear it from me the week I see it.
>
> A good example is [Story 2 or Story 10]…

Then go straight into Story 2 (S&O, Product, legal) or Story 10 (backend), and let the interviewer pick which one to dig into.

## Working with Product: problem definition, not requirements

This unpacks the script line: *"getting involved in problem definition rather than receiving requirements."*

| Receiving requirements (late) | Joining problem definition (early) |
| --- | --- |
| The PM decides the problem *and* the solution, writes a spec, and hands it to engineering | The PM brings a **problem** ("account takeover fraud is up 30%"), and you shape the solution together |
| Your team's job: estimate and build | Your team's job: help pick *what* to build, then build it |
| A solution is chosen, often a date is promised, and people are invested | Nothing is locked in yet, so changing direction is cheap |

Once the spec exists, the most valuable engineering input — "there's a much cheaper way to get this result" — arrives too late, and pushing back feels like blocking rather than helping.

**Why engineers often see the cheaper version.** PMs know the user and the business; your team knows what already exists and what's actually hard:

- "We already have a risk score — reuse it instead of building a new model."
- "That needs real-time data we don't have; a daily batch version gets 90% of the value in a tenth of the time."
- "Instead of verification for every user, apply it only to the riskiest 1% — far less friction."

**An example in your domain** (placeholder — replace with a real one):

- *Spec arrives late:* "Build an ID verification step for all new Dashers in onboarding." Six weeks of work, and every new Dasher gets extra friction.
- *Involved early:* the PM's real problem is fake Dasher accounts. Your team points out the existing risk score already flags most of them, so verification applies only to high-risk sign-ups. Two weeks of work, 95% of good Dashers never see it, and S&O's fraud metric still improves.

**How to actually get involved early:**

1. **Join planning before specs are written.** In quarterly planning with S&O and Product, discuss problems and goals first, solutions second.
2. **Ask for a one-page problem doc before the full spec** — what problem, for whom, how success is measured. Your team responds with options and rough costs.
3. **Pair a senior engineer with each PM** on their main area, so engineering sees ideas while they're still forming.
4. **Bring data proactively.** "We're seeing fraud shift to X" — sometimes engineering spots the problem first.
5. **Ask "what problem is this solving?"** whenever a request arrives as a solution. That one question turns a requirement back into a problem.

**The balance to show.** The PM still owns the "what" and the "why" (see the decision rights table). Getting in early means giving input when it's cheapest to act on, not taking over product decisions.

> I want my team in the room when the problem is being defined, not when the spec is done. The PM still owns what we build — but if the first time we see an idea is a finished spec, we've lost the chance to say "there's a version of this that's a third of the cost." So in planning we start from the problem and the metric, and my senior engineers partner with the PMs before anything is written up. A good example was [your real one] — we got involved early and the solution ended up [cheaper / faster / less friction].

**Have one real example:** a time your team's early input changed what Product built, with the cost or time saved. It's the strongest evidence for this line, and it tends to come up as "How do you work with a PM?"

## Shield from churn, never from context

**Churn** is constant change and noise that interrupts work without adding useful information: priorities that flip before they're decided, half-formed requests ("could we maybe also…?"), drive-by Slack asks sent straight to engineers, stakeholder debates that haven't reached a decision, repeated "is it done yet?" pings, and escalations that turn out not to be urgent. **Context** is the opposite: information that helps engineers decide better — why a project matters, which fraud patterns S&O is seeing, how the business metric is moving, what customers are experiencing. The principle: **absorb the churn yourself, and pass the context through.**

| Churn (filter it out) | Context (pass it through) |
| --- | --- |
| "S&O and Product are still debating X vs. Y" | "We decided on X, and here's why" — once it's decided |
| A VP pings an engineer for status | A written weekly status that answers it before anyone asks |
| Five small requests from different PMs in one week | "Here's the one request that made this sprint, and why" |
| "Can we change the threshold again?" — third time this week | "S&O is seeing a new fraud ring using X; here's the data" |
| A heated planning argument between stakeholders | The final tradeoff and decision, explained |

### How to absorb churn

1. **One front door for requests.** Requests come to you or one intake channel or queue, not straight to engineers. You triage: does it fit the mission, is it urgent, what does it displace? Engineers can say "great question — please route it through intake," and you back them up.
2. **Don't pass on undecided changes.** If S&O and Product are still debating a priority, wait until it's decided and deliver one clear message. When something is genuinely uncertain and will affect their work, give a dated heads-up: "This might change; I'll know by Thursday, so keep going for now."
3. **Batch changes at planning boundaries.** Unless it's truly urgent, new requests wait for the next sprint or planning cycle. Mid-sprint changes draw on the reserve capacity (Q10), not someone's half-finished work.
4. **Answer status questions before they're asked.** A short written weekly status that S&O, Product, and leadership can read removes most pings. If someone still pings an engineer for status, you take it.
5. **Go to the noisy meetings yourself.** Recurring stakeholder syncs, debates, escalations — you attend; engineers come when their expertise is needed. You bring back the decisions and the reasons.
6. **Use an interrupt rotation.** One engineer per week takes urgent asks, ad-hoc questions, and small fixes; everyone else keeps focus time. It spreads the load fairly.
7. **Absorb the pressure, not just the requests.** When a stakeholder is frustrated or pushing hard on a deadline, you take that conversation. The team hears the outcome ("we ship on the 15th with this reduced scope"), not the stress — the shock-absorber point from Round 1 Q1.

### How to pass context through

Shielding goes wrong when the manager filters *everything* — engineers build in a vacuum and the manager becomes a bottleneck relaying everything secondhand. So actively let context in:

- **Invite engineers to S&O fraud reviews** now and then, so they hear new fraud patterns firsthand.
- **Have engineers present their own work** to S&O and Product — direct feedback and visibility.
- **Share the "why" behind decisions,** including what was rejected and why.
- **Share the business metrics** — how fraud loss is moving, and how their model changed it.
- **Let senior engineers talk to stakeholders directly** on technical topics. You shield them from noise, not from people.

### Signs of the right balance

| Over-shielded | Under-shielded | About right |
| --- | --- | --- |
| Engineers don't know why they're building things | Half the day goes to Slack pings and meetings | Focus time, and they know why their work matters |
| Everything routes through you — you're the bottleneck | Priorities change mid-sprint constantly | Changes land at planning boundaries, with reasons |
| Engineers never meet S&O or Product | Every stakeholder argument lands on the team | Engineers meet stakeholders for real problems, not noise |
| Models are technically good but miss the business problem | Burnout and constant context switching | Engineers understand the fraud patterns behind the work |

### The spoken answer

> I shield my team from churn, never from context. Churn is the noise — priorities that haven't been decided yet, drive-by requests, repeated status pings, stakeholder debates. I absorb that: requests come through me or one intake channel, I don't pass on changes until they're decided, new asks wait for the next planning cycle unless they're truly urgent, and a written weekly status answers most "is it done yet?" questions before anyone asks. We also rotate one engineer on interrupt duty each week, so everyone else gets real focus time.
>
> But context goes straight through. My engineers regularly join S&O's fraud reviews and hear the patterns firsthand, they present their own work to Product and S&O, and they always know why a decision was made, not just what it was. Engineers who understand the fraud problem build better models — so I filter the noise, not the information.

**The example to have ready:** a week when priorities kept changing and you held them back from the team until they were settled — or, stronger, a time an engineer joined an S&O review and came back with an idea that improved the model. The second shows context paying off in a better result.
