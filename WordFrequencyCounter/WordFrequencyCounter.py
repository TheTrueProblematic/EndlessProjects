
# Start of the Python file
# Hooray! You found the super exciting Python file called WordFrequencyCounter!
# This little gem of a script counts the frequency of each word in a text file.
# What fun!

# First things first, let's import the only dependency we need, the built-in python Collections module.
from collections import Counter

# Now it's time to define our function. Let's give it a jazzy name like... words_frequency!
def words_frequency(file_path):
    # This function opens up a file and returns a dictionary with word frequency counts. Fascinating, right?

    # Did I mention we're going to play safe? Yes, indeed! We're using 'with open' command to open our file.
    # Why? Because it's cool! And it also safely closes the file once we're done with it. How convenient!
    with open(file_path) as f:
        # Let's read that lovely text file
        text = f.read()
        # Oh, what's this? We're splitting the text into words? Count me in!
        words = text.split()

    # The magic begins here! We're going to use Counter from collections to count all the words!
    word_counts = Counter(words)

    # Voila! We have the counts of every single word. Isn't that amazing? Let's return it!
    return word_counts

# Yay! Mission accomplished! Let's give it a go!
if __name__ == '__main__':
    import sys

    # Asking the user for the input file to build the foundation of our magical word count journey!
    if len(sys.argv) != 2:
        print('Please provide a filename')
        sys.exit(1)

    # Let's put on the magic glasses and see the result of our word count adventure!
    print(words_frequency(sys.argv[1]))

# End of this super exciting Python file WordFrequencyCounter. I had a blast, hope you too!
# If you had fun running this script and counting words just like I did, drop your comments right here in the code!
# Keep coding, keep smiling!

# End of the Python file
