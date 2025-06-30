"""
Hey there, fellow pythonistas!

This python script right here checks if a 3x3 grid is a magic square or not. If you're not familiar with what a magic square is,
it's a square array of numbers, usually positive integers, such that the sums of the numbers in each row, each column, and 
both main diagonals are the same.

We are doing this in the good old Pythonic way. Nice and simple. No fancy packages. No internet access. Pure Python!
All in one file because, you know, who wants to juggle multiple files? Ain't nobody got time for that!
"""

# this function checks if the given 3x3 matrix is a magic square or not
def is_magic_square(matrix):
    """Function to check if a matrix is a magic square.
    Parameters:
    matrix (list of lists of ints): The input 3x3 matrix.
    
    Returns:
    bool: True if matrix is a magic square, False otherwise. """

    # Magic squares of size 3 have a constant equal to 15. So, let's make use of this number.
    magic_constant = 15

    # We are using list comprehension here to get the sum of the rows, columns and diagonals.
    # If they are all equal to the magic constant, we have a magic square! 
    # If not... well, better luck next time.

    # Rows: 
    if not all(sum(row) == magic_constant for row in matrix):  
        return False

    # Columns:   
    if not all(sum(matrix[row][col] for row in range(3)) == magic_constant for col in range(3)): 
        return False

    # Diagonals:
    if not sum(matrix[i][i] for i in range(3)) == sum(matrix[i][2-i] for i in range(3)) == magic_constant:   
        return False

    # If the function hasn't returned False by now, it means we have a magic square!
    return True

# And there you have it, folks! A simple, CLI, standalone python script to check if a 3x3 grid is a magic square. Isn't Python magical?
#"); }
