#!/usr/bin/env python
"""
This scrape demonstrates how to 'page through' links and build on other
scripts in the PyJournos webscraping tutorial folder located here:

    https://github.com/PythonJournos/LearningPython/tree/master/tutorials/webscraping101

The site that we are using for this example can be found here:

    http://staticresults.sos.la.gov/


USAGE:

You can run this scrape by going to command line, navigating to the
directory containing this script, and typing the below command:

    python la_election_scrape.py

This script assumes that you learned about the requests library from the
fec_efiles_scrape.py file. Also, please note, that this script can take more than
30 seconds to run. Be patient.

HELPFUL LINKS:

 Python Modules used in this script:
 * BeautifulSoup: http://www.crummy.com/software/BeautifulSoup/documentation.html
 * CSV:           http://docs.python.org/library/csv.html
 * requests:      http://docs.python-requests.org/en/latest/user/quickstart/

 HTTP codes
 * http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

"""
import csv
import requests

from BeautifulSoup import BeautifulSoup

URL = 'http://staticresults.sos.la.gov/'

response = requests.get(URL)

# Create an empty link to identify bad links & race links
bad_links = []
races_links = []
date_links = []

if response.status_code == 200:

    # Parse the HTML into a form that's easy to use
    soup = BeautifulSoup(response.text)

    # Use BeautifulSoup's API to extract your data
    # This page is clean & simple. All links are links we want to crawl.
    # So, let's grab them all.

    for tag in soup.table:

        # soup.table is made of h1 tags & links.
        # only save links, which have a name equal to 'a'
        if tag.name == 'a':

            # 'href' is an attribute of item
            relative_link = tag['href']

            # the election date the text, so let's grab that to associate
            # with the link
            date = tag.text

            # we need a complete link to follow, so let's create that
            absolute_link = URL + relative_link

            # now we add the date & abs link to our list
            date_links.append((date, absolute_link))

'''
Note: at this point, we have a list links that looks something like this:
[
(u'04051986', u'http://staticresults.sos.la.gov/04051986/Default.html')
(u'02011986', u'http://staticresults.sos.la.gov/02011986/Default.html')
(u'01181986', u'http://staticresults.sos.la.gov/01181986/Default.html')
(u'03301985', u'http://staticresults.sos.la.gov/03301985/Default.html')
...
]
'''

# Now, we would apply the same logic as we are approaching the first page,
# except for now, we would apply that logic to each link in a for loop.
# Let's pull out links all of the race types on each page

for item in date_links:

    # to clarify which item is which in each tuple
    # this is extra code for demo purposes
    # Example item: (u'03301985', u'http://staticresults.sos.la.gov/03301985/Default.html')
    date = item[0]
    link = item[1]

    # this looks familar
    response = requests.get(link)

    # while we do not explain functions in this demo, this would be a good use
    # if you are feeling adventurous, you should try to turn & the code at
    # the start of the script into a funciton, then call that function

    if response.status_code == 200:
        soup = BeautifulSoup(response.text)

        # more familar stuff
        races_tags = soup.table.findAll('a')
        for races_tag in races_tags:
            relative_link = races_tag['href']
            absolute_link = URL + relative_link

            # now let's add the date, races_type, and races_link to the tuple
            races_type = races_tag.text
            races_links.append((date, races_type, absolute_link))

    else:
        bad_links.append((response.status_code, link))


################################################################################

# THE RESULTS:
# This is for easy viewing of the new list & not required for this script
count = 0
while count < 20:  # The number 50 is used to limit the output.
    for link in races_links:
        print "Election date: %s, Races link type: %s, Link: %s" % (link[0], link[1], link[2])
        count+=1

# Let's see which links failed
for bad_link in bad_links:
    print "Response code: %s, Link: %s" % (bad_link[0], bad_link[1])


'''
End Result looks something like this:
[
(u'10/22/2011', u'All Races in a Parish', u'http://staticresults.sos.la.gov/10222011_Parishes.html')
(u'07/16/2011', u'All Races in a Parish', u'http://staticresults.sos.la.gov/07162011_Parishes.html')
(u'04/30/2011', u'LA Legislature Races', u'http://staticresults.sos.la.gov/04302011_Legislative.html')
(u'04/30/2011', u'Multi-Parish Races', u'http://staticresults.sos.la.gov/04302011_MultiParish.html')
....
]

These are the bad links that came back:
[(404, u'http://staticresults.sos.la.gov/11021982/Default.html'),
(404, u'http://staticresults.sos.la.gov/09111982/Default.html')]
'''
