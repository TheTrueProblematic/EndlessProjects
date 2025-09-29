
# Hello fellow programmer! Welcome to our fun little project!
# We're going to create a TextFileReverser, which does exactly what it sounds like it does -
# It goes through a text file and interestingly, it reverses the order of all the lines!

# So buckle up, and let's get this party started! 

# We will need the good ol' sys module to handle command line arguments
import sys

def reverse_lines(filename):
    '''
    This function reads a text file and reverses the order of its lines.
    '''
    # First let's open the text file! Go Python go!
    with open(filename, 'r') as file:
        # Read all the lines from the file, Python makes it so easy! Ain't it cool??
        lines = file.readlines()

    # Now let's do the magic, reverse all the lines. Abracadabra!! 
    lines = lines[::-1]

    # Finally let's write the reversed lines back into our file.
    # Remember to open the file in write mode this time!
    with open(filename, 'w') as file:
        file.writelines(lines)

    # Woo hoo! We've just created a magic spell to reverse text file content. 
    # Ain't Python grand?

# This is the main block of our Python script.
if __name__ == "__main__":
    # Check if file name was passed as a command line argument.
    if len(sys.argv) != 2:
        print("Whoops! We need exactly one argument - the file to reverse. Please try again.")
        # Exit the program
        sys.exit(1)
    
    # Call our magic spell function!
    reverse_lines(sys.argv[1])

# And that's a wrap! You've been absolutely fantastic! I hope you had as much fun as I did. 
# Stay awesome and keep Python-ing! :) 

