# Video 10 — Level 2: One New Mechanic

**Length:** ~4:30  
**Best for:** Session 8 or Session 10

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W08: Level 2 Mechanic  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W08: LEVEL 2 MECHANIC**  
- Bottom: **Make it meaningfully new**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Make Level 2 meaningfully different. Difficulty should be a *new idea*, not just faster chaos.

## Pick ONE mechanic to add (choose the one you demo in class)
- Moving platforms (glide back and forth)
- Key + door (must collect key first)
- Enemy patrol (bounce)
- Wind/storm (push player sideways)
- Puzzle switch (touch switch to open door)

## Script
**HOOK (10s):**  
“Level 2 is where your game reveals its second thought.”

**TODAY’S GOAL (10s):**  
“Add one new mechanic that changes how the player plays.”

**BUILD STEPS (2:40):** *(example: enemy patrol)*  

## Lower-third captions for BUILD (paste into editor)
1. Pick ONE new mechanic for Level 2
2. Level2 backdrop switch: show the new mechanic
3. Enemy patrol: move steps in a loop
4. Enemy patrol: if on edge, bounce
5. If touching player → reset / lose life
6. Hide the mechanic in other backdrops
7. Challenge: Level 2 reward feels bigger

1) “Enemy sprite, Level 2 only:”  
   - `when backdrop switches to [Level2]` → `show` → `go to x: __ y: __`  
   - `forever`  
     - `move 3 steps`  
     - `if on edge, bounce`  
     - `if <touching [Player]> then broadcast [reset]` *(and/or lose a life)*

2) “Make sure enemy hides elsewhere:”  
   - `when backdrop switches to [Level1]` → `hide`  
   - `when backdrop switches to [Cutscene1]` → `hide`

**COMMON BUG (25s):**  
“If your new mechanic appears in the wrong level, you need show/hide tied to backdrops.”

**PAUSE & BUILD (30s):**  
“Pause. Add a reward that matches Level 2: gems worth 5, or a time bonus.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
