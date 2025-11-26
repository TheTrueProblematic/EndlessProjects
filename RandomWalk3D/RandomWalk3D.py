
# Hey there, Pythonistas!
# Welcome to our little 3D Random Walk simulator!
# This project simulates a random walk in three dimensions (ooh! advanced stuff!)
# And also calculates the distance our 'walker' has traversed from the origin point.
# All this, with no GUI, no external dependencies, no API, no internet access!
# This script's as lightweight as a feather!
# Now, Sit back, relax and let's start walking...randomly of course!

import random
import math

# Our 3D coordinate system initialization...
x, y, z = 0, 0, 0

# Number of steps we want the walker to take...
steps = 100000

# Now we walk for the specified steps...
for _ in range(steps):
    # Selecting random direction - X, Y or Z
    direction = random.choice(['x', 'y', 'z'])
    
    # Forward or backward?
    movement = random.choice([-1, 1])
    
    # Moving in the selected direction
    if direction == 'x':
        x += movement
    elif direction == 'y':
        y += movement
    elif direction == 'z':
        z += movement

# Now, let's calculate the distance from origin after our random stroll!
# Using 3D Pythagorean theorem, the square of the distance from origin would be x² + y² + z².
distance = math.sqrt(x**2 + y**2 + z**2)

# Finally, we print the distance our random walker has covered.
print("After", steps, "steps, the walker is approximately", round(distance, 2), "steps away from the origin.")

# And that's it! A super-simple 3D random walk simulator! Cool, isn't it?
# Remember, sometimes the solutions to complex problems is a whole bunch of simple steps executed randomly ;)
# Alright then, Happy Coding!

