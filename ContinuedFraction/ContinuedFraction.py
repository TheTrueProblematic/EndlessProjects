
# Hey there, joyful coder!
# This is a gleeful Python script called ContinuedFraction. 
# Its sole purpose in life is to calculate the continued fraction representation of a rational number.
# So let's dive right in and have some fun with math and Python!

def continued_fraction(numerator, denominator): 
    # This function takes a numerator and denominator, 
    # and it gives you back the continued fraction representation. How cool is that?

    # Here we have the python's list to hold our continued fraction representation.
    cf_representation = []

    while denominator: 
        # We'll keep going until our denominator is exhausted.
        # (Or as exhausted as a number can be. Numbers don't get tired like we do.)
        
        quotient = numerator // denominator
        cf_representation.append(quotient)
        numerator, denominator = denominator, numerator % denominator
        # Here it is! The magical line of code that makes everything work.
        # We're updating our numerator and denominator for the next cycle of the loop,
        # and we're using Python's fancy simultaneous assignment to do it in one line.
        # Isn't Python wonderful?
    
    return cf_representation # Voila! We've got our continued fraction representation.

# Here we are, at the end of our script. 
# All that's left is to print out our function results to the command line.
# You can add command line arguments using argparse or similar to make this script work with any input.
# But for now, I'm just going to use a test case: the continued fraction of 31415/27182.
# You can change these numbers to anything you like, and it'll still work. That's the power of coding!
print(continued_fraction(31415, 27182))  

# Isn't coding just the best?
# Hope you have as much fun using this script as I had writing it!

