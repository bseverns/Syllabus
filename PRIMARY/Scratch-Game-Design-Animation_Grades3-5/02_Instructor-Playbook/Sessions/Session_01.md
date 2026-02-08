# Session 01: Welcome to the Studio: Build the Controls

**Mission:** Start from *zero*: build a GPIO keyboard (Piper), then use it to move a sprite in Scratch.

This session is designed for rooms where students **do not start with a physical keyboard**.
Students can begin with a mouse, build keys through GPIO, and then play their projects with the DIY keyboard.

## Teacher prep (before class)
- Confirm the Piper app is installed and the **Keyboard / GPIO Keyboard** activity is available.
- Stage one keyboard kit per station (GPIO cable + conductive parts + tape/marker).
- Print:
  - **Handout 00** (Piper GPIO Keyboard Build)
  - **Handout 01** (Scratch Studio Rules + Controls)
- Optional: have a tiny Scratch “move + talk” demo project ready.

## Materials
- Devices with Piper app + Scratch access
- GPIO keyboard parts (per station)
- Timer visible
- Handouts (if used)

## Agenda (60 minutes)

**0:00–0:05 Launch**
- “Eyes on me — hands off controls.”
- Say today’s mission: “We build our keyboard, then we build our first Scratch test.”
- Show the end goal (10 seconds): sprite moves with DIY keys.

**0:05–0:20 Build Sprint: Piper Keyboard**
- Students open Piper with the mouse.
- Build 5 keys minimum: **Left / Right / Up / Down / Action (Space)**.
- Test keys inside Piper.

Teacher coaching line: “If nothing works, check **GND** first.”

**0:20–0:28 Scratch Micro-lesson (demo)**
- Show Scratch layout: stage, sprites, scripts.
- Build live: **5 key scripts** (move + talk).
- Teach: Events → Motion → Looks.
- Emphasize: click inside Scratch once so it “listens” for keys.

**0:28–0:50 Build sprints**
**Sprint A (10):** Rebuild the 5 key scripts (students do it, you coach).  
**Reset (2):** Save + rename.  
**Sprint B (10):** Add one “reaction” (click-to-talk OR click-to-change costume).  
**Reset (2):** Stand, stretch, save.  
**Sprint C (8):** Optional: add a simple title screen backdrop.

**0:50–0:58 Playtest rotation**
- Prompt: “Can you move? Does the game tell you what to do?”
- Testers leave **2 stars + 1 wish**.

**0:58–1:00 Share + Save**
- 1–2 quick shares.
- Everyone writes: “Next time I will…”

## Checkpoints (what you must see working)
- DIY keyboard registers at least 5 keys.
- Player sprite moves with keys.
- Project is saved with a clear name.

## Common stuck points + fixes
- **Nothing registers in Piper:** ground (GND) is missing/loose; reattach first.
- **Works in Piper but not Scratch:** click inside Scratch window once; confirm key choice (arrows vs WASD).
- **Movement feels “stuck”:** check for duplicated scripts or conflicting key blocks.
- **Students rush wiring:** pause and do a 30-second “hands off / check connections” reset.

## Extensions (fast finisher menu)
- Add a second sprite that reacts to clicks.
- Add a background and rename sprites clearly.
- Add a “Start” button that broadcasts `start game`.
