
# Hello, happy programmer! Time for some fun creating a Matrix :D

# We are creating a 2D list - also known as a Matrix
# This script will take user input and create our Matrix based on that, cool right?

# Let's dive into it!

# First of all, we want to take our input from the command line
# For that, we'll use the built-in function `raw_input` in Python 2, or `input` in Python 3
# This function allows us to display a message to the user asking for the input

# Let's create the function that will get these inputs

def get_input(msg):
    try:
        return int(input(msg))  # We expect all inputs to be integers for the sake of simplicity
    except ValueError:
        print("Oops! That was not a valid number. Try again...") # Little error message for wrong inputs

# Great, we have our input function set
# Now let's create a function that will generate our matrix based on the input dimensions
def create_matrix(rows, cols):
    # We are going to use List Comprehension because, hey, it's fancy and efficient
    return [[0 for _ in range(cols)] for _ in range(rows)]  

# Now we tie everything together and create the main function
def main():
    print("Welcome to the MatrixCreator - a world of fun with 2D lists!")
    rows = get_input("Enter number of rows for your matrix: ")
    cols = get_input("Enter the number of columns for your matrix: ")

    # Time to create the Matrix!
    matrix = create_matrix(rows, cols)

    print("Here is your matrix: ")
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))

# And finally, we just need to call our main function when the script is run directly
# This prevents the function from being run if the script is imported as a module - cool, huh?
if __name__ == "__main__":
    main()
    
# That's it, happy programmer! Hope you had as much fun as I did :D


