# Database Schema — payments.db

**Project:** From Cash to Platforms: The Transformation of Nepal's Digital Payments Industry, 2021–2026

---

## Purpose

This document defines the relational database schema for the project's SQLite database. The database is the **single source of truth** for all analytical queries.

**Critical principle:** Every observation in the database must reference a `source_id` from the source register. This makes the entire dataset auditable.

---

## Design Principles

1. **Source provenance is non-negotiable.** Every row links to a source.
2. **Normalization where useful.** Channels, institutions, and sources are reference tables.
3. **Denormalization where practical.** Monthly metrics are stored in wide format for analytical convenience.
4. **Raw data is never in the database.** Only processed and validated data.
5. **Schema is version-controlled.** Changes are documented and migrated.

---

## Entity-Relationship Diagram (Textual)

```
┌─────────────┐       ┌──────────────────────────┐       ┌─────────────┐
│  channels   │──────<│  monthly_payment_metrics  │>──────│   sources   │
│             │       │                          │       │             │
│ channel_id  │       │ date                     │       │ source_id   │
│ channel_name│       │ channel_id               │       │ institution │
│ channel_type│       │ transaction_count        │       │ document    │
│ description │       │ transaction_value        │       │ date        │
│ is_active   │       │ source_id                │       │ url         │
└─────────────┘       └──────────────────────────┘       │ tier        │
                                                          │ reliability │
┌─────────────┐       ┌──────────────────────────┐       └─────────────┘
│institutions │──────<│institution_metrics       │
│             │       │                          │
│institution │       │ date                     │
│ _id        │       │ institution_id           │
│ name       │       │ metric_name              │
│ type       │       │ metric_value             │
│ category   │       │ unit                     │
│ is_active  │       │ source_id                │
└─────────────┘       └──────────────────────────┘

┌─────────────┐       ┌──────────────────────────┐
│  banks      │──────<│ bank_digital_metrics     │
│             │       │                          │
│ bank_id     │       │ date                     │
│ name        │       │ bank_id                  │
│ bfi_type    │       │ metric_name              │
│ is_active   │       │ metric_value             │
│             │       │ unit                     │
│             │       │ source_id                │
└─────────────┘       └──────────────────────────┘

┌─────────────┐       ┌──────────────────────────┐
│  merchants  │       │regulatory_events         │
│             │       │                          │
│ merchant_id │       │ event_id                 │
│ name        │       │ date                     │
│ type        │       │ title                    │
│ channel     │       │ description              │
│ source_id   │       │ impact_assessment        │
│             │       │ source_id                │
└─────────────┘       └──────────────────────────┘

┌──────────────────────────┐
│  strategic_events        │
│                          │
│ event_id                 │
│ date                     │
│ title                    │
│ description              │
│ category                 │
│ source_id                │
└──────────────────────────┘
```

---

## Table Definitions

### 1. channels — Payment Channel Reference

Lookup table for all payment channels.

```sql
CREATE TABLE channels (
    channel_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    channel_code    TEXT NOT NULL UNIQUE,     -- 'wallet', 'mobile_banking', etc.
    channel_name    TEXT NOT NULL,            -- 'Mobile Wallet'
    channel_type    TEXT NOT NULL,            -- 'wallet', 'bank_digital', 'infrastructure', 'card'
    description     TEXT,
    is_active       INTEGER DEFAULT 1,        -- 1 = active, 0 = historical
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Seed data
INSERT INTO channels (channel_code, channel_name, channel_type, description) VALUES
('wallet', 'Mobile Wallet', 'wallet', 'Stored-value accounts operated by PSPs (eSewa, Khalti, etc.)'),
('mobile_banking', 'Mobile Banking', 'bank_digital', 'Banking services via mobile phone linked to bank account'),
('internet_banking', 'Internet Banking', 'bank_digital', 'Banking services via web interface'),
('qr', 'QR Code Payment', 'infrastructure', 'QR-code based payment initiation'),
('pos', 'Point of Sale', 'card', 'Card-based POS terminal payments'),
('card_online', 'Card Online', 'card', 'Card-based e-commerce/internet payments'),
('connectips', 'connectIPS', 'infrastructure', 'NCHL interbank payment system'),
('ecommerce', 'E-Commerce Payment', 'infrastructure', 'Online payment gateway transactions'),
('atm', 'ATM Cash Withdrawal', 'card', 'ATM cash withdrawal transactions'),
('other', 'Other Digital', 'infrastructure', 'Other digital payment channels');
```

