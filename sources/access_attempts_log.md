# NRB Data Source Access Attempts Log

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

**Date of attempts:** August 2026

**Purpose:** Document every URL access attempt made during Phase 2 (Data Inventory Verification) for audit trail purposes.

---

## Summary

| Category | Count |
|----------|-------|
| Total attempts | 48 |
| Successful (200) | 2 |
| Failed (500) | 22 |
| Failed (404) | 21 |
| Failed (other) | 3 |
| Data extracted | 2 homepage snapshots |

**Conclusion:** NRB website is completely down (500 errors). Two Wayback Machine homepage snapshots were successfully accessed and provided partial verification. No payment system-specific data pages were found in any archive.

---

## A. NRB Direct Website Attempts

All attempts to access nrb.org.np directly returned **500 Internal Server Error**.

| # | URL | Method | Result | Notes |
|---|-----|--------|--------|-------|
| 1 | https://www.nrb.org.np | read_url | ❌ 500 | Main homepage |
| 2 | https://nrb.org.np | read_url | ❌ 500 | Without www |
| 3 | https://www.nrb.org.np/en | read_url | ❌ 500 | English homepage |
| 4 | https://www.nrb.org.np/payment-system | read_url | ❌ 500 | Payment system page |
| 5 | https://www.nrb.org.np/statistics | read_url | ❌ 500 | Statistics page |
| 6 | https://www.nrb.org.np/payment-system-department | read_url | ❌ 500 | Payment system department |
| 7 | https://nrb.org.np/statistics | read_url | ❌ 500 | Statistics without www |
| 8 | https://www.nrb.org.np/statistics/payment-systems | read_url | ❌ 500 | Payment system statistics |
| 9 | https://www.nrb.org.np/payment-system-indicator | read_url | ❌ 500 | Payment system indicators |
| 10 | https://www.nrb.org.np/statistics/payment-system | read_url | ❌ 500 | Payment system stat |
| 11 | https://www.nrb.org.np/about-us/department | read_url | ❌ 500 | Department listing |
| 12 | https://www.nrb.org.np/doing-business | read_url | ❌ 500 | Doing business section |
| 13 | https://www.nrb.org.np/doing-business/payment-system | read_url | ❌ 500 | Payment system in doing-business |
| 14 | https://www.nrb.org.np/doing-business/payment-system-department | read_url | ❌ 500 | Payment system dept in doing-business |
| 15 | https://www.nrb.org.np/about-us/department/payment-system-department | read_url | ❌ 500 | Payment system dept in about-us |
| 16 | https://www.nrb.org.np/about-us/payment-system-department | read_url | ❌ 500 | Alternate path |
| 17 | https://www.nrb.org.np/about-us/payment-system-department/payment-systems-indicator | read_url | ❌ 500 | Indicator page |
| 18 | https://www.nrb.org.np/about-us/payment-system-department/payment-system-statistics | read_url | ❌ 500 | Statistics page |
| 19 | https://www.nrb.org.np/about-us/payment-system-department/payment-system-overview | read_url | ❌ 500 | Overview page |
| 20 | https://www.nrb.org.np/about-us/payment-system-department/payment-systems-overview | read_url | ❌ 500 | Overview (plural) |
| 21 | https://www.nrb.org.np/doing-business/payment-system/payment-systems-indicator | read_url | ❌ 500 | Indicator in doing-business |
| 22 | https://www.nrb.org.np/doing-business/payment-system/payment-system-statistics | read_url | ❌ 500 | Statistics in doing-business |

---

## B. Wayback Machine — Homepage Snapshots (SUCCESSFUL)

| # | URL | Method | Result | Data Extracted |
|---|-----|--------|--------|----------------|
| 23 | https://web.archive.org/web/2025/https://www.nrb.org.np/ | read_url | ✅ 200 | NRB homepage (Jan 2025 snapshot) — monetary policy, macro reports, indicators |
| 24 | https://web.archive.org/web/2024/https://www.nrb.org.np/ | read_url | ✅ 200 | NRB homepage (Jun 2024 snapshot) — same structure confirmed |

**Key data extracted from homepage snapshots:**
- Monetary Policy: English PDF 1.11 MB (2025-26), Nepali 890 KB (2082-83)
- Current Macroeconomic and Financial Situation: monthly, tables PDF 2.2-2.5 MB
- Payment System Directive: Dec 2024, 1.37 MB PDF
- Banking indicators: deposits, lending, CD ratio, inflation, remittance
- 146 total financial institutions, 107 licensed BFIs, 11,516 branches

