# Handout 03 — Score + Lives Block Recipes

## Recipe A: Score that behaves
1. Make a variable: `score`
2. Add to the collectible sprite:

- **when green flag clicked**
  - **show**
  - **go to random position**
- **forever**
  - **if <touching (Player)?> then**
    - **change [score] by (1)**
    - **hide**
    - **wait (0.2) seconds**
    - **go to random position**
    - **show**

## Recipe B: Lives + reset
1. Make a variable: `lives`
2. On the player sprite:

- **when green flag clicked**
  - **set [lives] to (3)**
  - **broadcast [reset]**
- **forever**
  - **if <touching (Hazard)?> then**
    - **change [lives] by (-1)**
    - **broadcast [reset]**
    - **wait (0.5) seconds**
  - **if <(lives) = (0)> then**
    - **broadcast [game over]**

## Recipe C: Reset pattern
- **when I receive [reset]**
  - **go to x: (startX) y: (startY)**

## Troubleshooting
- Score climbs too fast → hide/move the collectible after touch.
- Lives drop to 0 instantly → add a short wait after damage.

