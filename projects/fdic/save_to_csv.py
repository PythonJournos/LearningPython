"""
Save results of FDIC Scrape to a CSV file.

This module shows how to use the built-in csv module to 
easily write out data to a file.

"""
from datetime import datetime

# Import the scraper function
from scraper import scrape_data

# Function to change date strings to YYYY-MM-DD format
#   http://docs.python.org/2/library/datetime.html#datetime-objects
def convert_date(datestring):
    # First, transform the incoming string to a Python datetime object
    dt = datetime.strptime(datestring, '%B %d, %Y')
    # Then use the datetime object's strftime method to convert to final format
    final_date = dt.strftime('%Y-%m-%d')
    return final_date

# Store the results of the scrape_data function
# Results are dictionaries that look like below
"""
data = [
    {
        'bank': 'First Alliance',
        'city': 'Manchester',
        'state': 'NH',
        'cert_num': '34264',
        'acq_inst': 'Southern New Hampshire Bank & Trust',
        'closed': 'February 15, 2013',
        'updated': 'February 20, 2013',
        'url': 'http://www.fdic.gov/bank/individual/failed/firstalliance.html,
    },
]
"""
data = scrape_data()

# Loop through results and do perform basic data clean-up and conversion.
# Note that we're changing the data "in place" (i.e., in the pre-existing dictionary)
for row in data:
    # Convert cert_num to an integer
    row['cert_num'] = int(row['cert_num'])

    # Now we'll look at the two date fields. This is a little more
    # complicated, so we'll create a function that we can use for
    # both fields. We need to convert them to YYYY-MM-DD format.
    row['closed'] = convert_date(row['closed'])
    row['updated'] = convert_date(row['updated'])

for row in data:
    print row
#TODO: CSV writer here
# dynamically determine the file path using os.path (this will avoid windows path headaches)
#with open(
