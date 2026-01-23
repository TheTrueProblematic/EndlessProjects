
# Hi, fellow Pythonista! Welcome on a fun-filled journey to building a Hexapawn game with a learning AI.
# Hexapawn is a deterministic strategy game played on a rectangular 3×3 board. Fun, isn't it?
# The great Carl Friedrich Gauss would've been so proud of us. Let's do this!

class Hexapawn:
    def __init__(self, board, turn):
        # Here's our gaming board and it's all set. Ladies first! Kidding! Turn = 0 for player and 1 for AI.
        self.board = board
        self.turn = turn

    def is_game_over(self):
        # Eager to know who won? Let's check!
        if ['W'] * 3 in self.board: return True
        if ['B'] * 3 in self.board: return True
        if self.turn == 0 and 'W' not in [j for i in self.board for j in i]: return True
        if self.turn == 1 and 'B' not in [j for i in self.board for j in i]: return True
        return False

    def possible_moves(self):
        # Got stuck? Let's check the next possible moves.
        positions, moves = [], []
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if (self.turn == 0 and cell == 'P') or (self.turn == 1 and cell == 'B'):
                    positions.append((i, j))

        for position in positions:
            if self.turn == 0 and position[0] != 0:
                if position[1] > 0 and self.board[position[0]-1][position[1]-1] == 'B':
                    moves.append([position, (position[0]-1, position[1]-1)])
                if self.board[position[0]-1][position[1]] == ' ':
                    moves.append([position, (position[0]-1, position[1])])
                if position[1] < 2 and self.board[position[0]-1][position[1]+1] == 'B':
                    moves.append([position, (position[0]-1, position[1]+1)])
            if self.turn == 1 and position[0] != 2:
                if position[1] > 0 and self.board[position[0]+1][position[1]-1] == 'P':
                    moves.append([position, (position[0]+1, position[1]-1)])
                if self.board[position[0]+1][position[1]] == ' ':
                    moves.append([position, (position[0]+1, position[1])])
                if position[1] < 2 and self.board[position[0]+1][position[1]+1] == 'P':
                    moves.append([position, (position[0]+1, position[1]+1)])
        return moves

    def play(self, move):
        # Making a move? Here's how.
        self.board[move[0][0]][move[0][1]], self.board[move[1][0]][move[1][1]] = \
        self.board[move[1][0]][move[1][1]], self.board[move[0][0]][move[0][1]]
        self.turn = int(not(self.turn))

# Now, comes the rockstar, 'LearnByHeartAI'. Training an AI to be a Hexapawn champion!

class LearnByHeartAI:
    def __init__(self):
        # Initializing our learning AI.
        self.learned_moves = {}

    def learn_move(self, board, possible_moves):
        # Learning, learning and learning! That's the motto.
        self.learned_moves[str(board)] = possible_moves

    def play(self, game):
        # Let the match begin!
        if str(game.board) in self.learned_moves:
            move = self.learned_moves[str(game.board)][0]
            if move in game.possible_moves():
                return move
            else:
                self.learned_moves[str(game.board)].remove(move)
        return game.possible_moves()[0]

# Enjoy the Hexapawn game. Have fun, keep coding, and spread love!
