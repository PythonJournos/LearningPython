
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
        
























'''
Reference script:
# Define linetrim function
def linetrim(a):
    if len(a) == 701:
        return a
    else:
        return a.rstrip().ljust(700) + '\n'

# Define parsefilename function
def parsefilename(a, b):
    if b < 9:
        return a.replace('xx', '0' + str(b + 1))
    else:
        return a.replace('xx', str(b + 1))
    
# Create source directory and source file name variables.
srcDir = 'C:\\Python25\\Scripts\\Data\\'
srcFile = 'opra06xx.txt'



# NOTE:
# LOOP BELOW ONLY COVERS FIRST 12 FILES.
# REMAINING FILES HAD NOT BEEN COPIED TO MY COMPUTER YET.



# Create loop for 21 county files
for z in range(12):

    # Parse file name.
    sourcefile = parsefilename(srcFile, z)

    # Parse destination file name.
    dest = srcDir + 'Justified\\' + sourcefile.replace('.','-justified.')

    # Add full path to source file name.
    sourcefile = srcDir + sourcefile

    # Create and open destination file
    x = open(dest, 'w')

    # Create for loop to cycle through source file
    for line in open(sourcefile, 'rb'):
        y = linetrim(line)
        x.write(y)

    # Close destination file
    x.close()

    # Print message
    print sourcefile.replace(srcDir, '') + ' processed!'
'''
