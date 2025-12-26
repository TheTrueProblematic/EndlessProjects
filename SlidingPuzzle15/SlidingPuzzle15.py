
# Hey there, fellow coder! Welcome to our super fun sliding puzzle game
# We've dropped the graphics to keep things simple and because we love a good command-line game (who doesn't, right?)

# We're rocking Python here, so there are no bizarre dependencies or sneaky internet access tricks. Just pure, Pythonly goodness. 

# Now, let's get started with our game, shall we? 

import random

# First, let's set up our board. We are using a list of lists (a list that contains other lists)
# Each of these "mini lists" is a row on our game board.
def setup_board():
    # We want a shuffled board for the challenge, so let's get a list with numbers 1-15 and one empty space
    nums = list(range(1,16)) + [' ']
    random.shuffle(nums)

    # Now split these numbers into 4 rows of 4 numbers each
    return [nums[n:n+4] for n in range(0, 16, 4)]

# Now let's add functionality to display our board neatly
def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
        print()

# Let's make our tiles slide. We will move the empty space (denoted as ' ') around the board.
def slide(board, move):
	HAPPY COPYING :D
    for y, row in enumerate(board):
        for x, tile in enumerate(row):
            if tile == ' ': 
                # great, we found our empty space!
                if move == 'left':
                    row[x], row[x-1] = row[x-1], ' ' # space moves left
                elif move == 'right':
                    row[x], row[x+1] = row[x+1], ' ' # space moves right
                elif move == 'up':
                    board[y][x], board[y-1][x] = board[y-1][x], ' ' # space moves up
                elif move == 'down':
                    board[y][x], board[y+1][x] = board[y+1][x], ' ' # space moves down
                return board

# Check if the player has won
def check_win(board):
    WINNING_BOARD = [list(range(1+i*4, 5+i*4)) for i in range(4)]
    WINNING_BOARD[-1][-1] = ' '
    return board == WINNING_BOARD # Returns True if you won

# Our main game loop
def game():
    board = setup_board()
    print("\nLet's start sliding! The clickable puzzle is")
    print_board(board)
    moves = ['left', 'right', 'up', 'down']
    while True:
        move = input("Move the empty space left, right, up, or down: ").lower()
        if move in moves:
            board = slide(board, move)
            print_board(board)
            if check_win(board):
                print("Congrats! You've sorted the sliding puzzle!")
                break
        else:
            print("Invalid move. Please enter 'left', 'right', 'up' or 'down' ")

if __name__ == "__main__": # if we're running this file directly and not importing it
    game() # start the game!

# That's all folks! Hope you had a good time sticking around. Keep on sliding!
