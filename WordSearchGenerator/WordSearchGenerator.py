
# WordSearchGenerator.py
# Hello fellow programmers, buckle up! We're about to embark on a thrilling adventure.
# This script will create a fascinating word search puzzle from a pool of selected words.
# And of course, it's simple, convenient and can run entirely from your command line. Let's rock!

import random
import string

# Set the grid size - feel free to change this later
GRID = 10

def generate_grid():
    '''Generate a 2D list filled with random letters'''

    # Howdy! Here we prepare a grid filled with random letters - isn't it fun already?
    return [[random.choice(string.ascii_uppercase) for _ in range(GRID)] for _ in range(GRID)]

def place_words(grid, words):
    '''Fill the grid with words'''

    # It's time to scatter our precious words across the grid
    for word in words:
        word_length = len(word)
        if word_length > GRID:
            continue

        # We pick a random starting point
        start_x = random.randint(0, GRID - 1)
        start_y = random.randint(0, GRID - 1)

        # We place the word on the grid
        if start_x + word_length <= GRID:
            for i in range(word_length):
                grid[start_y][start_x + i] = word[i]
        elif start_y + word_length <= GRID:
            for i in range(word_length):
                grid[start_y + i][start_x] = word[i]

def print_grid(grid):
    '''Pretty print the grid'''

    # Just like Christmas lights, but it's our word puzzle grid lighting up the console!
    for line in grid:
        print(" ".join(line))

def main():
    # We define some beautiful words to fill in our puzzle.
    # You can change the word list to your liking.
    words = ["APPLE", "ORANGE", "BANANA", "PEAR", "CHERRY"]

    # Generate a random grid
    grid = generate_grid()

    # Place words in the grid
    place_words(grid, words)

    # Now, the magical moment - let's reveal the masterpiece to the world!
    print_grid(grid)

# Code entrance
if __name__ == "__main__":
    main()
# And we're done! You have just created a splendid word search puzzle.
# Run this script, have fun and stay awesome, coder!
