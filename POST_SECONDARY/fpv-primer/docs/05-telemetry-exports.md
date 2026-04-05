# Telemetry exports and capture

For this primer, telemetry capture is not an optional extra. It is how you turn “I think the rig did this” into something inspectable.

## What counts as telemetry here?

Depending on the rig and workflow, telemetry may include:

- receiver-linked values visible in Betaflight
- OSD-observable state such as voltage or timer
- blackbox logs
- serial streams consumed by another tool
- captured values replayed into a parser, mapping patch, or monitor

On a whoop-class baseline such as an Air65 with ELRS, the most realistic teaching path is often:

1. verify receiver and OSD values in Betaflight
2. record blackbox or other available flight-state data if supported
3. capture a short replayable dataset
4. route one signal into a downstream tool

## Minimum viable capture workflow

### Option A: Betaflight + screenshots + notes

Use when:

- the FC is limited
- storage is limited
- the teaching goal is systems understanding more than tuning depth

Artifacts:

- screenshots of key tabs
- written observed ranges
- short flight or bench log

### Option B: Blackbox capture

Use when:

- the FC supports dataflash, SD, or serial blackbox logging
- you want repeatable post-flight analysis

Artifacts:

- log file
- note of logging mode and rate
- export or viewer screenshot

### Option C: Serial / parser capture

Use when:

- your downstream system needs a clean message stream
- you are building a telemetry-to-sound or telemetry-to-control bridge

Artifacts:

- raw capture file
- replay command
- note of source rig, firmware, and semantics version

## Sanity checks before you trust a capture

Ask:

- Does the value move when the expected physical action happens?
- Does it return to a believable resting state?
- Does “disarmed” look different from “armed but idle”?
- Do dropouts have a defined behavior?
- Can I replay the same file twice and get the same result?

## Suggested artifact set

Every telemetry exercise should try to end with:

- one short capture file
- one replay command or viewer path
- one note describing expected ranges
- one note describing known failure behavior
