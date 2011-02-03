#!/usr/bin/env python
"""
This script parses a Census geo header file and converts it to a csv. 
It's just a bare start. Hopefully it's the germ of something.
Eventually, it could be used to populate database tables instead.

Currently the sample AL files and the geo header are both from Census 2000:
http://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/

The geo header fields for Census 2010 are slightly different, but the same approach will work for them if we update the data dictionary.

For the data dictionary, I created a pipe-delimited file from the text of the pdf documentation:
http://www.census.gov/prod/www/abs/pl94-171.pdf

The file layout is "description|fieldname|length|offset."
For example:
    File Identification|FILEID|6|1
    State/US-Abbreviation (USPS)|STUSAB|2|7
    Summary Level|SUMLEV|3|9

There are probably easier and more reusable ways of getting the fields for the data dictionary, such as parsing
the SAS script that comes with the files: 
http://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/0File_Structure/SAS/pl_geohd.sas
or parsing the HTML File Structure README:
http://www2.census.gov/census_2000/datasets/redistricting_file--pl_94-171/0File_Structure/File_Structure_README.htm

I'm not sure, though, that these files will be available for 2010. (They're not included in the 2008 Redistricting Prototype files.)

The approach to parsing the fixed-width format here uses the "unpack" method from the struct module. This method accepts a format string, 
which describes the fixed-width format, and a string to unpack. It returns a tuple representing the parts of the unpacked string.

The format string is a series of single characters representing the data types of parts of the string we're unpacking.
The format character for string is 's'. It can be preceded by an integer representing the size of the string.

So, the pattern describing a five-character string would be '5s'. And if we wanted to match the words in the string "onetwothree" we could 
use '3s3s5s'. 
The result looks like this:

>>> from struct import *
>>> unpack('3s3s5s', 'onetwothree')
('one', 'two', 'three')

"""

from struct import *

# Set up empty arrays for the fieldnames and lengths of the fixed-width fields
fields = []
sizes = []

# Iterate through the data dictionary file, grabbing the fieldname and length of each field
for line in open('./config/geo_file_fields.csv'):
  values = line.split('|')   # Split the line on the pipe delimiter (returns a list or fields)
  fields.append(values[1])   # Grab the fieldname (second field in the row) and push it onto the fields list
  sizes.append(values[2])    # Grab the field size (third field in the row) and push it onto the sizes list

# Create a format string from the field lengths to be used in the unpack function from the struct module
field_pattern = "s".join(sizes) + "s"  # Join the list of field lengths with the format character 's' and add another 's' after the final length.

print ",".join(fields)  # Print out a comma-separated string of the fieldnames to create the header row of the csv

# Iterate through all the lines of a single geo header file (this one for Alabama)
# We could make this loop through all directories, generating output for each state.
for line in open('./data/al/algeo.upl'):
  bare_line = line.rstrip('\n')           # Take off the newline character at the end of the line
  row = unpack(field_pattern, bare_line)  # Use struct.unpack to break out the fields according to the field pattern created above
  print ",".join(row)                     # Print out a comma-separated string of the extracted values
