# "How would you describe your leadership style?"

The answer to the most common opener in any EM leadership round: situational leadership, with examples, a delivery checklist, and follow-ups. Built from mock practice on Nov 22. Company-specific versions can link here (e.g. [Rula / Jay Floyd Q1](../company/rula/jay-floyd-leadership-qa.md)).

---

## Answer structure (use for any philosophy question)

| Step | What to say | Time |
|---|---|---|
| **1. Headline** | One sentence naming your style | 5s |
| **2. Why** | Where it came from: a short origin or lesson | 15s |
| **3. How** | The mechanism: how you decide, concretely | 25s |
| **4. Proof** | 1–2 examples with a result, ideally one each way | 35s |
| **5. Close** | The trap you watch for, or the principle you'd bring here | 10s |

**The first sentence is the answer.** If the interviewer stopped you after it, they should already know your style.

---

## Final answer (~80 seconds)

> My style is situational. It depends on the person, the skill, and the problem. I came up as a tech lead, and the main thing I learned in three years of managing is that one style doesn't fit every problem.
>
> I use the four modes from situational leadership: directing, coaching, supporting, delegating. For each task I ask: how much skill and confidence does this person have *on this specific problem*? A senior engineer can need directing on something brand new. A junior can own a part of the code they know well.
>
> I'm explicit about it. I tell each person where I think they are on their area, and I ask where *they* think they are. If we disagree, that gap is the conversation, and then we plan how to move them up.
>
> Two examples. In a production incident when we're losing money, I'm directive: I pick the people, assign the work, align on the goal, and we review afterward. On the other end, when my team split into two pods, I moved two senior ICs to delegation on purpose. I co-ran their stakeholder meetings for a month, then sat in, then stepped out. Now they own their team's decisions, and both grew into senior scope.
>
> The trap I watch for is over-coaching. If someone needs me to rebuild their confidence every week, I've created dependence. The goal is to move everyone toward delegation.

**Why this lands:** it shows you have a deliberate model rather than one habit, that style follows the skill and not the title, that you're transparent with reports about where they stand, and that the goal is ownership transfer, not dependence on you.

