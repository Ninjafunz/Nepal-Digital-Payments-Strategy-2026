# NRB Data Inventory — Verified (Partial)

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

**Status:** PARTIALLY VERIFIED — NRB website down (500 errors); verified via Wayback Machine snapshots (Jan 2025, Jun 2024)

---

## Purpose

This document identifies official Nepal Rastra Bank (NRB) datasets relevant to this research project. It maps each dataset to the variables defined in the data dictionary.

## Verification Status (August 2026)

**NRB website (nrb.org.np) is DOWN** — returning 500 Internal Server Error on all pages tested. The Internet Archive Wayback Machine's CDX API is also temporarily offline. Web search API returned no results for NRB queries.

**What was verified** via Wayback Machine cached snapshots of the NRB homepage (Jan 2025 and Jun 2024):

| Publication | Confirmed | Notes |
|-------------|-----------|-------|
| Monetary Policy (English & Nepali) | ✅ Yes | Published annually; full text PDF available |
| Current Macroeconomic and Financial Situation | ✅ Yes | Published monthly with tables PDF (2–2.4 MB) |
| NRB Annual Report | ✅ Yes | Published annually |
| Payment System Directives | ✅ Yes | Seen: "भुक्तानी प्रणालीसम्बन्धी एकीकृत निर्देशन, २०८०" (Integrated Directive on Payment System, 2080) |
| Financial Corporations Survey (FCS) | ✅ Yes | Referenced on homepage |
| Payment System Statistics / Indicators | ⚠️ NOT CONFIRMED | Not visible on homepage; may be in a sub-section that wasn't cached |
| Financial Stability Report | ⚠️ NOT CONFIRMED | Referenced in preliminary inventory but not seen in cached pages |
| Banking and Financial Statistics | ⚠️ NOT CONFIRMED | Referenced in preliminary inventory but not seen in cached pages |

**Critical finding:** The "Payment System Statistics" or "Payment System Indicators" publication — which would be the PRIMARY data source for this project — could NOT be confirmed through the Wayback Machine. This does not mean it doesn't exist; it may be in a sub-section of the NRB website that wasn't archived, or it may be published under a different name.

**Immediate next step:** When the NRB website comes back online, locate the exact payment system data publication and verify its format, coverage, and download method.

---

## Priority Classification

| Priority | Description |
|----------|-------------|
| **P1 — Essential** | Must have for core analysis |
| **P2 — Important** | Adds depth and context |
| **P3 — Supplementary** | Nice to have for robustness |

---

## A. NRB Payment System Indicators

### A1: Payment System Statistics (Monthly) — UNCONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Payment System Statistics / Payment System Indicators |
| **Source ID** | NRB001 |
| **Institution** | Nepal Rastra Bank — Payment System Department |
| **URL** | ⚠️ NOT CONFIRMED — NRB website down; sub-section not found in Wayback Machine |
| **Publication Frequency** | Likely monthly (unconfirmed) |
| **Historical Coverage** | Unknown — to verify when website is accessible |
| **File Format** | Unknown — to verify (likely PDF, possibly with Excel appendix) |
| **Verification Status** | ❌ NOT VERIFIED — primary data source for this project |

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

### A2: NRB Annual Report — CONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Nepal Rastra Bank Annual Report |
| **Source ID** | NRB003 |
| **Institution** | Nepal Rastra Bank |
| **URL** | https://www.nrb.org.np/ (Publications section) — ⚠️ website currently down |
| **Publication Frequency** | Annual (Nepali fiscal year ends mid-July) |
| **Historical Coverage** | FY 2020/21 — FY 2024/25 (to verify exact range) |
| **File Format** | PDF (full report) — ✅ confirmed from Wayback Machine |
| **Verification Status** | ✅ Publication confirmed; exact download URL needs verification |

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

### A3: Monetary Policy Statement — CONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Monetary Policy Statement |
| **Source ID** | NRB004 |
| **Institution** | Nepal Rastra Bank |
| **URL** | https://www.nrb.org.np/ (Publications section) — ⚠️ website currently down |
| **Publication Frequency** | Annual (with mid-year review) |
| **Historical Coverage** | FY 2020/21 — FY 2025/26 |
| **File Format** | PDF — ✅ confirmed (English: 1.11 MB for 2025-26; Nepali: 890 KB for 2082-83) |
| **Verification Status** | ✅ Publication confirmed with file sizes from Wayback Machine |

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

### A4: Financial Stability Report — UNCONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Financial Stability Report |
| **Source ID** | NRB005 |
| **Institution** | Nepal Rastra Bank |
| **URL** | ⚠️ NOT SEEN in Wayback Machine homepage snapshots |
| **Publication Frequency** | Unknown — likely annual |
| **Historical Coverage** | Unknown |
| **File Format** | Unknown |
| **Verification Status** | ❌ NOT VERIFIED — may exist but not visible in cached pages |

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

