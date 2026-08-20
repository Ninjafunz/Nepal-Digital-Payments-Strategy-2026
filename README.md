# From Cash to Platforms

## The Transformation of Nepal's Digital Payments Industry, 2021–2026

**Research Project**

---

> **Core Research Question:** How is digitalization changing the basis of competition and the distribution of economic value in Nepal's payments ecosystem?

This is not a "digital payments are growing" report. This is a strategic analysis of **who is gaining power, why, and who is positioned to capture the next profit pool**.

---

## What This Project Demonstrates

| Dimension | Description |
|-----------|-------------|
| **Strategic thinking** | Applying Porter's Five Forces, PvP, and scenario analysis to a real industry |
| **Industry analysis** | Structured understanding of Nepal's payments landscape |
| **Competitive dynamics** | How banks, wallets, PSPs, and infrastructure providers compete |
| **Quantitative research** | Rigorous data collection from official NRB sources |
| **Data engineering** | Traceable, auditable data pipeline with full provenance |
| **Evidence-based recommendations** | Strategic insights grounded in data, not opinion |

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/Nepal-Digital-Payments-Strategy-2026.git
cd Nepal-Digital-Payments-Strategy-2026

# Install dependencies
pip install -r requirements.txt

# Rebuild monthly CSV from the NRB XLSX (requires sources/NRB_PSD_Sep2025_REAL.xlsx)
python src/ingestion/extract_xlsx_v2.py

# Load the database
python src/ingestion/load_nrb_indicators.py

