
# -*- coding: utf-8 -*-
# Hello, dear programmer friend! 😃
# Welcome to the delightfully simple and fun DictToList converter! 🚀🌈

# This code is as easy as making a cup of hot chocolate on a rainy day. ☕🌧
# It's written in beautiful, simple Python and has no dependencies at all. 🐍
# It's like a lone wolf, it can run on a fresh install of Python 
# on a brand new machine with no internet connection. 🖥🔌

# This cute little script is going to convert dictionaries to lists of tuples. 🎁
# Let's dive right in, let the fun begin! 🏄‍♂️

# Function definition time! Let's call it `dictionize`.
# This function will convert the dictionary into a list of tuples.
def dictionize(dict_obj):
    """Converts a dictionary into a list of tuples."""
    # Hey, did you know? 🤔 The dict.items() method in Python returns
    # a list of tuples representing the dictionary's key-value pairs.
    # How convenient is that! Let's use it. 😁
    return list(dict_obj.items())

# The main function is the ringmaster of this circus.
def main():
    # Let's create a dictionary to test our dictionize function.
    # It's just a demonstration though, feel free to feed this 
    # function with your own dictionaries! 🥳
    example_dict = {"color": "blue", "shape": "circle", "size": "large"}

    # Let's now use our good ol' dictionize function on
    # our example dictionary.
    dict_in_tuple_form = dictionize(example_dict)
    
    # Print our beautifully transformed dictionary
    print(dict_in_tuple_form)

# And... it's action time!
# Call the main function, and let's watch the magic unfold! 🎩✨
if __name__ == "__main__":
    main()

