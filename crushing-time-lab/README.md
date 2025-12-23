# Crushing Time Lab (AE Modular Breadboard): Two-Session Workshop

Build a voltage-controlled **sample-rate reducer / “bit-crusher”** using **5V, NE555, CD40106, CD4051, and MCP602** on the Tangible Waves **BRAEDBOARD** module.

This repo is designed for teaching: fast to run, resilient to bench chaos, and tuned for learning-by-debugging.

## What students will make
A patchable AE-format breadboard circuit that:
- biases audio to mid-rail (Vref)
- generates a clock (NE555 → 40106)
- performs sample/hold (CD4051 + hold capacitor)
- outputs dry + crushed signals
- accepts CV to modulate crush rate

## Sessions
- **Session 1 (90–120 min):** Power + Vref + Audio buffer + Clock
- **Session 2 (90–120 min):** Sample/Hold crusher + CV-controlled crush + performance patching

See: [`syllabus/2-session-block.md`](syllabus/2-session-block.md)

## Files
- `syllabus/` — two-session block + objectives
- `handouts/` — student-facing build sheets + patch ideas
- `build/` — step-by-step lab build (with checkpoints)
- `troubleshooting/` — failure modes & fixes
- `schematic/` — single schematic + netlist
- `instructor-notes/` — facilitation plan + pacing + materials

## Suggested kit per pair
See [`parts/parts-list.md`](parts/parts-list.md)

## License
MIT (teaching-friendly).
