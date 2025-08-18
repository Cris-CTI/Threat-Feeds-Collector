# 🌐 Threat Intel Feeds Collector

Proyecto educativo que **normaliza y almacena IoCs** (IPs, dominios, hashes) en CSV para su análisis y visualización.

## ⚙️ ¿Qué hace?
- Carga IoCs desde `data/seed_iocs.txt` (ficticios).
- Normaliza y añade metadatos básicos (fecha, severidad, confianza).
- Actualiza `data/feeds.csv` con el histórico.
- Crea una vista previa `dashboards/preview.png` con estadísticas básicas.

## ▶️ Uso rápido
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python collector.py          # genera/actualiza data/feeds.csv
python dashboards/preview.py # (opcional) recrea el gráfico a partir del CSV
```

## 📁 Estructura
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
