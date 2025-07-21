
# Hey there! Welcome to our little piece of code heaven :D
# We're building a CoordinateConverter today - super fun.
# It's all about transforming cartesian coordinates to polar and other way around!
# And to add some spice, it's all going to happen from the command line.
# So buckle up and let's dive into this code adventure!

# Let's start by importing our armor and weapons! (just kidding, we only need math :P).
import math

# Alrighty! Now we define our functions which will do all the magic behind the curtain.

# This nifty function right here will convert cartesian to polar coordinates.
# Take a deep breath! Math ahead :D
def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, math.degrees(theta)

# Panic not! Our next little wizard will convert polar to cartesian coordinates.
# It's just as jolly and mathy as its sibling!
def polar_to_cartesian(r, theta):
    theta = math.radians(theta)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

# Time for the command line interface! It's nothing more than a friendly chat between us and user.
def main():
    print("Hey there, coordinate explorer!")
    print("Today, we're going to convert some coordinates.")
    print("1: Cartesian to Polar")
    print("2: Polar to Cartesian")
    choice = int(input("Enter your choice => "))

    if choice == 1:
        x = float(input("Enter x => "))
        y = float(input("Enter y => "))
        r, theta = cartesian_to_polar(x, y)
        print(f"\nThe polar coordinates are (r, theta): ({r}, {theta})")
    elif choice == 2:
        r = float(input("Enter r => "))
        theta = float(input("Enter theta => "))
        x, y = polar_to_cartesian(r, theta)
        print(f"\nThe cartesian coordinates are (x, y): ({x}, {y})")
    else:
        print("\nOops! Seems like you've entered a wrong choice. Please run the program again.")

# And finally, the kick off! But only when our script is run by itself and not imported. Python etiquette.
# So, put on your explorer hat and let's dive into the world of coordinates :D
if __name__ == "__main__":
    main()

