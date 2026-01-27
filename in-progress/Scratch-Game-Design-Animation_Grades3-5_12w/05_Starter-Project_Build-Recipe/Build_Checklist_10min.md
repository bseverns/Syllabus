# 10-Minute Build Checklist (Teacher)

Use this to assemble the starter project fast, without reading the full recipe.

## Setup
- [ ] New project name: `Scratch Game Template – Levels + Cutscenes`
- [ ] Variables (for all sprites): `level, score, lives, goal, controlsOn, spawnX, spawnY`
- [ ] Broadcasts: `go menu, start game, begin level1, level1 complete, begin cutscene1, begin level2, win, game over, reset level`
- [ ] Backdrops: `Menu, Level1, Cutscene1, Level2, Win, GameOver`
- [ ] Sprites renamed: `Player, Door, Coin, Hazard, NPC`

## Stage scripts
- [ ] Green flag: set defaults; broadcast `go menu`
- [ ] `go menu`: switch to Menu; controlsOff
- [ ] Space key: broadcast `start game`
- [ ] `start game`: score=0; level=1; broadcast `begin level1`
- [ ] `level1 complete`: broadcast `begin cutscene1`
- [ ] `begin level2`: level=2; broadcast `reset level`; switch to Level2; controlsOn
- [ ] `win` and `game over`: switch backdrops; controlsOff

## Player scripts
- [ ] `begin level1`: broadcast `reset level`; switch backdrop Level1; controlsOn
- [ ] `reset level`: go to spawn; show
- [ ] Movement loop checks `controlsOn`
- [ ] Touching Hazard: lives-- ; reset; if lives<=0 → `game over`

## Coin scripts
- [ ] On reset: random position
- [ ] Touch Player: score++ ; random position
- [ ] If level==1 and score>=goal → broadcast `level1 complete` (with 1s wait)
- [ ] Hide during cutscene; show in levels

## Hazard scripts
- [ ] Patrol + bounce; faster in Level 2
- [ ] Hide during cutscene; show in levels

## Door scripts
- [ ] Place door on begin level1/2; hide during cutscene
- [ ] If touching Player AND level==2 → broadcast `win`

## NPC scripts
- [ ] `begin cutscene1`: switch backdrop; controlsOff; say lines; broadcast `begin level2`
- [ ] Hide during levels

## Test
- [ ] Menu → Space → Level1 → Cutscene → Level2 → Win  
- [ ] Hazard decreases lives; lives==0 → GameOver
