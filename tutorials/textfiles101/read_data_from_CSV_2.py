#!/usr/bin/env python
"""
This script shows how to read data using Python's built-in csv module.

    http://docs.python.org/library/csv.html

The csv module is smart enough to handle fields that contain apostrophes, 
commas and other common field delimiters.

For this tutorial, we're using a subset of the FDIC failed banks list:

    http://www.fdic.gov/bank/individual/failed/banklist.html

"""
import csv


"""
            Why the CSV module? 

The manual approach to splitting CSV records into columns
is often tricky and error-prone.

In the below example, we see that splitting on a comma
does not work for the first record in our bank data.
"""

print "\n\nExample 1: Split lines manually\n"

for line in open('data/banklist_sample.csv'):
    clean_line = line.strip()
    data_points = clean_line.split(',')
    print data_points

"""
Splitting on a comma caused "San Luis Trust Bank, FSB " 
to become two fields: "San Luis Trust Bank" and "FSB".

In a case like this, it's much easier to let Python's 
built-in csv module handle the field parsing for you.

            Introducing the CSV module

We already imported the csv module at the top of this script.
Now we create a csv "reader" object, capable of stepping through
each line of the file and smartly parsing it out for us. 

The reader object is created by passing an open file to csv's 
reader method.
"""

print "\n\nExample 2: Read file with the CSV module\n"
bank_file = csv.reader(open('data/banklist_sample.csv', 'rb'))

for record in bank_file:
    print record 

"""
Notice that in the above example, csv is smart enough to handle 
the comma inside the first bank name. So instead of two fields,
it gives us "San Luis Trust Bank, FSB" as a single field.


            Customizing the delimiters

 By default, csv reader assumes the file is comma-delimited
 You can customize the delimiters and field quote characters by using 
 extra options when you create the reader object
"""
#TODO: Create new sample .tsv file with pipes as quote character
#print "\n\nExample 2: Read file with the CSV module\n"
#bank_file = csv.reader(open('data/banklist_sample.csv', 'rb'))
#
#for record in bank_file:
#    print record 

"""
        Working with Column Headers

- demo manual approach by first reading in all lines and extracting the
  first line. Show alternative for large files using "next" method to 
  extract first line and then iterating over the remaining lines 

- Even easier: the DictReader approach
"""
