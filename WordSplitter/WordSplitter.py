
# Hi There! This is 'WordSplitter'! 
# True to my name, I love splitting compound words into simpler ones!
# Remember, I'm a happy helper, and I don't need the internet, APIs or any dependencies to work. 
# Just pure, crispy clean Python! 

# Importing these standard Python packages to be our helping hands!
import sys
import re

def split_word(word):
    """A cheerful method to decompose a compound word into simpler individual words!"""
    # Using regular expressions to find all individual words in the compound word
    # We're searching for all alphabets between a-z and A-Z, bundled together in a word.
    return re.findall('[a-zA-Z][^A-Z]*', word)

def main():
    """The main function that gets, splits, and then returns individual words from the compound word"""
    # First, let's make sure we have a word as the command-line argument
    if len(sys.argv) != 2:
        print("Whoops! I need exactly one compound word to split!")
        return

    word = sys.argv[1]
    words = split_word(word)

    # Print the words separated by a single space. Just the way it should be! 
    print(' '.join(words))

# Ah! The heart of the script where everything kicks off!
if __name__ == "__main__":
    main()
    
# And voila! All beaming and cheerful, ready to split some words!
# Feel free to run me on any platform and I promise, we'll have a good time!


