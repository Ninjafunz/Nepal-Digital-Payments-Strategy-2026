# Data Dictionary — Master Variable Catalogue

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

---

## Purpose

This document defines every variable the project will use. Each variable has a unique identifier, clear definition, specified unit, expected source, and traceable strategic use.

**Rule:** No variable may be used in analysis without first being defined in this document. If a new variable is needed, this document must be updated first.

---

## Variable Naming Convention

All variable names use `snake_case` and follow this structure:

```
{channel}_{metric}
```

Examples:
- `wallet_transaction_count` — wallet channel, count metric
- `qr_transaction_value` — QR channel, value metric
- `mobile_banking_users` — mobile banking, user metric

---

## Source Types

| Code | Type |
|------|------|
| T1 | Regulatory / Official (NRB) |
| T2 | Audited Financial |
| T3 | Company-Reported |
| T5 | Reputable Secondary |
| T7 | Analyst Inference / Derived |

---

## Section A: Adoption & Penetration Metrics

These variables measure the breadth of digital payment adoption.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| A01 | `wallet_accounts_total` | Total registered wallet accounts across all PSPs | Count | Monthly | Stock | T1: NRB | Adoption breadth |
| A02 | `wallet_active_users` | Active wallet accounts (transacted in period) | Count | Monthly | Stock | T1: NRB / T3: Company | Real adoption vs. registration |
| A03 | `mobile_banking_users` | Total registered mobile banking users across all BFIs | Count | Monthly | Stock | T1: NRB | Bank digital adoption |
| A04 | `mobile_banking_active_users` | Active mobile banking users (transacted in period) | Count | Monthly | Stock | T1: NRB | Real bank digital adoption |
| A05 | `internet_banking_users` | Total registered internet banking users | Count | Monthly | Stock | T1: NRB | Digital banking breadth |
| A06 | `internet_banking_active_users` | Active internet banking users | Count | Monthly | Stock | T1: NRB | Real internet banking adoption |
| A07 | `card_users_total` | Total card holders (debit + credit) | Count | Annual | Stock | T1: NRB / T2: Company | Card-based adoption |
| A08 | `debit_card_count` | Total debit cards issued | Count | Annual | Stock | T1: NRB | Debit penetration |
| A09 | `credit_card_count` | Total credit cards issued | Count | Annual | Stock | T1: NRB | Credit penetration |
| A10 | `atm_count` | Total ATMs deployed | Count | Monthly | Stock | T1: NRB | Cash access infrastructure |
| A11 | `pos_count` | Total POS terminals deployed | Count | Monthly | Stock | T1: NRB | Merchant acceptance infrastructure |
| A12 | `psp_count` | Number of licensed Payment Service Providers | Count | Annual | Stock | T1: NRB | Industry structure |
| A13 | `pso_count` | Number of licensed Payment System Operators | Count | Annual | Stock | T1: NRB | Infrastructure structure |
| A14 | `bfi_digital_count` | Number of BFIs offering digital payment services | Count | Annual | Stock | T1: NRB | Bank digital participation |
| A15 | `nepal_population` | Total Nepal population | Count | Annual | Stock | T5: World Bank / CBS | Market size context |

---

## Section B: Transaction Volume & Value

