#!/usr/bin/env python
"""
This script demonstrates an alternative method for flexibly parsing 
fixed-width text.

In cmte_parser.py, we extracted each data point using the start and 
end points for each column (based on column descriptions in a data 
dictionary).

This time, we'll use Python's "struct" module to extract the columns.  
This built-in module lets you parse a string according to a pre-determined
format. For more details on the struct module, see:
  
  http://docs.python.org/library/struct.html


For this example, we'll use the Federal Election Commission's 
committee-to-committee, itemized contributions:

  ftp://ftp.fec.gov/FEC/DATA_DICTIONARIES/oth_dictionary.txt
  ftp://ftp.fec.gov/FEC/oth12.zip

The data dictionary describes the fields in the "itoth.dta" file, 
contained in itoth12.zip. It contains info such as the field's name,
start and end positions, and data type and length.
"""
from struct import unpack

# Below, we've hard-coded the FEC's field format codes, but ideally, these
# would be extracted dynamically from the data dictionary or another
# external file
FEC_FORMAT_CODES = ['9s', '1s', '3s', '1s', '11s', '3s', '34s', '18s', '2s', 
                    '5s', '35s', '2d', '2d', '2d', '2d', '7n', '9s', '7s',]


def get_header_format(format_codes):
    """
    This function returns a string format for use with the struct module.
    It requires a list of format codes extracted from a Data Dictionary.
    """
    # Below, we use a list comprehension to step through the FEC format codes.
    # Inside the list comp, we use slice notation to extract all but the last
    # the letter of each format code. This last letter represents the FEC's 
    # data-type specifier, which we can use elsewhere to properly convert our
    # data types. 
    # Finally, we use the "join" function to combine the list of format strings
    # and return that string.
    return "".join(["%ss" % format_code[0:-1] for format_code in FEC_FORMAT_CODES])

if __name__ == '__main__':
    format = get_header_format(FEC_FORMAT_CODES)
    for line in open('itoth.dta'):
        print unpack(format, line.strip())
