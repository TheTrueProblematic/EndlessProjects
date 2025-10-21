Python
# Hi there, Pythonista! Welcome to WordLengthHistogram.
# Your friendly neighbourhood code that helps you display histograms of word lengths in a text.
# Isn't that fun!

# Alrighty, let's roll up our sleeves and dive right in!

# First things first, let's import Counter from collections.
# Counter is a nifty little fellow that will help us count the occurrences of word lengths in our text.
from collections import Counter

def word_length_histogram(text):
    # Okeydokey, let's chop chop our words into a list.
    # We're using a list comprehension here because, well, they are pretty awesome!
    words = [word for word in text.split()]

    # Now, let's get the length of each word. Once again we'll use list comprehension because it rocks!
    word_lengths = [len(word) for word in words]

    # Great! Now we get to the heart of the matter. Let's count the occurrences of each word length.
    # We'll use our buddy, Counter, we talked about earlier. Isn't it handy?
    word_length_counts = Counter(word_lengths)

    # Okie dokie, let's get those word length counts in a nice sorted order.
    # Nothing like neatly sorted data to make a programmer's heart smile!
    word_length_counts_sorted = sorted(word_length_counts.items())

    # Bet you've been waiting for the histogram bit! Let's do it!
    # For every word length and its count let's print the word length and a bar made up of '#' symbols.
    # The bar's length will represent the count of the word length.
    # Let's be artsy and create a histogram on the console!
    for word_length, count in word_length_counts_sorted:
        print(f'{word_length}: {"#" * count}')

# There you have it, folks! A fun and friendly Python code to create a word length histogram on the console! 
# Feel free to try this out with any text! 

# To run the code, just call the function word_length_histogram with your text as input. Example below:
# word_length_histogram("Hello world, I love Python!")

# Happy coding!

