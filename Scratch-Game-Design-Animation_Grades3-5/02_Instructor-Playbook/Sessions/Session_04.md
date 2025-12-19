# Session 04: Obstacles + Lives: The Art of Try Again

**Mission:** Add hazards, lives, and a reset that returns the player to a start point.

## Teacher prep (before class)
- Have a reset pattern ready: `broadcast reset` and `go to x/y`.
- Consider marking “start spot” on stage with a visible object.

## Materials
- Devices with Scratch
- Timer visible
- Handouts (if used)

## Agenda (60 minutes)
**0:00–0:05 Launch**
- “Hands off keys.”
- Say today’s mission.
- Quick preview: what should be working by minute 40.

**0:05–0:12 Micro-lesson (demo)**
- Create variable `lives`.
- Build live: hazard reduces lives and broadcasts `reset`; player goes to start.
- Teach: `broadcast`, `if touching`, `set lives`, `change lives by`.

**0:12–0:42 Build sprints**
**Sprint A:** Add one hazard + lives system.  
**Reset:** Save + teacher checks “lives decreases once per hit.”  
**Sprint B:** Add a safe “start spot” and reset behavior.  
**Reset:** Stand + save.  
**Sprint C:** Add a simple game over screen when lives = 0.

**0:42–0:52 Playtest rotation**
- Prompt: “Is it fair? Does it feel like you get a second chance?”
- Testers note: too hard / too easy / confusing.

**0:52–1:00 Share + Save**
- 2–3 shares.
- Everyone writes: “Next time I will…”

## Checkpoints (what you must see working)
- `lives` variable decreases on hazard.
- `reset` returns player to a start point reliably.

## Common stuck points + fixes
- If it doesn’t start: add a hat block (green flag / key press).
- If it loops forever: add a condition or a reset.

## Extensions (fast finisher menu)
- Add invincibility blink for 1 second after hit.
- Add moving hazard (patrol left/right).
- Add health hearts UI (icons).

