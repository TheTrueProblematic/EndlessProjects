
# Hello dear programmer! Welcome to DigitsOnlyChecker! 
# This is a simple Python program that checks if a given string contains only digits.

# Our goal is to keep things sleek, simple, and dependency-free.
# Don't worry, this code works globally, even on a brand new computer.
# It won't call any APIs, won't access the internet, won't hassle you with the GUIs,
# and it's single-file! One and done, that's how we like it here.

# Alright, no time like the present, let's get started!

def check_digits(input_string):
    """
    This nifty function checks if a given string contains solely digits.

    Arguments:
        input_string {str} -- the string who's numerical authenticity we're checking.

    Returns:
        bool -- True if the string contains only digits, otherwise False
    """

    #Python's built-in isdigit() method returns True if all characters in a string are digits. 
    #If not, it returns False. Straightforward, isn't it?

    return input_string.isdigit()

if __name__ == '__main__':
    test_string = input("Enter a string to check: ")

    if check_digits(test_string):
        print("Woo-hoo! Your string contains only digits.")
    else:
        print("Oops! Looks like your string contains non-digit characters. Try again!")

# There we have it! Short, sweet, and simple.
# Quite like the digits we're chasing.
# Remember, don't be a stranger, always validate your data, 
# and above all else, keep on coding!
