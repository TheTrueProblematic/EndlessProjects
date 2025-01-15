
# Welcome to the fun world of palindromes! 🎉
# Palindromes are words that are spelled the same way forwards and backwards. Super cool, right?
# This little script right here is going to help you count how many palindromes are in a sentence. Let's get started, shall we? 

# Python is awesome, it has a built-in string class with lots of cool methods we can use.

def count_palindromes(sentence):
    # First, let's turn our sentence to lowercase and split it into words.
    # Think of it as breaking a chocolate bar into small delicious pieces - nom nom! 🍫
    sentence = sentence.lower().split(' ')
    
    # Then, we'll create a counter variable to keep count of our palindromes (super important!). 
    counter = 0

    # Let's loop through the pieces of our chocolate... oops, I mean words, 
    # and check if they're the same forwards and backwards.
    for word in sentence:
        if word == word[::-1]:  # The ::-1 syntax is a nifty Python trick to reverse a string.
            counter += 1  # If we have a match, the counter goes ding! Or, more accurately, it goes 'plus one'.
    
    # Finally, after we've gone through all of our words, we return the counter.
    # Like a proud fisherman showing off their catch of the day! 🐟
    return counter

# Now, let's test our function!
# This sentence is fed to the function from the command line when you run the script.
import sys
sentence = sys.argv[1] # argv[1] gives the first command line argument
num_of_palindromes = count_palindromes(sentence)

# We'll print the number of palindromes we found.
# It's like a treasure hunt, but with words! 🕵️‍♂️
print('Number of palindromes:', num_of_palindromes)

# And there you have it, my friend! A wonderful little piece of code that does something useful and cool.
# Isn't Python awesome? 🐍

