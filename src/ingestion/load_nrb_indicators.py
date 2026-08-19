"""Load NRB Payment Systems Indicators into SQLite database."""
import sqlite3, csv, os

db_path = 'database/payments.db'
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE channels (channel_id INTEGER PRIMARY KEY AUTOINCREMENT, channel_code TEXT NOT NULL UNIQUE, channel_name TEXT NOT NULL, channel_type TEXT NOT NULL, description TEXT)''')
c.execute('''CREATE TABLE sources (source_id TEXT PRIMARY KEY, institution TEXT NOT NULL, document_name TEXT NOT NULL, document_date TEXT, tier INTEGER NOT NULL, reliability TEXT, notes TEXT)''')
c.execute('''CREATE TABLE monthly_adoption_metrics (id INTEGER PRIMARY KEY AUTOINCREMENT, date_bs TEXT NOT NULL, date_ad TEXT NOT NULL, wallet_users INTEGER, mobile_banking_customers INTEGER, internet_banking_customers INTEGER, atm_machines INTEGER, debit_cards INTEGER, credit_cards INTEGER, prepaid_cards INTEGER, psp_agents INTEGER, branchless_banking INTEGER, rtgs_participants INTEGER, connectips_users INTEGER, ecc_members INTEGER, ips_members INTEGER, source_id TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, UNIQUE(date_bs))''')
c.execute('''CREATE TABLE monthly_payment_metrics (id INTEGER PRIMARY KEY AUTOINCREMENT, date_bs TEXT NOT NULL, date_ad TEXT NOT NULL, channel_code TEXT NOT NULL, transaction_count INTEGER, transaction_value_npr_millions REAL, source_id TEXT NOT NULL, created_at DATETIME DEFAULT CURRENT_TIMESTAMP, UNIQUE(date_bs, channel_code))''')

# Insert channels
for ch in [('rtgs','RTGS','infrastructure'),('atm','ATM Cash Withdrawal','cash'),('ecc','ECC','card'),('ips','IPS','infrastructure'),('connectips','ConnectIPS','infrastructure'),('debit_card','Debit Cards','card'),('credit_card','Credit Cards','card'),('prepaid_card','Prepaid Cards','card'),('internet_banking','Internet Banking','bank_digital'),('mobile_banking','Mobile Banking','bank_digital'),('branchless_banking','Branchless Banking','bank_digital'),('wallet','Wallet','wallet'),('qr','QR-Based Payments','infrastructure'),('pos','Point of Sale','card'),('ecommerce','E-Commerce','infrastructure'),('faster_payment','Faster Payment Systems','infrastructure'),('cross_border_qr','Cross Border QR','infrastructure'),('other_retail','Other Retail Payments','infrastructure')]:
    c.execute('INSERT INTO channels (channel_code, channel_name, channel_type) VALUES (?,?,?)', ch)

c.execute("INSERT INTO sources VALUES ('NRB_PSD001','NRB','Payment Systems Indicators XLSX (Sep 2025 snapshot)','2025-09',1,'High','Extracted from Wayback Machine. Monthly data Jul 2020 - Jul 2025.')")

def si(v):
    if not v or v == '': return None
    try: return int(float(v))
    except: return None

def sf(v):
    if not v or v == '': return None
    try: return float(v)
    except: return None

# Column mapping: channel_code -> (count_csv_col, value_csv_col)
M = {
    'rtgs': ('RTGS_Count','RTGS_Value'), 'atm': ('ATM_Cash_Withdrawal_Count','ATM_Cash_Withdrawal_Value'),
    'ecc': ('ECC_Count','ECC_Value'), 'ips': ('IPS_Count','IPS_Value'),
    'connectips': ('ConnectIPS_Count','ConnectIPS_Value'), 'debit_card': ('Debit_Card_Count','Debit_Card_Value'),
    'credit_card': ('Credit_Card_Count','Credit_Card_Value'), 'prepaid_card': ('Prepaid_Card_Count','Prepaid_Card_Value'),
    'internet_banking': ('Internet_Banking_Count','Internet_Banking_Value'), 'mobile_banking': ('Mobile_Banking_Count','Mobile_Banking_Value'),
    'branchless_banking': ('Branchless_Banking_Count','Branchless_Banking_Value'), 'wallet': ('Wallet_Count','Wallet_Value'),
    'qr': ('QR_Count','QR_Value'), 'pos': ('POS_Count','POS_Value'),
    'ecommerce': ('Ecommerce_Count','Ecommerce_Value'), 'faster_payment': ('Faster_Payment_Count','Faster_Payment_Value'),
    'cross_border_qr': ('Cross_Border_QR_Count','Cross_Border_QR_Value'), 'other_retail': ('Other_Retail_Count','Other_Retail_Value'),
}

with open('data/raw/NRB_Payment_Systems_Indicators_monthly.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        bs, ad = row['date_bs'], row['date_ad']
        c.execute('INSERT OR REPLACE INTO monthly_adoption_metrics (date_bs,date_ad,wallet_users,mobile_banking_customers,internet_banking_customers,atm_machines,debit_cards,credit_cards,prepaid_cards,psp_agents,branchless_banking,rtgs_participants,connectips_users,ecc_members,ips_members,source_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (bs,ad,si(row['Wallet_Users']),si(row['Mobile_Banking_Customers']),si(row['Internet_Banking_Customers']),si(row['ATM_Machines']),si(row['Debit_Cards']),si(row['Credit_Cards']),si(row['Prepaid_Cards']),si(row['PSP_Agents']),si(row['Branchless_Banking']),si(row['RTGS_Participants']),si(row['ConnectIPS_Users']),si(row['ECC_Members']),si(row['IPS_Members']),'NRB_PSD001'))
        for ch, (ck, vk) in M.items():
            cv, vv = si(row[ck]), sf(row[vk])
            if cv or vv:
                c.execute('INSERT OR REPLACE INTO monthly_payment_metrics (date_bs,date_ad,channel_code,transaction_count,transaction_value_npr_millions,source_id) VALUES (?,?,?,?,?,?)', (bs,ad,ch,cv,vv,'NRB_PSD001'))

conn.commit()
for t in ['monthly_adoption_metrics','monthly_payment_metrics','channels','sources']:
    c.execute(f'SELECT COUNT(*) FROM {t}')
    print(f'{t}: {c.fetchone()[0]} rows')
conn.close()
print('Database created: database/payments.db')
