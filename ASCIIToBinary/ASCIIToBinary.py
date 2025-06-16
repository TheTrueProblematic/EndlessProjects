
# Hello there, fellow Pythonist! Let's embark on an adventure today.
# We're about to script a fun command-line utility which will convert our ASCII text into binary.(Cue dramatic music)
# Import glob library to deal with input and output files from command line.

# Our adventurer's kit doesn't include any extra tools (libraries) so we will be generating this magical tool using bare hands (build-in Python functions). Let's go!

def ascii_to_binary(input_string):
    # Here's how we're going to tackle this:
    # Python by default gives us ASCII for characters using the ord function.
    # Once we have the ASCII value, all it takes is some binary magic to convert it into binary!

    binary_string = ""
    for character in input_string:
        # convert character to binary string of 8 bits
        binary_string += "{0:08b}".format(ord(character))

    # And voila! We've achieved what we set out to, and in such a stylish way too.
    return binary_string


def main():
    # Here comes the main function. (Drumrolls, please!)
    # This is where we'll interact with our wonderful audience - you!
    import sys

    # Let's fetch whatever the user has given us from command line.
    if len(sys.argv) > 1:
        input_string = str(sys.argv[1])
    else:
        # If the user didn't provide an input string, let's ask them to do so!
        print("No input string provided. Please run the script with an argument representing the ASCII string to convert.")

    # And now, for the climax of our wonderful program (drumroll...), we're going to once again call upon our heroic function, ascii_to_binary!
    print("Binary Representation:", ascii_to_binary(input_string))


# Python convention: the only effect of the main sentinel is to change __name__ to '__main__'.
if __name__ == "__main__":
    main()

# And... cut! That's a wrap on our small but impactful little program to convert ASCII text to binary.
# Wasn't that fun? Python sure makes things easy and enjoyable.
# Until next time, happy coding!
