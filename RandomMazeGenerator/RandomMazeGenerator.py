"""
Hey there lovely programmer or curious friend who is reading through the code! 🌟

I'm your not so ordinary RandomMazeGenerator, made up of pure Python code. 🐍

I won't use any kind of internet, not an API call or anything that requires internet connection! 🌐

I won't be needing any dependencies, no installs (apart from Python ofc), no downloads needed. Just pure, clean Python! 📦

Let's Go! 🥳
Be ready to get lost... just kidding... 😁
"""

import random

# Let's start by defining our maze. To make it simple let's use a 2D matrix. 🏁
def create_maze(width, height):
    maze = [['#' for x in range(width)] for y in range(height)]  # Creating the maze boundary with Walls
    starting_point = (1, 1)  # We can start at this point

    # Visited cells will be stored here
    visited_cells = set()
    visited_cells.add(starting_point)

    # Steps for moving around
    all_directions = ['N', 'S', 'E', 'W']

    # Start wandering around 🚶‍♂️
    wander_around(maze, visited_cells, starting_point, all_directions)

    return maze


# Now we start wandering! 🎒
def wander_around(maze, visited_cells, current_cell, all_directions):
    # Making a copy so we can shuffle without affecting the original
    directions = all_directions[:]

    random.shuffle(directions)  # let's randomly choose the direction we are going next

    # Start moving! Let's explore... 🕵️‍♂️
    for direction in directions:
        new_cell, middle_cell = get_new_cell(current_cell, direction)

        if not is_valid(new_cell, maze) or new_cell in visited_cells:
            continue

        # Oh look, we found a new cell! Let's add it to our visited cells
        visited_cells.add(new_cell)
        maze[middle_cell[1]][middle_cell[0]] = ' '
        maze[new_cell[1]][new_cell[0]] = ' '

        # Now let's go for a walk in this direction 🚀
        wander_around(maze, visited_cells, new_cell, all_directions)


# Now let's get the cell that comes after taking a step in a direction from the current cell 🦶
def get_new_cell(current_cell, direction):
    x,y = current_cell

    # This is like a map, or a guide on where to go, or step, next.
    # N is North (up), E is East (right), S is South (down), W is West (left)
    offsets = {'N': (0, -2), 'S': (0, 2), 'E': (2, 0), 'W': (-2, 0)}

    dx, dy = offsets[direction]
    new_cell = (x + dx, y + dy)
    middle_cell = (x + dx//2, y + dy//2)

    return new_cell, middle_cell


# Let's check if we are still within the maze boundaries 🧭
def is_valid(cell, maze):
    x, y = cell
    return 0 < x < len(maze[0]) and 0 < y < len(maze)


# Ok, enough of wandering. Let's print the maze! 🖨️
def print_maze(maze):
    print('\n'.join([''.join(row) for row in maze]))


# Here we go... Get ready to unleash the maze! 🔥
def main():
    maze = create_maze(41, 41)  # You can adjust this to get a maze as big as you like!
    print_maze(maze)


# Hope, you enjoyed the maze ride 😎
if __name__ == "__main__":
    main()
