
#! /usr/bin/python3

# Oh, hey there! I see you've stumbled upon my little creation here.
# Well let me introduce you to this nifty little python script, lovingly dubbed 'LineCounter'
# LineCounter, as I'm sure you have already guessed, does the simple yet vital job of counting lines in a text file. 

# And the good thing is, it's as easy as pie to use! It doesn't require any fancy GUIs, doesn't need the internet, and doesn't even need any pre-installed packages on your shiny new computer. 
# All that's needed is the lovely Python and a CLI. 

# So, Sit Back! Relax! And watch the magic happen! So let's dive right into it, shall we?

import sys      # We'll need this for command line arguments

def count_lines(filename):
    """
    Here's our superstar function, 'count_lines'!
    It takes in a file name, opens it, reads it, and, you guessed it, counts the number of lines! 
    It returns this number to be printed out later.
    """
    with open(filename, 'r') as f: # Open the file in read mode
        return len(f.readlines()) # Here the magic happens! We count the lines and return the count

def main():
    """
    Now we come to the main function. This is where our little script starts its work. 
    It's simple; just call our superstar 'count_lines' with the filename you passed in and print the result!
    """
    if len(sys.argv) != 2: # Let's make sure there's exactly one file to count lines in
        print(f"Usage: python {sys.argv[0]} [filename]")
    else:
        filename = sys.argv[1] # The first (and only) argument is our filename
        try:
            line_count = count_lines(filename) # Now, let's count those lines!
            print(f"Number of lines in file '{filename}': {line_count}")
        except FileNotFoundError:
            print(f"Oops! File '{filename}' not found. Please check the file path.")

# And that's it folks! That's our 'LineCounter'! Hope you liked it!

# Now we just need to call main and our script is ready to go!
if __name__ == "__main__":
    main()
