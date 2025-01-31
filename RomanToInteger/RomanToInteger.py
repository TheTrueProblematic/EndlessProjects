
# Alright, here's a fun little script for you! 🐍
# Let's dive into the world of Roman numerals and their integer equivalents. 

# I'm going to help you convert any Roman numeral to its Integer form.
# You guessed it right, we're going back in time 😁

# Firstly, let's setup a dictionary for roman numerals and their integer equivalents
roman_int_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romanToInt(roman):
    """
    Function to convert a given roman number to Integer
    :param roman: roman numeral as a string
    :return: equivalent integer value
    """
    total = 0 # We'll be keeping track of the magic number here
    prev = 0  # This is to keep track of the previous value for those special cases

    # Now, let's loop through the Roman numeral from the end to the beginning
    for i in range(len(roman) - 1, -1, -1):
        current = roman_int_dict[roman[i]]

        # Ah, the special cases! Say IV or IX. Remember these from School?
        # Here, we check if current value is less than the previous one
        # If so, we deduct the twice of that value [since it got added in the previous step]
        if current < prev:
            total -= current * 2

        # Now, we add the current value
        total += current

        # And then we update the previous character value for the next iteration
        prev = current

    # And Voila! We return the total value once the loop's done
    return total


# Time for testing. Let's take VII for example, which should output 7
# You can put any roman numeral of your choice here
rom_num = input("Please, enter a roman numeral: ").upper()
print(romanToInt(rom_num))
# You can replace the hardcoded 'VII' with any input method of your choice

# That's it! We have our very own Roman numeral to integer converter.
# Thanks for coming to my Ted Talk. Stay awhile and listen 🎧
