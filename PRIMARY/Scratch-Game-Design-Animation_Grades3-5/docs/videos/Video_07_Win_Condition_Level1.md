# Video 07 — Level 1 Win Condition: Door / Score / Timer

**Length:** ~4:30  
**Best for:** Session 5

## Title + Thumbnail (copy/paste)
**Title:** Scratch Game Studio — W05: Level 1 Win Condition  
**Thumbnail text:**  
- Top: **SCRATCH GAME STUDIO**  
- Big: **W05: LEVEL 1 WIN CONDITION**  
- Bottom: **Finish the level**

## On-screen chapter captions (consistent every video)
Use these as big, readable lower-third text (or quick full-screen cards):

- **HOOK**
- **TODAY’S GOAL**
- **BUILD**
- **COMMON BUG**
- **PAUSE & BUILD**
- **SAVE**


## Purpose
Give Level 1 a clear ending, so transitions and cutscenes have something real to connect to.

## Choose ONE win condition
- **Door:** reach the exit
- **Score:** collect enough
- **Timer:** survive long enough

## Script
**HOOK (10s):**  
“A level becomes a level when it has a goal.”

**TODAY’S GOAL (10s):**  
“When we win, we broadcast `level complete`.”

**BUILD STEPS (2:45):**

## Lower-third captions for BUILD (paste into editor)
1. Pick your win: Door, Score, or Timer
2. Door win: touching door → broadcast level complete
3. Score win: score ≥ target → broadcast level complete
4. Timer win: timer > target → broadcast level complete
5. Prevent repeats: stop scripts or set levelComplete flag
6. Challenge: 1-second celebration screen


### Option A — Door
- Door sprite:  
  - `when green flag clicked` → `show`  
  - `forever` → `if <touching [Player]> then broadcast [level complete]`

### Option B — Score
- Player:  
  - `forever` → `if <score >= 10> then broadcast [level complete]`

### Option C — Timer
- Player or Stage:  
  - `when green flag clicked` → `reset timer`  
  - `forever` → `if <timer > 20> then broadcast [level complete]`

**COMMON BUG (25s):**  
“If it completes over and over: after broadcasting, stop scripts or set a `levelComplete = 1` variable.”

**PAUSE & BUILD (30s):**  
“Pause. Add a one-second celebration: show text ‘LEVEL COMPLETE!’ and play a sound.”

---

## SAVE RITUAL (say this every time)
1) Rename: `FirstName_GameStudio_W##_YourTitle`  
2) **File → Save now**  
3) Test the green flag once before you close the tab
