
# Hey there, happy coder! Welcome to our little RGB to Hex converter :)
# Python is just plain amazing, isn't it?
# First let's start with creating a function for the conversion

def rgb_to_hex(rgb):
    # Here we're making sure each value is within the proper range
    # If not, we'll cap it at the 0-255 border
    # Why these numbers? That's the RGB color model for ya!
    rgb = [max(0, min(val, 255)) for val in rgb]

    # Now let's use Python's format method to convert each of the RGB values to hexadecimal
    # And voilà! Colorful magic!
    return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

# Alright, time to capture the RGB colors lines from the command line!
def main():
    try:
        # This will grab the RGB values from the command line
        # Oh, expect a ValueError if they're not integers!
        rgb = [int(x) for x in input("Enter RGB values (separate with spaces): ").split()]
        # Time to cross the rainbow bridge from RGB to Hex!
        print("The equivalent Hex color code is: " + rgb_to_hex(rgb))

    except ValueError:
        print("Hey, it seems you entered a non-integer value!")
        print("Remember, RGB values are three integers separated by spaces; for example: '123 45 67'")

    except Exception as err:
        print(f"Oops! Something else went wrong: {err}")

# Now, let's make sure this file is not imported as a module
# Want to know more about this? Google "Python if __name__ == "__main__""
if __name__ == "__main__":
    main()

