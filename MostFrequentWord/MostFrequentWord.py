
# Hey there fellow programmer! Welcome to the MostFrequentWord script. :)
# This is a neat little project that takes a text file and finds the most
# frequent word in it. It's like solving a super cool text-based mystery!

# First off, let's import the python stdlib modules we need.
# Only re and sys are required for this adventure! No need for external dependencies.
import re
import sys

def most_frequent_word(file_path):
    """
    This function takes a file path, reads the file,
    and then determines the most frequent word in that file.
    Like a bot detective!

    Args:
        file_path (str): path to the text file.
    """

    # And now, the adventure begins with opening the file.
    with open(file_path, 'r') as file:
        # read and lower-case the file contents
        # because we want our detective bot to treat "Word" and "word" as the same suspect
        data = file.read().lower()
        
    # split words using regex (regular expressions) to account for different word delimiters
    # This is our bot detective's secret language deciphering tool!
    words = re.findall(r'\b\w+\b', data)

    # Get the word frequencies using a dict, like a clever tally chart!
    frequencies = {word: words.count(word) for word in words}

    # find the word with highest frequency. It's like finding the mystery word!
    most_frequent = max(frequencies, key=frequencies.get)

    # return the most frequent word along with its frequency
    # It's the grand reveal of our text mystery!
    return most_frequent, frequencies[most_frequent]

def main():
    """
    The main function takes command line arguments and passes them to 
    the `most_frequent_word` function.
    """
    # We use sys.argv to read command line arguments.
    # sys.argv[0] is the script name itself, so we start from sys.argv[1]
    if len(sys.argv) != 2:
        # we need exactly one argument (the file path)
        print("Usage: python most_frequent_word.py <file_path>")
        return

    # run the detective function on the given file
    file_path = sys.argv[1]
    word, frequency = most_frequent_word(file_path)

    # reveal the most frequent word and its frequency to the user
    print(f"The most frequent word is '{word}', with a frequency of {frequency}.")

# This is the starting point of our script. 
# After defining all our secret tools and methods, we call the main function.
if __name__ == '__main__':
    main()
    
# And there you have it, fellow code wizard! This script will find the most frequently used 
# word in any given text file, all from the mysterious command line. Happy coding! 
