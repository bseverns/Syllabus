# Handout 02 — Animation Recipe (Costumes + Timing)

## The idea
Animation = switching costumes with a little time in between.

## Recipe A: Simple loop animation
1. Make 2–4 costumes.
2. Add this script:

- **when green flag clicked**
- **forever**
  - **next costume**
  - **wait (0.1) seconds**

## Recipe B: Animate only while moving
- **when green flag clicked**
- **forever**
  - **if <key (right arrow) pressed?> then**
    - **change x by (5)**
    - **next costume**
    - **wait (0.08) seconds**

## Tips
- If it looks too fast: increase the wait time.
- If it looks too slow: decrease the wait time.
- Keep names clear: `idle1`, `idle2`, `walk1`, `walk2`.

## Challenge (optional)
Make a “blink” animation that happens every 3 seconds.

