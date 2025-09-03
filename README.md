# 🛡️ Threat Intel Feeds Collector

![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Status](https://img.shields.io/badge/status-active-success)

**Threat Intel Feeds Collector** is an educational project that collects, normalizes, and stores Indicators of Compromise (**IoCs**) such as IP addresses, domains, and hashes.  
The processed data is stored in CSV format and can be analyzed and visualized with **Power BI**.

---

## 📌 Features

- 🔎 **IoC Collection**
  - From seed file (`data/seed_iocs.txt`)
  - (Optional) From public threat intel feeds (`URLhaus`, `FeodoTracker`)
- 🧹 **Normalization**
  - Automatic classification (`ip`, `domain`, `hash`)
  - Hash type detection (MD5, SHA1, SHA256)
- 🗂️ **Storage**
  - Updates and maintains `data/feeds.csv` as a historical dataset
  - Metadata included: `run_id`, `collected_at`, `source`, `severity`, `confidence`, `tags`
- 📊 **Visualization**
  - Interactive **Power BI dashboard** showing:
    - Severity distribution (low / medium / high)
    - Trends by date (`collected_at`)
    - IoC type distribution (`ip`, `domain`, `hash`)
    - Threat tags (`malware`, `botnet-c2`, etc.)

---

## ⚡ Quick Start

```bash
# 1. Clone repository
git clone https://github.com/yourusername/Threat-Feeds-Collector.git
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
```

👉 The generated dataset will be stored in:
data/feeds.csv

---

📊 Power BI Dashboard
The normalized data can be explored with the included Power BI dashboard located in the dashboards/ folder.

Example:

💡 Replace preview.png with real screenshots of your Power BI dashboard (e.g. dashboard1.png, dashboard2.png).
This is what gives the repository a truly professional look.

---

📂 Repository Structure
bash
Copiar código
Threat-Feeds-Collector/
├── collector.py              # Main collector script
├── dashboards/
│   ├── preview.py            # Simple matplotlib preview (optional)
│   └── preview.png           # Dashboard example
├── data/
│   ├── seed_iocs.txt         # Example/fake IoCs
│   └── feeds.csv             # Generated dataset
├── requirements.txt          # Python dependencies
├── LICENSE
└── README.md
✅ Example Usage
Collector run
bash
Copiar código
$ python collector.py
[+] Starting IoC collection…
[INFO] Remote feeds disabled (DISABLE_REMOTE_FEEDS=1)
[OK] Added 7 records to data/feeds.csv
[SUMMARY] By type: {'ip': 2, 'domain': 2, 'hash': 3}
Quick analysis with Pandas
python
Copiar código
import pandas as pd
df = pd.read_csv("data/feeds.csv")
print(df["severity"].value_counts())
---

🧪 Tests
bash
Copiar código
python -m pytest
✔️ All unit tests passing:
---

🚀 Roadmap
- Add integration with additional public feeds (AlienVault OTX, AbuseIPDB).

- Export to additional formats (JSON, Parquet).

- Interactive dashboard with Streamlit for web visualization.

---

📜 License
This project is licensed under the MIT License.
---
👤 Author
Cris-CTI
🔗 LinkedIn · GitHub

---
