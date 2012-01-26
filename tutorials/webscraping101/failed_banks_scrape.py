#!/usr/bin/env python
"""
This scrape demonstrates some Python basics using the FDIC's Failed Banks List.
It downloads a single web page and shows how to use a 3rd-party library
to extract data from the HTML.

USAGE:

You can run this scrape by going to command line, navigating to the
directory containing this script, and typing the below command:

    python failed_banks_scrape.py

NOTE:

The original FDIC data is located at the below URL:

    http://www.fdic.gov/bank/individual/failed/banklist.html

In order to be considerate to the FDIC's servers, we're scraping 
a copy of the page stored on Amazon S3.
"""

# Import a built-in library for working with data on the Web
# DOCS: http://docs.python.org/library/urllib.html
import urllib

# import a 3rd-party to help extract data from raw HTML
# DOCS: http://www.crummy.com/software/BeautifulSoup/documentation.html  
from BeautifulSoup import BeautifulSoup

# URL of the page we're going to scrape (below is the real URL, but
# we'll hit a dummy version to be kind to the FDIC)
URL = 'https://s3.amazonaws.com/python-journos/FDIC_Failed_Bank_List.html'

# Open a network connection using the "urlopen" method. 
# This returns a network "object" 
# http://docs.python.org/library/urllib.html#high-level-interface
web_cnx = urllib.urlopen(URL)

# Use the network object to download, or "read", the page's HTML
html = web_cnx.read() 

# Parse the HTML into a form that's easy to use
soup = BeautifulSoup(html)

# Use BeautifulSoup's API to extract your data
# 1) Fetch the table by ID
table  = soup.find(id='table') 

# 2) Grab the table's rows
rows = table.findAll('tr')

# 3) Get header names from first row
headers = rows[0].findAll('th')

# Extract the column names and add them to a list
columns = []
for header in headers:
    columns.append(header.text)

# Use the tab character's "join" method to concatenate
# the column names into a single, tab-separated string.
# Then print out the header column.
print '\t'.join(columns)

# 4) Process the data, skipping the initial header row
for row in rows[1:]:

    # Extract data points from the table row
    data = row.findAll('td')

    # Pluck out the text of each field and store in a separate variable
    bank_name = data[0].text    
    city = data[1].text
    state = data[2].text
    cert_num = data[3].text
    ai =  data[4].text
    closed_on = data[5].text 
    updated = data[6].text

    print "\t".join([bank_name, city, state, cert_num, ai, closed_on, updated])
