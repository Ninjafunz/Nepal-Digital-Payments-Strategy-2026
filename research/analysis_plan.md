# Analysis Plan

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

---

## Purpose

This document maps each research theme to specific analyses, data requirements, methods, and expected outputs. It is the operational roadmap for all analytical work.

---

## Phase Sequence

```
Phase 1: Architecture (NOW)
    ↓
Phase 2: Data Inventory — identify available NRB datasets
    ↓
Phase 3: Data Engineering — database, ingestion, first NRB dataset
    ↓
Phase 4: Data Validation — quality audit
    ↓
Phase 5: Core Analyses (1–5 below)
    ↓
Phase 6: Company Research — player-level data
    ↓
Phase 7: Strategic Analyses (6–10 below)
    ↓
Phase 8: Scenarios (11–14 below)
    ↓
Phase 9: Synthesis & Report
```

---

## Core Analyses (Phase 5)

These five analyses form the foundation. They must be completed before any strategic interpretation.

---

### Analysis 1: Is Nepal Actually Becoming More Digital?

**Theme:** Digital Payment Adoption (H1)

**Question:** What is the trajectory of digital payment adoption in Nepal (2021–2026)?

**Data Required:**

| Variable | Source |
|----------|--------|
| `total_digital_transaction_count` (B17) | NRB001 |
| `total_digital_transaction_value` (B18) | NRB001 |
| `nepal_population` (A15) | GOV001 |
| `digital_share_of_gdp` (I04) | NRB001 + INT001 |
| `cash_to_digital_ratio` (I05) | NRB001 |

**Method:**

1. Plot total digital transaction count and value over time (2021–2026)
2. Calculate CAGR for both count and value
3. Calculate digital share of GDP over time
4. Compare digital payment growth rate to GDP growth rate
5. Assess whether growth shows inflection points (structural shift vs. linear growth)

**Expected Output:**

- Chart: Total digital payment volume and value over time
- Chart: Digital payment CAGR vs. GDP CAGR
- Chart: Digital share of GDP trend
- Narrative: Assessment of whether adoption represents structural shift

**Hypothesis Test:**

- H1 is **supported** if digital payment growth significantly outpaces GDP growth and shows inflection points
- H1 is **rejected** if growth is proportional to GDP growth with no structural acceleration

---

### Analysis 2: Which Payment Channels Are Winning?

**Theme:** Payment-Channel Evolution (H3)

**Question:** How is the channel mix changing and which channels are gaining share?

**Data Required:**

| Variable | Source |
|----------|--------|
| `wallet_transaction_count/value` (B01, B02) | NRB001 |
| `mobile_banking_transaction_count/value` (B03, B04) | NRB001 |
| `internet_banking_transaction_count/value` (B05, B06) | NRB001 |
| `qr_transaction_count/value` (B07, B08) | NRB001 |
| `pos_transaction_count/value` (B09, B10) | NRB001 |
| `card_transaction_count/value` (B11, B12) | NRB001 |
| `connectips_transaction_count/value` (B13, B14) | NRB001 |
| `ecommerce_transaction_count/value` (B15, B16) | NRB001 |

**Method:**

1. Calculate `channel_transaction_value_share_{ch}` (D01) for each channel over time
2. Calculate `channel_transaction_count_share_{ch}` (D02) for each channel over time
3. Calculate `channel_growth_rate_{ch}` (D04) for each channel
4. Plot share evolution and growth rate comparison
5. Identify channel substitution patterns (are new channels growing at the expense of others?)

**Expected Output:**

- Chart: Channel share evolution (stacked area or line chart)
- Chart: Channel growth rate comparison (bar chart)
- Table: Channel metrics summary (count, value, share, growth)
- Narrative: Channel competitive dynamics

**Hypothesis Test:**

- H3 is **supported** if QR shows highest growth rate and growing share
- H3 is **rejected** if QR growth is not significantly above other channels

---

