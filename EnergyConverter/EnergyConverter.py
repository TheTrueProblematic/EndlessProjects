
# Hello there lovely person! I'm a piece of code called 'EnergyConverter'. Glad to meet you!
# You can count on me to convert between joules, calories, and kilowatt-hours. No sweat!

# In this fun journey of conversion, I'm going to be using three units:
# Joules (J), calories (cal), and kilowatt-hours (kWh)
# These are the conversion factors I will use:
# - 1 cal = 4.184 J
# - 1 kWh = 3.6e+6 J

# Let's first make a function to convert Joules to other units.
# I'm going to use lambda functions because they're quick and cool!

J_to_cal = lambda J: J / 4.184  # Convert Joules to calories
J_to_kWh = lambda J: J / 3.6e+6  # Convert Joules to kilowatt-hours

# Now let's convert from other units to Joules
# This makes it easier to convert between any units by going through Joules

cal_to_J = lambda cal: cal * 4.184  # Convert calories to Joules
kWh_to_J = lambda kWh: kWh * 3.6e+6  # Convert kilowatt-hours to Joules

# The most exciting part now: time to convert between any two units!
# I'm going to use a dictionary to call the right functions based on the units

from_units_to_J = {'J': lambda x: x, 'cal': cal_to_J, 'kWh': kWh_to_J}
J_to_to_units = {'J': lambda x: x, 'cal': J_to_cal, 'kWh': J_to_kWh}

def convert_energy(value, from_unit, to_unit):
    # This is the fun bit: converting from one unit to another!
    # It's like going on a mini adventure every time a unit conversion is made!
    
    # Convert from the original unit to J
    value_in_J = from_units_to_J[from_unit](value)
    
    # Then convert from J to the final unit
    converted_value = J_to_to_units[to_unit](value_in_J)
    
    # Voila! The conversion is done!
    return converted_value

# Let's test the converter with 1 cal to kWh
# The output should be about 0.00000116222 kWh
print(convert_energy(1, 'cal', 'kWh'))

# Time to say goodbye!
# Feel free to change the units and values as you like.
# Remember to handle exceptions when input is not as expected.
# Keep smiling and happy converting!
