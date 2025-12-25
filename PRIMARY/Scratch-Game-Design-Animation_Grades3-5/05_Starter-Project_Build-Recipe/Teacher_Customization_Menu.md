# Teacher Customization Menu (Choose-Your-Own-Adventure)

Use these swaps to tailor the template to different student skill levels without rewriting the structure.

## Swap A: Win Level 1 by reaching a door (instead of score goal)
- In `Coin`, remove the “level completion” loop.
- In `Door`, add:
  - if touching Player AND level = 1 → broadcast `level1 complete`

## Swap B: Key + Door (classic “unlock” mechanic)
Variables:
- `hasKey` (0/1)

Sprites:
- `Key` sprite

Flow:
- Touch Key → set `hasKey = 1`, hide key, play sound.
- Door checks `hasKey` before completing the level.

## Swap C: Timer survival level
Variables:
- `timeLeft`
- On begin level: set `timeLeft = 20`
- Every 1 second: change timeLeft by -1
- If timeLeft == 0 → broadcast `level1 complete`

## Swap D: Boss phase in Level 2 (clones)
- Hazard makes clones in Level 2:
  - every 1 second create a clone
  - clones move towards Player slowly

## Swap E: Cutscene “camera” trick
- During cutscene, hide Coin/Hazard/Door.
- Move Player and NPC with `glide` to create a cinematic beat.
- Use `change [ghost] effect` for fade-in/out.

## Swap F: Difficulty ramp without frustration
- Level 1: slower hazard, more space, goal=6
- Level 2: faster hazard, goal=10 or door + key

