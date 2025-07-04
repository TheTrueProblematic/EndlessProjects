
# Woohoo, coding time! Welcome to FracSimplifier!
# This little beauty will take your fraction and simplify it to its lowest terms.
# All you have to do is feed it a numerator and a denominator and, BOOM, out comes your simplified fraction!

from math import gcd  # We're importing gcd from math. These are the only bags we’ll be packing for this journey!

def simplify(numerator: int, denominator: int):
    """
    Returns a tuple that represents a simplified fraction.

    Args:
        numerator (int): The numerator of the fraction.
        denominator (int): The denominator of the fraction.

    Returns:
        tuple: A simplified fraction (still fabulous) in the form of (numerator, denominator).
    """

    # Good ol' gcd! You can always have fun with the greatest common divisors!
    greatest_divisor = gcd(numerator, denominator)

    # Now we're going to use our shiny gcd to simplify our fraction. So exciting!
    simplified_numerator = numerator // greatest_divisor
    simplified_denominator = denominator // greatest_divisor

    return simplified_numerator, simplified_denominator


"""
Remember, the best way to start is simply to start! Feed simplify() with a numerator and denomincator like this:

- numerator, denominator = simplify(18, 48)

Then do a little print action to see the magic:

- print(f"Simplified fraction: {numerator}/{denominator}")

So easy, so fun, so simplified!

"""

# That's it, folks! Until next time: happy coding!

