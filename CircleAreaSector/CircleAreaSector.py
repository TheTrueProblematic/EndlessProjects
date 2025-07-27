
# Hello there, glad to see you having fun with Python! :)
# In this script, we're going on a little geometry adventure to calculate the area of a sector in a circle.

# Python's coming packed with a lot of goodies, and one of them is the 'math' module. 
# We don't need to install anything at all to use it (how convenient is that?) and it has our good friend Pi. 
import math

# Now, let's get on with our calculation. We'll define a function so you can re-use it whenever needed.
# Who said math can't be fun? 

def calculate_sector_area(radius, angle):
    '''
    Function to calculate the area of a sector.
    It requires radius (the distance from the center to the edge of the circle),
    and angle (the angle subtended by the sector at the center of the circle).
    Make sure to input angle in degrees!
    ''' 
    # Convert angle in degree to radian because Python trigonometric function uses radian
    angle_in_radian = math.radians(angle)

    # Now let's calculate the area of our sector. Trust me, it's easier than it sounds.
    # It's basically (angle/360) * (pi * radius^2). 
    # Yes, that's all there is to it. Amazing, right?
    # The fun thing is, we're instructing the computer to do the calculation for us.
    sector_area = (angle_in_radian / (2 * math.pi)) * (math.pi * radius * radius)
    
    # Now we return the area we just calculated.
    # Python will just replace the function call with this value. Super useful!
    return sector_area

# Let's test our function with some values
# You can replace these values with your own
radius = 10
angle = 90

# Now we call our function and print the result.
# Look, no hands! The computer's doing all the work for us! :)
print("The area of the sector is: ", calculate_sector_area(radius, angle))
# Happy Coding!!

