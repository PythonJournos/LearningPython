
'''
This script is used to import 2010 Census redisticting data.
Written using Python 2.6.6

Prior to running this script, you should:
1 - Set the source directory (srcDir)
2 - Make sure your data files are in that directory.
3 - Set the names of your three SQLite tables (geotablename,
    data1tablename, data2tablename)

There are three types of files:
 * Geographic header files (*geo.txt)
 * Data files (first set) (*01.txt)
 * Data files (second set) (*02.txt)

The script will ignore any files that do not have a .txt extension.
Similarly, the program will stop if it finds a .txt file that does
not  meet one of the above three criteria for valid files.

'''

# import modules
import os
import glob
import sqlite3

# Specify source directory
srcDir = 'C:\\Data\\Census\\'

# Specify path of SQLite database
dbpath = '\\\\asb-bus02\\userdata\\cschnaars\\SQLite\\CenRedistData2010.sqlite'

# Specify table names
geotablename = 'tblTest'
data1tablename = 'tblData1'
data2tablename = 'tblData2'

# Connect to the sqlite database
db = sqlite3.connect(dbpath)

# Create a cursor
cursor = cnx_object.cursor()

# Run SQL scripts to create the data tables if they don't exist
SQL = 'CREATE TABLE IF NOT EXISTS "' + geotablename + '''" (
"FILEID" char(6) NOT NULL, "STUSAB" char(2) NOT NULL,
"SUMLEV" char(3) NOT NULL, "GEOCOMP" char(2) NOT NULL,
"CHARITER" char(3) NOT NULL, "CIFSN" char(2) NOT NULL,
"LOGRECNO" char(7) PRIMARY KEY NOT NULL UNIQUE, "REGION" char(1) NOT NULL,
"DIVISION" char(1) NOT NULL, "STATECODE" char(2) NOT NULL,
"COUNTY" char(3) DEFAULT NULL, "COUNTYCC" char(2) DEFAULT NULL,
"COUNTYSC" char(2) DEFAULT NULL, "COUSUB" char(5) DEFAULT NULL,
"COUSUBCC" char(2) DEFAULT NULL, "COUSUBSC" char(2) DEFAULT NULL,
"PLACE" char(5) DEFAULT NULL, "PLACECC" char(2) DEFAULT NULL,
"PLACESC" char(2) DEFAULT NULL, "TRACT" char(6) DEFAULT NULL,
"BLKGRP" char(1) DEFAULT NULL, "BLOCK" char(4) DEFAULT NULL,
"IUC" char(2) DEFAULT NULL, "CONCIT" char(5) DEFAULT NULL,
"CONCITCC" char(2) DEFAULT NULL, "CONCITSC" char(2) DEFAULT NULL,
"AIANHH" char(4) DEFAULT NULL, "AIANHHFP" char(5) DEFAULT NULL,
"AIANHHCC" char(2) DEFAULT NULL, "AIHHTLI" char(1) DEFAULT NULL,
"AITSCE" char(3) DEFAULT NULL, "AITS" char(5) DEFAULT NULL,
"AITSCC" char(2) DEFAULT NULL, "TTRACT" char(6) DEFAULT NULL,
"TBLKGRP" char(1) DEFAULT NULL, "ANRC" char(5) DEFAULT NULL,
"ANRCCC" char(2) DEFAULT NULL, "CBSA" char(5) DEFAULT NULL,
"CBSASC" char(2) DEFAULT NULL, "METDIV" char(5) DEFAULT NULL,
"CSA" char(3) DEFAULT NULL, "NECTA" char(5) DEFAULT NULL,
"NECTASC" char(2) DEFAULT NULL, "NECTADIV" char(5) DEFAULT NULL,
"CNECTA" char(3) DEFAULT NULL, "CBSAPCI" char(1) DEFAULT NULL,
"NECTAPCI" char(1) DEFAULT NULL, "UA" char(5) DEFAULT NULL,
"UASC" char(2) DEFAULT NULL, "UATYPE" char(1) DEFAULT NULL,
"UR" char(1) DEFAULT NULL, "CD" char(2) DEFAULT NULL,
"SLDU" char(3) DEFAULT NULL, "SLDL" char(3) DEFAULT NULL,
"VTD" char(6) DEFAULT NULL, "VTDI" char(1) DEFAULT NULL,
"RESERVE2" char(3) DEFAULT NULL, "ZCTA5" char(5) DEFAULT NULL,
"SUBMCD" char(5) DEFAULT NULL, "SUBMCDCC" char(2) DEFAULT NULL,
"SDELM" char(5) DEFAULT NULL, "SDSEC" char(5) DEFAULT NULL,
"SDUNI" char(5) DEFAULT NULL, "AREALAND" char(14) NOT NULL,
"AREAWATR" char(14) NOT NULL, "AREANAME" varchar(90) NOT NULL,
"FUNCSTAT" char(1) NOT NULL, "GCUNI" char(1) DEFAULT NULL,
"POP100" char(9) NOT NULL, "HU100" char(9) NOT NULL,
"INTPTLAT" char(11) NOT NULL, "INTPTLON" char(12) NOT NULL,
"LSADC" char(2) NOT NULL, "PARTFLAG" char(1) DEFAULT NULL,
"RESERVE3" char(6) DEFAULT NULL, "UGA" char(5) DEFAULT NULL,
"STATENS" char(8) NOT NULL, "COUNTYNS" char(8) DEFAULT NULL,
"COUSUBNS" char(8) DEFAULT NULL, "PLACENS" char(8) DEFAULT NULL,
"CONCITNS" char(8) DEFAULT NULL, "AIANHHNS" char(8) DEFAULT NULL,
"AITSNS" char(8) DEFAULT NULL, "ANRCNS" char(8) DEFAULT NULL,
"SUBMCDNS" char(8) DEFAULT NULL, "CD113" char(2) DEFAULT NULL,
"CD114" char(2) DEFAULT NULL, "CD115" char(2) DEFAULT NULL,
"SLDU2" char(3) DEFAULT NULL, "SLDU3" char(3) DEFAULT NULL,
"SLDU4" char(3) DEFAULT NULL, "SLDL2" char(3) DEFAULT NULL,
"SLDL3" char(3) DEFAULT NULL, "SLDL4" char(3) DEFAULT NULL,
"AIANHHSC" char(2) DEFAULT NULL, "CSASC" char(2) DEFAULT NULL,
"CNECTASC" char(2) DEFAULT NULL, "MEMI" char(1) DEFAULT NULL,
"NMEMI" char(1) DEFAULT NULL, "PUMA" char(5) DEFAULT NULL,
"RESERVED" char(18) DEFAULT NULL);'''

cursor.execute(SQL)

# Iterate through each file in the directory
for datafile in glob.glob(os.path.join(srcDir, '*.txt')):

    # Determine file type
    if datafile.endswith('geo.txt'):
        filetype = 'geo'
    elif datafile.endswith('01.txt'):
        filetype = 'data1'
    elif datafile.endswith('02.txt'):
        filetype = 'data2'
    else:
        print 'File not recognized: ' + datafile
        break

    # Iterate through each line in the file
    #for line in open(datafile, 'rb'):   # Should this be 'r' or 'rb'?
     #   parseddata = line.split(',')    # Copy the line to a list
        
























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
