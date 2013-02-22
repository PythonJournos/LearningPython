"""
Save results of FDIC Scrape to a CSV file.

This module shows how to use the built-in csv module to 
easily write out data to a file.

"""

# User variables
savedir = 'C:\\data\\Python\\'
outputheaders = ['bank', 'city', 'state', 'cert_num', 'acq_inst',
    'closed', 'updated', 'url']

# Import module created in Part I
# from scraper import scrape_data

# Import datetime modules
from datetime import datetime
import csv

# Function to change date strings to YYYY-MM-DD format
def convertdatestring(datestring):
    # Create variable for our return value
    ret_date = ''
    try:
        dt = datetime.strptime(datestring, '%B %d, %Y')
        ret_date = dt.strftime('%Y-%m-%d')
    except ValueError:
        print("Can't convert %s to date. Setting to NULL." % datestring)
        pass
    
    return ret_date

# Store the results of the scrape_data function
# Results are dictionaries that look like below

data = [
    {
        'bank': 'First Alliance',
        'city': 'Manchester',
        'state': 'NH',
        'cert_num': '34264',
        'acq_inst': 'Southern New Hampshire Bank & Trust',
        'closed': 'February 15, 2013',
        'updated': 'February 20, 2013',
        'url': 'http://www.fdic.gov/bank/individual/failed/firstalliance.html'
    },
    {
        'bank': 'First Alliance',
        'city': 'Manchester',
        'state': 'NH',
        'cert_num': '34264',
        'acq_inst': 'Southern New Hampshire Bank & Trust',
        'closed': 'February 15, 2013',
        'updated': 'February 20, 2013',
        'url': 'http://www.fdic.gov/bank/individual/failed/firstalliance.html'
    }
]

# data = scrape_data()

# Let's mess up one row to demo try/except:
# data[0]['closed'] = 'Jnauary 15, 2013'

# Iterate through each row of our data and verify data types valid
for row in data:
    # First, we'll verify cert_num is an integer
    try:
        row['cert_num'] = int(row['cert_num'])
    except ValueError:
        print("%s is not a valid integer. Setting to zero." % row['cert_num'])
        row['cert_num'] = 0

    # Now we'll look at the two date fields. This is a little more
    # complicated, so we'll create a function that we can use for
    # both fields. We need to convert them to YYYY-MM-DD format.
    try:
        row['closed'] = convertdatestring(row['closed'])
    except:
        row['closed'] = ''
    
    try:
        row['updated'] = convertdatestring(row['updated'])
    except:
        row['updated'] = ''

with open(savedir + 'fdic_output.txt', 'w') as outputfile:
    wtr = csv.DictWriter(outputfile, delimiter='|', fieldnames=outputheaders,
        lineterminator='\n', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    # Add headers to output
    wtr.writeheader()
    
    # Write the data
    wtr.writerows(data)
