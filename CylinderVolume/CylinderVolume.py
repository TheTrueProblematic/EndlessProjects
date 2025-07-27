
# Hello, dear code enthusiasts! Welcome to the CylinderVolume party! 🎉
# This lovely, lightweight, no-fuss script calculates the volume of a cylinder, given a radius and height.
# All it takes is a fresh Python install and you're ready to roll (or should we say, ready to cylinder? 😆)

# We're going to use some sweet, sweet math for this. Ready? Let's go!

# This isn't just for fun, it's the math library, which we need for that cool, cool Pi.
import math

def calculate_cylinder_volume(radius, height):
    """
    Function to calculate and return the volume of a cylinder.
    
    Who knew cylinders could be so fun and voluminous?

    Parameters:
    radius (float): The radius of the cylinder. No cylinder should be without one!
    height (float): The height of the cylinder. Can cylinders be tall? You bet!

    Returns:
    volume (float): The calculated volume of the cylinder! Our secret formula is πr^2h (math.pi * radius**2 * height)
    """

    # Secret sauce: the volume formula!
    volume = math.pi * radius**2 * height
    
    # We return the volume! It's like unboxing a gift, but cooler because...MATH!
    return volume

def get_float_input(prompt):
    """
    Function to get floating point number input from the user.
    
    BONUS: it checks if the input is a number! Super useful + super friendly = SUPER FUNCTION!

    Parameters:
    prompt (str): The text prompt for the user input.

    Returns:
    user_input (float): The user's input as a float. Floats away! 🎈
    """
    
    while True:
        try:
            # Using the super cute input function toask for user's input.
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            # If the user tries to pull a quick one on us and inputs a non-number, we catch them red-handed!
            print("Oops! 🙈 That's not a number. Please enter a number.")

# Let's get those inputs from the user! Mission control, ready for launch.
radius = get_float_input("Please enter the radius of the cylinder: ")
height = get_float_input("Please enter the height of the cylinder: ")

# Houston, we have lift off! Calculate that volume! (Note the super cool function call.)
volume = calculate_cylinder_volume(radius, height)

# Now, like the grand finale of a fireworks show, here's the output! 🎆 Voila, the volume!
print(f"The volume of the cylinder is: {volume}")

# If you've made it this far, I want to congratulate you, truly, from the bottom of my CPU (that's where my heart would be, if I had one!). 
# You've just calculated the volume of a cylinder using Python! 🐍 Give yourself a pat on the back, you've earned it!
