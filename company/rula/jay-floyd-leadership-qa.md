# Rula Engineering Leadership — Q&A Prep: Jay Floyd

**Interview:** Tuesday, Nov 24, 2026, 11:00 AM–12:00 PM PT, Zoom, 60 minutes
**Interviewer:** Jay Floyd, Sr. Engineering Manager, Analytics Engineering at Rula
**Role:** Engineering Manager – AI/ML
**Round scope (per recruiter Maria Hernandez):** leadership style, types of teams managed, cross-team coordination, technical roadmaps, mentoring and leveling up engineers, recruiting and growing teams.

## How to use this

36 questions — more than will fit in 60 minutes. ★ = most likely, given Jay's own material. Prioritize those first, then skim the rest. Answers are written to be spoken in 60–120 seconds. Philosophy questions: 60–90 seconds. Story questions: up to 2 minutes. If you run past 2 minutes, you're rambling.

**The sections mirror Jay's own structure.** The first five sections are his People Leadership OS steps, in his words and order: (1) Map Your Leadership Design, (2) Find the Leadership Drag, (3) Rebuild Delegation and Ownership, (4) Strengthen Performance and Hard Conversations, (5) Practice Calm Authority. Then: Coaching-First Management & Leveling, Recruiting & Growing Teams, Cross-Team Coordination & Roadmaps, and Alignment & Positioning (his RareStack system). The original 22 questions are all here, reorganized; 13 new questions (Q12, Q16, Q17, Q21–Q23, Q30–Q35) were added Nov 21 after auditing his websites, books, and podcast against the first version — see `jay-floyd-content-alignment-audit.md`. Q36 was added the same day from spoken practice in a voice call.

**Rule for this round:** Jay listens for *systems*, not just stories — a delegation system, a performance-conversation structure, how you handle former peers and stakeholder tension, and whether you can name what "level" means transparently for your reports. He explicitly dislikes over-explaining, rescuing, and being the "answer machine." Frame answers around ownership transfer, trust, and calm authority, with concrete 1:1 / feedback / leveling examples.

**Numbers used in these answers (all verified):** escalation rate 67% → 50%+; review time 30 → 5 min; manual tickets 500 → 260 per 10K orders; 60+ fraud models unified; restaurant underwriting $1M pilot → $25M; team meeting load 50% → ~20%; infrastructure upgrade shipped 4 weeks early; 12 engineers across two pods, built from scratch; 10 engineers inherited when their manager left. Anything marked **[NEEDS YOUR STORY]** is a gap — fill it in before the interview, don't improvise it live.

## Jay Floyd in 60 seconds

Jay is Sr. Manager, Analytics Engineering at Rula (since June 2026), previously a data-platform engineering manager at Zapier for ~5.5 years. In parallel since 2022 he has run a private coaching practice for technical managers and written two books: *The Driver's Seat* and *Rare On Purpose* (May 2025). His sites: iamjayfloyd.com and rareonpurpose.com. His podcast, *On Everything with Jay Floyd*, is now *The Rare On Purpose Podcast* (63 episodes).

His frameworks, in his words:

