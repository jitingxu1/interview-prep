# Rula Engineering Leadership — Q&A Prep: Jay Floyd

**Interview:** Tuesday, Nov 24, 2026, 11:00 AM–12:00 PM PT, Zoom, 60 minutes
**Interviewer:** Jay Floyd, Sr. Engineering Manager, Analytics Engineering at Rula
**Role:** Engineering Manager – AI/ML
**Round scope (per recruiter Maria Hernandez):** leadership style, types of teams managed, cross-team coordination, technical roadmaps, mentoring and leveling up engineers, recruiting and growing teams.

## How to use this

22 questions — more than will fit in 60 minutes. ★ = most likely, given Jay's own material. Prioritize those first, then skim the rest. Answers are written to be spoken in 60–120 seconds. Philosophy questions: 60–90 seconds. Story questions: up to 2 minutes. If you run past 2 minutes, you're rambling.

**Rule for this round:** Jay listens for *systems*, not just stories — a delegation system, a performance-conversation structure, how you handle former peers and stakeholder tension, and whether you can name what "level" means transparently for your reports. He explicitly dislikes over-explaining, rescuing, and being the "answer machine." Frame answers around ownership transfer, trust, and calm authority, with concrete 1:1 / feedback / leveling examples.

**Numbers used in these answers (all verified):** escalation rate 67% → 50%+; review time 30 → 5 min; manual tickets 500 → 260 per 10K orders; 60+ fraud models unified; restaurant underwriting $1M pilot → $25M; team meeting load 50% → ~20%; infrastructure upgrade shipped 4 weeks early; 12 engineers across two pods, built from scratch; 10 engineers inherited when their manager left. Anything marked **[NEEDS YOUR STORY]** is a gap — fill it in before the interview, don't improvise it live.

## Jay Floyd in 60 seconds

Jay is Sr. Manager, Analytics Engineering at Rula (since June 2026), previously a data-platform engineering manager at Zapier for ~5.5 years. In parallel since 2022 he has run a private coaching practice for technical managers and written two books: *The Driver's Seat* and *Rare On Purpose* (May 2025). His sites: iamjayfloyd.com and rareonpurpose.com.

His frameworks, in his words:

