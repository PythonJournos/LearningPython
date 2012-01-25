#!/usr/bin/env python
"""
The third scrape in our series demonstrates how to fetch data from
a remote server by making a POST request.

For this scrape, we'll request a list of campaign finance filing 
links from the Federal Election Election Commission. The form for 
these electronic filings is found at the below link:

    http://fec.gov/finance/disclosure/efile_search.shtml

"""
#TODO: add documentation links for language features and libs
import sys

import requests
from BeautifulSoup import BeautifulSoup

# Build a dictionary containing our form field values
form_data = {
    'name':'Romney', # committee name field
    'type':'P',      # committee type is P for Presidential
    'frmtype':'F3P', # form type
}

# Make the POST request by passing in our form data. This should 
# return a response object that contains status codes for your request and the
# raw HTML of the page.
response = requests.post('http://query.nictusa.com/cgi-bin/dcdev/forms/', data=form_data)

# If the response is OK, then process the HTML
if response.status_code == 200:

    # the raw HTML is stored in the response object's "text" attribute
    soup = BeautifulSoup(response.text)
    links = soup.findAll('a') 

    # Extract the download links 
    download_links = []
    for link in links:
        if link.text == 'Download':
            download_links.append(link)

    #NOTE: You can tighten up the above code by leveraging BeautifulSoup's 
    # more advanced features, which allow you to filter the results of the 
    # "findAll" method by using regular expressions or lambda functions. 
    #
    # Below, we use a lambda function to filter for links with "href" 
    # attributes starting with a certain URL path:

    #download_links = soup.findAll('a', href=lambda path: path.startswith('/cgi-bin/dcdev/forms/DL/'))
     
    # To learn more: 
    # http://www.crummy.com/software/BeautifulSoup/documentation.html#The basic find method: findAll(name, attrs, recursive, text, limit, **kwargs)
    # http://stackoverflow.com/questions/890128/python-lambda-why
    # http://docs.python.org/howto/regex.html

else:
    # Gracefully exit the program if response code is not 200
    sys.exit("Response code not OK: %s" % response.status_code)

