# Methodology Document — Research Constitution

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

---

## Purpose

This document is the **constitution** of the project. It governs how data is collected, evaluated, analyzed, and presented. Every methodological decision in the project must trace back to this document.

**If this document does not address a situation, the default is: state your assumption explicitly, flag it for review, and do not present inference as fact.**

---

## 1. Research Design

### 1.1 Overall Approach

This project uses a **mixed-methods research design** combining:

- **Quantitative analysis** of official and company-reported data (primary method)
- **Qualitative analysis** of regulatory documents, company disclosures, and industry reports (supporting method)
- **Strategic framework application** (Porter's Five Forces, PvP, strategic group mapping, scenario analysis)

The quantitative component provides the evidence base. The qualitative component provides context and interpretation. The strategic frameworks provide analytical structure.

### 1.2 Research Paradigm

This is **applied strategic research**, not academic social science. The purpose is to produce evidence-based strategic insight for an MSc Strategy dissertation. This means:

- We prioritize **relevance and rigor** over methodological purity
- We acknowledge limitations explicitly rather than hiding them
- We distinguish clearly between evidence and interpretation
- We are transparent about data gaps and their implications

### 1.3 Temporal Design

**Retrospective analysis** (2021–2026) with **forward-looking scenario projection** (2027–2030). The retrospective analysis is evidence-based. The scenario projection is framework-based and clearly marked as such.

---

## 2. Data Hierarchy

When sources conflict, this hierarchy governs. Higher tiers take precedence.

### Tier Structure

| Tier | Classification | Description | Examples |
|------|---------------|-------------|----------|
| **Tier 1** | Nepal Rastra Bank — Official Statistics | Published statistical data from NRB | Payment System Indicators, monthly payment statistics, NRB annual reports, monetary policy data |
| **Tier 2** | Audited Financial Information | Audited financial statements and annual reports of regulated entities | Company annual reports with auditor opinions, NRB-supervised institution disclosures |
| **Tier 3** | Official Company Disclosures | Regulated filings and official company-published data | PSP disclosures to NRB, press releases with specific metrics, investor presentations |
| **Tier 4** | Regulatory Publications | NRB guidelines, circulars, and directives (not statistical data) | Payment system directives, interoperability mandates, licensing decisions |
| **Tier 5** | Reputable Secondary Sources | Established industry reports and academic research | Nepal government reports, World Bank/IMF publications, academic papers |
| **Tier 6** | News and Media | Reporting from reputable outlets | Kantipur, The Kathmandu Post, Nepal Telecom Authority reports |
| **Tier 7** | Analyst Inference | Our own derived calculations and estimates | Growth rate calculations, market share estimates, scenario projections |

### Hierarchy Rules

1. **Higher tiers take precedence** over lower tiers when sources conflict.
2. **A higher-tier source can be supplemented** by lower-tier sources for context, but not contradicted.
3. **A lower-tier source can override a higher-tier source** only with **explicit written justification** in the source register, explaining why the higher-tier source is incomplete or misleading for that specific use case.
4. **Tier 7 (analyst inference) must always be clearly marked** as derived/estimated and must never be presented without its source data.
5. **Tier 6 (media) cannot be the sole source** for any quantitative claim that could be verified against Tiers 1–5.

### Application Example

| Scenario | Resolution |
|----------|-----------|
| NRB says 50 million wallet transactions; eSewa press release says 60 million | Use NRB figure (Tier 1 > Tier 3) |
| NRB data shows aggregate wallet data; eSewa provides company-specific breakdown | Use both — NRB for industry total, eSewa for company-level with clear source tagging |
| A news article reports a market share figure; NRB data exists but doesn't calculate market share | Use NRB data to calculate independently (Tier 1 + Tier 7, not Tier 6) |
| No Tier 1–5 data exists for a specific variable | Use Tier 6 with explicit caveat; flag as needing validation |

---

## 3. Source-Type Taxonomy

Every source in the project must be classified with one of these type codes:

| Code | Type | Description | Reliability Assessment |
|------|------|-------------|----------------------|
| `T1` | Regulatory / Official | NRB publications, government statistics | Highest — official, audited, regulated |
| `T2` | Audited Financial | Company annual reports, audited financials | High — independently verified |
| `T3` | Company-Reported | Press releases, disclosures, presentations | Medium — self-reported, not independently verified |
| `T4` | Regulatory Publication | Guidelines, circulars, directives | High for content, N/A for data |
| `T5` | Reputable Secondary | Academic papers, established industry reports | Medium-High — depends on methodology |
| `T6` | Media / News | News outlets, journalism | Medium — subject to reporting accuracy |
| `T7` | Analyst Inference | Our own calculations, estimates, projections | Variable — depends on underlying data quality |

### Source Evaluation Criteria

When assessing a source, evaluate:

1. **Authority** — Who produced it? What is their mandate or incentive?
2. **Methodology** — How was the data collected and processed?
3. **Timeliness** — How current is the data?
4. **Consistency** — Does it align with other reliable sources?
5. **Transparency** — Is the methodology disclosed?
6. **Completeness** — Does it cover the full population or a sample?

---

## 4. Data Collection Strategy

### 4.1 Primary Data Sources

**Nepal Rastra Bank (NRB)** is the primary data source. Relevant NRB publications include:

- Payment System Indicators (monthly)
- Payment System statistics publications
- NRB Annual Reports
- Monetary Policy statements
- Financial Stability Reports
- Banking and financial statistics publications
- NRB circulars and directives

### 4.2 Company Data Sources

For company-specific data:

| Source Type | Examples | Use Case |
|-------------|----------|----------|
| Audited financials | eSewa annual reports, bank annual reports | Revenue, cost, profitability data |
| Company disclosures | Press releases, official websites, investor presentations | User counts, transaction volumes |
| Regulated filings | NRB-supplied data, NEPSE filings | Compliance data, financial metrics |

**Rule:** Company-reported data (T3) must be cross-referenced against NRB data (T1) where possible. If no T1 data exists for a company-specific metric, use T3 with explicit source tagging.

### 4.3 Industry and Market Data

| Source Type | Examples | Use Case |
|-------------|----------|----------|
| Government statistics | Nepal government reports, CBS data | Economic context, demographics |
| International organizations | World Bank, IMF, ITU, GSMA | Regional comparisons, benchmarks |
| Industry bodies | Nepal Telecom Authority | Telecom context for mobile payments |
| Academic research | Published papers on Nepal payments | Literature review, methodology |

### 4.4 Data Collection Rules

1. **Collect metadata before data.** For every dataset, document: source, date, format, coverage, methodology, caveats.
2. **Download original files.** Store raw data in `data/raw/` exactly as received. Never modify the original.
3. **Record every transformation.** Any cleaning, transformation, or calculation must be documented and reproducible.
4. **Timestamp everything.** Source register entries must include access date.
5. **Verify file integrity.** Check that downloaded files match expected format and content.

---

## 5. Analytical Framework

### 5.1 Strategic Analysis Tools

| Framework | Application | Phase |
|-----------|------------|-------|
| **Industry Structure Analysis (Porter's Five Forces)** | Competitive dynamics in payments ecosystem | Phase 7 |
| **Strategic Group Mapping** | Identifying clusters of similar players | Phase 7 |
| **Value Chain Analysis** | Mapping where value is created and captured | Phase 7 |
| **Profit Pool Analysis (PvP)** | Estimating profit distribution across ecosystem | Phase 7 |
| **Network Effects Assessment** | Evaluating competitive moat potential | Phase 7 |
| **Scenario Analysis** | Constructing plausible industry futures | Phase 8 |
| **Capability Analysis** | Identifying strategic capabilities under each scenario | Phase 8 |

### 5.2 Quantitative Analysis Methods

| Method | Application | Data Required |
|--------|------------|---------------|
| **Time-series analysis** | Adoption trajectories, growth trends | Monthly/annual data over time |
| **Market share analysis** | Channel and player competitive positions | Volume/value data by channel and player |
| **Concentration analysis (HHI)** | Market structure assessment | Market share data |
| **Growth decomposition** | Understanding what drives market growth | Disaggregated growth data |
| **Ratio analysis** | Engagement, efficiency, economics metrics | Multiple related metrics |
| **Correlation analysis** | Network effects, driver identification | Paired time-series data |
| **Regression analysis** | Driver identification (if data permits) | Multiple variables over time |

### 5.3 Analysis Quality Standards

1. **Every analysis must state its data sources explicitly.** No "according to industry reports" — cite the specific source.
2. **Every calculation must be reproducible.** All code must be in the repository.
3. **Every chart must include source attribution.** Source, date, and any transformations must be noted.
4. **Confidence levels must be stated.** Distinguish between "the data shows X" and "this suggests X."
5. **Limitations must be acknowledged.** Every analysis section ends with limitations.

---

## 6. Data Engineering Standards

### 6.1 Database Principles

1. **Every observation must have a `source_id`** linking it to the source register. This is non-negotiable.
2. **Raw data is immutable.** Files in `data/raw/` are never modified after download.
3. **Transformations are recorded.** The `data/processed/` directory contains data with transformation logs.
4. **Final data is analysis-ready.** Files in `data/final/` are ready for direct use in analysis.
5. **The database is the single source of truth** for all analytical queries.

### 6.2 Data Pipeline

```
NRB website → Download → data/raw/ → Validate → data/processed/ → Transform → data/final/ → payments.db → analysis/
```

Each step is documented, versioned, and reproducible.

### 6.3 Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Raw data files | `{source}_{dataset}_{YYYY-MM}.csv` | `NRB_payment_indicators_2026-01.csv` |
| Processed files | `{step}_{dataset}_{YYYY-MM}.csv` | `validated_NRB_payment_indicators_2026-01.csv` |
| Final files | `{analysis}_{dataset}.csv` | `channel_growth_rates_2021_2026.csv` |
| Database tables | `snake_case` | `monthly_payment_metrics` |
| Variables | `snake_case` | `wallet_transaction_count` |

---

## 7. Validity Threats

### 7.1 Data Quality Threats

| Threat | Mitigation |
|--------|-----------|
| **Incomplete NRB data** | Cross-reference multiple NRB publications; flag gaps explicitly |
| **Definition changes over time** | Document all definition changes; adjust or flag affected observations |
| **Reporting lag** | Use most recent available data; document publication dates |
| **Stock vs. flow confusion** | Verify variable type before inclusion; document in data dictionary |
| **Selection bias** | Use full-population NRB data where possible; acknowledge when using samples |
| **FY total columns in NRB XLSX** | Skip columns whose headers contain `FY`; use Section A as the canonical month list. See `analysis/data_quality_report.md`. |
| **Channel double-counting** | NRB may record the same payment under more than one channel (e.g. QR and wallet). Summing all channels overstates unique payments; treat totals as reported-channel activity, not unique payments. |
| **Cash / cheque / wholesale in “digital” totals** | ATM cash withdrawal, ECC, and RTGS are not retail electronic payments. Headline “digital retail” series exclude these three codes. |
| **Bikram Sambat → Gregorian labels** | Month labels use the dominant Gregorian month (e.g. Saun → July). This is not a day-accurate calendar conversion. |
| **Partial calendar years** | 2020 starts in July and 2025 ends in July. CAGR and YoY use full calendar years 2021–2024 unless a partial-year note is attached. |
| **HHI on channels ≠ firm concentration** | Channel-mix HHI from NRB rails is not bank/PSP market concentration. |

### 7.2 Analytical Threats

| Threat | Mitigation |
|--------|-----------|
| **Correlation ≠ causation** | Never claim causation from correlation alone; use frameworks for causal reasoning |
| **Survivorship bias** | Include failed/exited players where data permits; acknowledge gaps |
| **Present bias** | Use historical data, not current snapshots; show trends |
| **Confirmation bias** | Test hypotheses against evidence; report disconfirming evidence |
| **Overfitting** | Use simple models; validate out-of-sample where possible |

### 7.3 Presentation Threats

| Threat | Mitigation |
|--------|-----------|
| **Cherry-picking data** | Present complete datasets; show all relevant data, not just supporting data |
| **Misleading visualizations** | Use appropriate scales; show zero baselines; label clearly |
| **Conflation of evidence and opinion** | Clearly mark analyst inference (T7); separate findings from recommendations |
| **Overconfidence** | State confidence levels; acknowledge uncertainty |

---

## 8. Ethical Considerations

### 8.1 Research Ethics

1. **No misrepresentation.** Data and sources are never fabricated, altered, or selectively presented to support a predetermined conclusion.
2. **Transparency.** All data sources, methods, and limitations are disclosed.
3. **Fair representation.** Competitors and market participants are represented accurately and fairly.
4. **No insider information.** All data used is publicly available or officially published.

### 8.2 Data Ethics

1. **No personal data.** This project uses aggregate industry data, not individual consumer data.
2. **No proprietary data misuse.** Company-specific data is used only from public disclosures.
3. **Attribution.** All sources are properly attributed.

### 8.3 Academic Integrity

1. **AI-assisted research.** AI tools (Antigravity/Codebuff) are used for data collection, engineering, and repetitive analysis. Strategic judgments, interpretations, and conclusions are made by the researcher.
2. **Disclosure.** The role of AI tools in the research process will be disclosed in the final report.
3. **Original analysis.** All strategic frameworks and their application to Nepal's payments ecosystem are the researcher's original work.

---

## 9. Quality Assurance Process

### 9.1 Data Quality Checks

Before any analysis:

1. **Source Audit:** Verify every data point has a valid source_id
2. **Completeness Check:** Identify missing months/observations
3. **Consistency Check:** Verify definitions are consistent across time periods
4. **Duplicate Check:** Identify and resolve duplicate observations
5. **Range Check:** Identify impossible or outlier values
6. **Methodology Check:** Identify definition or methodology changes

All checks documented in `analysis/data_quality_report.md`.

### 9.2 Analysis Quality Checks

Before presenting any finding:

1. **Source Verification:** Is the finding supported by the data?
2. **Alternative Explanation:** Could the data support a different conclusion?
3. **Sensitivity Check:** Does the finding hold under different assumptions?
4. **Limitation Check:** Are limitations acknowledged?
5. **Source Tag:** Is every data point tagged with its source?

### 9.3 Peer Review (Self-Review Protocol)

For each major analytical output:

1. Read the analysis as if you were a skeptical reviewer
2. Ask: "What would a competitor say to undermine this analysis?"
3. Ask: "What data would change this conclusion?"
4. Document weaknesses proactively

---

## 10. Project Governance

### 10.1 Decision Log

All significant methodological decisions are logged in this document or in a dedicated decision log. A decision is significant if it affects:

- Data scope or sources
- Analytical methods
- Presentation of findings
- Interpretation of results

### 10.2 Version Control

- All files are version-controlled via Git
- Database changes are version-controlled via migration scripts
- Methodology changes require documentation in this document

### 10.3 Review Points

| Review | Timing | Purpose |
|--------|--------|---------|
| Architecture Review | Phase 1 (NOW) | Validate research design and methodology |
| Data Quality Review | Phase 4 | Validate data before analysis |
| Analysis Review | Phase 5–7 | Validate findings before synthesis |
| Final Review | Phase 9 | Complete project review |

---

*Document status: Architecture complete. This is the research constitution. All subsequent work must comply with this document.*
