# Manager Questions & Answers

## People Leadership

### Q: How do you approach 1:1s with your team?
**A**: I structure them around the engineer's growth, not just status updates. I use a simple template:
- 5 min: how are they doing (personal/professional)?
- 15 min: what's blocking them or exciting them this week?
- 5 min: career/growth check-in (once per month deeper dive)
- Rest: flexible based on what they need

At DoorDash, I quickly learned that 1:1s are about understanding what motivates each person, not just assigning work. One engineer was frustrated with meetings and needed deep focus time; another wanted to learn more about production systems. Once I understood that, I could unblock them differently.

I also use 1:1s to give real-time feedback, not surprise them in reviews. My goal is: no surprises in annual reviews. If there's a performance concern, they should have heard it multiple times in 1:1s with a plan to improve.

---

### Q: How do you handle an underperforming engineer?
**A**: I'd diagnose before judging:
1. **Clarity**: Do they understand what success looks like? (Often it's a communication problem, not a capability problem)
2. **Fit**: Are they in a role that plays to their strengths? Sometimes someone is struggling because they're in the wrong seat.
3. **Support**: Have I given them the tools/time/mentoring to succeed? As a manager, underperformance is partly my problem.

If it's truly a capability gap after coaching: I'd create a clear, time-bound improvement plan with specific milestones. If they improve, great. If not, we'd have a conversation about fit.

I've learned that sometimes a "misfit" engineer is actually a high performer in a different role or team. I'd try to help them find that fit before assuming it's a performance issue.

---

### Q: How do you build a high-performing team?
**A**: Three things:
1. **Clear vision**: Engineers want to work on problems that matter. I spend time explaining why fraud detection matters to DoorDash (user trust, platform safety, business health). When they understand the "why," they care more.
2. **Autonomy + accountability**: I give ownership of systems/projects. Senior engineers own fraud ring detection; junior engineers own feature implementation with senior review. Clear ownership = clarity on who's responsible.
3. **Growth opportunities**: I actively level engineers. I identify high performers early, give them stretch projects, and mentor them publicly. They see a path to senior IC or technical leadership.

Also: hire for strengths, not the role. I've hired engineers strong in infrastructure who became key to platform improvements, even though they started in core fraud detection.

---

### Q: How do you give feedback?
**A**: I use a simple structure:
- **Observation**: "In yesterday's design review, you presented the model approach but didn't explain the tradeoffs with the previous approach."
- **Impact**: "The team wasn't sure why we were changing direction, and we had questions that could've been anticipated."
- **Expectation**: "For future reviews, start with: current state, proposed change, and key tradeoffs."
- **Support**: "Let me know if you want to prep together for the next review."

Positive feedback works the same way: observation + impact + keep doing it. I try to give feedback close to the event, not months later.

---

### Q: How do you handle conflict on your team?
**A**: I've had two engineers disagree on a model architecture. Instead of deciding for them, I:
1. Asked each person to write up their perspective (1-page design doc)
2. We had a structured discussion: assumptions, tradeoffs, unknowns
3. I helped them find common ground (we ended up doing a hybrid approach)
4. Made it clear: this is how we disagree productively—with data and respect

Most conflicts are about miscommunication or different priorities, not actual disagreement. If I step in too fast, I rob the team of learning to resolve it together.

---

### Q: How do you hire?
**A**: I look for:
1. **Technical foundation**: Can they think through systems? Can they code? (For fraud detection: do they understand ML fundamentals?)
2. **Learning mindset**: Have they grown in past roles? Do they ask good questions?
3. **Communication**: Can they explain complex ideas clearly? (Critical for cross-functional teams)
4. **Judgment**: How do they make decisions under uncertainty? (Real interview: walk me through a recent decision)

I stay involved in hiring—I do technical interviews and cultural fit assessments. It takes time, but it matters. I also give engineers a voice in hiring; they usually spot things I miss.

---

## Technical Leadership (as Tech Lead Manager)

### Q: How do you balance being a technical leader and a manager?
**A**: Honestly, it's a tension. Here's how I approach it:
- **Manager priorities win when it's people**: I'll drop everything for a 1:1 if someone is struggling or leaving.
- **Technical priorities win when it's blocking the team**: If we're down and urgent, I code.
- **Shared priorities**: Design review, hiring, strategy—I do both hats here.

I use "focus windows" (10am-3pm no meetings) to preserve coding time. I don't lead the day-to-day implementation, but I stay hands-on enough to have technical credibility and spot technical debt early.

At VoltronData, I made a mistake: I tried to code full-time and manage full-time. It didn't work. Now I'm deliberate: I do maybe 10-15% of the work myself (critical reviews, architecture decisions, spike investigations), and 85% is growing others.

---

### Q: How do you stay technically credible without being a bottleneck?
**A**: 
- I do design reviews on major projects, not every PR
- I code for 5-10 hours per week (architecture explorations, spike investigations, critical bugs)
- I stay on-call with the team (not in rotation, but I understand the systems)
- I read the code. I don't write it all, but I know what's happening

The goal is: engineers respect my technical judgment without feeling like I'm breathing down their neck. When I do code, I'm usually solving a hard problem or unblocking the team, which builds credibility.

---

### Q: How do you approach technical strategy?
**A**: I work backward from the business problem:
- Fraud is a growing threat (business insight)
- Our current model catches 40% with 2% false positives (current state)
- We want to catch 60% with <2% false positives (goal)
- What's blocking us? (Model architecture? Feature engineering? Throughput?)
- What's the 6-month roadmap to get there? (New model training, data pipeline improvements, etc.)

I bring in the team to debate the approach, but I own the strategy. I also adjust based on what we learn—if we hit a technical wall, we pivot.

I make sure we're not just building cool things; we're solving real problems. That alignment keeps the team motivated.

---

## Managing Up & Cross-Functional Work

### Q: How do you work with your manager?
**A**: I keep them informed without surprises:
- Weekly status: key wins, blockers, upcoming risks
- If something could affect hiring/budget/timeline, I flag early
- I ask for help when I need it (hiring, difficult performance issues, strategic guidance)

I also try to make their job easier. My director cares about fraud metrics and team health; I make sure they have those metrics without asking.

---

### Q: How do you handle requests from other teams?
**A**: I balance:
1. **What helps Roblox/DoorDash**: If another team has a real blocker and I can help, I do (within reason)
2. **What's in our scope**: Fraud detection is our domain; adjacent work isn't
3. **Team capacity**: We can't say yes to everything

Example: Product wanted our fraud team to also do chargeback prevention. We said: "That's a different problem space. We can advise, but you need a dedicated team." I helped them hire the first engineer, but we didn't absorb the work.

Clear boundaries respect the team's focus.

---

## Growth & Learning

### Q: What's something you got wrong as a manager?
**A**: Early on, I didn't give enough mid-cycle feedback. I thought 1:1s were for check-ins, not feedback. An engineer got surprised in a performance review because I'd never told them expectations clearly. That was on me.

I fixed it by:
- Building mid-cycle feedback into 1:1s
- Being explicit about expectations upfront
- Getting coaching from my HR partner

It was humbling, but it taught me that my job is to set people up to succeed, not surprise them.

---

### Q: What do you want to improve as a manager?
**A**: 
1. **Scaling myself**: As the team grows from 10 to 15+, I need to delegate more and let engineers own more decisions. I'm working on being less of a "decider" and more of a "enabler."
2. **Executive presence**: I want to be better at communicating strategy to senior leadership—translating technical trade-offs into business impact.
3. **Conflict navigation**: I can get too focused on data/logic and miss the human side of disagreement.

I'm reading "The Coaching Habit" and getting coaching from my skip-level manager. I'm a learner.

---

### Q: How do you think about career progression?
**A**: Two paths: IC and manager. Not everyone should be a manager; some of our best engineers are senior ICs.

For managers: I look for people who care about people, think strategically, and can make tough calls.

For ICs: I look for technical depth, the ability to mentor, and project ownership.

I try to give people choice and honest feedback about their strengths. One engineer I thought would be a great manager realized they loved the IC path more. That's fine.

I also think about: what role plays to their strengths? Not everyone is wired the same way.
