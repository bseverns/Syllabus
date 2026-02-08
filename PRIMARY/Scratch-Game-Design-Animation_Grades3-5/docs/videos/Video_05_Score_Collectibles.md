# Video 05 — Score + Collectibles: The Coin Pattern

**Length:** ~5:00  
**Best for:** Session 3

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W03: Score + Collectibles  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W03: SCORE + COLLECTIBLES**  
- Bottom: **Build the coin pattern**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Introduce variables through a satisfying mechanic: collect → feedback → score changes.

## Build recipe
- Variable: `score`
- Coin hides briefly after collection to prevent double-counting

## Script
**HOOK (10s):**  
“Collectibles are tiny rewards. Today we teach the game to *notice* when you earn one.”

**TODAY’S GOAL (10s):**  
“Touch a coin, the coin disappears, and your score goes up.”

**BUILD STEPS (3:10):**

## Lower-third captions for BUILD (paste into editor)
1. Make variable: score
2. Player green flag: set score to 0
3. Coin: if touching player → change score by 1
4. Coin: play sound (optional)
5. Coin: hide so it can’t double-count
6. Coin: wait 0.3 seconds
7. Coin: go to random position
8. Coin: show again
9. Challenge: gems worth 5 points

1) “Make a variable: `score` (for all sprites).”  
2) “On Player:”  
   - `when green flag clicked` → `set score to 0`  
3) “On Coin sprite, build this:”  
   - `when green flag clicked`  
   - `show`  
   - `forever`  
     - `if <touching [Player]> then`  
       - `change score by 1`  
       - `play sound [pop]` *(optional)*  
       - `hide`  
       - `wait 0.3`  
       - `go to random position`  
       - `show`

**COMMON BUG (25s):**  
“If score jumps by 3 or 4 at once: your coin is being counted multiple times. Keep the hide+wait.”

**PAUSE & BUILD (25s):**  
“Pause. Make a ‘gem’ worth 5 points by switching costumes.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
