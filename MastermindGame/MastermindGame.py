
# Hey there, Happy Python Programmer! 
# This is a fun 'Mastermind' code-breaking game that runs completely on the command line.
# We are using letters instead of colored pegs.
# Buckle in and let's get started!

import random

# Let's define our colors (which are actually letters)
colors = ['A', 'B', 'C', 'D', 'E', 'F']

# Our code will be a random list of 4 colors
code = [random.choice(colors) for _ in range(4)]

def print_instructions():
    # A casual greeting to the player, with the rules of the game
    print("""
        Hey there, Mastermind!
        Ready for a code-breaking challenge? Here are the rules:
        1. The code is a sequence of 4 colors (which are actually letters). 
        2. Colors could be: A, B, C, D, E or F
        3. After every guess, you will get feedback in the form of stars (*), representing correct colors in right places,
         and pluses (+), representing correct colors in wrong positions.
        4. You have 10 attempts to break the code. 
        Let's Play!
    """)

# Let's define our guess function
def guess():
    # A happy little reminder: This function is where all the action happens
    # Get an input, check it against the code, and give feedback

    guess = input('Enter your guess (4 colors): ').strip().upper()
    feedback = []

    for i in range(4):
        if guess[i] == code[i]:
            feedback.append('*')
        elif guess[i] in code:
            feedback.append('+')
            
    random.shuffle(feedback)
    print(''.join(feedback))
    return guess

# We're gonna need a game loop!
def game_loop():
    # A key part of the game, happy little loop that keeps the game going 
    for i in range(10): 
        g = guess()
        if g == code:
            print('Congrats! You are a true Mastermind!')
            return
    print('Game Over. Better luck next time! The code was: ' + ' '.join(code))

# And finally, let's tie it all together
def main():
    print_instructions()
    game_loop()

# An exciting message to remind you of the magic happening here
# This is where the spark of life enters our code!
if __name__ == "__main__":
    main()
