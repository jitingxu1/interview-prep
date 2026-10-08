# Today I announced that I won't be reviewing AI generated PRs at company meeting

**Source:** r/ExperiencedDevs · [original thread](https://www.reddit.com/r/ExperiencedDevs/comments/1towli9/today_i_announced_that_i_wont_be_reviewing_ai/)  
**Rank:** #60 of 100 by position in Reddit's top listings  
**Comments captured:** 40

## The situation

A web developer was reviewing PRs from data scientists using Claude Code to make changes to a Rails/Vue web service. They decided to stop, reasoning that AI-generated code looks plausible and reviewers therefore miss issues, leading to bugs and security problems. They announced it at a company-wide meeting and got significant support, including from leadership.

## What the community advised

- The reframing that dominated: the problem is not AI, it is submitting code you don't understand. 'No one should be raising PRs they don't understand — whether it was written by AI or not.'
- Reviewing is itself an act of ownership — several described approving a PR as taking partial responsibility for it existing in the codebase.
- One company encodes this in policy: you accept 51% ownership of any code you approve.
- A useful tactic: ask a question even when the code is fine, to surface 'that's the AI's code, not mine' early and set expectations.

## Dissent / counterpoints

- Some noted 'because Copilot' can be a legitimate answer for genuinely arbitrary choices like undefined style conventions — the objection is to using it for substantive logic.
- Others pointed out this is really a cross-team boundary problem: data scientists shipping to a web service they don't own.

## For your prep

Highly relevant to both your target roles. This is a live policy question you may be asked directly: *what's your position on AI-generated code in review?* The defensible answer isn't a ban — it's an authorship standard ('you must be able to defend and modify anything you submit') plus attention to who bears the review cost. Your DS-to-production experience makes the cross-team version of this credible for you.
