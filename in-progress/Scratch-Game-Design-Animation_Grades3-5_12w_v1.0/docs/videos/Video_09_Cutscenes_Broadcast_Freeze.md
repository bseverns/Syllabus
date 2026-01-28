# Video 09 — Cutscenes: Broadcast + Freeze + Stagecraft

**Length:** ~5:00  
**Best for:** Session 7

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W07: Cutscenes  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W07: CUTSCENES**  
- Bottom: **Story between levels**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Create a cutscene between levels that feels like a tiny movie: controls off, characters act, then the next level begins.

## Build recipe
- Broadcasts: `to cutscene`, `start level 2`, `freeze`, `unfreeze`
- Stage switches to `Cutscene1` backdrop
- Player controls off during cutscene

## Script
**HOOK (10s):**  
“Cutscenes are where the story breathes between challenges.”

**TODAY’S GOAL (10s):**  
“Level 1 ends → cutscene plays → Level 2 begins.”

**BUILD STEPS (3:10):**

## Lower-third captions for BUILD (paste into editor)
1. On level complete: broadcast freeze
2. Switch backdrop to Cutscene1
3. Broadcast: to cutscene
4. Cutscene character: show and speak
5. Animate: glide to a mark
6. Hide when done
7. Broadcast: start level 2
8. Stage: set level to 2
9. Switch backdrop to Level2
10. Broadcast: unfreeze (controls back on)
11. Challenge: add a second actor

1) “On Stage (or a director sprite):”  
   - `when I receive [level complete]`  
   - `broadcast [freeze]`  
   - `switch backdrop to [Cutscene1]`  
   - `broadcast [to cutscene]`

2) “On a Cutscene Character sprite:”  
   - `when I receive [to cutscene]`  
   - `show`  
   - `say "We did it… but the next room is harder." for 2 seconds`  
   - `glide 1 secs to x: __ y: __`  
   - `hide`  
   - `broadcast [start level 2]`

3) “Back on Stage:”  
   - `when I receive [start level 2]`  
   - `set level to 2`  
   - `switch backdrop to [Level2]`  
   - `broadcast [unfreeze]`

**COMMON BUG (25s):**  
“If the player moves during the cutscene, make sure `broadcast freeze` happens before any waiting.”

**PAUSE & BUILD (30s):**  
“Pause. Add a second character who appears, talks, then disappears.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
