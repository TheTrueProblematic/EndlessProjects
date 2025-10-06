
# Hello! This is your friendly neighbourhood Python script, LineSorter!
# This script's superpower is - *drumroll* - sorting lines in text files alphabetically!
# Exciting, eh? Let's get started!

# Remember, we're keeping things simple. No GUI, no dependencies, no API, just good old Python.

def sort_file_lines(input_filename, output_filename):
    # First, we'll open the text file that needs sorting.
    # We'll be treating it 'read-only' (the 'r' mode), as we won't be messing directly with it.
    with open(input_filename, 'r') as inputFile:
        lines = inputFile.readlines() # Let's read all lines in the text file

    # Now, let's exercise our sorting superpower!
    # Python's built-in sorted function will do the job nicely.
    sortedLines = sorted(lines)

    # Finally, let's write the sorted list of lines to a new file.
    # This time we're opening the file in 'write' mode ('w'), so be careful and make sure the file name is correct!
    with open(output_filename, 'w') as outputFile:
        outputFile.writelines(sortedLines) # Write each line to our file

    # And... we're done! See how easy that was?
    # The lines in the file should now be perfectly sorted, syllable by syllable.
    # If they're not, then you must have stumbled upon a bug... or maybe it's a feature?

# This is an 'executable' script, and the magic happens in the __main__ method
# Right now, the file names are hardcoded, but you can modify them in any way you need.
if __name__ == "__main__":
    sort_file_lines('input.txt', 'output.txt') # Replace with your file names.

# Thank you for flying with LineSorter! 'Til the next sort-fest!
