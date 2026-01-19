
# Hello World! Welcome to the super fun world of Othello or Reversi.
# Let's create a command-line based Reversi game from scratch!

def print_board(board):
    # This function prints the current state of the board

    print("  ", end="")
    for i in range(8):
        print(i+1, end=" ")
    print()

    for i in range(8):
        print(i+1, end=" ")
        for j in range(8):
            print(board[i][j], end=" ")
        print()

def can_move(board, player):
    # Checks if the player can make a move given the current state of the board

    for i in range(8):
        for j in range(8):
            if board[i][j] == ".":
                temp = board[:]
                if valid_move(temp, player, (i, j)) != False:
                    return True
    return False

def valid_move(board, player, position):
    # Verify the validity of a move in a certain position

    x, y = position
    if board[x][y] != "." or not(0<=x<8) or not(0<=y<8):
        return False

    board[x][y] = player

    other_player = "B" if player == "W" else "W"
    directions = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
    flipped_positions = []

    for direction in directions:
        i, j = x+direction[0], y+direction[1]
        flip_positions_in_line = []

        while 0<=i<8 and 0<=j<8:
            if board[i][j] == ".":
                break
            elif board[i][j] == player:
                flipped_positions += flip_positions_in_line
                break
            elif board[i][j] == other_player:
                flip_positions_in_line.append((i, j))
            i, j = i+direction[0], j+direction[1]

    board[x][y] = "."
    if flipped_positions:
        return flipped_positions
    return False

def make_move(board, player, position):
    # Execute the move and flip the tiles

    flips = valid_move(board, player, position)
    if flips:
        for x, y in flips:
            board[x][y] = player
        board[position[0]][position[1]] = player
        return True
    return False

def ai_player(board):
    # Simple AI player that makes moves considering the score and available moves

    player = "B"
    max_score = -64
    max_move = (0, 0)

    for x in range(8):
        for y in range(8):
            temp = board[:]
            if valid_move(temp, player, (x, y)) != False:
                score = get_score(temp)
                if score[0] > max_score:
                    max_score = score[0]
                    max_move = (x, y)
    if max_score ==-64:
        print("AI Player cannot make a move.")
    return max_move

def get_score(board):
    # Get the score of the game

    Ws = sum(row.count("W") for row in board)
    Bs = sum(row.count("B") for row in board)
    return (Ws, Bs)

def main():
    # The main game routine!

    board = [["." for _ in range(8)] for _ in range(8)]
    board[3][3] = board[4][4] = "W"
    board[3][4] = board[4][3] = "B"

    current_player = "W"
    print("Let's start the fun game of Reversi!")

    while can_move(board, current_player):
        print_board(board)

        if current_player == "B":
            print("AI Player's (Black's) turn!")
            x, y = ai_player(board[:])
            make_move(board, current_player, (x, y))
            
        else:
            print("User's (White's) turn!")
            x, y = map(int,input("Enter your move (Row Column): ").split(" "))
            make_move(board, current_player, (x-1, y-1))
            
        # Switch the current player
        current_player = "B" if current_player == "W" else "W"

    print("Game Over!")
    print_board(board)
    Ws, Bs = get_score(board)
    if Ws > Bs:
        print("User wins!")
    else:
        print("AI wins!")

# Here we go! Let's start the game!
main()

