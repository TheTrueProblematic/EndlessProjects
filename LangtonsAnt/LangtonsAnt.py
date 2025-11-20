
# Wahoo! Let’s go on a little adventure with our buddy, Langton's Ant!
# We'll be simulating this neat little automaton on a grid.
# The ant can move either ‘N’ (North/up), ‘E’ (East/right), ‘S’ (South/down) or ‘W’ (West/left).
# It takes a step forward in the direction it’s facing, and then turns either left or right, depending on the color of the square.
# The best part? All of this happens directly on the command line. Let's dive right in!

def main(grid_size):
    # We start with a grid full of 0's, out little ant at the middle facing up
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    # Our ant's current position in the middle
    ant_x, ant_y, ant_direction = grid_size // 2, grid_size // 2, 'N'

    while True:  # The magic happens in this little loop
        # Each step, if we land on a white square (0), we flip it to black (1), turn right, and step forward
        if grid[ant_y][ant_x] == 0:
            grid[ant_y][ant_x] = 1
            ant_direction = turn_right(ant_direction)
        else:  # On a black square, we flip it to white, turn left and step forward
            grid[ant_y][ant_x] = 0
            ant_direction = turn_left(ant_direction)

        # Stepping forward in the new direction
        ant_x, ant_y = move_forward(ant_x, ant_y, ant_direction, grid_size)

        # Show process each step on grid
        show_grid(grid, ant_x, ant_y, ant_direction)


def turn_right(direction):
    return {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]  # A neat way to 'turn right'


def turn_left(direction):
    return {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}[direction]  # Similarly clever way to 'turn left'


def move_forward(x, y, direction, size):
    if direction == 'N':
        y = max(0, y - 1)  # We hit a wall, no passing through, bouncing back
    elif direction == 'S':
        y = min(size - 1, y + 1)  # Same here
    elif direction == 'E':
        x = min(size - 1, x + 1)  # And here
    elif direction == 'W':
        x = max(0, x - 1)  # And finally here
    return x, y  # Our new position after taking a step forward


def show_grid(grid, ant_x, ant_y, direction):
    print("\n" + direction)  # Print the current direction the ant is facing
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # We'll print the ant as an X, and the grid as # for black squares, . for white squares
            print('X' if (x == ant_x and y == ant_y) else '#' if cell else '.', end='')
        print()


if __name__ == '__main__':
    main(50)  # Start the party with a reasonably sized grid

