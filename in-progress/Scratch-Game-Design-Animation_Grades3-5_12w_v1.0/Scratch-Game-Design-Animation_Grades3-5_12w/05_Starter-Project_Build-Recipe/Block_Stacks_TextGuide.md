# Block Stacks – Text Guide

Scratch is visual, so this guide uses **exact block names** and indentation to match stack structure.
Build in this order: **Stage → Player → Coin → Hazard → Door → NPC**.

## Notes
- Variables should be **for all sprites** so every sprite can read them.
- Use `broadcast [message] and wait` only inside cutscenes; regular broadcast elsewhere keeps things snappy.
- If you see repeated cutscene triggers, add short waits (0.5–1.0s) after broadcasts.

---

## Stage (Stage)

### Global setup
**when green flag clicked**
- set `score` to 0  
- set `lives` to 3  
- set `goal` to 10  
- set `level` to 0  
- broadcast `go menu`

### Menu
**when I receive `go menu`**
- switch backdrop to `Menu`
- set `controlsOn` to 0

**when space key pressed**
- broadcast `start game`

### Start game
**when I receive `start game`**
- set `score` to 0
- set `level` to 1
- broadcast `begin level1`

### Level transitions
**when I receive `level1 complete`**
- broadcast `begin cutscene1`

**when I receive `begin level2`**
- set `level` to 2
- broadcast `reset level`
- switch backdrop to `Level2`
- set `controlsOn` to 1

### End states
**when I receive `win`**
- switch backdrop to `Win`
- set `controlsOn` to 0

**when I receive `game over`**
- switch backdrop to `GameOver`
- set `controlsOn` to 0

---

## Player (Sprite: Player)

### Begin Level 1
**when I receive `begin level1`**
- broadcast `reset level`
- switch backdrop to `Level1`
- set `controlsOn` to 1

### Reset position
**when I receive `reset level`**
- set `spawnX` to -200
- set `spawnY` to -120
- go to x: `spawnX` y: `spawnY`
- show

### Movement loop
**when green flag clicked**
- forever
  - if `(controlsOn) = 1`
    - if key right arrow pressed → change x by 6
    - if key left arrow pressed → change x by -6
    - if key up arrow pressed → change y by 6
    - if key down arrow pressed → change y by -6

### Hazard hit loop
**when green flag clicked**
- forever
  - if touching `Hazard`
    - change `lives` by -1
    - broadcast `reset level`
    - wait 0.4 seconds
    - if `(lives) <= 0` → broadcast `game over`

---

## Coin (Sprite: Coin)

### Show/hide by scene
**when I receive `begin level1`** → show  
**when I receive `begin cutscene1`** → hide  
**when I receive `begin level2`** → show  

### Respawn
**when I receive `reset level`**
- go to random x/y

### Collect loop
**when green flag clicked**
- forever
  - if touching `Player`
    - change `score` by 1
    - go to random x/y

### Level 1 completion
**when green flag clicked**
- forever
  - if `level = 1` AND `score >= goal`
    - broadcast `level1 complete`
    - wait 1 seconds

---

## Hazard (Sprite: Hazard)

### Show/hide
**when I receive `begin level1`**
- show
- go to x: 0 y: 0

**when I receive `begin cutscene1`** → hide  
**when I receive `begin level2`** → show  

### Patrol
**when green flag clicked**
- forever
  - if `level = 1`
    - move 4 steps
    - if on edge, bounce
  - if `level = 2`
    - move 6 steps
    - if on edge, bounce

---

## Door (Sprite: Door)

### Place per level
**when I receive `begin level1`**
- go to x: 210 y: 150
- show

**when I receive `begin level2`**
- go to x: 210 y: 150
- show

**when I receive `begin cutscene1`** → hide  

### Win condition (Level 2)
**when green flag clicked**
- forever
  - if touching `Player`
    - if `level = 2`
      - broadcast `win`

---

## NPC (Sprite: NPC)

### Cutscene
**when I receive `begin cutscene1`**
- switch backdrop to `Cutscene1`
- set `controlsOn` to 0
- show
- go to x: 80 y: -40
- say “You did it! But the next room is… weird.” for 2 seconds
- say “New rule: hazards are faster. Ready?” for 2 seconds
- broadcast `begin level2`

### Hide otherwise
**when I receive `begin level1`** → hide  
**when I receive `begin level2`** → hide  

