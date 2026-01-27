# Session 06: Scene Switching: Backdrops as Rooms (Menu → Level 1)

**Mission:** Build clean transitions using backdrops and broadcasts.

## Teacher prep (before class)
- Consider creating a “Backdrops checklist” on the board:
  Menu, Level1, Cutscene1, Level2, Win, GameOver.

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
- Teach the doorway pattern:
  - touching door → `broadcast [level complete] and wait`
  - switch backdrop to Level1 / Cutscene / Level2
- Teach: `switch backdrop`, `when backdrop switches to`.

**0:12–0:42 Build sprints**
**Sprint A:** Create backdrops: Menu + Level1.  
**Reset:** Save + teacher checks “start button works.”  
**Sprint B:** Add a start button that broadcasts `start game` and switches to Level1.  
**Reset:** Stand + save.  
**Sprint C:** Make sure the right sprites show/hide on each backdrop.

**0:42–0:52 Playtest rotation**
- Prompt: “Can you start the game without help?”
- Testers write down the controls they discovered.

**0:52–1:00 Share + Save**
- 2–3 shares.
- Everyone writes: “Next time I will…”

## Checkpoints (what you must see working)
- Menu exists and leads to Level1.
- Sprites appear in the correct scene (no random leftovers).

## Common stuck points + fixes
- If it doesn’t start: add a hat block (green flag / key press).
- If it loops forever: add a condition or a reset.

## Extensions (fast finisher menu)
- Add an instructions screen from the menu.
- Add a settings toggle (sound on/off).
- Add a title animation on the menu.

