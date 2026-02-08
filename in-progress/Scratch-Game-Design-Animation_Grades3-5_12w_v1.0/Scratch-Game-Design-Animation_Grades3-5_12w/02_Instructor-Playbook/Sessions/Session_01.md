# Session 01: Welcome to the Studio: Play Like a Designer (Mouse-only → Keyboard)

**Mission:** Build a GPIO keyboard (Piper), then navigate Scratch, move a sprite, and make something react.

## Teacher prep (before class)
- Print **Handout 00** (Piper Keyboard Build) and **Handout 01** (Studio Rules + Controls).
- Confirm **mice** are available (students can start mouse-only).
- Confirm Piper app runs and the keyboard project is accessible.
- Have a tiny Scratch demo project ready (optional).

## Materials
- Piper computers + GPIO keyboard parts
- Mice (USB)
- Timer visible
- Handouts (if used)

## Agenda (60 minutes)
**0:00–0:05 Launch**
- “Hands off keys.”
- Say today’s mission: **build controls, then build a tiny game behavior**.
- Show the *end state*: Scratch cat moves with your DIY keys.

**0:05–0:18 Setup sprint: Build the keyboard (Piper app)**
- Students open Piper app with mouse and follow the keyboard build prompts.
- Goal: LEFT / RIGHT / UP / DOWN / SPACE all test correctly.

**0:18–0:22 Quick control test in Scratch**
- In Scratch, add one test block:
  - `when [right arrow] key pressed` → `change x by (10)`
- Confirm at least LEFT/RIGHT work before moving on.

**0:22–0:30 Micro-lesson (demo)**
- Show Scratch layout: stage, sprites, scripts, costumes, sounds.
- Build live: **Arrow keys move** (4 scripts) + **click to speak**.
- Teach: Events → Motion → Looks.
- Stop after the first success.

**0:30–0:50 Build sprints**
**Sprint A (10):** Make your character move with arrow keys.  
**Reset (2):** Save + rename project.  
**Sprint B (10):** Add click-to-talk OR click-to-change-costume.  
**Reset (2):** Stand, stretch, save.  
**Sprint C (6):** Add a simple “title screen” backdrop and a start button (optional).

**0:50–0:58 Share + Playtest**
- Prompt: “Can you figure out how to move? What should the game tell you?”
- 1 round of quick feedback: 2 stars + 1 wish.

**0:58–1:00 Save ritual**
- Everyone saves and writes: “Next time I will…”

## Checkpoints (what you must see working)
- Piper keyboard keys test correctly (at least LEFT/RIGHT/SPACE).
- Player sprite moves with keys.
- At least one interaction works (click, spacebar, or touching).

## Common stuck points + fixes
- **Keys not working:** check common ground; re-check the Piper pin map.
- If Scratch doesn’t start: add a hat block (green flag / key press).
- If it loops forever: add a condition or a reset.

## Extensions (fast finisher menu)
- Add a second character that says something different.
- Add a background and rename sprites clearly.
- Add a “Start” button that broadcasts `start game`.
