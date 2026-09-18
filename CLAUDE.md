# CLAUDE.md: working practices for the Sunrise Software site

The company site at https://sunrisesoftware.app/ (repo `pkorrrhonen-cmd/sunrisesoftware-site`).
One static page, no build step. Read `README.md` for layout and deploy, and the current
`docs/SEED-v3.0.0.md` for the design system, with `docs/design/copy-v3.md` (every text) and
`docs/design/apps-v3.md` (every image), before editing copy or layout.

## Documents and where things go

| What | Where |
|---|---|
| Design system, page architecture, locked copy | `docs/SEED-vX.Y.Z.md` (versioned by file; superseded versions in `docs/archive/`) |
| What a session changed and why | `docs/CHANGELOG.md` (newest first, "Sessio N (pvm): aihe") |
| Machine-readable state and the open items | `docs/BUILD_INFO.json` (`next` is the only open-items list; a repo this small has no BACKLOG) |
| Decisions | `docs/decisions/adr.sws.NNN.md`, one file per decision, Atlas record shape |
| Mistakes and the rule each one produced | `docs/LESSONS.md` |
| Working practices | this file |

The same fact lives in one place; everywhere else is a reference. When CLAUDE.md and the SEED
disagree, CLAUDE.md wins on working practice and the SEED wins on the page.

## The page is edited together, not alone

`index.html` changes only together with Petri, as agreed, and after the planning for a
revision is concluded (Petri, 17.9.2026). A session may research, draft the SEED, write
decisions and documentation on its own; it does not edit the page, delete or add images, or
generate page assets on its own initiative. The plan for a revision lives in the SEED and the
open decisions in `BUILD_INFO.next`. Lists of decisions are taken through question boxes, about
four items a round, each with the current text and alternatives; a recommended option with new
wording is shown verbatim and marked as a proposal. The method, why it works and the seven-step
guide: `docs/design/decision-method.md` (Atlas artifact `SUNRISE-TYOTAPA-PAATOSLAATIKOT`).

## Rules for the page

The rules below hold once their decision is accepted; a `proposed` decision in
`docs/decisions/` is a rule only after Petri accepts it.

- Every status on the page carries a version or a date (adr.sws.004). No "coming soon",
  "recently", "within the month". The footer carries the revision date and CI fails when it
  differs from `BUILD_INFO.updated`.
- None of the employer's applications, workspaces or names on the page until Petri has cleared
  it with the employer (adr.sws.006). CI forbids the name across the whole of `index.html`.
- The SF3D history is a claim, a lead and a cryo chamber behind a button after §03 (SEED v3
  §3.4). It does not grow back into a full section. Ember (`#D96B3A`) appears only in its section
  mark; the chamber uses the cryo palette.
- On-site copy: English, first person singular, no em dashes (commas, colons, or restructure),
  no hero statistics, no generic adjectives. Author name Petri Korhonen. The company name
  appears only in the footer, the meta row and the structured data.
- Facts on the page come from the product repos (`BUILD_INFO.json`, `README.md`, the live
  site), checked in the session, never from memory. The CHANGELOG entry says what was checked.
- Images: WebP first with a JPG or PNG fallback under `images/`; source screenshots under
  `source-assets/`. Every image gets `loading="lazy"` (except above the fold) and an alt text
  that describes the screen, not the product.
- Product plates show the real product (a capture or clip); drawn instruments only where the
  product has no public surface: Somnus, Atlas, ReviewGlass (`docs/design/apps-v3.md`).
- Spec strips carry no technology names; the AMD mention is exactly "AMD R9700 sample program ·
  white paper in progress".

## Session routine

1. Start: `git fetch origin`, then `git rev-list --left-right --count origin/main...HEAD`. If
   main is ahead, branch from `origin/main`. Read the top CHANGELOG entry, `BUILD_INFO.json`
   and `LESSONS.md`.
2. Work on a branch, one PR, squash merge. Cloudflare Pages gives every branch a preview URL:
   look at it, at desktop and at phone width, before merging.
3. Verify: `node scripts/check-site.mjs` (CI runs the same script). `--links` also checks the
   external links, which CI does not do.
4. End: a CHANGELOG entry; `BUILD_INFO.json` (`version`, `updated`, `state`, `next`); the
   footer date; `LESSONS.md` if a mistake taught something; a decision file if a decision was
   made; the SEED if the spec changed. The session is not over before this list is done.
5. Atlas mirror: when the Atlas MCP is reachable, write `sw-sivusto.STATUS` with
   `atlas_put_status` (read first, merge, then write) and send decision changes to
   `model/systems/sw-sivusto.model.json` through the proposals channel. Truth hierarchy, as in
   every Sunrise repo since 29.7.2026: repo `main` is the document truth, Atlas is the mirror.

## Deliverable formatting

- Conversation and commit messages in Finnish; commit subject "Sessio N: aihe".
- Code, on-site copy, README, SEED and decision files in English; CHANGELOG and LESSONS in
  Finnish (family practice).
- Never use em dashes in documents or copy. Each shell command in its own code block.
