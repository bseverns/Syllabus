# Fold & Fire — Pin-Accurate Netlist

Vref:
- 100k +5→Vref, 100k Vref→GND, 100nF Vref→GND

MCP602 (U1):
- pin 8 +5V, pin 4 GND, 100nF near pins
Input:
- IN → 100nF → IN_AC; 100k IN_AC→Vref
U1A:
- pin3=IN_AC; pin2 tied pin1; pin1=BUF
U1B:
- pin5=BUF; pin6=DRIVE_NEG; 10k DRIVE_NEG→Vref
- 100k pin7→DRIVE_NEG; pin7=DIST_OUT
Diodes across feedback:
- D1 anode pin7, cathode DRIVE_NEG
- D2 anode DRIVE_NEG, cathode pin7

CD40106 (U2):
- pin14 +5V, pin7 GND, 100nF near pins
Gate1:
- 100k DIST_OUT→pin1; pin2=GATE1_OUT
Gate2:
- 47k DIST_OUT→EDGE; 10nF EDGE→GND
- 100k EDGE→pin3; pin4=GATE2_OUT
