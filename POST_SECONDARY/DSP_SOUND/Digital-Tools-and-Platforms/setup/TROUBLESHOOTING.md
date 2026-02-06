# Troubleshooting

## Upload fails
- Wrong board selected in Arduino IDE
- Cable is charge-only (swap cable)
- Permissions (Linux): add user to `dialout` group

## Serial monitor garbage
- Baud mismatch. Most sketches use 115200.

## Nothing shows up in Serial Monitor
- Your sketch may not be printing
- Some boards reset on Serial open; wait 1–2 seconds

## Sensor readings jumpy
- Add smoothing (EMA), add hysteresis, check wiring and power noise.
