
# Oh boy! I get to make a Python script! Let's see, this one is going to be
# called DecimalToBaseN.py, it's going to be so much fun!
# Alright, let's get down to business, shall we?

# Just because it's fun, we're going to import the string standard module
import string

# We are going to use string's digits and ascii_letters methods to cover all the possible characters we'll need
digits = string.digits + string.ascii_lowercase

# Now we're going to create the function that will do all the heavy lifting
def decimal_to_base_n(number, base):
    """
    This function will convert a decimal number to a number with a different base,
    because who doesn't like variety, am I right?
    """
    # If the number is 0, well, it's going to stay 0 in whatever base, but let's not tell it that
    if number == 0:
        return '0'

    result = ''

    # While the number is not 0
    while number:
        # We get the remainder of the division of the number by the base
        number, remainder = divmod(number, base)
        # Then we add the corresponding character to our result
        result += digits[remainder]

    # And because we're polite, we will return the result reversed
    return result[::-1]

    
# Now let's add the bit that would allow this to run from the terminal
if __name__ == "__main__":
    """
    This is the part where we listen the user input.
    """
    # Read the number from the command line
    number = input("Enter a decimal number: ")

    # Error check while reading the base
    while True:
        base = input("Enter a base between 2 and 36: ")
        if 2 <= int(base) <= 36:
            break
        print("Invalid base! Base must be between 2 and 36")

    # And then we pass the values to the function and print the result
    print(decimal_to_base_n(int(number), int(base)))

# And that would be it! Not so complicated, right?
# So, that was DecimalToBaseN.py. Thanks for hanging out with me while I wrote this.
# Happy coding!
