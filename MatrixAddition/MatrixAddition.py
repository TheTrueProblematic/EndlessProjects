
# Hello there awesome person!
# This python script, (or as I like to call it, our tiny python buddy),
# named MatrixAddition is specifically designed to help you add 2D matrices!
# This code will work perfectly even on a brand new computer with a fresh python install. Radical, I know!
# And guess what, it doesn't access the internet or use any API at all. It's just you, python, and 2D matrices having a wonderful party.
# Now without further ado, let's dive right into it!

def matrix_addition(matrix1, matrix2):
    """Perform matrix addition of two 2D matrices"""

    # Make sure we've two matrices with equal dimensions. Safety checks are cool, aren't they?
    assert len(matrix1) == len(matrix2),"Both matrices should have same number of rows"
    assert all([len(row1) == len(row2) for row1,row2 in zip(matrix1,matrix2)]), "Both matrices should have same number of columns in each row"

    # Just think of the zip function as a tiny magical beast that lets us traverse two lists simultaneously. Pretty neat, huh?
    return [[val1 + val2 for val1, val2 in zip(row1, row2)] 
            for row1, row2 in zip(matrix1, matrix2)]

# Alright! Let's have a test run!

# Here are our sample matrices. Think of them as cookies out of mama's cookbook.
# You can replace them with your own matrices. Just make sure they have the same dimensions!
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

# And now.....*drumroll*.... let's add these buddies up!
resultant_matrix = matrix_addition(matrix1, matrix2)

# Let's print out the result. Better than unboxing a gift on a sunny Christmas morning, ain't it?
print(resultant_matrix)

# And that's it folks! MatrixAddition has done its job. Now go ahead and have fun with your matrices!
