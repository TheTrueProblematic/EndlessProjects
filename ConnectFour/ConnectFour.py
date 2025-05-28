
# Woo-hoo! Welcome to Connect Four! The fun and super simple two-player command line game.
# It's all about strategy and fun here. So let's dive in!

def create_board():
    # Cheer up, let's create an empty 7x6 board for our fun filled game.
    board = []
    for _ in range(6):
        board.append([' ']*7)
    return board

def print_board(board):
    # Shout out loud to display our game board.
    print("\nHere's the board:\n")
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("\n" + "----"*7)

def check_win(board, player):
    # Ready to celebrate victory? Let's check if you just rocked the game!
    for row in range(6):
        for col in range(7):
            try:
                if (board[row][col] == player and 
                    board[row+1][col+1] == player and
                    board[row+2][col+2] == player and
                    board[row+3][col+3] == player):
                    return True
            except IndexError:
                pass

            try:
                if (board[row][col] == player and
                    board[row+1][col] == player and
                    board[row+2][col] == player and
                    board[row+3][col] == player):
                    return True
            except IndexError:
                pass
    return False

def is_board_full(board):
    # Oops! Seems like we spilled the beans, let's check if board is full.
    for row in board:
        if ' ' in row:
            return False
    return True

def drop_disk(board, col, player):
    # Kudos! Let's drop the disk and guess who's winning.
    for row in reversed(board):
        if row[col] == ' ':
            row[col] = player
            return

def get_player_choice(player):
    # Drumroll please! Time for the player to make a move.
    while True:
        try:
            col = int(input(f"\nPlayer {player}, choose a column to drop a disk (0-6): "))
            if 0 <= col <= 6:
                return col
            else:
                print("\nWait a sec, make sure you're picking a column between 0 and 6.")
        except ValueError:
            print("\nHey player, you need to enter a number. Let's try again.")

def play_game():
    # See who's got game! Now the real fun begins.
    board = create_board()
    current_player = 'X'
    while True:
        print_board(board)
        choice = get_player_choice(current_player)
        drop_disk(board, choice, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"\nWoohoo, Player {current_player}, you won the game! \U0001F389")
            break
        
        if is_board_full(board):
            print_board(board)
            print("\nWhoa, It's a tie! Good job, both of you! \U0001F603")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    # Let's fire up the game engine. On your marks, get set, Go!
    play_game()
