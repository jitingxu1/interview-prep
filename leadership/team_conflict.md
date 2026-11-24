# "Tell me about a time two people on your team were in conflict. What did you do?"

Conflict types and how to resolve each, the spoken answer, checklist, and follow-ups. Built Nov 24. Company-specific version: [Rula / Jay Floyd Q13](../company/rula/jay-floyd-leadership-qa.md).

**This is the home for the architecture-deadlock story.** In the culture answer ([building_team_and_culture.md](./building_team_and_culture.md)) and "when to step in," use it in one line only.

---

## What the interviewer is testing

1. You **step in early**, rather than letting it fester or picking a winner.
2. You work out **what the conflict is really about**.
3. You make **the process fair**, so people can disagree without it becoming personal.
4. You **leave a rule behind**, so the next disagreement goes better.

---

## Types of team conflict, and how to resolve each

| Type | What it looks like | What it's really about | How to resolve it |
|---|---|---|---|
| **1. Technical / task** | "Model A vs. model B," "SQL vs. streaming" | The best solution | Write proposals, **agree on criteria first**, debate trade-offs, decide, commit. Use data or a small experiment if possible |
| **2. Process** | "We should do code review differently," "too many meetings" | How the team works | Discuss as a team, **try it for a set time**, review in a retro |
| **3. Priority / resources** | Two people both need the same engineer, data, or timeline | What matters most right now | **Go up a level**: tie it to team goals; the manager or roadmap decides |
| **4. Role / ownership** | "That's my area," "who owns this decision?" | Unclear boundaries | **Clarify decision rights in writing** ([delegation_and_quality.md](./delegation_and_quality.md)); it usually goes away once the line is clear |
| **5. Information / misunderstanding** | They're arguing but mean different things | Missing or different facts | **Get everyone the same facts**; often it isn't a real conflict |
| **6. Working style / values** | Fast vs. careful, direct vs. diplomatic, action vs. empathy | Different defaults | **Name it out loud**, agree when each style wins, and see both as strengths |
| **7. Personal / relationship** | Tension, disrespect, avoiding each other | Trust between two people | **Private 1:1s first**; focus on behavior and impact, not personality; clear expectations; HR if it continues |

**Key insight:** conflicts often look like one type but are really another. A "technical" fight is often about **ownership** (#4) or **feeling heard** (#7). That's what happened in the architecture deadlock.

**Two rules for every type:**
1. **Talk to each person separately first.**
2. **Step in early.** Small conflicts are cheap; old ones turn personal.

---

## Answer structure

| Step | What to say | ~Time |
|---|---|---|
| **0. Diagnose the type** | One sentence: each type needs a different fix; often it looks technical but isn't | 15s |
| **1. Situation and cost** | Who, what about, and why it mattered | 15s |
| **2. What it was really about** | Who gets heard and who decides | 10s |
| **3. Separately first** | Understand each side before bringing them together | 10s |
| **4. Fair process** | Each writes a proposal; criteria first; debate assumptions, trade-offs, unknowns | 20s |
| **5. Decide and commit** | The outcome; everyone commits | 10s |
| **6. Rule and lesson** | The standing process, the result, and what you learned | 15s |

---

## Final answer (~90 seconds)

> When two people on my team are in conflict, the first thing I do is work out what kind of conflict it is, because each needs a different fix. A technical disagreement needs criteria and data. An ownership conflict needs clear decision rights. A personal one needs private conversations about behavior. And often a conflict looks technical but is really about who gets heard or who decides.
>
> That's what happened when two of my senior engineers deadlocked on a model architecture. It was starting to slow the whole team down, and the discussion was getting personal.
>
> I talked to each of them one-on-one first, without picking a side. Then I asked each to write a one-page design doc. Before we compared them, we agreed on the criteria: latency, accuracy, cost to maintain. Then we ran a structured discussion on the assumptions, the trade-offs, and what we didn't know yet. Once it was about criteria instead of people, the temperature dropped.
>
> We landed on a hybrid that took the strongest part of each. **[REAL DETAIL: what the hybrid was, in a few words.]** And we set a standing rule: senior engineers propose, the team debates, I break ties if needed, and then everyone commits, including the person whose idea didn't win. **[REAL RESULT: e.g. the two of them worked well together after, or the team used the process on later decisions.]**
>
> What I learned is that most team conflict isn't about the technical question. It's about whether the process feels fair. Once it does, people can disagree hard without it becoming personal.

**[CONFIRM BEFORE USING LIVE: did you talk to each of them one-on-one first? What criteria did you use? What was the hybrid? What happened afterward? Only say what actually happened.]**

**Watch the time:** name three or four types in one sentence. Don't list all seven out loud; keep the table for follow-ups.

---

## Checklist before you speak

- [ ] Open by diagnosing the type, in one sentence
- [ ] "It looked technical, but it was about who gets heard and who decides"
- [ ] Separately first
- [ ] One-page docs, criteria agreed first
- [ ] Decide and commit, including the person whose idea lost
- [ ] The standing rule, and one real result
- [ ] Don't decide for them right away, take sides, or handle it in public first

---

## Traps

- **Deciding for them right away.** Ends the argument, kills ownership, and the "loser" stays resentful.
- **Waiting too long** and hoping it resolves itself.
- **Taking sides**, or seeming to.
- **Handling it in public** before talking to each person privately.
- **Only telling the technical side.** The interviewer cares about the people part.

---

## Quick hint

> **Diagnose the type → fix matches the type → separately first → write it down + criteria first → decide + commit → standing rule.**
> Types in one breath: *technical, process, priority, ownership, information, style, personal.*
> Key line: *"A conflict often looks technical but is really about who gets heard or who decides."*

---

## Likely follow-ups

| Follow-up | Hint | Key line |
|---|---|---|
| What if the conflict is personal, not technical? | **Private first, behavior and impact, clear expectations, HR if needed** | "I don't need them to be friends. I need them to work together respectfully." |
| What if one person won't commit after the decision? | **Disagree and commit; a direct 1:1; a performance issue if it continues** | "Disagreeing is fine. Undermining a decision isn't." |
| What if someone is in conflict with you? | **Listen first, invite the disagreement, change your mind if they're right** | "If people can't disagree with me, I've built the wrong team." |
| How do you prevent conflicts like this? | **Decision rights and the process set before the conflict starts** | "The best time to agree how we decide is before we disagree." |
| Two people with different working styles? | **Name it, agree when each style wins, both are strengths** | "The action person is why things ship; the empathy person is why people stay." |