### A5: Banking and Financial Statistics — UNCONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Banking and Financial Statistics |
| **Source ID** | NRB006 |
| **Institution** | Nepal Rastra Bank |
| **URL** | ⚠️ NOT SEEN in Wayback Machine homepage snapshots |
| **Publication Frequency** | Unknown |
| **Historical Coverage** | Unknown |
| **File Format** | Unknown |
| **Verification Status** | ❌ NOT VERIFIED |

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

### A6: Current Macroeconomic and Financial Situation — CONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | Current Macroeconomic and Financial Situation |
| **Source ID** | NRB008 |
| **Institution** | Nepal Rastra Bank |
| **URL** | https://www.nrb.org.np/ — ⚠️ website currently down |
| **Publication Frequency** | Monthly — ✅ confirmed |
| **Historical Coverage** | At least FY 2023/24 — FY 2025/26 — ✅ confirmed |
| **File Format** | PDF (English text ~400-800 KB; Tables ~2.2-2.5 MB) — ✅ confirmed |
| **Verification Status** | ✅ Publication confirmed with file sizes; contains GDP, inflation, monetary data |
| **Relevance** | Provides macroeconomic context; tables PDF may contain payment-relevant data |

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

### A7: NRB Directives — Payment Systems — CONFIRMED

| Field | Value |
|-------|-------|
| **Dataset Name** | NRB Directives and Circulars — Payment Systems |
| **Source ID** | NRB007 |
| **Institution** | Nepal Rastra Bank |
| **URL** | https://www.nrb.org.np/ — ⚠️ website currently down |
| **Publication Frequency** | As issued |
| **Historical Coverage** | At least FY 2080 (2023/24) — ✅ confirmed |
| **File Format** | PDF — ✅ confirmed (1.37 MB for payment system directive amendment, Dec 2024) |
| **Verification Status** | ✅ Publication confirmed: "भुक्तानी प्रणालीसम्बन्धी एकीकृत निर्देशन, २०८०" (Integrated Directive on Payment System, 2080) |
| **Key Finding** | NRB issued amendments to payment system directives in Dec 2024 — regulatory activity is active |

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

## Additional Confirmed NRB Data Points (from Homepage)

From the Wayback Machine snapshots, the NRB homepage displays these indicators:

| Indicator | Latest Value | Period |
|-----------|-------------|--------|
| Total Deposits | NPR 7,600 billion | Dec 2025 |
| Total Lending | NPR 5,693 billion | Dec 2025 |
| CD Ratio | 74.08% | Dec 2025 |
| Total Financial Institutions | 146 | FY 2025/26 Q4 |
| Licensed BFIs | 107 | FY 2025/26 Q4 |
| Total Branches | 11,516 | FY 2025/26 Q4 |
| Broad Money Growth | 12.5% | FY 2025/26 Q4 |
| Private Sector Credit Growth | 6.4% | FY 2025/26 Q4 |
| Remittance Inflow | NPR 687 billion | FY 2025/26 Q4 |
| Worker's Remittance % of GDP | 28.2% | FY 2024/25 |
| National CPI Inflation | 1.11% | FY 2025/26 Q4 |

**Note:** These are banking sector indicators, not payment system indicators. Payment system data is not displayed on the homepage.

## NRB Fiscal Year Convention

NRB uses the Nepali fiscal year: mid-July to mid-July.
- FY 2024/25 = mid-July 2024 to mid-July 2025
- FY 2025/26 = mid-July 2025 to mid-July 2026
- Nepali calendar year = fiscal year + ~56/57 years (e.g., 2082 BS ≈ 2025/26 AD)

This is important for date alignment when collecting monthly data.

## Verification Checklist

Before Phase 3 (Data Engineering), verify:

- [ ] **CRITICAL:** NRB website is accessible again
- [ ] **CRITICAL:** Locate the Payment System Statistics / Indicators publication — this is the PRIMARY data source
- [ ] Exact variable breakdown is confirmed (which channels are reported separately)
- [ ] Historical coverage is confirmed (how far back does monthly data go)
- [ ] File format is confirmed (PDF, Excel, or web-only)
- [ ] Data download method is documented
- [ ] Any methodology changes over 2021–2026 are identified
- [ ] Check if payment system data is embedded in the "Current Macroeconomic and Financial Situation" tables PDF
- [ ] Verify whether NRB publishes an annual "Payment System Overview" or similar report

---

## Next Steps

1. **Wait for NRB website to come back online** (currently returning 500 errors)
2. **Locate the Payment System Statistics publication** — this is the single most important task
3. **Check if payment system data is in the "Current Macroeconomic and Financial Situation" tables PDF** (2.2–2.5 MB files)
4. **Verify exact publication format** (PDF tables, Excel files, web portal)
5. **Download sample data** (most recent month) to confirm variable coverage
6. **Map confirmed variables** to data dictionary
7. **Update this inventory** with verified information
8. **Begin data ingestion** (Phase 3)

---

*Document status: PARTIALLY VERIFIED. NRB website down (500 errors as of Aug 2026). Verified via Wayback Machine: Monetary Policy ✅, Annual Report ✅, Macroeconomic Reports ✅, Payment System Directives ✅. Payment System Statistics publication NOT CONFIRMED — critical gap. Must verify when website is accessible.*
