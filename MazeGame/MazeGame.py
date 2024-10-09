
# Welcome to our super fun MazeGame python script! Oh what joy programming brings us!
# Pour yourself a cup of hot cocoa, we're going on a coding adventure!

# HUD (Heads-Up-Display) to help show the player where they are
def draw_map(player):
    print('-------')
    for cell in MAZE:
        if cell == player:
            print('X', end='')
        else:
            print('O', end='')
    print('\n-------')

# Check if the entered move is possible
def is_move_possible(player, direction):
    new_player = player + direction
    if new_player<0 or new_player>=len(MAZE):
        return False  # hit the boundaries of our maze
    if MAZE[new_player] == 1:
        return False  # hit a wall
    return True

# Assign numerical values to movement commands
def get_direction(command):
    if command == 'left':
        return -1
    elif command == 'right':
        return 1
    else:
        return 0

# Create our maze rooms! O is an open space, and 1 is a wall.
MAZE = [0, 0, 1, 0, 0]
player = 0
end = 4

# Start of this adventure!
while True:
    draw_map(player)

    # Checking if the player has reached the goal room
    if player == end:
        print("Congratulations, you escaped the maze! Woohoo!")
        break

    command = input("Enter your move (left/right): ")

    # Make a move only if it's possible, else laugh and move on!
    direction = get_direction(command)
    if is_move_possible(player, direction):
        player += direction
    else:
        print("Ha! Nice try, but you can't move that way! Try another direction!")

    print()  # because who doesn't love an organized console display!