These variables measure the scale of digital payment activity.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| B01 | `wallet_transaction_count` | Total wallet payment transactions | Count | Monthly | Flow | T1: NRB | Wallet channel scale |
| B02 | `wallet_transaction_value` | Total value of wallet payment transactions | NPR | Monthly | Flow | T1: NRB | Wallet economic value |
| B03 | `mobile_banking_transaction_count` | Total mobile banking transactions | Count | Monthly | Flow | T1: NRB | Mobile banking scale |
| B04 | `mobile_banking_transaction_value` | Total value of mobile banking transactions | NPR | Monthly | Flow | T1: NRB | Mobile banking economic value |
| B05 | `internet_banking_transaction_count` | Total internet banking transactions | Count | Monthly | Flow | T1: NRB | Internet banking scale |
| B06 | `internet_banking_transaction_value` | Total value of internet banking transactions | NPR | Monthly | Flow | T1: NRB | Internet banking economic value |
| B07 | `qr_transaction_count` | Total QR code payment transactions | Count | Monthly | Flow | T1: NRB | QR channel adoption |
| B08 | `qr_transaction_value` | Total value of QR payment transactions | NPR | Monthly | Flow | T1: NRB | QR economic value |
| B09 | `pos_transaction_count` | Total POS transactions | Count | Monthly | Flow | T1: NRB | POS channel activity |
| B10 | `pos_transaction_value` | Total value of POS transactions | NPR | Monthly | Flow | T1: NRB | POS economic value |
| B11 | `card_transaction_count` | Total card payment transactions (POS + online) | Count | Monthly | Flow | T1: NRB | Card channel scale |
| B12 | `card_transaction_value` | Total value of card payment transactions | NPR | Monthly | Flow | T1: NRB | Card economic value |
| B13 | `connectips_transaction_count` | Total connectIPS transactions | Count | Monthly | Flow | T1: NRB / T3: NCHL | Infrastructure-level activity |
| B14 | `connectips_transaction_value` | Total value of connectIPS transactions | NPR | Monthly | Flow | T1: NRB / T3: NCHL | Infrastructure economic value |
| B15 | `ecommerce_transaction_count` | Total e-commerce payment transactions | Count | Monthly | Flow | T1: NRB | E-commerce channel |
| B16 | `ecommerce_transaction_value` | Total value of e-commerce transactions | NPR | Monthly | Flow | T1: NRB | E-commerce economic value |
| B17 | `total_digital_transaction_count` | Sum of all digital payment transactions across channels | Count | Monthly | Flow | T1: NRB / Derived | Total market size |
| B18 | `total_digital_transaction_value` | Sum of all digital payment transaction values | NPR | Monthly | Flow | T1: NRB / Derived | Total market value |

---

## Section C: Engagement & Intensity Metrics

These variables measure how deeply users engage with digital payments.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| C01 | `wallet_transactions_per_user` | wallet_transaction_count / wallet_active_users | Transactions/user | Monthly | Derived | T1: Derived | Wallet engagement depth |
| C02 | `mobile_banking_transactions_per_user` | mobile_banking_transaction_count / mobile_banking_active_users | Transactions/user | Monthly | Derived | T1: Derived | Mobile banking engagement |
| C03 | `wallet_avg_transaction_value` | wallet_transaction_value / wallet_transaction_count | NPR/transaction | Monthly | Derived | T1: Derived | Wallet use-case positioning |
| C04 | `mobile_banking_avg_transaction_value` | mobile_banking_transaction_value / mobile_banking_transaction_count | NPR/transaction | Monthly | Derived | T1: Derived | Mobile banking use-case |
| C05 | `qr_avg_transaction_value` | qr_transaction_value / qr_transaction_count | NPR/transaction | Monthly | Derived | T1: Derived | QR use-case positioning |
| C06 | `pos_avg_transaction_value` | pos_transaction_value / pos_transaction_count | NPR/transaction | Monthly | Derived | T1: Derived | POS use-case positioning |
| C07 | `card_avg_transaction_value` | card_transaction_value / card_transaction_count | NPR/transaction | Monthly | Derived | T1: Derived | Card use-case positioning |
| C08 | `digital_penetration_rate` | total_digital_transaction_count / nepal_population × 100 | % | Annual | Derived | T1 + T5: Derived | Population-level adoption |
| C09 | `digital_value_per_capita` | total_digital_transaction_value / nepal_population | NPR/person | Annual | Derived | T1 + T5: Derived | Economic intensity |
| C10 | `wallet_penetration_rate` | wallet_accounts_total / nepal_population × 100 | % | Annual | Derived | T1 + T5: Derived | Wallet market penetration |

---

## Section D: Market Structure & Competition

These variables measure competitive dynamics and concentration.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| D01 | `channel_transaction_value_share_{ch}` | channel value / total digital value × 100 for channel ch | % | Monthly | Derived | T1: Derived | Channel competitive position |
| D02 | `channel_transaction_count_share_{ch}` | channel count / total digital count × 100 for channel ch | % | Monthly | Derived | T1: Derived | Channel volume share |
| D03 | `wallet_market_share_value` | eSewa + Khalti wallet value / total wallet value × 100 | % | Annual | Derived | T1 + T3: Derived | Wallet market concentration |
| D04 | `channel_growth_rate_{ch}` | (channel_current - channel_previous) / channel_previous × 100 | % | Monthly | Derived | T1: Derived | Channel growth dynamics |
| D05 | `total_digital_growth_rate` | (total_current - total_previous) / total_previous × 100 | % | Monthly | Derived | T1: Derived | Market growth rate |
| D06 | `hhi_wallet` | Sum of squared market shares (by value) among wallet providers | Index | Annual | Derived | T1 + T3: Derived | Wallet market concentration |
| D07 | `hhi_digital_payments` | Sum of squared market shares (by value) across all digital channels | Index | Annual | Derived | T1: Derived | Overall market concentration |

