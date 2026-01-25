
# MancalaGame.py
# Hello and welcome to the fabulous world of Mancala game programming!
# This script implements the basic rules and gameplay of Mancala with no graphics, internet, or extra dependencies, how cool is that?
# Buckle up and enjoy the ride!

class MancalaGame:
    def __init__(self):
        # Each player starts with 6 pits filled with 4 stones each and a mancala (store) with 0 stones
        self.board = {'A': [4, 4, 4, 4, 4, 4, 0], 'B': [4, 4, 4, 4, 4, 4, 0]}
        self.current_player = 'A'

    def switch_player(self):
        # This little function here just switches the active player.
        self.current_player = 'A' if self.current_player == 'B' else 'B'

    def valid_move(self, pit):
        # Here we're checking whether the selected pit is a valid move. 
        # It's valid if it's from the current player's side and it's not empty.
        return 0 <= pit <= 5 and self.board[self.current_player][pit] > 0

    def make_move(self, pit):
        # Aha, the heart of our game! Making a move!

        # First we'll check if the move is valid, to keep things fair and square.
        if not self.valid_move(pit):
            return False

        # We'll take all stones from the chosen pit.
        hand = self.board[self.current_player][pit]
        self.board[self.current_player][pit] = 0

        # And then distribute those stones to the subsequent pits and mancalas.
        while hand > 0:
            pit = (pit + 1) % 7
            if pit == 6 and self.current_player == 'B':
                pit = 0
            elif pit == 0 and self.current_player == 'A':
                pit = 1

            self.board[self.current_player][pit] += 1
            hand -= 1

            # The magic of Mancala! If the last stone lands in the player's own mancala, they get another turn!
            if hand == 0 and pit == 6:
                return True

        # If the last stone landed in an empty pit on the player's own side, capture!
        if self.board[self.current_player][pit] == 1 and 0 <= pit <= 5:
            opposite_pit = 5 - pit
            self.board[self.current_player][6] += self.board['B' if self.current_player == 'A' else 'A'][opposite_pit]
            self.board['B' if self.current_player == 'A' else 'A'][opposite_pit] = 0

        # If we made it through all that, we successfully made our move, so we'll switch the active player and confirm the move was made.
        self.switch_player()
        return True
            

    def is_game_over(self):
        # This function checks if all pits on one side of the board are empty, 
        # signifying the end of the game.
        return all(value == 0 for value in self.board['A'][:6]) or all(value == 0 for value in self.board['B'][:6])

    def declare_winner(self):
        # At the end of it all, we need to declare a winner!
        # The player with the most stones in their mancala at the end of the game wins!
        if self.board['A'][6] > self.board['B'][6]:
            return 'Player A wins!'
        elif self.board['A'][6] < self.board['B'][6]:
            return 'Player B wins!'
        else:
            return 'It is a draw!'

# This is the end of your Mancala game roller coaster ride! 
# We hope you enjoyed and learn something cool today! Happy Coding!
