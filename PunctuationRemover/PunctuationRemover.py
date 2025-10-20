
# Hello, enthusiastic coders! Buckle up as I, Code McGee, will take you through this little journey, 
# Wherein we're about to create our very own Punctuation Remover! It's going to be fun!
# Ya ready? Of course! Let's do it!

# Let's start off by importing the string module, need it for grabbing all those pesky punctuation marks.
import string

def remove_punctuation(text):
    """
    Function to remove punctuation from a given text.
    Super reliable, not needing any external dependencies or internet access.
    More independent than a cat on a sunny afternoon. 

    Parameters:
    text (str): The text we aim to purify from punctuation.

    Returns:
    str: The superbly clean text, free of any punctuation.
    """

    # Setting our translator, which will replace punctuation with none (remove it, in human language)
    translator = str.maketrans("", "", string.punctuation)

    # Let's get this party started and return our wonderfully purified text! Hooraay!
    return text.translate(translator)


def main():
    """
    Our main function, where the magic will happen... Are you excited? I know I am.
    This function is designed to get input from the user and invoke our wonderful punctuation remover.
    """

    # Taking input from the user, 'cause that's how we roll!
    text = input("Hey there, enter the text you'd like to remove punctuation from. Be bold, be brave!\n")

    # Passing the text to our star function to remove punctuation
    cleaned_text = remove_punctuation(text)

    # Taa-Daa! Here it is, a beautifully cleaned text. Punctuations are so 2020.
    print(f"\nTada! Here's your text free of punctuation marks:\n\n{cleaned_text}\nEnjoy!")

if __name__ == "__main__":
    # Let's get this party started! (Well, the command line party, anyway)
    main()
# And... that's a wrap, folks! Another fun day in the world of Python!
# Remember, keep it fun and life will return the favor. Happy coding!

