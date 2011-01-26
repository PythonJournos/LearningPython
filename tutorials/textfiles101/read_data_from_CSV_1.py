#!/usr/bin/env python
"""
Below is a bare-bones example showing how to read data from a CSV.

We combine a "for" loop with the "open" function to read each line
and print it to the command-line screen.
 
The "open" function accepts a number of extra options, but in 
in its most basic form can simply be called with the path to a file.
"""

# Note to Windows users: When specifying a file path, be sure you
# set the file path appropriately with back-slashes
for line in open('data/SmokeFreeComplaints_tab_delimited.csv'):
    print line
