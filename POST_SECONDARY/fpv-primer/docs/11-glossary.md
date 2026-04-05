# Glossary

## FC
Flight controller. The board that reads receiver commands and sensor data, then computes motor outputs.

## ESC
Electronic speed controller. The power stage that drives each motor.

## RX
Receiver. The part that receives pilot commands from the radio link.

## VTX
Video transmitter. Sends FPV video to goggles or a ground receiver.

## UART
A hardware serial port on the FC. Often used for receiver, VTX control, GPS, or logging functions.

## Failsafe
The craft’s behavior when the control link becomes invalid or disappears. Must be configured and tested intentionally.

## Rates
Settings that shape how stick input turns into rotational command. They affect feel, not only “speed.”

## Blackbox
Betaflight’s flight-data recording system. Useful for post-flight analysis, replay, and proof.

## Betaflight diff
A compact export of changed Betaflight settings relative to defaults. Useful for versioning and comparison.

## Telemetry
Structured values about the state of the craft, receiver, or control system.

## Arm / disarm
Arm enables motor output. Disarm removes active flight authority. Treat these as state transitions, not habits you do casually.

## Props-off
Bench doctrine requiring prop removal during setup, verification, and debugging.

## RSSI
Received signal strength indicator. A signal-strength measure that may be less useful than LQ on modern ELRS systems.

## LQ
Link quality. On ELRS-style systems, often more useful than RSSI for judging control-link health.

## Bench replay
Re-running captured telemetry through the pipeline so changes can be compared without another flight.
