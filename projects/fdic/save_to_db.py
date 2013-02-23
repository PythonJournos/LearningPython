"""
Load fdic data into sqlite
"""
import os
import sqlite3

# Import our dynamically calculated project directory
# It's a bit of magic that makes this code work on Macs, Windows, and Linux :)
from settings import PROJECT_DIR

# Create a SQLite database in our project directory
db_file = os.path.join(PROJECT_DIR, 'bootcamp.sqlite')

# Now we're ready to connect to the database
#   http://docs.python.org/2/library/sqlite3.html
conn = sqlite3.connect(db_file)

# Once we're connected, we get a database "cursor" 
# (which let's you send SQL statements to the database)
cur = conn.cursor()

# Here's the SQL to create our database table 
TBL_CREATE_STMT = """
    CREATE TABLE IF NOT EXISTS failed_banks (
        bank varchar (54) NOT NULL,
        city varchar (17) NOT NULL, 
        tate varchar (4) NOT NULL,
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


cur.executemany('INSERT INTO failed_banks (bank, city, state, cert_num, acq_inst, ' \
                'closed, updated, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', to_db)
# Commit our inserts
conn.commit()
# Close db connection
conn.close()
