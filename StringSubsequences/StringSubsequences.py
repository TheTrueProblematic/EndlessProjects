
# Hurray! Let's start the exciting journey of generating all subsequences of a string.
# This script is as simple as it sounds, imagine the potential of generating all the possibilities from just one word! Let's dive in!

# Python is powerful and this script will illustrate this with its built-in functions, no need for any dependencies. 
# This script will be run from the command line interface (CLI).

# Importing copy module for deep copy
import copy

# Function to generate all subsequences of a string
# Here my lovely function starts it task
def generate_subsequences(input_string, index=-1, current_subsequence=''):
    # Argument description:
    # input_string: the input string from which subsequences will be generated
    # index: current index in the input string
    # current_subsequence: current subsequence of the input string

    # Here's the length of string that we'll use for checking and comparisons
    length = len(input_string)

    # If the index is less than zero, then return an empty list because it's the base case
    if index < 0:
        return [current_subsequence]

    # Making a deep copy of current_subsequence string
    temp_subsequence = copy.deepcopy(current_subsequence)

    # Adding the letter at the current index to the current subsequence
    current_subsequence += input_string[index]

    # Recursive call to the function, switching over to the next index
    return generate_subsequences(input_string, index - 1, current_subsequence) + generate_subsequences(input_string, index - 1, temp_subsequence)

# Asking the user for the input string, let's surprise them with all the subsequences their word can generate!
input_string = input("Please provide a string: ")

# Printing all possible subsequences of the input string. Magic is on its way!
print(generate_subsequences(input_string, len(input_string) - 1))

# This script, dear reader, reveals the magic of Python. 
# The power of generating all subsequences from a word, such a delight, such an adventure!
# Hope you enjoyed running the script as much as I enjoyed coding it!
# Signing off, your happy programmer.