- **People Leadership OS** — "Technical skill got you promoted, but people leadership is the job now." Five steps: Map Your Leadership Design → Find the Leadership Drag → Rebuild Delegation and Ownership → Strengthen Performance and Hard Conversations → Practice Calm Authority. "A lot of technical managers are not failing. They are leading a new role with an old operating system." His coaching focus areas, per Leland: delegation, performance conversations, hard conversations, trust, communication under pressure, stakeholder friction, **former peer dynamics**.
- **Coaching-first management** — active listening, open-ended questions ("How do you feel about this approach?" / "What do you think could be a potential solution?"), a safe space for feedback, personalized development plans built on strengths — "not just what they're good at, but what type of work *energizes* them" — and being coachable yourself: "Even the best coaches have their own coaches." But coaching is only one of a manager's hats; over-coaching creates dependence. He has said managing is "only probably twenty percent coach."
- **RareStack / Rare On Purpose** — Surface → Structure → Land. "Lead with alignment, not performance — Build with purpose, not pressure." Surface: name the gap between how you operate and how you're perceived. Structure: positioning language, communication clarity, an operating rhythm that forces alignment. Land: clarity → behavior → positioning → career movement. Outcomes include: "You stop over-explaining and start being understood… You lead from Calm Authority — not urgency, not ego… You become more legible to leadership."
- **"Identify Your Seatbelts"** (*The Driver's Seat*, ch. 2) — "What's the thing that has you stuck in the backseat? What are you afraid of?" Address the fear at the root. "Fail faster and use that failure as fuel."
- **At Rula** he leads analytics engineering, data governance, and AI enablement, partnering with Product, Clinical, Finance, Operations, and Engineering — and his design principle there is that "the safest and healthiest path is also the easiest path."

---

## Step 1 — Map Your Leadership Design

**Jay's lens:** He believes most technical managers aren't failing — they're "leading a new role with an old operating system." He listens for whether you can name your own operating system — how you think, decide, handle pressure, build trust — and whether you've actually rebuilt it since becoming a manager.

### ★ Q1. How would you describe your leadership style?

My style is situational. It depends on the person, the skill, and the problem. I came up as a tech lead, and the main thing I learned in three years of managing is that one style doesn't fit every problem.

I use the four modes from situational leadership: directing, coaching, supporting, delegating. For each task I ask: how much skill and confidence does this person have *on this specific problem*? A senior engineer can need directing on something brand new. A junior can own a part of the code they know well.

I'm explicit about it. I tell each person where I think they are on their area, and I ask where *they* think they are. If we disagree, that gap is the conversation, and then we plan how to move them up.

Two examples. In a production incident when we're losing money, I'm directive: I pick the people, assign the work, align on the goal, and we review afterward. On the other end, when my team split into two pods, I moved two senior ICs to delegation on purpose. I co-ran their stakeholder meetings for a month, then sat in, then stepped out. Now they own their team's decisions, and both grew into senior scope.

The trap I watch for is over-coaching. If someone needs me to rebuild their confidence every week, I've created dependence. The goal is to move everyone toward delegation.

**Likely follow-ups** (full answers, delivery checklist, and practice log in [leadership/leadership_style.md](../../leadership/leadership_style.md)):

- *Someone thinks they're at delegating, you think coaching?* Give them a bounded piece to own fully, agree on what good looks like up front, and let the result settle it.
- *How do you go directive without it feeling like distrust?* Name the mode and why ("this is about the situation, not you"), and hand ownership back after the incident.
- *How do you assess skill and confidence?* What they bring me (decision, options, or question), how they handle the first surprise, and their own self-assessment.
- *A time you misjudged someone's stage?* **[NEEDS YOUR STORY]**
- *Doesn't directive undercut ownership?* Not if it ends with the incident and the area owner leads the follow-through.
- *What would your team say your style is?* **[NEEDS YOUR STORY: confirm with real feedback]**
- *Your default mode?* Coaching, which is exactly why I use a deliberate model.

### ★ Q2. What changed for you when you moved from tech lead to manager?

The biggest change was how I create value. As a tech lead, I created value by doing. As a manager, I create value by building the system the team runs on.

By doing, I mean I solved problems myself: I made the technical call, wrote the hard part, and unblocked people with my own answers. The team's output depended on mine.

As a manager, my job is to own that system. I design it: who owns what, how decisions get made, what good looks like. I bring people into it and grow them until they can run their part on their own. I watch whether it's working. And when it breaks, I fix the system, not just the symptom. When my team was spending half its time in meetings, I didn't ask people to work harder. I consolidated four stakeholder syncs into one and protected a no-meeting day, and we got meeting time down to about 20 percent.

My test is simple: if I'm out for two weeks, does the team slow down? If it does, the system isn't done yet.

*Jay angle: this is his "new role with an old operating system" and "answer machine" idea, told as your own story. Don't quote his framework back to him. He builds data platforms, so one short line works if natural: "I think of the team the way I'd think of a production system: design it, run it, monitor it, and fix it."*

**Likely follow-ups** (full answers, delivery checklist, and practice log in [leadership/tech_lead_to_manager.md](../../leadership/tech_lead_to_manager.md)):

- *How did you learn that?* VoltronData: tried to code full-time and manage full-time; cut to 10–15% hands-on and started asking "what would you do?"
- *Hardest thing to let go of?* Being the person with the answer. Answering took the learning away from them.
- *How do you know the system is working?* Decisions still coming to me each week, shipping when I'm not in the room, what I hear in 1:1s, stakeholders going to pod leads directly.
- *Technical credibility at 10–15%?* Depth on the work where judgment matters most: design reviews, spikes, critical bugs.
- *How did the team react when you stepped back?* **[NEEDS YOUR STORY]**
- *Do you miss coding?* Sometimes, but watching someone own a problem I used to own is the part I wouldn't give up.
- *An IC habit you still watch?* Over-explaining. Give the goal and constraints, and let them work out the rest.

### Q3. What kind of team and culture do you want to build?

I want a team where people have the context to make good decisions on their own, and the safety to say when something's wrong.

To me, culture isn't the values on a wall. It's what you protect when it costs you something. So there are three things I actually enforce.

First, clarity. Everyone knows the goal, who owns what, how decisions get made, and why we're doing the work, not just what. When that's explicit, nobody has to route decisions through me.

Second, transparency by default. I don't wait for people to ask. I share the context up front: the roadmap, the business reason, what leadership is worried about. I publish notes from stakeholder meetings so nobody has to attend just to stay informed. And it goes both ways: feedback comes early, so nobody is surprised at review time.

Third, safety to disagree and to fail. When two of my senior engineers deadlocked on a model architecture, I didn't pick a winner. Each wrote a one-page design doc, we debated the trade-offs as a team, and we landed on a hybrid. Since then the rule is: propose, debate, decide, and then everyone commits. And when something goes wrong, we ask what in the system allowed it, not who to blame.

At Rula, I'd add one more: every engineer should be able to say how their work helps a patient get care. What I'm going for is a team where the healthy way to work is also the easy way, so great people can do their best work.

*Jay angle: the close echoes his "the safest and healthiest path is also the easiest path" and "an environment where great people can do their best work," in your own words. Proof is different from Q2 (meeting load is used there).*

**Likely follow-ups** (full answers in [leadership/building_team_and_culture.md](../../leadership/building_team_and_culture.md)):

- *How do you know people feel safe to disagree?* They disagree with me with data, bad news arrives early, juniors speak in reviews, people report their own mistakes.
- *A time someone made a mistake?* My own: the blindsided engineer. Owned it, fixed the system (feedback within a week, mid-cycle check-ins).
- *Someone goes against the culture?* Early and private; check if the expectation was clear first; then the standard feedback structure. **[NEEDS YOUR STORY]**
- *Different from your team today?* **[CONFIRM: your real gap]**
- *Isn't propose-debate-commit slow?* Only for big, hard-to-reverse calls; reversible ones the owner just makes.
- *How do you keep culture as the team grows?* First hires set it; write standards down early.

---

## Step 2 — Find the Leadership Drag

**Jay's lens:** His diagnosis starts with naming the drag honestly — where your current habits are costing you energy, clarity, trust, or team ownership. He listens for the cost, not just the habit: what did the old operating system actually cost you and the team?

### ★ Q4. Tell me about a time you were the bottleneck. What did you change?

When I started managing the fraud ML team, I was the bottleneck, and it took me too long to see it.

The team had four areas, and each had its own stakeholders: a product manager, data scientists, data and backend engineers, and business partners. Every area had a weekly sync, and I was in all four, plus every decision that came out of them.

I noticed it in three ways. Decisions waited on me while I switched between areas. My calendar was every area's stakeholder calendar. And the engineers closest to each problem, who had the most context, were bringing their decisions to me instead of making them. **[ADD A REAL NUMBER]**

The problem wasn't my time, it was the design. I came up as a tech lead, and my instinct was: if something matters, I own it. That worked for one team. It didn't work for four areas.

So I made three changes. Each area got an owner, usually the senior engineer with the most context. I wrote down the decision rights: inside their area, they decide and tell me after. Anything that crosses areas, touches another team's metrics, is expensive to reverse, or changes headcount comes to me. And I handed over gradually: I co-ran their syncs for a few weeks, then sat in while they ran them, then stepped out. Now I read the sync notes and join when they need me, plus a weekly owners' sync where cross-area issues come up.

That freed me to work on the whole team: the roadmap, hiring, and how the areas fit together. **[ADD REAL RESULTS]**

It's not fully solved. On high-stakes calls my instinct is still to step in early. But now I catch it, and I track it by how many decisions still come to me each week.

*Jay angle: this is his "find the leadership drag" and "rebuild delegation and ownership" steps, told as your story. Full file, checklist, and follow-ups: [leadership/bottleneck_story.md](../../leadership/bottleneck_story.md).*

**[CONFIRM BEFORE USING LIVE: (1) team shape. Nov 22 practice says four areas inside fraud ML; Q1, Q2, Q5, Q19, Q26 and leadership/weaknesses.md say two pods (support automation and fraud & risk ML). Make them all match. (2) Real before/after numbers: decisions reaching you per week, recurring meetings, owners who grew, stakeholder feedback.]**

### ★ Q5. What's your biggest weakness as a manager?

*Jay will likely ask Q4 first, so don't retell the bottleneck story here. Use the answer-man instinct (below). Backup: negative feedback (`leadership/weaknesses.md` #3).*

My biggest weakness is that my instinct is to be the person with the answer. I was an engineer for eight years, and when someone brings me a problem, part of me wants to say, "Here's your answer," or just take it and do it myself.

It shows up in two ways. In 1:1s, when a junior engineer brings me a problem, I want to hand them the solution. And with real work: recently we needed to compare two fraud models, and my instinct was to run the POC myself.

The cost is real. If I answer too early, they don't build the skill, they learn to bring every problem to me, and I miss their ideas. Some of the best solutions on my team came from someone else's angle, not mine.

So I've built a habit. When someone brings me a problem, I ask first: "What do you think?" or "What have you tried?" If they're stuck, I give a hint, not the answer. And before I pick up any task, I ask myself, "Is this something only I can do?" **[REAL EXAMPLE OF IT WORKING: the POC handoff, or a 1:1 where their idea beat yours.]**

The instinct hasn't gone away. But now I notice it before I act on it.

*Jay angle: his "answer machine," in your own words. Have the balance line ready: "When it's urgent, high-stakes, or they've asked twice, I just give the answer." Full version, checklist, and follow-ups: [leadership/weaknesses.md #4](../../leadership/weaknesses.md#4-the-answer-man-instinct).*

### Q6. What's a belief about management you've changed your mind on?

I used to think my job was to have the answer. Now I think my job is to build the system that produces answers without me — and to name the fear that's keeping me in the answer seat.

The concrete version of that change is about feedback. Early on, I thought 1:1s were for check-ins, not feedback. I thought I was protecting the relationship by softening hard messages. Then an engineer got blindsided in a performance review because I'd never told him the expectation clearly — and he was right to be blindsided. That was on me. What I learned is that the discomfort of giving feedback early is much cheaper than the damage of giving it late. Now feedback happens within a week of noticing, in the 1:1, with a clear structure, and nobody is surprised at review time.

There's a second piece I took from Jay's own writing, actually — the idea of failing faster. I used to treat a miss as something to avoid. Now I treat it as fuel, but only if we name what actually happened. The fraud threshold call, the pod-lead handoff — both of those only worked because we said plainly what went wrong first. The fear doesn't go away by avoiding it; it goes away by addressing it at the root.

---

## Step 3 — Rebuild Delegation and Ownership

**Jay's lens:** His #1 diagnostic is whether everything still runs through you — "You know too much, so everything runs through you… You become the answer machine." He listens for a *delegation system*, not good intentions: written decision rights, a handoff plan, and how you inspect without micromanaging.

### Q7. How do you delegate without lowering the bar on quality?

By being explicit about what "good" means before I hand something over, and by inspecting outcomes instead of process.

The delegation system has three parts. First, written decision rights: inside your scope, you decide and inform me after. Cross-team, hard to reverse, or headcount — those come to me. The line is explicit, so nobody has to guess whether they should ask. Second, the quality bar lives in the artifact, not in my head: design docs, decision logs, and eval gates. When we unified 60-plus fraud models into one system, I couldn't review every model myself — so the bar became the evaluation: offline metrics plus a shadow run before anything shipped. Third, a gradual handoff: I co-run, then I sit in, then I step out. Stakeholders keep trust, and the person taking ownership gets coached, not dropped in.

A good example is the support review work. We cut review time from 30 minutes to 5 by building an eval-driven pipeline — but the quality bar was the eval set itself. Once that existed, engineers could move fast without me checking every case, because the system caught regressions. That's what delegation should feel like: the standard is enforced by the system, not by my calendar.

### Q8. How do you know when to step in on a technical decision — and when to stay out?

I have a simple rule. I step in when the decision crosses teams, is expensive to reverse, or needs judgment the team can't see yet — usually because it touches another org's metrics or a commitment I made. I stay out when it's reversible and inside their scope, even if I'd decide differently. That's the hard part: letting a good-enough decision stand because the ownership matters more than the extra five percent.

A real example: two of my senior engineers deadlocked on a model architecture. Instead of deciding for them, I had each write a one-page design doc, ran a structured discussion — assumptions, tradeoffs, unknowns — and we landed on a hybrid. Then we set the standing rule: senior engineers propose, the team debates, I break ties if needed, and then everyone commits. The commitment half is what makes the disagreement safe.

I stay technically close enough to judge well — I review design docs async, I do design reviews on major projects, I keep about 10 to 15 percent hands-on. But I don't review every PR, and I don't sit in every meeting. If I'm the only reviewer at 6 people, I'm a bottleneck at 12 and a liability at 20.

---

## Step 4 — Strengthen Performance and Hard Conversations

**Jay's lens:** He sells a "Performance Conversation Framework" and "Hard Conversation Scripts" — he listens for structure and timing, not courage. The signal is: feedback early, expectations in writing, no one surprised at review time. His scripts explicitly cover conflict, expectations, **former peers**, stakeholders, and direct reports.

### ★ Q9. How do you handle an underperforming engineer?

My rule is that a performance review should never be the first time someone hears they're behind. So I catch it early, diagnose before I judge, and agree on a clear plan.

Early: I watch for patterns, not one bad week: missed commitments, quality slipping, someone going quiet. When I see a pattern, I raise it in our next 1:1, not at review time.

Diagnose: I ask three questions, in order. Clarity: do they actually know what good looks like? Often it's a communication problem, not a capability one. Fit: are they in a role that plays to their strengths? Support: have I given them the time, tools, and help they need? And sometimes it's something personal, so I ask.

Agree a plan: I tell them what I see, what good looks like, and I ask for their view. If we see it differently, that's the conversation. Then we write down a plan with specific goals, a timeline, and weekly check-ins.

Example: I had a backend engineer who was struggling on his team. The easy path was a performance plan, but the diagnosis said fit, not effort: he was strong in infrastructure, just in the wrong seat. We moved him to the infrastructure side, and he became core to our platform work.

If it doesn't improve: if the plan runs its course and the gap is still there, we have an honest conversation about fit, and I bring in HR if it needs to become formal. The goal is that whatever happens, whether they improve, move, or leave, nobody is surprised and it's fair.

*Home of the backend-engineer story: in Q11, Q24, Q25, Q34 refer back to it in one line. Don't imply you've run a formal PIP (Q11: you haven't managed anyone out).*

**Likely follow-ups, with hints** (full answers in [leadership/underperformance.md](../../leadership/underperformance.md)):

- *How long before it's formal?* **4–8 weeks, said up front.** **[CONFIRM against your company's process]**
- *They disagree with you?* **Examples, their view, a measurable test.** "Let the result settle it."
- *Personal cause?* **People first, HR, privacy, then back to the plan.**
- *Effect on the team?* **Private, rebalance, thank.** "Ignoring it hurts the high performers most."
- *Ever had someone not improve?* **Honest no; the fit check changed the answer.**
- *Strong performer slipping?* **Something changed: ask what.** Usually a conversation, not a plan.

### ★ Q10. Tell me about a difficult conversation you had. How did you prepare?

The hardest conversation I've had was earlier this year, with my tech lead. For months we'd been preparing him to become an engineering manager. Then an org change took that path away, and I had to tell him.

Context: he wanted to move into management, and we'd built a real plan together: the skills, feedback from leadership, the calibration. It was going well. Then midyear, with **[a hiring freeze / reorg]**, the company set a new rule: every manager needs at least 10 to 15 reports. Our team couldn't support a second manager, so the promotion was off the table.

How I prepared: first, I got the facts straight from leadership: what was final, and what might change. Second, I decided what I could honestly offer, and what I couldn't promise. Third, I thought about how he'd feel. He'd done everything right, so I knew this would feel unfair. And I didn't wait: I told him within **[a day or two]** of hearing, so he wouldn't hear it from anyone else.

The conversation: I said it in the first minute, clearly: the manager role isn't going to happen right now, and here's why. He was disappointed and asked, "What happens now?" I didn't rush past that. I acknowledged it was unfair given the work he'd put in. Then I gave him the honest picture and a plan: he'd keep growing as a manager without the title. He now leads a sub-team of the fraud ML team, mentors them, and does most of a manager's job. I was clear that I couldn't promise a date, only that if the team grows, he's the first person I'll put forward.

Result: it took a month or two, but he came back fully engaged. **[REAL RESULT]**

What I learned: don't tie someone's growth plan to a title or a date you don't control. Now I build growth plans around readiness and scope, so a change in the org doesn't erase the progress.

*Jay angle: hard conversations with structure and timing, plus calm authority when bad news comes from above. If he asks Q16 later, refer back in one line. Full file, prep notes, follow-ups with hints: [leadership/difficult_conversation.md](../../leadership/difficult_conversation.md).*

**[CONFIRM BEFORE USING LIVE: the cause (hiring freeze / reorg / span rule), "calibration" vs "certifications," how fast you told him, the real result, and whether you actually said "no date, but you're first."]**

**Likely follow-ups, with hints:**
- *What did you say in the first minute?* **News first, then why.**
- *Could you have seen it coming?* **Own the date, not the org.** "I tied his plan to a title and a timeline I didn't control."
- *How did you keep him from leaving?* **Real scope, honest odds, regular check-ins.**
- *How did you handle the rest of the team?* **His news first, his to share.**

**Backup story (blindsided engineer), if the tech-lead story was already used:**

Giving negative feedback is harder for me than it should be. I care a lot about the team's trust, and early on I'd soften the message or wait for a better moment — which is really just postponing it.

It caught up with me as a new manager. I had a performance concern about one engineer that I'd hinted at but never said directly. When I finally raised it clearly, he was blindsided — and he was right to be. I'd never set the expectation in the first place. That was on me.

I went back, told him that directly, and we rebuilt the plan together. Then I changed how I run feedback for everyone. I use a simple structure — what I observed, why it matters, what good looks like, how I'll help — which takes the emotion out and makes it about the work. I give it within a week of noticing, in the 1:1, not saved for review season. Every engineer gets a mid-cycle check-in. And I got coaching from our HR partner on difficult conversations, including practicing a couple before I had them.

He stayed, his performance recovered, and the whole team got clearer expectations out of it. I track one thing above all: nobody is surprised at review time. It still isn't comfortable for me, and I don't think it should be — but I don't let discomfort set the timing anymore.

### Q11. Have you ever had to manage someone out?

No — and I want to be straight about that rather than dress something up. I haven't managed anyone out.

The closest I've come is the repositioning I just described: an engineer who was struggling in one seat, and instead of starting a performance process, we moved him to infrastructure work where his strengths actually fit, and he thrived there. My view is that managing someone out should be the last step after you've honestly checked clarity, fit, and support — and in the cases I've faced, the fit check changed the answer. If I ever do have to manage someone out, I'd want it to be after that same honest sequence, with clear expectations in writing and no surprises.

### ★ Q12. Tell me about a time you had to lead former peers — people who used to be at your level, or who you used to work alongside. How did you handle the shift?

I lived the adjacent version of this when I inherited a team of ten after their manager left — I wasn't their peer, but I was new authority to people who already had their own ways of working. I started by diagnosing before changing anything: in the first 1:1s I asked what was missing with the last manager and where they wanted to go, and I changed one visible thing fast — consistent 1:1s and protected focus time — and never missed it.

The rule I kept was: no surprises, expectations in writing, and earn the authority by absorbing the org load instead of passing it down. People judge a new manager by whether the first stated commitment survives contact with pressure — so I picked something small, painful, and real, and I held it. With former peers specifically, the hardest part is that the relationship changes and pretending it hasn't is what breaks trust — so I name the shift directly, I don't pull rank to settle old debates, and I let their work, not my title, do the convincing over time.

**[NEEDS YOUR STORY: a true former-peer case — who, what changed in the relationship, one hard moment. The inherited-team story is adjacent, not a former-peer story. Do not use this answer live until those details are real.]**

### Q13. Tell me about a time two people on your team were in conflict with each other. What did you do?

Two of my senior engineers deadlocked on a model architecture, and the disagreement was starting to cost us. Instead of deciding for them, I had each write a one-page design doc, then ran a structured discussion — assumptions, tradeoffs, unknowns — and we landed on a hybrid. Then we set the standing rule: senior engineers propose, the team debates, I break ties if needed, and then everyone commits. The commitment half is what makes the disagreement safe.

What I learned from it is that most team conflict isn't really about the technical question — it's about who gets heard and who decides. So my job in the conflict was to make the decision process explicit before anyone had to defend a position in public. Once the process was fair, the people could disagree without it becoming personal.

---

## Step 5 — Practice Calm Authority

**Jay's lens:** "Calm Authority" is the end state of his system — lead "without brute-forcing everything," "not urgency, not ego." He listens for steadiness under pressure, and for whether trust was built *before* it was needed.

### Q14. How do you build trust with a team — especially one that didn't choose you?

I inherited a team once — ten engineers, my manager had left, no interim — so I've actually lived this. The first thing I did was diagnose before changing anything. The first 1:1 question that mattered wasn't "what are you working on," it was "what was missing with the last manager?" and "where do you actually want to go?" You're finding out what the team believes about how this place works before you try to change it.

Then I changed one thing visibly and fast. People judge a new manager by whether the first stated commitment survives contact with pressure. I picked something small, painful, and real — consistent 1:1s and protected focus time — and I never missed it.

The deeper principle is that trust is built by removing surprises. Expectations in writing, feedback mid-cycle, no one blindsided at review time. And I try to be the surface the organization pushes against, so the team doesn't have to be. When people see you absorb the org load — the meetings, the stakeholder noise — instead of passing it down, they start to trust that you've got them. That's what calm authority actually is: not being loud, just being steady and predictable when it counts.

### Q15. Tell me about a time you led under real pressure. How did you keep the team steady?

The clearest one is the support automation work at DoorDash. Our escalation rate was 67 percent — two out of three cases were going to a human — review time was 30 minutes a case, and manual tickets were running 500 per 10,000 orders. The team was drowning, and every stakeholder wanted their issue first.

What kept us steady wasn't heroics, it was cadence and one clear system. I named the problem honestly to the team and to stakeholders: we're not going to fix this by working harder, we're going to fix it by building an agentic pipeline with real evals. I protected focus time — a no-meeting day, one consolidated stakeholder sync instead of four — so the team could actually build. And I gave them a single, measurable target to rally around instead of ten competing asks.

The results: escalation went from 67 percent to just over 50 percent, review time from 30 minutes to 5, manual tickets from 500 down to 260 per 10,000 orders. The lesson I took from it is that under pressure, the manager's job is to narrow, not to widen — one priority, one system, a steady rhythm — and to absorb the noise so the team can hear itself think.

### Q16. When something goes wrong — an outage, a missed deadline, bad news from above — how do you communicate it to the team?

I name the problem honestly and I narrow, not widen — during the support automation crunch, escalation was 67 percent and the team was drowning, so I gave them one measurable target instead of ten competing asks and absorbed the stakeholder noise myself. I'm transparent about the facts and the plan, but I don't pass my anxiety down — the team should hear steadiness from me, not urgency.

What I've learned is that there's a difference between transparency and dumping. Transparency is: here's what happened, here's what we know, here's the plan, here's what I need from you. Dumping is letting the team carry my stress about it. So I separate the two — I tell them the facts early, even when the facts are bad, because silence is what actually scares people. Then after the fix, we do the learning: what did we see, what do we carry forward, so the next time we're faster and calmer.

### Q17. How do you manage your own energy and pressure as a manager — what does your operating rhythm look like?

I know my engine: I'm a coach by instinct, so my risk is over-coaching and over-explaining when I'm under pressure, and carrying too much in my head. My rhythm is weekly: a pod-lead sync for cross-team issues, 1:1s built around growth not status, and protected focus time — I held a no-meeting day against real pressure because that's when the real work gets done.

And I track the numbers that tell me if I'm slipping back into the bottleneck: how many decisions still come to me per week, how many stakeholder meetings I'm in. When those numbers climb, that's my signal to step back and rebuild the delegation — not to work harder. The operating rhythm is the thing that keeps me steady, because pressure doesn't go away; the system is what absorbs it.

---

## Coaching-First Management & Leveling

**Jay's lens:** He always starts as a coach — "understanding who is this person, what's their motivation, and let's identify their unique strengths" — but he will test whether you know coaching is only about twenty percent of the job, and when to take the hat off.

### ★ Q18. How do you coach and mentor your engineers? How do you know it's working?

I start with listening, not telling. A coaching-first approach for me begins with active listening — really hearing the person, their aspirations, their concerns — and then asking open-ended questions instead of handing over the answer. "How do you feel about this approach?" "What do you think could be a potential solution?" That does two things: it builds ownership, and it builds their critical thinking, because they have to arrive at the insight themselves.

My 1:1s are built for this. A few minutes on how they're doing, most of the time on what's blocking or exciting them, and a regular career check-in. And I try to build personalized growth plans around strengths — not just what someone's good at, but what kind of work *energizes* them. One engineer on my team was frustrated by meetings and needed deep focus time; another wanted to learn production systems. Once I understood that, I could unblock them completely differently.

How do I know it's working? Three signals. People start bringing me decisions they've already made, not decisions they want me to make. They give each other feedback directly instead of routing it through me. And they disagree with me in a meeting, with data. When those three things are happening, the coaching is landing — because the point was never to make them dependent on me, it was to make them stronger without me.

### ★ Q19. How do you approach leveling and promotions? How do you keep it fair?

I'm very transparent about it. I tell every report: here's what's expected at your level, here's what I believe that looks like for you specifically, and let's talk about it. If you have aspirations for the next level, let's discuss what that looks like for you — because what I've found is that people are most frustrated not when they're told no, but when there's no clear expectation at all. "You did great" — great at what? "You were inconsistent this quarter" — inconsistent against what?

The second half is that I don't put people in a box. The level framework is real, but the unique version of it is per person. One engineer might be an empathizer, another a deliverer — you don't have to be your colleague to be at the same level as your colleague. So I look for the version of the next level that fits their strengths, and then I give them stretch work that proves it, and I mentor them publicly so the rest of the org can see it.

Two of my pod leads grew into senior scope exactly this way — they took on stakeholder alignment and technical decisions for their teams, and the promotion case wrote itself because the work was already visible. My rule is: the promotion should be a recognition of work already being done, not a promise about future work.

**[NEEDS YOUR STORY: name one specific promotion — who, from what level to what, and the stretch assignment that made the case. The repo references this story (S7) but the details weren't pulled.]**

### ★ Q20. When do you coach, and when do you just give the answer?

This is the hardest judgment call in management, and I had to learn it by getting it wrong. My natural inclination is to coach — I wake up wanting to coach people. But I walked into management assuming coaching *was* management, and within a few months I saw the problem: coaching takes time, and management doesn't always have it. If I coach everything, I create dependence — people who need me to rebuild their confidence every week instead of holding onto their own strength.

So now I sort it three ways. I coach when the person already has the answer and needs to find it — that's where growth and ownership live, and the blast radius is small. I give limited space when there's a real tradeoff: I'll say, "take two days to explore it, then bring me what you've got" — a cost-benefit call, because letting someone walk too long has dependencies attached. And I direct explicitly when it's urgent, high-stakes, or they've already asked twice. In those cases I tell them exactly what I want and exactly how I want it done, and I explain what I'm expecting so it's fair.

The signal I watch for is dependence. If someone's confidence collapses between our 1:1s and they need me to rebuild it every time, I'm over-coaching. The goal is the opposite: that they leave the conversation holding their own reasons to move, not mine.

### ★ Q21. Who coaches you? How do you stay coachable as a manager?

I have a coach in the form of our HR partner — when I had to have difficult conversations I practiced a couple with her first, and that changed how I give feedback. I also ask my reports directly in 1:1s what's working and what isn't about how I lead — if I'm asking them to be coached, I have to model being coached.

And honestly, this interview prep is part of it: I'm studying how Jay thinks about leadership because I want to keep rebuilding my own operating system. The day I stop being coached is the day I start assuming my instincts are right — and my instincts are exactly what got me into the bottleneck in the first place.

### Q22. How do you decide how much direction to give someone — how do you calibrate it to the person and the skill?

It varies by person and by skill — someone can be senior in one area and a beginner in another, so I don't give one person one fixed amount of direction. When someone already has the answer, I coach; when there's a real tradeoff, I'll give them bounded space — "take two days, bring me what you've got"; when it's urgent or they've asked twice, I direct explicitly.

The way I think about it is a competence spectrum: someone who's unconsciously competent in one skill can be unconsciously incompetent in another, and the amount and directness of direction has to follow the skill, not the title. The signal I watch is dependence: if their confidence collapses between 1:1s, I'm over-coaching. If they're stuck and not asking, I'm under-directing. Calibration is a weekly judgment, not a fixed style.

### Q23. How do you help a fellow manager who's struggling with the people side?

I start by exchanging notes, not giving a lecture — I want to improve on the strategy side, they want to improve on the people side, so we make each other better. The first thing I usually share is the 1:1s: I set them up with everybody in my perimeter, even people I have no work with, because knowing someone before you need them changes everything.

And I tell them the thing I had to learn myself — that coaching is only about twenty percent of the job, and the rest is systems: delegation, expectations in writing, and hard conversations on time. If they're over-coaching, I share the dependence signal I watch for; if they're avoiding the hard conversation, I share the structure I use — what I observed, why it matters, what good looks like, how I'll help.

**[NEEDS YOUR STORY: one real peer-manager example — who, what you shared, what changed.]**

---

## Recruiting & Growing Teams

**Jay's lens:** He's a hiring manager at Rula right now, and he joined Rula partly "to help grow this team… building an environment where great people can do the BEST work." He listens for a real bar, not a vibe — and for whether growth is a system, not a favor.

### Q24. Tell me about a team you built from scratch.

I built my current setup from nothing — 12 engineers across two pods, support automation and fraud and risk ML. Three things I got right, and one I'd do differently.

First, the first three hires are the culture. Whatever they do becomes the norm before you ever write anything down. So I hired for the behavior I wanted copied, not just the skills I needed that quarter. I hired for strengths rather than the req — one engineer who was strong in infrastructure became core to our platform work, even though he started in fraud detection.

Second, I said what "good" means on day one, in writing. Not values — standards. What a design doc contains, when you write one, what gets reviewed and by whom, who decides when people disagree. New people join a vacuum and fill it with guesses, and those guesses become the culture — much harder to change at 12 than at 3.

Third, I gave away decisions early, before it felt safe. Senior ICs owning areas and reviewing each other's work is what lets a team scale past my own attention. If I'm the only reviewer at 6 people, I'm a bottleneck at 12 and a liability at 20.

What I'd do differently: I'd write down the decision rights from the start instead of absorbing everything first and delegating later. That three-month lag I mentioned — where every decision still ran through me — was the cost of learning that lesson. Now when scope changes, I set up the owner and the decision rights at the start.

### Q25. How do you hire? What do you look for?

Four things, in order. Technical foundation — can they think through systems, can they code, do they understand ML fundamentals for the fraud side. Learning mindset — have they grown in past roles, do they ask good questions. Communication — can they explain complex ideas clearly, because that's critical on cross-functional teams. And judgment — how do they decide under uncertainty. In interviews I like to walk through a recent real decision with them and see how they reasoned.

I stay involved personally — I do technical interviews and culture assessments myself, and I give engineers on the team a voice in hiring, because they usually spot things I miss. And I hire for strengths, not the req. The infra-strong engineer I mentioned is the example: on paper he was a fraud-detection hire, but his real strength was platform thinking, and once I saw that, I put him where that strength compounded. Hiring is the highest-leverage thing I do, so I don't delegate the bar.

**[NEEDS YOUR STORY: one "best hire" story with a name and specifics — how you found them, what you saw in the interview, what they became. The question bank lists this as a standard question.]**

### Q26. Tell me about someone you promoted. What did you do that made the difference?

The honest structure of the answer is: who they were, what the gap was, what stretch I gave them, and what changed in them — not just in their title.

The clearest case I have is one of my pod leads. They started as a strong senior IC — deep context on the scope, good judgment, credibility with stakeholders — but they were still bringing every decision to me. The stretch was real ownership: their team's stakeholder alignment and technical decisions, with written decision rights so the line was explicit. I co-ran their stakeholder meetings for the first month, then sat in while they ran them, then stepped out. Within a few months they were making harder calls on their own, and the stakeholders trusted them directly — the promotion case wrote itself, because the work was already visible at the next level.

Would they have gotten there without me? Eventually, maybe — they had the ability. But I think the deliberate part mattered: naming the stretch, making the decision rights explicit, and creating the visibility so the rest of the org could see it. That's the difference between hoping someone grows and actually growing them.

**[NEEDS YOUR STORY: fill in the person's name, the levels involved, and one concrete decision they made independently that proved the promotion. Do not use this answer live until those details are real.]**

---

## Cross-Team Coordination & Technical Roadmaps

**Jay's lens:** His own career is cross-functional translation — a Data Governance Council with Legal, Finance, Product, and Engineering; a Redshift-to-Databricks migration across teams; 1:1s with everybody in his perimeter. He listens for how you build alignment *before* you need it, and for roadmaps argued in business terms, not technical ones. (Note: he has no published roadmap framework of his own — don't attribute one to him.)

### Q27. How do you set a technical roadmap when the goals are still being defined?

I work backward from the business problem, not forward from the technology. On the fraud side, the framing was: fraud is a growing threat, our current model catches 40 percent with 2 percent false positives, and we want to catch 60 percent with under 2 percent false positives. Then: what's blocking us — model architecture, feature engineering, throughput? Then what's the 6-month roadmap to get there — new model training, data pipeline improvements, and so on. I bring the team in to debate the approach, but I own the strategy. And I adjust based on what we learn — if we hit a technical wall, we pivot.

Two rules I hold. First, we're not building cool things, we're solving real problems — that alignment keeps the team motivated. Second, the roadmap is written in business units, not technical ones. When I report up, the first line is the decision or the ask, the second is the business impact — dollars, customers, risk — and the technical detail is an appendix, not the talk track. The fraud threshold discussion is the example: instead of debating precision and recall, I put fraud dollars prevented and legitimate customers blocked on the same chart at each threshold. The room argued about a number instead of a principle, and we agreed on a phased rollout in one meeting.

If I were setting a roadmap at Rula, I'd start the same way — with the clinical and operations problem, not the model. What does the care team need to decide faster or better, and what's the smallest system that proves it?

### ★ Q28. Tell me about a cross-org initiative you drove.

The biggest one is unifying fraud detection. We had 60-plus separate fraud models, built by different teams at different times, each with its own owner, its own features, its own blind spots. My job was to bring them into one system — one evaluation framework, one serving path, one set of ownership rules.

The technical work mattered, but the alignment work mattered more. I started by setting up 1:1s with everybody in my perimeter — the teams that owned the models, the product partners, the risk and operations folks — even when I had no immediate work with them. When the time came to ask them to give up their model, I wasn't a stranger making a demand; I knew what they cared about, and they knew I saw the value in what they'd built. That sounds soft, but it's the whole game: people don't hand over their system to someone who hasn't taken the time to understand it.

The other cross-org win was the restaurant underwriting work — a $1M pilot that grew to $25M. Same pattern: start with the business problem in their language, prove it small, then scale with their trust already earned.

**[NEEDS YOUR STORY: for the 60-model unification — which teams/orgs were involved, how long alignment took, and one moment where a team resisted and what you did. The repo references this as a cross-org story but the mechanics weren't pulled.]**

### Q29. How do you say no to a partner team or a senior stakeholder?

With an alternative, not a wall — and with a clear statement of what the boundary protects.

A real example: Product wanted our fraud team to also take on chargeback prevention. It was a real problem, but it was a different problem space, and absorbing it would have diluted the team's focus. So we said: that's a different problem space, we can advise, but you need a dedicated team. And then I helped them hire the first engineer for it. Saying no while helping them solve it is very different from saying no and walking away — the relationship got stronger, not weaker.

The same principle applies inside the team. I held a no-meeting day against real pressure from partner teams, because focus time was the thing my engineers needed most. Boundaries only work if you hold them when holding them costs you something — the moment you make an exception, the boundary is gone. So I decide the boundary in advance, I explain what it protects, and I offer the next-best help I can actually give.

### Q30. What do you do when the goals coming down from above are vague or keep moving? How do you create clarity for your team?

I work backward from the business problem, not forward from the technology — on the fraud side I framed it as: we catch 40 percent with 2 percent false positives, we want 60 percent with under 2 percent, so what's blocking us. Then I give the team one measurable target instead of ten competing asks, and I own the ambiguity upward instead of passing it down.

If I can't get clarity from above, I still won't let the team sit in fog — I'll name the decision we're making, the assumption behind it, and when we'll revisit it. Clarity isn't something a good boss hands you; it's something a good manager creates in the middle of the fog. And I use the 1:1s for exactly that: to reduce ambiguity, sharpen alignment, and make each person's value legible — including my own, upward.

### ★ Q31. How do you get a team to adopt AI tools well — and how do you build guardrails so the safe path is the easy path?

The quality bar has to live in the system, not in my head. On the support side we cut review time from 30 minutes to 5 with an eval-driven agentic pipeline — the eval set itself was the guardrail, so engineers could move fast without me checking every case because the system caught regressions.

Same idea for AI adoption: give people a paved path with evals and shadow runs first, so the safe way is also the fastest way, and keep humans on the high-stakes calls. That's the design principle I'd bring to Rula too — the safest and healthiest path should also be the easiest path, or people will route around it. Adoption isn't a training problem, it's a design problem: make the right way the easy way, and measure whether people actually use it.

**[NEEDS YOUR STORY: one concrete AI-adoption example at DoorDash — which workflow, what guardrail, what changed.]**

### Q32. Tell me about a time you led your team through a big change — a reorg, a migration, a new direction. How did you bring people along?

Unifying 60-plus fraud models into one system was as much a change problem as a technical one — people were being asked to give up models they'd built. I started with 1:1s with everybody in my perimeter before I needed anything from them, so when the time came I wasn't a stranger making a demand. I knew what they cared about, and they knew I saw the value in what they'd built.

And the support automation shift worked the same way: I named honestly that working harder wouldn't fix it, gave the team one system to rally around — an agentic pipeline with real evals — and protected their focus time while we built it. Change lands when people understand the why before they're asked to give up the how — and when the person asking has already earned their trust.

---

## Alignment & Positioning (RareStack)

**Jay's lens:** His book's system is Surface → Structure → Land: name the gap between how you operate and how you're perceived, build positioning language and an operating rhythm that forces alignment, then turn clarity into behavior, positioning, and career movement. He listens for whether you can see your own perception gap — for yourself and for your team — and close it. "Lead with alignment, not performance — Build with purpose, not pressure."

### ★ Q33. How do you make your team's work visible to leadership — how do you position impact so it actually lands?

I report up in business units, not technical ones — the first line is the decision or the ask, the second is the business impact, and the technical detail is an appendix. On the fraud threshold call, instead of debating precision and recall, I put fraud dollars prevented and legitimate customers blocked on the same chart at each threshold, and the room argued about a number instead of a principle — we agreed a phased rollout in one meeting.

I also mentor people publicly so the org can see the work at the next level before the promotion conversation ever happens. The pattern is the same either way: stop over-explaining and start being understood. If the work is strong but the signal isn't landing, that's my problem to fix — not the team's, and not leadership's.

### Q34. How do you tell whether someone on your team is burned out or just misaligned — and what do you do differently in each case?

I start by asking what energizes them, not just what they're good at — burnout and misalignment look the same from the outside but need opposite fixes. If it's load, I protect focus time — we cut meeting load from about 50 percent to 20 percent and held a no-meeting day against real pressure. That's a load problem, and the fix is subtraction.

If it's fit, I move the seat, not the person — I had a backend engineer struggling on his team, and instead of a PIP we moved him to infrastructure, where he became core to our platform work. Misalignment isn't a performance problem, it's a design problem: the person is running a bad query against their own strengths. Fix the query — the role, the scope, the energy match — and the same person looks like a different engineer.

### Q35. How do you lead a team where people have competing values — one person who defaults to action, another who leads with empathy?

I don't try to make them the same — a well-rounded team needs both, and I tell them that. What I do is name the tension out loud and agree on when each value wins: in an incident, action wins and we debrief with empathy after; in a performance conversation, empathy sets the tone and action sets the follow-through.

The mistake would be to treat one side as the problem. The person who defaults to action is why things ship; the person who leads with empathy is why people stay. My job is to help each of them work on what they're working on — the action person practicing a pause, the empathy person practicing a decision — so the team gets both strengths instead of one strength and one resentment.

**[NEEDS YOUR STORY: one real pair of people and one real moment where their values clashed.]**

### ★ Q36. How do you set priorities — and how do you balance long-term and short-term work?

I use two principles, and I say them out loud so the team and I are deciding by the same rule.

The long-term principle: we reserve capacity every week for the long-term goal. The short-term principle: for each week, we optimize by impact — the few things that matter most right now, with a clear owner for each.

The starting split is roughly 70 percent short-term, 30 percent long-term — but the number isn't the point. The point is that we agree on the split together, we make it visible, and we review it weekly, so short-term wins don't quietly eat the future.

And the two aren't separate lists. When we plan each month or each quarter, we decompose the long-term goal into milestones, and the short-term work is built from those milestones — so this week's priorities are steps toward the long-term outcome, not a different list. During execution we still keep the reserved time for the long-term work. That's how you avoid the local optimum: every priority has a why, an owner, and a place in the bigger story.

*(Added Nov 21 from spoken practice in a voice call — his own wording, refined with the assistant. The 70/30 split is a starting point he offered, not a DoorDash policy.)*

---

## Questions to ask Jay (have 4 ready — never say "none")

1. **On his core tension:** "You write about coaching being only one of a manager's hats — where do you draw the line at Rula between coaching and directing, especially in a clinical setting where the stakes are patient care?"
2. **On success in the role:** "What does 'good' look like for this EM in the first 90 days — and what would worry you by day 90?"
3. **On leveling:** "You talk about level transparency — how does Rula define levels for the AI/ML team today, and where do you see the biggest leveling gaps?"
4. **His favorite closer:** "What else should I be asking that I didn't?"

---

## [NEEDS YOUR STORY] — fill these in before Tuesday

1. **Q4 delegation story** — pod-lead names; decisions reaching you per week (before/after); recurring stakeholder meetings count (before/after).
2. **Q12 former-peer case** — who, what changed in the relationship, one hard moment. (New — the inherited-team story is adjacent, not a former-peer story.)
3. **Q19 / Q26 promotion story** — one specific promotion: name, levels, the stretch assignment, one independent decision that proved it.
4. **Q25 best hire** — one hire story: how you found them, what you saw in the interview, what they became.
5. **Q4 follow-up: a recent slip** — one real recent case where you jumped into a delegated decision and how you caught it.
6. **Q28 cross-org mechanics** — 60-model unification: which teams/orgs, how long alignment took, one moment of resistance and what you did.
7. **Q27 roadmap detail** — the 6-month shape of the agentic support pipeline roadmap (phases, gates) so the fraud example isn't the only roadmap story.
8. **Q31 AI-adoption example** — one concrete case at DoorDash: which workflow, what guardrail, what changed. (New.)
9. **Q35 competing-values pair** — one real pair of people and one real moment where their values clashed. (New.)
10. **Q23 peer-manager example** — one real peer manager you helped: who, what you shared, what changed. (New.)
11. **Q1 follow-up: misjudged stage** — one case where you delegated too early or held on too long. The Q4 three-month lag is a candidate. (New, Nov 22.)
12. **Q1 follow-up: what your team would say** — confirm with real feedback (skip-level, 360, or a report's words) before using it. (New, Nov 22.)
13. **Q2 VoltronData symptom** — one real sign that coding full-time and managing full-time wasn't working (reviews piling up, cancelled 1:1s, a slipped deadline). Also settle 10–15% vs 20–30% hands-on (`leadership/tech_leadership_balance.md` says 20–30%). (New, Nov 22.)
14. **Q2 follow-up: how the team reacted** when you stepped back from coding — one concrete moment. (New, Nov 22.)

## Sources

Jay Floyd material (all read live, Nov 21, 2026):

- https://iamjayfloyd.com/ — homepage; People Leadership OS, five steps, "Technical skill got you promoted. People leadership is the job now."
- https://iamjayfloyd.com/books — *Rare On Purpose* framing ("leading without erasing yourself").
- https://iamjayfloyd.com/about — operator background; stakeholder tension; "turn who you actually are into the way you lead."
- https://www.rareonpurpose.com/ — RareStack (Surface → Structure → Land), Calm Authority outcomes, Accelerator/Intensive, both books.
- https://powertofly.com/up/zapier-build-coaching-into-your-management-approach — "5 ways to build coaching into your management approach," Oct 25, 2023; coaching-first, five recommendations, "Even the best coaches have their own coaches."
- https://uncommonteams.com/uncommon-leadership-interview-series/feed-your-good-wolf-jay-floyd/ — "Feed your good wolf," Apr 15, 2024; manager-vs-coach, over-coaching/dependence, level transparency, 1:1s with your whole perimeter, "Identify Your Seatbelts," "Fail faster."
- https://www.joinleland.com/jay-floyd — career history (Rula since June 2026; Zapier ~5.5 yrs), People Leadership OS packages, focus areas incl. former peer dynamics.
- https://www.joinleland.com/jay-floyd/o/the-leader-you-actually-are-coaching-for-technical-managers — $4,500, 10 sessions, package contents.
- https://www.joinleland.com/jay-floyd/o/leadership-reset-sprint-for-technical-leaders — $1,500, 4h, contents.
- https://www.mento.co/coaches/jay-floyd — strengths-based / High 5, One of One workshop, book attribution.
- https://podcasts.apple.com/us/podcast/on-everything-with-jay-floyd/id1726490780 — now *The Rare On Purpose Podcast with Jay Floyd*, 63 episodes; 8 most recent read ("Your Life Is a Bad Query," "Nobody's Handing You Clarity," "A Polished Life Can Still Be a Borrowed One," "Champions Hurt," "You Want It One Way. It's The Other Way," "Stop Naming What You Don't Want," "Between Cabrini and Love Jones").
- https://bookshop.org/p/books/rare-on-purpose-jay-floyd/0406856f1bc112c8 — *Rare On Purpose*, May 26, 2025, 150 pp., $17.99.
- Full research report: `research_notes/jay-floyd-rula-leadership-coaching-20261121-1821/report.md`
- Alignment audit: `goals/rula-next-stage-interviews/files/jay-floyd-content-alignment-audit.md`

User's own interview-prep repo (github.com/jitingxu1/interview-prep, public, main branch):

- `leadership/manager_qa.md` — 1:1s, underperformance, feedback structure, conflict, hiring, tech-lead/manager balance, technical strategy.
- `leadership/weaknesses.md` — three weaknesses with spoken versions; "Have you ever managed someone out? No. Say so plainly."
- `leadership/building_team_and_culture.md` — culture thesis, three mechanisms, meeting load 50% → ~20%, No-Meeting Thursday, infra upgrade 4 weeks early, 12 engineers / two pods, inherited team (S1).
- `leadership/interview_questions.md` — 90-question bank.

Verified numbers used: escalation 67% → 50%+; review 30 → 5 min; manual tickets 500 → 260 per 10K orders; 60+ fraud models unified; restaurant underwriting $1M pilot → $25M. No other metrics were invented; bracketed items in the repo were not treated as facts.
