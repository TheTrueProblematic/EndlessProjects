
# Hello there fellow programmer!
# So great to have you here cracking this unique little secret called - 'UniqueChars'
# Let's go ahead and find all unique characters in a string...and hey, don't forget to grab your hot cup of coffee ;)

def unique_chars(some_string):
    # Built our own little unique cave to store the unique characters
    unique_cave = []

    # Now, let's dive into this string
    for character in some_string:
        # Check if the character has already been discovered in our cave (set)
        if character not in unique_cave:
            # Oh look, a new character! Let's add it to our cave
            unique_cave.append(character)

    # Phew! Done. Let's join them all and present our findings
    unique_string = ''.join(unique_cave)

    # Worship the unique string, it's really precious
    return unique_string

# Now, to make things interesting, let's give it a default string to work through
# whenever there's no input provided
def main():
    # Your trial string goes here. Give it an unexpected wild entry and see how our 'UniqueChars' tackles it
    trial_string = "GoodDayGoodPeople"

    # Uncover the secret hiding in the string!
    print(unique_chars(trial_string))

# Alright folks, stepping up the main game
if __name__ == "__main__":
    main()

# Congratulations! You've just completed your journey of finding all unique characters in a string.
# Don't forget to get overexcited and tell your friends about the happy time you spent here.
# Happy Pythoning till we see you next time!

