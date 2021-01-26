import sqlite3
import time
from math import ceil

class Company():
    def __init__(self, row):
        self.license_no = row['license']
        self.name = row['name']
        self.exp_date = time.strptime(str(row['expiry_date']), "%d/%m/%Y")
        self.email = row['email']
        self.tte_secs = time.mktime(self.exp_date) - time.time()
        self.tte_days = int(ceil(self.tte_secs/86400))
        self.is_expired = self.tte_days < 0

    def get_exp_date_str(self):
        date_str1, date_str2 = time.asctime(self.exp_date)[:11], time.asctime(self.exp_date)[-4:]
        return date_str1+date_str2

    def __repr__(self):
        return self.name

def get_companies_from_db(db):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute('SELECT * FROM license_info')
    row = c.fetchone()
    companies = []
    while row:
        try:
            coy = Company(row)
        except Exception as e:
            print(f"Warning: {e}")
        else:
            companies.append(coy)
        finally:
            row = c.fetchone()
    
    return companies

