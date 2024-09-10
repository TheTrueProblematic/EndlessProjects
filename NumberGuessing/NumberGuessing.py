
# Hey there, awesome programmer! 😁
# Welcome to the NumberGuessing python script!
# This jolly piece of code sets up a fun number guessing game right at your command line interface.
# No fancy GUIs, no pesky dependencies, no internet or API stuff. Just pure python fun! 🐍
# This means you can run this script on a brand spanking new computer with a fresh python install.
# How cool is that?! 😎

# Importing the necessary python module.
import random

# Let's get our game started! 🚀
def start_game():
    # First things first, we generate a random number between 1 and 100.
    random_number = random.randint(1, 100)

    # Now we initialize the guesses_taken variable to keep track of the number of guesses the user takes.
    guesses_taken = 0

    # Let's dive right into the main loop of the game.
    while True:
        # Taking user input for their guess.
        user_guess = input("\nGuess a number between 1 and 100: ")

        # Adding a try block here to ensure that the user enters a valid number.
        try:
            # Let's convert the input to an integer.
            user_guess = int(user_guess)
        except ValueError:
            # In case the user does not input a valid integer, we let them know and continue the loop.
            print("Whoops! That's not a valid number. Try again!")
            continue

        # Every valid guess counts, so we increment our guesses_taken variable.
        guesses_taken += 1

        # Now let's check if the guess is correct, too high, or too low.
        if user_guess == random_number:
            # User has guessed the secret number! Let's break the good news! 🎉
            print(f"Congratulations! You've cracked the code in {guesses_taken} guesses!")
            break
        elif user_guess < random_number:
            # User's guess is too low. We let them know.
            print("Too low! Aim higher!")
        else:
            # User's guess is too high. We give a hint.
            print("Too high! Go lower!")

# Let's call our start_game function to activate the fun!
start_game()

