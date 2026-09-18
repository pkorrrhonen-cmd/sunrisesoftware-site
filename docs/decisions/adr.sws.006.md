# adr.sws.006: The employer's applications are withheld until permission

| | |
|---|---|
| Status | accepted |
| Date | 2026-09-17 |
| Decided by | Petri Korhonen |
| Links | sws.site |

## Context

Some applications Petri has built belong to his employer's sphere. Showing them on a Sunrise
Software page needs that company's agreement, which has not been asked. V4.5 listed two of them.

## Decision

None of the employer's applications, workspaces or names appear on the page until Petri has
agreed it with the employer. The check script carries the name as a forbidden string across the
whole of `index.html` (body, script and head), so it cannot return by accident.

## Consequences

The clinical discipline in §01 stays: it is Petri's own. When permission arrives, the forbidden
string is removed, the rows return, and this decision is superseded by the one that records the
permission and its scope.
