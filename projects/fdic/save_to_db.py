# Load fdic data into sqlite

# User variables
csvfile = 'C:\\data\\Python\\fdic_output.txt'

# Import needed libraries
import csv
import sqlite3

# Create the database and the table if don't already exist
conn = sqlite3.connect('C:\\data\\python\\bootcamp.db')
cur = conn.cursor() # This creates a cursor
cur.execute('CREATE TABLE IF NOT EXISTS failed_banks (' \
            'bank varchar (54) NOT NULL, ' \
            'city varchar (17) NOT NULL, ' \
            'state varchar (4) NOT NULL, ' \
            'cert_num INTEGER NOT NULL, ' \
            'acq_inst VARCHAR (65) NOT NULL, ' \
            'closed DATE NOT NULL, ' \
            'updated DATE NOT NULL, ' \
            'url VARCHAR (100) NOT NULL' \
            ')')
conn.commit() # Commit our change

# Now let's add our data
# Open and parse the file
with open(csvfile, 'r') as data:
    rdr = csv.DictReader(data, delimiter='|', lineterminator='\n', quotechar='"')
    to_db = [(i['bank'], i['city'], i['state'], i['cert_num'], i['acq_inst'],
              i['closed'], i['updated'], i['url']) for i in rdr]

cur.executemany('INSERT INTO failed_banks (bank, city, state, cert_num, acq_inst, ' \
                'closed, updated, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', to_db)
conn.commit() # Commit our inserts
conn.close() # Close db connection
