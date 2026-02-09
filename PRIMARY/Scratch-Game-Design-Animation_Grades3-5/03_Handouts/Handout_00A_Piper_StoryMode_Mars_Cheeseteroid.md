# Handout 00A — Piper StoryMode: Mars + Cheeseteroid (Build the Controller)

**Goal:** Students build a simple **movement controller** with GPIO + a breadboard, then use it to help Piperbot **move** (Mars) and **jump** (Cheeseteroid).

This is a “start from zero” activity for rooms where students may not have a keyboard at the start.

---

## What you need (per station)
- Piper Computer Kit (Raspberry Pi + Piper app)
- Breadboard + jumper wires
- Buttons / conductive contacts (depending on your kit)
- Mouse (for navigating menus)

---

## Safety + setup rules (read first)
- **Power off before rewiring** if anything feels unclear or misaligned.
- Only use the GPIO pins the Piper app shows for the level.
- If a button press “does nothing,” don’t force it—**check ground + pin position**.

---

## Part 1 — Launch StoryMode
1. Start the Piper app.
2. Click **StoryMode**.
3. Select **Mars** (this is Level 1).

> Note: **Cheeseteroid** is Level 2 and typically unlocks after completing Mars.

---

## Part 2 — Mars: Make Piperbot move
**What you’re building:** a basic controller for movement (usually **Left / Forward / Right**).

1. Follow the on-screen instructions in Mars.
2. When the game asks you to wire the controller:
   - Match your **GPIO pins** to the exact pin diagram shown in the Piper app.
   - Build one button at a time (wire → test → move on).
3. Test the controller in-game until Piperbot can move reliably.

**Quick check:** Each button should give the *same result every time* you press it.

---

## Part 3 — Cheeseteroid: Add a jump button
1. Return to the StoryMode map and select **Cheeseteroid**.
2. Follow the on-screen wiring instructions to add the **Jump** input.
3. Test: jump should work without breaking the movement buttons.

---

## Part 4 — Reflection (1 minute)
On a sticky note or in a class notebook, answer:
- “Which physical input made the biggest difference?”
- “What did we have to get right for the controller to work?”

---

## Troubleshooting (fast)
- **Nothing works:** confirm the correct pins + confirm a shared **ground**.
- **One button works, one doesn’t:** rebuild just that button; check the wire order.
- **It’s glitchy:** check for loose wires; re-seat connections; try shorter jumpers.

---

## Optional extension
- After Mars + Cheeseteroid, try a **second layout** that feels better in your hands.
- Name your controller: *what kind of movement does it invite?*
