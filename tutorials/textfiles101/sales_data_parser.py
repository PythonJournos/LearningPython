#!/usr/bin/env python
"""
 This program shows how to read data from a CSV, perform some basic processing 
 on a column in that data, and then write the data out to a new file. 
 
 We first define an address-parsing function at the top of the file.
 Then we jump into the "main" portion of the program, which applies the
 address function to each row of data before writing it out to a new file.
"""
# We begin by importing the csv module, which helps you easily 
# parse tabular data that you'd normally work with in a
# spreadsheet program like Excel.
import csv

# Next, we define a function -- a reusable piece of code -- that will reformat 
# our address. This function checks to see if a direction (N, S, E, W, etc.) is 
# present at the end of an address. If so, it places the direction right before
# the street name: "123 Main St N" --> "123 N Main St"

# We'll apply this function to each address farther down in the  program,  
# when we loop through each line of our source data (below function is 
# courtesy of Brian Bowling).

def parse_address(address):
    # find the first and last spaces in the string
    last_space = len(address) - 1
    first_space = 0

    while address[last_space] != " ":
        last_space -= 1

    while address[first_space] != " ":
        first_space += 1
    
    # Test if the characters following the last space are a direction
    if address[last_space + 1:] in ("N", "S", "E", "W", "NE", "NW", "SE", "SW"):
    # Reformat the address 
        new_address = address[:first_space] + address[last_space:] + address[first_space:last_space]
    else:
        new_address = address

    return new_address


# The "main" function below is where the action happens. It's where we open
# the file, read in the data, apply our function to reformat the address, 
# and then write our data back out to a file. 

def main():

    # Open a file using the csv module
    source_data = csv.reader(open('data/SalesSnippet.csv','rb'))

    # Grab the column names from the first line
    header = source_data.next() # PRICE, ADDRESS, CITY, STATE, ZIP, ORIG

    # Open an output file and add the column headers
    output_file = csv.writer(open('data/SalesSnippet_output.csv','wb')) 
    output_file.writerow(header)

    # Now process the data in the input file
    for row in source_data:
        # Here's where "csv" is really helpful. It automatically parses
        # our columns into a list of data points. All we have to do is 
        # assign these data points to some variables, and then we can 
        # do some additional processing on each one. Below, we use
        # a technique known as "sequence unpacking" to assign the data 
        # points in the "row" variable, which is a list, to a 
        # bunch of variables.
        price, address, city, state, zipcode, orig = row

        # Now we can apply the code to reformat the address
        clean_address = parse_address(address)
        
        # Finally, we write out our new line with the clean address. Note
        # that the "writerow" method requires a list of data of data
        output_file.writerow([price, clean_address, city, state, zipcode, orig])


if __name__ == '__main__':
    main()
