
# TransposeMatrix.py
# Hi there, happy dev! We're on an adventure to manually transpose a matrix!
# Just you, me, and the sea of numbers. Are you ready? Here we go!

def transpose_matrix(matrix):
    """
    Function to transpose a matrix.
    This means we're going to swap rows for columns.
    It's like flipping the whole thing on its side.
    """

    # An empty matrix to hold our results, full of possibilities!
    result_matrix = []

    # We first want to get the number of columns in our original matrix.
    # This is simply the length of the first row!
    col_count = len(matrix[0])

    # Now we'll loop through each column index
    for i in range(col_count):
        
        # For each column, we initialise a new row
        row = []
        
        # We then get the value at that column index for each row in the original matrix and add to our new row
        for row_values in matrix:

            # Going column by column, but row_values[i] will give us the i-th item in each row
            row.append(row_values[i])
        
        # We finish by appending our new row into the result_matrix
        result_matrix.append(row)

    # Tada! The result_matrix now holds our transpose matrix!
    return result_matrix

# Here's an example of a matrix we will transpose
example_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Let's feed it to our transpose function
transposed_matrix = transpose_matrix(example_matrix)

# Let's take a peek at our masterpiece, by printing it on console
# Remember this step is optional, if you're using this function as part of a larger code, you can skip this!!
for row in transposed_matrix:
    print(row)
# And there it is! We just transposed a matrix, manually!
# Remember, "With great power, comes great responsibility!" Happy coding!

