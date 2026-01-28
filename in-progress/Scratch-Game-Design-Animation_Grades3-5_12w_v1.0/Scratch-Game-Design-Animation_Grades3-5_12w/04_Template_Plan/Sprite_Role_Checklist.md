# Sprite Role Checklist (Quick sanity check)

## Player
- ☐ movement gated by controlsOn
- ☐ start position set on reset
- ☐ collisions update score/lives
- ☐ win condition triggers level complete

## Door
- ☐ touching player triggers level complete
- ☐ visible only on level backdrops

## Collectible
- ☐ touching player adds score
- ☐ hides or relocates after collecting

## Hazard/Enemy
- ☐ predictable movement
- ☐ collision reduces lives once (cooldown)
- ☐ triggers reset

## UI
- ☐ shows instructions
- ☐ shows win/game over

