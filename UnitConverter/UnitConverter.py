
# Hey there, welcome to our fun UnitConverter Python program!
# This little code snippet is going to make our lives much easier. No more scratching our heads converting units back and forth.
# Be ready to amaze your classmates or colleagues with an instant conversion of meters into feet or kilograms into pounds!

# To keep it neat and readable, we are going to split the whole shebang into functions handling each unit type.

def length_converter():
    # Possible length conversions
    conversions = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34}

    # Prompt user input
    from_unit = input("Which unit would you like to convert from [mm, cm, m, km, in, ft, yd, mi]?: ")
    to_unit = input("Which unit would you like to convert to [mm, cm, m, km, in, ft, yd, mi]?: ")
    value = float(input("Enter your value: "))

    # Convert everything to meters first
    meters = value * conversions[from_unit]
    # Then convert meters to desired unit
    result = meters / conversions[to_unit]

    print("The result is: ", result)

def weight_converter():
    # Possible weight conversions
    conversions = {"mg": 0.001, "g": 1, "kg": 1000, "t": 1000000, "oz": 28.3495, "lb": 453.592, "st": 6350.29}

    from_unit = input("Which unit would you like to convert from [mg, g, kg, t, oz, lb, st]?: ")
    to_unit = input("Which unit would you like to convert to [mg, g, kg, t, oz, lb, st]?: ")
    value = float(input("Enter your value: "))

    grams = value * conversions[from_unit]
    result = grams / conversions[to_unit]

    print("The result is: ", result)

def volume_converter():
    # Possible volume conversions
    conversions = {"ml": 1, "l": 1000, "fl oz": 29.5735, "cup": 236.588, "pt": 473.176, "qt": 946.353, "gal": 3785.41}

    from_unit = input("Which unit would you like to convert from [ml, l, fl oz, cup, pt, qt, gal]?: ")
    to_unit = input("Which unit would you like to convert to [ml, l, fl oz, cup, pt, qt, gal]?: ")
    value = float(input("Enter your value: "))

    milliliters = value * conversions[from_unit]
    result = milliliters / conversions[to_unit]

    print("The result is: ", result)

# Finally, we will need a main function to call our converters
def main():
    print("Welcome to UnitConverter! Choose the type of conversion: ")
    print("1. Length")
    print("2. Weight")
    print("3. Volume")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    elif choice == "3":
        volume_converter()
    else:
        print("Oops! That's not a valid choice. Run the program again!")

# Finally call the main function and let's convert
if __name__ == "__main__":
    main()

