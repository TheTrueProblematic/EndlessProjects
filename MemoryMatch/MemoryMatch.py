
# Welcome to the MemoryMatch game! This fun CLI-based game is your basic card-matching memory game using ASCII cards.
# Get your memory muscles ready, it's time to have some fun!

import random

# No matter the odds, let's always try to have fun. I remember playing this as a child, hope this takes you back too :)

# Create a list with pair of numbers for our memory match game
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '1', '2', '3', '4', '5', '6', '7', '8']
random.shuffle(Numbers)

# This will hold the current state of the game
matches_info = [-1]*16

def print_board():
    # This function will print out the current board state 
    # The excitement is real! Will you guess the right pair?
    print("Here's the current state of the board:")
    for index, number in enumerate(matches_info):
        if number == -1:
            print("__", end = ' ')
        else:
            print(Numbers[index], end = ' ')
        if (index + 1) % 4 == 0:
            print()

def get_player_choice():
    # Oh oh! It's decision time. Choose wisely!
    print("Which card number will you flip?")
    card_number = int(input()) - 1
    while card_number < 0 or card_number > 15 or matches_info[card_number] != -1:
        print("Invalid card number, choose again:")
        card_number = int(input()) - 1
    return card_number

def play_turn():
    # Here we go. Let's play!
    card_number_1 = get_player_choice()
    matches_info[card_number_1] = Numbers[card_number_1]
    print_board()

    card_number_2 = get_player_choice()
    matches_info[card_number_2] = Numbers[card_number_2]
    print_board()

    if Numbers[card_number_1] != Numbers[card_number_2]:
        # Aww! Better luck next time.
        print("No match. Try again")
        matches_info[card_number_1] = -1
        matches_info[card_number_2] = -1
    else:
        # Whoop Whoop! We have a match!
        print("Match found!")

def game_loop():
    # The endless loop of fun begins here...
    # But remember, all you need is a little patience and a lot of memory ;)
    while True:
        if -1 not in matches_info:
            # Yeah, baby! You've won. Your memory is just splendid!
            print("Congratulations! You've matched all the cards.")
            break
        play_turn()

# Let's start this adventure!
game_loop()

