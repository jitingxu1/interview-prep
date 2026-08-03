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
