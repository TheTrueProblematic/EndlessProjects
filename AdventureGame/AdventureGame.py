
# Welcome to "Adventure Game"! This is an imaginary world born just from text.
# Let's jump into a fun text-based adventure game, which is purely powered by Python.
# Every line of code in this game is a step towards adventure, let's go!

# Importing system specific parameters and functions
import sys

def adventure_game():
    # Here's an intro of the game.
    print("Welcome to Adventure Game! 🏞️")
    print("Are you excited? Let's start the journey!")

    # Let's customize our adventurer.
    player_name = input("First things first, what should our hero be called? ")
    print(f"Welcome {player_name}! Best of luck for your adventure!")

    # Time for the first big decision!
    path = input("You are on a crossroad, where do you want to go? Left or Right? ")
    if path.lower() == "left":
        # You took the left path!
        left_path()
    elif path.lower() == "right":
        # You took the right path!
        right_path()
    else:
        print("Invalid option, Game Over! 👾")

def left_path():
    # Player decided to go left.
    print("You are walking into a mysterious forest 🌳, and suddenly you have encountered a scary monster! 😈 ")

    decision = input("Fight or Run? "
    if decision.lower() == 'fight':
        print("You decided to fight the monster! 🤺 You have won! Cheers 🎉  ")
    elif decision.lower() == 'run':
        print("You decided to run away like a hero knowing when to retreat!  🏃")
    else:
        print("Invalid option, Game Over! 👾 ")

def right_path():
    # Player decided to go right.
    print("You are climbing up a high mountain 🏔️, and suddenly there is a snow avalanche!")

    decision = input("Climb faster or Hide? ")
    if decision.lower() == 'climb faster':
        print("You decided to climb faster! 🏃‍♀️ Finally, you have reached to the top! Cheers 🎉  ")
    elif decision.lower() == 'hide':
        print("You decided to hide behind a big rock! You're safe now 🥳 ")
    else:
        print("Invalid option, Game Over! 👾 ")

if __name__ == "__main__":
    # We're starting the game now, seatbelts on!
    adventure_game()

