"""Report workstation boot times and flag slow starters.

Usage: python3 main.py boots.csv [--threshold 120]
CSV columns: host,boot_seconds.
SLOW when boot time is over the threshold (default 120 seconds),
otherwise OK. Slowest boot first.
"""
import argparse, csv, sys

def report(rows, threshold=120):
    out = []
    for row in rows:
        seconds = int(row["boot_seconds"])
        verdict = "SLOW" if seconds > threshold else "OK"
        out.append((row["host"].strip(), seconds, verdict))
    return sorted(out, key=lambda r: -r[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--threshold", type=int, default=120)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        results = report(list(csv.DictReader(f)), args.threshold)
    for host, seconds, verdict in results:
        print(f"{host}: {verdict} ({seconds} s)")
    print(f"{sum(1 for *_, v in results if v == 'SLOW')} slow boot(s) over {args.threshold} s.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
