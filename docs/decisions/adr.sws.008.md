# adr.sws.008: The React migration leaves the roadmap

| | |
|---|---|
| Status | proposed (Petri decides) |
| Date | 2026-09-17 |
| Proposed by | Claude Code, session 1 |
| Links | sws.site, sws.deployment |
| Would supersede | SEED v2.0.0 §5.1, §5.5 and §10 (Vite + React 19 build) |

## Context

SEED v2.0.0 declared the design "ready for Vite + React build" on 18.4.2026 and made the
year-range fix conditional on that build. Five months later the static page is still the
product, the fix waited with it, and the revision that is actually needed (content) does not
need a framework. Every other system in the family carries its own build because it has an
application behind it; this page has none.

## Decision (proposed)

The Vite + React migration leaves the roadmap. The single static file stays the deliverable,
and content is not extracted into modules. The question is reopened only if the page gains a
second page, a second language, or dynamic content.

## Consequences

SEED v2.1.0 §5 describes the static stack as the stack, not as an interim. adr.sws.001's
consequence clause ("a migration only if complexity warrants it") stands as the rule. A queued
fix is never tied to a future phase again (LESSONS 17.9.2026).
