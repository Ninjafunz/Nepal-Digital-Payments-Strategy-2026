# Source Register — Living Document

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

---

## Purpose

This is the **audit trail** of the entire project. Every source used must appear here. Every database observation must reference a source ID from this register.

**Rule:** If a source is not in this register, it cannot be used in analysis.

---

## How to Use This Register

1. **Before using any source:** Add it here with full metadata.
2. **When importing data:** Record the source_id and link it to database observations.
3. **When citing a finding:** Reference the source_id.
4. **When auditing:** Check that every data point in the database has a valid source_id.

---

## Source ID Format

```
{TYPE}{NUMBER}
```

Examples:
- `NRB001` — First NRB source
- `NRB002` — Second NRB source
- `ESW001` — First eSewa source
- `KHL001` — First Khalti source
- `GOV001` — First government source
- `INT001` — First international organization source
- `ACD001` — First academic source
- `MED001` — First media source

---

## Source Type Classification

| Type Code | Classification | Description |
|-----------|---------------|-------------|
| `T1` | Regulatory / Official | Nepal Rastra Bank publications, government statistics |
| `T2` | Audited Financial | Company annual reports, audited financial statements |
| `T3` | Company-Reported | Press releases, official disclosures, presentations |
| `T4` | Regulatory Publication | NRB guidelines, circulars, directives |
| `T5` | Reputable Secondary | Academic papers, established industry reports |
| `T6` | Media / News | Reputable news outlets |
| `T7` | Analyst Inference | Our own calculations and estimates |

---

## A. Nepal Rastra Bank (NRB) Sources — TIER 1

These are the primary data sources. Priority: highest.

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| NRB001 | NRB | Payment System Indicators | Monthly (latest available) | 2021–present | https://www.nrb.org.np | A01–A14, B01–B18, E01–E03, H01–H05 | To collect |
| NRB002 | NRB | Payment System Department — Statistics | Monthly/Annual | 2021–present | https://www.nrb.org.np | B01–B18 (detailed breakdown) | To collect |
| NRB003 | NRB | NRB Annual Report | Annual | 2021–2025 | https://www.nrb.org.np | Industry overview, regulatory context | To collect |
| NRB004 | NRB | Monetary Policy Statement | Annual | 2021–2026 | https://www.nrb.org.np | H01–H05, regulatory direction | To collect |
| NRB005 | NRB | Financial Stability Report | Annual | 2021–2025 | https://www.nrb.org.np | System risk, institutional health | To collect |
| NRB006 | NRB | Banking and Financial Statistics | Annual | 2021–2025 | https://www.nrb.org.np | BFI-level data, deposit/lending context | To collect |
| NRB007 | NRB | NRB Directives — Payment Systems | Varies | 2021–2026 | https://www.nrb.org.np | H01–H05, regulatory framework | To collect |
| NRB008 | NRB | Nepal Financial Statistics | Annual | 2021–2025 | https://www.nrb.org.np | GDP, inflation, economic context | To collect |

---

## B. Company Sources — Tier 2/3

These will be populated in Phase 6 (Company Research).

### eSewa

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| ESW001 | eSewa/F1Soft | Annual Report / Financial Disclosure | 2021–2025 | Company-level | TBD | J01–J10 | To collect |

### Khalti

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| KHL001 | Khalti/Janaki Tech | Annual Report / Financial Disclosure | 2021–2025 | Company-level | TBD | J01–J10 | To collect |

### Other PSPs

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| PSP001 | [PSP Name] | TBD | TBD | TBD | TBD | J01–J10 | To identify |

### Major Banks

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| BNK001 | [Bank Name] | Annual Report | 2021–2025 | Bank-level | TBD | J01–J10 | To identify |

### Payment Infrastructure

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| NCH001 | NCHL (Nepal Clearing House) | Annual Report / Disclosure | 2021–2025 | Infrastructure-level | TBD | B13–B14, G01–G06 | To collect |
| SAN001 | SANIMA / Smart Technologies | Disclosure | TBD | Infrastructure-level | TBD | G01–G06 | To identify |

---

## C. Government & International Sources — Tier 1/5

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| GOV001 | Nepal Government / CBS | National Census / Population Statistics | 2021 | National | TBD | A15 | To collect |
| GOV002 | Nepal Telecom Authority | Annual Report / Telecom Statistics | 2021–2025 | Telecom sector | TBD | A15 context, mobile penetration | To collect |
| INT001 | World Bank | World Development Indicators | 2021–2025 | Nepal | https://data.worldbank.org | A15, GDP, economic context | To collect |
| INT002 | IMF | World Economic Outlook | 2021–2025 | Nepal | https://www.imf.org | GDP, economic context | To collect |
| INT003 | ITU / GSMA | Digital Development / Mobile Money Reports | 2021–2025 | South Asia | TBD | Regional comparison context | To collect |

---

## D. Academic Sources — Tier 5

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| ACD001 | TBD | Literature review sources | TBD | Nepal / South Asia | TBD | Context, methodology | To identify |

---

## E. Media Sources — Tier 6

| Source ID | Institution | Document | Date | Coverage | URL | Variables | Status |
|-----------|------------|----------|------|----------|-----|-----------|--------|
| MED001 | Kantipur / Kathmandu Post | News articles on digital payments | 2021–2026 | Nepal | TBD | Context, company information | To collect as needed |

---

## F. Analyst Inference — Tier 7

| Source ID | Type | Description | Date | Variables | Status |
|-----------|------|-------------|------|-----------|--------|
| ANL001 | T7 | All derived/calculated metrics in the project | Ongoing | Derived variables | Active |

---

## Source Reliability Assessment

| Source ID | Reliability | Notes |
|-----------|------------|-------|
| NRB001–NRB008 | High | Official regulatory data; primary source |
| ESW001 | Medium | Company-reported; not independently audited (if private) |
| KHL001 | Medium | Company-reported; not independently audited (if private) |
| GOV001–GOV002 | High | Official government statistics |
| INT001–INT003 | High | Established international organization data |
| MED001 | Low-Medium | Subject to reporting accuracy; must be cross-referenced |
| ANL001 | Variable | Depends on underlying data quality |

---

## Source Usage Log

This section tracks which sources have been used for which analyses.

| Analysis | Sources Used | Date |
|----------|-------------|------|
| (No analyses completed yet) | — | — |

---

## Maintenance Rules

1. **Every new source must be added** before it is used in any analysis.
2. **Source IDs are never reused.** If a source is superseded, the old entry is marked `SUPERSEDED` and a new one is created.
3. **URLs must be verified** at time of entry. If a URL breaks, the entry is updated with an archive link.
4. **Access dates must be recorded** for every source at time of first use.
5. **The register is reviewed** at each phase transition.

---

*Document status: Architecture complete. NRB sources pre-identified. Company and secondary sources to be populated in subsequent phases.*
