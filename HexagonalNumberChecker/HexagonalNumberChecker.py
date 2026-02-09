
# Woohoo! Let's have some fun with Python!
# Welcome to our happy little Python program: HexagonalNumberChecker
# We are going to make a function to check if a number is hexagonal or not.
# A hexagonal number, for those who are wondering, is a figurate number represented as a hexagon. 
# The nth hexagonal number h(n) is given by the formula: n(2n-1). Fancy, right?

# Let's start by defining our function.

def is_hexagonal(num):
    """
    This function checks if a number is hexagonal or not. 
    It uses a little math magic to figure it out.
    It's like a little math wizard in your computer!
    """
    # The magic here is that for a number to be hexagonal, (1 + sqrt(1 + 8*num)) / 4 must be a whole number (integer).
    # If that's true, then the number is hexagonal. Otherwise, it's just a regular, non-magical number.
    return ((1 + (8 * num + 1) ** 0.5) / 4).is_integer()


# Okay, now we want to use our function from the command line.
# To do that, we're going to use an if __name__ == "__main__": block.
# This is a little bit of Python magic that lets us run code when we run a file from the command line,
# but not when we import it as a module.

if __name__ == "__main__":
    # We're going to use the Python built-in function input() to get a number from the user.
    # input displays a prompt to the user, and then waits for them to type something and hit enter.
    # Whatever they type is returned as a string, so we'll need to convert it to an integer.
    num = int(input("Enter a number: "))

    # Now we can use our magical mathemagician function to check if the number is hexagonal.
    if is_hexagonal(num):
        print(f"Hooray! {num} is a hexagonal number!")
    else:
        print(f"Oops! {num} is not a hexagonal number.")
    # And that's it! Our little magic checker is all done and ready to go.
    # Happy calculating!

