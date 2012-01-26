#!/usr/bin/env python
"""
This scrape demonstrates how to "fill out" an 
online form to fetch data from a remote server.

More accurately, we'll show how to make a POST request to 
to fetch a list of links for campaign finance reports
from the Federal Election Election Commission.

We'll then use these links to download campaign finance data
(in CSV format) for a specific committee.

The electronic filings/form we're using in this script can be found at:

    http://fec.gov/finance/disclosure/efile_search.shtml

USAGE:

You can run this scrape by going to command line, navigating to the
directory containing this script, and typing the below command:

    python fec_efiles_scrape.py


HELPFUL LINKS:

 Python Modules used in this script:
 * BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/documentation.html
 * CSV:           http://docs.python.org/library/csv.html
 * requests:      http://docs.python-requests.org/en/latest/user/quickstart/
 * sys:           http://docs.python.org/library/sys.html

 HTTP codes
 * http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

"""
import csv
import sys

import requests
from BeautifulSoup import BeautifulSoup

# Build a dictionary containing our form field values
# http://docs.python.org/tutorial/datastructures.html#dictionaries
form_data = {
    'name':'Romney', # committee name field
    'type':'P',      # committee type is P for Presidential
    'frmtype':'F3P', # form type
}

# Make the POST request with the form dictionary. This should 
# return a response object containing the status of the request -- ie 
# whether or not it was successful -- and raw HTML for the returned page.
response = requests.post('http://query.nictusa.com/cgi-bin/dcdev/forms/', data=form_data)

# If the request was successful, then process the HTML
if response.status_code == 200:

    # The raw HTML is stored in the response object's "text" attribute
    soup = BeautifulSoup(response.text)
    links = soup.findAll('a') 

    # Extract the download links 
    download_links = []
    for link in links:
        if link.text == 'Download':
            download_links.append(link)

    """
    NOTE: We could replace the 4 lines of code above with the single line below:

    download_links = soup.findAll('a', href=lambda path: path.startswith('/cgi-bin/dcdev/forms/DL/'))

    This one-liner leverages one of BeautifulSoup's more advanced features -- specifically, the 
    ability to filter the "findAll" method's results by applying regular expressions or 
    lambda functions.
    
    Above, we used a lambda function to filter for links with "href" 
    attributes starting with a certain URL path. 
     
    To learn more: 

    * http://www.crummy.com/software/BeautifulSoup/documentation.html
    * http://stackoverflow.com/questions/890128/python-lambda-why
    * http://docs.python.org/howto/regex.html
    """

    # Now that we have our target links, we can download CSVs for further processing.

    # Below is the base URL for FEC Filing CSV downloads. 
    # Notice the "%s" format character at the end. 
    BASE_URL =  'http://query.nictusa.com/comma/%s.fec'

    # To get at the raw data for each filing, we'll combine the above BASE_URL with
    # unique FEC report numbers (found in the download_links that we extracted above).

    for link in download_links:

        # Below, we use a single line of code to extract the unique FEC report number:
        fec_num = link.get('href').strip('/').split('/')[-1]

        # The one-liner above uses "method chaining" to:
        # 1) Extract the "href" attribute from the link and return it as a string
        # 2) Strip the slashes from either end of returned URL path string
        # 3) Split the resulting string on slashes, which returns a list of URL path components
        # 4) Extract the last element of the list (denoted by "-1"), which should be the FEC number

        # Use string interpolation to build the final download link
        # http://docs.python.org/library/stdtypes.html#string-formatting-operations
        csv_download_link =  BASE_URL % fec_num

        # Fetch the CSV data
        response = requests.get(csv_download_link)

        # Create a list of data rows by splitting on the line terminator character
        data_rows = response.text.split('\n')

        # Use the CSV module to parse the comma-separated rows of data. Calling 
        # the built-in "list" function causes csv to parse our data strings 
        # into lists of distinct data points (the same as if it they were
        # in a spreadsheet or database table).
        # http://docs.python.org/library/csv.html
        data = list(csv.reader(data_rows))

        # The first row in the FEC data contains useful info about the format of 
        # the remaining rows in the file.
        version = data[0][2] # e.g., 8.0
        print "Downloaded Electronic filing with File Format Version %s" % version
        
        ### WHAT'S NEXT? ###
        # In a normal script you would use the version number to fetch the
        # the appropriate file formats, which could then be used to process
        # the remaining data in the file.

        # But we know you get the picture -- and we want to be kind to 
        # the FEC's servers -- so we'll exit the program early and assign 
        # the rest of the script as homework :-)
        sys.exit("Exited script after processing one link.")

else:
    # Gracefully exit the program if response code is not 200
    sys.exit("Response code not OK: %s" % response.status_code)
