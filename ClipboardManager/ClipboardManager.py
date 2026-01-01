
#!/usr/bin/env python3
#Shebang line for Unix systems to run with Python 3

"""
Hey there! Ready to have some clipboard fun? Then let's go!
This is a solid little piece of code that takes stdin and saves it right away to your clipboard.
Now you don't have to keep typing or pasting the same things over and over again. Hurray for efficiency!
"""

import sys
# Let's bring in sys so that we can work with standard input (stdin)

def read_from_stdin():
    """
    Time to listen! This function reads input from stdin line by line.
    The end of your input is indicated by EOF signal (Ctrl + D in Unix or Ctrl + Z in Windows).
    """
    return sys.stdin.readlines()

def write_to_clipboard(input):
    """
    Put it in the magic pocket (AKA the clipboard)! This function takes a list of strings,
    joins them together into a single string, and saves it to the clipboard.
    Psst, note that we're just using the built-in functions in python, no extra libraries needed.
    """
    input_string = ''.join(input)
    command = 'echo ' + input_string.strip() + '| clip'
    return os.system(command)

def main():
    """
    And... action! This is our main function that does the magic of reading from stdin
    and writing to clipboard in one smooth move.
    """
    # Grab the input
    input = read_from_stdin()
    # And secure it in the clipboard!
    write_to_clipboard(input)


# Time to call our main function...
if __name__ == "__main__":
    main()

