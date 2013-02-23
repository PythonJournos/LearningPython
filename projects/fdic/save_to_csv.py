"""
Save results of FDIC Scrape to a CSV file.

This module shows how to use the built-in csv module to 
easily write out data to a file.
"""
import csv
import os
from datetime import datetime

# Import our scraper function to get the data
from scraper import scrape_data

# Import our dynamically calculated project directory
# It's a bit of magic that makes this code work on Macs, Windows, and Linux :)
from settings import PROJECT_DIR

# Function to change date strings to YYYY-MM-DD format
def convertdatestring(datestring):
    try:
        dt = datetime.strptime(datestring, '%B %d, %Y')
        ret_date = dt.strftime('%Y-%m-%d')
    except ValueError:
        print("Can't convert %s to date. Setting to NULL." % datestring)
    return ret_date

# Results is a list that includes our column headers and a list of data
results = scrape_data()
headers = results[0]
data = results[1]

"""
The results are list of data rows that look like below:

data = [
    [
        'First Alliance',
        'Manchester',
        'NH',
        '34264',
        'Southern New Hampshire Bank & Trust',
        'February 15, 2013',
        'February 20, 2013',
        'http://www.fdic.gov/bank/individual/failed/firstalliance.html'
    ],
]
"""

# Let's mess up one row to demo try/except:
# data[0][5] = 'Jnauary 15, 2013'

# Iterate through each row of our data and verify data types valid
for row in data:
    # First, we'll convert cert_num to an integer
    try:
        row[3] = int(row[3])
    except ValueError:
        print("%s is not a valid integer. Setting to zero." % row[3])
        row[3] = 0

    # Now we'll look at the two date fields. This is a little more
    # complicated, so we'll create a function that we can use for
    # both fields. We need to convert them to YYYY-MM-DD format.
    try:
        row[5] = convertdatestring(row[5])
    except:
        row[5] = ''
    
    try:
        row[6] = convertdatestring(row[6])
    except:
        row[6] = ''

filename = os.path.join(PROJECT_DIR, 'fdic.txt')

# This is a Python idiom you'll see often. 
# You're opening a file so that you can read data from it.
# Then, you use the csv module to help write the data to a file
#   http://docs.python.org/2/library/csv.html#csv.DictReader

with open(filename, 'wb') as outputfile:
    wtr = csv.writer(outputfile, delimiter='|', quotechar='"')

    # Add headers tooutput
    wtr.writerow(headers)
    
    # Write the data
    wtr.writerows(data)
