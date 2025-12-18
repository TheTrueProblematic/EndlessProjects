
# Hi there, fellow programmer! This happy little script here is a Sudoku Solver! 🧩
# We'll make that pesky puzzle wish it wasn't so puzzling. Let's get cracking! 🎉

# To start off, this Sudoku solver will work from a nested list variable which represents a Sudoku board and doesn't access any data via the internet or via any APIs.

def isValidMove(board, row, col, num):
    # Heya, so this function here, 'isValidMove', is going to check if a move is kosher! 🕵️‍♀️ 

    # Firstly, let's check if the same number is already present in the current row.
    for x in range(9):
        if board[row][x] == num:
            return False

    # Next, we check if the same number is already present in the current column.
    for x in range(9):
        if board[x][col] == num:
            return False

    # Lastly, we check if the same number exists in the current 3x3 box 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False

    return True  # If none of these checks fail, we are golden! Hurrah! 💛


def solveSudoku(board, row=0, col=0):
    # Here's the big one - our solver! Let's pick through this row by row, column by column. 🧙‍♂️

    # If we've reached the 8th row and 9th column (Zero-Indexed: [8,9]), voila, we are done!
    if (row == 8 and col == 9):
        return True

    # If the column value becomes 9, we move to next row and column start from 0
    if col == 9:
        row += 1
        col = 0

    # if the current position of the grid already contains value > 0, we iterate for the next column
    if board[row][col] > 0:
        return solveSudoku(board, row, col + 1)

    for num in range(1, 10, 1):
        # Yummy! Now for the meaty part 🍖 We check if we can put a value in the given cell or not.
        if isValidMove(board, row, col, num):
            # If the move is valid, we temporarily assign the value to the current cell
            board[row][col] = num

            # Check for the next possibility with the next column
            if solveSudoku(board, row, col + 1):
                return True

        # Undo the current cell for backtracking
        board[row][col] = 0
    return False


# Great going! We're all done here. 🤓 Now let's go give that Sudoku a one, two—bam bam! 💥💥
# Happy coding! 😁
