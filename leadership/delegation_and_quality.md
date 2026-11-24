# "How do you delegate without lowering the bar on quality?"

Spoken answer, decision rights (manager / tech lead / DRI), visibility without micromanaging, checklist, and follow-ups. Built Nov 24. Company-specific version: [Rula / Jay Floyd Q7](../company/rula/jay-floyd-leadership-qa.md). Related: [bottleneck_story.md](./bottleneck_story.md) (how the DRIs and decision rights came about), [leadership_style.md](./leadership_style.md) (matching oversight to skill).

**Don't repeat the bottleneck story here.** That answer is about decision rights and the handoff; this one is about **quality**. Mention DRIs in one line.

---

## What the interviewer is testing

A **system** that keeps quality high without you checking everything. For Rula's Jay Floyd, this is his "everything runs through you" worry, plus his point that delegation feels risky "because quality still matters."

---

## Framework: define → build into the system → match oversight to risk → inspect outcomes

| Step | What it means | ~Time |
|---|---|---|
| **1. Define "good" before you hand off** | What done looks like: success criteria, constraints, what's not OK | 15s |
| **2. Put the bar in the system, not in your head** | Design docs, review checklists, tests, eval gates, decision logs | 25s |
| **3. Match oversight to risk and experience** | More checkpoints for new skills or high-risk work; fewer for proven owners | 15s |
| **4. Inspect outcomes, not process** | Check the result and the key decisions, not every step or PR | 15s |
| **5. Example** | One case where the system held the bar | 20s |

---

## Final answer (~75 seconds)

> I keep the bar high by moving it out of my head and into the system.
>
> **First, I define "good" before I hand anything off:** what done looks like, the constraints, and what's not acceptable. Most quality problems after delegating come from an unclear bar, not a weak engineer.
>
> **Second, I build the bar into the work itself:** a design doc before anything big, a review checklist, tests, and for ML work, an evaluation gate that has to pass before anything ships.
>
> **Third, I match how closely I check to the risk.** New skill or high stakes: more checkpoints early. A proven owner: I review the design and the outcome, not every step.
>
> **Example:** on our support automation work, we cut review time from 30 minutes to 5 with an eval-driven pipeline. The eval set itself was the quality bar. Engineers could move fast without me checking every case, because the system caught regressions.
>
> That's what delegation should feel like: the standard is enforced by the system, not by my calendar.

**Optional add-on (~40 seconds), if asked about decision boundaries or visibility:**

> Each area on my team has a DRI. Inside their area, they decide and tell me after. Decisions across areas go to the tech lead. Anything that affects other teams, is expensive to reverse, or involves headcount comes to me. It's all written down, so nobody has to guess.
>
> For visibility, the rule is "inform, don't ask." DRIs log their decisions, post a short weekly update (shipped, decisions, risks, help needed), and there are written triggers for when to tell me right away, like a slipped date or a serious incident. My test is simple: I should never learn about something important from my boss or a stakeholder first.

**Story homes:** the support-automation numbers (30 → 5 min) are verified; their full story lives in the "leading under pressure" answer, so keep it to the one sentence above. The 60 fraud models belong to the cross-org answer.

**[CONFIRM: team shape. This assumes areas with DRIs (the bottleneck answer). If your real setup is two pods with pod leads, swap "area" for "pod" throughout.]**

---

## Decision rights: who decides what

Sort decisions by **how far they reach** and **how hard they are to reverse**.

| Decision | DRI (owns an area) | Tech lead | Manager (you) |
|---|---|---|---|
| Design and implementation **inside their area** | **Decides** | Consulted on big ones | Informed after |
| Technical choices **across areas** (shared data, services, interfaces) | Proposes | **Decides** | Informed |
| New technology, vendor, or big architecture change | Proposes | **Decides** with you | **Approves** if costly or hard to reverse |
| Priorities **within their area** this sprint | **Decides** | — | Informed |
| Quarterly roadmap and priorities **across areas** | Proposes for their area | Advises on technical sequencing | **Decides** |
| Dates and commitments to **their own stakeholders** | **Decides** | — | Informed |
| Commitments that affect **other teams or other orgs' metrics** | Proposes | Consulted | **Decides** |
| Incident response | **Leads** (or on-call) | Supports | Informed right away for serious incidents |
| Hiring, headcount, performance, promotions | Gives input | Gives input | **Decides** |

**Three kinds of involvement:**
- **Decides:** makes the call and owns the result.
- **Consulted before:** gets a say before the decision. Use sparingly; it slows things down.
- **Informed after:** hears once it's done. The default for anything inside a DRI's area.

**The test for any new decision:** inside one area and easy to reverse → the DRI decides. Crosses areas, affects other teams, or hard to undo → it goes up a level.

---

## Visibility without micromanaging

The principle: **"inform, don't ask."** DRIs don't need your permission, but you shouldn't be surprised.

| Mechanism | What it looks like | Why it works |
|---|---|---|
| **Decision log** | DRIs write a short note for every meaningful decision: what, why, alternatives | You can read it async; context survives without meetings |
| **Weekly async update** | Four lines per DRI: shipped · decisions made · risks · help needed | Five minutes for them, full picture for you |
| **Owners' sync** | 30 minutes a week; cross-area issues and escalations only, not status | Catches problems between areas, where most surprises come from |
| **Escalation triggers** | Written "tell me within a day if…": a date slips more than a week, a serious incident, a stakeholder conflict, a cost over a set amount, anything touching another team | Removes "should I tell my manager?" guesswork |
| **Design docs** | You read the important ones async and comment with questions, not orders | You stay technically close without taking over |
| **Dashboards** | Key metrics per area: delivery, quality or model metrics, incidents | You see trends without asking |

**Your rule for yourself:** "I should never learn about something important from my boss or a stakeholder first." If that happens, fix the visibility system, not the person.

**How to avoid it feeling like micromanaging:**
- **Agree on all of this up front, in writing.** Checking in is then the agreed system, not a sign of distrust.
- **Comment as questions**, like "what happens if X fails?", not "do Y instead."
- **When you disagree with a DRI's in-area decision**, say so and let them decide anyway, unless it's hard to reverse. That's what makes the ownership real.

---

## Checklist before you speak

- [ ] First sentence: move the bar out of my head and into the system
- [ ] Define "good" before handing off
- [ ] Name the mechanisms: design doc, checklist, tests, eval gate
- [ ] Oversight matches risk and experience
- [ ] One example: the eval-driven pipeline (30 → 5 min), one sentence
- [ ] Close: "enforced by the system, not by my calendar"
- [ ] Don't say "I trust my team" as the answer, or "I review everything"

---

## Likely follow-ups

| Follow-up | Hint | Key line |
|---|---|---|
| Delegated work comes back below the bar? | **Was the bar clear? → specific feedback → they fix it** | "If I fix it myself, I've taught them I'll always fix it." |
| How do you avoid micromanaging? | **Agree the checkpoints up front; questions, not orders** | "Checking in is the agreed system, not a sign of distrust." |
| What do you never delegate? | **Hiring decisions, hard people conversations, cross-team commitments, hard-to-reverse calls** | "I delegate the work, not the accountability." |
| Who decides what between you, the tech lead, and DRIs? | **Inside area → DRI · across areas → tech lead · other teams / hard to reverse / people → me** | "It's written down, so nobody has to guess." |
| How do you stay informed? | **Inform, don't ask: decision log, weekly update, escalation triggers** | "I should never learn about something important from my boss first." |
