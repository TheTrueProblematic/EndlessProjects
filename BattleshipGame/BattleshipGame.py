
# Ahoy there, matey! We are going to have a blast creating a classic Battleship game to play in the command line. 
# Get ready for a fun adventure against the wily computer!

import random

# Let's start with creating the board. We'll use a list of lists to do this.
board = []

# Seven seas! But a 5x5 grid is enough for our battleship game, mate!
for x in range(0, 5):
  board.append(["O"] * 5)

# Now let's fashion a function to print our board out in a neat and tidy way.
def print_board(board):
  for row in board:
    print(" ".join(row))

# To add a sense of suspense, we'll initially hide the enemy ship.
def random_row(board):
  return random.randint(0, len(board) - 1)

def random_col(board):
  return random.randint(0, len(board[0]) - 1)

# Shiver me timbers! Let's hide our enemy ship in a random location
ship_row = random_row(board)
ship_col = random_col(board)

# Blimey! Now for the game loop. 
# We give the player 4 turns to find the ship.
for turn in range(4):

  print("\nTurn", turn + 1)
  # We print the board at the beginning of each turn.
  print_board(board)

  # We ask the player for their guess.
  guess_row = int(input("Guess Row (0-4):"))
  guess_col = int(input("Guess Col (0-4):"))

  # If they're super lucky and find the ship, we congratulate them!
  if guess_row == ship_row and guess_col == ship_col:
    print("\nCongratulations! You sank my battleship!")
    break
  else:
    # We give them another chance if they guessed a location that's even on the board.
    if guess_row not in range(5) or guess_col not in range(5):
      print("\nOops, that's not even in the ocean.")
    # Or if they guess a location they've already guessed.
    elif board[guess_row][guess_col] == "X":
      print("\nYou guessed that one already.")
    # Otherwise, they simply miss and we mark their guess on the board.
    else:
      print("\nYou missed my battleship!")
      board[guess_row][guess_col] = "X"

    # Game over if the player has taken all 4 turns.
    if turn == 3:
      print("\nGame Over")

# After the game ends, we reveal the location of our battleship.
print("\nMy ship was at Row: {} Col: {}". format(ship_row, ship_col))

