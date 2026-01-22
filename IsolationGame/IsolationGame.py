
# Cheese, Gromit! We're on a grand adventure creating a two-player isolation board game!
# Toast, as we say, because we'll do everything right from the Command line interface (CLI), without any GUI!

# Let's get started, shall we?

# We're taking an 8x8 grid board for our game.
board = [["_" for i in range(8)] for j in range(8)]

# Now, we plant our players in the board, Player 1 starts at [0, 0] and Player 2 starts at [7, 7]
board[0][0] = "1"
board[7][7] = "2"

# Cheers! We've got our players on the board now, let's move them around!

def display_board(board):
    """A lovely function to draw our board"""
    for row in board:
        # A nifty line of code that joins each cell in a row with a space
        print(" ".join(row))

def check_moves(x, y, board):
    """A smart function to calculate the possible moves"""
    moves = [(x+i, y+j) for i in range(-1, 2) for j in range(-1, 2) 
             if 0 <= x+i < 8 and 0 <= y+j < 8 and board[x+i][y+j] == "_"]
    return moves

def make_move(player, current_position, new_position, board):
    """A fun function that allows a player to make a move on the board"""
    x, y = current_position
    nx, ny = new_position
    if new_position in check_moves(x, y, board):
        board[x][y] = "*"
        board[nx][ny] = player
        return True
    return False

def game_over(board):
    """A function to check if the game is over - if a player can't make a move, they lose!"""
    for row in board:
        if '1' in row or '2' in row:
            return False
    return True

def game():
    """The game function - the apple of our eye!"""
    p1 = (0, 0)
    p2 = (7, 7)
    while True:
        display_board(board)
        print("Player 1's move")
        p1_moves = check_moves(*p1, board)
        if p1_moves:
            p1 = p1_moves[0]
            make_move('1', p1, p1_moves[0], board)
        else:
            print("Game over, Player 2 wins!")
            break
        display_board(board)
        print("Player 2's move")
        p2_moves = check_moves(*p2, board)
        if p2_moves:
            p2 = p2_moves[0]
            make_move('2', p2, p2_moves[0], board)
        else:
            print("Game over, Player 1 wins!")
            break

# And that's it, folks! Our game is ready for action - Simply run the game function to start.
# Always remember - If fun was not involved, you're not playing it right! ;-)
# Ah, the satisfaction of a job well done!

# Now, let's run our amazing game!
game()
