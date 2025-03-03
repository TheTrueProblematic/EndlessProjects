
# Hooray! Let's get started! This super cool script is going to generate a random HEX color for you. 
# Why? Well, why not? Plus, it's fun! 

# Also, real quick reminder: no GUI here, this is a CLI-only party. 
# Also, no Internet, no APIs, and absolutely no non-python shenanigans. Just python, friends.

# Let's import what we need: just the basics! A little `random` to spice things up!
import random


# Now, let's create a function to represent each color component.
def random_color_part():
    # Every color component is two bytes. One digit is hexadecimal.
    # So we will generate a random number between 0 and 255 (which is FF in hexadecimal)
    # And then, convert it to hexadecimal, happy and jolly.
    return "{:02X}".format(random.randint(0, 255))


# Finally, let's create our main function that will perfect the art of color generation:
def generate_hex_color():
    # We just concatenate the individual color components mentioned above, 
    # with '#' in front because that's how HEX colors work in the world of web! Wee!
    return '#' + random_color_part() + random_color_part() + random_color_part()
    
    
# Now, let's see what color we got today:
print(generate_hex_color())

# That's it! Pretty simple, pretty amazing. This is your lucky color today!
# You may run this program as many times as you want for different colors.
# Hope you are left amused and are grinning from ear to ear. Happy coding, mate!

