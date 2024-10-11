
# Hey there, Sunny Side Up Programming Club! Let's start coding a fun word scramble game!

import random

# I like to keep my word list to something familiar, here are some words related to sunny breakfast.
word_list = ['pancakes', 'juice', 'eggs', 'sausages', 'cereals', 'waffles', 'toast', 'jams', 'fruits', 'bacon']

# Now, let's mix up those letters! Who doesn't love a good scramble, after all it's not just for eggs.
def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

# Here's the main function for our game. Ready, set, guess!
def main():
    # I usually start my day with a random breakfast, let's do the same with our game word!
    chosen_word = random.choice(word_list)

    # Let's scramble those letters!
    scrambled_word = scramble_word(chosen_word)

    # Alright, let's start the game!
    print("Welcome to Word Scramble, where your breakfast isn't the only thing that's mixed up!\n")
    print(f"Here's your scrambled word: {scrambled_word}")

    # Let's see if they can unscramble our breakfast!
    guess = input("Your guess: ")

    # As long as their guess isn't right, we keep going! The game must go on, after all.
    while guess != chosen_word:
        print("Try again!")
        guess = input("Your guess: ")

    # And they've got it! Round of applause!
    print(f"Well done, you've unscrambled the word! It was indeed {chosen_word}. Have a nice day!")

# And this is how we make it all happen! Go, little script, go!
if __name__ == '__main__':
    main()

