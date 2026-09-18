# adr.sws.009: Documentation follows the family standard

| | |
|---|---|
| Status | accepted |
| Date | 2026-09-17 |
| Decided by | Petri Korhonen (instruction: documentation to the level of Atlas and Luviamo) |
| Links | sws.site, sws.deployment |

## Context

The repo had a README, one SEED and an archive folder. Atlas, Luviamo and the newer repos
(ReviewGlass, Ultra Gravel, Kalastus) carry a README with a dated status, a session CHANGELOG,
a machine-readable BUILD_INFO, LESSONS, decision records and a CLAUDE.md, and CI as the gate.
Atlas already held two decisions for this site that the repo itself did not.

## Decision

`docs/` gains `CHANGELOG.md`, `BUILD_INFO.json`, `LESSONS.md` and `decisions/` (one file per
decision in the Atlas record shape, ids `adr.sws.NNN` continuing Atlas's numbering). The root
gains `CLAUDE.md` and a CI workflow that runs a dependency-free check script
(`scripts/check-site.mjs`). The SEED stays the design and content spec, versioned by file.
Atlas's model of `sw-sivusto` is mirrored from these files, never the other way round, and the
mirror moves through the proposals channel. The page itself is edited only together with
Petri, after planning is concluded; documentation and the plan are the session's own work.

## Consequences

A session on this repo ends by updating CHANGELOG, BUILD_INFO, the footer date and, when a
decision was made, a decision file. A few minutes per session; the payoff is that April to
September cannot pass unnoticed again.
