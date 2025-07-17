
# Distance3DCalculator.py
# Put on your space suits because we're about to take off into the 3-D space!

# How exciting is that! Using the power of Pythagorean theorem in three dimensions,
# we can calculate the distance between any two points in this space. 

# Importing the math module. No bells and whistles. Simply out of the box, old good Python stuff!
import math

def calculate_3D_distance(point1, point2):
    """Computes and returns the 3D distance between two points."""
    # Whoa! Did you know that distance in 3D space is calculated using Pythagoras theorem.
    # But this time it's multiple dimensions. Three to be precise!

    # Difference in x coordinates.
    dx = point2[0] - point1[0]

    # Keeping up, are you? Now let's do the same for y coordinates.
    dy = point2[1] - point1[1]

    # And z. We're in 3D remember?
    dz = point2[2] - point1[2]

    # Pythagoras would be so proud! Squaring the differences.
    dx_sq = dx ** 2
    dy_sq = dy ** 2
    dz_sq = dz ** 2

    # Time to sum up squares.
    sum_of_squares = dx_sq + dy_sq + dz_sq

    # Finally, let's find square root of the sum. That's our distance in 3D space. *Mind Blown*
    distance = math.sqrt(sum_of_squares)

    return distance

def main():
    # Let's test our function with example points.
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)

    # Call the function and store the result.
    distance = calculate_3D_distance(point1, point2)

    # Print the result.
    print(f"The distance between {point1} and {point2} is {distance} units.")

# Standard boilerplate for calling the main() function.
# Because if we don't call our function, who will!
# Python's __name__ attribute let's us check whether we are running as a standalone script or being imported.
if __name__ == "__main__":
    main()

