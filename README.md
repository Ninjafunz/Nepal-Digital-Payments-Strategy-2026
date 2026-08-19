# From Cash to Platforms

## The Transformation of Nepal's Digital Payments Industry, 2021–2026

**Project type:** MSc Strategy — Industry & Competitive Analysis

---

## Core Research Question

> **How is digitalization changing the basis of competition and the distribution of economic value in Nepal's payments ecosystem?**

This is not a "digital payments are growing" report. This is a strategic analysis of **who is gaining power, why, and who is positioned to capture the next profit pool**.

---

## What This Project Demonstrates

1. **Strategic thinking** — applying frameworks to a real, complex, evolving industry
2. **Industry analysis** — structured understanding of Nepal's payments landscape
3. **Competitive dynamics** — how banks, wallets, PSPs, and infrastructure providers compete
4. **Quantitative research** — rigorous data collection and analysis from official sources
5. **Data engineering** — traceable, auditable data pipeline with full provenance
6. **Evidence-based strategic recommendations** — grounded in data, not opinion

---

## Project Repository Map

```
Nepal-Digital-Payments-Strategy-2026/
│
├── README.md                          # This file
│
├── research/                          # Research architecture
│   ├── research_question.md           # Formal questions, scope, definitions
│   ├── hypotheses.md                  # 14 testable hypotheses
│   ├── methodology.md                 # Research constitution & data hierarchy
│   ├── data_dictionary.md             # Master variable catalogue
│   ├── source_register.md             # Living register of all sources
│   ├── nrb_data_inventory.md          # NRB dataset inventory (Phase 2)
│   └── analysis_plan.md              # Step-by-step analysis mapping
│
├── data/
│   ├── raw/                           # Unprocessed data as downloaded
│   ├── processed/                     # Cleaned, transformed data
│   └── final/                         # Analysis-ready datasets
│
├── database/
│   ├── payments.db                    # SQLite database (Phase 3)
│   └── schema.md                      # Database schema documentation
│
├── sources/                           # Raw source documents (PDFs, etc.)
│
├── notebooks/                         # Jupyter analysis notebooks
│
├── src/
│   ├── ingestion/                     # Data ingestion scripts
│   ├── cleaning/                      # Data cleaning scripts
│   ├── validation/                    # Data validation scripts
│   └── analysis/                      # Analysis scripts
│
├── analysis/                          # Structured analytical outputs
│
├── dashboard/                         # Visual dashboard specifications
│
├── report/                            # Paper sections, figures, tables
│
└── agents/                            # AI agent configurations
```

---

## Data Quality Constitution

### Fundamental Rules

1. **Every quantitative observation must be traceable to a source.** No exceptions.
2. **No data is invented.** If we don't have it, we say so.
3. **No strategic conclusions without evidence.** Hypotheses are testable propositions, not assertions.
4. **No arbitrary scoring systems.** Indices and scores require methodological justification.
5. **Secondary sources cannot override primary data** without explicit justification.

### Source-Type Taxonomy

Every source used in this project must be classified as one of:

| Type Code | Classification | Description |
|-----------|---------------|-------------|
| `T1` | Regulatory / Official | Nepal Rastra Bank publications, government statistics |
| `T2` | Audited Financial | Company annual reports, audited financial statements |
| `T3` | Company-Reported | Press releases, investor presentations, official social media |
| `T4` | Regulatory Publication | NRB guidelines, circulars, directives (not data publications) |
| `T5` | Reputable Secondary | Academic papers, industry reports from established firms |
| `T6` | Media / News | Reputable news outlets, journalism |
| `T7` | Analyst Inference | Our own analysis, derived calculations, estimates |

**Rule:** T7 (analyst inference) must be clearly marked and must never be presented as fact. T6 (media) cannot override T1–T3 without explicit justification documented in the source register.

---

## Data Hierarchy

When sources conflict, the hierarchy governs:

```
Tier 1: Nepal Rastra Bank (NRB) — official statistics, payment system indicators
Tier 2: Audited company annual reports and financial statements
Tier 3: Official company disclosures and regulated filings
Tier 4: Regulatory publications (NRB guidelines, circulars, directives)
Tier 5: Reputable secondary sources (academic, established industry reports)
Tier 6: News and media reporting
Tier 7: Analyst inference and derived calculations
```

**Higher tiers take precedence** unless there is documented evidence that higher-tier data is incomplete or mischaracterized for a specific use case.

---

## Project Phase Roadmap

| Phase | Name | Description |
|-------|------|-------------|
| **Phase 1** | Architecture | Research question, methodology, data dictionary, schema (CURRENT) |
| **Phase 2** | Data Inventory | NRB dataset identification and documentation |
| **Phase 3** | Data Engineering | SQLite database, ingestion pipeline, first NRB dataset import |
| **Phase 4** | Data Validation | Quality audit, duplicate detection, gap analysis |
| **Phase 5** | Core Analysis | Five foundational analyses |
| **Phase 6** | Company Research | eSewa, Khalti, banks, PSPs |
| **Phase 7** | Strategic Analysis | Competitive positioning, network effects, value chains |
| **Phase 8** | Scenarios | Industry scenarios for 2027–2030 |
| **Phase 9** | Synthesis | Final report, strategic recommendations |

---

## Abbreviations

| Abbreviation | Full Name |
|-------------|-----------|
| NRB | Nepal Rastra Bank |
| PSP | Payment Service Provider |
| PSO | Payment System Operator |
| QR | Quick Response (code) |
| POS | Point of Sale |
| NEPSE | Nepal Stock Exchange |
| HHI | Herfindahl-Hirschman Index |
| NPR | Nepalese Rupee |
| GDP | Gross Domestic Product |
| KYC | Know Your Customer |
| AML | Anti-Money Laundering |
| CDR | Call Detail Record |

---

## Technology Stack

- **Database:** SQLite (payments.db)
- **Language:** Python 3
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Notebooks:** Jupyter
- **Version Control:** Git

---

## How to Work With This Project

### Rules of Engagement

1. **Research question → methodology → variables → sources → database → analysis → strategy.** This is the sequence. Don't skip steps.
2. **Primary sources first.** Always start with NRB data before looking at company claims.
3. **Every number has a source tag.** The `source_id` field in the database is non-negotiable.
4. **The strategy agent reads but does not modify raw data.** This protects evidence integrity.
5. **Validate before analyzing.** Every dataset gets a quality audit before any analysis begins.

---

*Project created: August 2026*
*This is a research architecture document. No data has been collected or analyzed yet.*
