"""Simple G-code scanner
- Extracts time/filament estimates (if commented), pause points, and M600 inserts.
- Usage: python gcode_scan.py path/to/file.gcode
"""
import sys, re, pathlib, csv

def scan(path):
    pauses = []
    est_time = None
    est_filament = None
    for ln, line in enumerate(path.read_text(encoding='utf-8', errors='ignore').splitlines(), 1):
        if 'M600' in line or re.search(r'\bM0\b|\bM25\b|\bM601\b', line):
            pauses.append((ln, line.strip()))
        if 'TIME:' in line or 'TIME_MS' in line:
            m = re.search(r'TIME[:=]\s*(\d+)', line)
            if m: est_time = int(m.group(1))
        if 'Filament used' in line or 'filament used' in line.lower():
            m = re.search(r'([0-9.]+)\s*m', line)
            if m: est_filament = float(m.group(1))
    return {'pauses': pauses, 'est_time_s': est_time, 'est_filament_m': est_filament}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python gcode_scan.py file.gcode')
        sys.exit(1)
    p = pathlib.Path(sys.argv[1])
    if not p.exists():
        print('File not found:', p)
        sys.exit(1)
    info = scan(p)
    print('Estimated time (s):', info['est_time_s'])
    print('Estimated filament (m):', info['est_filament_m'])
    print('Pauses:')
    for ln, txt in info['pauses']:
        print(f'  line {ln}: {txt}')
