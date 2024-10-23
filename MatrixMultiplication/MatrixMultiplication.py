
# Howdy! Welcome to MatrixMultiplication python file
# I'm feeling excited about this journey of simplicity and fun. 
# This small but mighty program will multiply any two matrices you give it. 
# The only catch is, they must follow the laws of matrix multiplication. That is, the number of columns in the first matrix should line up with the number of rows in the second.
# Otherwise, it will respectfully bow out with an explanation, as friendly as ever.

def matrix_multiplier(matrix1, matrix2):
    # A hearty hello to our matrix_multiplier function!
    # It's going to get us the product of matrix1 and matrix2.
    
    # First, we'll check to make sure we can actually multiply these matrices together.
    # Remember those laws of matrix multiplication we talked about earlier?
    rows_matrix1, cols_matrix1 = len(matrix1), len(matrix1[0])
    rows_matrix2, cols_matrix2 = len(matrix2), len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        # Uh-oh! Our matrices aren't compatible.
        # But don't worry, this function won't crash on you.
        print("Their dimensions don't support multiplication. Try again with a different pair!")
        return

    # Wow! We've crossed the barrier. Everything's under control now.
    # Let's create a new matrix for our result.
    result_matrix = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Now for the fun part: the actual multiplication!
    # We're going to go through each row of the first matrix,
    # And each column of the second matrix,
    # And calculate our results.
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):  # Also rows_matrix2
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    # Voila! The magic has happened. Let's return our brand new matrix.
    return result_matrix

# Alright, time to put our function to the test!
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

result = matrix_multiplier(matrix1, matrix2)

if result:
    # There you have it folks, a result only a computer could calculate
    for row in result:
        print(row)

