# adr.sws.015: no product version numbers on the page; a status carries a date

| | |
|---|---|
| Status | accepted (Petri, 20.9.2026: "nyt on jo 0.388 menossa eli kun nuo ei päivity muuta kuin manuaalisesti niin ne on poistettava") |
| Date | 2026-09-20 |
| Decided by | Petri Korhonen |
| Links | sws.site |
| Amends | adr.sws.004 (a status carried "a version or a date"; from now on a date) |

## Context

Two days after the V5 launch the page said Luviamo `v0.385` while production was at 0.388.
Product versions change several times a week across the family and the page has no build
step and no feed from the product repos; every version on it is typed by hand and is stale
the day after. adr.sws.004 allowed "a version or a date" because the April page had carried
versions; the version half of that rule is the part that cannot be kept true by hand.

## Decision

No product version numbers on the page: not in status lines, not in the hero meta row, not in
the drawn instruments' card data. A status carries a date (the year the product went live,
`2026 →`, or a dated event in the body copy, "in September 2026 its free tier was rebuilt").
The hero meta cell "Latest release" is replaced by "Email", a fact that does not age.
`scripts/check-site.mjs` fails on `v1.2`-shaped strings and on "<product> 1.2" anywhere in
`index.html`.

## Consequences

The page stops competing with the product repos on a fact only they can keep. Dated facts
stay: they are history and remain true. The session routine still checks the product states
(live, closed beta, pre-alpha) against the repos; the numbers are no longer its concern. If a
version ever belongs on the page again, it comes through one source and a check
(adr.sws.014), not by hand.
