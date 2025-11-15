
# Hi there! Welcome to our exciting journey into programming with Python! 😄
# Are you ready for an adventure across the fantasy world of town names? Let's go then! 
# This script is called RandomTownName

# First, we import the random module which is already built-in Python 🐍, 
# so we don't even need to install anything extra! How cool is that? 😉
import random
import string


# We start our adventure by creating a list of fantasy sounding syllables.
# Feel free to make it as fun and creative as you want to make each town unique and interesting!
SYLLABLES = ['gar', 'dem', 'mor', 'fay', 'shi', 'zar', 'pol', 'riv', 'mal', 'ash', 'thor', 'il', 've', 'kri',
             'na', 'ba', 'dal', 'far', 'hin', 'old', 'rin', 'ron', 'myr', 'vit', 'jander', 'hrast', 'bris', 'krand', 
             'bro', 'tark', 'gent']



# Now, we define our function generate_town_name.
# To make things exciting, we can generate town names of various lengths by combining the syllables!
# So, some towns may be short and sweet, others may be long and majestic. It's all down to sheer luck! 🎲
def generate_town_name(min_length=2, max_length=5):
    """
    A functions to generate a random town name by combining random syllables.
    The length of the town name (i.e., the number of syllables it comprises) 
    will also be determined randomly within the provided limits.
    """

    # Decide the length of the town name
    name_length = random.randint(min_length, max_length)

    # Individual syllables will be stored in this list before they are combined into the final town name
    name_parts = []

    for i in range(name_length):
        # Choose a random syllable and append it to name_parts
        part = random.choice(SYLLABLES)
        name_parts.append(part)

    # Combine all the individual syllables into the final town name
    town_name = ''.join(name_parts)

    # To make the town name look even more fancy, we make sure the first letter is always capital
    town_name = string.capwords(town_name)

    # And voilà, the town name is ready! 🎉
    return town_name


# This is like the orchestrator function, all the magic starts from here! 🎩
def main():
    # The mighty random town name generator starts here!
    town_name = generate_town_name()

    # Let's print out the town name!
    print(f"Welcome traveler, to the grand city of {town_name}!")


# If the script is being run (as opposed to being imported), start the adventure!
if __name__ == "__main__":
    main()

# That's all folks! Thanks for joining me on this transportation to a fantasy world, happy town-hopping! 🌁🏯🌃
