# Handout 00 — Build Your Keyboard (Piper + GPIO) (Grades 3–5)

## Today’s goal
Build a **physical keyboard** using the Piper app and the GPIO pins so you can control Scratch with:
- **Arrow keys** (move)
- **Space** (action/jump)

You can do this with **only a mouse** at first.

---

## What you need (per pair)
- Piper computer (booted)
- Mouse (USB)
- Piper app (already installed)
- Piper GPIO board / breakout + wires
- Conductive “keys” (foil, coin, paperclip, conductive tape, etc.)
- Tape + marker (label keys)

---

## Build steps (follow the Piper app prompts)
1. **Open the Piper app** (mouse only).
2. Choose the project: **Build a Keyboard** (or similar).
3. The app will show a **pin map**. Connect wires from the GPIO board to the pins it names.
4. Make 5 keys and label them:
   - **LEFT**
   - **RIGHT**
   - **UP**
   - **DOWN**
   - **SPACE**
5. **Test inside the Piper app**:
   - Press each key.
   - The app should light up (or confirm) that key.

---

## Quick test in Scratch (1 minute)
1. Open Scratch (browser or app).
2. Start a new project.
3. Add one block:
   - `when [right arrow] key pressed` → `change x by (10)`
4. Press your **RIGHT** key. The sprite should move.

---

## Common stuck points (fast fixes)
- **Nothing works:** Check the **ground/common wire** is connected (the “shared” wire for all keys).
- **Wrong key triggers:** One wire is on the wrong pin — match the Piper app’s pin map.
- **Keys trigger randomly:** Tighten connections; avoid loose foil; tape it down.
- **Hard to press:** Make bigger pads; use tape to hold the contact point steady.

---

## Save / reset ritual
- Take a quick photo of your keyboard and label it with names.
- Leave it connected so next class starts faster.
