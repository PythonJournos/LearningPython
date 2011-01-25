import os, glob
path = './iterables'   # set our directory path

# Here is our function
def process(filename):
    print a.read()     # read and print the file contents

# iterate through all files in the path specified above
for infile in glob.glob( os.path.join(path, '*.*') ):
    a = open(infile)   # open the file, assign it to a
    process(a)         # call the process function, pass in a
    a.close()          # close the file


