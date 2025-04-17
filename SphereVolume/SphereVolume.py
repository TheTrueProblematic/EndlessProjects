
# Hey fellow programmer, hope you're having a fantastic day! 🚀
# Let's embark on a mind-blowing journey of calculating the volume of a sphere, shall we? 😉

# To begin with, we are importing the math module
# It houses a lot of fun functions that can make our sphere-volume-calculating journey swift and breezy!
import math

# Now, let's declare our main function. 
# This magical function will calculate the volume of a sphere for us! Abracadabra! ✨🔮
def calculate_sphere_volume(radius):
    
    # Let the magic happen: in the next line, we're writing the formula to calculate the volume of a sphere.
    # (You may remember it from high school - 4/3πr³)
    # Ah, the beauty of mathematics! ❤️📚
    volume = (4/3) * math.pi * radius ** 3

    # Returning the volume back from where the function was called.
    # Like a homing pigeon 🐦 carrying the volume back to our program!
    return volume

# Let's get a little chatty with the user.
# Prompting the user to enter the radius of the sphere (user inputs are always a little full of surprises, right? 😅)
radius = float(input("Input the radius of the sphere: "))

# Let's invoke the magic function and store the mystical sphere volume it sends our way.
sphere_volume = calculate_sphere_volume(radius)

# Finally! The moment that everyone has been waiting for:
# We reveal the answer to the user, like pulling a rabbit out of a hat! 🎩🐇
print("The Volume of the Sphere is:", sphere_volume)

# And that's the end of our magical journey! Simple yet elegant, isn't it? 
# Now you have your handy-dandy sphere volume calculator, right in your terminal! So sit back, relax and calculate! 🥳

