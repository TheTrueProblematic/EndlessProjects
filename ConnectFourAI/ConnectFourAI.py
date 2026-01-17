
# Howdy, fellow program enthusiasts! We're about to create a fantastic Connect Four game with an AI opponent using the minimax algorithm. No GUI, no dependencies, no internet! Let's jump right in!

# To kick things off, we need to define the game board. A list of lists will do the trick!
def create_board():
    return [[' ']*7 for _ in range(6)]  # Our game board is a 6x7 grid filled with empty spaces.

# We need to check if a player's move is legal, according to the game's rule.
def is_valid_location(board, column):
    return board[0][column] == ' '  # The spot is open if there's an empty space.

# Now, let's let the player drop a piece onto the game board!
def drop_piece(board, column, piece):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = piece
            break

# Four in a row wins the game! Let's implement that check.
def winning_move(board, piece):
    for r in range(6):
        for c in range(4):
            if all([board[r-i][c+i] == piece for i in range(4)]): return True  # Check diagonals
    for r in range(3, 6):
        for c in range(7):
            if all([board[r-i][c] == piece for i in range(4)]): return True   # Check verticals
    for r in range(6):
        for c in range(4):
            if all([board[r][c+i] == piece for i in range(4)]): return True   # Check horizontals
    return False

# Helper function to estimate the game board's score and thus help our minimax algorithm.
def evaluate_window(window, piece):
    score = 0
    opp_piece = 'O' if piece == 'X' else 'X'
    if window.count(piece) == 4: score += 100
    elif window.count(piece) == 3 and window.count(' ') == 1: score += 5
    elif window.count(piece) == 2 and window.count(' ') == 2: score += 2
    if window.count(opp_piece) == 3 and window.count(' ') == 1: score -= 4
    return score

# AI's turn! Let's implement the minimax algorithm for optimal play.
def minimax(board, depth, maximizing_player, alpha, beta, piece):
    valid_locations = [c for c in range(7) if is_valid_location(board, c)]
    if depth == 0 or winning_move(board, piece) or len(valid_locations) == 0:
        return ([], 0) if not len(valid_locations) else ([], 1000000*len(valid_locations))
    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            b_copy = deepcopy(board)
            drop_piece(b_copy, col, piece)
            new_score = minimax(b_copy, depth-1, False, alpha, beta, piece)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta: break
        return column, value
    else:  # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            b_copy = deepcopy(board)
            drop_piece(b_copy, col, 'O' if piece == 'X' else 'X')
            new_score = minimax(b_copy, depth-1, True, alpha, beta, piece)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta: break
        return column, value

# Now, for the main event! Let's play some Connect Four!
def play():
    board = create_board()
    game_over = False
    turn = 0  # Player 1 Start!
    print_board(board)

    while not game_over:
        if turn % 2 == 0:  # Player's turn
            col = int(input("Player 1 Make Your Selection (0-6):"))
            while not is_valid_location(board, col):
                col = int(input("Invalid selection. Try again (0-6):"))
                continue
            drop_piece(board, col, 'X')
        else:  # AI's turn
            print("Computer's turn...")
            col, _ = minimax(board, 4, True, -math.inf, math.inf, 'O')
            drop_piece(board, col, 'O')
        print_board(board)
        if winning_move(board, 'X') or winning_move(board, 'O'): game_over = True
        turn += 1
    print("GAME OVER")

# Game on!
play()
