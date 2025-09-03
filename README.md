<img width="980" height="382" alt="intel feeds collector" src="https://github.com/user-attachments/assets/0207ee18-9be3-4e23-abc4-08a0176b3562" />


# 1. Threat Intel Feeds Collector

![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/status-active-success)

**Threat Intel Feeds Collector** is an educational project that collects, normalizes, and stores Indicators of Compromise (**IoCs**) such as IP addresses, domains, and hashes.  
The processed data is stored in CSV format and can be analyzed and visualized with **Power BI**.

*This project is intended for educational and training purposes in Cyber Threat Intelligence (CTI)*

---

## 2. Features

- 2.1 **IoC Collection**
  - From seed file (`data/seed_iocs.txt`)
  - (Optional) From public threat intel feeds (`URLhaus`, `FeodoTracker`)
- 2.2 **Normalization**
  - Automatic classification (`ip`, `domain`, `hash`)
  - Hash type detection (MD5, SHA1, SHA256)
- 2.3 **Storage**
  - Updates and maintains `data/feeds.csv` as a historical dataset
  - Metadata included: `run_id`, `collected_at`, `source`, `severity`, `confidence`, `tags`
- 2.4 **Visualization**
  - Interactive **Power BI dashboard**. Designed to help analysts quickly identify hotspots, high severity IoCs, and source reliability. Showing:
    - Severity distribution (low / medium / high)
    - Trends by date (`collected_at`)
    - IoC type distribution (`ip`, `domain`, `hash`)
    - Threat tags (`malware`, `botnet-c2`, etc.)

---

## 3. Quick Start

```bash
# 1. Clone repository
git clone https://github.com/Cris-CTI/Threat-Feeds-Collector.git
cd Threat-Feeds-Collector

# 2. Create virtual environment
python -m venv .venv
# Linux/Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run collector
python collector.py
[+] Starting IoC collection…
[OK] Added X records to data/feeds.csv

```

👉 The generated dataset will be stored in:
data/feeds.csv and can be directly imported into Power BI

---

## 4. Power BI Dashboard

The normalized data can be explored with the included Power BI dashboard located in the dashboards/ folder.

#### - 4.1 Overview
- Full overview of the Power BI dashboard, showing all charts together. This view allows a quick understanding of the collected IoCs, their types, severities, and overall distribution at a glance.

<img width="1155" height="655" alt="dashboard_overview" src="https://github.com/user-attachments/assets/581dfb85-7362-4f8a-a735-a1996063dce2" />

#### - 4.2 IoC Type Distribution (IP, Domain & Hash)
- Distribution of collected IoCs by type. It shows the proportion of IP addresses, domain names, and hashes, helping to identify which type of indicators are most common in the dataset.
  
*(Domain)*

<img width="600" alt="dashboard_types_domain" src="https://github.com/user-attachments/assets/46641608-429b-4143-b1d9-7914ddb2944f" />

*(Hash)*

<img width="600" alt="dashboard_types_hash" src="https://github.com/user-attachments/assets/6568193e-ff16-4189-84f5-672d5fa88d44" />


*(IP)*

<img width="600" alt="dashboard_types_ip" src="https://github.com/user-attachments/assets/90791de2-9ea9-43b2-a11c-81b422f03f50" />

#### - 4.3 Severity Distribution (Low / Medium / High)
- Counts of IoCs grouped by severity level. This chart highlights which indicators pose the highest risk, helping prioritize monitoring or response actions.

<img width="600" alt="dashboard_severity" src="https://github.com/user-attachments/assets/4fc84782-00e2-4a9d-aca8-f831c6fd023b" />

#### - 4.4 IoC Distribution by Source / Tags
- Shows the number of IoCs grouped by their source (e.g., seed file, FeodoTracker) and categorized by threat tags (e.g., botnet-c2).  
- This visualization is useful to understand both **where the indicators come from** and **what type of threats they represent**.

<img width="600" alt="dashboard_tags" src="https://github.com/user-attachments/assets/16ba9cb4-669e-4d25-8dbd-1ac9a137869d" />

---

## 5. Repository Structure

```bash
Threat-Feeds-Collector/
├── collector.py              # Main collector script
├── dashboards/               # Power BI dashboards and screenshots
│   ├── dashboard_overview.png
│   ├── dashboard_types_domain.png
│   ├── dashboard_types_hash.png
│   ├── dashboard_types_ip.png
│   ├── dashboard_severity.png
│   └── dashboard_tags.png
├── data/
│   ├── seed_iocs.txt         # Example/fake IoCs
│   └── feeds.csv             # Generated dataset
├── requirements.txt          # Python dependencies
├── LICENSE                   # Project license (MIT)
└── README.md                 # Project documentation

```
## 6. Example Usage

### Collector run

```bash
$ python collector.py
[+] Starting IoC collection…
[INFO] Remote feeds disabled (DISABLE_REMOTE_FEEDS=1)
[OK] Added 7 records to data/feeds.csv
[SUMMARY] By type: {'ip': 2, 'domain': 2, 'hash': 3}


Quick analysis with Pandas
import pandas as pd

# Load dataset
df = pd.read_csv("data/feeds.csv")

# Check IoC severity distribution
print(df["severity"].value_counts())

# Count IoCs by type
print(df["type"].value_counts())


```
## 7. Roadmap

Planned improvements and future work for this project:

- **Additional threat intel feeds**  
  Integrate new public feeds such as AlienVault OTX and AbuseIPDB to enrich the dataset.

- **Extended export formats**  
  Support exporting the collected IoCs to formats beyond CSV, including JSON and Parquet.

- **Web-based visualization**  
  Develop an interactive dashboard with Streamlit to allow real-time exploration of IoCs directly from a browser.

---

## 8. License

This project is licensed under the MIT License.

---

## 9. Author

Cris-CTI
- LinkedIn -> https://www.linkedin.com/in/cristina-martinez-campos/ 
- GitHub -> https://github.com/Cris-CTI
