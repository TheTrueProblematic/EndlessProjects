
# Hello there fellow coder! Welcome to the BearingCalculator.py file :D
# This python script is designed to get the bearing angle between two sets of geographical coordinates.
# It's a CLI-tool, so no fancy GUI to distract you.
# Just remember to feed in two coordinates and it will give you the bearing angle. How cool is that?
# And the best part? No dependencies or internet access needed!

# Alright, without further ado, let's dive into the magical world of code!!!

# We will need two python in built libraries for our work today
import math
import sys

# Function to convert degrees to radians because math operations in python work with radians. 
def degrees_to_radians(degrees):
    return degrees * math.pi / 180.0

# Function to calculate the bearing angle
def get_bearing(lat1, lon1, lat2, lon2):
    
    # First thing we do is to convert the latitude and longitude values to radians
    lat1 = degrees_to_radians(lat1)
    lon1 = degrees_to_radians(lon1)
    lat2 = degrees_to_radians(lat2)
    lon2 = degrees_to_radians(lon2)
    
    # Now, we use the fancy maths to get the bearing angle. Don't worry if you don't get it at first, it's all in the math :D
    diff_lon = lon2 - lon1
    x = math.cos(lat2) * math.sin(diff_lon)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(diff_lon)
    
    # We convert our result back to degrees since that's easier to understand for us normal folks
    bearing_angle = math.atan2(x,y)
    bearing_angle = bearing_angle * (180.0 / math.pi)
    
    # We are rounding the result to two decimal points because precision is key!
    return round(bearing_angle, 2)

if __name__ == '__main__':
    
    # Checking if the user has inputed enough coordinates for our calculation
    if(len(sys.argv) < 5):
        print("Please provide two sets of geographic coordinates!")
        sys.exit(1)
    
    # We fetch the coordinates from the command line arguments. Isn't python neat?
    lat1 = float(sys.argv[1])
    lon1 = float(sys.argv[2])
    lat2 = float(sys.argv[3])
    lon2 = float(sys.argv[4])
    
    # Now we calculate the bearing angle using our get_bearing function and print it out for the user
    bearing = get_bearing(lat1, lon1, lat2, lon2)
    print(f'The bearing angle between the two set of geographic coordinates is {bearing} degrees.')
    
# Voilà! That's all folks! Keep on coding and having fun!