### Analysis 3: Are Users Actually Engaging?

**Theme:** Consumer Engagement (H4)

**Question:** Are users transacting more frequently and with higher values over time?

**Data Required:**

| Variable | Source |
|----------|--------|
| `wallet_transaction_count/value` (B01, B02) | NRB001 |
| `wallet_active_users` (A02) | NRB001 |
| `mobile_banking_transaction_count/value` (B03, B04) | NRB001 |
| `mobile_banking_active_users` (A04) | NRB001 |
| All channel transaction count/value (B01–B16) | NRB001 |
| All channel active users (A02, A04, A06) | NRB001 |

**Method:**

1. Calculate `wallet_transactions_per_user` (C01) over time
2. Calculate `mobile_banking_transactions_per_user` (C02) over time
3. Calculate `wallet_avg_transaction_value` (C03) over time
4. Calculate `mobile_banking_avg_transaction_value` (C04) over time
5. Calculate `qr_avg_transaction_value` (C05) over time
6. Compare engagement metrics across channels
7. Compare engagement trends over time

**Expected Output:**

- Chart: Transactions per user over time (wallet vs. mobile banking)
- Chart: Average transaction value over time (by channel)
- Table: Engagement metrics summary
- Narrative: Engagement dynamics and channel positioning

**Hypothesis Test:**

- H4 is **supported** if wallet transactions per user > mobile banking transactions per user, and wallet avg transaction value < mobile banking avg transaction value
- H4 is **rejected** if patterns differ from this hypothesis

**Why This Matters:** "Users increased" is not a finding. "Users are transacting 3x more frequently" is a finding. Engagement depth is strategically more important than registration breadth.

---

### Analysis 4: Is the Market Concentrating?

**Theme:** Market Structure (D06, D07)

**Question:** Is digital payment activity becoming concentrated among fewer players/channels?

**Data Required:**

| Variable | Source |
|----------|--------|
| Channel value shares (D01) | NRB001 (derived) |
| `wallet_market_share_value` (D03) | NRB001 + company data |
| `hhi_digital_payments` (D07) | NRB001 (derived) |
| `hhi_wallet` (D06) | NRB001 + company data |

**Method:**

1. Calculate HHI for overall digital payments: HHI = Σ(si²) where si = market share of channel i
2. Calculate HHI for wallet segment (requires company-level data)
3. Track HHI over time to assess concentration trends
4. Compare to benchmarks (HHI < 1,500 = unconcentrated; 1,500–2,500 = moderate; > 2,500 = concentrated)

**Expected Output:**

- Chart: HHI trend over time
- Table: Market shares by channel and player
- Narrative: Concentration assessment and implications

**Hypothesis Test:**

- If HHI is increasing → market is concentrating
- If HHI is decreasing → market is fragmenting
- If HHI is stable → market structure is stable

**Note:** This analysis may be limited if company-level data (T3) is insufficient for wallet market shares. In that case, channel-level HHI will be the primary metric, with wallet HHI flagged as requiring more data.

---

### Analysis 5: Where Is Economic Value Moving?

**Theme:** Value-Chain Economics (H9, H10)

**Question:** How does the economic value of different channels compare, and where is value migrating?

**Data Required:**

| Variable | Source |
|----------|--------|
| All channel transaction count/value (B01–B16) | NRB001 |
| `qr_avg_transaction_value` (C05) | NRB001 (derived) |
| `pos_avg_transaction_value` (C06) | NRB001 (derived) |
| `card_avg_transaction_value` (C07) | NRB001 (derived) |
| `channel_transaction_value_share_{ch}` (D01) | NRB001 (derived) |

**Method:**

1. Plot transaction count vs. transaction value for each channel
2. Create a "channel positioning map" with count on x-axis and value on y-axis
3. Track how each channel moves on this map over time
4. Identify which channels are "high-frequency, low-value" vs. "low-frequency, high-value"
5. Assess value migration patterns

**Expected Output:**

