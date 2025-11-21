# Here's the python code for our fun Forest Fire Simulation:


# Let's the party start, we're simulating a forest fire! Sounds scary, right?
# No worries, it's all virtual. Happy coding!

import random # To light the initial fires.

# The width and height of our forest. Feel free to make it as large as you want!
forest_width, forest_height = 100, 100 

# Define the 'density' of the forest.
forest_density = 0.60

# How fast our fire spreads. Higher numbers will make the fire spread faster!
spread_rate = 0.25

# Let's start with an empty grid for the forest.
forest = []

def initial_fire():
    # Let's populate our forest with trees and...fire! Oh no!

    for y in range(forest_height):
        row = []

        for x in range(forest_width):
            # If a random number is less than forest_density, we add a tree.
            # Else, it's empty space... for now! Fire could come soon!
            row.append(1 if random.random() <= forest_density else 0)

        forest.append(row)

    # Let's light the initial fires on the edge of the forest. Burn, baby, burn!
    for i in range(forest_width):
        if forest[0][i] == 1:
            forest[0][i] = 2  # 2 represents a burning tree. It's getting hot in here!


def fire_spread():
    # Fire does not stop on its own, does it? Let's simulate that!

    for y in range(1, forest_height):
        for x in range(forest_width):

            # If the tree is already burnt or if there's no tree at all, we skip this spot.
            if forest[y][x] != 1:
                continue

            # Here we check if the previous line has fire to spread.
            if forest[y-1][x] == 2 and random.random() <= spread_rate:
                forest[y][x] = 2

            # If not, we should also check the previous spots in the line.
            elif x > 0 and forest[y][x-1] == 2 and random.random() <=spread_rate:
                forest[y][x] = 2

def main():
    # Everything starts here!

    initial_fire()
    while True:
        fire_spread()
        print('\n'.join(''.join('.' if cell == 0 else 'T' if cell == 1 else 'F' for cell in row) for row in forest))

        # Oh wait, we need some time to see the fire spreading. Let's take a break!
        input("Press Enter to Continue...")

if __name__ == "__main__":
    main()

# There you go! You've created an exciting, albeit terrifying, Forest Fire Simulator. Enjoy watching...safely!
Remember, only YOU can prevent forest fires - both virtual and real ones. Happy coding!