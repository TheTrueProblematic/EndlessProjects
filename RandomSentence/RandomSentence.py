
# Hello, fellow Pythonista! Welcome to an adventure! 
# Isn't it cool we're about to create a program to make random sentences? Simulating human language? That's wild!

# As we start, let's keep in mind that great power comes great randomness! 

import random

# Oh look, arrays, our good ol' friend! 
# These are the building blocks of our sentences. Feel free to get creative and change them up!

subjects = ["I", "You", "Bob", "Alice", "The cat", "The robot"]
verbs = ["ate", "kicked", "saw", "liked", "ran from", "was"]
objects = ["an apple", "the ball", "a ghost", "the novel", "a line of code", "its shadow"]

# Now for the fun part! Let's make some grammar magic.
# This function grabs a random element from each list and smashes them together to create a sentence!

def generate_sentence():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    object = random.choice(objects)
    
    # Concatenating our string to form a sentence. It's like playing word Lego!
    sentence = subject + " " + verb + " " + object + "."
    return sentence

# Let's bring our creation to life! The Frankenstein of sentences, if you will. 
# Every time you run this, it's a wonderful surprise what it will say.

if __name__ == "__main__":
    sentence = generate_sentence()
    print(sentence)

# And that's it! A random sentence generator, ready to surprise and amaze. 
# Isn't Python awesome? 
# See you on the next coding adventure, my friend!
