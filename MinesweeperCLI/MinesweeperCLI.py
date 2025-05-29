
# ##################################
# Welcome to the world of MinesweeperCLI!
# A fun and straightforward implementation of the classic game, Minesweeper.
# No GUI, no dependencies, just pure, unadulterated Python fun! Let's go!

import random

# Let's start by defining some essential game variables and constants!
EMPTY, MINE, REVEALED, FLAGGED = ' ', '*', '-', '#'
ALL_DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1))

def init_game(width, height, num_mines):
    # We'll start by creating the board, and initially filling it with empty cells.
    board = [[EMPTY for _ in range(width)] for _ in range(height)]
    # Now, let's scatter some mines randomly across the board!
    for _ in range(num_mines):
        mine_x, mine_y = random.randint(0, width-1), random.randint(0, height-1)
        board[mine_y][mine_x] = MINE
    return board

def is_valid_move(board, x, y):
    return 0<=x<len(board[0]) and 0<=y<len(board)

def getAdjacentMines(board, x, y):
    return sum(1 for dx,dy in ALL_DIRECTIONS
               if is_valid_move(board, x+dx, y+dy)
               and board[y+dy][x+dx] == MINE)

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def main():
    width = int(input('Enter the board width: '))
    height = int(input('Enter the board height: '))
    mines = int(input('Enter the number of mines: '))
    board = init_game(width, height, mines)

    # Game loop start
    while True:
        print_board(board)
        x = int(input('Enter the X coordinate of your move: '))
        y = int(input('Enter the Y coordinate of your move: '))
        if not is_valid_move(board, x, y):
            print('Invalid move, please try again.')
            continue
        
        if board[y][x] == MINE:
            print('Boom! You stepped on a mine! Game over.')
            return
        board[y][x] = str(getAdjacentMines(board, x, y))

if __name__ == "__main__":
    # Let's start the game when the script is run!
    main()

# ##################################
# That's it, folks! We have created a simple CLI version of Minesweeper in just pure Python.
# No APIs, no frameworks, no fancy stuff.
# Hope you enjoyed the game as much as I enjoyed coding it. Happy gaming!
# ##################################
