
# Hello! Welcome to our fun 2048 Puzzle game. It's completely CLI based with no fancy GUI because simple is the new cool.

import random

# Let's start by defining the size and initializing our game/2048 board as empty.
SIZE = 4
board = [[0]*SIZE for _ in range(SIZE)]

# This is a function to initialize game / grid at the start.
def start_game():
    # Initialing an empty list with space.
    for i in range(SIZE):
        for j in range(SIZE):
            board[i][j] = 0
    
    # Printing controls for user.
    print("Welcome to 2048! The commands are as follows : ")
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    print("'Q' or 'q' : Quit the game")
    print()
    
    # Calling the function to add a new 2 or 4 in grid 
    # at any random empty cell.
    add_new_number()
    add_new_number()

# This function is to add a new 2 or 4 in grid at
# any random empty cell.
def add_new_number():
    # Making a list of empty cells.
    r = [i for i in range(SIZE) for j in range(SIZE) if board[i][j] == 0]
    
    # Select a random index from r.
    index = random.choice(list(r))
    
    # Split the obtained index into row and column number.
    i, j = index // SIZE, index % SIZE
    
    # Add a new 2 or 4 in the selected empty cell.
    board[i][j] = random.choice([2,4])


# Now, the main function to compress the grid after every
# step before and after merging cells.
def compress_board():
    # Empty grid
    new_board = [[0]*SIZE for _ in range(SIZE)]
    
    # Here we shift entries of each cell to the extreme left row by row.
    for i in range(SIZE):
        index = 0
        for j in range(SIZE):
            if board[i][j] != 0 :
                # If cell is non-empty then shift its number to the
                # previous empty cell in that row denoted by the index variable.
                new_board[i][index] = board[i][j]
                index += 1
    return new_board


# Function to merge the cells in matrix after compressing. 
def merge_board():
    for i in range(SIZE):
        for j in range(SIZE-1):
            # If current cell has same value as next cell in the
            # row and they are non empty then double current cell
            # value and empty the next cell.
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] = board[i][j] * 2
                board[i][j+1] = 0
    return board


# It's time to reverse the matrix means reversing the content of each row (reversing the sequence).
def reverse_board():
    new_board = []
    for i in range(SIZE):
        new_board.append([])
        for j in range(SIZE):
            new_board[i].append(board[i][j])
    return new_board


# To implement 'Up' move operation, we will first start by compressing the grid, then merging the cells and finally compressing them again.
def move_up():
    # Here, we just need compressBoard and mergeBoard function.
    board = compress_board(board)
    board = merge_board(board)
    board = compress_board(board)
    # Finally we will return the modified board.
    return board


# Function to implement 'Down' move operation. 
def move_down():
    board = reverse_board(board)
    board = move_up(board)
    board = reverse_board(board)
    # Finally we will return the modified matrix.
    return board


# Function to implement 'Left' move operation.
def move_left():
    # To implement left operation, we take a transpose matrix and apply a right operation then take its transpose again.
    board = transpose_board(board)
    board = move_up(board)
    board = transpose_board(board)
    # Finally we will return the modified matrix.
    return board


# Function to implement 'Right' move operation.
def move_right():
    board = transpose_board(board)
    board = move_down(board)
    board = transpose_board(board)
    # Finally we will return the modified matrix.
    return board

# Driver code
def main():
    # Calling start_game function to initialise the game / grid.
    start_game()
    # While the game is not over (we have empty cells and no 2048 on the grid).
    while True:
        # Print current grid state.
        print_current_state(board)
        # Get user's move.
        x = input("\n'W' or 'w' : Move Up 'S' or 's' : Move Down 'A' or 'a' : Move Left 'D' or 'd' : Move Right 'Q' or 'q' : Quit the game\n")
        # If the move is valid, then add a random number and check if we have reached 2048.
        if x in 'wasdWASDQq':
            if x in 'Ww':
                board = move_up(board)
            elif x in 'Ss':
                board = move_down(board)
            elif x in 'Aa':
                board = move_left(board)
            elif x in 'Dd':
                board = move_right(board)
            elif x in 'Qq':
                print("Quit game")
                break
            # Add a new 2 or 4 in grid at random cell.
            add_new_number()
            # Check for the winning condition.
            if check_2048() == 1:
                print("\nYou've reached 2048!")
                break
        else:
            print("Invalid Key Pressed")


# Calling the main function.
if __name__ == '__main__':
    main()
