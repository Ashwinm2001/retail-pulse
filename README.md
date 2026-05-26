<div align="center">

<img src=""C:\Users\ashwi\retail-pulse\dashboard_images\retail_pulse.png"" alt="Retail Pulse Dashboard Preview" width="100%" style="border-radius:8px;" />

<br/><br/>

# 🏪 Retail Pulse
### Real-Time Retail Intelligence & Anomaly Detection Platform

<br/>

<!-- Tech stack badges — these auto-render on GitHub -->
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-Cloud_Warehouse-4285F4?style=flat-square&logo=googlebigquery&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Direct_Query-F2C811?style=flat-square&logo=powerbi&logoColor=black)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![SendGrid](https://img.shields.io/badge/SendGrid-Email_Alerts-1A82E2?style=flat-square&logo=twilio&logoColor=white)
![Cloud Run](https://img.shields.io/badge/Cloud_Run-Deployed-4285F4?style=flat-square&logo=googlecloud&logoColor=white)

<br/>


</div>

---

## 📌 The Problem This Solves

> Retail companies lose millions every year — not because their data doesn't exist, but because nobody sees it in time.

A revenue crash on Monday morning gets noticed on Wednesday in the weekly report. A product category bleeding profit goes undetected for a full quarter. The executive dashboard shows yesterday's numbers because the data refresh broke silently at 2am and nobody knew.

**Retail Pulse** is an end-to-end analytics platform built to solve all three problems simultaneously:

| Pain Point | Before | After Retail Pulse |
|---|---|---|
| Revenue anomaly detection | Found in weekly review (24–72 hrs later) | Email alert in **< 15 minutes** |
| Dashboard stale data | Detected when someone complains | Health monitor fires **automatically** |
| Customer churn signals | Manual spreadsheet analysis monthly | Live RFM segmentation, always fresh |
| Sales forecasting | Gut feel or static Excel model | Prophet ML model with 90-day horizon |
| Executive reporting | Manual exports, emailed CSVs | Self-updating live dashboard, anytime |

---

<div align="center">


</div>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        RETAIL PULSE ARCHITECTURE                     │
└─────────────────────────────────────────────────────────────────────┘

  📦 DATA SOURCES                📡 INGESTION               ☁️ CLOUD WAREHOUSE
  ┌──────────────┐              ┌──────────────┐            ┌──────────────────┐
  │ Kaggle CSV   │──────────────▶              │            │   Google BigQuery │
  │ (Historical) │              │  Python      │───────────▶│                  │
  └──────────────┘              │  generator   │            │  ┌─────────────┐ │
                                │  + scheduler │            │  │ fact_sales  │ │
  ┌──────────────┐              │              │            │  │ dim_product │ │
  │ Faker Engine │──────────────▶  Cloud Run   │            │  │ dim_customer│ │
  │ (Live POS    │              │  15-min cron │            │  │ dim_date    │ │
  │  simulation) │              └──────────────┘            │  │ dim_store   │ │
  └──────────────┘                                          │  │ rfm_segments│ │
                                                            │  │ anomaly_log │ │
                                                            │  │ alert_log   │ │
  🧠 ANALYTICS                  🔔 ALERTS                   └──────────────────┘
  ┌──────────────┐              ┌──────────────┐                     │
  │ Python       │              │ check_alerts │                     │
  │ Notebooks    │              │ .py          │◀────────────────────┘
  │              │              │              │
  │ • EDA        │              │ • Revenue    │            📊 DASHBOARD
  │ • RFM model  │              │   spike/drop │            ┌──────────────────┐
  │ • Prophet    │              │ • Inventory  │            │   Power BI       │
  │   forecast   │──────────────▶  risk        │            │   (Direct Query) │
  │ • Anomaly    │              │ • Dashboard  │            │                  │
  │   detection  │              │   health     │            │  5 Report Pages  │
  └──────────────┘              │              │◀───────────│  + RLS Security  │
                                │ SendGrid     │            └──────────────────┘
                                │ HTML Emails  │
                                └──────────────┘
```

---

## ✨ Key Features

### 📊 Live Power BI Dashboard (Direct Query)
- **5 report pages**: Executive Summary, Product Performance, Regional Heatmap, Customer Segments, Anomaly Log
- **Direct Query mode** — no data import, always querying live BigQuery data
- **Row-Level Security** — store managers see only their region's data
- **DAX measures** — rolling averages, period-over-period comparisons, dynamic KPIs

### 🔔 Intelligent Alert System
- **Revenue spike alert** — fires when daily revenue exceeds 30% above 7-day rolling average
- **Revenue crash alert** — fires when daily revenue drops more than 20% below average
- **Inventory risk alert** — flags product categories with profit margin below 5%
- **Dashboard health monitor** — pings Power BI REST API every 15 minutes; emails on failure
- **Anomaly detection alert** — fires when Z-score on daily revenue exceeds ±2σ
- All alerts delivered as **colour-coded HTML emails** via SendGrid

### 🧠 Python Analytics Engine
- **RFM customer segmentation** — scores every customer on Recency, Frequency, Monetary value
- **90-day Prophet forecast** — time-series model with weekly and yearly seasonality
- **Statistical anomaly detection** — Z-score based flagging of unusual revenue days
- **Exploratory analysis** — category profitability, regional trends, discount impact analysis

### ☁️ Cloud-Native Pipeline
- **BigQuery star schema** — fact_sales + 4 dimension tables + materialized views
- **Streaming inserts** — new transactions pushed to BigQuery every 15 minutes via Cloud Run
- **Cloud Scheduler** — fully automated, runs 24/7 without manual intervention
- **GitHub Actions CI/CD** — automatic linting and formatting check on every push

---

## 🗂️ Project Structure

```
retail-pulse/
│
├── src/
│   ├── ingestion/
│   │   └── generator.py          # Faker-based live transaction simulator
│   ├── transformation/
│   │   └── build_schema.py       # Python script to orchestrate BigQuery schema build
│   └── alerts/
│       └── check_alerts.py       # Alert engine — all 5 alert types + email delivery
│
├── sql/
│   ├── create_dim_date.sql        # Date dimension — 2020 to 2026
│   ├── create_dim_product.sql     # Product dimension
│   ├── create_dim_customer.sql    # Customer dimension
│   ├── create_dim_store.sql       # Store/region dimension
│   ├── create_fact_sales.sql      # Central fact table with all foreign keys
│   ├── create_views.sql           # Materialized views for dashboard performance
│   └── anomaly_detection.sql      # Scheduled query for anomaly log population
│
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb     # EDA — category, region, time trends
│   ├── 02_rfm_segmentation.ipynb         # RFM scoring and segment labelling
│   ├── 03_forecasting.ipynb              # Prophet 90-day sales forecast
│   └── 04_anomaly_detection.ipynb        # Z-score anomaly detection
│
├── dashboards/
│   └── retail_pulse.pbix          # Power BI Desktop file (Direct Query)
│
├── docs/
│   ├── screenshots/               # Dashboard page screenshots
│   ├── data_dictionary.xlsx       # Column-level documentation for all 5 tables
│   └── analysis_summary.xlsx      # Plain-English business findings from notebooks
│
├── .github/
│   └── workflows/
│       └── lint.yml               # GitHub Actions — flake8 + black on every push
│
├── .env.example                   # Template showing required environment variables
├── .gitignore                     # Excludes .env, keys, __pycache__, venv
├── requirements.txt               # All Python dependencies with pinned versions
└── README.md                      # This file
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python 3.11 | Data ingestion, analytics, alerts |
| Cloud Warehouse | Google BigQuery | Star schema, streaming inserts, SQL analytics |
| Dashboard | Power BI (Direct Query) | Live executive reporting, RLS |
| Orchestration | Google Cloud Run + Scheduler | 24/7 automated pipeline |
| Alerting | SendGrid API | HTML email delivery |
| Version Control | Git + GitHub | Source control, CI/CD |
| CI/CD | GitHub Actions | Auto linting on every push |
| Data Generation | Python Faker | Realistic live transaction simulation |
| Forecasting | Facebook Prophet | 90-day time-series forecast |
| Anomaly Detection | SciPy (Z-score) | Statistical outlier detection |
| Segmentation | Pandas + BigQuery ML | RFM customer scoring |
| Notebook IDE | Jupyter | Exploratory analysis |
| Email Template | HTML + Jinja2 | Colour-coded alert emails |

---

## ⚙️ Setup & Installation

### Prerequisites

Before starting, make sure you have:
- Python 3.11+ installed
- A Google Cloud account (free tier works — $300 credit available)
- A SendGrid account (free tier — 100 emails/day)
- Power BI Desktop installed (Windows; or use a VM on Mac)
- Git installed

### Step 1 — Clone the repository

```bash
git clone https://github.com/🔧YOUR-GITHUB-USERNAME/retail-pulse.git
cd retail-pulse
```

### Step 2 — Create and activate virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Mac/Linux
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables

```bash
# Copy the template
cp .env.example .env

# Open .env and fill in your values
nano .env   # or open in VS Code
```

Your `.env` file should contain:

```env
# 🔧 Google Cloud
GCP_PROJECT_ID=your-project-id
BIGQUERY_DATASET=retail_pulse
GOOGLE_APPLICATION_CREDENTIALS=path/to/your/service-account-key.json

# 🔧 SendGrid
SENDGRID_API_KEY=your-sendgrid-api-key
ALERT_FROM_EMAIL=alerts@yourdomain.com
ALERT_TO_EMAIL=your-email@gmail.com

# 🔧 Power BI REST API (for dashboard health monitor)
PBI_CLIENT_ID=your-azure-app-client-id
PBI_CLIENT_SECRET=your-azure-app-client-secret
PBI_TENANT_ID=your-azure-tenant-id
PBI_DATASET_ID=your-powerbi-dataset-id
```

### Step 5 — Build the BigQuery schema

```bash
# Run all SQL files in order
python src/transformation/build_schema.py
```

This creates all 5 tables, materialized views, and seeds the schema.

### Step 6 — Upload historical data

```bash
# Upload Superstore CSV to BigQuery raw layer
python src/ingestion/upload_data.py --file data/superstore.csv
```

### Step 7 — Run the analytics notebooks

Open Jupyter and run all 4 notebooks in order:

```bash
jupyter notebook
```

Run: `01_exploratory_analysis.ipynb` → `02_rfm_segmentation.ipynb` → `03_forecasting.ipynb` → `04_anomaly_detection.ipynb`

Each notebook writes its output back to BigQuery automatically.

### Step 8 — Start the live data generator

```bash
# Streams 3–8 new transactions every 15 minutes
python src/ingestion/generator.py

# To inject a revenue spike for testing alerts
python src/ingestion/generator.py spike

# To simulate a revenue crash
python src/ingestion/generator.py crash
```

### Step 9 — Run the alert engine

```bash
# Run all alert checks once manually
python src/alerts/check_alerts.py

# The alert engine also runs automatically via Cloud Scheduler
# See deployment instructions below
```

### Step 10 — Connect Power BI

1. Open `dashboards/retail_pulse.pbix` in Power BI Desktop
2. When prompted, sign in with your Google Cloud credentials
3. Verify **DirectQuery** mode is active (check the bottom status bar)
4. All 5 pages should load with your live data

---

## ☁️ Cloud Deployment

### Deploy generator to Cloud Run

```bash
# Build and deploy
gcloud run deploy retail-pulse-generator \
  --source . \
  --region us-central1 \
  --set-env-vars GCP_PROJECT_ID=your-project-id

# Schedule it every 15 minutes via Cloud Scheduler
gcloud scheduler jobs create http retail-pulse-stream \
  --schedule="*/15 * * * *" \
  --uri="https://YOUR-CLOUD-RUN-URL/stream" \
  --location=us-central1
```

### Deploy alert engine to Cloud Run

```bash
gcloud run deploy retail-pulse-alerts \
  --source . \
  --region us-central1 \
  --set-env-vars GCP_PROJECT_ID=your-project-id,SENDGRID_API_KEY=your-key

# Schedule alerts every 15 minutes
gcloud scheduler jobs create http retail-pulse-alerts \
  --schedule="*/15 * * * *" \
  --uri="https://YOUR-ALERTS-CLOUD-RUN-URL/check" \
  --location=us-central1
```

---

## 📊 Dashboard Pages

| Page | Description | Key Visuals |
|---|---|---|
| 1. Executive Summary | Top-level KPIs and revenue trends | KPI cards, revenue line chart, top 10 products |
| 2. Product Performance | Category and SKU deep-dive | Matrix with drill-through, margin scatter plot |
| 3. Regional Heatmap | Geographic revenue distribution | Filled map, region ranking, city KPI |
| 4. Customer Segments | RFM cohort analysis | Segment donut, LTV trends, Champion customer table |
| 5. Anomaly Log | Live alert and anomaly history | Colour-coded alert table with timestamps and severity |

<!-- 🔧 Add screenshots of each page here -->
<!-- Format: ![Page Name](docs/screenshots/page_name.png) -->

---

## 🔔 Alert System

The system monitors 5 conditions every 15 minutes:

```
Condition                    Threshold              Email Colour
─────────────────────────────────────────────────────────────
Revenue spike                > +30% vs 7-day avg    Green  ✅
Revenue drop                 < -20% vs 7-day avg    Red    🔴
Inventory risk               Margin < 5%            Amber  🟡
Dashboard health failure     Refresh failed or      Red    🔴
                             > 2 hours stale
Geographic anomaly           Region revenue         Amber  🟡
                             Z-score > ±2σ
```

Every triggered alert is also logged to `retail_pulse.alert_log` in BigQuery, which feeds the live Anomaly Log page in Power BI.

---

## 📈 Business Results

<!-- 🔧 Fill in your actual results after building and running the system -->
<!-- These numbers make the README powerful — measure them during your demo -->

| Metric | Result |
|---|---|
| Time to detect revenue anomaly | **Reduced from 24–72 hrs → < 15 minutes** |
| Dashboard data freshness | **Always live (Direct Query, no import delay)** |
| Dashboard failure detection | **Automated — no manual checking required** |
| Customer segments identified | **🔧 ADD: e.g. 4 segments across X customers** |
| Forecast accuracy (MAPE) | **🔧 ADD: e.g. ~12% Mean Absolute Percentage Error** |
| Alert types monitored | **5 alert types, running 24/7 automatically** |

---

## 🧪 Running Tests

```bash
# Lint check (also runs automatically on every GitHub push)
flake8 src/ --max-line-length=100

# Format check
black src/ --check

# Auto-format all files
black src/

# Run unit tests
pytest tests/ -v
```

---

## 🗺️ Roadmap

- [x] BigQuery star schema with streaming inserts
- [x] Power BI Direct Query dashboard — 5 pages
- [x] 5-alert email system with HTML templates
- [x] Power BI dashboard health monitor
- [x] RFM customer segmentation
- [x] Prophet 90-day sales forecast
- [x] Row-level security for regional managers
- [x] GitHub Actions CI/CD pipeline
- [ ] 🔧 AI-generated weekly insight summary (LLM integration — planned)
- [ ] 🔧 Slack alert delivery as alternative to email (planned)
- [ ] 🔧 Automated A/B test analysis for promotions (planned)
- [ ] 🔧 Mobile-optimised Power BI layout (planned)

---

## 📁 Data Dictionary

Full column-level documentation is available in [`docs/data_dictionary.xlsx`](docs/data_dictionary.xlsx).

Quick reference — `fact_sales` table:

| Column | Type | Description |
|---|---|---|
| `order_id` | STRING | Unique order identifier |
| `date_key` | INT64 | Foreign key to dim_date (YYYYMMDD format) |
| `product_key` | INT64 | Foreign key to dim_product |
| `customer_key` | INT64 | Foreign key to dim_customer |
| `store_key` | INT64 | Foreign key to dim_store |
| `revenue` | FLOAT64 | Gross sales revenue |
| `profit` | FLOAT64 | Net profit after cost of goods |
| `units_sold` | INT64 | Quantity of items in this order |
| `discount_pct` | FLOAT64 | Discount applied (0.0 to 1.0) |
| `profit_margin_pct` | FLOAT64 | Profit as % of revenue |

---

## 🤝 Contributing

Contributions, suggestions, and issue reports are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add: your feature description'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 🙋 About the Author

<!-- 🔧 Fill in your own details below -->

**[ASHWIN M]**

<!-- 🔧 Write 2–3 sentences about yourself — your background, what you're looking for, and why you built this -->
> [Aspiring Data Analyst passionate about transforming raw data into meaningful business insights. Skilled in Python, SQL, Machine Learning, Generative AI, Power BI, Google BigQuery, AWS Cloud, and data visualization, with a strong interest in building end-to-end analytics and automation solutions. Built Retail Pulse to demonstrate real-world analytical thinking — from live data ingestion and cloud warehousing to anomaly detection, forecasting, and executive dashboards.]

<!-- 🔧 Add your real links -->
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/ashwinm2001/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/Ashwinm2001)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat-square&logo=gmail&logoColor=white)](ashwin2001hitech@gmail.com)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

*Built with Python · BigQuery · Power BI · SendGrid · GitHub Actions*

<!-- 🔧 Optional: Add your city/country here -->
*[KOZHIKODE, INDIA] · [2024]*

</div>