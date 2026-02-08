# Video 06 — Hazards + Lives + Reset: The “Try Again” Loop

**Length:** ~5:00  
**Best for:** Session 4

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W04: Lives + Reset  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W04: LIVES + RESET**  
- Bottom: **Fail safely, try again**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Teach failure as feedback, not shame: lose a life, reset, try again.

## Script
**HOOK (10s):**  
“Every good game has a safe way to fail.”

**TODAY’S GOAL (10s):**  
“Touch a hazard → lose a life → return to start.”

**BUILD STEPS (3:20):**

## Lower-third captions for BUILD (paste into editor)
1. Make variable: lives
2. Player green flag: set lives to 3
3. Broadcast: reset (start position)
4. If touching hazard → lives -1
5. Broadcast reset after losing a life
6. Wait 0.5 so it doesn’t chain-hit
7. If lives = 0 → broadcast game over
8. Reset receiver: go to start x/y
9. Challenge: safe zone restores 1 life

1) “Make a variable: `lives` (for all sprites).”  
2) “On Player:”  
   - `when green flag clicked`  
   - `set lives to 3`  
   - `broadcast [reset]`  
   - `forever`  
     - `if <touching [Hazard]> then`  
       - `change lives by -1`  
       - `play sound [buzz]` *(optional)*  
       - `broadcast [reset]`  
       - `wait 0.5`  
     - `if <lives = 0> then broadcast [game over]`

3) “Reset script (Player):”  
   - `when I receive [reset]` → `go to x: 0 y: 0` *(or your start spot)*

**COMMON BUG (25s):**  
“If lives drops from 3 to 0 instantly: add the `wait 0.5` after losing a life.”

**PAUSE & BUILD (25s):**  
“Pause. Add a safe zone: touching it restores 1 life, but never above 3.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