---

### 2. sources — Source Register (Database Version)

Mirror of the source register, enabling foreign key relationships.

```sql
CREATE TABLE sources (
    source_id       TEXT PRIMARY KEY,          -- 'NRB001', 'ESW001', etc.
    institution     TEXT NOT NULL,             -- 'NRB', 'eSewa', etc.
    document_name   TEXT NOT NULL,             -- 'Payment System Indicators'
    document_date   TEXT,                      -- '2026-01' or '2025'
    coverage_start  TEXT,                      -- '2021-01'
    coverage_end    TEXT,                      -- '2026-06'
    url             TEXT,
    file_path       TEXT,                      -- Local path in sources/
    tier            INTEGER NOT NULL,          -- 1-7 source tier
    reliability     TEXT,                      -- 'High', 'Medium', 'Low'
    notes           TEXT,
    access_date     TEXT,                      -- When we last accessed this source
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

### 3. monthly_payment_metrics — Core Monthly Data

The central fact table. One row per channel per month.

```sql
CREATE TABLE monthly_payment_metrics (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    date                TEXT NOT NULL,            -- 'YYYY-MM' format
    channel_id          INTEGER NOT NULL REFERENCES channels(channel_id),
    
    -- Transaction metrics
    transaction_count   INTEGER,                  -- Number of transactions
    transaction_value   REAL,                     -- Total value in NPR
    
    -- Derived engagement metrics (calculated during processing)
    avg_transaction_value REAL,                   -- transaction_value / transaction_count
    
    -- Metadata
    source_id           TEXT NOT NULL REFERENCES sources(source_id),
    data_quality_flag   TEXT DEFAULT 'unreviewed', -- 'verified', 'flagged', 'estimated'
    notes               TEXT,
    
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date, channel_id)
);

CREATE INDEX idx_monthly_payment_date ON monthly_payment_metrics(date);
CREATE INDEX idx_monthly_payment_channel ON monthly_payment_metrics(channel_id);
CREATE INDEX idx_monthly_payment_source ON monthly_payment_metrics(source_id);
```

---

### 4. monthly_adoption_metrics — Adoption & Penetration Data

Stock variables measured monthly.

```sql
CREATE TABLE monthly_adoption_metrics (
    id                          INTEGER PRIMARY KEY AUTOINCREMENT,
    date                        TEXT NOT NULL,        -- 'YYYY-MM'
    
    -- Wallet adoption
    wallet_accounts_total       INTEGER,              -- Total registered wallet accounts
    wallet_active_users         INTEGER,              -- Active wallet users
    
    -- Mobile banking adoption
    mobile_banking_users        INTEGER,              -- Total registered mobile banking users
    mobile_banking_active_users INTEGER,              -- Active mobile banking users
    
    -- Internet banking adoption
    internet_banking_users      INTEGER,
    internet_banking_active_users INTEGER,
    
    -- Infrastructure
    atm_count                   INTEGER,
    pos_count                   INTEGER,
    
    -- Metadata
    source_id                   TEXT NOT NULL REFERENCES sources(source_id),
    data_quality_flag           TEXT DEFAULT 'unreviewed',
    notes                       TEXT,
    
    created_at                  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at                  DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date)
);

