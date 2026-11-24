# Hiring: How to Decide, Level, Judge Fit, and Hold the Bar

Two uses: (1) your answer to "How do you hire? What do you look for?" in EM interviews, and (2) a practical playbook and question bank for when you're the hiring manager. Built Nov 24. Company-specific answer: [Rula / Jay Floyd Q25](../company/rula/jay-floyd-leadership-qa.md). Related: [Stripe hiring standards](./stripe_people_and_leadership/03_hiring_standards.md), [questions to ask candidates (Stripe prep)](./stripe_people_and_leadership/interviewer_questions.md).

---

## Spoken answer: "How do you hire?" (~60 seconds)

> I decide what good looks like before I interview: a scorecard with the mission, three to five must-have skills, and the behaviors that matter. Each interviewer covers different areas, and everyone writes feedback before the debrief so the loudest voice doesn't win. To judge level, I listen for scope and independence, not years: I always ask "what was your part, specifically?" For fit, I look for what the team is missing, not people like us. My bar is simple: would this person raise the team's average at this level? If I'm not sure, it's a no. And I hire for strengths: one clear strength the team needs beats being fine at everything.

**Hint:** *Scorecard → split areas → written feedback first → scope, not years → culture add → raise the average.*

**Proof you can add:** the backend engineer who was strongest at infrastructure ([underperformance.md](./underperformance.md)), as the "hire for strengths" lesson, in one line. **[NEEDS YOUR STORY: one "best hire": how you found them, what you saw in the interview, what they became.]**

---

## 1. Decide what "good" means before you interview

The most common hiring mistake is judging candidates on a gut feeling. Write a **scorecard** first:

| Part | Example for an ML engineer on your team |
|---|---|
| **The mission** | "Own the fraud model lifecycle: from features to production monitoring." |
| **Must-have skills, 3–5** | ML fundamentals, production ML systems, coding, debugging data problems |
| **Behaviors** | Ownership, clear communication, learns fast, good judgment under uncertainty |
| **Level** | Which level, and what scope that means (see section 2) |
| **Nice-to-haves** | Fraud / risk domain, LLM and agent experience |

Then **assign each interviewer one or two areas**, so you get depth instead of five people asking the same thing.

---

## 2. How to work out their level

Listen for **scope and independence** in their stories, not years of experience:

| Signal | Mid-level | Senior | Staff |
|---|---|---|---|
| **Scope of their stories** | A feature or a model | A system end to end | Across teams; set the direction |
| **Who decided** | "My lead decided, I built it" | "I designed it and made the call" | "I aligned three teams on the approach" |
| **Ambiguity** | Needs a clear problem | Turns a vague problem into a plan | Finds the problem nobody asked about |
| **Trade-offs** | Knows one way | Compares options and picks one | Explains the trade-offs in business terms |
| **Influence** | Their own work | Mentors teammates, raises the team's bar | Changes how other teams work |
| **Failure stories** | "It broke, I fixed it" | "I found the root cause and fixed the system" | "I changed the process so it can't happen again" |

**The best levelling tool is a follow-up question:** "What was your part, specifically?" and "What would you do differently at twice the scale?" "We" stories often shrink when you ask that.

This matches the dimensions in [leveling_and_promotions.md](./leveling_and_promotions.md) (scope, depth, independence, influence, impact).

---

## 3. Fit and the bar

**Fit, done right: "culture add," not "people like us."**
- Do they share the **values that matter**: ownership, honesty, learning, respect?
- Do they add something **the team is missing**: a skill, a perspective, a working style?
- Avoid "would I get a beer with them?" That's how teams end up all the same.

**Raising the bar:**
- **The rule:** would this person **raise the average** of the team at this level? (Amazon calls this the "bar raiser" test.)
- **"Not sure" means no.** A bad hire costs far more than a slower hire.
- **Hire for strengths, not for the absence of weaknesses.** One clear strength the team needs beats being "fine at everything."

**Making the decision fair:**
1. Each interviewer **writes feedback before the debrief**, so the loudest person doesn't sway the group.
2. Feedback is **evidence**: what they said or did, not "seemed smart."
3. Score **each area separately**, then decide.
4. **One strong "no" with evidence gets discussed.** Don't just average it away.

---

## 4. Question bank (ML / AI engineers)

### Technical depth: ML
- "Walk me through a model you took to production. What was the hardest part *after* training?"
- "Your model's offline metrics are great but production performance dropped. How do you debug it?"
- "How did you choose your evaluation metric? What would have gone wrong with a different one?"
- "Tell me about a time the data was the problem, not the model."
- *For AI/LLM roles:* "How would you evaluate an LLM agent? How do you find which part of it is failing?" (See [agent_eval_playbook.md](../agent-infra/evaluation/agent_eval_playbook.md) for what a good answer covers.)

### System design
- "Design a real-time fraud scoring system. Latency budget is 100ms." Probe: features, fallbacks, monitoring, retraining.
- "How would you safely roll out a new model that replaces one the business depends on?"

### Ownership and impact
- "Tell me about something you owned end to end. What did you do that wasn't asked of you?"
- "What's a project that didn't go well? What was your part in that?"
- "How did you know your work mattered to the business?"

### Judgment under uncertainty
- "Tell me about a decision you made without enough data. How did you decide, and how did it turn out?"
- "When have you chosen a simpler solution over a better one? Why?"

### Collaboration and communication
- "Tell me about a disagreement with a teammate or PM. How was it resolved?"
- "Explain a recent technical decision to me as if I were the business owner."
- "How do you give feedback on someone else's code or design?"

### Learning and growth
- "What's something you learned in the last six months? How did you learn it?"
- "Tell me about feedback that was hard to hear. What did you change?"

### AI-native ways of working
- "How do you use AI coding tools in your work? Where don't you trust them?"
- "How do you review code an AI wrote?"

### Follow-ups that work on any story (use these to judge level)
- "What was *your* part, specifically?"
- "What were the alternatives, and why didn't you pick them?"
- "What would you do differently now?"
- "What would break at ten times the scale?"
- "How did you measure success?"

### For senior / staff candidates
- "Tell me about a time you changed how another team worked."
- "How have you made the engineers around you better?"
- "What technical direction did you set that others followed?"

---

## Likely follow-ups when you're the candidate

| Follow-up | Hint | Key line |
|---|---|---|
| Tell me about a bad hire. | **What I missed → what I changed in the process** | "I trusted a strong interview over weak references." **[NEEDS YOUR STORY, or say it hasn't happened]** |
| How do you hire fast without lowering the bar? | **Scorecard up front, fast loop, no "maybe"** | "Speed comes from clarity, not from lowering the bar." |
| How do you avoid bias? | **Scorecard, split areas, written feedback first, evidence** | "Everyone decides alone before anyone decides together." |
| Do you let the team interview? | **Yes, for a real area, with the same scorecard** | "They often spot things I miss." |
