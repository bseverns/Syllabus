# Broadcast Map (Suggested)

## Menu → Level 1
- Start button: broadcast `start game`
- Stage: when I receive `start game` → switch backdrop to `Level1` → broadcast `reset`

## Level 1 complete → Cutscene
- Door or Player: broadcast `level complete`
- Stage: when I receive `level complete` → broadcast `freeze` → switch backdrop to `Cutscene1`

## Cutscene end → Level 2
- Cutscene script ends with: switch backdrop to `Level2` → broadcast `reset` → broadcast `unfreeze`

## Game over / Win
- Player checks lives/goal:
  - if lives = 0 → broadcast `game over`
  - if goal met in Level2 → broadcast `win`

