# Reddit Manager Threads

100 of the highest-ranked threads from five management and engineering-leadership
subreddits, summarised and grouped by topic. Built to increase exposure to the
situations managers actually face — and how experienced managers argue about them.

Each thread note has four parts: **the situation**, **what the community advised**,
**dissent/counterpoints**, and **for your prep** (how it connects to your question
bank and STAR stories).

---

## Topics

| Folder | Threads | What's in it |
|---|---|---|
| [ai-and-engineering-culture](./ai-and-engineering-culture/) | 17 | AI mandates, code review ownership, the juniors pipeline |
| [remote-work-and-trust](./remote-work-and-trust/) | 11 | Monitoring, PTO, flexibility, overemployment |
| [retaining-top-performers](./retaining-top-performers/) | 10 | Why strong people leave and the levers you have |
| [managing-up-and-org-politics](./managing-up-and-org-politics/) | 10 | Influencing upward, dysfunction, visibility |
| [burnout-and-wellbeing](./burnout-and-wellbeing/) | 8 | Spotting burnout, manager burnout, hard human moments |
| [crisis-and-judgment-calls](./crisis-and-judgment-calls/) | 7 | Incidents, blameless postmortems, judgment under pressure |
| [feedback-and-communication](./feedback-and-communication/) | 7 | Delivering feedback, the euphemism problem, listening |
| [hiring-and-references](./hiring-and-references/) | 7 | Hiring from the manager's side, reference ethics |
| [team-culture-and-recognition](./team-culture-and-recognition/) | 7 | Rituals, recognition, alumni, incentive design |
| [performance-management](./performance-management/) | 6 | PIPs, terminations, accountability, calibration |
| [career-transitions](./career-transitions/) | 5 | IC→manager, manager→director, staying too long |
| [delegation-and-scaling-yourself](./delegation-and-scaling-yourself/) | 5 | Letting go, strategic thinking, learned helplessness |

## Start here

If you read only six, read these:

1. [CFO's $180k saving was actually a $400k loss](./managing-up-and-org-politics/cfo-wanted-to-outsource-support-for-180k-savings-i-did-the.md) — the best template in the set for influencing above your level.
2. [Wiped the production database](./crisis-and-judgment-calls/wiped-my-company-s-production-db-last-week.md) — model blameless postmortem, and the EM's move of converting an incident into tooling budget.
3. [Team penalised for not performing panic](./burnout-and-wellbeing/upper-management-is-penalizing-my-team-because-we-do-not-w.md) — the invisibility of prevention, a genuine senior-manager problem.
4. [Rewarding the best person with more work](./retaining-top-performers/realized-i-was-managing-my-top-performer-wrong-i-kept-givi.md) — the most common retention failure, stated plainly.
5. [Won't review AI-generated PRs](./ai-and-engineering-culture/today-i-announced-that-i-won-t-be-reviewing-ai-generated-p.md) — a live policy question for AI-org interviews.
6. [What I wish I'd known as a new manager](./delegation-and-scaling-yourself/ok-real-talk-shit-i-wish-i-knew-when-i-first-became-a-mana.md) — the richest single thread on 1:1s.

## Cross-cutting patterns

Themes that recurred across unrelated subreddits, which is the strongest signal in the data:

- **Delay is the root failure in performance management.** Nearly every bad outcome traces to a problem named months too late.
- **Prevention is invisible; firefighting is rewarded.** Appears in at least four threads from four different angles. Making absorbed chaos legible upward is a real skill, not self-promotion.
- **"Read between the lines" management is universally condemned.** Vagueness intended as kindness is received as cowardice.
- **Rewarding your best person with more work is the most common way to lose them.**
- **The best-regarded managers talk least.** Three independent threads; short naive questions beat having answers.
- **Behaviour problems get blamed on generations, and get corrected every time.** Counter-examples always arrive from every age bracket.
- **"If you submit it, you own it."** The AI authorship standard is settled among experienced engineers, even where their employers' mandates aren't.

---

## How this was built

**Source:** r/managers, r/AskManagers, r/leadership, r/ExperiencedDevs, and
(intended) r/ExperiencedManagers — 1,200 posts pooled from `top/all`, `top/year`,
`top/month` and `hot` listings, with the best 100 selected and their comment
threads fetched. 3,877 comments captured, ~39 per thread.

Raw data is in [`_raw/`](./_raw/): `posts.json` (full pool), `selected.json` (the
chosen 100), `threads.json` (posts + comments), and `crawl.py` (the crawler).

### Four caveats that affect how you should read this

**1. "Highest valued" means most upvoted, not most useful.** Reddit's RSS feed
exposes no score, so rank here is *position within Reddit's own top listings*.
Upvotes measure resonance and entertainment, not instructional value. Roughly a
dozen of the 100 are jokes, venting, or viral stories with little management
content — [#63](./career-transitions/life-s-taught-me-control-your-emotions-pick-the-right-batt.md)
is the clearest example, where the entire comment section is song lyrics. They're
included because you asked for the top 100; the notes say plainly when a thread is
thin.

**2. r/ExperiencedManagers is missing entirely.** Three of its four listings
returned zero results during the crawl, and my code couldn't distinguish a failed
fetch from an empty subreddit. Only its `top/year` listing succeeded, which carries
a rank penalty in the weighting — so all 25 of its posts were mathematically
excluded before content mattered. I attempted a re-fetch; Reddit had put this IP in
a rate-limit penalty box (sustained 429s and login redirects) and it never
completed. **The gap is unresolved, and it is a crawler artifact rather than a
finding about that subreddit.** Re-running `_raw/crawl.py` from a fresh IP, or with
API credentials, would close it.

**3. Non-tech subreddits dominate the people-management half.** r/managers and
r/AskManagers skew heavily toward retail, healthcare and hospitality. The human
dynamics transfer well; the specifics (shift scheduling, dress codes, attendance
points) often don't. r/ExperiencedDevs carries nearly all the engineering-specific
material.

**4. A meaningful share of top leadership posts are AI-generated.** Commenters
flagged this repeatedly, sometimes convincingly — see
[#59](./team-culture-and-recognition/the-manager-s-guide-to-spotting-burnout-before-it-s-too-la.md)
and [#15](./delegation-and-scaling-yourself/i-handed-off-a-project-to-a-new-hire-and-what-happened-nex.md).
In several threads the practitioner knowledge is in the comments while the post
itself is content marketing. The notes flag this where it applies.

### Sampling note

These are *top-of-all-time and top-of-year* threads, so they over-represent dramatic
and extreme situations. Routine management — the ordinary 1:1, the unremarkable
quarter — doesn't get upvoted. Read this as a catalogue of edge cases and failure
modes, not as a description of the median day.
