# Wiped my company's production DB last week.

**Source:** r/ExperiencedDevs · [original thread](https://www.reddit.com/r/ExperiencedDevs/comments/1j2wrdv/wiped_my_companys_production_db_last_week/)  
**Rank:** #40 of 100 by position in Reddit's top listings  
**Comments captured:** 40

## The situation

Eight years' experience, at a big company that had acquired a small successful product lacking any staff tooling — support requests were routinely handled by running SQL directly against production. Woken on-call for an 'urgent' product code update before a demo, the poster ran the familiar UPDATE statement without its WHERE clause, applying one user's codes to every user.

## What the community advised

- The EM's response is the centrepiece: they attributed it to missing tooling rather than the individual, and immediately allocated time to build the first version of staff tools.
- 'The question should never be who fucked up. It should be why were you able to fuck up, and how do we prevent it.'
- Commenters called this the best possible outcome and noted every alternative — data loss, firings, blame — would have been worse.
- 'Any process that enables and provides for human error will INEVITABLY result in human error.'

## Dissent / counterpoints

- A sharper critique: the entire process was broken well before the incident, and the poster's heroics may let the people responsible for that continue ignoring it.
- A recognisable adjacent pattern — PMs tapping developers for 'one small change' for an 'urgent customer' while ignoring proposals for internal tooling because it doesn't move their numbers.

## For your prep

The single best incident-response case in the dataset, and directly usable for *'tell me about a time someone on your team made a serious mistake.'* The reusable structure: absorb the blame publicly, fix the system immediately, and convert the incident into the tooling budget you couldn't get before. That last move — using an incident as leverage for the investment — is the senior beat most candidates miss. Pairs with S2.
