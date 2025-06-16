
# Oh hey there! I see you're looking into this Python file.
# Well welcome aboard, you're in for a ride. That's right, it's a fun journey
# from any number in any base to a beautiful decimal.
# So strap in, and let's get converting!

import sys

def base_to_decimal(number, base):
    """ Convert a given number from a specified base to decimal. """
    # See, the thing is, python is kinda a genius in making things pretty simple.
    # So simple that conversion to decimal is as easy as int() makes it. Neat, right?
    return int(number, base)

def main():
    # OK, first thing first we need to fetch the base and the number from our command line.
    # And python has this super cool library 'sys' just for that.
    base = int(sys.argv[1])
    number = str(sys.argv[2])
    # Why use str for numbers you ask? Well, we are flexible with our bases
    # So the numbers could be anything between 0-9 or a-z. So let's just
    # play safe and treat them as strings for now.

    # Alright! Now, let's get down to some fun business and do our conversion.
    result = base_to_decimal(number, base)
    
    # And now for the cherry on the top, let's print that result.
    print(f"The decimal of your number {number} in base {base} is: {result}.")

if __name__ == "__main__":
    main()
# Well, that's about it! I told you it's going to be a fun journey, didn't I? 
# Reach out whenever you want to travel from a random base to a decimal, okay? 
# This little old script will always be here to guide you.
# Til next time pal, happy coding! 

