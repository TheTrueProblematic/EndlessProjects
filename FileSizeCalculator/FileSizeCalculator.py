
# Hello Pythonistas! Here's a nifty program that will help you calculate the total size of a directory. 
# It's a handy-dandy tool that is easy to use and fun to play with! Let's get started!

# First off, we need to import the os module because we'll be dealing with system pathnames
import os

# This mighty function right here is  our hero. It takes in a directory, 
# and then calculates the total size of all the files in that directory.
def calculate_directory_size(directory):
    # Initialize the total size to 0.
    total_size = 0

    # os.walk() generates filenames in a directory tree by walking the tree
    # It's like a woodcutter making his way through a forest, no tree (or file) shall be left unchopped!
    for dirpath, dirnames, filenames in os.walk(directory):
        # Here we go through each file in the directory
        for f in filenames:
            # os.path.join() function: let's make sure we don't get lost in the woods by bringing a map (file pah)
            fp = os.path.join(dirpath, f)
            # We'll check if the file path is symbolic link (because we're not counting those)
            # If it isn't, we add its size to our total
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    # Yahoo! We survived the forest trail. Let's go home and tell everyone how big the forest was!
    return total_size

# Oops! Almost forgot, this is the magical incantation you recite to start your adventure in the forest!
def main(directory):
    # And... there it is! That's how big the forest (ahem, I mean directory) is!
    print(f'Total size of directory "{directory}" is {calculate_directory_size(directory)} bytes')

# Woohoo! Ready to go?
# Just tell our hero which forest (directory) to venture into, by providing the path when you run the script 
# like: python FileSizeCalculator.py /path/to/forest
# And enjoy the adventure!
if __name__ == "__main__":
    import sys
    # Check if the directory path is provided.
    if len(sys.argv) < 2:
        print("Directory path is not provided.")
        sys.exit(1)
    # Now really start the adventure!
    main(sys.argv[1])

