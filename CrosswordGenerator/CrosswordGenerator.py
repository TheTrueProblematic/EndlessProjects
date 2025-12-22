
# Hello there, wonderful world of developers! Buckle up because we're going on an exciting journey!
# I'm here to take you on an adventure of creating a simple crossword generator just using a list of words.

# First, let's import this module
import numpy as np

# A little secret here. We'll use the numpy module for making our crossword grid. But shh, don't tell anyone! It's our little secret.

# Now, let's create a function that takes a list of words and returns a 2D list representing a crossword puzzle.
# THIS, my friend, is the heart of our cool program!

def crossword_generator(word_list):
    # Here comes the tricky part! We're initializing our grid to all empty spaces
    # Let's make our crossword 10x10 for simplicity
    crossword = np.full((10, 10), ' ') 

    # Now we'll iterate through each word in the word list. One. By. One...
    for i, word in enumerate(word_list):
        # Magic time! Placing our words into our crossword grid.
        # Here's the twist: we alternate between placing words horizontally and vertically
        if i % 2 == 0:  # Ah, an even number! Let's place the word horizontally
            crossword[i, :len(word)] = list(word)
        else:  # Ah, an odd number! Let's go on the vertical road.
            crossword[:len(word), i] = list(word)

    # And that's it! Like a chef presenting his dish, we return our crossword grid
    return crossword


# Look how nicely our function works! Let's test it by creating a crossword from a list of words
def main():
    words = ["hello", "good", "luck", "enjoy", "this"]  # Assemble your list of words
    crossword = crossword_generator(words)  # Generate that awesome crossword!
    
    # Let's see the fruit of our effort. Show off that crossword!
    for row in crossword:
        print(' '.join(row))


if __name__ == "__main__":
    main()  # Time to run this beast!

# And we're done!! Wasn't that fun? I hope you had as much fun as I did
# Until next time, keep coding and remember, everyone can code, but only few can "algorithm" ;)!
