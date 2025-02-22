
# Hey there, fellow coder! This script simulates a random walk on a 2D grid. 
# Let us embark on a journey full of random turns and twists, shall we? 

# First off, we're gonna need the random module to make our steps unpredictable!
import random

# Now, we set the initial co-ordinates of our walk. We'll start right in the middle of our grid, at (0,0).
x, y = 0, 0 

# Let's set a limit to our wanderings, shall we? We wouldn't want to be lost forever!
num_steps = 5000

# Time to take a walk!
for i in range(num_steps):

    # By using random.choice, we tell our walker to choose a random direction each time. North, south, east, or west.
    direction = random.choice(['N', 'S', 'E', 'W'])

    # If our random choice is N (north), increase the y coordinate by one.
    if direction == 'N':
        y += 1
    # If our random choice is S (south), decrease the y coordinate by one.
    elif direction == 'S':
        y -= 1
    # If our random choice is E (east), increase the x coordinate by one.
    elif direction == 'E':
        x += 1
    # If our random choice is W (west), decrease the x coordinate by one.
    else:  # direction == 'W'
        x -= 1

    # Now, let's print out where we are after every random step.
    print("Step {}. Location: ({},{})".format(i+1, x, y))

# After the walk, print the final location!
print("This sure was a crazy walk! Our final location is: ({}, {})".format(x, y))

# Phew! There we have it folks! A nice, simple random 2D walk simulation! Try playing with the number of steps 
# or imagining what the path looks like! Fun, isn't it?

