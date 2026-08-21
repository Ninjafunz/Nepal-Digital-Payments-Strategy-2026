# Phase 6 — Payment-Player Landscape

**Scope:** Nepal's licensed payment-institution universe and the evidence available for player-level analysis.

**As of:** 16 July 2025 for the registry; accessed 21 August 2026.

## Decision-useful result

The competitive unit is not a single homogeneous "digital-payment company" category. NRB separates **payment-system operators (PSOs)**—the clearing, switching, card-network and QR/interbank rails—from **payment-service providers (PSPs)**—the customer-facing payment-service layer. The regulatory universe at mid-July 2025 contained **9 PSOs and 23 PSPs**. This means national NRB channel statistics cannot support a defensible eSewa-versus-IME Khalti market-share calculation: they are rail/channel totals, not an issuer-level ledger.

The player registry is in `sources/payment_institutions_2025.csv`. It intentionally lists the major/identifiable institutions directly confirmed from NRB's Annex 1; it is not a full PSP directory. Use the official annex for the complete 23-PSP universe.

## Auditable infrastructure exception: NCHL

NCHL is the one major infrastructure player in the current scope with a public, comparable financial-report series. Its audited net profit rose from **NPR 354.6m in FY 2021/22** to **NPR 417.3m in FY 2024/25** (17.7% cumulative); operating profit rose from **NPR 563.0m** to **NPR 723.6m** (28.5%). In FY 2024/25, it processed **211m transactions** with settlement value above **NPR 18.6tn**. The series is stored in `sources/nchl_financials_fy2021_25.csv`.

This is infrastructure-company performance, not market share. NCHL's transaction count includes clearing and settlement systems and must not be added to the NRB channel totals or interpreted as unique retail-payment demand.

## Market structure

| Layer | Main actors | Economic role | What the project can measure now |
|---|---|---|---|
| Regulatory and settlement | NRB, RTGS participants | Rules, settlement and oversight | Official counts and system indicators |
| Network / infrastructure (PSO) | NCHL, Fonepay, SCT, card schemes, gateways | Clearing, switching, routing, interoperability | Rail-level volume/value; license registry |
| Consumer / merchant services (PSP) | eSewa, IME Khalti and other PSPs | Wallets, merchant acceptance, bill pay and customer interface | Licensed status; limited company-reported metrics |
| Bank-led distribution | Commercial banks and development banks | Deposit-account-linked mobile/internet banking and cards | Aggregated NRB channel series; BFI registry |

The first wallet merger is a structural change: Khalti and IME Pay operate as the unified **IME Khalti** entity in the mid-July 2025 NRB annex. Historical legacy-brand claims must therefore be labelled pre-merger and never be added to post-merger figures.

## Evidence matrix and data-quality gate

| Data needed for Phase 7 | Availability | Permitted use |
|---|---|---|
| National wallet, mobile-banking, QR and infrastructure activity | Complete in the corrected NRB monthly extract | Compare *channels/rails*, with double-counting caveat |
| Active PSP/PSO legal identity and licence | Complete at the 16 Jul 2025 cut-off | Build player universe and classify role |
| Individual PSP transactions, value, active users, merchants, revenue or take rate | Not publicly standardized in sources reviewed | Do **not** estimate market share or economics |
| Bank-level digital activity | Not present in the current monthly NRB extract | Use only if institution disclosures are separately sourced and time-aligned |
| NCHL financial reports | Publicly available, extraction not yet completed | Candidate source for infrastructure financial research |
| NCHL audited financials and total system throughput | Validated for FY 2021/22–2024/25 | Infrastructure profitability / scale trend only |

**Phase-6 gate: partially met.** The licensed-player universe and merger status are validated, but a validated player-level financial/operational dataset is not yet available. Phase 7 may proceed with a **channel- and rail-level** strategic assessment; player-market-share, unit-economics and financial-performance analyses remain out of scope until auditable company disclosures are collected.

## Implications for the next analysis

1. Frame "banks vs wallets" as a **use-case and channel** comparison, not as a winner-takes-all company market-share ranking.
2. Treat QR, wallet and bank-mobile figures as potentially overlapping payment records; they do not equal unique consumer transactions.
3. Separate infrastructure concentration from customer-facing PSP competition. A channel-mix HHI is not an operator or PSP HHI.
4. Use a separate event field for the Khalti–IME Pay merger when interpreting wallet adoption after July 2025.

## Sources

- **NRB009 (T1):** Nepal Rastra Bank, *Payment Systems Oversight Report 2024/25*, Annex 1, licensed institutions as of mid-July 2025. https://www.nrb.org.np/contents/uploads/2026/08/Payment-Oversight-Report-2024-25-1.pdf
- **NRB010 (T1):** Nepal Rastra Bank, *Payment Systems Indicators: Asar 2082* (mid-July 2025), including 9 PSOs, 23 PSPs, wallet and mobile-banking access indicators. https://www.nrb.org.np/psd/payment-systems-indicators-of-2082-asar/
- **KHL002 (T3):** Khalti / IME Khalti merger information. https://khalti.com/
- **NCH002 (T3):** NCHL financial reports index. https://nchl.com.np/financial-reports/
- **NCH003 (T2):** NCHL Annual Report 2078/79 (2021/22). https://nchl.com.np/wp-content/uploads/2023/12/Annual-Report-2078-79-2021-22.pdf
- **NCH004 (T2):** NCHL Annual Report 2079/80 (2022/23). https://nchl.com.np/wp-content/uploads/2024/04/NCHL_Annual-report-79-80.pdf
- **NCH005 (T2):** NCHL Annual Report 2080/81 (2023/24). https://nchl.com.np/wp-content/uploads/2025/01/Annual-Report-2080-81-2023-24.pdf
- **NCH006 (T2):** NCHL Annual Report 2081/82 (2024/25). https://nchl.com.np/wp-content/uploads/2025/12/NCHL-AR-2024-25.pdf

*This memo adds no unsourced company revenue, user, merchant, transaction, or market-share claim.*
