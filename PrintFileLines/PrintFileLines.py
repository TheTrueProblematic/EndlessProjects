
# Hello, happy programmers! Let's have some fun coding.
# This awesome, minimalistic, multi-platform CLI script will read a file and print each line. It's like throwing an awesome party for our line-friends!
# The best thing? No libraries, no internet, no GUI required. It's our little secret club, but for file lines!

# We will only need this super handy built-in python function for file related stuff!
import sys

# We will provide the name of the file as a command-line argument. It's like Python's mailman delivering the file name as a letter.
filename = sys.argv[1]

# Let's open that letter... I mean file. Just like opening a box of happiness!
# We're using the 'with' keyword so Python automatically close it later, because, ya know we don't want our happiness-box remains opened!
with open(filename, 'r') as file:

    # Now let's read each line just as you savour each slice of a pizza, one slice at a time.
    for line in file:

        # Let's spread the joy of each line to the world! Okay, just printing it for now.
        print(line, end = '') # using end = '' as print() adds an extra \n by default

# And that's it, folks! Simple, fun and resourceful! Just like Python. Keep coding and stay awesome!

