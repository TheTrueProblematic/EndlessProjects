
# Hi there, happy programmer! 🥳
# Welcome to my Python script called TextFileMerger. 🐍
# This little piece of code will help you to get the content of two text files, 
# and create a new one with all the information. Isn't that cool?

# Let's begin our wonderful and exciting journey through the world of Python! 🚀

# First of all, we are going to need the sys module to handle command-line arguments
import sys

# Now, we're going to define a function to do all the magic! 🎩✨
def merge_files(file1, file2, output):
    """Merge two text files into one.
    
    Params:
    file1: First input file to read from.
    file2: Second input file to read from.
    output: Output file to write the merged content.

    """
    # Let's open the first file now and read from it
    with open(file1, 'r') as f1:
        content1 = f1.read()
    # Done! Phew, that was not so hard, was it? 😄

    # Now, let's open and read the second file.
    with open(file2, 'r') as f2:
        content2 = f2.read()
    # All the reading is done, good job so far! 👏

    # Now, let's create that output file and write all the scraped content to it.
    with open(output, 'w') as out:
        out.write(content1 + "\n" + content2)
    # And, BOOM! 💥 We're done merging files! Yay! 🎉

# Now that we have our function, let's use it!
# We're gonna make sure that the script is being run directly (not being imported)
if __name__ == '__main__':
    # Check if the number of command line arguments is correct.
    if len(sys.argv) != 4:
        print("Usage: TextFileMerger.py <Input File 1> <Input File 2> <Output File>")
        sys.exit(1)
    
    # Unpack command line arguments
    _, input_file_1, input_file_2, output_file = sys.argv

    # Call our function with the input and output file paths.
    merge_files(input_file_1, input_file_2, output_file)
    # And there you have it, sweet success! 🎉🍰
    # Be proud, because we've just created a program using nothing but our mighty Python powers! 💪😎

# Thank you for joining me on this adventure. Until next time!
# Signing out, your faithful Python script. 🐍💖

