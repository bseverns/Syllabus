# Week 06 — Serial protocol as a contract

## Goals
- Distinguish message framing, fields, values, acknowledgment, and errors.
- Send bounded commands without blocking the device loop.
- Document a protocol another person can implement.

## Session arc (165 minutes)

1. Diagnose ambiguous example messages (15 min).
2. Model newline framing and the `COMMAND / ACK / ERR / DATA` contract (25 min).
3. Flash `week06_serial_protocol`; test `PING`, `GET`, `LED`, and `RATE` (35 min).
4. Record valid and invalid exchanges (20 min).
5. Break and device reset (10 min).
6. Design one additional paper-level command before changing code (20 min).
7. Pair test: one team uses only the other's protocol document (25 min).
8. Revise contract, save transcript, and reflect (15 min).

## Minimum evidence

A protocol table, successful request/response transcript, rejected invalid command, and safe bounded parameter behavior.

## Recovery

Use a saved Serial transcript and role-play parser/device responses if ports or uploads fail.

## Links
- Firmware: `firmware/week06_serial_protocol/`
- Lab: `labs/week06_protocol_design.ipynb`
- HW: `assignments/hw06_protocol.md`
