
# Hello, welcome to RandomQuote!
# This python script is here to share some wisdom (or humor) with you!
# Whenever you feel like needing a break, just launch this script and enjoy a random quote!
# The best thing is - it's developed with love and happiness!

# We're gonna need the randint function from the random module to pick our random quote
from random import randint

def main():
    # Let's create a list that holds all our awesome quotes
    quotes = ["Just because something doesn’t do what you planned it to do doesn’t mean it’s useless. - Thomas Edison",
              "Programming is like writing a book, except if you miss a single comma on page 126 the entire thing makes no sense. - Unknown",
              "Hardware: the parts of a computer that can be kicked. - Jeff Pesis",
              "In theory, there is no difference between theory and practice. But, in practice, there is. - Jan L.A. van de Snepscheut",
              "Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live. - John Woods",
              "Programming: A pastime similar to banging one's head against a wall, but with fewer opportunities for reward. - Unknown"]

    # Now, it's time to pick our quote of the day!
    # We'll use the randint function which will give us a random number between 0 and the length of our list (minus one because lists in Python start at 0)
    quote_of_the_day = quotes[randint(0, len(quotes) - 1)]

    # And... drumroll please... let's print our quote of the day!
    print(quote_of_the_day)

# Make sure we call our main function when the script is launched
if __name__ == '__main__':
    main()

