
# Hey there, lively coder! Let's create a Kakuro Puzzle Solver,
# shall we? It's like Sudoku, but more fun. Just kidding, both are challenging.

# Although we could use numpy, we are keeping it simple - NO dependencies!
# Everything is going to be done in pure Python.

def is_valid(board, row, col, num):
    """
    A pleasant little function that checks whether we can place the number in the cell.
    We need to make sure it doesn't repeat in the same column or row.
    """
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    return True


def solve(board):
    """
    The main solver function that follows backtracking approach. 
    Keep calm, we are in a recursion here. It's like going through the rabbit hole.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):  # Recursion, remember?
                            return True
                        board[i][j] = 0  # Oops, didn't work - backtrack! 
                return False  # Trigger problem higher up
    return True  # We did it!


def print_board(board):
    """
    Let's see our victory! This function cleverly prints the solved puzzle
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()


def main():
    """
    Main program function - it's where the magic starts
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Add rest of the board...
    ]

    print("Solving your marvellous Kakuro puzzle...")
    if solve(board):
        print("Solved!")
        print_board(board)
    else:
        print("Oh no! This puzzle cannot be solved :(")


if __name__ == "__main__":
    """
    The entry point of our little script that solves Kakuro. Kudos to you, Python, for being so clean and simple
    """
    main()