- **Coaching-first management** — active listening, open-ended questions ("How do you feel about this approach?" / "What do you think could be a potential solution?"), a safe space for feedback, personalized development plans built on strengths — "not just what they're good at, but what type of work *energizes* them" — and being coachable yourself: "Even the best coaches have their own coaches." But coaching is only one of a manager's hats; over-coaching creates dependence. He has said managing is "only probably twenty percent coach."
- **People Leadership OS** — "Technical skill got you promoted, but people leadership is the job now." Five steps: Map Your Leadership Design → Find the Leadership Drag → Rebuild Delegation and Ownership → Strengthen Performance and Hard Conversations → Practice Calm Authority. "A lot of technical managers are not failing. They are leading a new role with an old operating system."
- **RareStack / Rare On Purpose** — Surface → Structure → Land. "Lead with alignment, not performance — Build with purpose, not pressure." Outcomes include: "You stop over-explaining and start being understood… You lead from Calm Authority — not urgency, not ego."
- **"Identify Your Seatbelts"** (*The Driver's Seat*, ch. 2) — "What's the thing that has you stuck in the backseat? What are you afraid of?" Address the fear at the root. "Fail faster and use that failure as fuel."

---

## (a) Leadership Design / leadership style

**Jay's lens:** He believes most technical managers aren't failing — they're "leading a new role with an old operating system." He listens for whether you can name your own operating system — how you think, decide, handle pressure, build trust — and whether you've actually rebuilt it since becoming a manager.

### ★ Q1. How would you describe your leadership style?

I'd call it coaching-first, but not coaching-only — and that second half matters, because I learned it the hard way.

I start by understanding the person. What's their motivation, what kind of work energizes them, what are they trying to get better at. In a 1:1, I ask more than I tell — open-ended questions, real listening, not jumping to the answer. My 1:1s are structured around the engineer's growth, not status: a few minutes on how they're doing, most of the time on what's blocking or exciting them, and a regular career check-in. The goal is that nobody is ever surprised in a review — if there's a concern, they've heard it from me multiple times already, with a plan.

But coaching is one hat. When something is urgent, or high-stakes, or someone has asked me twice, I direct — clearly and explicitly. I had to learn that, because my instinct as a former tech lead was to either coach everything or solve everything myself. Neither one scales. So my style now is: coach by default, direct when the situation demands it, and be honest with the team about which mode I'm in.

### ★ Q2. What changed for you when you moved from tech lead to manager?

Everything about what I was measured on. As a tech lead, I was measured by answers — how fast I could solve it, how good the design was. As a manager, I'm measured by the system — whether the team can produce good answers without me in the room.

There's a line Jay uses — leading a new role with an old operating system — and that was exactly my experience. I came up as a strong tech lead, so my instincts were: if it matters, own it; if someone's stuck, jump in; if the reasoning is sound, explain it in depth. All of that was useful as an IC. As a manager, each one became a drag. At VoltronData I made the classic mistake — I tried to code full-time and manage full-time. It didn't work.

So I rebuilt the operating system deliberately. I stay about 10 to 15 percent hands-on — design reviews on major projects, spike investigations, critical bugs — enough to keep technical credibility and spot debt early. The other 85 percent is growing others: setting direction, clearing blockers, and building the layer below me that owns decisions. The shift took time, and honestly on a high-stakes call my instinct is still to step in early. But I catch it now, and that's the difference.

### Q3. What kind of team and culture do you want to build?

My honest view is that culture is the set of behaviors you're willing to protect when protecting them costs you something. Everything else is a poster on a wall.

So I think about it as three things I actually enforce, not three things I believe. First, clarity — people always know what good looks like and where they stand. I learned that the hard way: early on, an engineer was blindsided in a review because I'd never clearly stated the expectation. That was my failure, not theirs. So now feedback is mid-cycle, in writing, with a standard structure, and my rule is no surprises at review time.

Second, real ownership — not "you own this" as a phrase, but actual decision rights. Senior ICs own areas and review each other's work, so I'm not the bottleneck.

Third — and this is the one I'd actually be judged on — I absorb the organizational load so engineers get to build. My team was spending about 50 percent of its time in meetings. I consolidated four stakeholder syncs into one, made async prep mandatory so meeting time was for decisions, published structured notes so nobody had to attend just to stay informed, and I held a no-meeting day against real pressure from partner teams. We got engineers down to about 20 percent meeting time, and shipped a major infrastructure upgrade four weeks early. I'd rather be the one taking the hit from the org than have my team take it.

---

## (b) Delegation & Ownership

**Jay's lens:** His #1 diagnostic is whether everything still runs through you — "You know too much, so everything runs through you… You become the answer machine." He listens for a *delegation system*, not good intentions: written decision rights, a handoff plan, and how you inspect without micromanaging.

### ★ Q4. Tell me about a time you were the bottleneck. What did you change?

My biggest weakness is that I'm slow to let go of decisions. I came up as a tech lead, so if something matters, my instinct is to own it.

For a while that worked. I used to lead one team — one pod, one group of stakeholders — and owning every alignment and every technical call was efficient. Then the team grew into two teams — support automation and fraud and risk ML — each with its own scope and its own stakeholders. We're 12 engineers, but the surface area is much bigger than the headcount. I couldn't handle it all on my own — but I kept trying to for about three months longer than I should have. Every stakeholder alignment and every high-level technical decision still went through me.

I noticed it in three ways. My calendar was every team's stakeholder calendar. Teams were waiting on me for decisions while I was context-switching across scopes. And the engineers closest to each problem, who had the most context, were bringing their decisions to me instead of making them. I was the bottleneck, and honestly I was exhausted.

So I restructured it. Each team now has a senior IC who owns that team's stakeholder alignment and its technical decisions. I wrote down the decision rights: within the team's scope, they decide and tell me after. What comes to me is anything that crosses teams, touches another org's metrics, is expensive to reverse, or changes headcount. I didn't just hand it over — for the first month I co-ran their stakeholder meetings, then they ran them with me sitting in, then I stepped out. And we have a weekly pod-lead sync where they bring cross-team issues and I catch anything that needs me.

That freed me to do the work only I can do: the roadmap across teams, how the teams fit together, hiring, and leadership alignment. And two of the pod leads grew into senior scope because of it. It's not fully solved — on high-stakes calls my instinct is still to step in early. But this is exactly the model I'd bring to a bigger team: build the layer that owns decisions, and keep myself for the decisions that cross the layers.

**[NEEDS YOUR STORY: confirm the pod-lead names and the before/after numbers — decisions reaching you per week, recurring meetings count — before using this live. The repo has them as blanks.]**

### Q5. How do you delegate without lowering the bar on quality?

By being explicit about what "good" means before I hand something over, and by inspecting outcomes instead of process.

The delegation system has three parts. First, written decision rights: inside your scope, you decide and inform me after. Cross-team, hard to reverse, or headcount — those come to me. The line is explicit, so nobody has to guess whether they should ask. Second, the quality bar lives in the artifact, not in my head: design docs, decision logs, and eval gates. When we unified 60-plus fraud models into one system, I couldn't review every model myself — so the bar became the evaluation: offline metrics plus a shadow run before anything shipped. Third, a gradual handoff: I co-run, then I sit in, then I step out. Stakeholders keep trust, and the person taking ownership gets coached, not dropped in.

A good example is the support review work. We cut review time from 30 minutes to 5 by building an eval-driven pipeline — but the quality bar was the eval set itself. Once that existed, engineers could move fast without me checking every case, because the system caught regressions. That's what delegation should feel like: the standard is enforced by the system, not by my calendar.

### Q6. How do you know when to step in on a technical decision — and when to stay out?

I have a simple rule. I step in when the decision crosses teams, is expensive to reverse, or needs judgment the team can't see yet — usually because it touches another org's metrics or a commitment I made. I stay out when it's reversible and inside their scope, even if I'd decide differently. That's the hard part: letting a good-enough decision stand because the ownership matters more than the extra five percent.

A real example: two of my senior engineers deadlocked on a model architecture. Instead of deciding for them, I had each write a one-page design doc, ran a structured discussion — assumptions, tradeoffs, unknowns — and we landed on a hybrid. Then we set the standing rule: senior engineers propose, the team debates, I break ties if needed, and then everyone commits. The commitment half is what makes the disagreement safe.

I stay technically close enough to judge well — I review design docs async, I do design reviews on major projects, I keep about 10 to 15 percent hands-on. But I don't review every PR, and I don't sit in every meeting. If I'm the only reviewer at 6 people, I'm a bottleneck at 12 and a liability at 20.

---

## (c) Performance & Hard Conversations

**Jay's lens:** He sells a "Performance Conversation Framework" and "Hard Conversation Scripts" — he listens for structure and timing, not courage. The signal is: feedback early, expectations in writing, no one surprised at review time.

### ★ Q7. How do you handle an underperforming engineer?

I diagnose before I judge. There are three questions, in order. First, clarity: do they actually understand what success looks like? Very often it's a communication problem, not a capability problem. Second, fit: are they in a role that plays to their strengths? Sometimes someone is struggling because they're in the wrong seat. Third, support: have I given them the tools, the time, and the mentoring to succeed? As a manager, underperformance is partly my problem.

If it's truly a capability gap after coaching, I'd build a clear, time-bound improvement plan with specific milestones. If they improve, great. If not, we have an honest conversation about fit.

I want to give you a real example of the fit question. I had a backend engineer who was struggling on his team, and the easy path was a PIP. But the diagnosis said skill-fit, not performance — he was strong in infrastructure, just in the wrong role. So we moved him to the infrastructure side instead. It was the slower, more expensive path, and it was the right one: he became core to our platform work. Sometimes a "misfit" engineer is actually a high performer in a different role, and I'd rather find that fit than manage someone out of a seat they were never going to win in.

### ★ Q8. Tell me about a difficult conversation you had. How did you prepare?

Giving negative feedback is harder for me than it should be. I care a lot about the team's trust, and early on I'd soften the message or wait for a better moment — which is really just postponing it.

It caught up with me as a new manager. I had a performance concern about one engineer that I'd hinted at but never said directly. When I finally raised it clearly, he was blindsided — and he was right to be. I'd never set the expectation in the first place. That was on me.

I went back, told him that directly, and we rebuilt the plan together. Then I changed how I run feedback for everyone. I use a simple structure — what I observed, why it matters, what good looks like, how I'll help — which takes the emotion out and makes it about the work. I give it within a week of noticing, in the 1:1, not saved for review season. Every engineer gets a mid-cycle check-in. And I got coaching from our HR partner on difficult conversations, including practicing a couple before I had them.

He stayed, his performance recovered, and the whole team got clearer expectations out of it. I track one thing above all: nobody is surprised at review time. It still isn't comfortable for me, and I don't think it should be — but I don't let discomfort set the timing anymore.

### Q9. Have you ever had to manage someone out?

No — and I want to be straight about that rather than dress something up. I haven't managed anyone out.

The closest I've come is the repositioning I just described: an engineer who was struggling in one seat, and instead of starting a performance process, we moved him to infrastructure work where his strengths actually fit, and he thrived there. My view is that managing someone out should be the last step after you've honestly checked clarity, fit, and support — and in the cases I've faced, the fit check changed the answer. If I ever do have to manage someone out, I'd want it to be after that same honest sequence, with clear expectations in writing and no surprises.

---

## (d) Calm Authority / trust

**Jay's lens:** "Calm Authority" is the end state of his system — lead "without brute-forcing everything," "not urgency, not ego." He listens for steadiness under pressure, and for whether trust was built *before* it was needed.

### Q10. How do you build trust with a team — especially one that didn't choose you?

I inherited a team once — ten engineers, my manager had left, no interim — so I've actually lived this. The first thing I did was diagnose before changing anything. The first 1:1 question that mattered wasn't "what are you working on," it was "what was missing with the last manager?" and "where do you actually want to go?" You're finding out what the team believes about how this place works before you try to change it.

Then I changed one thing visibly and fast. People judge a new manager by whether the first stated commitment survives contact with pressure. I picked something small, painful, and real — consistent 1:1s and protected focus time — and I never missed it.

The deeper principle is that trust is built by removing surprises. Expectations in writing, feedback mid-cycle, no one blindsided at review time. And I try to be the surface the organization pushes against, so the team doesn't have to be. When people see you absorb the org load — the meetings, the stakeholder noise — instead of passing it down, they start to trust that you've got them. That's what calm authority actually is: not being loud, just being steady and predictable when it counts.

### Q11. Tell me about a time you led under real pressure. How did you keep the team steady?

The clearest one is the support automation work at DoorDash. Our escalation rate was 67 percent — two out of three cases were going to a human — review time was 30 minutes a case, and manual tickets were running 500 per 10,000 orders. The team was drowning, and every stakeholder wanted their issue first.

What kept us steady wasn't heroics, it was cadence and one clear system. I named the problem honestly to the team and to stakeholders: we're not going to fix this by working harder, we're going to fix it by building an agentic pipeline with real evals. I protected focus time — a no-meeting day, one consolidated stakeholder sync instead of four — so the team could actually build. And I gave them a single, measurable target to rally around instead of ten competing asks.

The results: escalation went from 67 percent to just over 50 percent, review time from 30 minutes to 5, manual tickets from 500 down to 260 per 10,000 orders. The lesson I took from it is that under pressure, the manager's job is to narrow, not to widen — one priority, one system, a steady rhythm — and to absorb the noise so the team can hear itself think.

---

## (e) Coaching-first management & mentoring/leveling

**Jay's lens:** He always starts as a coach — "understanding who is this person, what's their motivation, and let's identify their unique strengths" — but he will test whether you know coaching is only about twenty percent of the job, and when to take the hat off.

### ★ Q12. How do you coach and mentor your engineers? How do you know it's working?

I start with listening, not telling. A coaching-first approach for me begins with active listening — really hearing the person, their aspirations, their concerns — and then asking open-ended questions instead of handing over the answer. "How do you feel about this approach?" "What do you think could be a potential solution?" That does two things: it builds ownership, and it builds their critical thinking, because they have to arrive at the insight themselves.

My 1:1s are built for this. A few minutes on how they're doing, most of the time on what's blocking or exciting them, and a regular career check-in. And I try to build personalized growth plans around strengths — not just what someone's good at, but what kind of work *energizes* them. One engineer on my team was frustrated by meetings and needed deep focus time; another wanted to learn production systems. Once I understood that, I could unblock them completely differently.

How do I know it's working? Three signals. People start bringing me decisions they've already made, not decisions they want me to make. They give each other feedback directly instead of routing it through me. And they disagree with me in a meeting, with data. When those three things are happening, the coaching is landing — because the point was never to make them dependent on me, it was to make them stronger without me.

### ★ Q13. How do you approach leveling and promotions? How do you keep it fair?

I'm very transparent about it. I tell every report: here's what's expected at your level, here's what I believe that looks like for you specifically, and let's talk about it. If you have aspirations for the next level, let's discuss what that looks like for you — because what I've found is that people are most frustrated not when they're told no, but when there's no clear expectation at all. "You did great" — great at what? "You were inconsistent this quarter" — inconsistent against what?

The second half is that I don't put people in a box. The level framework is real, but the unique version of it is per person. One engineer might be an empathizer, another a deliverer — you don't have to be your colleague to be at the same level as your colleague. So I look for the version of the next level that fits their strengths, and then I give them stretch work that proves it, and I mentor them publicly so the rest of the org can see it.

Two of my pod leads grew into senior scope exactly this way — they took on stakeholder alignment and technical decisions for their teams, and the promotion case wrote itself because the work was already visible. My rule is: the promotion should be a recognition of work already being done, not a promise about future work.

**[NEEDS YOUR STORY: name one specific promotion — who, from what level to what, and the stretch assignment that made the case. The repo references this story (S7) but the details weren't pulled.]**

### ★ Q14. When do you coach, and when do you just give the answer?

This is the hardest judgment call in management, and I had to learn it by getting it wrong. My natural inclination is to coach — I wake up wanting to coach people. But I walked into management assuming coaching *was* management, and within a few months I saw the problem: coaching takes time, and management doesn't always have it. If I coach everything, I create dependence — people who need me to rebuild their confidence every week instead of holding onto their own strength.

So now I sort it three ways. I coach when the person already has the answer and needs to find it — that's where growth and ownership live, and the blast radius is small. I give limited space when there's a real tradeoff: I'll say, "take two days to explore it, then bring me what you've got" — a cost-benefit call, because letting someone walk too long has dependencies attached. And I direct explicitly when it's urgent, high-stakes, or they've already asked twice. In those cases I tell them exactly what I want and exactly how I want it done, and I explain what I'm expecting so it's fair.

The signal I watch for is dependence. If someone's confidence collapses between our 1:1s and they need me to rebuild it every time, I'm over-coaching. The goal is the opposite: that they leave the conversation holding their own reasons to move, not mine.

---

## (f) Recruiting & growing teams

**Jay's lens:** He's a hiring manager at Rula right now, and he joined Rula partly "to help grow this team… building an environment where great people can do the BEST work." He listens for a real bar, not a vibe — and for whether growth is a system, not a favor.

### Q15. Tell me about a team you built from scratch.

I built my current setup from nothing — 12 engineers across two pods, support automation and fraud and risk ML. Three things I got right, and one I'd do differently.

First, the first three hires are the culture. Whatever they do becomes the norm before you ever write anything down. So I hired for the behavior I wanted copied, not just the skills I needed that quarter. I hired for strengths rather than the req — one engineer who was strong in infrastructure became core to our platform work, even though he started in fraud detection.

Second, I said what "good" means on day one, in writing. Not values — standards. What a design doc contains, when you write one, what gets reviewed and by whom, who decides when people disagree. New people join a vacuum and fill it with guesses, and those guesses become the culture — much harder to change at 12 than at 3.

Third, I gave away decisions early, before it felt safe. Senior ICs owning areas and reviewing each other's work is what lets a team scale past my own attention. If I'm the only reviewer at 6 people, I'm a bottleneck at 12 and a liability at 20.

What I'd do differently: I'd write down the decision rights from the start instead of absorbing everything first and delegating later. That three-month lag I mentioned — where every decision still ran through me — was the cost of learning that lesson. Now when scope changes, I set up the owner and the decision rights at the start.

### Q16. How do you hire? What do you look for?

Four things, in order. Technical foundation — can they think through systems, can they code, do they understand ML fundamentals for the fraud side. Learning mindset — have they grown in past roles, do they ask good questions. Communication — can they explain complex ideas clearly, because that's critical on cross-functional teams. And judgment — how do they decide under uncertainty. In interviews I like to walk through a recent real decision with them and see how they reasoned.

I stay involved personally — I do technical interviews and culture assessments myself, and I give engineers on the team a voice in hiring, because they usually spot things I miss. And I hire for strengths, not the req. The infra-strong engineer I mentioned is the example: on paper he was a fraud-detection hire, but his real strength was platform thinking, and once I saw that, I put him where that strength compounded. Hiring is the highest-leverage thing I do, so I don't delegate the bar.

**[NEEDS YOUR STORY: one "best hire" story with a name and specifics — how you found them, what you saw in the interview, what they became. The question bank lists this as a standard question.]**

### Q17. Tell me about someone you promoted. What did you do that made the difference?

The honest structure of the answer is: who they were, what the gap was, what stretch I gave them, and what changed in them — not just in their title.

The clearest case I have is one of my pod leads. They started as a strong senior IC — deep context on the scope, good judgment, credibility with stakeholders — but they were still bringing every decision to me. The stretch was real ownership: their team's stakeholder alignment and technical decisions, with written decision rights so the line was explicit. I co-ran their stakeholder meetings for the first month, then sat in while they ran them, then stepped out. Within a few months they were making harder calls on their own, and the stakeholders trusted them directly — the promotion case wrote itself, because the work was already visible at the next level.

Would they have gotten there without me? Eventually, maybe — they had the ability. But I think the deliberate part mattered: naming the stretch, making the decision rights explicit, and creating the visibility so the rest of the org could see it. That's the difference between hoping someone grows and actually growing them.

**[NEEDS YOUR STORY: fill in the person's name, the levels involved, and one concrete decision they made independently that proved the promotion. Do not use this answer live until those details are real.]**

---

## (g) Cross-team coordination & technical roadmaps

**Jay's lens:** His own career is cross-functional translation — a Data Governance Council with Legal, Finance, Product, and Engineering; a Redshift-to-Databricks migration across teams; 1:1s with everybody in his perimeter. He listens for how you build alignment *before* you need it, and for roadmaps argued in business terms, not technical ones. (Note: he has no published roadmap framework of his own — don't attribute one to him.)

### Q18. How do you set a technical roadmap when the goals are still being defined?

I work backward from the business problem, not forward from the technology. On the fraud side, the framing was: fraud is a growing threat, our current model catches 40 percent with 2 percent false positives, and we want to catch 60 percent with under 2 percent false positives. Then: what's blocking us — model architecture, feature engineering, throughput? Then what's the 6-month roadmap to get there — new model training, data pipeline improvements, and so on. I bring the team in to debate the approach, but I own the strategy. And I adjust based on what we learn — if we hit a technical wall, we pivot.

Two rules I hold. First, we're not building cool things, we're solving real problems — that alignment keeps the team motivated. Second, the roadmap is written in business units, not technical ones. When I report up, the first line is the decision or the ask, the second is the business impact — dollars, customers, risk — and the technical detail is an appendix, not the talk track. The fraud threshold discussion is the example: instead of debating precision and recall, I put fraud dollars prevented and legitimate customers blocked on the same chart at each threshold. The room argued about a number instead of a principle, and we agreed on a phased rollout in one meeting.

If I were setting a roadmap at Rula, I'd start the same way — with the clinical and operations problem, not the model. What does the care team need to decide faster or better, and what's the smallest system that proves it?

### ★ Q19. Tell me about a cross-org initiative you drove.

The biggest one is unifying fraud detection. We had 60-plus separate fraud models, built by different teams at different times, each with its own owner, its own features, its own blind spots. My job was to bring them into one system — one evaluation framework, one serving path, one set of ownership rules.

The technical work mattered, but the alignment work mattered more. I started by setting up 1:1s with everybody in my perimeter — the teams that owned the models, the product partners, the risk and operations folks — even when I had no immediate work with them. When the time came to ask them to give up their model, I wasn't a stranger making a demand; I knew what they cared about, and they knew I saw the value in what they'd built. That sounds soft, but it's the whole game: people don't hand over their system to someone who hasn't taken the time to understand it.

The other cross-org win was the restaurant underwriting work — a $1M pilot that grew to $25M. Same pattern: start with the business problem in their language, prove it small, then scale with their trust already earned.

**[NEEDS YOUR STORY: for the 60-model unification — which teams/orgs were involved, how long alignment took, and one moment where a team resisted and what you did. The repo references this as a cross-org story but the mechanics weren't pulled.]**

### Q20. How do you say no to a partner team or a senior stakeholder?

With an alternative, not a wall — and with a clear statement of what the boundary protects.

A real example: Product wanted our fraud team to also take on chargeback prevention. It was a real problem, but it was a different problem space, and absorbing it would have diluted the team's focus. So we said: that's a different problem space, we can advise, but you need a dedicated team. And then I helped them hire the first engineer for it. Saying no while helping them solve it is very different from saying no and walking away — the relationship got stronger, not weaker.

The same principle applies inside the team. I held a no-meeting day against real pressure from partner teams, because focus time was the thing my engineers needed most. Boundaries only work if you hold them when holding them costs you something — the moment you make an exception, the boundary is gone. So I decide the boundary in advance, I explain what it protects, and I offer the next-best help I can actually give.

---

## (h) Strengths-based development / "Identify Your Seatbelts"

**Jay's lens:** His book's chapter 2 is "Identify Your Seatbelts" — "What's the thing that has you stuck in the backseat? What are you afraid of?" He listens for honest self-knowledge: a real fear named at the root, and what you do with it — not a humblebrag.

### ★ Q21. What's your biggest weakness as a manager?

My biggest weakness is that I'm slow to let go of decisions. I came up as a tech lead, so if something matters, my instinct is to own it.

For a while that worked — when I led one team, owning every alignment and every technical call was efficient. Then the team grew into two teams, each with its own scope and stakeholders, and I kept running it the old way for about three months longer than I should have. Every decision still went through me. My calendar was every team's stakeholder calendar, teams waited on me while I context-switched, and the engineers with the most context were bringing me their decisions instead of making them.

They share one root, and naming it is the honest part: I came up as a strong tech lead, and the instincts that made me good at that — owning the call, explaining the reasoning in depth, protecting the team's harmony — each needed rewiring when I started managing. So I restructured: a senior IC per team owns stakeholder alignment and technical decisions, decision rights are written down, and I hand off gradually — co-run, sit in, step out — with a weekly sync for cross-team issues.

I track it: how many decisions still come to me per week, how many stakeholder meetings I'm in, and I ask stakeholders directly whether alignment got better or worse. It's much better, but it's not fully solved — on high-stakes calls my instinct is still to step in early. That's what I'm watching now, and it's the first thing I'd design for in a bigger team: build the layer that owns decisions, and keep myself for the decisions that cross the layers.

### Q22. What's a belief about management you've changed your mind on?

I used to think my job was to have the answer. Now I think my job is to build the system that produces answers without me — and to name the fear that's keeping me in the answer seat.

The concrete version of that change is about feedback. Early on, I thought 1:1s were for check-ins, not feedback. I thought I was protecting the relationship by softening hard messages. Then an engineer got blindsided in a performance review because I'd never told him the expectation clearly — and he was right to be blindsided. That was on me. What I learned is that the discomfort of giving feedback early is much cheaper than the damage of giving it late. Now feedback happens within a week of noticing, in the 1:1, with a clear structure, and nobody is surprised at review time.

There's a second piece I took from Jay's own writing, actually — the idea of failing faster. I used to treat a miss as something to avoid. Now I treat it as fuel, but only if we name what actually happened. The fraud threshold call, the pod-lead handoff — both of those only worked because we said plainly what went wrong first. The fear doesn't go away by avoiding it; it goes away by addressing it at the root.

---

## Questions to ask Jay (have 4 ready — never say "none")

1. **On his core tension:** "You write about coaching being only one of a manager's hats — where do you draw the line at Rula between coaching and directing, especially in a clinical setting where the stakes are patient care?"
2. **On success in the role:** "What does 'good' look like for this EM in the first 90 days — and what would worry you by day 90?"
3. **On leveling:** "You talk about level transparency — how does Rula define levels for the AI/ML team today, and where do you see the biggest leveling gaps?"
4. **His favorite closer:** "What else should I be asking that I didn't?"

---

## [NEEDS YOUR STORY] — fill these in before Tuesday

1. **Q4 delegation story** — pod-lead names; decisions reaching you per week (before/after); recurring stakeholder meetings count (before/after).
2. **Q13 / Q17 promotion story** — one specific promotion: name, levels, the stretch assignment, one independent decision that proved it.
3. **Q16 best hire** — one hire story: how you found them, what you saw in the interview, what they became.
4. **Q4 follow-up: a recent slip** — one real recent case where you jumped into a delegated decision and how you caught it.
5. **Q19 cross-org mechanics** — 60-model unification: which teams/orgs, how long alignment took, one moment of resistance and what you did.
6. **Q18 roadmap detail** — the 6-month shape of the agentic support pipeline roadmap (phases, gates) so the fraud example isn't the only roadmap story.

## Sources

Jay Floyd material (all read live, Nov 21, 2026):

- https://iamjayfloyd.com/ — homepage; People Leadership OS, five steps, "Technical skill got you promoted. People leadership is the job now."
- https://iamjayfloyd.com/books — *Rare On Purpose* framing ("leading without erasing yourself").
- https://www.rareonpurpose.com/ — RareStack (Surface → Structure → Land), Calm Authority outcomes, both books.
- https://powertofly.com/up/zapier-build-coaching-into-your-management-approach — "5 ways to build coaching into your management approach," Oct 25, 2023; coaching-first, five recommendations, "Even the best coaches have their own coaches."
- https://uncommonteams.com/uncommon-leadership-interview-series/feed-your-good-wolf-jay-floyd/ — "Feed your good wolf," Apr 15, 2024; manager-vs-coach, over-coaching/dependence, level transparency, 1:1s with your whole perimeter, "Identify Your Seatbelts," "Fail faster."
- https://www.joinleland.com/jay-floyd — career history (Rula since June 2026; Zapier ~5.5 yrs), People Leadership OS packages.
- https://www.mento.co/coaches/jay-floyd — strengths-based / High 5, book attribution.
- https://bookshop.org/p/books/rare-on-purpose-jay-floyd/0406856f1bc112c8 — *Rare On Purpose*, May 26, 2025, 150 pp., $17.99.
- Full research report: `research_notes/jay-floyd-rula-leadership-coaching-20261121-1821/report.md`

User's own interview-prep repo (github.com/jitingxu1/interview-prep, public, main branch):

- `leadership/manager_qa.md` — 1:1s, underperformance, feedback structure, conflict, hiring, tech-lead/manager balance, technical strategy.
- `leadership/weaknesses.md` — three weaknesses with spoken versions; "Have you ever managed someone out? No. Say so plainly."
- `leadership/building_team_and_culture.md` — culture thesis, three mechanisms, meeting load 50% → ~20%, No-Meeting Thursday, infra upgrade 4 weeks early, 12 engineers / two pods, inherited team (S1).
- `leadership/interview_questions.md` — 90-question bank.

Verified numbers used: escalation 67% → 50%+; review 30 → 5 min; manual tickets 500 → 260 per 10K orders; 60+ fraud models unified; restaurant underwriting $1M pilot → $25M. No other metrics were invented; bracketed items in the repo were not treated as facts.
