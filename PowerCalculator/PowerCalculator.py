# Welcome to the PowerCalculator script!
# This script is a fun and simple way to calculate the power of a number without using python's built-in pow() function.
# We'll only be using pure Python, no external dependencies, so it's fresh and clean as a daisy on a new computer!
# No need for internet or API access, this script is as self-reliant as a husky in the wild.
# One trick pony? No way, this script runs on any platform that supports Python.
# So let's jump into the world of powers, and no, we're not talking superpowers... or are we?!

#######################################

def calculate_power(base: int, exponent: int) -> int:
    """Calculate the power of a number.

    Parameters:
    base (int): The base number
    exponent (int): The exponent number

    Returns:
    int: The result of the power calculation.
    """

    # The initial result value. We start from 1 because 1 multiplied
    # by anything doesn't change the value.
    result = 1

    # Now, let's loop over the exponent range. We start at 0 up to the exponent number.
    for _ in range(exponent):

        # For each iteration, we'll multiply the result by the base number.
        # This is the core logic of our power calculation.
        result *= base

    # And voila! Our power calculation is done. Let's return the result back.
    return result
  
# Let's test this out, shall we? Prepare to be amazed!
if __name__ == "__main__":
    base = 2
    exponent = 3
    result = calculate_power(base, exponent)
    print(f"The power of {base} to the exponent {exponent} is: {result}")
    # Outputs: The power of 2 to the exponent 3 is: 8
   
# And that's it folks! We've built a powerful (get it?) script without using the pow() function.
# So flex your programming muscles and calculate your powers away!