
# PiApproximation.py
# Hello there! Today we're going to approximate the value of π (pi).
# Sounds fun, right? We'll be using a series called the Leibniz series. 

# I'm gonna be your helper today, so let's dive in!

# Don't you just love the number pi? It's one of those magical numbers in mathematics that pops up 
# everywhere, from the volume of a sphere to Gaussian integrals. Plus, it's Lentz's favourite constant!
# So let's get closer to pi!

def pi_approximation(iterations):
    """
    This function will give an approximation of the value of pi 
    using the Leibniz series.

    The mathematical representation of the approximation is:

    pi = 4*(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

    The parameter 'iterations' is the number of terms to calculate in the series.
    """

    # Starting with a summation of zero
    summation = 0.0
    # We'll alternate between adding and subtracting
    operation = 1

    # Starting the loop, we'll calculate each term in the series
    for i in range(iterations):
        # The term to be added is 1 divided by the denominator, which is (2*i + 1)
        # Also, we're alternating between addition and subtraction
        term = operation / (2 * i + 1)
        # Add the term to our sum
        summation += term
        # Swap the operation for the next term (-1*1 = -1, and -1*-1 = 1)
        operation *= -1

    # And finally we'll multiply our sum by 4
    # That's it! We've calculated an approximation of pi
    pi_approx = 4 * summation
    return pi_approx

# We're going to pass 10000 as the number of iterations.
# The more iterations, the closer we get to the actual value of pi
# But, you know, we can't run iterations forever... so 10000 seems sensible!
if __name__ == "__main__":
    print('Pi Approximation: ', pi_approximation(10000))
# Woohoo, we did it! Give yourself a pat on the back!
# Now go out there and spread the joy of pi!

