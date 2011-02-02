"""
This script performs a Twitter search on Egypt, for English language tweets.  Using the Twitter JSON API, it takes those tweets, iterates through returned JSON files
and pulls key information into a CSV.  Could be adapted to transform other JSON APIs into structured data in spreadsheet or database form.
"""

#To put this into a CSV, csv code adapted from this recipe (http://www.palewire.com/posts/2009/03/03/django-recipe-dump-your-queryset-out-as-a-csv-file/) of Ben Welsh at the LAT (who taught me much of this while I interned over there):


# IMPORTS


#Make Python understand how to read things on the Internet
import urllib2

#Make Python understand the stuff in a page on the Internet is JSON
import json

# Make Python understand csvs
import csv

# Make Python know how to take a break so we don't hammer API and exceed rate limit
from time import sleep

# tell computer where to put CSV
outfile_path='/Users/MichelleMinkoff/Desktop/test.csv'

# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))

#create a list with headings for our columns
headers = ['user', 'date_created','tweet_text','latitude', 'longitude']

#write the row of headings to our CSV file
writer.writerow(headers)


# GET JSON AND PARSE IT INTO DICTIONARY

# We need a loop because we have to do this for every JSON file we grab

#set a counter telling us how many times we've gone through the loop, this is the first time, so we'll set it at 1
i=1

#loop through pages of JSON returned, if you have 100 tweets per pg, and there's 1500 tweet limit on searches, 15 pages will do it
while i<=15:
    #print out what number loop we are on, which will make it easier to track down problems when they appear
    print i
    #create the URL of the JSON file we want.  We search for 'egypt', want English tweets, and set the number of tweets per JSON file to the max of 100, so we have to do as little looping as possible
    url = urllib2.Request('http://search.twitter.com/search.json?q=egypt&lang=en&rpp=100&page=' + str(i))
    #use the JSON library to turn this file into a Pythonic data structure
    parsed_json = json.load(urllib2.urlopen(url))    
    #now you have a giant dictionary.  Type in parsed_json here to get a better look at this.  You'll see the bulk of the cotent is contained inside the value that goes with the key, or label "results".  Refer to results as an index.  Just like list[1] refers to the second item in a list, dict['results'] refers to values associated with the key 'results'.  I'll do a better job explaining for next week.
    print parsed_json


#TRANSFORM JSON INTO STRUCTURED ROWS THAT FORM OUR CSV


    #run through each item in results, and jump to an item in that dictionary, in this case, the text of the tweet    
    for tweet in parsed_json['results']:
            #initialize the row
            row = []
            #add every 'cell' to the row list, identifying the item just like an index in a list
            row.append(str(tweet['from_user'].encode('utf-8')))           
            row.append(str(tweet['created_at'].encode('utf-8')))
            row.append(str(tweet['text'].encode('utf-8')))
            #Often, no geo info comes with the tweet.  Python can't grab nothing, so it'll choke.
            #We help the computer out by putting on a condition: Only do the following, if there's a value to go with the geo key.
            if tweet['geo']:
                #We need to dig into the geo object, which is yet ANOTHER dictionary, to get to the coordinates list.
                #Then separate that list into two separate columns, so we can deal w/lat + long separately.
                # We use the index to specify which item in the list we care about.
                row.append(str(tweet['geo']['coordinates'][0]).encode('utf-8'))
                row.append(str(tweet['geo']['coordinates'][1]).encode('utf-8'))
           # Wait!  What if there's no geo information?  Let's fill those cells in with empty strings.
           #It's not a big deal here, but if we had more columns after the blank ones, without something in these cells, the next cells would be two columns off.
           #The list structure takes positions very literally, so I've found it to be good practice to fill in cells with an else condition to avoid mistakes.
            else:
                row.append("")
                row.append("")
            #once you have all the cells in there, write the row to your csv
            writer.writerow(row)
    #increment our loop counter, now we're on the next time through the loop
    i = i +1
    #tell Python to rest for 5 secs, so we don't exceed our rate limit
    sleep(5)