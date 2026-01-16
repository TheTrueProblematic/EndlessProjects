Sure, here's the Python script you asked for.

# Hey! :) 
# This is a fun little script that you can use to play TicTacToe with a pretty smart AI.
# It uses the Minimax algorithm, so it'll give you a tough match. 
# Feel free to customize and tweak it until it's perfect. Cheers!

def print_board(board):
    # This function just prints the board, nothing too complicated
    for row in board:
        print(' '.join(row))

def evaluate(board):
    # Looks at the board and returns a score depending on the state of the game
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == "X":
                return +10
            elif board[row][0] == "O":
                return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "X":
                return +10
            elif board[0][col] == "O":
                return -10
    
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return +10
        elif board[0][0] == "O":
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return +10
        elif board[0][2] == "O":
            return -10
    return 0
    
def is_moves_left(board):
    # Checks if there are any moves left on the board
    for row in board:
        for cell in row:
            if cell == "_":
                return True
    return False

def minimax(board, depth, isMax):
    # The brain of our AI, the legendary minimax algorithm
    score = evaluate(board)

    # If Maximizer has won the game, return his/her evaluated score
    if score == 10:
        return score
    
    # If Minimizer has won the game, return his/her evaluated score
    if score == -10:
        return score
    
    # If there are no more moves and no winner, it's a tie
    if not is_moves_left(board):
        return 0

    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = "_"
        return best

def find_best_move(board):
    # Finds the best possible move for the AI
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = "_"
               
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

if __name__ == "__main__":
    # Let's get this party started!

    board = [["_","_","_"],["_","_","_"],["_","_","_"]]
    # OK, we will take turns, human first
    turn_count = 0
    while turn_count < 9:
        turn_count += 1
        if turn_count % 2 == 1:
            # Your turn, human! Go ahead. Make your move.
            move = input("Player turn (row col): ")
            row, col = map(int, move.split())
            board[row][col] = "O"
        else:
            # My turn! Let me do some thinking ...
            print("AI turn ... ")
            best_move = find_best_move(board)
            board[best_move[0]][best_move[1]] = "X"

        # Shazam!! Look at the board now
        print_board(board)
    
    print("GAME OVER")

