# On‑Screen D‑Pad Controller (Scratch) — Keyboardless Rooms

This doc gives you a simple **mouse‑driven D‑pad** for Scratch so students can play and debug games **without a physical keyboard** (works well on Raspberry Pi setups).

Use this as a Day‑1 “controls bridge” after Piper StoryMode (Mars → Cheeseteroid):  
**Inputs → messages → actions.**

---

## What students will build

A small control pad on the Scratch Stage:

- **Up / Down / Left / Right** (movement)
- **Jump** (optional)

Two versions are included:
1. **Tap-to-step** (easiest; one click = one move)
2. **Hold-to-move** (feels more like a controller; still simple)

---

## Layout (Stage)

Scratch Stage is **480×360**.

Suggested placement:
- Put the D‑pad in the **bottom-left**.
- Put Jump in the **bottom-right**.

Suggested sizes:
- Each arrow button: ~70×70 px
- Jump button: ~90×70 px

Keep it chunky and readable.

---

## Sprite setup (recommended)

Create **5 sprites**:
- `BTN_Left`
- `BTN_Right`
- `BTN_Up`
- `BTN_Down`
- `BTN_Jump` (optional)

Each button sprite:
- Has a simple costume (arrow icon or big letter).
- Has a hit area that’s easy to click.
- Uses the same pattern of code.

Create **one player sprite** (`Player`) that moves.

---

# Version 1 — Tap-to-step (fastest to teach)

### Button sprites (example: BTN_Right)
**When clicked**, broadcast a message:

- `when this sprite clicked`
- `broadcast [MOVE_RIGHT v]`

Do the same for the other directions:
- MOVE_LEFT, MOVE_UP, MOVE_DOWN, JUMP

### Player sprite (movement)
In `Player`:

**Right**
- `when I receive [MOVE_RIGHT v]`
- `change x by (10)`

**Left**
- `when I receive [MOVE_LEFT v]`
- `change x by (-10)`

**Up**
- `when I receive [MOVE_UP v]`
- `change y by (10)`

**Down**
- `when I receive [MOVE_DOWN v]`
- `change y by (-10)`

**Jump (optional)**
- `when I receive [JUMP v]`
- `change y by (40)`
- `wait (0.1) seconds`
- `change y by (-40)`

> Teaching note: This version is perfect for Grades 3–5 because it is very legible:
> click → message → action.

---

# Version 2 — Hold-to-move (still beginner-friendly)

This version uses simple “is the mouse held over this button?” logic.

## Step A — Create variables
Make these variables (for all sprites):
- `moveX`
- `moveY`
- `jumpNow` (optional)

Set defaults in the Stage (or in Player) at start:
- `set [moveX v] to (0)`
- `set [moveY v] to (0)`
- `set [jumpNow v] to (0)`

## Step B — Button sprites set the direction while held
Example for `BTN_Right`:

- `when green flag clicked`
- `forever`
  - `if <(mouse down?) and <touching [mouse-pointer v] ?>> then`
    - `set [moveX v] to (1)`
    - `set [moveY v] to (0)`
  - `end`

Do the same for each arrow:
- Left sets moveX = -1, moveY = 0
- Up sets moveX = 0, moveY = 1
- Down sets moveX = 0, moveY = -1

## Step C — A “neutral zone” resets movement
Add a small sprite called `BTN_Neutral` (a transparent square) around/behind the pad, or just do it in the Stage:

In the **Stage**:
- `when green flag clicked`
- `forever`
  - `if <not (mouse down?)> then`
    - `set [moveX v] to (0)`
    - `set [moveY v] to (0)`
  - `end`

This prevents “stuck direction” if the mouse is released.

## Step D — Player sprite moves continuously
In `Player`:

- `when green flag clicked`
- `forever`
  - `change x by ((moveX) * (6))`
  - `change y by ((moveY) * (6))`
  - `if <(jumpNow) = (1)> then`
    - `change y by (40)`
    - `wait (0.1) seconds`
    - `change y by (-40)`
    - `set [jumpNow v] to (0)`
  - `end`
  - `wait (0.02) seconds`
- `end`

## Jump button (optional)
For `BTN_Jump`:

- `when green flag clicked`
- `forever`
  - `if <(mouse down?) and <touching [mouse-pointer v] ?>> then`
    - `set [jumpNow v] to (1)`
  - `end`
- `end`

---

## Optional: add feedback (makes it feel “real”)

On each button:
- When pressed: switch to a “lit” costume OR change color effect.
- When not pressed: switch back.

This helps students *see* the input state.

---

## Classroom tips (Raspberry Pi 3)

- Keep sprites simple (big shapes, few costumes).
- Avoid heavy clones, filters, or many simultaneous sounds in early lessons.
- If Scratch slows down, reduce the Player’s movement loop rate (increase waits slightly).

---

## Quick “bridge talk” from Piper → Scratch (30 seconds)

“Piper gave us **physical inputs** that trigger actions in a game.  
In Scratch we’re doing the same thing: **a button (input) sends a message**, and the Player responds.  
Once you understand that pattern, you can control anything.”

---

## Next upgrades (if you want them later)

- Add diagonal movement (set both moveX and moveY)
- Add a “run” button (multiplier)
- Add on-screen **A/B** buttons for game actions
- Map Piper GPIO buttons to the same messages for a seamless hybrid controller
