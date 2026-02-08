# Video 03 — Controls: Arrow Keys + Freeze/Unfreeze

**Length:** ~4:30  
**Best for:** Session 3 (controls) and Session 7 (cutscenes)

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W03: Controls + Freeze  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W03: CONTROLS + FREEZE**  
- Bottom: **Cutscenes won’t break**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Create reliable controls and a switch to disable movement during cutscenes.

## Build recipe
- Variable: `controlsOn`
- Broadcasts: `freeze`, `unfreeze`
- Player movement runs only if `controlsOn = 1`

## Script
**HOOK (10s):**  
“A game needs a body. Today we give your character controls—and a way to pause controls during cutscenes.”

**TODAY’S GOAL (10s):**  
“Arrow keys move. A variable called `controlsOn` turns movement on or off.”

**BUILD STEPS (3:00):**

## Lower-third captions for BUILD (paste into editor)
1. Make variable: controlsOn (for all sprites)
2. Green flag: set controlsOn to 1
3. Forever: only move if controlsOn = 1
4. Arrow keys: change x/y to move
5. Add broadcast: freeze
6. On freeze: set controlsOn to 0
7. Add broadcast: unfreeze
8. On unfreeze: set controlsOn to 1
9. Challenge: space key = boost speed

1) “Make a variable: `controlsOn` (**for all sprites**).”  
2) “On your Player sprite, build this:”  
   - `when green flag clicked`  
   - `set controlsOn to 1`  
   - `forever`  
     - `if <controlsOn = 1> then`  
       - `if <key right arrow pressed?> then change x by 5`  
       - `if <key left arrow pressed?> then change x by -5`  
       - `if <key up arrow pressed?> then change y by 5`  
       - `if <key down arrow pressed?> then change y by -5`  
3) “Now add two receivers:”  
   - `when I receive freeze` → `set controlsOn to 0`  
   - `when I receive unfreeze` → `set controlsOn to 1`

**COMMON BUG (25s):**  
“If your player moves during a cutscene, you forgot the `controlsOn` check.”

**PAUSE & BUILD (25s):**  
“Pause. Add a ‘boost’ key: when space is pressed, move faster.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
