# Story 6: Handling Team Conflict & Building Psychological Safety

**Situation**: Two senior engineers on your fraud detection team had a heated disagreement about the architecture for the new model serving system. One wanted a microservices approach (more complex but flexible), the other wanted a monolithic system (simpler but less flexible). The tension spilled over into code reviews—they were being critical of each other's work, and it was starting to affect team morale.

**Task**: Resolve the conflict and establish a framework for how the team makes technical decisions together.

## Action
- Met 1:1 with each engineer separately to understand their concerns (not just the technical disagreement, but what was really bothering them)
- Learned that Engineer A felt unheard in previous decisions, and Engineer B felt their experience was being dismissed
- Scheduled a structured 1-hour meeting with both (not a free-for-all debate)
- Set ground rules: listen to understand, not to win; focus on tradeoffs, not egos
- Asked each to present their proposal with assumptions, tradeoffs, and unknowns (in writing before meeting)
- Facilitated the discussion: "What's your biggest concern with their approach?" instead of "Who's right?"
- Proposed a hybrid approach: start with the monolith but design for future migration to microservices
- Created a decision-making framework for future architecture: team votes, I break ties if needed, we all commit to the decision

## Result
- Both engineers felt heard; relationship recovered
- Hybrid approach shipped on time and performed well
- Team learned how to disagree productively
- They established a "architecture council" pattern for future decisions—senior engineers propose, team debates, decision is made transparently
- Morale improved; people felt safe to disagree without personal friction

## Key Takeaway
You don't avoid conflict—you create structures that let people disagree productively. You care about psychological safety. You don't make every technical decision; you teach the team how to decide.
