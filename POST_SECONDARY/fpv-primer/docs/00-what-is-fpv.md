# What is FPV?

FPV (First Person View) is not one thing. It is a stack:

- **power**
- **propulsion**
- **radio link**
- **flight control**
- **video transport**
- **telemetry**
- **software and logs**

The point of this primer is not to worship any one brand or build style; it’s to make the stack *legible*:
- what talks to what
- what can fail
- what must be measured
- what can be safely simulated on the bench

**Key idea:** you don’t “learn FPV” once—you learn the *interfaces* between layers.

## Minimum viable mental model

An FPV craft usually involves at least five interacting systems:

1. **Energy system**
Battery, connectors, regulators, current draw, heat.

2. **Vehicle control system**
Receiver -> flight controller -> ESCs -> motors.

3. **Perception system**
Camera, VTX, goggles or ground receiver.

4. **State / telemetry system**
OSD, blackbox, serial telemetry, logs, exported values.

5. **Operator system**
Pilot habits, mode discipline, arming logic, stop rules, maintenance, and decision-making.

## What post-secondary rigor should mean here

For this primer, rigor means:

- you can identify the active subsystem during a failure
- you can generate an artifact that proves a claim
- you can compare two states of the same rig without hand-waving
- you can explain the difference between control, video, and telemetry

## Three distinctions students must stop blurring

### 1. Control link is not video link

The receiver may still have control even when the goggles go bad.
The goggles may still show video even when the control link is unhealthy.

### 2. Telemetry is not truth unless semantics are defined

A number only becomes useful when you know:

- what it measures
- when it is valid
- what range is expected
- what a dropout means

### 3. Bench proof is not “less real” than flight

Bench replay is where you prove:

- parsing works
- failsafe logic is sane
- mappings behave on repeatable input
- you can compare versions without risking a crash
