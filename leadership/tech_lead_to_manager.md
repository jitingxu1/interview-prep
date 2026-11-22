# "What changed for you when you moved from tech lead to manager?"

A common second question in EM leadership rounds, right after "describe your leadership style" ([leadership_style.md](./leadership_style.md)). Includes the answer structure, final answer, prep notes, delivery checklist, follow-ups, and practice log. Built from mock practice on Nov 22. Company-specific version: [Rula / Jay Floyd Q2](../company/rula/jay-floyd-leadership-qa.md).

---

## Answer structure (use for any "what changed / what did you learn" question)

| Step | What to say | Time |
|---|---|---|
| **1. Headline** | The one shift, in a sentence | 5s |
| **2. Before** | How you worked as a tech lead | 15s |
| **3. After** | How you work now, concretely | 30s |
| **4. Proof** | One real example with a result | 15s |
| **5. Close** | A simple test or principle, then stop | 10s |

Keep the main answer positive and short. Save the mistake (VoltronData) for the follow-up "how did you learn that?"

---

## Final answer (~75 seconds)

> The biggest change was how I create value. As a tech lead, I created value by doing. As a manager, I create value by building the system the team runs on.
>
> By doing, I mean I solved problems myself: I made the technical call, wrote the hard part, and unblocked people with my own answers. The team's output depended on mine.
>
> As a manager, my job is to own that system. I design it: who owns what, how decisions get made, what good looks like. I bring people into it and grow them until they can run their part on their own. I watch whether it's working. And when it breaks, I fix the system, not just the symptom. When my team was spending half its time in meetings, I didn't ask people to work harder. I consolidated four stakeholder syncs into one and protected a no-meeting day, and we got meeting time down to about 20 percent.
>
> My test is simple: if I'm out for two weeks, does the team slow down? If it does, the system isn't done yet.

**Why this lands:**
- A clear, memorable headline: doing vs. building the system.
- "With me or without me" shows you're not absent, just not a bottleneck.
- A concrete example of fixing the system, with verified numbers (meeting load 50% → ~20%, four syncs into one).
- A one-line test as the close.

**Tailoring by interviewer:** for a coaching-heavy interviewer like Rula's Jay Floyd, whose framework is that new managers lead "a new role with an old operating system" and become "the answer machine," this answer is his idea in your own words. Don't quote his framework back to him. He builds data platforms, so one short line works if it comes naturally: *"I think of the team the way I'd think of a production system: design it, run it, monitor it, and fix it."* Don't push the analogy further. For an execution-heavy interviewer, lean on the meeting-load result and what the team shipped.

**If you've actually been out for two weeks and the team shipped without you**, add that as the proof: "Last time I was out for two weeks, the team shipped [X] without me." That's stronger than the test alone. Only use it if it's true.

---

## Prep notes

### What a manager owns when the job is the system

The manager owns the whole lifecycle of the team's system, the way an engineer owns a production service.

| Role | What it means | Your real examples |
|---|---|---|
| **1. Design it** | Goals and priorities, who owns what, decision rights, what "good" looks like, team rhythms (planning, 1:1s, reviews) | Written decision rights for pod leads; design-doc standards; the 70/30 long-term vs. short-term split |
| **2. Staff it and onboard people into it** | Hire, onboard, put people where their strengths fit, move them up from directing to delegating | Hiring for strengths; moving the backend engineer to infrastructure; co-run → sit in → step out |
| **3. Observe it** | Watch whether it's actually working: signals, not feelings | Decisions still coming to you each week; meeting load; eval gates; what you hear in 1:1s; stakeholder feedback |
| **4. Debug and fix it** | When something breaks, fix the system, not just the symptom | Meeting load 50% → ~20%; an engineer blindsided in a review → mid-cycle feedback with a set structure; the three-month delegation lag → written decision rights |
| **5. Connect it to the org** | Bring context in (strategy, priorities), absorb organizational noise, align with other teams, report up in business terms | One stakeholder sync instead of four; the no-meeting day; reporting fraud trade-offs in dollars |
| **6. Handle the exceptions** | What the system isn't built for: incidents, irreversible or cross-team calls, hard conversations | Directive mode in incidents; cross-team decisions come to you by design |

