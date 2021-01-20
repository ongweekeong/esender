import sqlite3

class Company:
    all_by_id = {}

    def __init__(self, row):
        self.license_no = row['license']
        self.name = row['name']
        self.exp_date = row['expiry_date']
        self.not_date = row['notice_date']
        Company.all_by_id[self.license_no] = self

conn = sqlite3.connect('licenses.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute('SELECT * FROM licenses')
row = c.fetchone()

while row:
    Company(row)
    print(row['license'])
    row = c.fetchone()

print(Company.all_by_id)

