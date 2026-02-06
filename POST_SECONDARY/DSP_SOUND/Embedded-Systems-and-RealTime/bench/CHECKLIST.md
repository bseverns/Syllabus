# Bench Checklist (before calling it “done”)

## Power + enumeration
- [ ] device powers reliably from USB
- [ ] serial enumerates and prints startup banner
- [ ] (if MIDI) device appears as MIDI device

## Inputs
- [ ] each knob covers full range cleanly (0..127)
- [ ] buttons do not chatter (no false edges)
- [ ] no “stuck” states after rapid tapping

## Timing
- [ ] event rate capped (no host spam)
- [ ] latency feels consistent (no periodic hiccups)

## Persistence + recovery
- [ ] config saves and reloads correctly
- [ ] factory reset works
- [ ] safe mode works (hold button on boot)

## Documentation
- [ ] connection instructions
- [ ] control map
- [ ] config steps
- [ ] known issues
