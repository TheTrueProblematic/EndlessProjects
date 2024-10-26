
# Hello World! Or should I say, Hello Developers!
# This is your jolly little number wizard here, all set to perform some magical maths.
# Our magical task today is converting hexadecimal numbers to their decimal equivalents. 
# Sounds like fun, doesn't it? Well, buckle up and let's begin our adventure!

# import the sys module for Command Line magic
import sys

def hex_to_decimal(hex_number):
    # Let's cast our first spell and convert hex_number to its decimal equivalent
    decimal_number = int(hex_number, 16)

    # Well, that's it! Our magic trick is done.
    # But hey, every good magician should present his trick, right?
    # So let's return our trick
    return decimal_number

# But our magic show isn't over! We now must prepare to dazzle our audience.
# So let's take input from them.
hex_input = sys.argv[1]

# Perform our magic trick (Psst... it's really just math. But don't tell the audience!)
decimal_output = hex_to_decimal(hex_input)

# Now, for our grand finale, let's reveal the trick!
print(decimal_output)

# And with that, the curtain closes on our magic show.
# Hope y'all enjoyed folks!

# Happy Coding! Keep spreading the magic!

