
# Hey there happy coder! This file is none other than our beloved number guessing game Bulls and Cows.
# Yep, the classic game where you've got to guess the secret number with some friendly bulls and cows guiding you along.
# Fear not, the rules are so simple that even a capybara could play! (if it had fingers and knew how to code, that is.)
# Bulls are digits in the correct location, while Cows are digits that exist in the secret number but not in the right place.

import random

def generate_secret_number():
    """
    Generates a random 4-digit "secret" number with no duplicate digits
    Isn't that neat?
    """
    digits = list("0123456789")
    secret_number = []
    for _ in range(4):  # We're looking for a 4-digit secret number
        digit = random.choice(digits)  # Pick a "random" digit
        secret_number.append(digit)  # Add it to our secret number
        digits.remove(digit)  # We don't want duplicates - let's remove that digit
    return secret_number

def get_bulls_and_cows(secret_number, guess):
    """
    Function to return the number of bulls and cows for a given guess
    Bulls for digits in the correct place
    And Cows for digits somewhere else in the secret number
    """
    bulls = sum([s == g for s, g in zip(secret_number, guess)])  #way to go!
    cows = sum([g in secret_number for g in guess]) - bulls  # Don't worry, we've got you covered!
    return bulls, cows

def play_bulls_and_cows():
    """
    Main game logic lives here!
    Generates the secret number, takes user input, and grants us some fun interaction!
    """
    secret_number = generate_secret_number()  # Shhh, it's a secret!
    guess_count = 0

    while True:  # We'll keep going until you win, or you decide to give up and sip a Pina Colada!
        guess = list(input("\nWhisper your 4-digit guess: "))  # String of guesses to list (for zip function)
        if len(guess) != 4 or not all(d.isdigit() for d in guess):
            print("Not quite right. Make sure your guess is a 4-digit number!")  # Gotta keep it 4 digits!
            continue  # That wasn't a valid guess, so it doesn't count
        guess_count += 1  # That's a valid guess!
        bulls, cows = get_bulls_and_cows(secret_number, guess)
        
        if bulls == 4:  # 4 bulls means you've won the game!
            print(f"Hooray! You've guessed the secret number in {guess_count} attempts!")
            break  # You've won, thus the game ends.

        print(f"{bulls} Bull(s), {cows} Cow(s)")  # That's some friendly feedback for ya!

# Let's initialize this exciting game!
if __name__ == "__main__":
    play_bulls_and_cows()  # Off we go on an adventure!
