# Starter Project Build Recipe (Scratch)

This is a **starter project you can build in Scratch in ~10–20 minutes**.  
It matches the course arc: **Menu → Level 1 → Cutscene → Level 2 → Win**, with **Score + Lives**, and a clean “freeze controls during cutscenes” pattern.

You can use it in three ways:
1) **Teacher-built template** (recommended): you build once, remix/share with students.
2) **Guided whole-class build**: students follow the recipe over 1–2 sessions.
3) **Rescue scaffold**: when a project gets tangled, students can port assets into this structure.

---

## What you’ll build

### Backdrops (Stage)
- `Menu`
- `Level1`
- `Cutscene1`
- `Level2`
- `Win`
- `GameOver`

### Sprites (minimum)
- `Player`
- `Door`
- `Coin`
- `Hazard`
- `NPC` (for the cutscene—can be any sprite)

### Variables (for all sprites)
- `level` (number)
- `score` (number)
- `lives` (number)
- `goal` (number; the score needed to clear Level 1)
- `controlsOn` (0/1; freezes player during cutscenes)
- `spawnX` (number)
- `spawnY` (number)

### Broadcast messages
- `go menu`
- `start game`
- `begin level1`
- `level1 complete`
- `begin cutscene1`
- `begin level2`
- `win`
- `game over`
- `reset level`

---

## Build steps (teacher recipe)

### 1) New project + naming (1 minute)
- Create a new Scratch project.
- Rename the project: `Scratch Game Template – Levels + Cutscenes`.
- Optional: delete the Scratch Cat if you want a clean slate.

### 2) Create variables (2 minutes)
Create variables **for all sprites**:
- `level, score, lives, goal, controlsOn, spawnX, spawnY`

Set a suggested default:
- `lives = 3`
- `goal = 10`

### 3) Create broadcasts (1 minute)
In the Events palette, make these broadcasts:
- `go menu`, `start game`, `begin level1`, `level1 complete`, `begin cutscene1`, `begin level2`, `win`, `game over`, `reset level`

### 4) Add Stage backdrops (2 minutes)
Add or draw six backdrops with the names above.  
They can be simple color cards with big text; polish later.

### 5) Add sprites (2 minutes)
Pick anything from the Scratch library—keep it simple:
- **Player**: something that reads well as “you”
- **Door**: a portal/door/flag
- **Coin**: a star/coin/gem
- **Hazard**: spike/enemy/laser
- **NPC**: any character for dialogue in the cutscene

Rename sprites exactly: `Player`, `Door`, `Coin`, `Hazard`, `NPC`.

---

## Block stacks (copy these exactly)

> Tip: build in this order: **Stage → Player → Coin → Hazard → Door → NPC**.

### Stage scripts

**A) Global setup**
- `when green flag clicked`
  - `set [score v] to (0)`
  - `set [lives v] to (3)`
  - `set [goal v] to (10)`
  - `set [level v] to (0)`
  - `broadcast [go menu v]`

**B) Menu**
- `when I receive [go menu v]`
  - `switch backdrop to [Menu v]`
  - `set [controlsOn v] to (0)`
  - `show` *(Stage is always visible; ignore if not present)*
  - *(optional)* `set [score v] to (0)` and `set [lives v] to (3)`

- `when [space v] key pressed`
  - `broadcast [start game v]`

**C) Start game → Level 1**
- `when I receive [start game v]`
  - `set [score v] to (0)`
  - `set [level v] to (1)`
  - `broadcast [begin level1 v]`

**D) Level 1 complete → Cutscene**
- `when I receive [level1 complete v]`
  - `broadcast [begin cutscene1 v]`

**E) Cutscene → Level 2**
- `when I receive [begin level2 v]`
  - `set [level v] to (2)`
  - `broadcast [reset level v]`
  - `switch backdrop to [Level2 v]`
  - `set [controlsOn v] to (1)`

**F) Win / Game over**
- `when I receive [win v]`
  - `switch backdrop to [Win v]`
  - `set [controlsOn v] to (0)`

- `when I receive [game over v]`
  - `switch backdrop to [GameOver v]`
  - `set [controlsOn v] to (0)`

---

### Player scripts

**A) Spawn + reset**
- `when I receive [begin level1 v]`
  - `broadcast [reset level v]`
  - `switch backdrop to [Level1 v]`
  - `set [controlsOn v] to (1)`

- `when I receive [reset level v]`
  - `set [spawnX v] to (-200)`
  - `set [spawnY v] to (-120)`
  - `go to x: (spawnX) y: (spawnY)`
  - `show`