---

## C. Wayback Machine — Payment System Pages (ALL FAILED)

| # | URL | Method | Result | Notes |
|---|-----|--------|--------|-------|
| 25 | https://web.archive.org/web/2024/https://www.nrb.org.np/payment-system-department | read_url | ❌ 404 | Not archived |
| 26 | https://web.archive.org/web/2024/https://www.nrb.org.np/statistics/payment-system-statistics | read_url | ❌ 404 | Not archived |
| 27 | https://web.archive.org/web/2024/https://www.nrb.org.np/payment-system-indicator | read_url | ❌ 404 | Not archived |
| 28 | https://web.archive.org/web/2024/https://www.nrb.org.np/doing-business/payment-system-department | read_url | ❌ 404 | Not archived |
| 29 | https://web.archive.org/web/2024/https://www.nrb.org.np/doing-business/payment-system | read_url | ❌ 404 | Not archived |
| 30 | https://web.archive.org/web/2024/https://www.nrb.org.np/about-us/department/payment-system-department | read_url | ❌ 404 | Not archived |
| 31 | https://web.archive.org/web/2025/https://www.nrb.org.np/payment-system-department | read_url | ❌ 404 | Not archived |
| 32 | https://web.archive.org/web/2025/https://www.nrb.org.np/statistics/payment-system-statistics | read_url | ❌ 404 | Not archived |
| 33 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/doing-business/payment-system-department | read_url | ❌ 404 | Specific timestamp |
| 34 | https://web.archive.org/web/20230601000000/https://www.nrb.org.np/doing-business/payment-system-department | read_url | ❌ 404 | Older timestamp |
| 35 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/about-us/department/payment-system-department | read_url | ❌ 404 | About-us path |
| 36 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/payment-system-department | read_url | ❌ 404 | Direct path |
| 37 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/payment-system | read_url | ❌ 404 | Short path |
| 38 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/statistics/payment-systems | read_url | ❌ 404 | Statistics path |
| 39 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/payment-system/payment-systems-indicator | read_url | ❌ 404 | Nested path |
| 40 | https://web.archive.org/web/20240601002203/https://www.nrb.org.np/payment-system/payment-system-overview | read_url | ❌ 404 | Overview path |
| 41 | https://web.archive.org/web/20250101042704/http://www.nrb.org.np/doing-business/payment-system-department/payment-systems-overview | read_url | ❌ 404 | HTTP variant |
| 42 | https://web.archive.org/web/20250101042704/http://www.nrb.org.np/doing-business/payment-system-department/payment-systems-indicators | read_url | ❌ 404 | HTTP variant |
| 43 | https://web.archive.org/web/20250101042704/http://www.nrb.org.np/doing-business/payment-system-department/payment-systems-statistics | read_url | ❌ 404 | HTTP variant |
| 44 | https://web.archive.org/web/20250102093525/https://www.nrb.org.np/doing-business/payment-system-department | read_url | ❌ 404 | Doing-business path |
| 45 | https://web.archive.org/web/20250102093525/https://www.nrb.org.np/doing-business/payment-system-department/payment-systems-indicator | read_url | ❌ 404 | Indicator page |
| 46 | https://web.archive.org/web/20250102093525/https://www.nrb.org.np/doing-business/payment-system-department/payment-system-statistics | read_url | ❌ 404 | Statistics page |
| 47 | https://web.archive.org/web/20250102093525/https://www.nrb.org.np/doing-business/payment-system-department/payment-systems-overview | read_url | ❌ 404 | Overview page |

---

## D. Wayback Machine — API/CDX Attempts

| # | URL | Method | Result | Notes |
|---|-----|--------|--------|-------|
| 48 | https://web.archive.org/cdx/search/cdx?url=nrb.org.np/*payment*&output=text&fl=original&limit=50 | run_terminal_command (curl) | ❌ Temporarily Offline | IA services offline |
| 49 | https://web.archive.org/cdx/search/cdx?url=nrb.org.np/*indicator*&output=text&fl=original&limit=50 | read_url | ❌ No readable text | CDX API down |
| 50 | https://web.archive.org/cdx/search/cdx?url=nrb.org.np/doing-business/*&output=text&fl=original&collapse=urlkey&limit=100 | read_url | ❌ No readable text | CDX API down |
| 51 | https://web.archive.org/web/2024*/https://www.nrb.org.np/payment-system-department* | read_url | ⚠️ Search page (no results) | Wayback Machine search returned empty |
| 52 | https://web.archive.org/web/2025*/https://www.nrb.org.np/payment-system* | read_url | ⚠️ Search page (no results) | Wayback Machine search returned empty |

