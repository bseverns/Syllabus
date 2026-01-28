# Video 04 — Animation: Costumes + Timing

**Length:** ~4:00  
**Best for:** Session 2

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W02: Animation  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W02: ANIMATION**  
- Bottom: **Make sprites feel alive**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Teach costume-based animation as the foundation for both gameplay motion and cutscene acting.

## Script
**HOOK (10s):**  
“Animation is the breath between frames.”

**TODAY’S GOAL (10s):**  
“Your character will have a simple walk cycle using costumes and timing.”

**BUILD STEPS (2:30):**

## Lower-third captions for BUILD (paste into editor)
1. Create 2–4 walking costumes
2. Green flag: start an animation loop
3. If key pressed: repeat next costume
4. Wait a tiny beat (timing = style)
5. Tune speed by changing the wait value
6. Challenge: add a jump costume

1) “Open **Costumes**. Make or choose 2–4 walking poses.”  
2) “Back to Code. Add:”  
   - `when green flag clicked`  
   - `forever`  
     - `if <key right arrow pressed?> then`  
       - `repeat 4`  
         - `next costume`  
         - `wait 0.07 seconds`

**COMMON BUG (20s):**  
“Too fast? Increase the wait. Too slow? Decrease the wait.”

**PAUSE & BUILD (30s):**  
“Pause. Add a jump costume: when up arrow is pressed, switch to a jump costume for 0.2 seconds.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
