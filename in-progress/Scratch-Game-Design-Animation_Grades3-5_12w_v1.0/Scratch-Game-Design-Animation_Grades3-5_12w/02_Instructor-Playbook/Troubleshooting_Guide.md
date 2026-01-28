# Troubleshooting Guide (Scratch Game + Cutscenes)

## 1) “My sprite won’t move”
- Check the script starts with an event block (green flag / key press).
- Check `controlsOn` is 1 (if using the controls gate).
- Confirm you didn’t put movement blocks under the wrong sprite.

## 2) “Score keeps going up forever”
- Your collision check is inside a `forever` loop without a guard.
Fix: when touching collectible:
- add points
- hide collectible (or move it)
- wait 0.1 seconds (optional)
- show again later

## 3) “Door doesn’t change levels”
- Door and player must agree on which sprite checks collision.
- Use `broadcast [level complete] and wait`
- Then switch backdrop.

## 4) “Cutscene plays but I can still move”
- In cutscene start: `set controlsOn to 0` (or broadcast `freeze`)
- At cutscene end: `set controlsOn to 1` (or broadcast `unfreeze`)

## 5) “Sprites are on the wrong backdrop”
- Use `when backdrop switches to [Level1]` to show/hide sprites for that scene.

## 6) “Everything is messy — too many scripts”
- Create broadcasts for major moments:
  - `reset`, `level complete`, `game over`
- Group scripts by purpose:
  - Controls
  - Collisions
  - Scene switching
  - UI

