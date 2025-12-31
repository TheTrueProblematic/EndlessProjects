
# Hey, fellow Pythonistas! Today, we're going to have a little fun on the command line.
# Our mission: create a Python script to parse command-line arguments.
# Let's get started!

# First and foremost, we're going to need the argparse module.
# Don't worry! It comes with Python. No downloading required.
import argparse

# Let's dive into our main function.
# We're going to create an ArgumentParser object and give it a description.
# The description is a mini 'docstring' for the command-line user. Fun, right?
def main():
    parser = argparse.ArgumentParser(description='Demo on command-line argument parsing for options.')

    # Now for the fun part! Let's add some arguments.
    # For the purpose of this demo,  we will add a simple argument "option".
    # Using "--" before the argument makes it optional. Super handy!
    # And 'default' gives it a...well, default value. 
    parser.add_argument('--option', type=str, help='An optional command-line argument', default='Default Value')

    # Now that we have our arguments, we need to catch them in the act of being input.
    # That's where parse_args() enters the scene.
    args = parser.parse_args()

    # As promised, no GUI. But we need to see what we're working with.
    # So, let's print our argument(s) to our dear friend, the command prompt.
    print(f'Option value: {args.option}')

# We only want to run the function when this script is run directly, right?
# That's why we're doing this.
if __name__ == "__main__":
    main()

# And there you have it—a command-line argument parsing demo in Python.
# Go forth and write command-line interfaces with aplomb!
# Remember: argparse is your friend, and the command-line is your playground. 
# Enjoy playing!

