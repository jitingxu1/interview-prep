# Interview Brief — Sergei Tolkachov, Sept 8, 4:00 PM PDT

## Open with a role probe (first 5 minutes)

The recruiter was vague — "AI" could mean applied AI on product surfaces, AI platform/infra, or trust & safety AI. You need to know within the first five minutes, because it changes which stories you tell.

After intros, when he asks if you have questions or hands you the floor:

> "Before I dive in — can you give me shape on the team? Is this closer to applied AI on product surfaces, AI platform and infrastructure, or trust and safety? And is the role managing engineers directly, or managers?"

That's not a stall. It's what a manager does. Then aim your stories at the answer:

| If he says… | Lead with |
|---|---|
| Applied AI / product surfaces / relevance | Airbnb engagement work + agentic support automation + S10 (cross-org product launch) |
| AI platform / infrastructure | Ibis & Ibis-ML open source + S8 (built agent infra) + risk data platform |
| Trust & safety / anti-abuse | Fraud detection is your home turf — S2, S10, the whole DoorDash risk story |
| Manager of managers | Be honest: you lead 12 across two pods with senior ICs owning areas. Frame it as *ready for, not done yet* — see "Growth" below. |

---

## Theme 1 — Build, support, scale high-performing teams

**What he's listening for**: Did you actually build something, or did you inherit it? Can you name individuals and what changed for them? Do you make hard people calls?

**Your lead**: You built a 12-person ML/AI team from zero across two pods. That's the headline — say it early.

| Question shape | Story |
|---|---|
| "Tell me about building a team" | S1 (transition, built from scratch) + S4 (hiring/leveling) |
| "Tell me about developing someone" | S7 (mid → senior IC) |
| "Someone struggling / hard people call" | **S8 (right person, wrong seat)** — this is your most distinctive story. Lead with it. |
| "Psychological safety / conflict" | S6 |

**S8 is your best people story** because it shows diagnosis, not just empathy: you correctly identified that a strong backend engineer was failing at ML decisions, and instead of managing him out you found the agent-infrastructure work where he'd win. Most candidates only have PIP stories. Tell this one.

**Weakness to expect**: he may ask "have you ever managed someone out?" You don't have that story. Don't invent one. Say plainly: "I haven't had to terminate someone. The closest I've come is [S8], where the honest read was skill-fit rather than performance, and I had somewhere to put those strengths. If repositioning hadn't been available, I'd have gone to a clear, time-bound plan and been direct that the outcome was in question."

---

## Theme 2 — Execution, tradeoffs, ambiguity

**What he's listening for**: Do you make decisions, or do you socialize them forever? Can you name what you gave up?

| Question shape | Story |
|---|---|
| "Hardest tradeoff" | S2 (fraud recall vs. false positives, phased rollout, guardrails) |
| "Operating in ambiguity" | S1 (no manager, no playbook, stepped in within 24 hours) |
| "Protecting execution" | S3 (meeting burden 50% → 20%, shipped 4 weeks early) |

**Sharpen S2.** As written it's thin: "40% of fraud at <2% false positive." At this level he'll ask what that meant in dollars, how many legitimate users got blocked, and who disagreed with you. Have those numbers, or an honest "I can't share exact figures, but the order of magnitude was X."

**Have ready, and you currently don't**: a story about a project that slipped or something you shipped that didn't work. This is asked in most manager screens. See `risks.md`.

---

## Theme 3 — Cross-functional partnership & influence at scale

**What he's listening for**: Can you move a team you don't control? Do you understand what your Product partner is optimizing for?

**Your lead**: **S10 (embedding fraud risk into assignment ranking)** is your strongest story in the whole kit. It has everything a senior interviewer wants:

- A partner team that said no
- You understood *why* they said no (lost tribal knowledge + fear of hurting their metrics)
- You paid a real cost to earn the yes — you rebuilt *their* simulation system, which wasn't your job
- You made their metric the primary objective and yours the guardrail — that's the move that shows you understand incentives
- Joint launch, shared dashboards

**Tell it as your influence story. Practice it at 2 minutes.** The one thing to add: state the scale — how many teams, how long the alignment took, what the launch was worth.

**Gap to name honestly**: "influence at scale" at LinkedIn means many teams and many layers. Your best example is one partner team. Don't overclaim. Generalize the playbook instead: *understand their metric, absorb their cost, make their success the primary objective.* That's what transfers.

**Product specifically**: he'll probe this. Have an answer for "where do you and your PM disagree most?" A real one. "We don't disagree" is a red flag.

---

## Theme 4 — Growth trajectory

**What he's listening for**: Do you know what you're not good at yet? Is your ambition compatible with this role?

Use the material in `leadership/manager_qa.md`, but tighten to two things, not three. Pick the two that are true and specific:

1. **Scaling through others rather than through yourself.** At 12 engineers you can still be in every important decision. At 25+ you can't. "I want to get better at growing the layer below me so I'm not the connective tissue."
2. **Executive communication.** Translating technical tradeoffs into business framing for senior leadership.

Drop the "conflict navigation" one — it's vaguer and it reads as a weakness without a plan.

**On trajectory**: if asked where you want to be in three years, say manager of managers, and say why in terms of the work: "I want the scope where I'm setting technical direction across several teams rather than one." Don't hedge — hedging at a leadership screen reads as low ambition.

---

## Delivery notes

- **Rewrite in your head to first person.** Most of your STAR files are written in second person ("You called a team meeting"). If that leaks into your speech it sounds coached. Say "I."
- **Numbers.** Have three real ones ready: team size grown, fraud loss prevented, meeting load reduced. Vague metrics get probed.
- **Two-minute cap per story.** Then stop and ask "want me to go deeper on any part of that?"
- **Don't recite.** He asked four themes; he'll follow his own thread. Listen to the actual question.