**Key point: fix the system, not the symptom.** When something goes wrong, ask *why did the system allow it?* rather than *who made the mistake?* The feedback story is the proof: you didn't just apologise to one engineer, you changed how feedback works for everyone.

### The two operating systems: tech lead vs manager

Use this to prepare, not to recite. Pick one or two rows that match your real experience and tell them as your story.

| Dimension | Tech lead operating system | Manager operating system | The habit to unlearn |
|---|---|---|---|
| **What you're measured on** | Your answers: design quality, how fast you solve it | The team's answers: what they deliver without you | Judging your week by what *you* built |
| **Where your impact comes from** | Your own output | Other people's output: multiplied, delayed, indirect | Doing the hard part yourself because it's faster |
| **When someone is stuck** | Solve it, unblock them | Ask "what would you do?"; coach, or give bounded room | Being the answer machine |
| **Decisions** | You make the technical calls | You design who decides what: written decision rights | Everything still running through you |
| **Time horizon** | This sprint, this design, this launch | Next 2–4 quarters: roadmap, hiring, team shape | Living only in the current sprint |
| **Feedback loop** | Fast: tests pass, the PR merges, it ships | Slow: people grow over months; results show up a quarter later | Needing a daily win to feel productive |
| **What a good day looks like** | Hours of deep focus, something shipped | Several decisions unblocked, one hard conversation done, nobody waiting on you | Protecting your own focus time over the team's |
| **Calendar** | Mostly yours, built for building | Mostly others': 1:1s, stakeholders, hiring | Treating meetings as interruptions instead of the job |
| **Quality bar** | Lives in your head and your reviews | Lives in the system: design docs, eval gates, standards written down | Reviewing every PR yourself |
| **Information** | You know the code best | You know the context best: priorities, people, org | Using technical depth to win arguments |
| **Communication** | Technical detail, explaining the full reasoning | Decision first, business impact second, detail on request | Over-explaining |
| **Conflict** | Debate the technical merits | Make the decision process fair; hard conversations early | Avoiding the people side because it's uncomfortable |
| **Risk you own** | Your code breaks | Your team burns out, stalls, or leaves; bad hires; misalignment | Seeing people problems only when they become technical ones |
| **Identity and satisfaction** | "I built that" | "They built that, and they couldn't have a year ago" | Needing to be the smartest person in the room |
| **Failure mode** | Slow or buggy output | The team is busy but dependent on you; you become the bottleneck | Working harder instead of redesigning the system |

The rows you actually lived: **when someone is stuck** (solving → "what would you do?"), **decisions** (pod-lead decision rights), and **communication** (reporting up in business terms, see [weaknesses.md](./weaknesses.md) and [reporting_up.md](./reporting_up.md)).

**One-line summary if asked:** "As a tech lead, I scaled by being faster. As a manager, I scale by being less necessary."

### Operating system = mindset + skills + habits

"Operating system" is wider than mindset or skill. It's what you do by default, especially under pressure.

| Layer | What it is | Example |
|---|---|---|
| **Mindset** | What you believe your job is and what you value | "My value is having the answer" → "My value is the team having the answer" |
| **Skills** | What you're able to do | Designing systems → giving feedback, delegating, hiring, reporting up |
| **Habits / systems** | What you do by default, plus the structures you've built | Jumping in to solve → asking "what would you do?"; written decision rights; weekly 1:1s |

Each layer can fail on its own:
- **Right mindset, missing skill:** you know you should give hard feedback but don't know how, so you soften it. (Your feedback story.)
- **Right skill, old mindset:** you can delegate, but you still believe your value is the answer, so you take it back.
- **Right mindset and skill, no habits:** it works on calm days, and under pressure you fall back to the old way.

**One sentence that covers all three, in your own words:**
> "The change wasn't just a new skill set. It was my mindset and my habits. I had to stop believing my value was having the answer, learn how to coach and delegate, and then build habits so I don't fall back to the old way under pressure."

