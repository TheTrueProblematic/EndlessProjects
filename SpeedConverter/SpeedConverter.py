
# Woohoo! Welcome to the SpeedConverter. You're gonna love this. We're having fun with speed conversions today.
# This is a simple python script that converts speed from one unit to another.
# Let's dive in, buddy!

# Defining some cool functions for the actual conversions

# Function to convert from km/h to m/s
def kmph_to_mps(speed):
    return speed * 1000 / 3600

# Function to convert from m/s to km/h
def mps_to_kmph(speed):
    return speed * 3600 / 1000

# Function to convert from km/h to mph
def kmph_to_mph(speed):
    return speed * 0.621371

# Function to convert from mph to km/h
def mph_to_kmph(speed):
    return speed * 1.60934


# Here, we're creating a function for the user input.
# We will use it to get both the speed and the units that we want to convert to/from.
def get_input(input_type):
    while True:
        val = input(f'Enter {input_type}: ')
        if val.isnumeric():
            return float(val)
        else:
            print('Invalid input, try again!')


# Now, let's get to the sweet stuff. The conversion itself
def convert_speed():
    print("\n~*~ SpeedConverter ~*~")
    print("Units: m/s, km/h, mph\n")

    # First, we're asking the user for the speed they want to convert and then the units.
    speed = get_input('the speed')
    original_unit = input('Enter the original unit: ')
    target_unit = input('Enter the target unit: ')

    # Now we do the actual conversion
    # For each of the possible units, we first convert the speed to km/h
    # and then if necessary, we convert it to the target unit.
    if original_unit == 'km/h':
        if target_unit == 'm/s':
            print('Result:', kmph_to_mps(speed))
        elif target_unit == 'mph':
            print('Result:', kmph_to_mph(speed))
        else:
            print('Invalid unit')
    elif original_unit == 'm/s':
        speed = mps_to_kmph(speed)
        if target_unit == 'km/h':
            print('Result:', speed)
        elif target_unit == 'mph':
            print('Result:', kmph_to_mph(speed))
        else:
            print('Invalid unit')
    elif original_unit == 'mph':
        speed = mph_to_kmph(speed)
        if target_unit == 'km/h':
            print('Result:', speed)
        elif target_unit == 'm/s':
            print('Result:', kmph_to_mps(speed))
        else:
            print('Invalid unit')
    else:
        print('Invalid unit')


# Finally, we call the conversion function
if __name__ == '__main__':
    convert_speed()

