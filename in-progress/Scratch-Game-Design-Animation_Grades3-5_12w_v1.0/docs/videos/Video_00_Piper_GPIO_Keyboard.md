# Video 00 — Build a Keyboard (Piper + GPIO) + Test in Scratch

**Length:** ~3:00–4:30  
**Best for:** Session 1 (or a “Day 0” setup video)

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W00: Build Your Keyboard (Piper + GPIO)  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W00: BUILD A KEYBOARD**  
- Bottom: **GPIO → Scratch controls**

## On-screen chapter captions (consistent every video)
- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**

---

## Purpose
Some classrooms start with **no keyboard**. This video gets students from **mouse-only** to a working set of keys:
**Left / Right / Up / Down / Space** — using the Piper app and GPIO.

---

## Script

**HOOK (10–15s):**  
“Watch this: I’m moving the Scratch cat with a keyboard I built out of wires.”  
(Show: press LEFT/RIGHT/SPACE — sprite moves / jumps.)

**TODAY’S GOAL (10s):**  
“By the end, you’ll build five keys with the Piper app, and you’ll test them in Scratch.”

---

## BUILD STEPS (2:00–3:00)

### Step 1 — Open Piper app (mouse-only)
“Open the **Piper app**. Choose **Build a Keyboard** (or the keyboard project).”

### Step 2 — Follow the pin map
“The app shows a **pin map**. Connect wires to the exact pins it names.  
One wire will be the **common ground** — that’s the shared wire all keys need.”

### Step 3 — Make five labeled keys
“Make five big, easy-to-press pads and label them:
LEFT, RIGHT, UP, DOWN, SPACE.”

### Step 4 — Test in the Piper app
“Press each key. The app should confirm the key is working.”

---

## COMMON BUG (20–30s)
“If nothing works: the **ground/common wire** is missing or loose.  
If the wrong key triggers: one wire is on the wrong pin — match the pin map.  
If it triggers randomly: tape the pads down and tighten the clips.”

---

## PAUSE & BUILD (10s)
“Pause the video. Build the five keys and test them in the Piper app.  
Unpause when every key lights up correctly.”

---

## Scratch test (30–45s)
“Open Scratch. Add one quick test script:

- `when [right arrow] key pressed` → `change x by (10)`

Press your RIGHT key. If the sprite moves, you’re ready.”

---

## SAVE RITUAL (say this every time)
1) Take a photo of your keyboard and write your name on it  
2) Leave it connected (so next class starts faster)  
3) Save your Scratch test: `FirstName_GameStudio_W00_TestControls`
