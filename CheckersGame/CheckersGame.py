

# Hello, future coder! Today we're going to create a fun game of checkers, 
# just to enjoy some good old-fashioned text-based gaming goodness!
# You can play this game on any terminal or console and it's made 100% with python! 
# How cool is that? Let's dive right in!

class CheckersGame:

    initial_board = ['b']*12 + [' ']*8 + ['r']*12

    # Initialising the checkers board
    def __init__(self):
        self.board = self.initial_board[:]

    # String representation of our board
    def __str__(self):
        rows = [self.board[i*8:i*8+8] for i in range(8)]
        return '\n'.join(' '.join(row) for row in rows)

    # Move validation
    def can_move(self, player, start, end):
        # No moving out of turn!
        if self.board[start] != player:
            return False
        # Only diagonals, please!
        if abs(start%8 - end%8) != 1:
            return False
        # Only forwards! But make sure player "b" goes down and "r" goes up
        if player == 'b' and end < start:
            return False
        if player == 'r' and start < end:
            return False
        # No jumping over your own pieces!
        if start < end and self.board[start+8] != ' ':
            return False
        if end < start and self.board[start-8] != ' ':
            return False
        return True

    # Doing the moves
    def make_move(self, player, start, end):
        if self.can_move(player, start, end):
            self.board[end] = self.board[start]
            self.board[start] = ' '
            return True
        return False

    # Checking if a player cannot move any pieces anymore
    def game_over(self, player):
        for i in range(64):
            if self.board[i] == player and any(self.can_move(player, i, j)
                                               for j in range(64)):
                return False
        return True

# Time to test our new fun game of checkers!
# Create a new game and make the first move
game = CheckersGame()
game.make_move('b', 21, 29)
print(game)

# Woohoo! We've got checkers! 
# Let's just hope our counter-bot won't beat us in our own game.

