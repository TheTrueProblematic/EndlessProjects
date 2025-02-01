
# Hey there, Super Coder! Let's delve into some Number-ology Today. 
# We're going on a time machine ride back to Ancient Rome! Ready?

# Our mission, if we choose to accept it, is to build a little Python program that can 
# Convert any given integer into a Roman Numeral. 

# EQUIPMENT: Just Python! No extras, no libraries, no APIs, no GUIs. 

# Let's get this show on the road!

def integer_to_roman(num):
    # Here are some mappings that we are going to use.
    # Romans didn't have a zero in their number system. Talk about difficult maths homework!
    mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 
               40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    # Let's dive into the action. Define a blank string that we are going to fill with our Roman Numeral, piece by piece!
    roman = ''

    # Let's travel from the largest value to the smallest in our map (hence, we reverse sort).
    # If our number is larger than the current map value, we'll take it off the top and put the corresponding Roman Numeral into our result!
    for i in sorted(mapping.keys(), reverse=True):
        while num >= i:
            roman += mapping[i]
            num -= i
    
    # Mission Complete! Time to show off our lovely Roman Numeral! 
    return roman

num = int(input("Enter an integer: ")) 
print(integer_to_roman(num))

