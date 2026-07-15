# Scratch Arcade Adventure Studio (Grades 3–5) — Instructor Play-by-Play

This is the operating guide for the course: pacing, rituals, success conditions, and session flow.

## Course success conditions

Students finish with a playable Scratch game that includes:

- title screen and instructions
- a working HUD with at least two variables
- one enemy or hazard pattern
- one power-up or temporary advantage
- three stages, waves, or challenge zones
- one final challenge or boss-style moment
- win and restart flow

## Weekly classroom rhythm

### 0:00–0:05 | Launch

- hands off mice and keys
- one-sentence mission
- one tiny teacher demo

### 0:05–0:12 | Micro-lesson

- teach only the new blocks or pattern for that day
- show one small working example

### 0:12–0:42 | Build sprints

- Sprint A: 12 minutes
- reset: 3 minutes
- Sprint B: 12 minutes
- reset: 3 minutes
- Sprint C: 12 minutes

### 0:42–0:52 | Test round

- partner playtest, teacher checkpoint, or bug hunt

### 0:52–1:00 | Share + save

- two quick shares
- everyone writes: "Next time I will..."

## Roles

Rotate weekly:

- Debugger
- Artist
- Systems Coach
- Playtester
- Save Captain

## Teacher prep before Week 1

1. confirm devices open Scratch reliably
2. decide whether students use individual accounts or a class studio
3. print the handouts you want to use
4. choose whether students begin from a blank project or a simple starter file
5. review the template plan in `04_Template_Plan/`

## Recommended starter architecture

Variables:

- `score`
- `health`
- `stage`
- `gameState`
- `powerMode`

Suggested broadcasts:

- `start game`
- `show instructions`
- `stage clear`
- `boss start`
- `player hit`
- `game over`
- `you win`
- `reset run`

## Patterns to teach early

### Pattern A — Game state gate

Only run player controls when `gameState = play`.

### Pattern B — Damage cooldown

After a hit, make the player flicker or wait briefly so health does not drop instantly to zero.

### Pattern C — Power-up timer

Set `powerMode` to on, wait a short time, then turn it off again.

### Pattern D — Stage or wave clear

Use a condition such as score, timer, or defeated enemies to trigger the next section.

## Assessment approach

Use fast milestone checks:

- Working
- Almost
- Not yet

Save detailed comments for playtests and showcase prep.

## When the room gets noisy

- pause the timer
- give one instruction only
- restart the sprint
- praise the students who already made the transition

## Companion files

- `Sessions/`
- `Classroom_Routines.md`
- `Troubleshooting_Guide.md`
- `Assessment_Rubrics.md`

## ClassHub Delivery Map

| Checkpoint | Evidence worth reviewing | ClassHub materials |
| --- | --- | --- |
| Weekly save | Current `.sb3`, one working milestone, and `Next time I will…` | Private `.sb3` upload; checklist; reflection |
| Systems checkpoint | HUD, damage cooldown, power-up timer, and stage/wave transition | Midpoint rubric; private project upload |
| Playtest checkpoint | Specific player confusion/bug and one applied change | Playtest reflection; revised upload |
| Showcase checkpoint | Title/instructions, three stages, final challenge, win/restart flow | Final rubric; optional moderated gallery game |

Scope helper support to Scratch blocks, state flow, save recovery, and symptom → check → retest debugging. Do not let helper output replace the student's game design.
