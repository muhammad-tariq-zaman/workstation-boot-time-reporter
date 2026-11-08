# workstation-boot-time-reporter

Report workstation boot times from a CSV: SLOW over a threshold (default 120 seconds), otherwise OK — slowest first, so machines needing a clean-up or SSD are obvious.

## How to run

```sh
python3 main.py boots.csv --threshold 120
```

## Example output

```
PC-12: SLOW (300 s)
PC-07: OK (45 s)
1 slow boot(s) over 120 s.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
