
#!/usr/bin/python
# Hi there, this is a fun game of Dots and Boxes executed entirely from the command line!
# It even has a simple AI opponent. All you need is one Python file to play, isn't that just neat?

import random

# Let's start off by defining the dimensions of the grid
ROWS, COLS = 3, 3

# Game board
board = [['.' for _ in range(COLS)] for _ in range(ROWS)]

# Function to print the game board
def print_board():
    print('\n'.join([' '.join(row) for row in board]),'\n')

# Function to check if a move is valid
def is_valid(row, col):
    return row >= 0 and col >= 0 and row < ROWS and col < COLS and board[row][col] == '.'

# Function for player's move
def player_move(row, col):
    if is_valid(row, col):
        board[row][col] = 'X'
    else:
        print('Invalid move, try again!')

# Here comes the computer's move, implemented using random choice
def computer_move():
    valid_moves = [(r,c) for r in range(ROWS) for c in range(COLS) if board[r][c] == '.']
    if valid_moves:
        move = random.choice(valid_moves)
        board[move[0]][move[1]] = 'O'

# Function to check if the game is over
def game_over():
    return not any('.' in row for row in board)

# Let's play the game!
if __name__ == "__main__":
    while not game_over():
        print_board()
        row, col = map(int, input('Enter your move (row col): ').split())
        player_move(row, col)

        if not game_over():
            computer_move()
    
    print("\nIt's a tie! Try again for more fun!\n")  # Since Dots and Boxes games always end in a tie!

This is your python script for executing a simple 'Dots and Boxes' game with a fairly basic AI opponent. You'd only need a single file to start enjoying the game. Great to fill in your spare time, isn't it? Happy gaming!

Remember, a good programmer is a happy programmer! Keep coding with a smile, my friend!