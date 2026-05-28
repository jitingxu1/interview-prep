# STAR Stories for Behavioral Questions

## Story 1: Leading Through Management Transition
**Situation**: Your manager left the Risk ML team, leaving 10 engineers without leadership during a critical period.

**Task**: You stepped in as Tech Lead Manager—managing both technical strategy and people for the first time at full scale.

**Action**:
- Immediately stabilized the team by being transparent about the transition
- Maintained technical credibility by staying hands-on with critical fraud detection work
- Set clear priorities: keep the engine running (production fraud systems) while building team processes
- Implemented 1:1s with each engineer, learned their goals and pain points
- Worked with HR on hiring for a technical lead to eventually take on IC responsibilities
- Built a team roadmap that balanced technical debt, new capabilities, and team growth

**Result**:
- Team stayed productive through transition (no churn)
- Hired 2 new engineers and promoted 1 to senior IC role
- Established team processes (design reviews, postmortems, career conversations)
- Maintained fraud detection SLAs while investing in tech foundation

**Key takeaway for Roblox**: Showed you can lead under pressure, wear multiple hats, and scale people systems.

---

## Story 2: High-Stakes Tradeoff Under Uncertainty
**Situation**: Your fraud ML model had high accuracy but also high false positive rate, blocking legitimate users. The business wanted to ship it to reduce fraud losses, but you had concerns about user experience impact.

**Task**: Make a decision on model deployment with incomplete information—perfect accuracy wasn't possible.

**Action**:
- Set up a cross-functional meeting with product, ops, legal, and business
- Modeled the tradeoff: fraud losses prevented vs. user friction (account lockouts, support tickets)
- Proposed a phased rollout: start with high-confidence fraud signals, monitor false positive rate
- Built monitoring to catch when false positives exceeded acceptable thresholds
- Committed to weekly reviews with business to adjust thresholds as we learned
- Personally reviewed edge cases to understand where the model was failing

**Result**:
- Deployed safely: caught 40% of fraud with <2% false positive rate
- False positive rate stayed within tolerance over 3 months
- Gradually increased aggressiveness as we understood the failure modes
- Established a pattern for future model deployments (tradeoff framework, phased rollouts, monitoring)

**Key takeaway for Roblox**: You think deeply about impact, listen to stakeholders, and make data-informed decisions under uncertainty. This is critical for safety work.

---

## Story 3: Unblocking Engineers & Building Technical Culture
**Situation**: Your team was spending ~30% of time in meetings, context-switching between code reviews, design reviews, oncall rotation, and manager syncs. Productivity was suffering, and engineers were frustrated.

**Task**: Improve focus time and engineering velocity while maintaining quality and safety.

**Action**:
- Surveyed the team to understand pain points (meetings were biggest complaint)
- Designed a "focus window" policy: 10am-3pm no meetings, async updates via design docs/Slack
- Moved oncall rotation to dedicated weekly coverage instead of ad-hoc paging
- Consolidated design reviews into twice-weekly batches instead of ad-hoc interruptions
- Established an async design doc template for easy review (fraud models, pipeline changes, etc.)
- Modeled the behavior myself—blocked my calendar, responded to Slack async

**Result**:
- Focus time increased from 30% to ~60%
- Code review cycle time dropped from 3 days to 1 day (less context switching)
- Oncall satisfaction improved; team knew when they were on rotation
- Shipped major fraud detection infrastructure upgrade 4 weeks ahead of schedule

**Key takeaway for Roblox**: You care about engineer productivity and well-being, and you're willing to rethink processes to unblock them. You model the behavior you want to see.

---

## Story 4: Hiring & Leveling to Scale
**Situation**: You inherited a team of 10 mostly mid-level engineers. Your manager cycle was shifting toward strategy and hiring, but you needed to grow technically to support the roadmap.

**Task**: Scale the team while increasing senior IC contributions.

**Action**:
- Identified 2 engineers with IC potential and created leveling plans (technical depth, ownership of systems, mentoring junior engineers)
- Defined a hiring rubric for new engineers: ML fundamentals + platform/fraud understanding
- Conducted technical interviews alongside recruiting (stayed credible, learned about candidates)
- For leveled engineers: gave them ownership of major projects (fraud ring detection system, new feature rollout)
- Created a "technical mentoring" culture: senior engineers reviewed junior engineers' code and design docs, not just me
- Set clear expectations: high performers get autonomy and mentorship, mid-level get clear growth plans

**Result**:
- Promoted 1 engineer to senior IC role (now leads 2 other engineers)
- Hired 2 new mid-level engineers who integrated quickly
- Team now has healthy IC hierarchy: 1 senior IC, 4 mid-level, 3 junior, 2 expanding scope
- Reduced my personal code review bottleneck; senior IC now owns code quality

**Key takeaway for Roblox**: You think about scaling teams, you're intentional about hiring, and you develop talent. You're building an organization, not just managing individuals.

---

## Story 5: Learning & Growth in New Role
**Situation**: You'd never been a full manager before stepping into the dual role. Mistakes happened—you had a tough conversation with an engineer about performance that didn't land well, and they felt blindsided.

**Task**: Learn from the mistake and build better processes.

**Action**:
- Asked for feedback from the engineer (vulnerable, honest conversation)
- Realized you hadn't set clear expectations upfront for the performance area
- Implemented mid-cycle feedback (not just end-of-cycle) for all engineers
- Created a feedback template: situation (what I observed), impact (why it matters), expectation (what success looks like), support (how I'll help)
- Got coaching from your HR partner on difficult conversations
- Revisited the conversation with the engineer, acknowledged the misstep, set a new plan together

**Result**:
- Engineer stayed on the team, performance improved, relationship recovered
- Entire team benefited from clearer expectations and more feedback
- You built credibility by being open about learning

**Key takeaway for Roblox**: You're a learner, you take feedback well, and you iterate on your management approach. You're humble about what you don't know.

---

## How to Use These Stories

1. **Listen for the question**, don't just recite stories
   - "Tell me about a time you made a hard decision" → Story 2
   - "How do you develop your team?" → Stories 3, 4
   - "How do you handle feedback?" → Story 5
   - "What's your management style?" → Story 3 or 4

2. **Adapt and personalize**
   - Use real details (dates, team names, specific metrics)
   - Be honest if you made mistakes or learned something hard
   - Connect back to Roblox when possible ("This is like critical harm because...")

3. **Have 1-2 minute versions ready**
   - Full story = 3-5 minutes
   - Short version = 1-2 minutes (Situation + Action + Result, skip Task detail)

4. **Practice telling them out loud**
   - You'll remember better
   - You'll sound more natural and less rehearsed
   - You can gauge interviewer interest and adjust depth
