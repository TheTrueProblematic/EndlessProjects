
# RockPaperScissors.py
# Woohoo! Welcome to the coolest command-line version of Rock-Paper-Scissors!
# You'll be pitting your wits against the formidable computer - an epic battle is just moments away!

import random

# Here's where we define our options
OPTIONS = ['Rock', 'Paper', 'Scissors']

# Don't worry, fellow human, we're not revealing our radiant AI's choice just yet!
def get_computer_choice():
    # Something random, something cool. Let's get rockin'!
    return random.choice(OPTIONS)

def get_player_choice():
    # What's it gonna be, champ? Rock? Paper? Scissors? Can't wait!
    choice = ''
    while choice not in OPTIONS:
        print("\nPlease enter your choice (Rock, Paper, or Scissors):")
        choice = input().title()
    return choice

def determine_winner(player, computer):
    # It's judgement time! Will it be the unstoppable human or the unflappable AI? Let's see!
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or (player == 'Scissors' and computer == 'Paper') or (player == 'Paper' and computer == 'Rock'):
        return "You win! Well played, my friend!"
    else:
        return "Computer wins! Well, you can't win them all, can you?"

def play_game():
    # This is it - game time! The excitement is palpable.
    print("\n\n--- Welcome to Rock-Paper-Scissors! ---")
    player = get_player_choice()
    computer = get_computer_choice()

    # The suspense ends here. Let's announce the choices.
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    # The finale - who gets the glory? Let's find out!
    print(determine_winner(player, computer))

# Back to the main event! 
if __name__ == '__main__':
    while True:
        play_game()

        # Once isn't enough, is it? Let's play again!
        print("\nDo you want to play again? (yes/no)")
        play_again = input().lower()
        if play_again != 'yes':
            break
    print("\n--- Thank you for playing! Looking forward to the rematch. ---")   

