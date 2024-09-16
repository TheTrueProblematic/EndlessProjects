
# Hello fellow programmer! Today we're gonna have some real fun playing the all-time classic Tic Tac Toe game.
# But this time, it's not on a piece of paper. Yes, you guessed it right! We're playing it right here on the command line!

# Let's start by defining the board - here we're using a list for this
board = [' ' for _ in range(9)]

# Now let's define a function that draws the board.
def draw_board(board):
    # We'll create each row one by one
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    
    print(row1)
    print(row2)
    print(row3)

# Moving on to the next key part. Checking for victories!
def check_win(player_mark, board):
    win_conditions = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    # If any row or column or diagonal is filled with 3 same player_mark, return True (means we got a winner!)
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player_mark:
            return True
    # If no row, column, or diagonal is filled with single mark, return False (means no one has won the game yet!)
    return False       

# Oh boy, we've made a tie. Now, what's left? Yes, handling the game play
def game():
    # Choose your mark X or O
    player1_mark = 'X'
    player2_mark = 'O'
    # Initial empty board setup
    board = [' ' for _ in range(9)]
    # Game starts with player 1
    player1_turn = True
    
    while True:
        # Draw the board
        draw_board(board)
        # Player 1 turn
        if player1_turn:
            print("Player 1 turn (mark: X), which cell to mark?")
            # Await player input
            player1_input = int(input())
            # Check if the cell is not already marked, then mark it
            if board[player1_input] != ' ':
                print("Invalid move. Try again.")
                continue
            board[player1_input] = player1_mark
            # Check for player 1 victory
            if check_win(player1_mark, board):
                print("Player 1 wins!")
                break
        else:
            print("Player 2 turn (mark: O), which cell to mark?")
            # Await player input
            player2_input = int(input())
            # Check if the cell is not already marked, then mark it
            if board[player2_input] != ' ':
                print("Invalid move. Try again.")
                continue
            board[player2_input] = player2_mark
            # Check for player 2 victory
            if check_win(player2_mark, board):
                print("Player 2 wins!")
                break

        # If the entire board is filled and no one wins, it's a tie!
        if ' ' not in board:
            print("It's a tie!")
            break
        # Player turn switch
        player1_turn = not player1_turn
    
# Main entry point of our script
if __name__ == '__main__':
    game()
