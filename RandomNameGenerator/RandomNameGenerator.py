
# Hello there, fellow coder! I'm your friendly Python script that generates random human-like names
# (from given lists of syllables). Invite me to your tea party anytime by typing `python RandomNameGenerator.py` 
# in your command line, and voila, fascinating names will come to life!

# So, seatbelts fastened and let's start this fun journey code!


import random

# Array of possible syllables
syllables = ['ba', 'be', 'bi', 'bo', 'bu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu',
             'ga', 'ge', 'gi', 'go', 'gu', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 
             'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
             'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
             'xa', 'xe', 'xi', 'xo', 'xu', 'ya', 'ye', 'yi', 'yo', 'yu', 'za', 'ze', 'zi', 'zo', 'zu']

def generate_name(syllables, min_length=2, max_length=5):
    # Here I am, making a random name.
    # Yes, you heard it right -
    # Not just a string of random characters, 
    # but an human-like name.
    name_length = random.randint(min_length, max_length)
    name = ''.join(random.choice(syllables) for _ in range(name_length))
    return name.capitalize()

# Now, let's make some random names and cheer!

for _ in range(10):
    print(generate_name(syllables))

# Oh, look at the names! Aren't they fascinating?
# Now you have some new friends ready to be populated in your imaginary world.
# Feel free to access this any time!
