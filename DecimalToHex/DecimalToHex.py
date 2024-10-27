
# Hey there fab programmer! Time to dive into the beautiful world of numerical systems conversion.
#
# We have a super simple and fun task here: we're converting decimal numbers into their glamorous hexadecimal equivalents.
# It's like dressing up numbers for a glossy, shiny Math Red Carpet event! 
#
# If you're executing this script from the command line, just input your decimal number and the program will do the rest!

# Importing the system-specific parameters and functions
import sys


# Let's roll up our sleeves and create a function to convert decimal numbers to hexadecimal.
def convert_to_hex(decimal_number):
    # Any integer in Python can easily be converted to any base between 2 and 36 using the built-in function hex()
    # The hex function may return a string starting with "0x" to indicate that it's a hexadecimal number.
    # If we prefer stripping the "0x" from our glamorous number, we can use the Python string slicing feature.
    return hex(decimal_number)[2:]


def main():
    # Our friend sys.argv, willing to provide command line arguments in a list where sys.argv[0] is the script name.
    try:
        # our command line provided decimal number will be at index 1
        decimal_number = int(sys.argv[1])
    except (IndexError, ValueError):
        print("Please provide a valid integer number as input.")
        sys.exit(1)  # exits the program because a number was not provided

    # Convert the decimal number to hexadecimal
    hex_number = convert_to_hex(decimal_number)
    
    # Print the hexadecimal number with all of its radiance!
    print("The hexadecimal representation of the number is : ", hex_number)


# And now, our main function is ready to shine.
if __name__ == "__main__":
    main()

# Isn't that just a treat? Now go on, convert things. Have fun!
