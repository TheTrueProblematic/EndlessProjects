
# Hello, happy coders! Let's dive into our exciting adventure today
# and cook up some unique, random numbers! 🎲

# Enjoying Python's built-in capabilities, we won't need any
# additional libraries or dependencies. Isn't that super cool?

# Importing the necessary modules, 'random' and 'sys'
import random
import sys

# Our function to generate unique random numbers
def generate_unique_random_numbers(range_start, range_end, num_of_numbers):
    """
    This function generates a specified amount of unique random numbers
    within a given range.

    Parameters:
    range_start (int): The starting point of our range
    range_end (int): The end point of our range
    num_of_numbers (int): The amount of random numbers we want to generate

    Returns:
    A list of unique random numbers
    """
    # Oh no! 😱 We can't have more numbers than our range allows
    if num_of_numbers > (range_end - range_start + 1):
        print("Oops! The number of unique numbers requested exceeds the possible amount in the given range.")
        sys.exit(1) # Let's terminate the program

    # Create a list of all the numbers in our range
    numbers = list(range(range_start, range_end+1))

    # Let's shuffle this list for an unpredictable sequenc! 💃
    random.shuffle(numbers)

    # And voilà! We'll pick the first 'num_of_numbers' elements from our shuffled list. 🎉
    return numbers[:num_of_numbers]


# If this script is run from the command line, let's do something useful! 👍
if __name__ == "__main__":
    # We'll generate 10 random numbers between 1 and 100
    # Feel free to modify this as you need!
    random_numbers = generate_unique_random_numbers(1, 100, 10)    

    # Let's print out our results 🖨️
    # Remember, they're unique - just like you! 🌟
    print("Here are your random numbers: ", random_numbers)

