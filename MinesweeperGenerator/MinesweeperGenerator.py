
# Hey there, happy coder! Get ready to dive into this jolly bunch of code that generates a Minesweeper grid.
# We will make this as snappy and easy as a walk in the park. Let's get into it!

import random

def generate_minesweeper_grid(rows, columns, mine_density):

    # First things first, we calculate the approximate number of mines.
    mine_count = int(rows * columns * mine_density)

    # Let's create an empty grid first where '0' represents a free spot and 'M' a mine.
    grid = [['0' for _ in range(columns)] for _ in range(rows)]

    # Boom! Time to place the mines! It's like planting flowers in a digital field.
    for _ in range(mine_count):
        while True:
            x, y = random.randint(0, rows-1), random.randint(0, columns-1)
            if grid[x][y] != "M":  # If the spot is free, we bless it with a mine.
                grid[x][y] = 'M'
                break

    # Great! Now let's count the neighboring mines for each spot. Minesweeper rules, you know!
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] != "M":
                # We look around each spot (top, bottom, left, right and the 4 diagonals) for friends (mines).
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    nx, ny = i+dx, j+dy
                    if (0 <= nx < rows) and (0 <= ny < columns) and grid[nx][ny] == "M":
                        # We have a friend nearby! Increase the counter.
                        grid[i][j] = str(int(grid[i][j]) + 1)

    return grid

# Let's test this fun generator!
grid = generate_minesweeper_grid(5, 5, 0.2)
for row in grid:
    print(' '.join(row))

# There you have it, friend! A console-based Minesweeper grid generator.
# Hope you enjoyed this trip as much as I did! Happy coding!


