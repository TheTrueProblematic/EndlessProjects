
# Hey there! Get ready for an exciting game of Hangman!
# This here is a command-line game, so no fancy GUI is needed.
# This is a fun word-guessing game that will keep you on the edge of your seat!
# Guess the word by suggesting letters within a certain number of turns.
# No dependencies, no API, no internet access, pure Python - let's dive into the action!

import random

# Let's get a pool of words for the Hangman game
WORDS = [
    'python', 'java', 'ruby', 'javascript',
    'csharp', 'golang', 'rust', 'kotlin',
    'swift', 'typescript', 'pearl', 'fortran'
]

def get_word():
    # Randomly select a word from the pool
    return random.choice(WORDS)

def play_hangman():
    # It's game time, folks!
    word = get_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    # We give the user 6 lives (head, body, 2x arms, 2x legs)
    lives = 6

    # Greeting our player!
    print('Let\'s play Hangman!')

    # Game loop starts here
    while len(word_letters) > 0 and lives > 0:
        print('You have used these letters: ', ' '.join(used_letters))
        
        # Show user what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

        elif user_letter in used_letters:
            print('You have already used that letter. Try again.')

        else:
            print('Invalid character. Please try again.')
            lives = lives - 1

    # Game ends here
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__ == '__main__':
    play_hangman()
# That's the end folks! We hope you enjoyed it.
# This one-file script of Hangman was brought to you by a happy Python programmer.
# Have more fun and keep playing!
