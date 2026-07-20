# Choir Divider — Student Guide

## What you’re making
A **clock divider / rhythm chorus**: one pulse becomes many related pulses.

The CD4017 is a counter. Each clock tick moves it to the next output:
Q0 → Q1 → Q2 → ... → Q9 → back to Q0.

By choosing which Q outputs you listen to (and when you reset), you create rhythms.

## Two ways to make divisions
### 1) Pick steps
Take only Q0 → one pulse every 10 ticks (slow downbeat).  
Take Q0 and Q5 → two pulses per 10 ticks (half-time/offbeat pair).

### 2) Reset early
Reset at Q3 → play Q0–Q1–Q2, then reset (3-step cycle).  
Reset at Q4 → 4-step cycle. Reset at Q5 → 5-step cycle.

## What to patch in
- A clock from your rack **or** the internal 555 clock.

## What you’ll turn in
- Photo of your build
- Patch diagram
- 30–60s recording + 3 sentences about how you chose your rhythms
