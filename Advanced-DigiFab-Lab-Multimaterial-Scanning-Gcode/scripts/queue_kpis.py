"""Aggregate queue KPIs from print-queue-log.csv
Usage: python queue_kpis.py data/print-queue-log.csv
Outputs: success rate, average runtime estimate, pause count.
"""
import sys, csv

def main(path):
    total = 0
    success = 0
    pauses = 0
    time_sum = 0.0
    with open(path, newline='', encoding='utf-8') as f:
        r = csv.DictReader(f)
        for row in r:
            total += 1
            if row.get('result','').strip().lower() in ('pass','ok','success','done'):
                success += 1
            try:
                time_sum += float(row.get('est_time',0))
            except:
                pass
            try:
                pauses += int(row.get('pauses',0))
            except:
                pass
    print('Jobs:', total)
    print('Success rate:', f'{(success/total*100 if total else 0):.1f}%')
    print('Avg est time:', f'{(time_sum/total if total else 0):.1f}')
    print('Total pauses:', pauses)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python queue_kpis.py data/print-queue-log.csv')
        sys.exit(1)
    main(sys.argv[1])