---

## Section E: Merchant Ecosystem

These variables measure the acceptance side of the payments ecosystem.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| E01 | `merchant_count_total` | Total merchants accepting digital payments | Count | Annual | Stock | T1: NRB / T3: Company | Acceptance breadth |
| E02 | `merchant_count_qr` | Merchants accepting QR payments | Count | Annual | Stock | T1: NRB / T3: Company | QR acceptance coverage |
| E03 | `merchant_count_pos` | Merchants with POS terminals | Count | Annual | Stock | T1: NRB | POS acceptance coverage |
| E04 | `merchant_to_user_ratio` | merchant_count_total / wallet_active_users | Ratio | Annual | Derived | T1: Derived | Supply-demand balance |
| E05 | `merchant_growth_rate` | (merchant_current - merchant_previous) / merchant_previous × 100 | % | Annual | Derived | T1: Derived | Merchant-side network growth |
| E06 | `avg_merchant_transactions` | total merchant transactions / merchant_count_total | Transactions/merchant | Annual | Derived | T1 + T3: Derived | Merchant engagement intensity |
| E07 | `avg_merchant_value` | total merchant transaction value / merchant_count_total | NPR/merchant | Annual | Derived | T1 + T3: Derived | Merchant economic value |

---

## Section F: Value Chain & Economics

These variables measure the financial structure of the payments ecosystem.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| F01 | `fee_per_transaction_{ch}` | Average fee charged per transaction for channel ch | NPR/transaction | Annual | Flow | T3 / T7: Derived | Channel economics |
| F02 | `revenue_per_transaction_{ch}` | Average revenue earned per transaction for channel ch | NPR/transaction | Annual | Flow | T2 / T3: Derived | Channel revenue model |
| F03 | `float_income_{player}` | Estimated float income from held balances | NPR | Annual | Flow | T2 / T7: Derived | Float economics |
| F04 | `merchant_discount_rate` | Average merchant fee as % of transaction value | % | Annual | Flow | T3 / T7: Derived | Merchant economics |
| F05 | `interchange_rate` | Card interchange fee rate | % | Annual | Flow | T1 / T3: Derived | Card economics |
| F06 | `cost_to_serve_{ch}` | Estimated cost per transaction for channel ch | NPR/transaction | Annual | Flow | T2 / T7: Derived | Channel cost structure |
| F07 | `total_digital_revenue` | Estimated total digital payment revenue across ecosystem | NPR | Annual | Flow | T2 / T7: Derived | Profit pool estimation |
| F08 | `profit_margin_{player}` | Net income / revenue for player | % | Annual | Flow | T2: Company | Player profitability |

---

## Section G: Network Effects & Ecosystem

These variables measure ecosystem dynamics and network effects.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| G01 | `user_merchant_correlation` | Correlation between user growth and merchant growth over time | Correlation coefficient | Annual | Derived | T1: Derived | Cross-side network effects |
| G02 | `interoperability_score` | Degree of cross-platform transaction capability | Qualitative (1-5) | Annual | Qualitative | T1 / T4: Assessed | Interoperability impact |
| G03 | `switching_cost_indicator` | Qualitative assessment of user switching costs | Qualitative (1-5) | Annual | Qualitative | T1 / T5: Assessed | Lock-in potential |
| G04 | `platform_overlap_rate` | % of users active on multiple platforms | % | Annual | Derived | T3 / T5: Derived | Multi-homing behavior |
| G05 | `network_growth_rate` | Growth rate of total active users across all platforms | % | Monthly | Derived | T1: Derived | Ecosystem expansion |
| G06 | `acceptance_gap` | Difference between user growth rate and merchant growth rate | Percentage points | Annual | Derived | T1: Derived | Demand-supply imbalance |

---

## Section H: Regulatory Environment

These variables measure the regulatory context.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| H01 | `transaction_limit_wallet` | Maximum per-transaction limit for wallets | NPR | Event | Stock | T1 / T4: NRB | Regulatory constraint |
| H02 | `daily_limit_wallet` | Maximum daily transaction limit for wallets | NPR | Event | Stock | T1 / T4: NRB | Regulatory constraint |
| H03 | `kyc_requirement_level` | KYC tier required for various transaction levels | Qualitative | Event | Qualitative | T1 / T4: NRB | Adoption barrier |
| H04 | `interoperability_mandate_date` | Date of NRB interoperability mandate implementation | Date | Event | Stock | T1 / T4: NRB | Critical juncture |
| H05 | `regulatory_event_count` | Number of significant NRB regulatory actions per year | Count | Annual | Flow | T1 / T4: NRB | Regulatory intensity |

