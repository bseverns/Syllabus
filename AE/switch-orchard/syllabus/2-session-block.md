# Switch Orchard — Two-Session Lab Block

**Format:** 2 sessions × 90–120 minutes  
**Platform:** Tangible Waves AE Modular BRAEDBOARD (0–5V)  
**Core:** CD4051 (analog switch) + simple addressing (manual or stepped)

## Course description
In this lab, students build a **router**: a circuit that chooses where a signal goes (or which signal gets through).
Instead of shaping sound directly, this module shapes **pathways**—the hidden architecture of a patch.

The CD4051 is the heart: an 8-channel analog switch that connects one of eight pins to a common pin.
We use three address lines (A/B/C) to select the active channel.

## Learning outcomes
Students will:
1. Explain what a “multiplexer/demultiplexer” does in plain language.
2. Build a manual selector using three bits derived from a knob (coarse stepping with Schmitt thresholds).
3. Build an automatic scanner where a clock advances the selection.
4. Patch routing creatively: modulation selection, audio slicing, and “moving spotlight” control voltage.
5. Debug analog switching: power, inhibit, address lines, and signal biasing.

## Materials (per pair)
From your bench kit:
- ICs: CD4051, CD40106, (optional) CD4017, (optional) MCP602
- Resistors: 1k, 10k, 47k, 100k
- Capacitors: 100nF (decoupling), 10nF/100nF for smoothing
- LEDs + 1k
- 50k pot (manual selection) + (optional) 50k pot for scan rate if building a clock
- Slide switch (mode select), tactile switch (reset/step) optional

---

## Session 1 — Manual router: “choose the branch”
### Build focus
- Power + decoupling discipline
- CD4051 core wiring (Z, X0–X7, INH)
- Manual address control (A/B/C)

### Agenda
- 0:00–0:10 Demo: routing as composition (“same signal, different path”)
- 0:10–0:30 Wire the 4051 safely: power, GND, INH, Z
- 0:30–1:10 Build manual selector: pot → 3 thresholds → A/B/C
- 1:10–1:40 Add LED readout for selection states (optional)
- 1:40–2:00 Patch lab (audio or CV)

### Checkpoints
- Z routes to exactly one Xn at a time
- Turning the selector changes which channel is active
- No “mystery silence”: INH is LOW and chips are powered

---

## Session 2 — Scanner: “the orchard walks itself”
### Build focus
- Create a clock (or use external AE clock)
- Step selection automatically (4017) and translate to A/B/C (diode encoding)
- Patch lab: rotating modulation, rhythmic rerouting, scanning a set of voltages

### Checkpoints
- Selection advances on clock ticks
- At least 4 distinct routes are audible/visible
- Optional: RESET returns to channel 0

### Studio assessment
- Photo of build + patch diagram
- 30–60s patch recording
- 3 sentences: what did scanning *change* in your music?
