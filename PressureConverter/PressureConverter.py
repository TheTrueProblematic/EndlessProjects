
# Hello fellow code enthusiast! Get ready because we are going on an adventure.
# Our journey? We're creating a handy Pressure Converter with ZERO dependencies! Fantastic!

# We are going to work with Pascals (Pa), bars, pounds per square inch (psi), 
# and atmospheres (atm). So buckle up! 

# Let's start by defining the conversion rates from Pascals to our other units - 
# purely because Pascals are the SI unit, and SI units rock!

PA_TO_BAR = 1e-5
PA_TO_PSI = 0.00014503773773020998
PA_TO_ATM = 9.869232667160128e-6

def convert_pressure(value, from_unit, to_unit):
    """ Convert Pressure From One Unit to Another.
    
    Args:
        value (float): The pressure value that needs to be converted.
        from_unit (str): The unit of the input value, can be 'pa', 'bar', 'psi' or 'atm'.
        to_unit (str): The unit to which the value needs to converted, can be 'pa', 'bar', 'psi' or 'atm'.
        
    Returns:
        float: The converted pressure value.
    """

    # Convert the input value to Pascals.
    
    if from_unit.lower() == 'pa':
        pressure_in_pa = value
    elif from_unit.lower() == 'bar':
        pressure_in_pa = value / PA_TO_BAR
    elif from_unit.lower() == 'psi':
        pressure_in_pa = value / PA_TO_PSI
    elif from_unit.lower() == 'atm':
        pressure_in_pa = value / PA_TO_ATM
    else:
        print("Invalid from_unit! Please use 'pa', 'bar', 'psi' or 'atm'.")
        return

    # Now, convert the value in Pascals to the desired output unit.
    
    if to_unit.lower() == 'pa':
        return pressure_in_pa
    elif to_unit.lower() == 'bar':
        return pressure_in_pa * PA_TO_BAR
    elif to_unit.lower() == 'psi':
        return pressure_in_pa * PA_TO_PSI
    elif to_unit.lower() == 'atm':
        return pressure_in_pa * PA_TO_ATM
    else:
        print("Invalid to_unit! Please use 'pa', 'bar', 'psi' or 'atm'.")
        return

# That's it! Our incredible Pressure Converter is ready for action!
# Now, wherever you are, and whatever pressure you are under, you can always convert it!
# Happy coding!


