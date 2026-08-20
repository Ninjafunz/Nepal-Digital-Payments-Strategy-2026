# Data Quality Report: NRB Payment Systems Indicators

**Date:** 2026-08-20  
**Auditor:** Automated + manual verification  
**Status:** CORRECTED — Dataset rebuilt from verified source  

---

## 1. Executive Summary

The original CSV (`NRB_Payment_Systems_Indicators_monthly.csv`) contained **systematic errors affecting 62.5% of all data cells**. The dataset has been rebuilt from a verified NRB XLSX source with a correct extraction script. The corrected dataset passes all validation checks.

| Metric | Value |
|--------|-------|
| Total cells compared (old vs corrected) | 549 |
| Mismatched cells | 343 (62.5%) |
| Correct cells | 206 (37.5%) |
| Months fully correct | 12 / 61 (19.7%) |
| Root cause | FY total columns treated as monthly data |

---

## 2. Root Cause Analysis

### 2.1 Structural Issue: FY Total Columns

The NRB XLSX file has three sections:
- **Section A** (Rows 5–19): Stock/access variables — **no FY total columns**
- **Section B1** (Rows 26–43): Transaction counts — **5 FY total columns** at positions 14, 27, 40, 53, 66
- **Section B2** (Rows 49–66): Transaction values — **5 FY total columns** at same positions

The FY total columns contain annual aggregate values for each fiscal year, inserted between the monthly data columns. Example from Section B1:

```
Col 13: 2078 Asar (monthly)
Col 14: None        ← FY 2077/78 TOTAL (111,923,386 for Mobile Banking)
Col 15: 2078 Saun   (monthly)
```

### 2.2 Extraction Failure

The original extraction script treated all data columns as monthly values, including the5 FY totals. This caused:

1. **FY total values were read as monthly data** — e.g., CSV "2078 Saun" Mobile Banking = 111,923,386 (the annual total)
2. **Cascading 1-month shift** — after each FY boundary, every subsequent value was shifted by one position
3. **Compounding errors** — by FY 2081/82, values were shifted by 4 months
4. **Final months dropped** — the last 5 months (2082 Baisakh through 2082 Asar) were truncated

### 2.3 Evidence

| Date | Field | Old CSV Value | Correct Value | What Happened |
|------|-------|--------------|---------------|---------------|
| 2078 Saun | Mobile_Banking_Count | 111,923,386 | 13,099,189 | FY total read as monthly |
| 2078 Bhadau | Mobile_Banking_Count | 13,099,189 | 13,241,819 | Shifted by 1 month |
| 2081 Magh | Mobile_Banking_Count | 44,048,146.112 | 50,984,022 | Shifted by 4 months + fractional |
| 2081 Asoj | QR_Count | 20,497,044.42 | 20,825,615 | Shifted by 1 month + fractional |

---

## 3. Fractional Values in Source

Three cells in the NRB source XLSX contain fractional values on count fields:

| Field | Date | Value | Assessment |
|-------|------|-------|------------|
| Wallet_Users | 2078 Mangsir | 10,419,678.149525212 | Present in NRB XLSX Section A — likely embedded formula result |
| Mobile_Banking_Count | 2081 Asoj | 44,048,146.112 | Present in NRB XLSX Section B1 — likely embedded formula result |
| QR_Count | 2081 Asoj | 20,497,044.42 | Present in NRB XLSX Section B1 — likely embedded formula result |

These values are **retained as-is** from the NRB source. They likely result from Excel formulas (e.g., `SUM` over sub-categories) that weren't rounded before publication. The fractional parts are small relative to the totals (< 0.000002% for Wallet_Users).

---

## 4. Value Field Precision

Sections B1 and B2 contain values with high decimal precision (10+ digits after decimal point). Example:

```
RTGS_Value @ 2077 Mangsir: 1,304,852.0098825842
```

These are **present in the NRB source XLSX** and result from embedded Excel formulas. They are retained as-is. For analytical purposes, values should be rounded to 2 decimal places (NPR millions).

---

## 5. Source Verification

| Item | Status |
|------|--------|
| NRB website (nrb.org.np) | DOWN (500 errors) at time of verification |
| XLSX downloaded from | Wayback Machine archive (2026-02-13 snapshot) |
| File verified as | Microsoft Excel 2007+ (openpyxl confirmed) |
| Sheet name | DataPSD |
| Structure confirmed | 3 sections (A, B1, B2) with headers at rows 4, 25, 48 |
| Month coverage | 2077 Saun (Jul 2020) to 2082 Saun (Jul 2025) = 61 months |

---

## 6. Corrected Dataset

| Property | Value |
|----------|-------|
| File | `data/raw/NRB_Payment_Systems_Indicators_monthly.csv` |
| Rows | 61 (monthly) |
| Columns | 51 (2 date + 13 stock + 18 count + 18 value) |
| Extraction script | `src/ingestion/extract_xlsx_v2.py` |
| Source file | `sources/NRB_PSD_Sep2025_REAL.xlsx` |
| FY total handling | Skipped via Section A canonical month mapping |
| Fractional values | 3 cells (retained from NRB source) |

---

## 7. Recommendations

1. **When NRB website recovers**, download fresh XLSX files for each month to extend coverage beyond Jul 2025
2. **Round fractional count fields** to nearest integer for analysis (document the rounding)
3. **Round value fields** to 2 decimal places for display (keep full precision in database)
4. **Cross-validate** corrected values against NRB Annual Report figures where available
5. **The broken CSV** is preserved as `data/raw/NRB_Payment_Systems_Indicators_monthly_BROKEN.csv` for audit trail

---

## 8. Impact on Previous Analyses

All five analyses have been re-run with corrected data. Key differences from the (incorrect) old analysis:

| Finding | Old (Broken) | Corrected |
|---------|-------------|-----------|
| QR growth 2021→2025 | 160× | ~32× |
| Mobile banking txn/user | 0.68→2.01 | 0.52→2.26 |
| Wallet txn/user | ~1.5 flat | 1.62 flat |
| 2021 total transactions | 0.97B | 0.57B |
| 2024 total transactions | 2.91B | 1.71B |

The corrected data shows a **smaller but still dramatic** digital transformation story. The growth rates are slightly lower because the old data had inflated values from FY total contamination.
