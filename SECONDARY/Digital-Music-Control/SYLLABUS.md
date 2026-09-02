# Digital Music Control — Canonical Course Syllabus

## Course contract

- **Audience:** teen/early-college learners; select Maker or Studio track from documented experience
- **Structure:** one level = four weekly two-hour sessions; levels may be taken in sequence
- **Default first delivery:** Maker Level 1, [From Blink to MIDI](maker_track/LEVEL1_FROM_BLINK_TO_MIDI.md)
- **Equipment:** Arduino Uno-compatible board, breadboard, controls, LEDs, computer, known-good firmware, and a tested MIDI monitor or serial visualizer
- **Result:** one documented input-to-MIDI mapping, functional prototype, short demo, and revision note

This file is the course front door. It does not duplicate the detailed level packets already in this package.

## Choose the route

### Maker track

1. [From Blink to MIDI](maker_track/LEVEL1_FROM_BLINK_TO_MIDI.md)
2. [Object-Oriented Control](maker_track/LEVEL2_OBJECT_ORIENTED_CONTROL.md)
3. [Firmware Architecture and Performance UX](maker_track/LEVEL3_FIRMWARE_ARCHITECTURE.md)

Use [Maker Teacher Quickstart](maker_track/TEACHER_QUICKSTART_MAKER.md), [Teacher Binder](maker_track/TEACHER_BINDER_MAKER.md), and [Student Handout](maker_track/STUDENT_HANDOUT_MAKER.md).

### Studio track

1. [From Blink to MIDI — Advanced](studio_track/LEVEL1_FROM_BLINK_TO_MIDI_ADV.md)
2. [Object-Oriented Control — Advanced](studio_track/LEVEL2_OBJECT_ORIENTED_CONTROL_ADV.md)
3. [Firmware Architecture — Advanced](studio_track/LEVEL3_FIRMWARE_ARCHITECTURE_ADV.md)

Use [Studio Teacher Quickstart](studio_track/TEACHER_QUICKSTART_STUDIO.md), [Teacher Binder](studio_track/TEACHER_BINDER_STUDIO.md), and [Student Handout](studio_track/STUDENT_HANDOUT_STUDIO.md).

## Four-session rhythm

1. **Baseline:** identify the signal path, flash a known-good example, and verify one input and one visible or audible output.
2. **Build:** add controls, map ranges deliberately, and keep a pin/CC map.
3. **Extend:** add a scene, state, or feedback behavior; test one change at a time with a peer.
4. **Perform and explain:** demonstrate the controller, show the map, name one failure, and record the next revision.

Each meeting reserves time for bench reset, cable inspection, file naming, and a final known-state test.

## Safety, access, and fallback

- Power off before moving wires; facilitator inspects unknown circuits before power is restored.
- Use only low-voltage USB/battery systems documented by the package. No mains wiring.
- Protect hearing: begin at low monitor volume and provide visual MIDI feedback as an audio-free path.
- Give learners seated, large-control, and partner-operation options.
- Do not install unapproved drivers or software during class.
- If MIDI host software fails, use the bundled serial or Processing visualizers and assess the input-to-message mapping without audio.
- If hardware fails, use one known-good shared board and have teams revise mappings, state diagrams, and test evidence while rotating through it.

## Observable evidence

A completed level shows:

- a reproducible known-good baseline;
- a labeled pin and MIDI-control map;
- at least one input range translated into a deliberate message or behavior;
- a peer test with one recorded failure and revision;
- a short performance or demonstration with an explanation of the signal path.

## Preflight and post-delivery review

Before class, follow the selected track's quickstart, flash every board, verify the exact cable/port/host combination, stage replacement components, and test the audio-free visualizer fallback.

After class, record board/host versions, failed components, setup time, learner bottlenecks, hearing/access accommodations, and changes needed before the next delivery. The catalog's `GO-P` status depends on this local technical preflight; this syllabus does not prove a specific site is ready.

## ClassHub Delivery Map

| Phase | Private evidence | ClassHub materials |
| --- | --- | --- |
| Baseline | Board/port result and setup faults | Selected quickstart, signal-path diagram, safety boundary |
| Build | Pin/CC map and test notes | Selected level packet, student handout, MIDI/C++ cheat sheets |
| Extend | Failure log and peer feedback | Scene/state guidance and example links |
| Demonstrate | Facilitator observation and access notes | Demo prompt, reflection prompt, approved artifact only |

ClassHub may distribute reviewed instructions and collect approved artifacts. It does not authorize wiring, driver installation, volume changes, equipment use, or publication; those remain live facilitator and site decisions.
