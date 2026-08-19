# NRB Data Inventory — Preliminary

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

**Status:** PRELIMINARY — requires verification against actual NRB website and publications

---

## Purpose

This document identifies official Nepal Rastra Bank (NRB) datasets relevant to this research project. It maps each dataset to the variables defined in the data dictionary.

**Important:** This inventory is based on known NRB publications. The exact availability, format, and coverage of each dataset must be verified when the NRB website is accessible.

---

## Priority Classification

| Priority | Description |
|----------|-------------|
| **P1 — Essential** | Must have for core analysis |
| **P2 — Important** | Adds depth and context |
| **P3 — Supplementary** | Nice to have for robustness |

---

## A. NRB Payment System Indicators

### A1: Payment System Statistics (Monthly)

| Field | Value |
|-------|-------|
| **Dataset Name** | Payment System Statistics / Payment System Indicators |
| **Source ID** | NRB001 |
| **Institution** | Nepal Rastra Bank — Payment System Department |
| **Likely URL** | https://www.nrb.org.np/ (Payment System Department section) |
| **Publication Frequency** | Monthly |
| **Historical Coverage** | Likely 2018/19 — present (to verify) |
| **File Format** | PDF report; may contain tables; possibly Excel附录 |
| **Priority** | P1 — Essential |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| Wallet accounts total | A01 | Yes |
| Wallet active users | A02 | Likely (may be annual) |
| Mobile banking users | A03 | Yes |
| Mobile banking active users | A04 | Likely |
| Internet banking users | A05 | Yes |
| Internet banking active users | A06 | Likely |
| Card counts | A07–A09 | Possibly (may be in annual report) |
| ATM count | A10 | Yes |
| POS count | A11 | Yes |
| PSP count | A12 | Yes |
| PSO count | A13 | Yes |
| Wallet transaction count | B01 | Yes |
| Wallet transaction value | B02 | Yes |
| Mobile banking transaction count | B03 | Yes |
| Mobile banking transaction value | B04 | Yes |
| Internet banking transaction count | B05 | Yes |
| Internet banking transaction value | B06 | Yes |
| QR transaction count | B07 | Yes (if published at channel level) |
| QR transaction value | B08 | Yes (if published at channel level) |
| POS transaction count | B09 | Yes |
| POS transaction value | B10 | Yes |
| Card transaction count | B11 | Yes |
| Card transaction value | B12 | Yes |
| connectIPS transaction count | B13 | Yes |
| connectIPS transaction value | B14 | Yes |
| E-commerce transaction count | B15 | Possibly |
| E-commerce transaction value | B16 | Possibly |
| Merchant count | E01–E03 | Possibly |

**Methodological Notes:**
- NRB definitions of "active" may change over time — must check
- Whether QR data is broken out separately vs. bundled with other channels — must verify
- Whether e-commerce is a separate channel or subset — must verify
- Monthly data may have reporting lag of 1–3 months

---

### A2: NRB Annual Report

| Field | Value |
|-------|-------|
| **Dataset Name** | Nepal Rastra Bank Annual Report |
| **Source ID** | NRB003 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ (Publications section) |
| **Publication Frequency** | Annual (Nepali fiscal year ends mid-July) |
| **Historical Coverage** | FY 2020/21 — FY 2024/25 (to verify) |
| **File Format** | PDF (full report) |
| **Priority** | P1 — Essential |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| Industry overview | — | Narrative |
| GDP context | — | Economic data |
| Financial system overview | — | Banking context |
| Payment system summary | A01–A16 | Summary data |
| Regulatory changes | H01–H05 | Regulatory timeline |

**Methodological Notes:**
- Annual reports provide context and cross-verification for monthly data
- May contain higher-level aggregates not in monthly publications
- Fiscal year: mid-July to mid-July (e.g., FY 2024/25 = mid-July 2024 to mid-July 2025)

---

### A3: Monetary Policy Statement

| Field | Value |
|-------|-------|
| **Dataset Name** | Monetary Policy Statement |
| **Source ID** | NRB004 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ (Publications section) |
| **Publication Frequency** | Annual (with mid-year review) |
| **Historical Coverage** | FY 2020/21 — FY 2025/26 |
| **File Format** | PDF |
| **Priority** | P2 — Important |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| Transaction limits | H01–H02 | Narrative/directive |
| Interoperability mandates | H04 | Policy announcement |
| Digital payment targets | — | Policy direction |
| Regulatory priorities | H05 | Narrative |

**Methodological Notes:**
- Not a statistical publication — provides regulatory context
- Critical for understanding regulatory influence on competitive dynamics
- Key policy announcements that may have shaped market structure

---

### A4: Financial Stability Report

| Field | Value |
|-------|-------|
| **Dataset Name** | Financial Stability Report |
| **Source ID** | NRB005 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ |
| **Publication Frequency** | Annual (or semi-annual) |
| **Historical Coverage** | To verify |
| **File Format** | PDF |
| **Priority** | P2 — Important |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| System risk assessment | — | Narrative |
| BFI health indicators | — | Institutional context |
| Digital payment risk | — | Risk perspective |

