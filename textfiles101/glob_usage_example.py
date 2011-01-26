#!/usr/bin/env python
"""
 This script shows how to use the glob module to grab a list of 
 filenames in a directory.  This is a convenient way to quickly 
 generate a list of files for additional processing.

 More info on the glob module can be found at:

    http://docs.python.org/library/glob.html
"""
import glob

# Use glob's asterisk wild-card to get a list of all '.csv'
# files in the iterables directory. Note that we're using 
# the glob function inside the identically named glob module,
# hence the "glob.glob" syntax below. 
my_filenames = glob.glob('data/iterables/*.csv')

# Now loop through the files and read the data
for infile in my_filenames:
    a = open(infile)   # open the file, assign it to a
    print a.read()     # call the process function, pass in a
    a.close()          # close the file


# Alternatively, you can combine the "for" loop and glob
# into a single line of code
for infile in glob.glob('data/iterables/*.csv'):
    a = open(infile)   # open the file, assign it to a
    print a.read()     # call the process function, pass in a
    a.close()          # close the file
