
# Hello there! I'm your friendly neighborhood programmer who wrote this script.
# This is like the cartoon guide for egyptian fractions. 🐪

# Is that not something you've heard of before? No worries!
# An 'Egyptian fraction' is a fraction that is being expressed as a sum of unique unit fractions.
# A unit fraction is a fraction with the numerator 1 and a positive integer as denominator.
# The fractions are fun, right? Let's make this journey together! 🚀

# We won't be using any external libraries, so your vanilla python installation is enough!
# All you need to do is to feed this bot, I mean script, with a fraction.

def egyptian_fraction(nr, dr):
    """
    This function expresses a fraction as a sum of unique unit fractions.
    :param nr: Numerator of the fraction
    :param dr: Denominator of the fraction
    :return:
    """
    # Woohoo! Nothing can stop us! Here begins the magic! 💫

    # An empty list to store the unit fractions
    ef = []

    # As long as numerator is not zero
    while nr != 0:
        # We find the ceiling of dr/nr which will be our unit fraction's denominator
        x = dr // nr
        if dr % nr:
            x += 1

        ef.append(x)

        # Since we've found one unit fraction, let's subtract it from our original fraction
        nr = nr * x - dr
        dr = dr * x

    # And there you have it! Your Egyptian fraction!
    return ef


def main():
    """
    This is where it all starts. The main function.
    The epicenter of the script! 🌋
    :return:
    """
    # Let's go, team! 🦸‍♀️🦸‍♂️
    # You and me, we can do it!
    nr = 6  # numerator
    dr = 14  # denominator

    ef = egyptian_fraction(nr, dr)

    print("Egyptian Fraction Representation of {0}/{1} is: ".format(nr, dr), end="")
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print("1/{0} + ".format(ef[i]), end="")
        else:
            print("1/{0}".format(ef[i]))


# Are you excited? Let's bring it on!!!
if __name__ == "__main__":
    main()
# And here we are, ready to wind up!
# Thanks for being on this adventurous ride with me!
# We did a great job! High Five! 👋

