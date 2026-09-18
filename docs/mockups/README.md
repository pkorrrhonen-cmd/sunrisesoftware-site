# Mockups

Separate HTML files, never the live page. Each round is looked at together (browser pane at
desktop and phone width, and the PNGs next to the files) before anything is decided; the
decisions then go to `docs/decisions/` and the accepted look to the SEED.

| Round | Files | Question | Brief |
|---|---|---|---|
| Flow 4, app view (18.9.2026) | `flow-4.html` (served: `http://localhost:8765/docs/mockups/flow-4.html`), `flow-4-desktop.png`, `flow-4-phone.png`, `media/masterforge-eq.mp4`, `media/salpa-defence-*.svg`, `shots/ultragravel*.png` | Flow 3 with the decided app views (`docs/design/apps-v3.md`): MasterForge's real EQ capture on loop, Luviamo's video with click-to-sound, the Somnus rack panel, the Atlas workspace board, Visit pills; drawers with real captures only (Ultra Gravel's planned loop from Petri), Salpa's brand mark with ACCESS DENIED on hover, a ReviewGlass interface mockup, SpectralForge's screenshot; the cryo strip reordered | `docs/design/apps-v3.md` |
| Flow 3, copy check (18.9.2026) | `flow-3.html` (served: `http://localhost:8765/docs/mockups/flow-3.html`), `flow-3-desktop.png`, `flow-3-phone.png` | Flow 2 with the decided copy from `docs/design/copy-v3.md` and the decided structure: §02 in two groups (Commercial products: MasterForge, Luviamo; Tools and research instruments: Somnus, Atlas), Quaesitor gone, §03 seven rows, SF3D as a claim, rewritten rules, "Let's talk." Plates and images are still placeholders for the app-view round | `docs/design/copy-v3.md` |
| Type 1, type round (18.9.2026) | `type-1.html` (served; a strip at the top switches the pair and the label style, keys 1 to 6 and m; `?pair=N&labels=mono` opens one), `type-1-pair1..6.png`, `type-1-sheet.png` (heroes), `type-1-sheet-sections.png` (sections) | six typeface pairs on the Flow 2 hero and one section, same light, placeholder copy: Newsreader + Albert Sans, Instrument Serif + Sans, Bricolage Grotesque + Figtree, Familjen Grotesk + Public Sans, Gloock + Golos Text, Young Serif + Onest; labels in mono or in the body sans | `docs/design/look-2026-09.md`, section "Type round" |
| Flow 2, round 3 (18.9.2026) | `flow-2.html` (served: `http://localhost:8765/docs/mockups/flow-2.html`; `?static=1` for captures), `flow-2-desktop.png`, `flow-2-phone.png`, `media/luviamo-poster.jpg` | Petri's answers to Flow 1 applied: tighter, portrait top faded, the reading light that follows the section you read, previews twice the size parked beside a plus that grows as the pointer nears, a lighter shore, the overclocking behind a cryo-chamber button, living product plates (canvas sketches, Luviamo's real intro video) | `docs/design/look-2026-09.md`, section "Round 3" |
| Flow 1, round 2 (17.9.2026) | `flow-1.html` (open it served, e.g. `python -m http.server 8765` then `http://localhost:8765/docs/mockups/flow-1.html`; `?static=1` for captures), `flow-1-desktop.png`, `flow-1-phone.png`, `shots/*.png` (live product sites for the drawers) | elements, motion and flow on the whole page in palette A′: moving glow and cursor light, feathered portrait, the nav sun rising with scroll, word reveals, parallax plates, a living Atlas plate, cabinet drawers (hover pulls, click opens, drag the strip), the SF3D film strip, rules and the creed, the page dissolving into the sea. Placeholder type (DM Sans) and copy on purpose | `docs/design/look-2026-09.md`, section "Round 2" |
| Look 1 (17.9.2026) | `look-A-ensisade`, `look-B-lampo-kasvoilla`, `look-C-aamu-usva` (`.html`, `-desktop.png`, `-phone.png`) | which morning: three palettes of the sunrise-over-the-sea direction on one identical screen, placeholder copy | `docs/design/look-2026-09.md` |

Screenshots: `python docs/mockups/shoot.py url <url> <png> [w h]` or `... file <html> <png> [w h] [query]`; a headless Edge returns before it writes the file, so the script waits for the file (a run that deletes the profile too early loses the image).

Regenerate a round from its script (the template lives in the script so the variants stay
identical apart from their tokens):

```
python docs/mockups/build-look.py --shots
```

`docs/` is served by Cloudflare Pages with the rest of the repo root, so a merged mockup is
reachable by URL (robots keeps it out of search once `robots.txt` lands). Keep nothing here that
may not be public.
