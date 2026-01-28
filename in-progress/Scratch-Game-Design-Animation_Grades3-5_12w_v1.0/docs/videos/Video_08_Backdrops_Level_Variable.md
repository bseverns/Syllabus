# Video 08 — Switching Rooms: Backdrops + `level` Variable

**Length:** ~5:00  
**Best for:** Session 6

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W06: Rooms + Level Variable  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W06: ROOMS + LEVEL VARIABLE**  
- Bottom: **Real levels, clean swaps**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Make “levels” legible using backdrops/rooms and a `level` variable.

## Script
**HOOK (10s):**  
“Backdrops are rooms. Changing rooms is how we make levels.”

**TODAY’S GOAL (10s):**  
“Use `level` so the game knows where it is.”

**BUILD STEPS (3:10):**

## Lower-third captions for BUILD (paste into editor)
1. Make variable: level
2. Stage green flag: set level to 1
3. Stage: switch backdrop to Level1
4. Per backdrop: show/hide the right sprites
5. Per backdrop: place sprites at start positions
6. Challenge: UI sprite shows Level: (level)

1) “Make a variable: `level` (for all sprites).”  
2) “On the Stage:”  
   - `when green flag clicked`  
   - `set level to 1`  
   - `switch backdrop to [Level1]`

3) “Make sure sprites behave per room:”  
   - For each sprite, add at least one:  
     - `when backdrop switches to [Level1]` → `show` / go to start  
     - `when backdrop switches to [Cutscene1]` → `hide` *(if needed)*  
     - `when backdrop switches to [Level2]` → `show` / go to start

**COMMON BUG (25s):**  
“Sprites appearing in the wrong level means they need show/hide scripts tied to backdrops.”

**PAUSE & BUILD (25s):**  
“Pause. Make a UI sprite that displays `Level: (level)` in the corner.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