---

## E. Google Cache Attempts

| # | URL | Method | Result | Notes |
|---|-----|--------|--------|-------|
| 53 | https://webcache.googleusercontent.com/search?q=cache:nrb.org.np/payment-system-department | read_url | ❌ Redirect to search | Google cache not available |

---

## F. Alternative Data Sources

| # | URL | Method | Result | Notes |
|---|-----|--------|--------|-------|
| 54 | https://data.nepal.gov.np | read_url | ❌ DNS failure | Nepal open data portal does not exist |
| 55 | https://www.npc.gov.np | read_url | ❌ Connection closed | Nepal Planning Commission unreachable |
| 56 | https://data.worldbank.org/indicator/IS.ACD.PCFT?locations=NP | read_url | ⚠️ 200 (no data) | World Bank indicator page loaded but no Nepal data |
| 57 | https://www.adb.org/countries/nepal/economy | read_url | ❌ 403 Forbidden | ADB blocked access |
| 58 | https://datacatalog.worldbank.org/search/dataset/0038132/Nepal-Financial-Sector | read_url | ❌ 502 Bad Gateway | World Bank catalog unreachable |

---

## G. Web Search Attempts

All web searches returned **no results** for NRB-related queries.

| # | Query | Method | Result |
|---|-------|--------|--------|
| 59 | "Nepal Rastra Bank payment system indicators monthly statistics 2024 2025 digital payments data" | web_search | ❌ No results |
| 60 | "NRB Nepal Rastra Bank payment system statistics report site:nrb.org.np" | web_search | ❌ No results |
| 61 | "Nepal digital payments statistics wallet mobile banking QR transactions data 2024" | web_search | ❌ No results |
| 62 | "site:nrb.org.np payment system statistics indicators" | web_search | ❌ No results |
| 63 | "Nepal digital payment growth wallet users QR transactions 2023 2024" | web_search | ❌ No results |
| 64 | "eSewa Khalti Nepal users transactions market share" | web_search | ❌ No results |
| 65 | "Nepal NRB eSewa Khalti digital wallet users transactions 2024 2025" | web_search | ❌ No results |
| 66 | "Nepal Rastra Bank payment system statistics report PDF download 2023 2024 2025" | web_search | ❌ No results |
| 67 | "Nepal Rastra Bank payment system department publications reports list" | web_search | ❌ No results |
| 68 | "Nepal NRB payment system data report PDF 2024" | web_search | ❌ No results |
| 69 | "Nepal Rastra Bank annual report 2024 payment system data PDF" | web_search | ❌ No results |

---

## Analysis

### Why did this fail?

1. **NRB website is completely down** — 500 errors on all 22 direct URL attempts. This is a server-side failure, not a URL structure issue.

2. **NRB payment system pages were never archived** — All 23 Wayback Machine attempts for payment-specific sub-pages returned 404. This suggests:
   - The payment system data may be behind a login or dynamic rendering
   - The pages may use JavaScript rendering that Wayback Machine couldn't capture
   - The payment system section may be a recent addition not yet archived
   - The URL structure may be different from what was assumed

3. **Web search API returned no results** — This may be a temporary API issue or a regional content limitation.

4. **Alternative data sources are limited** — Nepal's open data portal doesn't exist, World Bank doesn't have Nepal payment-specific data, and ADB blocked access.

### What this tells us about NRB's data publishing

From the confirmed homepage snapshots:
- NRB publishes **banking sector data** prominently (deposits, lending, CD ratio)
- NRB publishes **macroeconomic data** monthly (Current Macroeconomic and Financial Situation)
- NRB publishes **regulatory documents** including payment system directives
- NRB does **NOT** prominently display payment system statistics on the homepage
- The payment system department **exists** (confirmed by directive publication)

### Implication for the project

The "Payment System Statistics" publication may be:
1. Published in a section of the NRB website that wasn't archived
2. Embedded within the "Current Macroeconomic and Financial Situation" tables PDF
3. Published under a different name than assumed
4. Only available through direct NRB website access

**When the NRB website recovers, the first action should be to navigate to the Payment System Department section and document the exact publication structure.**

---

*Log created: August 2026*
*Total attempts: 69 (URL accesses + web searches)*
*Successful data extraction: 2 homepage snapshots*
*Payment system data found: 0*
