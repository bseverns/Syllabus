# Test Procedures (simple, repeatable)

## Loop timing
1) Flash `firmware/week01_loop_timing`
2) Run:
```bash
python host/serial_loop_logger.py --port YOUR_PORT --seconds 10 --outfile export/loop.csv
```
3) Open `labs/week01_latency_jitter.ipynb` and interpret spikes.

## Calibration
1) Flash `firmware/week04_adc_calibration`
2) Send `CAL_START`, move knob full range
3) Send `CAL_SAVE`
4) Send `SHOW` and confirm persisted min/max

## Safe mode
1) Flash `firmware/week09_diagnostics_safe_mode`
2) Hold BTN while plugging USB
3) Confirm it prints `MODE,SAFE`
