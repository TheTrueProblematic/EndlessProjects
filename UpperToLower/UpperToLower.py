# Hello there! In this wonderful program we'll convert a string from UPPERCASE to lowercase.
# We will do this magic without resorting to using built-in python functions!
# Sounds like an exciting adventure, isn't it!

def convert_uppercase_to_lowercase(input_string):
    # hashlibadabra, let the magic begin!

    # Initializing an empty string to store our marvellous output
    output_string = ""

    # It's loop time! We're moving through every character in our input string
    for char in input_string:
        # ASCII values of uppercase alphabets are from 65 to 90
        # Let's catch these mischievous uppercase letters
        if 65 <= ord(char) <= 90:
            # If it's an uppercase letter, let's transform it to a lower case
            # We do this by adding 32 to the ASCII value, 'coz that's how ASCII rolls!
            char = chr(ord(char) + 32)
        # Now we'll keep appending our transformed characters to the output string
        output_string += char

    # That's all folks! The string has been transformed!
    # Let's return our magical result!
    return output_string

# Now let's test our powerful function with an example
# Remember though, in REAL Mystic Python Land, this would be input from somewhere else.
# But for now, let's amuse ourselves with this string:
example_string = "HELLO, PROGRAMMERS!"

# Hocus pocus, let's call our magical function and see the wonders!
print(convert_uppercase_to_lowercase(example_string))
# Et voila! You'll see "hello, programmers!"- Magic isn't it!

# Journey ends here, traveller.
# Now go forth and use this mighty function in your awesome program!
# Happy coding! Don't forget that Magic is nothing but understanding the rules our universe functions on!