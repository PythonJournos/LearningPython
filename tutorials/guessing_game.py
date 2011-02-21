"""
This script demonstrates statement concepts in Chapter 10
of Learning Python, 4th Edition, by Mark Lutz.
Script adapted from a game in http://inventwithpython.com/chapter4.html
"""

# A guess-the-number game.

# Module for generating random numbers
import random

# Init variables to count guesses and for a number to be guessed
guessesTaken = 0
number = random.randint(1, 20)

# Get the player's name. 
# Also, use a newline character (\n) to pretty up the screen
myName = raw_input('\nHello! What is your name? ')

print "\nLet's play a game, " + myName + '. I am thinking of a number between 1 and 20.'

# Here's our while loop. The player gets six tries.
# Note that we can nest if/else statements in others
while guessesTaken < 6:

# If it's the player's first try, print one statement; on subsequent tries, print 'another'
    if guessesTaken == 0:
        print 'Take a guess: ' 
    else: print 'Take another guess: '  # Note the alternate to indenting
    
# Retrieve the guess and increment the counter by 1
    guess = raw_input()
    guessesTaken = guessesTaken + 1

# Here we use a try/except statement to catch errors that occur if the player
# types in a string or a decimal instead of a whole number.
#
# In the "try" portion, we attempt to convert the input to an integer.
# If that fails, the "except" block is triggered and we print a warning.
#
# If conversion succeeds, the "else" block executes and we give hints. Again,
# nested if/else statements are used to provide levels of hints. Ultimately,
# if the player guesses the number or if the number of attempts maxes out, 
# we exit the loop.
    try:
        guess = int(guess)
    except:
        print 'Whole numbers only, please!'
    else:     
        if guess < number:
            if guess == number - 1:
                print "You're low but real close!"
            else:
                print 'Your guess is too low.' 
        elif guess > number:
            if guess == number + 1:
                print "You're high but real close!"
            else: 
                print 'Your guess is too high.'
        elif guess == number:
            break

# Finally, two blocks to display success or failure.
if guess == number:
    guessesTaken = str(guessesTaken)
    print '\nYou got it, ' + myName + '! You guessed my number in ' + guessesTaken + ' tries!'

if guess != number:
    number = str(number)
    print '\nOut of luck! The number I was thinking of was ' + number

