
# Hello there, fellow code enthusiasts! Welcome to ShuffleList.py!
# This funky little piece of software is designed to shuffle a list of items randomly.
# You know how sometimes in life, everything gets a bit predictable?
# Well, no more! This script will add a bit of spice (or entropy, if you want to get technical) to your life.

# No GUIs, no dependencies, no internet access, pure python and cross-platform compatibility!
# Sounds like a fun project to me. Let's dive in!

# Firstly, we'll need our friend, the random library. Don't worry, it comes standard with all python installations.
import random

# Now, let's create a function to do the heavy lifting of shuffling our list.
def shuffle_list(input_list):
    """
    This function shuffles a list of items.
    Input: List
    Output: Shuffled list
    """
    # random.shuffle is super cool, it does all the work for us.
    # It's like a party organizer for your list elements. No wallflowers at this event!
    random.shuffle(input_list)

    # Once the party's over, everyone's in a different order!
    # Let's return the list and see what happened.
    return input_list

# And that's it! Life's a party with Python and its in-built libraries.
# To shuffle a list of your own, just use the shuffle_list function on any list and voila!
# Happy shuffling, everyone!
