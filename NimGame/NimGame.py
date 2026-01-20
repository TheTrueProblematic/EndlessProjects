
# Hey there, happy programmer! Welcome to this super fun implementation of the mathematical game of Nim!
# In this game, you and the computer take turns removing sticks from a pile. The player who picks up the last stick loses the game.

def nim_game():
  # First, we need a pile of sticks. Let's start with 21.
  num_sticks = 21

  # Welcome the player and explain the rules
  print("Welcome to the game of Nim! Start with a pile of 21 sticks. You and the computer take turns, and each turn you can take 1-4 sticks. The player who takes the last stick loses.")

  # Pick a random number between 1 and 4 to decide which player goes first
  import random
  player_turn = random.randint(1, 2)

  # Now, it's time to play the game!
  while True:
    print("Number of sticks left: ", num_sticks)
    # Check if current player is human or AI
    if player_turn == 1:
      # It's the human's turn
      print("Your turn!")
      while True:
        try:
          # Take user input for number of sticks to be removed
          num_remove = int(input("Enter number of sticks to remove (1-4): "))
          # If the number is between 1 to 4 (inclusive) and less-or-equal to num_sticks, we're good to go
          if (num_remove >= 1) and (num_remove <= 4) and (num_remove <= num_sticks):
            break
          else:
            print("Invalid number. Try again.")
        except ValueError:
          print("Invalid number. Try again.")
          
    else:
      # It's the AI's turn
      print("AI's turn!")
      # AI is designed to play optimally, according to the Winning Strategy for Nim
      # We want the number on the pile to be a multiple of (m+1) = 5 where m is the maximum number can be removed (4 in our case).
      # So, AI should play (number_sticks % (m+1)).
      num_remove = num_sticks % 5
      # If num_remove becomes zero, then remove only one stick
      if num_remove == 0:
        num_remove = 1
      print("AI removes", num_remove, "stick(s)")
      
    # After player's/ AI's turn, update the pile
    num_sticks -= num_remove

    # Player turn finished, now it's opponent's turn
    player_turn = 1 if player_turn == 2 else 2

    # If there is no stick left after a player's turn, the other player wins
    if num_sticks == 0:
      winner_player = 'You' if player_turn == 2 else 'AI'
      break
  
  # And finally, announce the winner!
  print(winner_player, " wins the game!")
  

if __name__=='__main__':
  nim_game()

