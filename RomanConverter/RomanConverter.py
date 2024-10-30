
# Hello there, you Roman Numerals’ lovers or scholars!!!
# Welcome to the most amazing Roman Numerals Converter ever!!!
# This is the one and only, the unique, the matchless RomanConverter file!!!
# With it you can enlighten your life and your routines by converting those cryptic but fascinating Roman numerals to understandable integers and the other way around.

# Let's start off by creating a dictionary to map Roman numerals to their integer equivalents

roman_to_int_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# This fantastic function is designed to convert Roman numerals to integers.
# Put your sunglasses on, and let’s see how it shines!!!

def roman_to_int(s):
    # Initialize a variable to store the result.
    total = 0

    # Let's start to look through each character of your Roman numeral string.
    for i in range(len(s)):
        # If the current value is less than the next one, we subtract it. Otherwise, add it!!!
        if i + 1 < len(s) and roman_to_int_mapping[s[i]] < roman_to_int_mapping[s[i + 1]]:
            total -= roman_to_int_mapping[s[i]]
        else:
            total += roman_to_int_mapping[s[i]]
    # And VOILA!!!, Here is your shiny integer.
    return total
    
# Now, let’s do the magic in reverse!!!
# We are going to go from integers to Roman numerals!!!

int_to_roman_mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                        50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

def int_to_roman(num):
    # This is your beautiful canvas in which the output will be painted.
    roman = ''

    # Let's start to break down the number, starting from the largest value in our mapping.
    for i in sorted(int_to_roman_mapping.keys(), reverse=True):
        # While our number is larger or equal to the current key, add its Roman equivalent to the string, and reduce it.
        while num >= i:
            roman += int_to_roman_mapping[i]
            num -= i
    
    # Now, let the world behold your dazzling Roman numeral!!!
    return roman

# We've had a blast writing this for you!!!
# Now you can change the world by converting Roman numerals into integers and vice versa!!!
# ENJOY!!!

