# Story 2: High-Stakes Tradeoff Under Uncertainty

**Situation**: Your fraud ML model had high accuracy but also high false positive rate, blocking legitimate users. The business wanted to ship it to reduce fraud losses, but you had concerns about user experience impact.

**Task**: Make a decision on model deployment with incomplete information—perfect accuracy wasn't possible.

## Action
- Set up a cross-functional meeting with product, ops, legal, and business
- Modeled the tradeoff: fraud losses prevented vs. user friction (account lockouts, support tickets)
- Proposed a phased rollout: start with high-confidence fraud signals, monitor false positive rate
- Built monitoring to catch when false positives exceeded acceptable thresholds
- Committed to weekly reviews with business to adjust thresholds as we learned
- Personally reviewed edge cases to understand where the model was failing

## Result
- Deployed safely: caught 40% of fraud with <2% false positive rate
- False positive rate stayed within tolerance over 3 months
- Gradually increased aggressiveness as we understood the failure modes
- Established a pattern for future model deployments (tradeoff framework, phased rollouts, monitoring)

## Key Takeaway
You think deeply about impact, listen to stakeholders, and make data-informed decisions under uncertainty. This is critical for safety work.
