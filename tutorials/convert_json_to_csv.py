

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
outfile_path='/path/to/my/file.csv'

# open it up, the w means we will write to it
writer = csv.writer(open(outfile_path, 'w'))

#create a list with headings for our columns
headers = ['user', 'tweet_text']

#write the row of headings to our CSV file
writer.writerow(headers)


# GET JSON AND PARSE IT INTO DICTIONARY

# We need a loop because we have to do this for every JSON file we grab

#set a counter telling us how many times we've gone through the loop, this is the first time, so we'll set it at 1
i=1

#loop through pages of JSON returned, 100 is an arbitrary number
while i<100:
    #print out what number loop we are on, which will make it easier to track down problems when they appear
    print i
    #create the URL of the JSON file we want.  We search for 'egypt', want English tweets, and set the number of tweets per JSON file to the max of 100, so we have to do as little looping as possible
    url = urllib2.Request('http://search.twitter.com/search.json?q=egypt&lang=en&rpp=100&page=' + str(i))
    #use the JSON library to turn this file into a Pythonic data structure
    parsed_json = json.load(urllib2.urlopen(url))    
    #now you have a giant dictionary.  Type in parsed_json here to get a better look at this.  You'll see the bulk of the cotent is contained inside the value that goes with the key, or label "results".  Refer to results as an index.  Just like list[1] refers to the second item in a list, dict['results'] refers to values associated with the key 'results'.  I'll do a better job explaining for next week.
    print parsed_json



    #run through each item in results, and jump to an item in that dictionary, in this case, the text of the tweet	
    for tweet in parsed_json['results']:
    		#initialize the row
    		row = []
    		#add every 'cell' to the row list, identifying the item just like an index in a list
    		row.append(str(tweet['from_user'].encode('utf-8')))	       
    		row.append(str(tweet['created_at'].encode('utf-8')))
    		row.append(str(tweet['text'].encode('utf-8')))
    		#once you have all the cells in there, write the row to your csv
    		writer.writerow(row)
    #increment our loop counter, now we're on the next time through the loop
    i = i +1
    #tell Python to rest for 5 secs, so we don't exceed our rate limit
    sleep(5)