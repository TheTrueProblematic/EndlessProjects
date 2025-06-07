
# Yay, welcome to the fun AngleConverter program! 
# This program is gonna be a blast, it's all about converting angles.
# We're going to convert between degrees, radians, and gradians. Wooohoooo! Let's get started!

import math

# Alright-okay, time to define functions for converting angles, one for each conversion.

# Conversion from degrees to radians. Piece of cake!
def deg_to_rad(angle_in_degrees):
    # There are 2 * pi radians in a circle, same as 360 degrees. Let's use that!
    angle_in_radians = angle_in_degrees * (math.pi / 180)
    return angle_in_radians

# Conversion from degrees to gradians. Easy-peasy!
def deg_to_grad(angle_in_degrees):
    # There are 400 gradians in a circle, same as 360 degrees. Fun facts!
    angle_in_gradians = angle_in_degrees * (400 / 360)
    return angle_in_gradians

# Conversion from radians to degrees. No sweat!
def rad_to_deg(angle_in_radians):
    # We've done this conversion before, but the other way around. Time for some deja vu!
    angle_in_degrees = angle_in_radians * (180 / math.pi)
    return angle_in_degrees

# Conversion from radians to gradians. You're doing great!
def rad_to_grad(angle_in_radians):
     # Remember the fun fact? Let's take it for a spin!
    angle_in_gradians = rad_to_deg(angle_in_radians) * (400 / 360)
    return angle_in_gradians

# Conversion from gradians to degrees. Keep going!
def grad_to_deg(angle_in_gradians):
    # Flip the gradian-to-degree conversion and voilà!
    angle_in_degrees = angle_in_gradians * (360 / 400)
    return angle_in_degrees

# Conversion from gradians to radians. You got this!
def grad_to_rad(angle_in_gradians):
    # Converting to degrees first, then to radians.
    angle_in_radians = grad_to_deg(angle_in_gradians) * (math.pi / 180)
    return angle_in_radians

# Alright, time to put these conversion functions to use. Turn on the engine!

if __name__ == "__main__":
    # Feel free to input any angle you want to convert.
    # Just change the angle and its type below.
    # Don't worry, it's all in the command line. And it's gonna be gorgeous!
    
    angle = 90  # Just a random angle choice here, you can try whatever angle you like. 
    angle_type = "degrees"  # Let's start with degrees. You can switch to radians or gradians.

    # Alright-okay, now let's see what this angle is in other units
    if angle_type == "degrees":
        print(f"{angle} degrees is equal to {deg_to_rad(angle)} radians.")
        print(f"{angle} degrees is equal to {deg_to_grad(angle)} gradians.")
    elif angle_type == "radians":
        print(f"{angle} radians is equal to {rad_to_deg(angle)} degrees.")
        print(f"{angle} radians is equal to {rad_to_grad(angle)} gradians.")
    elif angle_type == "gradians":
        print(f"{angle} gradians is equal to {grad_to_deg(angle)} degrees.")
        print(f"{angle} gradians is equal to {grad_to_rad(angle)} radians.")

# So, that's the end of our fun little journey here! Hope you enjoyed it. Keep converting those angles!
