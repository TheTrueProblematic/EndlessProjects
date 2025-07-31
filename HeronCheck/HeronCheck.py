
# Let's have some fun with some great old Greek math! Welcome to my HeronCheck script!

import math  # Hey! We gotta do maths here

def calculate_triangle_area(a, b, c):
    ''' 
    Use this function to calculate the area of a triangle using Heron's formula.
    Heron's formula allows you to calculate the area of a triangle if you know the length of all three sides.
    '''

    # First, we need to calculate the semi-perimeter of our triangle
    s = (a + b + c) / 2

    # Now let's use Heron's formula to calculate the area
    # What a genius that Heron guy was!
    # Notice that we use our awesome "math" module to calculate square root
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # returns the calculated area
    return area

def heron_check():
    ''' 
    Let's calculate area of some triangles using Heron's formula to test if it works correctly.
    '''

    # Let's compute the area of a triangle with sides of lengths 3, 4, and 5
    print(f"Area: {calculate_triangle_area(3, 4, 5)} square units.")

    # Now let's compute the area of a triangle with sides of lengths 5, 12, and 13
    print(f"Area: {calculate_triangle_area(5, 12, 13)} square units.")

    # How about the area of a triangle with sides of lengths 7, 24, and 25?
    print(f"Area: {calculate_triangle_area(7, 24, 25)} square units.")

# This is where we start our program.
if __name__ == "__main__":
    print("Welcome to HeronCheck! Hold on to your hats as we do some ancient Greek maths!")
    heron_check()