- Chart: Channel positioning map (count vs. value)
- Chart: Channel value trajectory over time
- Table: Channel economics comparison
- Narrative: Value migration patterns and strategic implications

**Why This Matters:** This analysis can reveal one of the project's most interesting insights. If wallets are becoming high-frequency, low-value engagement platforms while banks retain high-value transactions, this has profound strategic implications for profit pools and competitive advantage.

---

## Strategic Analyses (Phase 7)

These analyses require company-level data (Phase 6) and build on core analyses.

---

### Analysis 6: Banks vs. Wallets — Who Is Winning?

**Theme:** Banks vs. Wallets vs. Infrastructure (H6)

**Data Required:**

| Variable | Source |
|----------|--------|
| `mobile_banking_*` (B03, B04, C02, C04) | NRB001 |
| `wallet_*` (B01, B02, C01, C03) | NRB001 |
| `connectips_*` (B13, B14) | NRB001 |
| Company-level data for major banks and wallets | T2/T3 |

**Method:**

1. Compare bank mobile banking vs. wallet growth trajectories
2. Compare engagement metrics (transactions/user, avg transaction value)
3. Assess whether banks and wallets serve different use cases or directly compete
4. Analyze customer overlap (if data permits)

**Expected Output:**

- Comparative growth chart (bank digital vs. wallet)
- Channel positioning comparison
- Strategic assessment of bank vs. wallet competitive dynamics

---

### Analysis 7: Network Effects Assessment

**Theme:** Network Effects (H7)

**Data Required:**

| Variable | Source |
|----------|--------|
| `user_merchant_correlation` (G01) | NRB001 (derived) |
| `merchant_to_user_ratio` (E04) | NRB001 (derived) |
| `acceptance_gap` (G06) | NRB001 (derived) |
| `switching_cost_indicator` (G03) | Qualitative |
| `interoperability_score` (G02) | T4 (NRB directives) |

**Method:**

1. Calculate correlation between user growth and merchant growth
2. Assess whether merchant growth is lagging user growth (acceptance gap)
3. Evaluate switching costs based on interoperability mandates
4. Assess whether network effects are approaching tipping point

**Expected Output:**

- Network effects assessment matrix
- Merchant-to-user ratio trend
- Switching cost and interoperability analysis

---

### Analysis 8: Customer Ownership Mapping

**Theme:** Customer Ownership (H8)

**Data Required:**

| Variable | Source |
|----------|--------|
| All adoption and engagement metrics | NRB001 |
| `platform_overlap_rate` (G04) | T3/T5 |
| Company-level data | T2/T3 |

**Method:**

1. Map the customer journey from initiation to settlement
2. Identify which layer "owns" the customer at each step
3. Assess whether interface ownership (wallet apps) is displacing account ownership (banks)
4. Evaluate data access and control by player type

**Expected Output:**

- Customer ownership map (visual)
- Assessment of ownership shift trajectory
- Strategic implications of ownership dynamics

---

### Analysis 9: Value Chain & Profit Pool Estimation

**Theme:** Value-Chain Economics (H9, H10)

**Data Required:**

| Variable | Source |
|----------|--------|
| `fee_per_transaction_{ch}` (F01) | T2/T3/T7 |
| `revenue_per_transaction_{ch}` (F02) | T2/T3 |
| `merchant_discount_rate` (F04) | T3/T7 |
| `interchange_rate` (F05) | T1/T3 |
| `total_digital_revenue` (F07) | T2/T7 |
| `profit_margin_{player}` (F08) | T2 |

**Method:**

1. Estimate total digital payment revenue pool
2. Decompose revenue by source (fees, float, data, ancillary services)
3. Map profit distribution across ecosystem layers
4. Identify which profit pools are growing and which are shrinking

**Expected Output:**

- Profit pool map (visual)
- Revenue decomposition by channel and player type
- Value chain economics assessment

---

### Analysis 10: Strategic Group Mapping

