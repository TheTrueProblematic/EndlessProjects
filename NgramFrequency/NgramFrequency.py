
# Hello there! This is an exciting Python script called NgramFrequency. Its primary function is to compute the frequency of n-grams in a given text file. Nothing more, nothing less.
# Can't use anything other than python?! No problem! We show python plenty of love

# Now let's start. Import the necessary packages

import re
import sys
from collections import defaultdict

# In order to read the command line arguments that are passed to the python script, we need to use the sys module.
# We will use the first argument as the text file name and the second one as the number of sizers of the n-gram (n)

text_file = sys.argv[1]
n = int(sys.argv[2])

# We need an empty dictionary. But what kind of dictionary are you asking? A defaultdict (which is a subclass of dict)? In Python? Yes, in Python! It's a neat trick for counting the frequencies of n-grams!

ngram_freq = defaultdict(int)

# Let's comb through that text file. Beautifully open it, read each line, split words, handle punctuation...

with open(text_file, 'r') as file:
    for line in file:
        # Split the line into words. This function is basic, for example it will carve "you're" into "you" and "re"
        words = re.findall(r'\b\w+\b', line)
        # Now we have the words, let's find the n-grams.
        for i in range(len(words) - n + 1):
            # An n-gram is just a fancy slice on the list of words from i to i+n
            ngram = ' '.join(words[i : i + n])
            # Each time we see an n-gram, increase its frequency by 1
            ngram_freq[ngram] += 1

# There we go, all the file reading and n-gram frequency counting happened above!

# Let's print those most frequent n-grams, shall we?

for ngram, freq in ngram_freq.items():
    print(f'{ngram}: {freq}')

# So, there you have it folks, a small yet mighty Python script that calculates the frequency of n-grams in a text file.
# Ngrams are pretty important in the world of Natural Language Processing (NLP).

# Well, that’s all folks, enjoy your NgramFrequency!

