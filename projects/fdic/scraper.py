#!/usr/bin/env python
"""
This scrape demonstrates some Python basics using the FDIC's Failed Banks List.
It contains a function that downloads a single web page, uses a 3rd-party library
to extract data from the HTML, and packages up the data into a reusable
list of data "row".

NOTE:

The original FDIC data is located at the below URL:

    http://www.fdic.gov/bank/individual/failed/banklist.html

In order to be considerate to the FDIC's servers, we're scraping 
a copy of the page stored on Amazon S3.
"""
# Import a built-in library for working with data on the Web
#   http://docs.python.org/library/urllib.html
import urllib

# Import a 3rd-party library to help extract data from raw HTML
#   http://www.crummy.com/software/BeautifulSoup/documentation.html  
from bs4 import BeautifulSoup

# Below is a re-usable data scraper function that can be imported and used by other code.
#   http://docs.python.org/2/tutorial/controlflow.html#defining-functions
def scrape_data():
    # URL of the page we're going to scrape (below is the real URL, but
    # we'll hit a dummy version to be kind to the FDIC)
    #URL = 'http://www.fdic.gov/bank/individual/failed/banklist.html'
    URL = 'https://s3.amazonaws.com/python-journos/FDIC_Failed_Bank_List.html'

    # Open a network connection using the "urlopen" method. 
    # This returns a network "object" 
    #   http://docs.python.org/library/urllib.html#high-level-interface
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

    # Create a list to store our results
    results = []

    # 3) Process the data, skipping the initial header row
    for tr in rows[1:]:

        # Extract data points from the table row
        data = tr.findAll('td')

        # Pluck out the text of each field, and perform a bit of clean-up
        row = [
            data[0].text,
            data[1].text,
            data[2].text,
            data[3].text,
            data[4].text,
            data[5].text.strip(),
            data[6].text.strip(),
            'http://www.fdic.gov/bank/individual/failed/' + data[0].a['href'],
        ]
        # Add the list of data to our results list (we'll end up with a list of lists)
        results.append(row)

    # Let's package up the results with the field names
    headers = [
        'bank_name',
        'city',
        'state',
        'cert_num',
        'acq_inst',
        'closed',
        'updated',
        'url'
    ]
    return [headers, results]

if __name__ == '__main__':
    results = scrape_data()
    for row in results[1]:
        print row
