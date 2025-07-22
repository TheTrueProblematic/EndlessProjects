
# Welcome to VectorMagnitude.py! This is a fun little project designed to calculate the magnitude of a vector in n‑dimensional space.
# Who knew numbers and dimensions could be so much fun, right?

# We're going to need math for this. No need to worry, even if numerals aren't your strong suit. Math is doing all the heavy lifting here!
import math

# Our main function, called calculate_magnitude, does exactly what it says on the tin.
def calculate_magnitude(vector):
    """Calculate the magnitude of a vector in n‑dimensional space."""
    # First, we square each component of the vector. It's like giving the components a second power boost! 
    squared_components = [i ** 2 for i in vector]
    
    # Next, we add them all up to get the sum of the squares. It's getting interesting, isn't it?
    sum_of_squares = sum(squared_components)
    
    # And at last, we take the square root of that sum to get the magnitude. And... voila! We got the result. Didn't know you were so good with numbers, did you?
    magnitude = math.sqrt(sum_of_squares)
    
    # Finally, our function returns the calculated magnitude. It's yours to do with it whatever you want! Sky's the limit, friend!
    return magnitude

# Let's put our function to work! We'll define a vector right here in our script.
# You can, of course, modify this to suit your needs. This is just to make sure everything is working as expected.
vector = [3, 4, 0]

# Now, drum roll, please... We're going to calculate the magnitude of our vector.
magnitude = calculate_magnitude(vector)

# Let's print out the result so we can revel in the glory of our mathematical prowess! And hey, it's something to brag about at parties. Who wouldn't be impressed?
print(f"The magnitude of the vector {vector} is {magnitude}")

# See? Vectors and dimensions are fun. And they said math couldn't be cool. Until next time, happy vectoring!

