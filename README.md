# Threat Intel Feeds Collector

Educational project that normalizes and stores IoCs (IPs, domains, hashes) in CSV format for analysis and visualization.

## What it does?
- Loads IoCs from data/seed_iocs.txt (sample/fake data).
- Normalizes them and adds basic metadata (date, severity, confidence).
- Updates data/feeds.csv with historical records.
- Creates a preview dashboards/preview.png with basic statistics.

## Uso rápido
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python collector.py          # generates/updates data/feeds.csv
python dashboards/preview.py # (optional) recreates the chart from the CSV
```

## Structure
```
Threat-Feeds-Collector/
├── collector.py
├── dashboards/
│   ├── preview.py
│   └── preview.png
├── data/
│   ├── seed_iocs.txt
│   └── feeds.csv
├── requirements.txt
├── LICENSE
└── README.md
```
