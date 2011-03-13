#!/usr/bin/env python
"""
This script shows how to read and write data using Python's built-in csv module.
The csv module is smart enough to handle fields that contain apostrophes, 
commas and other common field delimiters. In this tutorial, we'll show how to:
 * use csv to read data
 * work with CSV column headers
 * read data as a stream 
 * write data back out using csv

The official Python docs for the csv module can be found here:
  http://docs.python.org/library/csv.html

For this tutorial, we're using a subset of the FDIC failed banks list:
  http://www.fdic.gov/bank/individual/failed/banklist.html

"""
import csv
from datetime import datetime


"""
            Why the CSV module? 

With simple CSV data, you can often get away with reading data
from a file and "manually" handling the process of splitting up
lines into appropriate columns. 

But the manual approach is tricky and error-prone when dealing with
all but the simplest source data.

In the bank data, for instance, we see that the manual approach 
of splitting on commas will not work because the first bank 
-- "San Luis Trust Bank, FSB " -- contains a comma in its name.

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
each line of the file and smartly parsing the fields.

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


            Customizing the Delimiters

By default, csv reader assumes the file is comma-delimited.
You can customize the delimiters, quote characters, and
a number of other options by setting additional parameters
when you create the reader object. More details on the avaiable 
options are here:
  http://docs.python.org/library/csv.html#dialects-and-formatting-parameters

Below, we set the field delimiter to a tab so that we can read a version 
of the bank data formatted as a "tsv" (tab-separated values).

"""

print "\n\nExample 3: Read tab-delimited data\n"

bank_file = csv.reader(open('data/banklist_sample.tsv', 'rb'), delimiter='\t')

for record in bank_file:
    print record

"""
        Working with Column Headers


CSVs often come with column headers that you'll want to retain as labels
for data points. There are a number of ways to do this, and the approach
can vary depending on the number of columns and size of the file.

The simplest approach is to read all of the data into memory as a list,
and then grab the column headers from the beginning of the list.

"""

print "\n\nExample 4: Extracting Column Headers and Writing Out Data\n"

# Read all lines using a list comprehension
bank_records = [line for line in csv.reader(open('data/banklist_sample.tsv', 'rb'), delimiter='\t')]

# Pop header from the start of the list and save it
header = bank_records.pop(0) 
print header

# Open a new file object
outfile = open('data/banklist_sample_reformatted_dates.tsv', 'wb')

# Create a writer object
outfileWriter = csv.writer(outfile, delimiter='\t')

# Write out the header row
outfileWriter.writerow(header) 

# Now process and output the remaining lines. 
for record in bank_records:
    # Do some basic processing and then write the data back out

    # Below, we use Python's built-in datetime library to reformat 
    # the Closing and Update dates. 

    # First, we use the "strptime" method to parse dates formatted 
    # as "23-Feb-11" into a native Python datetime object.

    # Then we apply the "strftime" method to the resulting datetime
    # object to create a date formatted as YYYY-MM-DD.
    record[-1] = datetime.strptime(record[-1], '%d-%b-%y')
    record[-1] = record[-1].strftime('%Y-%m-%d')

    # We can combine the above steps into a single line
    record[-2] = datetime.strptime(record[-2], '%d-%b-%y').strftime('%Y-%m-%d')

    # Print to the shell and write data out to file
    print record
    outfileWriter.writerow(record)

# Closing the file ensures your data flushes out of the buffer 
# and writes to the output file
outfile.close()

"""
When working with large files, it's often wise to avoid reading the 
entire file into memory. Instead, you can read the data as a stream,
plucking each line from the file object as needed.

The way to do this is by calling a file object's "next" method. This is
what Python does implicitly when stepping through the lines of a file
in a "for" loop. We'll use the same method to extract our header line,
before continuing to process the file as a stream.

More details on file objects and the next method are here:
    http://docs.python.org/library/stdtypes.html#file.next

"""
print "\n\nExample 5: Reading Large Files as a Stream\n"

# Create a csv file object
bank_file = csv.reader(open('data/banklist_sample.tsv', 'rb'), delimiter='\t')

# Grab the header line from the file by calling the file object's next method
header = bank_file.next() 
print header

# Now proceed to process the remaining lines as normal
for record in bank_file:
    print record
