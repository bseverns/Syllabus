# Build checklist (pre-flight readiness)

Run this before first flight and again after any major rebuild.

## 1. Mechanical

- frame is not cracked or twisted
- motor screws are correct length and secure
- props are the correct orientation and in good condition
- stack hardware is secure but not crushing the FC
- antennas and camera mounts have strain relief
- battery strap or mount is trustworthy

## 2. Electrical

- no obvious solder bridges or cold joints
- no pinched wires
- motor wires are clear of props
- battery lead and capacitor are secure
- smoke stopper or current limiting is ready for first power-up

## 3. Firmware and orientation

- FC target is correct
- board orientation matches physical build
- accelerometer or gyro behavior is believable
- arming logic is not bypassing obvious safety checks

## 4. Receiver and radio

- receiver protocol is correct
- channel map matches transmitter
- endpoints are sane
- arming switch is intentional
- failsafe is proven, not assumed

## 5. Video and OSD

- camera image is stable
- VTX antenna is attached before power-up
- OSD shows at least the key fields you need
- channel / power plan is known if other systems are active nearby

## 6. Logging and telemetry

- blackbox is enabled if the FC supports it
- serial telemetry or export path is configured if needed
- one short capture path has already been tested

## 7. Bench proof

Before field power with props:

1. props off
2. power safely
3. verify receiver movement
4. verify motor outputs in the expected order and direction
5. verify failsafe behavior
6. save config export or diff

End with the only acceptable pre-flight sentence:

**Bench proves it first.**
