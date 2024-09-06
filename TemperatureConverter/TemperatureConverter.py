
# Hi there! Let's dive into the fun world of temperature conversion! Today, we're converting between Celsius, Fahrenheit, and Kelvin.
# Don't you dare think about touching that GUI or making an API request. It's just us, the terminal, and our cool temperature conversions.

def convert_temperature(degrees, from_unit, to_unit):
    # Starting off with some dictionaries of our conversion formulas. Oh, the power of key-value pairing!
    conversion_formulas = {
        ("c", "f"): lambda x: (x * 9/5) + 32,
        ("c", "k"): lambda x: x + 273.15,
        ("f", "c"): lambda x: (x - 32) * 5/9,
        ("f", "k"): lambda x: (x - 32) * 5/9 + 273.15,
        ("k", "c"): lambda x: x - 273.15,
        ("k", "f"): lambda x: (x - 273.15) * 9/5 + 32,
    }
    
    # Now let's account for those cases where the user wants to convert a temp to the same unit. Chillin' in its own uniqueness.
    if from_unit == to_unit: 
        return degrees

    # Gotcha! We've got a formula for this temperature conversion.  
    elif (from_unit, to_unit) in conversion_formulas: 
        return conversion_formulas[from_unit, to_unit](degrees)

    # Well, looks like their conversion request is not on our menu today folks. Good thing they've got you around.
    else:
        return "Sorry, can't convert from {} to {}".format(from_unit, to_unit)

if __name__ == "__main__":

    # Ask for temperature input and which units to convert from and to. 
    degrees = float(input("Enter the temperature: "))
    from_unit = input("Which unit is the temperature in currently? (c/f/k): ")
    to_unit = input("To which unit would you like to convert the temperature? (c/f/k): ")

    # Perform temperature conversion and print results like a boss.
    result = convert_temperature(degrees, from_unit, to_unit)
    print(f"The converted temperature is {result}")

