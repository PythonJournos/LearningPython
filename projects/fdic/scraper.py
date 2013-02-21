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

        # Pluck out the text of each field and store as a 
        # separate key in a dictionary
        #   http://docs.python.org/2/tutorial/datastructures.html#dictionaries
        row = {
            'bank_name': data[0].text,
            'city': data[1].text,
            'state': data[2].text,
            'cert_num': data[3].text,
            'acq_inst': data[4].text,
            'closed': data[5].text.strip(),
            'updated': data[6].text.strip(),
            'url': 'http://www.fdic.gov/bank/individual/failed/' + data[0].a['href'],
        }
        # Add the dictionary to our final set of results
        results.append(row)

    # Return the results 
    return results

if __name__ == '__main__':
    results = scrape_data()
    for row in results:
        print row['url']
