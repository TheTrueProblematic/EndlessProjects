
# Hello, happy coder! 😄
# Welcome to the HexToBinary python file! We're going to take an exciting journey to
# convert hexadecimal numbers to their binary counterparts! 🎉
# Make sure to tie your shoes, because it's going to be an amazing ride!

# The first thing we're going to need to do is import the handy dandy "sys" module.
# This allows us to take command line arguments!
import sys

# Now let's define our function that will do the magical conversion! 🎩✨
def hex_to_bin(hex_value):

    # Here's some fun magic in action:
    # Python actually has a built-in function to convert hexadecimal to binary!!
    # And woohooo, it's super simple to use!
    return bin(int(hex_value, 16))[2:]

# Let's do a little dance 💃🕺 because we're nearly done! 
# Now all we need to do is take the user's input and use our function!

if len(sys.argv) != 2: # Here, we're checking that the user has provided exactly one argument: the hex number!
    print("Oh oh! Looks like you forgot to give me a hex to play with! 🙀\nPlease re-run the program with a hex number as argument!")
else:
    hex_value = sys.argv[1] # This is the command line argument i.e. the hex number the user has given us!

    # Et voilà!
    # Let's print out the binary equivalent of the given hex value!
    # And celebrate our success! 🥳
    print(hex_to_bin(hex_value))

# And there you have it! Super easy-peasy lemon squeezy, right? 🍋
# You've now got a cheerful little python script that can convert hexadecimals to binaries!
# Go on and spread the love of code, you fabulous programmer! 🚀🌟

