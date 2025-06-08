
# Heyo! I hope you're having a fantastic day because this little script will make it even better!
# We're calling this little guy "LengthConverter" and it does exactly what it sounds like it does.

# LengthConverter can convert between meters, feet, inches, and yards. Pretty cool, huh?
# Imagine, you'll never have to Google "how many feet in a meter?" again!

# To keep it simple and smart, our script lives entirely in the command line (CLI) with no GUI.
# Plus, it has zero dependencies, doesn't need internet access, and it's multi-platform capable. 
# It only speaks Python (and really fluent in it BTW), and it fits snugly in just one Python file. Let's dive in!

# Definitions for length conversion factors
CONVERSION_FACTORS = {
    ('meters', 'feet'): 3.281,
    ('feet', 'meters'): 1/3.281,
    ('meters', 'inches'): 39.37,
    ('inches', 'meters'): 1/39.37,
    ('yards', 'meters'): 1/1.094,
    ('meters', 'yards'): 1.094,
    ('feet', 'inches'): 12,
    ('inches', 'feet'): 1/12,
    ('yards', 'feet'): 3,
    ('feet', 'yards'): 1/3,
    ('yards', 'inches'): 36,
    ('inches', 'yards'): 1/36,
}

def length_converter(from_unit, to_unit, value):
    """ Returns the converted value of a length from one unit to another. """

    # Just check if we can make the conversion
    if (from_unit, to_unit) not in CONVERSION_FACTORS:
        raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")
    
    # If we can, let's do the math!
    factor = CONVERSION_FACTORS[(from_unit, to_unit)]
    return value * factor

def main():
    """ Main function to get user input and perform conversion. """

    print("Welcome to the LengthConverter! Super happy you're here.")

    from_unit = input("Enter the unit you are converting from (meters, feet, inches, yards): ").lower()
    to_unit = input("Enter the unit you are converting to (meters, feet, inches, yards): ").lower()
    value = float(input("Enter the value you want to convert: "))

    try:
        # Let's run our conversion function with the user input
        result = length_converter(from_unit, to_unit, value)
        print(f"\nConverted: {value} {from_unit} is equal to {result} {to_unit}")

    except ValueError as e:
        # Oops! Something went wrong. Print the error message.
        print(str(e))

if __name__ == "__main__":
    main()
