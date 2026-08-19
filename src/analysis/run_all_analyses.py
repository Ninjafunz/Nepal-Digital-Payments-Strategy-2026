"""Run all five core analyses with charts."""
import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

os.makedirs('analysis/charts', exist_ok=True)

conn = sqlite3.connect('database/payments.db')
c = conn.cursor()

# Helper: run query and return rows
def q(sql, params=()):
    c.execute(sql, params)
    return c.fetchall()

# Color scheme
COLORS = {
    'wallet': '#2196F3', 'mobile_banking': '#4CAF50', 'internet_banking': '#9C27B0',
    'qr': '#FF9800', 'pos': '#F44336', 'debit_card': '#795548', 'credit_card': '#E91E63',
    'prepaid_card': '#00BCD4', 'atm': '#607D8B', 'branchless_banking': '#8BC34A',
    'ecc': '#CDDC39', 'ips': '#3F51B5', 'connectips': '#009688', 'rtgs': '#FF5722',
    'ecommerce': '#795548', 'faster_payment': '#673AB7', 'cross_border_qr': '#FF9800',
    'other_retail': '#9E9E9E',
}

# ============================================================
# ANALYSIS 1: Is Nepal Becoming More Digital?
# ============================================================
print("=" * 60)
print("ANALYSIS 1: Is Nepal Becoming More Digital?")
print("=" * 60)

# Total transaction count and value per month
data1 = q("""
    SELECT date_ad, 
           SUM(transaction_count) as total_count,
           SUM(transaction_value_npr_millions) as total_value
    FROM monthly_payment_metrics
    WHERE transaction_count IS NOT NULL
    GROUP BY date_ad
    ORDER BY date_ad
""")

dates = [r[0] for r in data1]
counts = [r[1] for r in data1]
values = [r[2] for r in data1]

# Annual totals
annual = q("""
    SELECT SUBSTR(date_ad, 1, 4) as year,
           SUM(transaction_count) as total_count,
           SUM(transaction_value_npr_millions) as total_value
    FROM monthly_payment_metrics
    WHERE transaction_count IS NOT NULL AND SUBSTR(date_ad,1,4) >= '2021'
    GROUP BY year ORDER BY year
""")

print("\nAnnual totals:")
print(f"{'Year':>6} | {'Txn Count (B)':>15} | {'Txn Value (B NPR)':>18}")
print("-" * 45)
for r in annual:
    print(f"{r[0]:>6} | {r[1]/1e9:>15.2f} | {r[2]/1e3:>18.1f}")

# CAGR
if len(annual) >= 2:
    y0, y1 = annual[0], annual[-1]
    years = int(y1[0]) - int(y0[0])
    cagr_count = ((y1[1]/y0[1])**(1/years) - 1) * 100
    cagr_value = ((y1[2]/y0[2])**(1/years) - 1) * 100
    print(f"\nCAGR (count): {cagr_count:.1f}%")
    print(f"CAGR (value): {cagr_value:.1f}%")

