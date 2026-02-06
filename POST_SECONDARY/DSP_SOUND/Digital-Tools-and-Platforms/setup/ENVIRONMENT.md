# Python Environment (for logging + analysis)

We use Python only for *observing* what the microcontroller is doing.

## Install
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m ipykernel install --user --name digital-tools --display-name "Digital Tools"
```

## Log Serial to CSV
```bash
python scripts/serial_logger.py --port YOUR_PORT --baud 115200 --outfile export/week01.csv
```

## Plot CSV
```bash
python scripts/plot_csv.py export/week01.csv
```