**Theme:** Strategic Groups (H12), Competitive Advantage (H13)

**Data Required:**

| Variable | Source |
|----------|--------|
| All company-level metrics (J01–J10) | T2/T3 |
| Channel positioning data | NRB001 |
| Product range data | T3 |

**Method:**

1. Identify key strategic dimensions (from data, not assumption)
2. Plot players on multi-dimensional map
3. Identify clusters (strategic groups)
4. Assess group mobility over time
5. Map competitive advantages by group

**Expected Output:**

- Strategic group map (visual)
- Competitive advantage assessment
- Group dynamics narrative

---

## Scenario Analyses (Phase 8)

---

### Analyses 11–14: Industry Scenarios for 2027–2030

**Theme:** Industry Scenarios (H14)

**Scenario A: Platform Consolidation**

> One or two major platforms gain strong network effects, creating winner-take-most dynamics.

**Scenario B: Interoperability**

> Multiple platforms coexist because switching costs remain low and interoperability mandates prevent lock-in.

**Scenario C: Bank-Led Digital Ecosystems**

> Banks leverage customer accounts, deposits, and financial products to dominate digital relationships.

**Scenario D: Hybrid / Regulated Pluralism**

> A mixed outcome where platforms lead in payments but regulation prevents full consolidation, and banks retain strength in financial products.

**Method:**

1. Define key uncertainties (network effect strength, regulatory direction, technology development)
2. Construct scenario matrix based on two most critical uncertainties
3. For each scenario, identify: what must be true, leading indicators, strategic capabilities that matter
4. Map current players to their positioning under each scenario
5. Identify robust strategies (work across multiple scenarios)

**Expected Output:**

- Scenario framework (2×2 matrix or alternative)
- Scenario narratives
- Capability-scenario mapping
- Leading indicator dashboard
- Strategic recommendation per scenario

---

## Analysis Dependencies

```
Analysis 1 (Adoption) ──────────────────┐
Analysis 2 (Channels) ──────────────────┤
Analysis 3 (Engagement) ────────────────┼──→ Analysis 6 (Banks vs Wallets)
Analysis 4 (Concentration) ─────────────┤    Analysis 7 (Network Effects)
Analysis 5 (Value Migration) ───────────┘    Analysis 8 (Customer Ownership)
                                             Analysis 9 (Profit Pools)
                                             Analysis 10 (Strategic Groups)
                                                    │
                                                    ↓
                                             Analyses 11–14 (Scenarios)
```

---

## Timeline Estimate

| Phase | Duration | Dependencies |
|-------|----------|-------------|
| Phase 1: Architecture | Complete | — |
| Phase 2: Data Inventory | 1–2 days | Phase 1 |
| Phase 3: Data Engineering | 2–3 days | Phase 2 |
| Phase 4: Data Validation | 1–2 days | Phase 3 |
| Phase 5: Core Analyses | 3–5 days | Phase 4 |
| Phase 6: Company Research | 3–5 days | Phase 5 |
| Phase 7: Strategic Analyses | 3–5 days | Phase 6 |
| Phase 8: Scenarios | 2–3 days | Phase 7 |
| Phase 9: Synthesis | 3–5 days | Phase 8 |
| **Total** | **~20–30 days** | |

---

## Quality Gates

Before moving from one phase to the next:

| Gate | Check |
|------|-------|
| Phase 1 → 2 | Architecture reviewed and approved |
| Phase 2 → 3 | NRB data inventory complete and verified |
| Phase 3 → 4 | Database created, first dataset imported |
| Phase 4 → 5 | Data quality report complete, issues resolved |
| Phase 5 → 6 | Core analyses complete, hypotheses tested |
| Phase 6 → 7 | Company data collected and validated |
| Phase 7 → 8 | Strategic analyses complete |
| Phase 8 → 9 | Scenarios constructed, capability mapping done |

---

*Document status: Architecture complete. Analyses are planned. No data collected or analyzed.*
