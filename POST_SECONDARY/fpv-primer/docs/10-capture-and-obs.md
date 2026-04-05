# Capture and OBS patterns

FPV + music systems need capture that shows process, not just spectacle.

## Capture layers worth recording

- screen capture:
  - Betaflight
  - blackbox viewer
  - MIDI monitor
  - parser or patch UI
- audio:
  - DAW or synth output
- camera:
  - hands, rig, pilot actions
- optional:
  - DVR or video feed

## Show “the truth” on screen

Whenever possible, include at least one truth surface:

- telemetry plot
- level meter
- blackbox trace
- MIDI monitor
- log timestamp

If the viewer cannot see the data source, they cannot evaluate the claim.

## Suggested OBS scene set

### Scene 1: Full explanation
- face or hands cam
- source patch or parser
- meter or monitor

### Scene 2: Comparison
- A/B capture labels
- same telemetry source
- two mapping outputs

### Scene 3: Playback proof
- blackbox or replay source visible
- target output visible
- note of version / preset

## Reproducibility rule

Every capture should make it easy to recover:

- which rig
- which config
- which mapping preset
- which replay file
- which date or version
