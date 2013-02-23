"""
Load fdic data into sqlite
"""
import os
import sqlite3

from settings import PROJECT_DIR

from scraper import scrape_data

# Construct the file path to our (soon-to-be-created) SQLite database
db_file = os.path.join(PROJECT_DIR, 'fdic.sqlite')

# Now we're ready to create our database and open a connection to it
#   http://docs.python.org/2/library/sqlite3.html
conn = sqlite3.connect(db_file)

# Once we're connected, we need a database "cursor" so
# we can send SQL statements to the db
cur = conn.cursor()

# Here's the SQL to create our database table 
TBL_CREATE_STMT = """
    CREATE TABLE IF NOT EXISTS failed_banks (
        bank varchar (54) NOT NULL,
        city varchar (17) NOT NULL, 
        state varchar (4) NOT NULL,
        cert_num INTEGER NOT NULL, 
        acq_inst VARCHAR (65) NOT NULL,
        closed DATE NOT NULL, 
        updated DATE NOT NULL,
        url VARCHAR (100) NOT NULL
    )
"""

# Execute the create table sql
cur.execute(TBL_CREATE_STMT)
# Commit our change
conn.commit()

# Get results data (recall that it's a list of two elements [headers, data])
results = scrape_data()
data = results[1]

cur.executemany('INSERT INTO failed_banks (bank, city, state, cert_num, acq_inst, ' \
                'closed, updated, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', data)
# Commit our inserts
conn.commit()
# Close db connection
conn.close()
