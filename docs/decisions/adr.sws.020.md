# adr.sws.020: HomeTeam's plates show its design mockups

| | |
|---|---|
| Status | accepted (Petri, 13.11.2026, round Y in `docs/design/copy-v4-pages.md`) |
| Date | 2026-11-13 |
| Decided by | Petri Korhonen |
| Amends | the rule on drawn instruments (CLAUDE.md, "Rules for the page"; `docs/design/apps-v3.md` B.6b; copy-v4-pages 3.46 and B.3 of 11.11.2026) |
| Links | sws.site |

## Context

The page shows the real product: a capture or a clip. Where a product has no public surface, the
page draws an instrument instead. On 11.11.2026 HomeTeam got a drawing (B.3) for two reasons: the
application runs behind a list of allowed addresses, so nothing public can be captured, and a
capture of production would carry the family's own data.

At the close of 13.11.2026 Petri set a new line: real mockups of the applications onto the pages,
in place of the drawn instruments, decided one product at a time. HomeTeam is the first. Its
repository holds 21 mockups (`hometeam/mockups/`), one page each, made with the family before each
feature was built; the option Petri chose in each is what the application was built from. They
carry no production data. Some of them carry real names.

## Decision

HomeTeam's images on the site are screens cut from its design mockups, the chosen option of each:

- `/hometeam/` leads with the child's and the adult's Today side by side and shows Wallet, the
  weekly scoreboard and the treasure island after the body (Y.1).
- The front page's HomeTeam drawer shows the child's Today in place of its drawing (Y.4).
- The screens stay in Finnish, as the application is, with an English caption (Y.2).
- No child's name and no family surname appears in a screen or in any file in this repository: the
  copy that is captured swaps them for the mockups' own nicknames, outside the repository.
  `Hei, Petri!` may stay (Y.3).
- The page does not present a mockup as a capture of production; how it says so is a copy question
  (round Z).

The rule on drawn instruments keeps its other products for now: Somnus, Atlas and ReviewGlass each
get their own decision when their turn comes, and ReviewGlass's cannot be a plain screen capture
(the glass excludes itself from capture, ReviewGlass adr.rg.025).

## Consequences

HomeTeam's plates look like the application instead of a sketch of it, and nothing on them needs
keeping up as the family's data changes. The cost is drift: a mockup is the plan, and the shipped
screen may move on (mood moved behind the settings on 8.10.2026, hometeam PR #35). A screen is
chosen only where the chosen option was built, and the session that changes a HomeTeam image reads
the hometeam repository's `mockups/README.md` and CHANGELOG first.

The names rule is the strictest part: the site's repository is public, so a capture with a name in
it is a leak the moment it is committed, not only when it is published. The capture is made from a
copy outside the repository, and the commit is checked for the names before it is made.
