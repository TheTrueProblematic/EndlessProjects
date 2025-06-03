
# Hello lovely people! I hope you're having a fab day.
# I'm excited to present you with our WordleClone - a five‑letter word guessing game with color‑coded hints via letters.
# This game will sure put your vocabulary and guessing skills to test. Let's dive in, shall we? :)

import random

# A cheerful list of pre-defined five-letter words to pick from.
WORDS = ['apple', 'logic', 'table', 'pizza', 'grape', 'globe', 'sugar', 'write', 'music', 'proud']

# Let's pick a five-letter word randomly from our list.
TARGET_WORD = random.choice(WORDS)

# Let's be fair and give 6 attempts to guess the word.
ATTEMPTS_ALLOWED = 6

# We'll use the underscore '_' to represent a letter that has not been guessed yet.
INITIAL_DISPLAY = ['_' for _ in range(5)]

# Alright, let's dive into the actual game part!

def print_word(word):
    '''This function takes an array of letters
    and nicely prints it out in a row.'''
    print('\nYour word:')
    print(' '.join(word))

def process_guess(guess):
    '''This function compares the guessed word with the TARGET_WORD
    and returns the processed word to display containing correct letter positions, correct letters in wrong position,
    and also letters that were not guessed yet.'''
    # starts by making a clone of INITIAL_DISPLAY
    processed = INITIAL_DISPLAY[:]
    for i in range(len(guess)):
        if guess[i] == TARGET_WORD[i]:
            # Hooray! The letter is in the correct position
            processed[i] = guess[i]
        elif guess[i] in TARGET_WORD:
            # Yay! The letter is correct but not in correct position
            processed[i] = guess[i].upper()
    return processed

print('Let\'s start the WordleClone!\n'
      'You have 6 attempts to guess a five-letter word.\n'
      'If a letter appears in the word and is in the correct position, it will be displayed in lower-case.\n'
      'If a letter appears in the word but not in the correct position, it will be displayed in upper-case.\n'
      'If the letter does not appear in the word, it will not be displayed at all.')
      
for attempt in range(ATTEMPTS_ALLOWED):
    print_word(INITIAL_DISPLAY)
    guess = input('Attempt {}: '.format(attempt + 1))
    INITIAL_DISPLAY = process_guess(guess)
    if guess == TARGET_WORD:
        print("\nWoohoo! You've guessed the word correctly. The word was indeed {}!".format(TARGET_WORD))
        break

if guess != TARGET_WORD:
    print("\nOh no! You've used all your attempts. The word was {}.".format(TARGET_WORD))

# And that's it! I hope you've enjoyed this WordleClone. Until next time, keep guessing! :)

