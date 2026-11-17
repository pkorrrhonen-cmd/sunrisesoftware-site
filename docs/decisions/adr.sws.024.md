# adr.sws.024: Small text on the page passes WCAG AA contrast

| | |
|---|---|
| Status | accepted (Petri, 17.11.2026, session 13, round AU, decision boxes) |
| Date | 2026-11-17 |
| Decided by | Petri Korhonen |
| Links | sws.site; amends adr.sws.010 (palette A′); SEED v4.1.0 section 4 |

## Context

The live checks of 15.11.2026 (Lighthouse 13.6.0) flagged colour contrast on every page. A scan of the
front page's text against its real backgrounds on 17.11.2026 found two tokens of palette A′ under WCAG AA's
4.5:1 for text under 24 px (18.66 px bold):

- `--text-meta` #8B96A0: 2.81:1 on `--base` #F9F7F1, on about 30 texts (the hero's meta labels, §03's years,
  the group labels, the sub-pages' captions).
- `--sun-deep` #C57A2C: 3.16:1 on `--base`, on about 34 texts: the product tags (17 px), the warm clauses of
  §01 and the rules, §03's links, the kicker, the section marks and the method's labels. Lighthouse listed only
  the section marks.

The large display text (the hero's coloured clause, the creed) passes at 3:1 and is not affected.

## Decision

1. `--text-meta` is **#66717B**, the same blue grey darker: 4.65:1 on `--base`, 4.91:1 on `--paper`.
2. A text shade of the sun, **`--sun-ink` #9E5F1E** (4.77:1 on `--base`), is used for the sun's colour on text
   under 24 px. `--sun-deep` #C57A2C stays for the coloured clause of display text 24 px and over, for lines
   (the kicker's rule, the drawer links' underline), marks and the plus. The "sound on" note over the dark
   MasterForge video keeps `--sun-deep`, where the darker shade would lose contrast.

Comparison images shown with the question: `docs/mockups/contrast/round-AU-*-now-left-proposal-right.jpg`.

## Consequences

- All five pages and `404.html` carry both tokens; every text rule that used `--sun-deep` under 24 px uses
  `--sun-ink`. Lighthouse accessibility measured 100 on the five pages locally after the change (94 to 95
  before).
- A new rule that colours text with the sun picks `--sun-ink` unless the text is display size.
- The canvas sketches' own colour constants (`SUN_D`) are drawings, not text, and are unchanged.
