
# Hey there, happy coder! Welcome aboard the Python-flavored fun train!
# Today, we've got a nifty trick for you called 'BinaryToDecimal' 
# which, yes you guessed it right, converts binary numbers into their equivalent decimal form. How cool's that!

# We start by defining our amazing function. Hold onto your hats, off we go!
def binary_to_decimal(binary):
    # Our binary number might be scared of us right now. It's hiding as a string!
    # So, we need to convert it to an integer first. Integer to base 2, of course. That's how binaries roll!
    binary = int(binary, 2)

    # As simple as it sounds, we just return our shy binary number, 
    # now proudly turned integer! Talk about transformations *wink*
    return binary

# As our beloved function is quite shy too, it won't run on its own. 
# We use this strapping main function to give it a little nudge.
def main():
    # Get the binary number to convert. The water's warm, promise!
    binary_input = input("Enter the binary number to convert into decimal: ")
    
    # Run our binary_to_decimal function and print the incredible results.
    # All under the safe cover of try, except. Because hey, exceptions happen!
    try:
        print("The decimal form of the binary number is: ", binary_to_decimal(binary_input))
    except ValueError:
        print("Oops! Seems like the input isn't a valid binary number. Try again, will you!")

# This is where we tickle Python's belly and it runs the main function. 
# Such a ticklish creature, Python is!
if __name__ == "__main__":
    main()
    
# And voila, we're done! As simple as it can get! Give yourself a pat on the back, you're killing it!
# Thank you happy coder, for taking this glorious ride with us! Until next time.

