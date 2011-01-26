'''
This script is used to import 2010 Census redisticting data.
Written using Python 2.7.1

Prior to running this script, you should set the source directory
(srcDir) and make sure your three data files are in the appropriate
directories: Geo, Data1 and Data2.

You also should check the file extension and alter the "for datafile"
line of code accordingly. Presently, the file extension is set to .txt.
'''

# import modules
import os
import glob

# Specify source directory
srcDir = 'C:\\Data\\Census\\'

# Note: We need to determine whether the Census files will
# have a file extension and adjust the code below accordingly.

# Iterate through each file in the directory
for datafile in glob.glob(os.path.join(srcDir, '*.txt')):

    # Iterate through each line in the file
    for line in open(datafile, 'rb'):   # Should this be 'r' or 'rb'?
        parseddata = line.split(',')    # Copy the line to a list
        

