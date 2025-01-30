
# Hello, fellow programmers!
# Welcome to AgeCalculator: The fun, fresh python script that'll calculate your age before you can say 'Happy Birthday'!

# In coding, and in life, simplicity is key. So, our trusty AgeCalculator sticks to the basics.
# No GUIs, no APIs, no Internet access, and no dependencies. And yes, of course, it's powered by our favorite language: Python.

# In true Python spirit, it's also cross-platform -- making it the perfect party trick, no matter whose computer you're using.

# Let's dive in, shall we?

import datetime  # This built-in module helps us tackle dates and times (critical for age calculation)

def calculate_age():
    # Whoa, slow down! Before we start any calculating, we need some user input.
    # Birth date. Simple, right?
    print("Please enter your birthdate (in DD-MM-YYYY format): ")
    birth_date = input()

    # Let's turn the birthdate from a string to a datetime object, which 
    # we can use to do all sorts of fun date-related adventures
    day, month, year = map(int, birth_date.split('-'))  # Divide the input into day, month and year
    birth_date = datetime.date(year, month, day)  # The birthdate, ready for action

    # But wait! We also need today's date. Again, Python's datetime module to the rescue 
    today = datetime.date.today()

    # Now for the actual calculation. A moment of silence please...
    age = today.year - birth_date.year  # Start by subtracting the birth year from the current year

    # But we're not done yet! We should also check if the birthdate has occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1  # If the birthday hasn't occurred yet this year, we take off 1 year from the age

    # Voila! The age, ready to be announced to the world (or at least to the user)
    print("You are {} years old.".format(age))

# And that's our script, my fellow coders!
# Indubitably, the epitome of "simple but effective"

# Let's wrap this up by actually calling our function (creating all that and not using it would be a waste!)
calculate_age()

# Thank you for joining us on this pythonic journey. Until the next script, keep coding!