CREATE INDEX idx_adoption_date ON monthly_adoption_metrics(date);
```

---

### 5. institutions — Institution Reference

All institutions in the payments ecosystem.

```sql
CREATE TABLE institutions (
    institution_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    short_name      TEXT,
    institution_type TEXT NOT NULL,           -- 'psp', 'pso', 'bank', 'mno', 'infrastructure'
    category        TEXT,                     -- 'private', 'public', 'joint_venture'
    license_type    TEXT,                     -- 'psp', 'pso', 'bank', 'finance_company'
    is_active       INTEGER DEFAULT 1,
    website         TEXT,
    notes           TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

### 6. institution_metrics — Company-Level Metrics

Flexible key-value store for company-specific metrics.

```sql
CREATE TABLE institution_metrics (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,            -- 'YYYY-MM' or 'YYYY'
    institution_id  INTEGER NOT NULL REFERENCES institutions(institution_id),
    metric_name     TEXT NOT NULL,            -- 'users', 'transaction_count', 'revenue', etc.
    metric_value    REAL NOT NULL,
    unit            TEXT NOT NULL,            -- 'count', 'npr', 'percent'
    period_type     TEXT DEFAULT 'annual',    -- 'monthly', 'quarterly', 'annual'
    source_id       TEXT NOT NULL REFERENCES sources(source_id),
    data_quality_flag TEXT DEFAULT 'unreviewed',
    notes           TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date, institution_id, metric_name)
);

CREATE INDEX idx_inst_metrics_date ON institution_metrics(date);
CREATE INDEX idx_inst_metrics_inst ON institution_metrics(institution_id);
CREATE INDEX idx_inst_metrics_name ON institution_metrics(metric_name);
```

---

### 7. banks — Bank Reference

Banks offering digital payment services.

```sql
CREATE TABLE banks (
    bank_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    institution_id  INTEGER REFERENCES institutions(institution_id),
    name            TEXT NOT NULL,
    bfi_type        TEXT,                     -- 'commercial', 'development', 'finance', 'microfinance'
    has_mobile_banking INTEGER DEFAULT 0,
    has_internet_banking INTEGER DEFAULT 0,
    has_pos         INTEGER DEFAULT 0,
    is_active       INTEGER DEFAULT 1,
    notes           TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

### 8. bank_digital_metrics — Bank-Level Digital Metrics

```sql
CREATE TABLE bank_digital_metrics (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    bank_id         INTEGER NOT NULL REFERENCES banks(bank_id),
    metric_name     TEXT NOT NULL,            -- 'mobile_banking_users', 'mobile_transactions', etc.
    metric_value    REAL NOT NULL,
    unit            TEXT NOT NULL,
    source_id       TEXT NOT NULL REFERENCES sources(source_id),
    data_quality_flag TEXT DEFAULT 'unreviewed',
    notes           TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date, bank_id, metric_name)
);

