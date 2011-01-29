#!/usr/bin/env python
"""
This script demonstrates how to use column metadata to extract data 
points from a fixed-width text file.

Details such as the start and end positions of columns, 
when known in advance, can allow us to code a more flexible 
application. This lets us avoid having to update lots of hard-coded
start and end positions if the structure of our source data changes.

For this example, we're using the Federal Election Commission's master 
list of campaign committees:

  ftp://ftp.fec.gov/FEC/cm_dictionary.txt
  ftp://ftp.fec.gov/FEC/cm12.zip

The data dictionary describes the fields in the "foiacm.dta" file, 
contained in cm12.zip. It contains info such as the field's name,
start and end positions, and length.

Below, we've hard-coded the header values below from the data
dictionary. Ideally, in a real-world application, these header 
values would be extracted dynamically from an external source 
such as the data dictionary. 

See below for additional ideas on how to improve and extend this code sample.

        ####  Additional Exercises #### 

 - Create a function that performs additional clean-up on each
   data point, such as stripping extra white space, converting
   strings to integers, etc.

 - Update the parse_data function to accept a file argument, rather
   than hard-coding a path to a file 

 - Write a new function that uses the length of a column, rather than
   its offsets, to extract each field from a line

 - Write a function that can parse the FEC data dictionary and dynamically
   extract the column header info
"""

# Below are three data points from our data dictionary:
# name, start-end position, number of characters
# remember that we're extracting these header values
# initially as strings
headers = [
  ("Committee Identification",      "1-9",     "9"),
  ("Committee Name",                "10-99",   "90"),
  ("Treasurer's Name",              "100-137", "38"),
  ("Street One",                    "138-171", "34"),
  ("Street Two",                    "172-205", "34"),
  ("City or Town",                  "206-223", "18"),
  ("State",                         "224-225", "2"),
  ("Zip Code",                      "226-230", "5"),
  ("Committee Designation",         "231-231", "1"),
  ("Committee TypeType",            "232-232", "1"),
  ("Committee Party",               "233-235", "3"),
  ("Filing Frequency",              "236-236", "1"),
  ("Interest Group Category",       "237-237", "1"),
  ("Connected Organiz's NameError", "238-275", "38"),
  ("Candidate Identification",      "276-284", "9"),
]

def get_column_offsets(headers):
    """
    Two key rules to remember when using the slice notation
      1) Values are zero-indexed, meaning you start counting from 
           0 instead of 1
      2) The first index in the slice notation is *inclusive*, while 
         the second is *exclusive*
    
    >>> x = 'Python'
    >>> x[0:2] # get the first two letters (positions 0 and 1)
    'Py'
    """ 
    column_offsets = []
    for header in headers:
        # We do a bunch of work in one line below
        #  Extract the second item from the tuple
        #  Split that item on the dash
        #  Assign the resulting values from the split operation 
        #    to a pair of variables (start_value, end_value)
        start_value, end_value = header[1].split('-')
        # Before  our indexes, we need to convert our 
        # values from strings to integers, and "zero-index" our
        # start position by subtracting 1 
        column_offsets.append( (int(start_value) - 1, int(end_value)) )
    # finally, we return our list of column offsets
    return column_offsets


def parse_data():
    """
    This function returns a list of parsed campaign committee records.
    It relies on the get_column_offsets function to extract the data
    points from each line.
    """
    column_offsets = get_column_offsets(headers)
    
    # Set up a list to store our parsed committee records
    committees_data = []
    
    # Extract the data using our offsets
    for line in open('foiacm.dta'):
        # For each line, create a record to store the various data points
        record = []
        
        # Now, step through each of our column_offsets
        # and use them to extract the fields from our
        # line. Recall that the values in the column_offsets
        # list are just tuples like (0-9). So below,
        for start, end in column_offsets:
            # ADDITIONAL DATA CLEANING HERE
            # Below, we're just appending each column
            # to a list, and then returning that list. 
            # In a real application, this would be a good place
            # to do some additional data clean-up,
            # such as calling the strip method on each 
            # value, converting strings to integers as appropriate, etc.
            record.append(line[start:end])
        committees_data.append(record)
    
    # Return our parsed records
    return committees_data

# The below code snippet ("if __name__ == '__main__') is a very common
# convention used in Python programs. Basically, it tells Python to run 
# the ensuing code whenever the program is called from the command line.
if __name__ == '__main__':
    # Generate our data points, and then print the first 10 records
    data = parse_data()
    for item in data[:10]:
        print item
