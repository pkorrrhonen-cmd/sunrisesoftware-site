# adr.sws.012: The typefaces are Familjen Grotesk and Public Sans

| | |
|---|---|
| Status | accepted (Petri, 18.9.2026: "4 is the only serious option; easy to read and neutral, it fits this well") |
| Date | 2026-09-18 |
| Decided by | Petri Korhonen |
| Links | sws.site |
| Supersedes | SEED v2.0.0 §3.1 (Fraunces + Inter + JetBrains Mono) |

## Context

Fraunces, the display serif of V4.5, is the ornate serif every LLM-made site now carries
(adr.sws.010). The type round (`docs/mockups/type-1.html`, six pairs on the identical Flow 2 hero
and section in the same light) put a calm editorial serif, a condensed serif, a characterful
grotesque, a Nordic grotesque, a high-contrast display serif and a warm slab-leaning serif side by
side. Petri read the sheets and chose pair 4 as the only serious candidate: easy to read and
neutral, and it fits the sunrise.

## Decision

- **Display** (headlines, product names, the creed): Familjen Grotesk, weight 400, tight tracking
  (about -0.03 em), no italics; emphasis by colour (`--sun-deep`) only.
- **Body** (paragraphs, UI, nav, buttons): Public Sans 300 to 600.
- **Labels** (section marks, years, statuses, specs, meta row): JetBrains Mono stays for the
  archival rhythm unless Petri says otherwise after seeing both in the mockup switcher
  (`labels=mono` vs `labels=sans`). Default in Flow 2: mono.
- Both from Google Fonts, as the family's other sites; self-hosting is decided with the page
  assets if the performance budget asks for it.

## Consequences

The design system for SEED v3.0.0 is now complete on colour, motion and type. The copy overhaul
starts on this pair. Flow 2 is updated to it; type-1.html stays as the record of the choice.
