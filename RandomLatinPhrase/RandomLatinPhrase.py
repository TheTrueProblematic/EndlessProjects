
# Hey there, curious explorer! 🎩
# Let's have some fun with Latin phrases today! 🎉
# This script will give you a random Latin phrase whenever you run it.
# Who knows you might end up impressing someone with a Latin phrase!

# No internet, no external libraries, no GUI - just pure Python magic!
# So let's dive into this classical adventure!

import random

# Here are some cool Latin words broken up into three categories: adjectives, nouns, and verbs. Feel free to add more to your taste! 😜
adjectives = ['Magnus', 'Parvus', 'Potens', 'Superus', 'Victor']
nouns = ['Imperium', 'Regnum', 'Gloria', 'Pax', 'Veritas']
verbs = ['Vigilo', 'Pugno', 'Vincere', 'Superare', 'Regnare']

# Now to the fun part! 🎢
# Let's generate a random Latin phrase!
def generate_phrase():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    verb = random.choice(verbs)

    # Et voila! Your Latin phrase is ready! 🎊
    return f'{adjective} {noun} {verb}'

# Now all you have to do is run the script and get a cool Latin phrase.
# Remember, 'Ars longa, vita brevis'.
# Happy learning and keep having fun!

if __name__ == "__main__":
    print(generate_phrase())

