# Assignment ranking experimentation: Navigating Difficult Stakeholder Alignment

**Situation**: I'd built a delivery-level risk score that worked well for triaging fraud after assignment. Now I wanted to shift from reactive to proactive—embed this risk score into the assignment algorithm to block risky deliveries *before* assignment happened.

I had buy-in from the assignment team initially. But when the model was ready and I proposed online experimentation, they hit the brakes. Two concerns: (1) They couldn't tune offline simulations for a new input—the engineers who built the system had left DoorDash, and they lacked bandwidth to understand how to integrate my model; (2) They worried my risk model would block assignments, hurting their assignment rate and time-to-assignment metrics.

**Task**: The challenge was to persuade the assignment team to greenlight online experimentation and commit resources to make it work together.

## Action

### Understand Their Real Constraints
- I didn't push back on their concerns. Instead, I went deeper: "Walk me through how your assignment algorithm works. What's hard about adding a new input?"
- I discovered the real problem: they had lost institutional knowledge when key engineers left. They had no way to validate offline that a new weighted input wouldn't break their system
- I realized the tension: they weren't being defensive—they were genuinely under-resourced

### Build Capability Together
- I volunteered to help them *understand and rebuild* the offline simulation system
- I worked side-by-side to document how their weighting system worked, wrote clear tests, made the system reviewable
- This wasn't a quick ask—it was a commitment to their success, not just mine

### Align on Shared Metrics
- I acknowledged their concern: "You're right—we can't impact assignment time. Let's make that a guardrail metric during experimentation"
- I built a system that mapped fraud cost savings *into assignment time improvements*: fraud avoided → faster, higher-quality assignments → better assignment utilization
- I showed them the math: "If we block risky deliveries, you're not losing capacity—you're reallocating it to higher-probability assignments"

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
