
# Alright folks, buckle up! It's time for some fun with mathematics and Python!
# Heptagonal numbers. Sounds pretty cool, right? Let's check them out.
# Lemme tell you something about Heptagonal numbers: They are figurate numbers, 
# meaning they can be represented by a regular geometric arrangement of equally spaced dots. 
# They are given by the formula: n(5n - 3) / 2

# This file is a CLI Python program that checks whether a given number is a Heptagonal number.

# Our environment? A fresh Python install on a new computer. No GUI. No API. No Internet. Just raw Python power!

# First things first - let's get some input from the user

import sys

# Checking command line arguments
if len(sys.argv) != 2:
    print("Usage: python HeptagonalNumberChecker.py <number>")
    sys.exit()

# We've been given some number. First, make sure it's actually a number
try:
    num = int(sys.argv[1])
except ValueError:
    print("That's not a valid number buddy!")
    sys.exit()

# Let's jump straight into the mathematics. The formula to find the nth Heptagonal number is n(5n-3)/2

# A helper function that checks if a number is a Heptagonal number using inverse function
# we solve n(5n - 3)/2 = num for n and round off to the nearest integer. Then, we use the integer to 
# calculate the Heptagonal number again. If it matches the original, it's a Heptagonal number.

def is_heptagonal(num):
    n = round((1 + ((24*num + 1)**0.5))/10)
    return num == n*(5*n - 3)//2

# Now, let's use our function to check if the number is Heptagonal number
if is_heptagonal(num):
    print("Wow, you've got yourself a Heptagonal number there!")
else:
    print("Sorry mate, that's not a Heptagonal number!")
