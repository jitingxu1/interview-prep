# Reporting Up — How to Brief Leadership

The fix for weakness #2 in [`weaknesses.md`](./weaknesses.md#2-too-technical-when-reporting-up): as a former tech lead, the default is to explain how something works. Leadership needs what it costs and what it buys. Use this before any exec update, and as concrete evidence when an interviewer asks "how did you fix it?"

---

## The core principle: bottom line up front

Leadership cares about three things, in this order:

1. **What do you need from me?** A decision, resources, or just awareness.
2. **What's the business impact?** Dollars, customers, risk, timeline.
3. **How confident are you?** Where the risk is, what the fallback is.

Technical detail comes last, **and only if they ask.** Keep it in an appendix, not the talk track.

---

## Four templates

### 1. Asking for a decision (the most important one)

> **Ask:** "I need a decision on X by [date]."
> **Options:** "Two options: A does ___, B does ___."
> **Recommendation:** "I recommend A, because [business reason]."
> **Cost / risk:** "The tradeoff is ___. If it goes wrong, we'll know by ___ and roll back."

**❌ Technical version:**
"Our new model's precision went from 0.82 to 0.89, recall dropped a bit, we tested three thresholds, it's XGBoost with 20 new features..."

**✅ Bottom-line version:**
"I need a go/no-go on the new fraud model by Friday. I recommend we ship at the conservative threshold: it prevents about [$X] a month in fraud and blocks under [2%] of good customers. We'll roll out to 10% first and expand weekly if the false-positive rate holds."

### 2. Status update

> **One-line status:** "On track / at risk / off track."
> **What changed since last time:** 1–3 bullets, impact only.
> **What I need from you:** If nothing, say "nothing needed."

The red/yellow/green goes in the **first line**, so leadership knows in one glance whether to keep reading.

### 3. Bad news

> **What happened:** One sentence.
> **Impact:** Who's affected, how much.
> **What we've done:** Mitigation already in place.
> **What's next:** Next step and when.
> **What I need:** Anything requiring their involvement.

Rule: **deliver bad news early, and with a plan.** Don't wait until you've figured everything out. What leadership hates most is hearing it from someone else first.

### 4. Impromptu — hallway, elevator, Slack ping

> "Short version: [conclusion]. The main risk is [one thing]. I'll send details by [time]."

Under 30 seconds. Being caught off guard is exactly when the instinct to dive into technical detail kicks in. **One sentence of conclusion, then "I'll follow up with details"** — that's enough.

---

## Translating technical into business

| Technical | What leadership hears |
|---|---|
| Precision / recall improved | X fewer good customers blocked, $Y more fraud caught |
| Latency down 200ms | Conversion up / users waiting less |
| Refactored the pipeline | New models ship in 2–3 weeks instead of 6–8 |
| Agent tool-calling accuracy up | Auto-resolution up X%, Y fewer manual tickets a month, $Z saved |
| Tech debt | If we don't fix it, every new feature next quarter takes X extra weeks |

Before every update, ask: **"So what?"** If a technical statement can't answer "what does this mean for the business," it isn't translated yet.

---

## Pre-flight checks

1. **Two-line test:** Reading only the first two lines, can they tell what I need and what the impact is?
2. **30-second test:** Can I say the conclusion and impact out loud in 30 seconds?
3. **First-question test (after):** If their first question is "so should we do it?", it landed. If it's "what did you mean by X?", the conclusion was buried.

---

## Using this in interviews

- **As evidence for weakness #2.** "How did you fix it?" → the decision template, the two-line test, the first-question test. Concrete mechanisms beat "I'm working on it."
- **As your answer format.** ByteDance's **Be Candid and Clear** value expects conclusion first and data behind it — answer every interview question with the same structure.
- **For business-leader rounds** (e.g., TikTok's Head of short video): use the translation table. Talk creator, content, and cost outcomes, not architecture.
