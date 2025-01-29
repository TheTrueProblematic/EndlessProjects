
# Hello, fellow Pythonistas! 👋 Welcome to the exciting journey of AlternateCaps.
# This fun little script will, quite capriciously, decide to capitalize even and odd indexed characters in your strings.
# Just because it can! 😁

# Now, watch the Python magic perform in your console without any GUI, Internet, API, or pesky dependencies. 🐍

# Our powerful wizard (also known as Python 😋) that helps us in this task, is multi-platform capable. 🌍
# So don't worry, no matter if you're team Windows, macOS, Linux, or secretly thinking about switching to another OS, 
# the AlternateCaps magic will work for you anyway. 💼

# Let's get the enchantment started!

# We will begin by defining our wonderful function print_alternate_caps()

def print_alternate_caps(your_string):

    # Now, isn't this fun? We take the string you provided and turn it into a list! 📝
    altered_letters = list(your_string)

    # Hold on! Because we're about to take a crazy roller coaster ride through each character of your string! 🎢
    for i in range(len(altered_letters)):
        # Our roller coaster takes a different path depending on whether the index is odd or even!
        # If it's an even index, it bravely decides to capitalize the character! 💪
        if i % 2 == 0:
            altered_letters[i] = altered_letters[i].upper()
        # If it's an odd index, it modestly decides to stay in lower case! 🙈
        else:
            altered_letters[i] = altered_letters[i].lower()

    # After this wild adventure, we join all the characters back together into a string! 💖
    your_string = ''.join(altered_letters)

    # And finally, we reveal the magic! Voila! 🎉
    print(your_string)

# Welcome, dear user! Please enter a string to see the magical transformation. ✨
user_string = input("\nHey you! Yes, you. Type out any string:\n")
print_alternate_caps(user_string)

# There you go! You've just witnessed the crazy magic of AlternateCaps. 🥳
# Thank you for being part of this quirky Python adventure. Until next time! 💻