# Chart 1: Total digital transactions over time
fig, ax1 = plt.subplots(figsize=(14, 6))
ax2 = ax1.twinx()
x = range(len(dates))
ax1.bar(x, [c/1e6 for c in counts], alpha=0.6, color='#2196F3', label='Transaction Count (M)')
ax2.plot(x, [v/1e3 for v in values], color='#F44336', linewidth=2, label='Transaction Value (B NPR)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Transaction Count (Millions)', color='#2196F3')
ax2.set_ylabel('Transaction Value (Billion NPR)', color='#F44336')
ax1.set_xticks(x[::6])
ax1.set_xticklabels([dates[i] for i in range(0, len(dates), 6)], rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('Nepal Digital Payment Volume and Value (Jul 2020 - Jul 2025)\nSource: NRB Payment Systems Indicators (NRB_PSD001)')
plt.tight_layout()
plt.savefig('analysis/charts/01_total_digital_growth.png', dpi=150)
plt.close()
print("\nChart saved: analysis/charts/01_total_digital_growth.png")

# ============================================================
# ANALYSIS 2: Which Payment Channels Are Winning?
# ============================================================
print("\n" + "=" * 60)
print("ANALYSIS 2: Which Payment Channels Are Winning?")
print("=" * 60)

# Channel value shares for key channels
channels_of_interest = ['wallet', 'mobile_banking', 'qr', 'debit_card', 'pos', 'credit_card', 'internet_banking', 'atm']

# Annual value by channel
ch_annual = q("""
    SELECT SUBSTR(date_ad, 1, 4) as year, channel_code,
           SUM(transaction_value_npr_millions) as total_value,
           SUM(transaction_count) as total_count
    FROM monthly_payment_metrics
    WHERE transaction_value_npr_millions IS NOT NULL AND SUBSTR(date_ad,1,4) >= '2021'
    GROUP BY year, channel_code ORDER BY year, channel_code
""")

# Build pivot
from collections import defaultdict
pivot_value = defaultdict(dict)
pivot_count = defaultdict(dict)
for year, ch, val, cnt in ch_annual:
    pivot_value[ch][year] = val
    pivot_count[ch][year] = cnt

years = sorted(set(r[0] for r in ch_annual))
print(f"\nChannel value shares (% of total) by year:")
print(f"{'Channel':>20}", end='')
for y in years: print(f" | {y:>8}", end='')
print()
print("-" * (20 + 11 * len(years)))

for ch in channels_of_interest:
    print(f"{ch:>20}", end='')
    for y in years:
        total = sum(pivot_value[c].get(y, 0) for c in pivot_value)
        share = pivot_value[ch].get(y, 0) / total * 100 if total > 0 else 0
        print(f" | {share:>7.1f}%", end='')
    print()

# Chart 2: Channel value shares stacked area
fig, ax = plt.subplots(figsize=(14, 7))
bottom = np.zeros(len(years))
for ch in ['mobile_banking', 'wallet', 'qr', 'debit_card', 'pos', 'credit_card', 'internet_banking', 'atm']:
    vals = [pivot_value[ch].get(y, 0) for y in years]
    totals = [sum(pivot_value[c].get(y, 0) for c in pivot_value) for y in years]
    shares = [v/t*100 if t > 0 else 0 for v, t in zip(vals, totals)]
    ax.bar(years, shares, bottom=bottom, label=ch.replace('_',' ').title(), color=COLORS.get(ch, '#999'))
    bottom += np.array(shares)
ax.set_ylabel('Share of Total Digital Transaction Value (%)')
ax.set_xlabel('Fiscal Year')
ax.set_title('Payment Channel Value Shares Over Time\nSource: NRB Payment Systems Indicators (NRB_PSD001)')
ax.legend(loc='upper right', fontsize=8)
plt.tight_layout()
plt.savefig('analysis/charts/02_channel_value_shares.png', dpi=150)
plt.close()
print("\nChart saved: analysis/charts/02_channel_value_shares.png")

# Chart 2b: QR growth trajectory
fig, ax1 = plt.subplots(figsize=(14, 6))
ax2 = ax1.twinx()
qr_data = q("""SELECT date_ad, transaction_count, transaction_value_npr_millions 
                FROM monthly_payment_metrics WHERE channel_code='qr' AND transaction_count IS NOT NULL ORDER BY date_ad""")
qr_dates = [r[0] for r in qr_data]
qr_counts = [r[1] for r in qr_data]
qr_values = [r[2] for r in qr_data]
x = range(len(qr_dates))
ax1.fill_between(x, [c/1e6 for c in qr_counts], alpha=0.5, color='#FF9800', label='QR Count (M)')
ax2.plot(x, [v/1e3 for v in qr_values], color='#F44336', linewidth=2, label='QR Value (B NPR)')
ax1.set_ylabel('Transaction Count (Millions)', color='#FF9800')
ax2.set_ylabel('Transaction Value (Billion NPR)', color='#F44336')
ax1.set_xticks(x[::6])
ax1.set_xticklabels([qr_dates[i] for i in range(0, len(qr_dates), 6)], rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.title('QR-Based Payment Explosion in Nepal (Jul 2020 - Jul 2025)\nSource: NRB Payment Systems Indicators (NRB_PSD001)')
plt.tight_layout()
plt.savefig('analysis/charts/02b_qr_growth.png', dpi=150)
plt.close()
print("Chart saved: analysis/charts/02b_qr_growth.png")

# ============================================================
# ANALYSIS 3: Are Users Actually Engaging?
# ============================================================
print("\n" + "=" * 60)
print("ANALYSIS 3: Are Users Actually Engaging?")
print("=" * 60)

# Transactions per user for wallet and mobile banking
engage = q("""
    SELECT p.date_ad, p.channel_code,
           p.transaction_count,
           CASE WHEN p.channel_code='wallet' THEN a.wallet_users
                WHEN p.channel_code='mobile_banking' THEN a.mobile_banking_customers
           END as users
    FROM monthly_payment_metrics p
    JOIN monthly_adoption_metrics a ON p.date_ad = a.date_ad
    WHERE p.channel_code IN ('wallet', 'mobile_banking')
      AND p.transaction_count IS NOT NULL AND p.transaction_count > 0
    ORDER BY p.date_ad
""")

from collections import defaultdict
engage_data = defaultdict(lambda: {'dates': [], 'tpu': [], 'atv': []})
for date_ad, ch, txn_count, users in engage:
    if users and users > 0:
        engage_data[ch]['dates'].append(date_ad)
        engage_data[ch]['tpu'].append(txn_count / users)
        engage_data[ch]['atv'].append(0)  # will compute separately

# Also get avg transaction value
atv_data = q("""
    SELECT date_ad, channel_code, transaction_count, transaction_value_npr_millions
    FROM monthly_payment_metrics
    WHERE channel_code IN ('wallet', 'mobile_banking')
      AND transaction_count > 0 AND transaction_value_npr_millions IS NOT NULL
    ORDER BY date_ad
""")
for date_ad, ch, cnt, val in atv_data:
    if cnt and val and date_ad in engage_data[ch]['dates']:
        idx = engage_data[ch]['dates'].index(date_ad)
        engage_data[ch]['atv'][idx] = val * 1e6 / cnt  # NPR per transaction

# Print summary
for ch in ['mobile_banking', 'wallet']:
    d = engage_data[ch]
    if d['tpu']:
        print(f"\n{ch.upper()}:")
        print(f"  Transactions/user (first): {d['tpu'][0]:.2f}")
        print(f"  Transactions/user (last):  {d['tpu'][-1]:.2f}")
        if d['atv']:
            print(f"  Avg txn value NPR (first): {d['atv'][0]:,.0f}")
            print(f"  Avg txn value NPR (last):  {d['atv'][-1]:,.0f}")

# Chart 3: Transactions per user
fig, axes = plt.subplots(1, 2, figsize=(16, 6))
for ch, color, label in [('mobile_banking', '#4CAF50', 'Mobile Banking'), ('wallet', '#2196F3', 'Wallet')]:
    d = engage_data[ch]
    axes[0].plot(range(len(d['tpu'])), d['tpu'], color=color, label=label, linewidth=2)
axes[0].set_title('Transactions per User per Month')
axes[0].set_ylabel('Transactions / User / Month')
axes[0].legend()
xticks = list(range(0, len(engage_data['mobile_banking']['dates']), 12))
axes[0].set_xticks(xticks)
axes[0].set_xticklabels([engage_data['mobile_banking']['dates'][i] for i in xticks], rotation=45)

for ch, color, label in [('mobile_banking', '#4CAF50', 'Mobile Banking'), ('wallet', '#2196F3', 'Wallet')]:
    d = engage_data[ch]
    if d['atv']:
        axes[1].plot(range(len(d['atv'])), [v/1000 for v in d['atv']], color=color, label=label, linewidth=2)
axes[1].set_title('Average Transaction Value')
axes[1].set_ylabel('NPR (Thousands)')
axes[1].legend()
axes[1].set_xticks(xticks)
axes[1].set_xticklabels([engage_data['mobile_banking']['dates'][i] for i in xticks], rotation=45)

plt.suptitle('User Engagement: Wallet vs Mobile Banking\nSource: NRB Payment Systems Indicators (NRB_PSD001)', fontsize=13)
plt.tight_layout()
plt.savefig('analysis/charts/03_user_engagement.png', dpi=150)
plt.close()
print("\nChart saved: analysis/charts/03_user_engagement.png")

# ============================================================
# ANALYSIS 4: Is the Market Concentrating? (HHI)
# ============================================================
print("\n" + "=" * 60)
print("ANALYSIS 4: Is the Market Concentrating?")
print("=" * 60)

hhi_data = q("""
    SELECT SUBSTR(date_ad, 1, 4) as year, channel_code,
           SUM(transaction_value_npr_millions) as total_value
    FROM monthly_payment_metrics
    WHERE transaction_value_npr_millions IS NOT NULL AND SUBSTR(date_ad,1,4) >= '2021'
    GROUP BY year, channel_code
""")
hhi_by_year = defaultdict(dict)
for year, ch, val in hhi_data:
    hhi_by_year[year][ch] = val

print(f"\n{'Year':>6} | {'HHI':>8} | {'Channels':>8} | Top 3 channels")
print("-" * 70)
hhi_years = []
hhi_vals = []
for year in sorted(hhi_by_year.keys()):
    chs = hhi_by_year[year]
    total = sum(chs.values())
    if total > 0:
        shares = [v/total for v in chs.values()]
        hhi = sum(s**2 for s in shares) * 10000
        top3 = sorted(chs.items(), key=lambda x: -x[1])[:3]
        top3_str = ', '.join([f"{c} ({v/total*100:.1f}%)" for c, v in top3])
        print(f"{year:>6} | {hhi:>8.0f} | {len(chs):>8} | {top3_str}")
        hhi_years.append(year)
        hhi_vals.append(hhi)

# Chart 4: HHI over time
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hhi_years, hhi_vals, 'o-', color='#3F51B5', linewidth=2, markersize=8)
ax.axhline(y=1500, color='orange', linestyle='--', alpha=0.7, label='Moderate concentration (1500)')
ax.axhline(y=2500, color='red', linestyle='--', alpha=0.7, label='High concentration (2500)')
ax.set_ylabel('HHI (0-10000)')
ax.set_xlabel('Fiscal Year')
ax.set_title('Market Concentration (HHI) by Channel Value Share\nSource: NRB Payment Systems Indicators (NRB_PSD001)')
ax.legend()
ax.set_ylim(0, max(hhi_vals) * 1.3)
plt.tight_layout()
plt.savefig('analysis/charts/04_hhi_concentration.png', dpi=150)
plt.close()
print("\nChart saved: analysis/charts/04_hhi_concentration.png")

# ============================================================
# ANALYSIS 5: Where Is Economic Value Moving?
# ============================================================
print("\n" + "=" * 60)
print("ANALYSIS 5: Where Is Economic Value Moving?")
print("=" * 60)

# Channel positioning: count vs value scatter
ch_totals = q("""
    SELECT channel_code,
           SUM(transaction_count) as total_count,
           SUM(transaction_value_npr_millions) as total_value,
           AVG(transaction_value_npr_millions * 1e6 / NULLIF(transaction_count, 0)) as avg_txn_value
    FROM monthly_payment_metrics
    WHERE transaction_count > 0 AND transaction_value_npr_millions > 0
      AND SUBSTR(date_ad,1,4) >= '2021'
    GROUP BY channel_code
    ORDER BY total_value DESC
""")

print(f"\n{'Channel':>20} | {'Total Count (B)':>15} | {'Total Value (B NPR)':>20} | {'Avg Txn NPR':>12}")
print("-" * 75)
for r in ch_totals:
    if r[1] and r[2]:
        print(f"{r[0]:>20} | {r[1]/1e9:>15.2f} | {r[2]/1e3:>20.1f} | {r[3]:>12,.0f}")

# Chart 5: Channel positioning scatter (count vs value, bubble = avg txn value)
fig, ax = plt.subplots(figsize=(12, 8))
for r in ch_totals:
    if r[1] and r[2] and r[3] and r[0] in COLORS:
        size = min(r[3] / 500, 500)
        ax.scatter(r[1]/1e9, r[2]/1e3, s=max(size, 50), color=COLORS.get(r[0], '#999'), alpha=0.7, edgecolors='black')
        ax.annotate(r[0].replace('_', ' ').title(), (r[1]/1e9, r[2]/1e3), textcoords="offset points", xytext=(5,5), fontsize=8)
ax.set_xlabel('Total Transaction Count (Billions, Jul 2020 - Jul 2025)')
ax.set_ylabel('Total Transaction Value (Billion NPR, Jul 2020 - Jul 2025)')
ax.set_title('Payment Channel Positioning: Volume vs Value\nBubble size = Average transaction value\nSource: NRB Payment Systems Indicators (NRB_PSD001)')
ax.set_xscale('log')
ax.set_yscale('log')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('analysis/charts/05_channel_positioning.png', dpi=150)
plt.close()
print("\nChart saved: analysis/charts/05_channel_positioning.png")

# Value migration: year-over-year growth by channel
print(f"\nChannel YoY value growth rates:")
print(f"{'Channel':>20}", end='')
for i in range(1, len(years)):
    print(f" | {years[i]:>8}", end='')
print()
print("-" * (20 + 11 * (len(years)-1)))

for ch in channels_of_interest:
    print(f"{ch:>20}", end='')
    prev = None
    for y in years:
        val = pivot_value[ch].get(y, 0)
        if prev and prev > 0:
            growth = (val/prev - 1) * 100
            print(f" | {growth:>7.1f}%", end='')
        else:
            print(f" | {'--':>8}", end='')
        prev = val
    print()

conn.close()
print("\n" + "=" * 60)
print("ALL FIVE ANALYSES COMPLETE")
print("=" * 60)
