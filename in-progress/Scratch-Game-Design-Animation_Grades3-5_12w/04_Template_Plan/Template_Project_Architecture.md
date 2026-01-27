# Template Project Plan (Architecture Only — no file required yet)

This is a shared blueprint students can follow so projects stay stable.

## Backdrops (scenes)
- `Menu`
- `Level1`
- `Cutscene1`
- `Level2`
- `Win`
- `GameOver`

## Variables (suggested)
- `level` (number)
- `score` (number)
- `lives` (number)
- `controlsOn` (0 or 1)

## Broadcast messages (suggested)
- `start game`
- `freeze`
- `unfreeze`
- `level complete`
- `reset`
- `game over`
- `win`

## Sprite roles (recommended)
### Player
- movement (gated by controlsOn)
- collision with collectibles/hazards
- tells the door when level complete

### Door
- checks touch (or receives a message from player)
- broadcasts `level complete`

### UI sprite (optional)
- shows instructions
- shows score/lives styling
- handles menu buttons

### Enemy/Hazard
- movement
- damage trigger (broadcast reset)

## The “controls gate” pattern
Player movement scripts only run when `controlsOn = 1`.

## The “cutscene freeze” pattern
- At cutscene start: set controlsOn to 0 (or broadcast freeze)
- At cutscene end: set controlsOn to 1 (or broadcast unfreeze)

