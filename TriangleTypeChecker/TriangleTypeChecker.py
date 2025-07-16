
# Well, hello there! Get ready for some fun with geometry. Today, we're going to write a Python program that'll tell us if three sides could form
# a right, acute, or obtuse triangle. Sounds cool, right? Let's dive in!

# First, we'll need a function to find out the type of the triangle
def triangle_type(a, b, c):
    # All right! We're going to use the given sides lengths to determine the type of triangle.
    # Buckle up, this will be a fun ride!

    # First, we have to sort the sides lengths to make our calculations easier.
    # Whoops! Looks like we've stumbled upon a clever Python "hack" here. The function sorted() helps us to do the job.
    a, b, c = sorted([a, b, c])

    # Now let's check if the sum of the squares of the two smaller sides equals the square of the longest side
    # If it does, then we've found ourselves a right triangle! (Thanks, Pythagoras!)
    if a**2 + b**2 == c**2:
        return "Right triangle"

    # If the sum of the squares of the two smaller sides is greater than the square of the longest side, then the triangle is acute.
    elif a**2 + b**2 > c**2:
        return "Acute triangle"

    # If none of the above is true, then the triangle must be obtuse.
    else:
        return "Obtuse triangle"

# Now for the command line interface part. Here, we'll make use of Python's built-in 'argparse' library to command line arguments
import argparse
parser = argparse.ArgumentParser(description='Determine the type of triangle based on three side lengths.')
parser.add_argument('sides', metavar='S', type=float, nargs=3,help='lengths of the sides of the triangle')

args = parser.parse_args()

# Now we simply call our function on the inputs given from the command line!
print(triangle_type(*args.sides))

# And that's it! We've just created our very own triangle detector! Isn't Python just amazing? Happy coding folks!
