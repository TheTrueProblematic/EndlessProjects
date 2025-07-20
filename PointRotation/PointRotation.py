
# PointRotation.py
# Hey there, cheerful coder! Welcome to our fun and awesome PointRotation project. 
# We're creating a rad script that performs a cool task of rotating a point around the origin by a certain angle. Just like a rollercoaster ride, yeah?

import math

# Here, we'll define a function that accepts a point and the angle by which it should be rotated.
# Why two parameters, you ask? Well, the point is the passenger on our ride, and 
# the angle is how many spins that passenger will get!

def rotate_point(point, theta):
    """
    Rotates a point around the origin (0,0) by theta degrees.
    """
    theta_rad = math.radians(theta)  # Conversion to radians, because our sine and cosine buddies work with radians!

    x = point[0]  # Let's ease things up by unpacking
    y = point[1]  # our coordinate pair. Hello, X and Y!

    # Now, we get to the actual magic, the rotation transformation. Fasten your seatbelts! 
    rotated_x = x * math.cos(theta_rad) - y * math.sin(theta_rad)
    rotated_y = x * math.sin(theta_rad) + y * math.cos(theta_rad)

    # We return the coordinates of our point after the wild ride.
    # Revised, refreshed and rotated!
    return (rotated_x, rotated_y)

# We're all set and ready to provide some thrilling but precise rotations. So, get your coordinates and angles ready and let's take 'em for an exhilarating spin in the Python World!

