
# Welcome fellow Pythonistas! Time for some fun with number magic! 🎱🔮
# We're going to implement binary exponentiation, a super speedy way to calculate big powers of numbers.

# Let's begin!

def binary_exponentiation(base, exponent):
    """
    This function takes a base and an exponent and returns the result of the base to the power of the exponent. 🧮
    It uses the binary exponentiation method to achieve this in an efficient manner, so no big computation takes too long! ⌛😃
    """
    
    # We start off by setting our initial result to 1. This is because any number raised to the power 0 is 1, and we'll be building up from there.
    result = 1
    
    # Now we're going to start a loop that will last as long as our exponent is greater than 0.
    while exponent > 0:
        # The first thing we're going to do in this loop is to check if the current exponent is odd. We do this using the bitwise AND operator.
        if exponent & 1:
            # If it is odd, that means we have a power to account for now, so we multiply our result by our current base (which starts off as the initial base).
            result *= base

        # In both cases (the exponent being odd or even), we now square the base and divide the exponent by 2. 
        # This is the secret sauce to the binary exponentiation algorithm. 🍔🧂😄
        base *= base
        exponent >>= 1
    
    # Once the exponent is no longer greater than 0, we're done and we can return the result. 🎉 Tutti compiuto! 🥳
    return result

# And there you have it, folks! A quick, efficient, and simple implementation of binary exponentiation. 💪😎
# Now, let's try it out, shall we?

if __name__ == "__main__":
    # Let's find out what 3 to the power of 13 is. (Just for fun!)
    print(binary_exponentiation(3, 13))  # should give us 1594323

