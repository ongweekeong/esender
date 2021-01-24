import sqlite3
import time

class Company():
    def __init__(self, row):
        self.license_no = row['license']
        self.name = row['name']
        self.exp_date = time.strptime(str(row['expiry_date']), "%d/%m/%Y")
        self.email = row['email']
        self.tte_secs = time.mktime(self.exp_date) - time.time()
        self.tte_days = int(self.tte_secs//86400)
        self.expired = self.tte_days < 0

    def get_exp_date_str(self):
        return time.asctime(self.exp_date)

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