# Run all analyses
python src/analysis/run_all_analyses.py
```

---

## Repository Structure

```
Nepal-Digital-Payments-Strategy-2026/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── LICENSE                            # MIT License
│
├── research/                          # Research architecture
│   ├── research_question.md           # Formal questions, scope, definitions
│   ├── hypotheses.md                  # 14 testable hypotheses
│   ├── methodology.md                 # Research constitution & data hierarchy
│   ├── data_dictionary.md             # 91 variables across 10 sections
│   ├── source_register.md             # Living register of all sources
│   ├── nrb_data_inventory.md          # NRB dataset inventory
│   └── analysis_plan.md              # Step-by-step analysis mapping
│
├── data/
│   ├── raw/                           # Unprocessed data (excluded from repo)
│   ├── processed/                     # Cleaned data
│   └── final/                         # Analysis-ready datasets
│
├── database/
│   ├── payments.db                    # SQLite database (excluded from repo)
│   └── schema.md                      # Database schema documentation
│
├── sources/                           # Source documents and extraction scripts
│   ├── bank_registry.csv              # 20+ banks with merger history
│   ├── data_dictionary.md             # Variable definitions
│   ├── config.yaml                    # Project configuration
│   ├── access_attempts_log.md         # NRB access audit trail
│   └── *.pdf                          # NRB reports (excluded from repo)
│
├── src/
│   ├── ingestion/
│   │   ├── extract_xlsx_v2.py         # XLSX → monthly CSV (skips FY totals)
│   │   └── load_nrb_indicators.py     # Database loading script
│   └── analysis/
│       └── run_all_analyses.py        # All 5 core analyses
│
├── analysis/
│   ├── data_quality_report.md         # FY-total extraction audit
│   └── charts/                        # Generated visualizations
│       ├── 01_total_digital_growth.png
│       ├── 02_channel_value_shares.png
│       ├── 02b_qr_growth.png
│       ├── 03_user_engagement.png
│       ├── 04_hhi_concentration.png
│       └── 05_channel_positioning.png
│
├── agents/                            # AI agent configurations
│   ├── data-researcher.md
│   ├── data-engineer.md
│   ├── source-auditor.md
│   ├── strategy-analyst.md
│   └── visualization-analyst.md
│
├── notebooks/                         # Jupyter notebooks (future)
├── dashboard/                         # Dashboard specs (future)
└── report/                            # Paper sections (future)
```

---

## Data Sources

### Primary: Nepal Rastra Bank (NRB)

| Dataset | Coverage | Variables |
|---------|----------|-----------|
| **Payment Systems Indicators** (XLSX) | Jul 2020 – Jul 2025 | 49 variables, 61 months |
| Bank Supervision Reports (PDF) | 2019–2025 | Bank-level financial data |
| Payment System Directives | 2021–2026 | Regulatory timeline |

### Source Hierarchy

```
Tier 1: NRB Official Statistics (Payment Systems Indicators)
Tier 2: Audited Company Financial Statements
Tier 3: Company Disclosures
Tier 4: Regulatory Publications
Tier 5: Reputable Secondary Sources
Tier 6: News and Media
Tier 7: Analyst Inference
```

**Every observation in the database has a `source_id` linking to the source register.**

---

## Key Findings (Preliminary)

Figures below use the **corrected** monthly extract (FY total columns skipped). The original CSV mixed annual totals into monthly series; see `analysis/data_quality_report.md`. Calendar years are Gregorian labels of `date_ad`. **All-channel** totals include ATM cash, ECC (cheques), and RTGS; they are reported-channel activity and may double-count overlapping rails.

### 1. Nepal is Becoming More Digital
- All NRB-reported channels: **0.57B (2021) → 1.71B (2024)** transaction count — about **3×** (CAGR **44.6%**)
- Digital retail (excl. ATM cash, ECC, RTGS): **0.46B → 1.56B** — CAGR **50.0%**
- QR value grew **219%** in calendar 2022 (corrected series)

### 2. Two-Layer Market Emerging
| Layer | Channels | Avg Transaction (2021–Jul 2025) | Growth |
|-------|----------|----------------------------------|--------|
| **High-value** | Mobile banking, internet banking | ~NPR 7,300 (mobile); internet much higher | Steady |
| **High-frequency** | Wallet, QR, POS | ~NPR 1,100–5,000 | Strong |

### 3. Engagement Depth Varies by Channel
- **Mobile banking**: transactions/user **0.52 → 2.26** (first vs last month in the series)
- **Wallet**: about **1.62** transactions/user — flat engagement, growing user base

### 4. QR Payments Are Transforming Retail
- QR transaction count: **195K/month (Jul 2020) → 40.9M/month (Jul 2025)**
- QR transaction value: **NPR 0.59B → NPR 100.7B** monthly
- **~210×** growth in transaction count on those monthly endpoints (not a 2021 vs 2025 annual ratio)

---

## Research Themes

| # | Theme | Status |
|---|-------|--------|
| 1 | Digital payment adoption | ✅ Data collected |
| 2 | Transaction volume and value | ✅ Data collected |
| 3 | Payment-channel evolution | ✅ Data collected |
| 4 | Consumer engagement | ✅ Data collected |
| 5 | Merchant ecosystem | ⏳ Pending |
| 6 | Banks vs wallets vs infrastructure | ⏳ Pending |
| 7 | Network effects | ⏳ Pending |
| 8 | Customer ownership | ⏳ Pending |
| 9 | Value-chain economics | ⏳ Pending |
| 10 | Profit pools | ⏳ Pending |
| 11 | Regulatory influence | ⏳ Pending |
| 12 | Strategic groups | ⏳ Pending |
| 13 | Competitive advantage | ⏳ Pending |
| 14 | Industry scenarios (2027–2030) | ⏳ Pending |

---

## Methodology

- **Mixed-methods design**: quantitative analysis of NRB data + qualitative regulatory analysis
- **Strategic frameworks**: Porter's Five Forces, PvP profit pool analysis, strategic group mapping, scenario construction
- **Data integrity**: Every observation has a `source_id`, every calculation is reproducible, raw data is immutable

See `research/methodology.md` for the full research constitution.

---

## Project Phases

| Phase | Name | Status |
|-------|------|--------|
| Phase 1 | Architecture | ✅ Complete |
| Phase 2 | Data Inventory | ✅ Complete |
| Phase 3 | Data Engineering | ✅ Complete |
| Phase 4 | Data Validation | ✅ Complete |
| Phase 5 | Core Analyses | ✅ Complete |
| Phase 6 | Company Research | ⏳ Next |
| Phase 7 | Strategic Analyses | ⏳ Pending |
| Phase 8 | Scenarios | ⏳ Pending |
| Phase 9 | Synthesis | ⏳ Pending |

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Acknowledgments

- **Nepal Rastra Bank** for publishing the Payment Systems Indicators
- **Wayback Machine / Internet Archive** for preserving NRB data during website downtime
- Academic and industry sources listed in `research/source_register.md`

---

*Project created: August 2026*
