#!/usr/bin/env python3
"""Normaliza IoCs desde data/seed_iocs.txt y actualiza data/feeds.csv."""
from datetime import date
import csv
from pathlib import Path

SEVERITY_MAP = {"ip":"medium","domain":"high","url":"high","sha256":"medium"}
CONFIDENCE_DEFAULT = 70

root = Path(__file__).resolve().parent
seed_path = root / "data" / "seed_iocs.txt"
csv_path  = root / "data" / "feeds.csv"

def parse_seed_line(line: str):
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 3:
        return None
    ioc_type, value, source = parts[:3]
    # Sanea valores simples
    value = value.replace("[.]", ".")
    return {
        "date": date.today().isoformat(),
        "type": ioc_type.lower(),
        "value": value,
        "source": source,
        "confidence": CONFIDENCE_DEFAULT,
        "severity": SEVERITY_MAP.get(ioc_type.lower(), "low"),
        "country": "",
        "threat_family": "Unknown",
        "notes": ""
    }

def load_existing(csvfile):
    if not csvfile.exists():
        return []
    with open(csvfile, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_all(csvfile, rows):
    fieldnames = ["date","type","value","source","confidence","severity","country","threat_family","notes"]
    with open(csvfile, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

if __name__ == "__main__":
    existing = load_existing(csv_path)
    existing_set = {(r["type"], r["value"]) for r in existing}

    new_rows = []
    for line in seed_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        row = parse_seed_line(line)
        if not row:
            continue
        key = (row["type"], row["value"])
        if key not in existing_set:
            new_rows.append(row)

    updated = existing + new_rows
    save_all(csv_path, updated)
    print(f"Añadidas {len(new_rows)} filas nuevas. Total: {len(updated)} -> {csv_path}")
