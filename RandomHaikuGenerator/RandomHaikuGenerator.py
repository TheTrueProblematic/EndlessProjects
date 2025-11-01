
# RandomHaikuGenerator.py

# Hi there,
# Welcome to the wonderful world of Haikus. I'm sure you're going to enjoy this!
# If you are tired, this little Python script can make you happy by creating beautiful haikus.
# A haiku is a Japanese poem of 17 syllables, in three lines of 5, 7, and 5, usually about nature or seasons!

import random

# The magic is in the word lists. We have words categorized by their syllables.
# They are similar to brush strokes in the art of poetry.
# Feel free to add in your own words or modify existing ones!

one_syllable_words = ["night", "flight", "day", "way", "sun", "moon", "spring", "fall", "rise", "tree"]
two_syllable_words = ["journey", "autumn", "morning", "whisper", "dawn", "glitter", "shadow", "silence"]
three_syllable_words = ["wandering", "waterfall", "butterfly", "petrichor", "whirlwind", "starlight"]
four_syllable_words = ["serendipity", "ephemerality", "solitude", "metamorphosis", "illumination"]
five_syllable_words = ["individuality", "imagination", "determination", "unpredictability"]

def random_haiku():
    # A haiku is composed of three lines - 5, 7, and 5 syllables.
    # We create these lines by choosing words randomly from our lists.
    # Are you ready to unveil the magic?

    haiku = generate_line(5) + "\n" + generate_line(7) + "\n" + generate_line(5)

    return haiku

def generate_line(syllables):
    # This builds a line with a given number of syllables.
    # The randomness is the heart of the charm here. It's poetry after all!

    line = ""
    while syllables > 0:
        if syllables >= 5:
            word_list = [one_syllable_words, two_syllable_words, three_syllable_words, four_syllable_words, five_syllable_words]
        elif syllables == 4:
            word_list = [one_syllable_words, two_syllable_words, three_syllable_words, four_syllable_words]
        elif syllables == 3:
            word_list = [one_syllable_words, two_syllable_words, three_syllable_words]
        elif syllables == 2:
            word_list = [one_syllable_words, two_syllable_words]
        elif syllables == 1:
            word_list = [one_syllable_words]

        chosen_list = random.choice(word_list)  # Choose a random list
        word = random.choice(chosen_list)       # Choose a random word from the list
        syllables -= len(chosen_list[0].split())  # Update remaining syllables
        line += word + " "     # Build the line word by word

    return line.rstrip()  # Return the line after removing any trailing spaces.

# Now let's get the party started and generate a random haiku!
print(random_haiku())