**Methodological Notes:**
- Provides risk context for digital payment growth
- May contain institutional-level data not available elsewhere

---

### A5: Banking and Financial Statistics

| Field | Value |
|-------|-------|
| **Dataset Name** | Banking and Financial Statistics |
| **Source ID** | NRB006 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ (Statistics section) |
| **Publication Frequency** | Annual |
| **Historical Coverage** | To verify |
| **File Format** | PDF / Excel |
| **Priority** | P2 — Important |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| BFI deposits, lending | — | Banking context |
| BFI digital services | — | Bank digital participation |
| Financial inclusion | — | Adoption context |

**Methodological Notes:**
- Provides banking sector context
- May contain BFI-level data for digital services
- Cross-reference with payment system statistics

---

### A6: Nepal Financial Statistics

| Field | Value |
|-------|-------|
| **Dataset Name** | Nepal Financial Statistics / Economic Bulletin |
| **Source ID** | NRB008 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ (Statistics section) |
| **Publication Frequency** | Monthly / Quarterly |
| **Historical Coverage** | To verify |
| **File Format** | PDF / Excel |
| **Priority** | P2 — Important |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| GDP | — | Economic context |
| Inflation | — | Economic context |
| Exchange rate | — | Economic context |

**Methodological Notes:**
- Provides macroeconomic context for digital payment growth
- GDP data essential for calculating digital share of GDP

---

### A7: NRB Directives — Payment Systems

| Field | Value |
|-------|-------|
| **Dataset Name** | NRB Directives and Circulars — Payment Systems |
| **Source ID** | NRB007 |
| **Institution** | Nepal Rastra Bank |
| **Likely URL** | https://www.nrb.org.np/ (Directives section) |
| **Publication Frequency** | As issued |
| **Historical Coverage** | To verify |
| **File Format** | PDF |
| **Priority** | P1 — Essential |

**Expected Variables Covered:**

| Variable | ID | Expected in Dataset |
|----------|----|--------------------|
| Transaction limits | H01–H02 | Directive text |
| KYC requirements | H03 | Directive text |
| Interoperability mandates | H04 | Directive text |
| Licensing requirements | — | Directive text |

**Methodological Notes:**
- Not a statistical publication — provides regulatory framework
- Critical for H11 (regulatory influence hypothesis)
- Timeline of directives is essential for event study analysis

---

## B. Supplementary NRB Sources

### B1: Nepal Telecom Authority Reports

| Field | Value |
|-------|-------|
| **Source ID** | GOV002 |
| **Institution** | Nepal Telecom Authority |
| **Relevance** | Mobile penetration, internet access, smartphone adoption |
| **Priority** | P3 — Supplementary |

### B2: World Bank Data — Nepal

| Field | Value |
|-------|-------|
| **Source ID** | INT001 |
| **Institution** | World Bank |
| **URL** | https://data.worldbank.org/country/nepal |
| **Relevance** | GDP, population, economic indicators, financial inclusion |
| **Priority** | P2 — Important |

### B3: Central Bureau of Statistics — Nepal

| Field | Value |
|-------|-------|
| **Source ID** | GOV001 |
| **Institution** | CBS, Nepal Government |
| **Relevance** | Population, demographics, economic census |
| **Priority** | P2 — Important |

---

## Data Gap Analysis (Preliminary)

Based on this inventory, the following data gaps are anticipated:

| Gap | Impact | Mitigation |
|-----|--------|-----------|
| **Company-level data** — NRB publishes aggregate data, not company-level | Cannot do player-level analysis from NRB alone | Supplement with T2/T3 company disclosures |
| **Merchant data** — unclear if NRB publishes detailed merchant metrics | Limits Analysis 5 (merchant ecosystem) | May need to use company-reported data |
| **Channel-level QR data** — QR may not be broken out separately from other mobile channels | Limits H3 testing | Check if NRB publishes QR-specific data |
| **Fee/revenue data** — NRB unlikely to publish fee structures | Limits profit pool analysis | Use T3 company disclosures and T7 estimates |
| **User overlap** — NRB unlikely to publish multi-platform usage data | Limits network effects analysis | Use T5 research or T7 estimates |

---

## Verification Checklist

Before Phase 3 (Data Engineering), verify:

- [ ] NRB website is accessible
- [ ] Payment System Statistics publication exists and format is documented
- [ ] Exact variable breakdown is confirmed (which channels are reported separately)
- [ ] Historical coverage is confirmed (how far back does monthly data go)
- [ ] File format is confirmed (PDF, Excel, or web-only)
- [ ] Data download method is documented
- [ ] Any methodology changes over 2021–2026 are identified

---

## Next Steps

1. **Access NRB website** and locate Payment System Statistics
2. **Verify exact publication format** (PDF tables, Excel files, web portal)
3. **Download sample data** (most recent month) to confirm variable coverage
4. **Map confirmed variables** to data dictionary
5. **Update this inventory** with verified information
6. **Begin data ingestion** (Phase 3)

---

*Document status: PRELIMINARY. Based on known NRB publications. Requires verification against actual NRB website and publications. Do not treat as confirmed.*
