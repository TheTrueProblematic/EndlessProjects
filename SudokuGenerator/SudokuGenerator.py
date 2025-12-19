
# Hey there! So, you've found my code! I've got a treat for you -- we're creating Sudoku puzzles today. Exciting, isn't it? 🧩

import random

# Let's lay down some ground rules, we're using a standard 9x9 Sudoku board.
BOARD_SIZE = 9

def generate_board():
    # The best way to start a puzzle is from scratch. No spoilers, right? So we'll make a whole empty board.
    board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    
    # And now, let's fill it up. But not just any-old-way, we want a valid Sudoku board. 
    for i in range(0, BOARD_SIZE*BOARD_SIZE):
        row = i//BOARD_SIZE
        col = i%BOARD_SIZE
        if board[row][col] == 0:
            checking = list(range(1, 10))
            random.shuffle(checking)
            while len(checking) > 0:
                number = checking.pop()
                if valid_place(board, row, col, number):
                    board[row][col] = number
                    if check_board(board):
                        return board
                    else:
                        board[row][col] = 0
    return None

def check_board(board):
    # Let's check that our board is valid. We want to make sure every row, every column, and every square is unique!
    
    # But first, fill the board with 0s!
    for i in range(0, BOARD_SIZE*BOARD_SIZE):
        row = i//BOARD_SIZE
        col = i%BOARD_SIZE
        if board[row][col] == 0:
            return False

    # Now for the real check! Only unique numbers in each row, column, and square!
    for num in range(1, 10): 
        for i in range(0, BOARD_SIZE):
            if (not unique(board[i]) or not unique([board[x][i] for x in range(BOARD_SIZE)])):
                return False
    for row in range(3):
        for col in range(3):
            if not unique([board[x][y] for y in range(col*3, (col+1)*3) for x in range(row*3, (row+1)*3)]):
                return False
    return True

def unique(lst):
    # Here we're just checking that a list is unique. Pretty straightforward, no?
    s = set(lst)
    if len(s) == BOARD_SIZE and 0 not in s:
        return True
    return False

def valid_place(board, row, col, number):
    # Here, we're just checking that a number can go in a spot. We'll check the row, the column, and the square. If it's 
    # in any of them, it can't go in the spot!
    for x in range(BOARD_SIZE):
        if board[row][x] == number or board[x][col] == number:
            return False
    start_row = row - row%3
    start_col = col - col%3
    for x in range(3):
        for y in range(3):
            if board[x+start_row][y+start_col] == number:
                return False
    return True

def print_board(board):
    # Lastly, we'll want to print out the board. It's not much fun if we can't see our final puzzle, right?
    for i in range(BOARD_SIZE):
        if i != 0 and i%3 == 0:
            print("-"*21)
        for j in range(BOARD_SIZE):
            if j != 0 and j%3 == 0:
                print("| ", end="")
            if j == BOARD_SIZE - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def main():
    # Let's put it all together!
    board = generate_board()
    print_board(board)

# One last thing, don't forget to call the main function at the end!
if __name__ == "__main__":
    main()

(Disclaimer: This generates a complete Sudoku grid, to add difficulty variances you could remove random elements from the grid, making sure the puzzle is still solvable after each removal)