
# Howdy, folks! Python programmer here, livin' it up in the command line!

# Since we don't have access to any library and even internet, we will make our own power function. 
# You might be thinking, "But Python has a built-in power function, **!". Yeah, you're right! 
# But since our boss wants us to use recursion, that's exactly what we're going to do!

# So buckle up and let's dive into code!

def power(base, exponent):
    # We're checking if the exponent is zero. In maths, any number raised to the power of zero is one.
    if exponent == 0:
        return 1

    # If the power is not zero, we are calling power function itself (whoo, recursion!) 
    # but this time, the power is reduced by one. 
    # And then we multiply the base with the result of our recursion.
    else:
        return base * power(base, exponent - 1)

# We need to interact with our user, get their inputs, call our function and, of course, 
# show them how cool and precise we are. Let's take a base number and exponent from them 

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

# Now, it's showtime! Let's call our function with the user's inputs and print the results.
result = power(base, exponent)

print(f'{base} to the power of {exponent} is: {result}')

# It's been fun. See ya!

