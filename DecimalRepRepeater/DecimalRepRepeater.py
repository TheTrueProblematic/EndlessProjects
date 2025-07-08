
# DecimalRepRepeater.py
# An exuberant creation by a joy-filled coder!
# This is a fabulous python script that has one sole purpose in life: to detect any repeating sequences in the output of decimal divisions.

# The wonderful news is, this python script can run smoothly on any fresh install of python
# (So advanced, it even doesn't need internet access or API use. Woohoo!)
# It only has one python file, and is capable of working on any platform.

# To make sure our script remains as free and independent as possible, we won't be including any external dependencies.
# It's just pure python goodness we're serving here, folks!


def find_repeat(n, d):
    """Finds and returns the repeating sequence of numbers in the decimal representation of n/d."""
    
    # Creating an empty dictionary to store the remainder and the position of the remainder.
    # It's like our tiny reservoir of mathematical memory!
    # The key will be the remainder and value will be its position
    
    rem_position_dict = dict()
    
    # Initialing the remainder
    remainder = n % d
    
    # Keep finding remainder until either remainder becomes 0 or repeats
    # It's like our script becomes a tiny detective, hunting for those repeat sequences!
    
    while ((remainder != 0) and (remainder not in rem_position_dict)):
    
        # Storing this remainder and its position
        rem_position_dict[remainder] = len(rem_position_dict)
         
        # Multiplying remainder with 10
        remainder = remainder * 10
         
        # Append remainder / d to result
        # Ignore the integral part of result
        remainder = remainder % d

    # If we did not find a remainder that could suggest a repeat sequence,
    # it means we have to expose this number as a falsehood!
    # The party poopers of the math world - the non-repeating decimal numbers!
    if (remainder == 0):
        return ""

    # If we found a repeating sequence, we'll celebrate by returning it!
    return str(remainder)

# Now, we'll call our detective function find_repeat on a number and its divisor.
# You can change this to any number/divisor pair you're curious about
print(find_repeat(1, 3))
