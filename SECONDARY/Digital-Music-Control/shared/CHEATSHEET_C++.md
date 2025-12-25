# C++ Cheat Sheet (Arduino AVR)

- `setup()` runs once; `loop()` repeats.
- Types: `int` (‑32768..32767 on AVR), `byte` (0..255), `bool`, `float`.
- Digital: `pinMode(pin, INPUT_PULLUP)`, `digitalWrite(pin, HIGH/LOW)`, `digitalRead(pin)`.
- Analog: `analogRead(A0)` (0‑1023), `analogWrite(9, 0..255)` for PWM pins.
- Timing: use `millis()` for non‑blocking; avoid long `delay()` in production.
- Functions: declare before use or provide prototypes in headers.
- Structs/classes: encapsulate state + behavior; prefer `.h` + `.cpp` pairs for larger projects.
- Pointers/refs: pass by reference for speed; avoid heap allocation on AVR.
- `constexpr`, `enum class`, and `inline` are your friends for clarity and zero‑cost abstractions.
