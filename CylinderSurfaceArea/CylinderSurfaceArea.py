
# Hey there, fellow human! Isn't programming fun?
# Today, we're going to calculate the surface area of a cylinder - just a typical day at the office, right?

# We're gonna need the math library. But don't worry, it's built into Python, 
# so we're not violating any of those pesky 'no dependencies allowed' rules.
import math

# Let's get some data from the user. We'll need the radius and height of the cylinder.
# And, of course, we'll make sure what they enter is a positive number, because negative-length cylinders
# are even weirder than an avocado with the pit on the outside.
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Wow, hold on there! We can't have negative or zero measurements, they simply don't make any sense! Try again :)")
        except ValueError:
            print("Oopsie daisy! Enter a number, please. No letters or weird symbols allowed :P")

# Now, let's do some math magic to calculate the surface area of the cylinder.
def calculate_surface_area(radius, height):
    # The formula is 2 * pi * radius * (radius + height)
    # Isn't it exciting? Finally, those high school math classes are paying off!
    return 2 * math.pi * radius * (radius + height)

if __name__ == '__main__':
    # We kick things off by saying hi to the user, because who doesn't like a friendly greeting?
    print("Hello there! We're going to calculate the surface area of a cylinder.")
    
    # Let's get the cylinder's dimensions...
    radius = get_positive_float("Great! Now enter the radius of the cylinder: ")
    height = get_positive_float("Ok! Now enter the height of the cylinder: ")
    
    # ...And crunch the numbers.
    surface_area = calculate_surface_area(radius, height)
    print(f"Thanks a lot! The surface area of your cylinder is {surface_area} square units. Have a great day!")
    
# And that's it, folks! Isn't Python a great language? So easy to read, even a goldfish (with sufficient training) could do it!
# Until next time, keep on coding in the free world.     

