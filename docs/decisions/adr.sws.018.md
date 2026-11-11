# adr.sws.018: the site gains pages, and the front page keeps the short version

| | |
|---|---|
| Status | accepted (Petri, 11.11.2026: "lyhyet jutut etusivulla, esiteltävät asiat omilla sivullaan") |
| Date | 2026-11-11 |
| Decided by | Petri Korhonen |
| Links | sws.site, sf3d-ai-lab, atlas, reviewglass, hometeam |

## Context

The page had nowhere to put an event. Two hackathon results arrived in two months, Since AI
2026 in Turku (Silent context, third of fifteen in Elisa's challenge, 8.11.2026, the repository
public) and the AMD Developer Hackathon ACT III in October, and neither fits a product plate or
a drawer. The deeper subjects have the same problem in the other direction: the Atlas decision
rooms and ReviewGlass need more than a drawer's paragraph, and the rooms already have a video
and four published articles at sf3d.fi.

The one-page architecture of SEED v3.0.0 answered a different question: in September the task
was one glance that explains the work. A subject that takes two minutes to understand has no
room in a glance, and burying it on the front page would cost the glance.

The lab had already decided the form for this: `adr.sf3d.010`, a video leads each topic and the
article page is its evidence, and the site plays its own file with no third-party player.

## Decision

The site becomes several static pages. The front page keeps the short version of everything and
each subject worth presenting gets its own address: `/rooms/`, `/reviewglass/`,
`/silent-context/`, `/hometeam/`, each one an `index.html` in its own directory with the same
frame, the same design system, and a button back to the front page in the nav and at the foot.
No build step, no framework, no shared template file (adr.sws.001, adr.sws.008 hold).

The front page gains a dated section `§04 Recent` between §03 and the SF3D chamber, holding at
most five entries newest first, each with its date, two sentences, and a link to its page where
there is one. Approach and Correspondence renumber to §05 and §06, and the nav gains `Recent`
between Products and Approach. HomeTeam joins §03 as its eighth drawer.

The rooms page tells the Atlas room system with the names the field uses, taken from Atlas
`ATLAS-HUONEET-KAR-ARV-20261031` v1: multi-agent debate, model heterogeneity, blind sealed
first votes, devil's advocate and dialectical inquiry, LLM-as-a-judge and judge calibration,
pre-registration, maximin, sycophancy and conformity. The word Delphi does not go on the page
until a source for it is recorded in the SEED, although the structure is that method's shape.

Video is copied into this site's own `media/` and played from here, and the long writing stays
where it was published: the rooms page links the sf3d.fi articles rather than repeating them.

The spec is SEED v4.0.0. Nothing is built alone: the page round and each sub-page is a pull
request made together with Petri (CLAUDE.md), after its copy has been decided item by item in
`docs/design/copy-v4-pages.md`.

## Consequences

The frame now lives in five files rather than one, so a change to the nav or the shore is five
edits. `scripts/check-site.mjs` grows to run its checks over every page and to require that the
sitemap names each one; that script, not a template, is what keeps the copies honest. The cost
is accepted because the alternative, a build step, was already refused twice (adr.sws.001,
adr.sws.008) for a site this size.

Each page is its own crawlable address with its own title, description and structured data,
which is most of what the status review wanted from the SEO and GEO side.

Media weight stays off the front page: a clip lives on the page that is about it, with
`preload="none"` and controls rather than autoplay.

The site now has more places where a fact can go stale. The rule stands and extends to every
page: a status carries a date, never a version (adr.sws.004, adr.sws.015), and a claim about
another project is checked from that project's repository or its live service in the same
session.