---

## Checklist before you speak

- [ ] First sentence = the answer: "by doing" vs. "by building the system"
- [ ] No ego in the "before" part: describe how you worked, not how important you were
- [ ] Say what you still own (design, people, watching, fixing), so "without me" doesn't sound like "absent"
- [ ] One concrete fix with numbers: meeting load 50% → ~20%
- [ ] Close with the two-week test, then stop. Don't trail off with "so…"
- [ ] No "right?" after sentences. Pause instead
- [ ] Save VoltronData for "how did you learn that?"

---

## Likely follow-ups

### 1. How did you learn that? / What went wrong at first?

> When I first became a manager, at VoltronData, my tech-lead habits kept running. If something mattered, I owned it. If someone was stuck, I solved it. I tried to code full-time and manage full-time, and it didn't work: the team waited on me instead of growing. So I changed two things. I cut my hands-on work to about 10 to 15 percent: design reviews on major projects, spikes, critical bugs. And when someone brought me a problem, I stopped answering and started asking, "What would you do?" Most of the time their answer was good, and that's how ownership moved to them.

**[CONFIRM BEFORE USING LIVE: the repo records only "at VoltronData I tried to code full-time and manage full-time; it didn't work" ([manager_qa.md](./manager_qa.md)). Add one real symptom, e.g. reviews piling up, 1:1s getting cancelled, a deadline slipping, or someone telling you. Also, [tech_leadership_balance.md](./tech_leadership_balance.md) says 20–30% technical time, while this answer says 10–15%. Pick the true number and use it everywhere.]**

### 2. What was the hardest thing to let go of?

> Being the person with the answer. As a tech lead that was my value. Early on, when someone brought me a hard problem, solving it felt like helping. Now I see that answering it took the learning away from them, and taught the team to bring everything to me.

### 3. How do you keep technical credibility at 10 to 15 percent hands-on?

> I pick the work where my judgment matters most: design reviews on major projects, spikes on new problems, and critical bugs. I read design docs closely and ask hard questions in reviews. Engineers can tell quickly whether you understand the system, and that comes from depth on the important things, not from writing the most code.

### 4. How do you know the system is working?

> I watch a few signals. How many decisions still come to me each week, and what kind. Whether the team ships on time when I'm not in the room. What I hear in 1:1s: are people blocked, or bored? And whether stakeholders go to the pod leads directly instead of to me. When those move the wrong way, that's where I look for what's broken.

### 5. How did your team react when you stepped back from coding?

> **[NEEDS YOUR STORY: what actually happened. Did anyone push back, or did they step up? One concrete moment, e.g. the first time someone made a call you would have made differently, and it worked.]**

### 6. Do you miss coding? Would you go back to IC?

> Sometimes, and I still get my hands dirty on spikes and hard bugs. But the work I find most satisfying now is watching someone own a problem I used to own and do it well. That's the part I wouldn't give up.

### 7. What's one IC habit you still have to watch?

> Over-explaining. When I can see the reasoning, I want to walk through all of it. As a manager, a long explanation can turn into me making the decision for them. So I try to give the goal and the constraints, and let them work out the rest.

---

## Practice log

**Attempt 1 (Nov 22):** right insight, weak delivery.
- No headline ("the biggest change for me is the transition, right?").
- Five "right?"s, which sounds like asking for approval.
- Stayed abstract ("mindset and technology are completely different," "the influence is different").
- One shaky claim: "before, a bad judgment only impacted myself."
- No story, no result, trailed off on "So."
- Good: the core idea (measured by the team's output, not yours), the larger blast radius, the move to higher-level goals.

**Your own reframes (Nov 22), now in the final answer:**
- From "the team couldn't run without me" to "the team runs with me or without me."
- Not "being needed" but **doing vs. leading**: solving it yourself vs. setting up the rules and the system.
- The manager owns the system itself: design it, onboard people into it, find the issues, and fix them. Not just cross-team calls and hiring.
