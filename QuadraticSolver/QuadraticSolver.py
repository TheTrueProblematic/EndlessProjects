
# Hey! Welcome to Quadraticsolver, a fun, simple, and compact program written in python.
# If quadratic equations make you feel like you're trying to decipher alien language,
# don't worry, esteemed friend 
# because this program's got you covered! 

# Let's get right to it!

# We'll need the math module to perform square root operations  
import math 

# Function to find the roots of any quadratic equation.
# A quadratic equation is of the form ax^2 + bx + c
# where 'a', 'b', 'c' are coefficients
# The roots of the quadratic equation can be found using the quadratic formula: (-b ± sqrt(b^2 - 4ac))/2a
def find_roots(a, b, c):
    # Calculate the discriminant
    disc = b**2 - 4 * a * c
    
    # If discriminant is less than 0, the roots are complex,
    # and cannot be calculated in normal realm.
    if disc < 0:
        return "Complex Roots", "Complex Roots"
    
    # If discriminant is greater than or equal to 0, 
    # the roots can be real and can be calculated as follows
    root1 = (-b + math.sqrt(disc)) / (2 * a)
    root2 = (-b - math.sqrt(disc)) / (2 * a)
    
    # return the roots
    return root1, root2

# Coefficients are hard coded here for simplicity sake.
# You can consider using `input` function to take coefficients
# from standard input in order to solve different equations without changing the code.
a = 1
b = 2
c = -8

# Let's rock and roll!
root1, root2 = find_roots(a, b, c)

# Aha! We found the roots! Let's print the results!
print("The roots of the equation are : ", root1, root2)

# There you have it! 
# A simple python script to help you solve quadratic equations!
# Now wasn't that a joy ride?
# Feel free to use, play, and modify this program as you like.
# Happy Coding!

