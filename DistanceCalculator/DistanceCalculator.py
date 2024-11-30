
# Hello fellow Pythonista! This short and sweet script here is a "Distance Calculator".
# It's designed to calculate the distance between two points on our beautiful (but flat in this case) Earth. 

# We're all about portability here, aren't we? That's why this script is dependency-free. 
# No installations, no obscure libraries, and definitely...no internet! This baby runs offline. 

# And guess what? It's a command-line interface script, a real back to the basics kind of program. 
# Just run it, input your points, and get your distance.

import math

def calculate_distance(x1, y1, x2, y2):
    # Our handy-dandy helper function here calculates the Euclidean distance between two points
    # Math is so cool, right?

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    # Welcome to the main program! Let's get those points' coordinates.
    print('Hello! Please provide coordinates for two points (x and y).')

    x1 = float(input('Enter x for the first point: '))
    y1 = float(input('Enter y for the first point: '))
    x2 = float(input('Enter x for the second point: '))
    y2 = float(input('Enter y for the second point: '))

    distance = calculate_distance(x1, y1, x2, y2)

    # Voila! Here's your distance.
    print('The distance between points ({}, {}) and ({}, {}) is {:.2f}'.format(x1, y1, x2, y2, distance))

# Time for action! Let's run this program.
if __name__ == "__main__":
    main()

