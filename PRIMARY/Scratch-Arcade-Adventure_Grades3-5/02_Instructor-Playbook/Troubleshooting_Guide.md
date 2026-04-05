# Troubleshooting Guide

## Problem: player will not move

Check:

- does the script start with the right event?
- is `gameState` set to play?
- are the key blocks inside a forever loop?

## Problem: health drops too fast

Check:

- is the touching-enemy script running every frame?
- add a short wait or invincibility cooldown

## Problem: score keeps climbing forever

Check:

- does the collectible hide after touch?
- does it reappear only when intended?

## Problem: stage never changes

Check:

- what exact condition triggers the change?
- is the variable name correct everywhere?
- is the broadcast spelled exactly the same?

## Problem: boss starts too soon or never starts

Check:

- what sets `stage` or `boss start`?
- is there one script controlling the change, not three competing scripts?

## Debugging chant

Recreate -> Point -> Expect -> Change one thing -> Test again
