
# Hey there, delightful being! Welcome to our sweet little power_converter.py file :)
# Here we have a mission: convert between watts, horsepower, and kilowatts!
# Don't worry, we're keeping it simple: No GUIs, no external dependencies, no internet access... Pure Python fun!
# Let's get to it!

# First things first, let's define our conversion values. 
# These constants are the heart of our program: without them there wouldn't be any conversion happening!
WATT_TO_KILOWATT = 0.001
WATT_TO_HORSEPOWER = 0.00134102
KILOWATT_TO_WATT = 1000
KILOWATT_TO_HORSEPOWER = 1.34102
HORSEPOWER_TO_WATT = 745.7
HORSEPOWER_TO_KILOWATT = 0.7457

# Now we delve into the world of conversion functions.
# Each of our functions gets one job: Convert from one unit to another. 
# They take a value, apply the proper conversion rate, and return the result. Simple enough, right? Let's do it!

def convert_watt_to_kilowatt(watt):
    return watt * WATT_TO_KILOWATT

def convert_watt_to_horsepower(watt):
    return watt * WATT_TO_HORSEPOWER

def convert_kilowatt_to_watt(kilowatt):
    return kilowatt * KILOWATT_TO_WATT

def convert_kilowatt_to_horsepower(kilowatt):
    return kilowatt * KILOWATT_TO_HORSEPOWER

def convert_horsepower_to_watt(horsepower):
    return horsepower * HORSEPOWER_TO_WATT 

def convert_horsepower_to_kilowatt(horsepower):
    return horsepower * HORSEPOWER_TO_KILOWATT


# To create interactive, command-line friendly environment, we will use built-in input function.

print("Hello there! Ready for some almighty power conversions? Here's what I can do for you:")
print("1) Watt to Kilowatt")
print("2) Watt to Horsepower")
print("3) Kilowatt to Watt")
print("4) Kilowatt to Horsepower")
print("5) Horsepower to Watt")
print("6) Horsepower to Kilowatt")


# User inputs the choice.
choice = int(input("Enter your choice number: ")) 

# Now, depending on the choice, we call the appropriate conversion function. 
# We also gather the necessary input from the user.
if choice == 1:
    watt = float(input("Enter power in watts: "))
    print(f"That's {convert_watt_to_kilowatt(watt)} Kilowatt(s)!")
elif choice == 2:
    watt = float(input("Enter power in watts: "))
    print(f"That's {convert_watt_to_horsepower(watt)} horsepower!")
elif choice == 3:
    kilowatt = float(input("Enter power in kilowatts: "))
    print(f"That's {convert_kilowatt_to_watt(kilowatt)} W!")
elif choice == 4:
    kilowatt = float(input("Enter power in kilowatts: "))
    print(f"That's {convert_kilowatt_to_horsepower(kilowatt)} Horsepower!")
elif choice == 5:
    horsepower = float(input("Enter power in horsepower: "))
    print(f"That's {convert_horsepower_to_watt(horsepower)} W!")
elif choice == 6:
    horsepower = float(input("Enter power in horsepower: "))
    print(f"That's {convert_horsepower_to_kilowatt(horsepower)} KW!")

# And that's it! Super small, super light, and super powerful. ¯\_(ツ)_/¯ 
# A Python power converter that works in a fresh install on any machine. Enjoy!