**B) Movement (simple + reliable)**
- `when green flag clicked`
  - `forever`
    - `if <(controlsOn) = (1)> then`
      - `if <key [right arrow v] pressed?> then change x by (6)`
      - `if <key [left arrow v] pressed?> then change x by (-6)`
      - `if <key [up arrow v] pressed?> then change y by (6)`
      - `if <key [down arrow v] pressed?> then change y by (-6)`
    - `end`

**C) Hit hazard → lose life**
- `when green flag clicked`
  - `forever`
    - `if <touching [Hazard v] ?> then`
      - `change [lives v] by (-1)`
      - `broadcast [reset level v]`
      - `wait (0.4) seconds`
      - `if <(lives) <= (0)> then broadcast [game over v]`
    - `end`

---

### Coin scripts

**A) Level-aware show/hide**
- `when I receive [begin level1 v]`
  - `show`

- `when I receive [begin cutscene1 v]`
  - `hide`

- `when I receive [begin level2 v]`
  - `show` *(or swap for different collectibles)*

**B) Spawn loop**
- `when I receive [reset level v]`
  - `go to x: (pick random (-220) to (220)) y: (pick random (-160) to (160))`

**C) Collect**
- `when green flag clicked`
  - `forever`
    - `if <touching [Player v] ?> then`
      - `change [score v] by (1)`
      - `play sound [pop v] until done` *(optional)*
      - `go to x: (pick random (-220) to (220)) y: (pick random (-160) to (160))`
    - `end`

**D) Trigger Level 1 completion**
- `when green flag clicked`
  - `forever`
    - `if <<(level) = (1)> and <(score) >= (goal)>> then`
      - `broadcast [level1 complete v]`
      - `wait (1) seconds` *(prevents repeated broadcast spam)*
    - `end`

---

### Hazard scripts

**A) Level-aware behavior**
- `when I receive [begin level1 v]`
  - `show`
  - `go to x: (0) y: (0)`

- `when I receive [begin cutscene1 v]`
  - `hide`

- `when I receive [begin level2 v]`
  - `show`

**B) Patrol (easy AI)**
- `when green flag clicked`
  - `forever`
    - `if <(level) = (1)> then`
      - `move (4) steps`
      - `if on edge, bounce`
    - `end`
    - `if <(level) = (2)> then`
      - `move (6) steps`
      - `if on edge, bounce`
    - `end`

---

### Door scripts

**A) Place door per level**
- `when I receive [begin level1 v]`
  - `go to x: (210) y: (150)`
  - `show`

- `when I receive [begin level2 v]`
  - `go to x: (210) y: (150)`
  - `show`

- `when I receive [begin cutscene1 v]`
  - `hide`

**B) Touch door → win (Level 2)**
- `when green flag clicked`
  - `forever`
    - `if <touching [Player v] ?> then`
      - `if <(level) = (2)> then`
        - `broadcast [win v]`
      - `end`
    - `end`

> Optional: In Level 1, touching the door could *also* complete the level (instead of score goal).

---

### NPC scripts (Cutscene)

**A) Play cutscene**
- `when I receive [begin cutscene1 v]`
  - `switch backdrop to [Cutscene1 v]`
  - `set [controlsOn v] to (0)`
  - `show`
  - `go to x: (80) y: (-40)`
  - `say [You did it! But the next room is... weird.] for (2) seconds`
  - `say [New rule: hazards are faster. Ready?] for (2) seconds`
  - `broadcast [begin level2 v]`

**B) Hide otherwise**
- `when I receive [begin level1 v]` → `hide`
- `when I receive [begin level2 v]` → `hide`

---

## Quick test checklist
1) Green flag shows **Menu**.  
2) Press Space → **Level 1** begins. Player can move.  
3) Collect coins → score rises.  
4) Touch hazard → lose life + reset.  
5) Score reaches goal → **Cutscene** plays, controls frozen.  
6) Cutscene ends → **Level 2** begins.  
7) Touch door in Level 2 → **Win**.  
8) Lives reach 0 → **Game Over**.

---

## How this template supports the 12-week course
- Weeks 1–2: movement + animation (Player costumes)
- Week 3: coin/score system
- Week 4: hazards/lives + reset loop
- Week 5–6: level transitions (backdrops + broadcasts)
- Week 7: cutscene pattern (freeze/unfreeze)
- Week 8–10: Level 2 new mechanic + polish
- Week 11: structured debugging
- Week 12: showcase

---

## Teacher customization ideas (low effort, high payoff)
- Replace score goal with a **mission**: “find key” (variable) then unlock door.
- Add a **timer** level: survive 20 seconds.
- Add a **boss**: hazard spawns clones in Level 2.
- Add a **second cutscene** before the Win screen.

