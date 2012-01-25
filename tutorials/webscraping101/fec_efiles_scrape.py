#!/usr/bin/env python
"""
The third scrape in our series demonstrates how to fetch data from
a remote server by making a POST request.

For this scrape, we'll request a list of campaign finance filing 
links from the Federal Election Election Commission. The form for 
these electronic filings is found at the below link:

    http://fec.gov/finance/disclosure/efile_search.shtml

HELPFUL LINKS:
 * http://www.crummy.com/software/BeautifulSoup/documentation.html
 * http://docs.python-requests.org/en/latest/user/quickstart/
 * http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

"""
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
# return a response object containing the status of the request --ie 
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

    #TODO: download the newest filing

else:
    # Gracefully exit the program if response code is not 200
    sys.exit("Response code not OK: %s" % response.status_code)

