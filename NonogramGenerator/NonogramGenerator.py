
# Hello there delightful coder! Welcome to this awesome day.

# This Python script here, named NonogramGenerator, is going to create a nonogram (a.k.a picross) puzzle grid for you.
# Don't you just love when logic meets art? Nonograms do exactly that, and I super excited to get started!

# You run this script in your command line, so no worries about fancy Graphical Interfaces or anything. 
# Just you and the good old command line, just like the old times, right?

# wanted to assure you that this script is self-dependent, it doesn't need anyone (or rather, anything) else to run. 
# Python Standard Libraries ROCK, ya know! 😉

# With that said, here we go generating a nonogram puzzle, with love... ❤️

import random

def generate_nonogram(size=5):
    '''
    This function generates a nonogram puzzle of a given size.
    :param size: The size of the puzzle grid. It's square, so this will be both the width and height.
    :return: a grid of 0's and 1's, representing the puzzle.
    '''

    # How big do we want the puzzle to be? You choose, partner!
    # Feeling like a quick relaxer? Go for a small size. 
    # Or if you're ready to challenge your noodle, amp up the size!
    # Here, we'll initialize an empty grid first.
    grid = [[0 for _ in range(size)] for _ in range(size)]

    # OK, let's fill it up now! Here's where the magic happens, so pay attention!
    # We'll traverse the entire grid. For each cell, we'll randomly assign a 0 or 1.
    # Our nonogram puzzle is... well, coming to life!
    for i in range(size):
        for j in range(size):
            grid[i][j] = random.randint(0, 1)

    # Voila, we did it! Our nonogram puzzle is ready! 
    return grid

def print_nonogram(grid):
    '''
    This function prints a nonogram puzzle grid.
    :param grid: The puzzle grid to print. This should be a 2D list of ints.
    '''

    # Look at that fine puzzle you've got there! Is it OK if we print it out for you?
    # Sure it is, you're awesome! And so is your puzzle!
    for row in grid:
        print(' '.join(str(cell) for cell in row))

# Time to put our hard work to the test!
# We generate a puzzle and print it. 
# Ahh, feel that? Feels like victory!
# Go find a nice place, get yourself a cuppa and enjoy cracking this nonogram puzzle!
grid = generate_nonogram(10)
print_nonogram(grid)