**Tailoring by interviewer:** for a coaching-heavy interviewer (e.g. Rula's Jay Floyd, who says coaching is only ~20% of the job), lean on the over-coaching trap. For an execution-heavy one, lean on the incident example and the results.

---

## Checklist before you speak

- [ ] First sentence = the answer
- [ ] No self-deprecation in the opening ("young manager," "still struggling," "I don't know how many")
- [ ] Say **directive**, never "dictator"
- [ ] Name the model precisely: four modes
- [ ] "A senior can **need** directing," not "can **do** directing"
- [ ] Examples go in both directions: down (incident) and up (pod-lead delegation), and each ends with a result
- [ ] Close with the over-coaching trap, then stop talking
- [ ] Short sentences; if one goes wrong, stop and restart it

---

## Likely follow-ups

### 1. What happens when someone thinks they're at delegating and you think they're at coaching?

> I give them a bounded piece to own fully, agree on what good looks like up front, and let the result settle it. Either they prove me wrong, which is great, or we both see the gap. Then the gap is something we work on together, not my opinion against theirs.

### 2. How do you switch to directive without it feeling like distrust?

> I name the mode out loud: "This one is urgent, so I'm going to be directive. It's about the situation, not about you." Then once the incident is over, I hand ownership back and we review together. People accept a directive moment when they know it's temporary and they know why.

### 3. How do you assess someone's skill and confidence on a problem?

**Spoken answer (~60 seconds):**

> I look at skill and confidence separately, because they don't always move together.
>
> For skill, I look at the work, not the talk: the quality of their design doc, how they handle the first surprise, whether they see the edge cases before I point them out.
>
> For confidence, I look at what they bring me. A finished decision means high confidence. Two options with a recommendation means they're close. An open question with no view means they're not there yet on this problem.
>
> Then I ask them directly: "On this area, where do you think you are?" If their answer matches what I see, great. If it doesn't, the gap tells me what to do. Skilled but unsure, I give them support and more room. Confident but not yet skilled, I give more structure and check in earlier.
>
> And I reassess per problem. The same senior engineer can be at delegating on their own service and at directing on a new domain.

**Going deeper (if they probe):**

*The four combinations, and what each one needs.* These are the development levels behind the four modes:

| Skill on this problem | Confidence | What it looks like | Mode |
|---|---|---|---|
| Low | High | New to it and excited; doesn't know what they don't know | **Directing:** clear steps, what good looks like, frequent check-ins |
| Some | Low | Hit the first hard part and lost momentum | **Coaching:** still give direction, but explain why and ask for their ideas |
| High | Variable | Can do it, but hesitates or keeps checking with me | **Supporting:** less direction, more encouragement; "what would you do?" |
| High | High | Owns it end to end, brings me decisions, not questions | **Delegating:** set the outcome and the boundaries, then step back |

The second row is the one people miss. Someone's confidence often *drops* after the excitement of starting something new wears off. That's normal, and it's the moment they need the most support.

*The signals I watch:*

| | Signals |
|---|---|
| **Skill** | Quality of design docs and PRs · do they spot the edge cases and tradeoffs before I do · how they handle the first surprise (adapt, or stall) · whether others go to them for help in this area · track record on similar work |
| **Confidence** | What they bring me (decision, options, or question) · how often they check in, and about what · whether they speak up in design reviews · how they describe their own work (hedging vs clear) · how they react when something goes wrong |

*Questions I ask in a 1:1:*
- "On a scale from 'I need a lot of help' to 'I could run this without you', where are you on this area?"
- "What part of this feels solid, and what part keeps you up at night?"
- "If I were out for two weeks, what would you decide differently?"
- "What do you want from me on this: more direction, or more room?"

*Traps I watch for in myself:*
- **Mistaking volume for skill.** The loudest person in the room isn't always the most capable, and the quiet one often knows more than they say.
- **Title bias.** Assuming a senior engineer is at delegating on everything, or a junior is at directing on everything.
- **Stale reads.** People move fast. I reassess at each new project, not once a year.
- **Over-reading one bad week.** One missed deadline doesn't move someone down a level; a pattern does.

*Example: skilled but not yet confident (~45 seconds, use after the spoken answer if they ask "give me an example"):*

> One of my pod leads is a good example. On skill, they were clearly there: deep context on the scope, good judgment in design reviews, and stakeholders already trusted them. But on confidence, every decision still came to me, and they framed things as questions: "what do you think we should do?"
>
> So I read it as high skill, lower confidence, which means supporting, not coaching. I stopped answering the question and started asking theirs back: "what would you do?" Almost every time, their answer was the right one. Then I made it official: written decision rights for their team's scope. I co-ran their stakeholder meetings for a month, then sat in, then stepped out.
>
> Within a few months they were bringing me decisions they'd already made, not questions. That's the signal I was looking for, and they grew into senior scope.

**What it shows:** you separated skill from confidence; you read the signal (questions instead of decisions); you picked the right mode (supporting, not coaching); and you watched for a specific change to confirm it worked.

**[CONFIRM BEFORE USING LIVE: this draft is built from the pod-lead story in the Rula Q&A (Q4, Q26), whose details are still unconfirmed. Check that it's true for one specific person, and add the real result: a promotion or level, or one decision they made on their own. For balance, it's also worth having the opposite case ready: a confident engineer who needed more structure.]**

### 4. Tell me about a time you misjudged someone's stage.

> **[NEEDS YOUR STORY: one real case where you delegated too early or held on too long. Who, what happened, what you changed. The three-month delegation lag in Q4 is a candidate: you kept the pod leads at "coaching" longer than they needed.]**

### 5. Doesn't being directive in an incident undercut the ownership you're building?

> Only if it lasts past the incident. In the moment, clarity matters more than ownership: people want one clear call. Afterward we run the review together, and the person who owns that area leads the fix. Done that way, the incident actually builds ownership, because they own the follow-through.

### 6. What would your team say your style is?

> I ask them directly in 1:1s. What I hear most is that I'm clear about expectations and that I give people room on their own areas. What I've heard as criticism is that on high-stakes calls I can step in too early. That's the same weakness I watch for myself, and I track it by how many decisions still come to me each week.
>
> **[NEEDS YOUR STORY: confirm this matches real feedback you've received, such as a skip-level, a 360, or something a report said. Don't use this live unless it's true.]**

### 7. What's your default mode, when nothing pushes you either way?

> Coaching. It's my instinct: I'd rather ask the question than give the answer. That's exactly why I use a model. My default isn't always right, and without a deliberate check I'd coach things that need a clear direction.

---

## Practice log

**Attempt 1 (Nov 22):** right idea but weak delivery.
- Opened with self-doubt ("young manager," "struggling to find my own style").
- Said "dictator."
- Framework was vague ("1, 2, delegate, something like that").
- One example and no result; no conclusion.

**Attempt 2 (Nov 22):** much better.
- Headline came first, the four modes were named, the close was clean.
- New and strongest line: "here's where I think you are; maybe you disagree; let's find the gap."
- Still to fix:
  - "a senior can **do** directing" (meaning flipped)
  - the second example lost the pod-lead story and its result
  - the "why" line got garbled
  - filler words
