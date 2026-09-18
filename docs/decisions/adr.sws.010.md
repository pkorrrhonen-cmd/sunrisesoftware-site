# adr.sws.010: The look is the sunrise over the sea, palette A shifted a little toward C

| | |
|---|---|
| Status | accepted (Petri, 17.9.2026, from look round 1) |
| Date | 2026-09-17 |
| Decided by | Petri Korhonen |
| Links | sws.site |
| Supersedes | the visual direction of SEED v2.0.0 (cabinet dark); the design system moves to SEED v3.0.0 |

## Context

The cabinet-dark theme of V4.5 has become the default look of AI-made sites in 2026. Luviamo's
branding is the family's best and does not read as a language-model product: a light base, one
warm accent, the birch forest carried as atmosphere rather than pictures. Look round 1
(`docs/mockups/look-A/B/C`, `docs/design/look-2026-09.md`) put three sunrise palettes on one
identical screen.

## Decision

- **Direction**: warm paper, the sunrise over the sea as atmosphere. A change of direction, so
  the design system is written as SEED v3.0.0 once round 2 is accepted.
- **Palette**: A (Ensisäde) with a few percent of warmth taken out towards C. Tokens in the
  brief under "A′".
- **Hero**: the glow moves slowly. The portrait stays in the hero, its edges fade into the page.
- **Footer**: a seamless transition into the sea, never a sharp box.
- **Motion and elements**: more of it, on purpose: galleries pulled out with the mouse, parallax,
  animation and flow. The page must carry the feeling that it was not thrown together in an hour
  but conveys the whole ideology: imagination is the limit, build and enjoy the world.
- **Order of work**: colour (done) → elements, motion and flow (round 2) → typefaces and texts,
  with the content designed alongside. This takes longer than the April revision and that is
  intended.

## Open, decided later in their own rounds

- **Typeface**: Fraunces is rejected as the ornate serif every LLM-made site now carries. The
  typeface round looks for one that fits the sunrise and separates the page from the generic.
  Round 2 uses a neutral placeholder (DM Sans everywhere) so that motion is judged, not letters.
- **Mono labels**: looked at with the typefaces.
- **SF3D shape**: adr.sws.003 stays open; round 2 shows one alternative in the new look as a
  placeholder placement.

## Consequences

adr.sws.002's editorial structure (numbered sections, archive rows, first person, restraint)
survives; its palette and its italic-serif signature do not. Ember stays reserved for SF3D.
