# Ask DoorDash agent memory (study notes)

[← Project deep dives](README.md)

How the Ask DoorDash agents fetch, use and write consumer memory, with flowcharts and worked examples. Study material for agent system design questions (memory, personalization, context engineering), not a project of yours.

**Sources:**
- [Building Ask DoorDash (Part 2): Intelligence](https://careersatdoordash.com/blog/building-ask-doordash-part-two-intelligence/) — June 18, 2026. Zhucheng Zhan, Raghav Saboo, Heather Song, Fan Xia, Xiaochang Miao.
- [Building DoorDash Assistant: An engineering overview](https://careersatdoordash.com/blog/building-doordash-assistant-an-engineering-overview/) — June 11, 2026.

> **What's from the posts vs. illustrated.** The architecture, the four-stage pipeline, the save/forget rules and the impact numbers come from the posts. The posts only name `memory_search` and a "scan" action and show one result object, so the tool parameters, query plans and data in the examples are **illustrations**, not DoorDash's real API.

---

## Summary (one page)

**Why memory:** agents start every session from zero. Memory-backed sessions did measurably better (7-day early snapshot, memory vs. no memory):

| Metric | Change |
| --- | --- |
| Grocery checkout conversion (relative) | **+24%** |
| Grocery basket size | **+17%** |
| Grocery conversation turns | **−7%** |
| Restaurant conversion, open-ended queries (relative) | **+15%** |
| Misunderstood intent (LLM judge) | **−33%** |
| Egregiously irrelevant results (LLM judge) | **−24%** |

**Three gaps the system closes:**
1. **Direct connectivity:** producing memory blocks is not the same as using them; an agent needs query planning, hybrid retrieval, ranking and injection at the right moment.
2. **Task awareness:** different tasks need different memories; naive top-K by similarity wastes context and misses facts that matter.
3. **Signal loss:** durable facts mentioned in chat die with the session unless they're extracted and written back.

**Three memory types:**

| Type | Source | Cadence | Examples |
| --- | --- | --- | --- |
| **Long-term** | Batch LLM pipelines over behavioral history | Offline, scheduled; versioned blocks | Dietary Preference, Dining Patterns, Item Brand, Item Taxonomy, Store Preferences, Cross-Channel Patterns; 100+ facts for a heavy user |
| **In-session** | Live app activity | Real time, recency-weighted | Cart, active searches, items viewed or rejected |
| **Conversational** | What the user states in chat | Per turn, via extraction | "I prefer Oatly," "household of four" |

**Three layers:**

```
 Offline batch LLM pipelines ──write──►  ┌───────────────────────────┐
 (order history → memory blocks)         │  TOOLING LAYER            │
                                         │  plan · retrieve · rank · │ ◄──── agents call tools
 Agents (conversation facts) ──write──►  │  package · extract · dedup│       (memory_search, scan…)
                                         └────────────┬──────────────┘
                                                      ▼
                                   Managed Agent Services (storage)
                                   distributed SQL + vector/ANN search,
                                   namespaces per signal type × consumer
```

- **Storage** "does not understand tasks or agents; it merely stores and retrieves."
- **Ingestion never blocks reads:** text is readable immediately; embeddings are computed asynchronously (server-side at write time is the main path; bulk loads bring precomputed embeddings).
- **Namespaces:** isolated per signal type (a grocery agent can't surface restaurant data), except a **shared namespace** for cross-vertical facts like household size and vegetarianism.

---

## 1. One turn, end to end

```
 User: "Make chicken tikka masala for dinner"
   │
   ▼
┌──────────────────────┐
│ Orchestrator         │── route ──► Grocery agent (pinned for follow-ups)
└──────────────────────┘
   │
   ▼
┌──────────────────────────────────────────────────────────────────────┐
│ GROCERY AGENT (LLM)                                                  │
│                                                                      │
│  System prompt already has (once per session):                       │
│    • Memory Bank Index: tokens that exist in this user's memory      │
│    • Skill: "recipe → shopping list" instructions                    │
│                                                                      │
│  ① calls memory tool ──────────────┐                                 │
│                                    ▼                                 │
│              ┌─────────────────────────────────────────┐             │
│              │ MEMORY TOOLING LAYER                    │             │
│              │  1. Intent & scope resolution           │             │
│              │  2. Query planning                      │             │
│              │  3. Retrieval & ranking  ──► storage    │             │
│              │  4. Context packaging                   │             │
│              └───────────────┬─────────────────────────┘             │
│  ② gets ~5-10 facts ◄────────┘                                       │
│                                                                      │
│  ③ calls grounding tools (store search, item search, cart)           │
│  ④ reconciles memory ↔ live data                                     │
│  ⑤ renders widget + reply                                            │
│  ⑥ fires memory extraction job (background, fire-and-forget)         │
└──────────────────────────────────────────────────────────────────────┘
```

## 2. Inside the tooling layer (read path)

```
 Agent call:  memory_search(query="what I need to cook chicken tikka masala")
      │
      ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. INTENT & SCOPE RESOLUTION                                │
│    task type?          → recipe                             │
│    which memory kinds? → pantry, portion size, protein,     │
│                          dietary, brand                     │
│    freshness rules?    → pantry: strict (items get used up) │
│                          dietary: none (stated, no TTL)     │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. QUERY PLANNING  (one sub-query per need)                 │
│    each = (modality, target namespace, filter envelope)     │
│    over-fetch, since filters will drop some candidates      │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. RETRIEVAL & RANKING                                      │
│    run sub-queries in PARALLEL across namespaces            │
│    one source fails? → degrade gracefully, keep the rest    │
│    merge → dedupe → rank by relevance → recency breaks ties │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. CONTEXT PACKAGING                                        │
│    trim to context budget, return structured facts:         │
│    {category, content, timestamp, relevance, durability}    │
└─────────────────────────────────────────────────────────────┘
```

**Stage 1 — which memories each task needs (from the post):**

| Task | Memories needed |
| --- | --- |
| "Find a dinner spot" | Cuisine tendencies, price point, daypart, recent orders |
| "Make chicken tikka masala" | Pantry inventory, portion size, protein preferences |
| "Shop my usuals" | Order history, replenishment patterns |
| "Get me snacks" | Brand affinities, dietary constraints |

**Stage 2 — the three query axes:**
- **Modality:** semantic (embeddings), deterministic keyword, or direct structured fetch.
- **Target:** which namespaces or memory chunks.
- **Filter envelope:** top-K, similarity floor, fact category, recency window.

**Stage 4 — the result shape (from the post):**

```json
{"fact_id": "mem_892a", "category": "brand_preference",
 "content": "Prefers Oatly oat milk", "timestamp": "2026-05-12T14:23:00Z",
 "relevance_score": 0.91, "durability": "stated"}
```

The agent's task-specific instructions (a skill-based prompt system) decide how each fact is used: reasoning context, input to product search, or a strict exclusion.

---

## 3. Worked examples

### Example A — Recipe → shopping list (exclusion)

**User:** "Make chicken tikka masala for dinner."

**Query plan:**

| # | Need | Modality | Target namespace | Filter envelope |
| --- | --- | --- | --- | --- |
| q1 | What's already at home | Structured fetch | `pantry` | Recency window that depends on the item |
| q2 | How many people | Structured fetch | `shared/household` | None (durable) |
| q3 | Protein and dietary limits | Semantic | `shared/dietary`, `taxonomy` | top-K=10, similarity ≥ 0.7 |
| q4 | Brands for recipe ingredients | Keyword ("chicken", "yogurt", "rice") | `brand` | top-K=5 |

**Raw results (over-fetched, then filtered):**

```
pantry:    "olive oil" (80d ago) ✅ kept: oil lasts
           "milk" (12d ago)      ❌ dropped: past milk's lifetime
           "basmati rice" (20d)  ✅ kept
           "garam masala" (45d)  ✅ kept
household: "cooking for 4"       ✅
dietary:   "no pork"             ✅   "likes spicy food" ✅
brand:     "prefers Fage yogurt" ✅   "Oatly oat milk" ❌ not relevant to this recipe
```

**Returned to the agent:**

```json
[
 {"category":"household", "content":"Cooks for 4",               "durability":"stated"},
 {"category":"pantry",    "content":"Has basmati rice",          "durability":"inferred"},
 {"category":"pantry",    "content":"Has garam masala",          "durability":"inferred"},
 {"category":"pantry",    "content":"Has olive oil",             "durability":"inferred"},
 {"category":"brand",     "content":"Prefers Fage Greek yogurt", "durability":"stated"},
 {"category":"dietary",   "content":"Likes spicy food",          "durability":"inferred"}
]
```

**How the agent uses each fact:**

```
 "Cooks for 4"      → SCALE:        recipe quantities × 2 (base serves 2)
 pantry items       → EXCLUDE:      skip rice, garam masala, oil
 "Fage yogurt"      → SEARCH INPUT: item_search("Fage Greek yogurt")
 "Likes spicy"      → REASONING:    add extra chilies, mention it in the reply
```

**Reconcile with live data:**

```
 item_search("Fage Greek yogurt", store=Safeway)
   → OUT OF STOCK
 agent: pick the closest substitute (Chobani Greek) and SAY SO:
   "Fage is out at Safeway today, so I used Chobani instead."
```

### Example B — Restaurant discovery (reasoning context + shared namespace)

**User:** "Find me a dinner spot."

```
 1. INTENT     restaurant discovery, dinner daypart
               needs: cuisine tendencies, price sensitivity, daypart patterns,
                      recent orders (to avoid repeats), dietary

 2. PLAN       q1 semantic  → dining_patterns   "dinner cuisine preferences"  top-K 8
               q2 fetch     → recent_orders     last 14 days (strict recency)
               q3 fetch     → shared/dietary    (cross-vertical, learned in grocery!)
               q4 semantic  → price             "price sensitivity dinner"

 3. RETRIEVE   in parallel. Suppose recent_orders TIMES OUT
               → graceful degradation: continue without it

 4. RETURN     "Orders Thai ~3x/month"  "Usually $20-35 for dinner"
               "Vegetarian household"   ← saved during a GROCERY conversation
```

- The agent searches open Thai and similar restaurants in $20–35 with strong vegetarian options.
- "Vegetarian household" came from the **shared namespace**: learned by the grocery agent, used by the restaurant agent, and the user never repeats it.
- **Isolation:** the restaurant agent can't reach the grocery `brand` namespace, so "prefers Oatly" never appears in restaurant results.

### Example C — "Shop my usuals" (scan before read)

Order history is large; pulling it all would blow the context budget.

```
 Agent ── scan(namespace="order_history") ──► tooling
   ◄── {total_orders: 212, last_90d: 31,
        top_categories: ["dairy","produce","snacks","household"],
        replenishment_signals: available}            ← cheap metadata only

 Agent decides: only need recurring items, last 90 days

 Agent ── memory_search(target="order_history",
                        filter={window:"90d", min_frequency:3}) ──►
   ◄── 14 recurring items with typical cadence
        "Milk, every ~7 days, last bought 9 days ago"     → DUE, add
        "Paper towels, every ~30 days, last 6 days ago"   → NOT DUE, skip
        "Bananas, every ~5 days, last bought 6 days ago"  → DUE, add
```

List first, then read only what's needed, like running `ls` before `cat`.

### Example D — Keyword lookup with the Memory Bank Index

The agent is editing a shopping list and wants a brand preference by name.

```
 System prompt (injected once per session):
 ┌──────────────────────────────────────────────┐
 │ MEMORY BANK INDEX                            │
 │ brand:    oatly, fage, kerrygold, barilla    │
 │ taxonomy: oat milk, greek yogurt, pasta      │
 │ dietary:  vegetarian, dairy-free             │
 └──────────────────────────────────────────────┘

 ✅ Agent: memory_search(mode="keyword", target="brand", terms=["barilla"])
          → "Prefers Barilla pasta"      (term is in the index → guaranteed hit)

 ❌ Without the index, the agent guesses:
          terms=["De Cecco","pasta brand","spaghetti"] → nothing; wasted tokens
```

Keyword search fits here because the agent already has the exact words: lower latency, transparent scoring, and the index means it never searches blind.

---

## 4. Write path

### Saving — after every turn, in the background

```
 User turn finishes
   │
   ├──► reply streams to the user (no waiting)
   │
   └──► fire-and-forget: extract_memory(turn)
            │
            ▼
   ┌──────────────────────────────────────────────────┐
   │ EXTRACTION LLM: the policy gate                  │
   │  durable + explicit?           ─no──► drop       │
   │  domain durability rule?       (restaurant: needs│
   │                                 "always/never")  │
   │  user-initiated, not passive?  ─no──► drop       │
   │  health/medical?               ─yes─► NEVER save │
   └──────────────┬───────────────────────────────────┘
                  ▼
   ┌──────────────────────────────────────────────────┐
   │ DEDUP & CONSOLIDATE                              │
   │  search existing facts on the same topic         │
   │   none          → INSERT                         │
   │   overlapping   → MERGE                          │
   │   refined       → UPDATE in place                │
   │   contradicted  → DELETE old, INSERT new         │
   └──────────────┬───────────────────────────────────┘
                  ▼
   write text instantly (readable now) + embed async (searchable soon)
```

| User says | Agent | Saved? | Why |
| --- | --- | --- | --- |
| "We're a family of four" | Grocery | ✅ shared namespace | Stable, explicit, applies across verticals |
| "I prefer Oatly" | Grocery | ✅ brand | In grocery, a casual brand mention counts as durable |
| "I don't want ramen" | Restaurant | ❌ | A passing mood: no "always" or "never" |
| "I **never** eat ramen" | Restaurant | ✅ | Explicit durability language |
| "What's cheap at Safeway?" | Grocery | ✅ price-sensitive | The user started the price framing |
| Accepts the cheaper store the agent suggested | Grocery | ❌ | Passive acceptance doesn't count |
| "Getting this for a friend tonight" | Any | ❌ | One-off |
| "I'm diabetic" | Any | ❌ never | Health information is blocked even on request |
| "I'm vegan now" (old fact: vegetarian) | Any | ✅ update | Contradiction: replace the old fact |

### Forgetting — two stages, synchronous

```
 User: "Forget that I like Nova's grilled cheese"
   │
   ▼
 Stage 1: semantic search(deletion query) → candidates
   [0] "Likes Nova's grilled cheese"
   [1] "Orders from Nova Café weekly"
   [2] "Prefers sharp cheddar"
   [3] "Likes grilled cheese sandwiches"
   │
   ▼
 Stage 2: separate LLM, given the candidates + the original request,
          told "don't delete facts that are merely related"
   → returns [0]
   │
   ▼
 delete [0] (parallel deletes if several), wait for confirmation
   │
   ▼
 Agent: "Done, I've forgotten that you like Nova's grilled cheese.
         I still remember you order from Nova Café weekly."
```

A naive similarity threshold would also have deleted [1], [2] and [3]. Saving is fire-and-forget; deleting is synchronous so the agent can confirm exactly what it forgot.

### Lifecycle depends on what the fact is about

- Stated lifestyle preferences (vegan, gluten-free): **no TTL**, kept until the user says otherwise.
- Food preferences: evolve slowly. Ordering patterns: seasonal.
- Pantry staples: depends on the item. Oil bought 80 days ago is probably still there; milk bought 12 days ago is gone.
- A blanket "older than X is stale" rule wastes durable signal and over-trusts ephemeral signal.

---

## 5. Cheat sheet — one fact, four uses

| Use | Example fact | What the agent does |
| --- | --- | --- |
| **Reasoning context** | "Orders Thai 3×/month" | Leans toward Thai in recommendations |
| **Search input** | "Prefers Fage yogurt" | `item_search("Fage Greek yogurt")` |
| **Hard exclusion** | "Has olive oil at home" | Leaves it off the list |
| **Parameter** | "Cooks for 4" | Scales recipe quantities |

**Live data always wins:** memory says what the user wants; tools say what's actually available right now.

---

## 6. Lessons from the post

- **Exclusion is harder than inclusion.** With 100+ facts, injecting too many made the agent **start dropping instructions**. Retrieval has to be task-aware, not top-K by similarity.
- **Memory as a tool, not an agent feature.** Otherwise every new agent team re-solves query planning, context budgeting, extraction and deduplication. Grocery and restaurant agents register the same interfaces with vertical-specific extraction rules, sources and ranking.
- **Embedding strategy:** they launched with static precomputed embeddings for read latency, then moved to server-side embedding at write time. Static embeddings freeze the model choice; upgrading means reprocessing the whole corpus.
- **The flywheel compounds:** better memory → better agent behavior (e.g., auto-scaling recipes to the saved portion size) → more trust and engagement → more conversational signal to capture.

## 7. Connections to other notes

- **Support chatbot case state** ([chatbot_offline_simulator.md](chatbot_offline_simulator.md)): same lesson — raw context becomes noise; give the model a curated, structured slice.
- **Super-agent context assembly:** "start minimal, inline by locality, spill and recall on demand" is the same idea as task-aware retrieval, scan before read, and the Memory Bank Index.
- **Ask DoorDash evaluation:** the −33% misunderstood-intent number comes from the same calibrated LLM-judge approach as the support simulator.

## 8. Evaluating the memory pipeline (proposed design)

> **Not from the posts.** DoorDash only reports end-to-end results (A/B conversion and judge-measured intent errors). This is a proposed per-stage design, built from standard retrieval evaluation plus the calibrated binary judges from the [support simulator](chatbot_offline_simulator.md).

### The failure funnel

When an answer is badly personalized, find the **first stage where the needed fact got lost**:

```
 Was the needed fact IN the store?         no → write path problem (extraction)
        │ yes
 Did INTENT ask for that memory kind?      no → intent/scope error
        │ yes
 Could the PLAN reach it?                  no → planning error (wrong namespace/filter)
        │ yes
 Did RETRIEVAL rank it in?                 no → retrieval/ranking error
        │ yes
 Did PACKAGING keep it within budget?      no → packaging/trim error
        │ yes
 Did the AGENT use it correctly?           no → usage error (prompt/skill)
        │ yes
 ✅ fact made it all the way through
```

### The golden set

Each case is **(user memory snapshot, task) → expected answers per stage**:

```yaml
case_id: recipe_017
memory_snapshot:        # a synthetic or anonymized user with known facts
  - pantry: "Has basmati rice" (20d)
  - pantry: "Has milk" (12d)          # should be filtered out as stale
  - household: "Cooks for 4"
  - brand: "Prefers Fage yogurt"
  - brand: "Prefers Oatly"            # distractor: irrelevant to this task
task: "Make chicken tikka masala"
expected:
  intent: recipe
  memory_kinds: [pantry, household, dietary, brand, protein]
  must_return:   [basmati rice, cooks for 4, Fage]
  must_not_return: [milk (stale), Oatly (irrelevant)]
  agent_behavior: [exclude rice, scale ×2, search Fage]
```

Labels come from **planted facts** in synthetic users (you know exactly what should come back), a **calibrated binary relevance judge** ("is fact X relevant to task Y?"), and human labels on sampled production traces.

### Metrics per stage

| Stage | Metrics |
| --- | --- |
| **1. Intent & scope** | Task-type accuracy; **memory-kind recall** (a missing kind is unrecoverable downstream — weight it over precision); memory-kind precision; freshness-rule correctness |
| **2. Query planning** | **Plan coverage** (could the plan reach every must-return fact? it's the recall ceiling); **isolation violations = 0** (hard guardrail); modality fit; share of keyword terms found in the Memory Bank Index; context-starvation rate |
| **3. Retrieval & ranking** | **Recall@K** (most important); precision@K; nDCG / MRR; stale-fact rate; duplicate rate; p95 latency and partial-failure rate |
| **4. Packaging** | **Critical-fact survival** after the trim; **distractor rate** (too many facts make the agent drop instructions); token budget adherence; schema validity |
| **5. Agent usage** (binary judge rubrics) | Exclusion honored; constraint respected; parameter applied; **no memory hallucination** (claims a preference not in memory); no over-personalization; live data wins over memory |
| **6. End to end** | Online A/B (conversion, basket size, turns); judge rates for misunderstood intent and irrelevant results; **fact ablation** (remove a fact, re-run; no change means it wasn't worth its tokens) |

### Write path

| Stage | Metric |
| --- | --- |
| Extraction | Precision (no junk like "getting this for a friend") and recall (didn't miss "family of four") |
| Durability classification | "Don't want ramen" transient in restaurants; "prefer Oatly" durable in grocery |
| Health block | Health facts saved = **0%** |
| Deduplication | Duplicate rate; contradictions resolved ("vegan now" replaces "vegetarian") |
| Forgetting | **Over-deletion** (also deleted "Nova Café weekly") and under-deletion (target survived) |

### Where each eval runs

| Where | What runs |
| --- | --- |
| **CI** (every change) | Stages 1–4 on the golden set; cheap and deterministic. Gate on recall@K and zero isolation violations |
| **Offline simulation** | Stage 5 rubrics on simulated sessions with planted-fact users |
| **Online** | Same rubrics on sampled production traces (offline and online share rubric and judge), plus A/B metrics |

**How to say it:**

> "I'd evaluate memory as a funnel: was the fact stored, requested, reachable by the plan, retrieved, kept after the trim, and used correctly? Each stage gets its own metric, so an end-to-end failure points to one stage. The backbone is a golden set of synthetic users with planted facts and tasks with must-return and must-not-return lists. Intent gets memory-kind recall; planning gets coverage and zero isolation violations; retrieval gets recall@K; packaging gets critical-fact survival and distractor rate; usage gets binary judge rubrics like 'exclusion honored' and 'no memory hallucination.' On top: end-to-end A/B, fact ablation, and write-path evals with health data and over-deletion held to zero."

---

## How to say it (about 60 seconds)

> "Agents never touch the store directly; memory is a tooling layer. The agent says what it needs in natural language, and the tools resolve which memories matter for that task, plan the query — semantic, keyword or direct fetch, with filters — retrieve in parallel, rank, and return a few structured facts with category, timestamp and durability. The agent reconciles them against live catalog data on the turn. On the write side, every turn fires a background extraction job with a policy gate: save stable explicit facts, skip passing moods, never save health data, and deduplicate against what we already know. Domain namespaces are isolated, but cross-vertical facts like household size are shared. The biggest lesson was exclusion: too many facts made the agent drop instructions, so retrieval has to be task-aware, not top-K."
