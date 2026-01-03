
# Hey there happy coders! Get ready for an exciting journey through arithmetic... with a twist
# We are going to perform calculations with Roman numerals (You heard it right!!)
# So buckle up, and let's dive into it.

# we are going to use a dictionary to map the roman numerals to their corresponding integer values
roman_integer_map = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

#Defining a function to convert Roman numerals to integers
def roman_to_integer(roman):
    integer = 0
    for i in range(len(roman)):
        #if the current numeral is smaller than the next one, we are going to subtract it
        if i < len(roman) - 1 and roman_integer_map[roman[i]] < roman_integer_map[roman[i + 1]]:
            integer -= roman_integer_map[roman[i]]
        else:
            integer += roman_integer_map[roman[i]]
    return integer

#And now defining a function to convert integers to Roman numeral
def integer_to_roman(integer):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    sybols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    for i in range(len(values)):
        while integer >= values[i]:
            integer -= values[i]
            roman += sybols[i]
    return roman

# Now, it's time to define our arithmetic functions,
# So let's go with addition first(we're friendly like that)
def add_roman(roman1, roman2):
    integer1 = roman_to_integer(roman1)
    integer2 = roman_to_integer(roman2)
    return integer_to_roman(integer1 + integer2)

# And now, let's define our subtraction function.
def subtract_roman(roman1, roman2):
    integer1 = roman_to_integer(roman1)
    integer2 = roman_to_integer(roman2)
    return integer_to_roman(integer1 - integer2)

# We already have addition and subtraction, why not bring in multiplication as well 
def multiply_roman(roman1, roman2):
    integer1 = roman_to_integer(roman1)
    integer2 = roman_to_integer(roman2)
    return integer_to_roman(integer1 * integer2)

# And finally, let's define our division function.
def divide_roman(roman1, roman2):
    integer1 = roman_to_integer(roman1)
    integer2 = roman_to_integer(roman2)
    if integer2 != 0:
        return integer_to_roman(integer1 // integer2)
    else:
        return 'Roman numerals cannot express zero or negative numbers, so division by zero is undefined'

if __name__ == '__main__':
    print("Enter two roman numerals and the operation to be performed from the following: ")
    print("Addition: 1\nSubtraction: 2\nMultiplication: 3\nDivision: 4")
    roman1 = input("Enter the first roman numeral: ").upper()
    roman2 = input("Enter the second roman numeral: ").upper()
    operation = int(input("Enter the operation: "))
    if operation == 1:
        print(add_roman(roman1, roman2))
    elif operation == 2:
        print(subtract_roman(roman1, roman2))
    elif operation == 3:
        print(multiply_roman(roman1, roman2))
    elif operation == 4:
        print(divide_roman(roman1, roman2))
    else:
        print("Invalid operation!") 
    print("Have fun doing arithmetic with Roman numerals!")
