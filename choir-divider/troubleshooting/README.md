# Troubleshooting — Choir Divider

## No clock (nothing blinks)
- 555: pin 8=+5, pin 1=GND, pin 4=+5
- pins 2 and 6 tied
- timing cap correct node and polarity (+ to node)
- try different timing cap if too fast/slow

## 4017 not counting
- 4017: pin 16=+5, pin 8=GND
- pin 13 is LOW (to GND)
- reset pin 15 is LOW (pull-down)
- clock reaches pin 14

## Weird / double triggers
- add/verify 100nF decoupling near 4017
- use 40106 cleanup
- shorten clock wiring

## Early reset fails
- diode direction for reset: anode at Q, cathode at RESET
- add 100k pull-down on RESET

## Pattern always HIGH
- 100k pull-down at PATTERN present
- OR diode direction: anode at Q, cathode at PATTERN
