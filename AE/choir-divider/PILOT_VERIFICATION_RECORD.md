# Choir Divider — Pilot Verification Record

Complete one record for the instructor build and one after the first learner delivery. Attach redacted photos/diagrams and measurement notes. Do not promote readiness from an incomplete or desk-only record.

## Build identity

- Date / site:
- Facilitator / verifier:
- Platform and power source:
- CD4017 marking/variant:
- NE555 marking/variant or external clock:
- CD40106 marking/variant, if used:
- Patch destination modules:
- Local substitutions:

## Bench proof

| Check | Measurement or observation | Pass / revise |
| --- | --- | --- |
| Rail polarity and measured voltage |  |  |
| Power at every populated IC |  |  |
| Decoupling installed at each IC |  |  |
| External/internal clock visible |  |  |
| Q0–Q9 advance in order |  |  |
| Q3 reset gives Q0–Q2 cycle |  |  |
| Q4 reset gives Q0–Q3 cycle |  |  |
| Q5 reset gives Q0–Q4 cycle |  |  |
| PATTERN returns low and triggers correctly |  |  |
| Three outputs work at intended destination |  |  |
| Power-down/change/repower routine works |  |  |

Unexpected heat, voltage, output, damaged part, or unsafe behavior: ______________

## Delivery evidence

- Learners / pairs:
- Actual Session 1 time by stage:
- Actual Session 2 time by stage:
- Parts consumed or failed:
- Longest queue/bottleneck:
- Most common wiring error:
- Most useful recovery move:
- Plain-language terms that needed revision:
- Access/participation routes used:
- Did every team reach the minimum external-clock build? Why/why not?
- Did optional stages displace required evidence? Why/why not?

## Readiness decision

- [ ] Keep `PILOT`: verification or first-run evidence is incomplete.
- [ ] Revise and rerun: list required changes below.
- [ ] Candidate for `GO-P`: exact build is proven, timing/quantities are confirmed, safety/recovery worked, and all repository changes are recorded.

Required documentation, parts, timing, or safety changes:

______________________________________________________________________________

Verifier signature/date: ______________________________________________________