---

## Section I: Growth & Trend Metrics

These variables are derived from other variables to show trends.

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| I01 | `cagr_{metric}_{period}` | Compound annual growth rate for any metric | % | Annual | Derived | Derived | Long-term growth comparison |
| I02 | `yoy_growth_{metric}` | Year-over-year growth rate for any metric | % | Annual | Derived | Derived | Annual growth tracking |
| I03 | `mom_growth_{metric}` | Month-over-month growth rate for any metric | % | Monthly | Derived | Derived | Short-term momentum |
| I04 | `digital_share_of_gdp` | total_digital_transaction_value / GDP × 100 | % | Annual | Derived | T1 + T5: Derived | Economic significance |
| I05 | `cash_to_digital_ratio` | digital_transaction_value / total payment value × 100 | % | Annual | Derived | T1: Derived | Structural shift indicator |

---

## Section J: Company-Level Metrics

These variables are used for company-specific analysis (Phase 6+).

| ID | Variable Name | Definition | Unit | Frequency | Stock/Flow | Expected Source | Strategic Use |
|----|--------------|-----------|------|-----------|------------|----------------|---------------|
| J01 | `company_users` | Total registered users for a specific company | Count | Annual | Stock | T2 / T3: Company | Company scale |
| J02 | `company_active_users` | Active users for a specific company | Count | Annual | Stock | T2 / T3: Company | Company engagement |
| J03 | `company_transaction_volume` | Transaction count for a specific company | Count | Annual | Flow | T2 / T3: Company | Company activity |
| J04 | `company_transaction_value` | Transaction value for a specific company | NPR | Annual | Flow | T2 / T3: Company | Company economic scale |
| J05 | `company_revenue` | Total revenue for a specific company | NPR | Annual | Flow | T2: Company | Company financials |
| J06 | `company_net_income` | Net income for a specific company | NPR | Annual | Flow | T2: Company | Company profitability |
| J07 | `company_market_share` | Company value / total market value × 100 | % | Annual | Derived | T1 + T2/T3: Derived | Competitive position |
| J08 | `company_revenue_per_user` | company_revenue / company_active_users | NPR/user | Annual | Derived | T2 / T3: Derived | Monetization efficiency |
| J09 | `company_transactions_per_user` | company_transaction_volume / company_active_users | Txn/user | Annual | Derived | T2 / T3: Derived | User engagement |
| J10 | `company_avg_transaction_value` | company_transaction_value / company_transaction_volume | NPR/txn | Annual | Derived | T2 / T3: Derived | Use-case positioning |

---

## Summary Statistics

| Section | Variables | Direct Data | Derived |
|---------|-----------|-------------|---------|
| A: Adoption & Penetration | 15 | 14 | 1 |
| B: Transaction Volume & Value | 18 | 16 | 2 |
| C: Engagement & Intensity | 10 | 2 | 8 |
| D: Market Structure & Competition | 7 | 0 | 7 |
| E: Merchant Ecosystem | 7 | 4 | 3 |
| F: Value Chain & Economics | 8 | 1 | 7 |
| G: Network Effects & Ecosystem | 6 | 0 | 6 |
| H: Regulatory Environment | 5 | 4 | 1 |
| I: Growth & Trend Metrics | 5 | 0 | 5 |
| J: Company-Level Metrics | 10 | 4 | 6 |
| **Total** | **91** | **45** | **46** |

---

## Notes

1. **Variables marked "Derived"** are calculated from other variables and require the source data to be available first.
2. **Variables marked "Qualitative"** require human judgment and cannot be purely data-derived.
3. **Company-level variables (Section J)** are placeholders — specific companies will be added in Phase 6.
4. **This is a living document.** New variables may be added as analysis progresses. Any additions must follow the same format and include all fields.
5. **Channel-specific variables** use `{ch}` as a placeholder. In practice, `ch` will be one of: `wallet`, `mobile_banking`, `internet_banking`, `qr`, `pos`, `card`, `connectips`, `ecommerce`.

---

*Document status: Architecture complete. Variable definitions are established. No data has been collected.*