CREATE INDEX idx_bank_metrics_date ON bank_digital_metrics(date);
CREATE INDEX idx_bank_metrics_bank ON bank_digital_metrics(bank_id);
```

---

### 9. merchants — Merchant Ecosystem Data

```sql
CREATE TABLE merchants (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    merchant_type   TEXT,                     -- 'qr', 'pos', 'online', 'total'
    merchant_count  INTEGER,
    source_id       TEXT NOT NULL REFERENCES sources(source_id),
    data_quality_flag TEXT DEFAULT 'unreviewed',
    notes           TEXT,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date, merchant_type)
);
```

---

### 10. regulatory_events — Regulatory Timeline

```sql
CREATE TABLE regulatory_events (
    event_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,            -- 'YYYY-MM-DD' or 'YYYY-MM'
    title           TEXT NOT NULL,
    description     TEXT,
    issuing_body    TEXT DEFAULT 'NRB',       -- 'NRB', 'Government', etc.
    event_type      TEXT,                     -- 'directive', 'circular', 'policy', 'licensing'
    impact_area     TEXT,                     -- 'interoperability', 'limits', 'kyc', 'licensing'
    impact_assessment TEXT,                   -- Qualitative assessment of competitive impact
    source_id       TEXT NOT NULL REFERENCES sources(source_id),
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_reg_events_date ON regulatory_events(date);
```

---

### 11. strategic_events — Significant Industry Events

```sql
CREATE TABLE strategic_events (
    event_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    title           TEXT NOT NULL,
    description     TEXT,
    event_type      TEXT,                     -- 'partnership', 'launch', 'acquisition', 'funding'
    institution_id  INTEGER REFERENCES institutions(institution_id),
    impact_notes    TEXT,
    source_id       TEXT NOT NULL REFERENCES sources(source_id),
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_strat_events_date ON strategic_events(date);
```

---

### 12. data_quality_log — Quality Audit Trail

Tracks data quality issues discovered during validation.

```sql
CREATE TABLE data_quality_log (
    issue_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    date_discovered DATETIME DEFAULT CURRENT_TIMESTAMP,
    table_name      TEXT NOT NULL,
    record_id       INTEGER,
    issue_type      TEXT NOT NULL,            -- 'duplicate', 'missing', 'outlier', 'definition_change', etc.
    description     TEXT NOT NULL,
    likely_cause    TEXT,
    recommended_treatment TEXT,
    resolution      TEXT,                     -- 'retained', 'excluded', 'adjusted', 'pending'
    resolved_date   DATETIME,
    notes           TEXT
);
```

---

### 13. derived_metrics — Calculated Metrics Cache

Stores calculated metrics to avoid recomputation.

```sql
CREATE TABLE derived_metrics (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    date            TEXT NOT NULL,
    metric_name     TEXT NOT NULL,
    metric_value    REAL,
    unit            TEXT,
    calculation_method TEXT,                  -- SQL or Python expression used
    dependencies    TEXT,                     -- JSON list of source tables/columns
    source_ids      TEXT,                     -- JSON list of source_ids used
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(date, metric_name)
);

CREATE INDEX idx_derived_date ON derived_metrics(date);
CREATE INDEX idx_derived_name ON derived_metrics(metric_name);
```

---

## Relationships Diagram

```
channels ──────< monthly_payment_metrics >────── sources
                        │
                        │ (date)
                        ▼
monthly_adoption_metrics ──────── sources

institutions ────< institution_metrics >────── sources
      │
      └──────── banks ────< bank_digital_metrics >────── sources

merchants ──────── sources

regulatory_events ──────── sources

strategic_events ──────── sources
                  │
                  └── institutions (optional)

data_quality_log (standalone audit table)

derived_metrics (standalone calculation cache)
```

---

## Key Constraints

| Constraint | Rule |
|-----------|------|
| `source_id` is mandatory | Every fact table requires a valid `source_id` |
| No orphan records | Every foreign key must reference an existing record |
| Date format | All dates in `YYYY-MM` or `YYYY-MM-DD` format |
| No raw data in DB | Raw data stays in `data/raw/`; only processed data enters the DB |
| Unique observations | `(date, channel_id)` or `(date, institution_id, metric_name)` must be unique |
| Quality flag required | Every observation must have a `data_quality_flag` |

---

## Data Loading Pipeline

```
1. Download NRB data → data/raw/
2. Validate raw data → data_quality_log
3. Transform and clean → data/processed/
4. Load into SQLite → payments.db (channels, monthly_payment_metrics, monthly_adoption_metrics)
5. Calculate derived metrics → derived_metrics table
6. Export analysis-ready data → data/final/
```

---

## Migration Strategy

| Version | Changes | Date |
|---------|---------|------|
| v1.0 | Initial schema (this document) | Phase 1 |
| v1.1 | Add tables as needed during Phase 3–6 | TBD |

All schema changes must be documented in this file before implementation.

---

*Document status: Architecture complete. Schema designed. Database to be created in Phase 3.*
