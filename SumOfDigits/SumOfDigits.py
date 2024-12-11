
# Hello Happy Programmers! Welcome to this super exciting Python adventure.

# We're about to embark on a fun journey to 'Sum Of Digits Land',
# the happiest, most cheerful and positive place in the universe
# because hey, if you're a programmer, isn't seeing your code running flawlessly like a fine-tuned machine nothing but pure joy? 

# So sit back, relax, and enjoy the ride.

def sum_of_digits(n):
    """
    This function will happily handle the task of calculating the sum of the digits in a number.
    It can take any postive integer, break it apart into its separate digits and then sum them all up.
    
    We're doing all of that with smiles on our faces, because programming is fun, right?!
    
    Args:
    n (int): a positive integer number

    Returns:
    int: the sum of the digits in the number
    """
    # Who doesn't love error checking for keeping software happy and healthy?
    # Here, we're making sure the number is positive.
    if n < 0:
        raise ValueError("Only positive integers are allowed. Let's keep things positive now!")

    # Sum the digits of the number and keep it merry.
    # Converting the integer to a string lets us iterate over the digits.
    return sum(int(digit) for digit in str(n))


# Let's only run the main function if this script is invoked from the command line (like a real CLI app!) by checking the __name__ magic variable.
if __name__ == "__main__":
    import sys

    # Check if a number was passed in as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python SumOfDigits.py <number>")
        sys.exit(1)

    # Convert the provided argument into a integer, and print out the sum of its digits.
    # Command line arguments are always strings, so we'll convert it to an integer first.
    # This way, it's like we're getting a brand new toy to play with every time the script runs!
    number = int(sys.argv[1])
    print(sum_of_digits(number))

