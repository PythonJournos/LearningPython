#!/usr/bin/env python
"""
Below are two techniques showing how to reformat an address.

The functions below check an address to see if it has a direction
at the end of the address; if so, they reformat the address so the
direction appears before the street name. 

The first function uses indexing and slice notation
to pull apart the address. The second function relies on 
regular expresions to extract the relevant address portions.

Usage examples:

>>> parse_address("123 Main St N")
'123 N Main St'

>>> parse_address_with_regex("123 Main St N")   
'123 N Main St'
"""

import re

def parse_address(address):
    """
    This function uses slice notation to parse and reformat an address.

    More info on slice notation is here:
       http://docs.python.org/tutorial/introduction.html#strings
    """
    # find the first and last spaces in the string
    last_space = len(address) - 1
    first_space = 0

    while address[last_space] != " ":
        last_space -= 1

    while address[first_space] != " ":
        first_space += 1
    
    # test to see if the characters following the last space are a direction
    if address[last_space + 1:] in ("N", "S", "E", "W", "NE", "NW", "SE", "SW"):
    # make the transformation
        new_address = address[:first_space] + address[last_space:] + address[first_space:last_space]
    else:
        new_address = address

    return new_address


# Create a regular expression pattern, which we'll use to match address strings
address_pattern = re.compile(r'^(\w+)\s(.+?)\s(N|S|E|W|NW|NE|SW|SE)$')

def parse_address_with_regex(address_string):
    """
    This function uses a regular expression to parse and reformat an address.

    More info on regular expressions are here:
        http://docs.python.org/library/re.html
    """
    # Try matching the address_string against the address_pattern
    regex_match = address_pattern.match(address_string.strip()) 

    if regex_match:
        # If there's a match, then assign the address components to variables
        number, address, direction = regex_match.groups()
        # Reformat the address components into a new string
        new_address = "%s %s %s" % (number, direction, address)
    else:
        new_address = address_string

    return new_address


if __name__ == '__main__':
    import doctest
    doctest.testmod()
