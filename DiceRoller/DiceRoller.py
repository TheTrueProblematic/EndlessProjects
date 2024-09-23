
# Greetings fellow programmer! We're about to embark on a FUNtasitc journey, to a land where dice roll and the outcomes are unpredictable!

# For this adventure, we're going to make full use of python's standard library
import random

# Ah, the magic of dice rolling. Quite a simple act, isn't it? But the results...ahh, they can change fates! Don't believe me? Ask a DnD player!
def roll_dice(num_dice=1, num_sides=6):
    """Roll a specified number of dice, and return their total."""
    # We'll use a cool python trick called a list comprehension to roll all our dice in one go!
    # With each roll, we generate a random number between 1 (inclusive) and the number of sides on the dice (also inclusive).
    dice_results = [random.randint(1, num_sides) for _ in range(num_dice)]
    # Now let's add up all our rolls for the grand total!
    total = sum(dice_results)
    # And there you have it! The mighty total of your dice rolls!
    return total, dice_results
  
def main():
    """The main function to run our dice roller program."""
    # Roll the dice!
    # For now, we'll just do a single roll of a standard 6-sided dice.
    total, dice_results = roll_dice()
    # Time to reveal the results of your dice roll. Drumroll please...
    print('You rolled the following: ', dice_results)
    print('For a grand total of: ', total)

# Ah, the grand finale! This bit checks to see if our script is being run as a main file (rather than being imported by another script),
# and if so, it sets off our grand Dice Roller Adventure!
if __name__ == "__main__":
    main()
# Thanks for coming along on this coding journey with me! It's been a blast, hasn't it? Here's to many more!

