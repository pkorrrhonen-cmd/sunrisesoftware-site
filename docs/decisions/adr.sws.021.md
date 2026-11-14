# adr.sws.021: ReviewGlass is shown by its own windows over a staged screen

| | |
|---|---|
| Status | accepted (Petri, 14.11.2026, round AE in `docs/design/copy-v4-pages.md`) |
| Date | 2026-11-14 |
| Decided by | Petri Korhonen |
| Amends | the rule on drawn instruments (CLAUDE.md, "Rules for the page"; `docs/design/apps-v3.md` B.5); RG.8 and X.1 of 13.11.2026 (the drawing as `/reviewglass/`'s lead medium) |
| Links | sws.site; ReviewGlass adr.rg.025 (the glass excludes itself from capture) |

## Context

Since 18.9.2026 ReviewGlass has been a drawing on the page: blurred text columns, a reading frame
and a glass (apps-v3 B.5), because a real screenshot would show Petri's code and conversation. On
13.11.2026 the drawing became `/reviewglass/`'s lead medium too (RG.8, X.1), with the caption
`A drawing, not a capture: ...`.

At the close of 13.11.2026 Petri set the line that real mockups replace the drawings, one product
at a time, and that ReviewGlass's has to be made some other way than a screen capture: the glass,
its halo and the finder exclude themselves from every capture (`WDA_EXCLUDEFROMCAPTURE`, ReviewGlass
adr.rg.025), so a screenshot shows the screen without them. Without the exclusion the glass would
show itself inside itself.

ReviewGlass's windows are SvelteKit pages that talk to a Rust core through Tauri's `invoke`. The
glass page asks the core for frames (`glass_frame`: the source pixels at 1:1) and zooms them on its
own canvas. Tauri's core can be stood in for in a browser, so the pages can run there with every
answer of the core staged. A trial on 14.11.2026 rendered the glass, the diff window, the halo and
the dock from ReviewGlass's `main` (`2654ab4`) this way, over a staged screen
(`docs/mockups/reviewglass/round-AE-method.jpg`).

## Decision

ReviewGlass's image on the site is its own windows, drawn by its own code with a staged core, laid
over a staged screen (AE.1):

- The glass, the diff window, the halo and the dock are ReviewGlass's own pages from its public
  `main`, run in Edge with `docs/mockups/reviewglass/tauri-mock.js` in place of the core. The
  glass's frames are cut from the staged screen around a staged pointer, at the real zoom, as the
  core cuts them from the real screen. `docs/mockups/reviewglass-mockup.py` makes the image and is
  run again when the interface changes.
- The screen the glass reads is a staged re-enactment (AE.2): two session panes whose text is
  written for the picture, telling a true story of this site (session 6, 11.11.2026: the version
  guard that never fired), with the real diff of its fix, commit `2aef4d2` of this public
  repository. No real conversation, no private code, no imitation of the Claude app's own look.
- The windows use Windows's light theme (AE.4). In the dark theme ReviewGlass draws the latest
  edit's rows with light text on its yellow mark (measured `#ececec` on `#fff1a8`); that is a
  ReviewGlass fix of its own, not the site's.
- The mockup replaces the drawing in both places (AE.3): `/reviewglass/`'s lead medium (RG.8) and
  the front page's §03 ReviewGlass drawer. Its caption and labels are a copy question (round AF);
  the page does not present the mockup as a capture.

The rule on drawn instruments now covers Somnus and Atlas only; each gets its own decision when its
turn comes.

## Consequences

The page shows what ReviewGlass looks like and does: the glass reading a pane at 200 %, the column
lock naming the pane, the diff window attached beside it with the latest edit marked, the dock with
the quota. Every pixel of ReviewGlass in the picture comes from its own code; only the core's
answers and the screen are staged, and the screen's code is real and public.

The cost is upkeep and a toolchain: the image is made from a copy of ReviewGlass's source and its
installed dependencies, with a dev server running, and it shows the interface of the commit it was
made from. The image names that commit in its build notes, and a session that changes it exports
ReviewGlass's `main` again. If ReviewGlass's core commands change shape, `tauri-mock.js` changes
with them; a page that fails to render stops the script rather than producing an empty window.

Staging is a claim of its own: the picture is a re-enactment, so the caption says so (round AF),
as `/hometeam/` says its screens are design mockups.
