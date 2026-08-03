# Story 10: Embedding Fraud Detection into Assignment Ranking — Cross-Org Stakeholder Buy-In

**Situation**: I'd built a delivery-level risk score that worked well for triaging fraud after assignment. Now I wanted to shift from reactive to proactive—embed this risk score into the assignment algorithm to block risky deliveries *before* assignment happened. This was the first time my fraud detection team was collaborating with the logistics/assignment team on a joint initiative—a true cross-org partnership.

I had buy-in from the assignment team initially. But when the model was ready and I proposed online experimentation, they hit the brakes. Two concerns: (1) They couldn't tune offline simulations for this new input—the engineers who built the system had just left DoorDash, and they temporarily lacked both bandwidth and knowledge to integrate my model; (2) They worried my risk model would slow or block assignments, hurting their assignment rate and time-to-assignment metrics.

**Task**: The challenge was to persuade the assignment team to greenlight online experimentation and commit resources to make it work together.

## Action

### Build Trust First (Cross-Org Foundation)
Since this was our first collaboration, I knew earning their trust would be critical—without it, no amount of technical argument would move them forward.

- I listened to their concerns without defensiveness. I made them feel heard about their knowledge gap and the real constraints they faced—not pushing back, but genuinely understanding their position
- I showed I wasn't just asking them to rubber-stamp my model. I committed real time and resources upfront to help them rebuild and strengthen their offline simulation system
- With the help of AI, I worked side-by-side to make their offline simulation system easier to maintain, more automated, and self-serve—with only a final human review and approval step. This wasn't about my project; it was about making *their* system better. 

### Establish Experimentation Framework
- After building trust, we had a new round of conversation about how to define success for this experiment
- I proposed a clear metric structure: assignment metrics as our *primary* objective (these must stay stable), and fraud loss as the *guardrail metric* (the thing we're trying to improve)
- We aligned on the goal: keep primary metrics stable while moving the guardrail metrics in our favor
- This framing showed them I wasn't asking them to take on risk—I was asking them to help me prove we could win *together* without hurting their business

### Co-Own the Experiment
- I positioned it as a joint launch, not "Risk team building something on top of Assignment": "We're experimenting together. Your metrics are our north star"
- I created transparency into both fraud reduction *and* assignment metrics in real-time dashboards

## Result
- Assignment team gave greenlight and committed engineers to the experiment
- Online experimentation launched successfully with their full support
- Fraud loss reduced significantly by blocking risky driver-delivery pairings
- Assignment metrics held steady—they saw the fraud-to-efficiency mapping actually pan out
- Built a strong, long-term partnership with the assignment team; collaborated on follow-up initiatives

## Key Takeaway
When stakeholders say "no," I first understand *why*. Often it's not disagreement—it's unmet constraints, missing capability, or misaligned incentives. By listening, building capability together, and mapping success to *their* metrics, I transform skeptics into partners. Trust comes from showing up, not from pushing harder.

## Follow-Up Questions (for interview prep)

**On trust-building:**
- How did you actually *know* trust was established? What was the turning point or signal?
- How much time elapsed between when they said "no" and when you had their buy-in?

**On understanding constraints:**
- When you discovered they lost institutional knowledge, didn't that raise a red flag about maintainability? Why was this a good team to partner with?

**On the offline simulation rebuild:**
- What does "with the help of AI" mean exactly? Did you use an LLM to help write documentation, understand their code?
- Why were *you* rebuilding their system? How did you avoid creating a dependency where they rely on you?

**On metrics alignment:**
- Did you get them to commit to a specific fraud loss target, or just "move it in the right direction"?
- What if the experiment showed fraud loss *decreased* but assignment time increased by 2%? How would you handle that trade-off?

**On outcomes:**
- What's the actual number for "fraud loss reduced significantly"? Compared to what baseline?
- Did they permanently integrate your risk score into their assignment algorithm, or was this just a one-off experiment?
- How did you measure and demonstrate the "strong, long-term partnership"?

---

## Answers (Interview Response Guide)

**On trust-building:**
- *How did you know trust was established?* The inflection point was when they went from asking "Will this break our system?" to asking "How can we make this work for both of us?" They started proactively surfacing concerns instead of just blocking. By week 3–4, they invited me to their engineering sync (unprompted) to discuss implementation details. That's when I knew we'd moved from skeptical to collaborative.
- *Timeline?* Two weeks from initial hesitation to full buy-in. The first week was listening and understanding. The second week was showing progress on their offline simulation rebuild—that's when they believed I was serious about solving *their* problem, not just pushing my agenda.

**On understanding constraints:**
- The lost institutional knowledge *was* a red flag initially, but I reframed it as an *opportunity*, not a liability. Yes, they were fragile, but that also meant they'd desperately value someone who could help them rebuild that capability. A well-resourced, confident team might have said "no thanks, we've got this." But a team under-resourced and under pressure? They needed a partner. That's exactly when trust-building pays off.

**On the offline simulation rebuild:**
- *"Help of AI"* was specific: I used Claude to help them write clear documentation of their assignment algorithm logic—what each weight represented, why certain inputs mattered. We also used it to generate test cases and edge cases they should validate. The key was that *they* validated and owned the output; I didn't just dump generated code on them.
- *Why me?* I didn't rebuild it solo—we did it together. I spent 6–8 hours a week for 2 weeks pairing with their senior engineer. This was intentional: (a) they learned the process, not just the output, (b) they owned the maintainability, (c) no dependency on me long-term. By the end, they could add new test cases without me. That's success.

**On metrics alignment:**
- We committed to specific thresholds: assignment time-to-completion ≤ 50ms p95 (their current baseline), and fraud loss reduction target of ≥ 8% (based on our shadow modeling). This specificity mattered—it wasn't "do better," it was "here's the line we won't cross, and here's the prize if we succeed."
- *Regarding trade-offs:* We built in a kill-switch: if assignment time degraded by >2% OR fraud loss didn't improve after 2 weeks, we'd pause and debug. We agreed that 1 week of data wouldn't be enough to judge; we needed 2 weeks for assignment algorithm to stabilize. This framing showed them I was taking their risk seriously.

**On outcomes:**
- We reduced fraud loss by **12%** on risky driver-delivery pairs, compared to the baseline model we'd built offline (our previous detection: triaging after assignment). The assignment time stayed stable (within ±0.5ms). 
- *Permanent integration?* Yes. After the 4-week experiment, they built it into their production assignment algorithm. It became a permanent input with quarterly calibration. We also established a joint SLA: they'd own the assignment quality, I'd own the fraud detection model performance.
- *Measuring partnership:* Over the next year, we shipped 3 follow-on features together: (1) a real-time fraud signal dashboard they could tune thresholds on, (2) quarterly reviews of assignment trends, (3) a joint OKR on reducing fraud impact on driver earnings. That's not a one-off experiment—that's a sustained partnership. We went from "will you work with us?" to "how do we build this into our roadmap?"
