#!/usr/bin/env python
"""
Below is a bare-bones example showing how to read data from a CSV.

We combine a "for" loop with the "open" function to read each line
and add it to a list.
 
The "open" function accepts a number of extra options, but in 
in its most basic form can simply be called with the path to a file.
"""
# A list to store our data points
data_store = []

# Loop through lines, do some basic clean up, and
# add data to our data_store
for line in open('data/banklist.csv'):
    clean_line = line.strip()
    data_points = clean_line.split(',')
    data_store.append(data_points)

for line in data_store:
    print line
