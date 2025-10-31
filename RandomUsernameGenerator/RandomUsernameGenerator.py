
"""
Hey there, happy programmer! 
Welcome to our magnificent little program: RandomUsernameGenerator. 
Our mission is simple - to entertain you by generating random, fun, and quirky usernames. 

Let's dive in, shall we?
"""

# To generate some randomness, we'll start with the random module.
import random

# Here are our lists of adjectives and nouns for the username. 
# Feel free to spice things up and add more words! 
adjectives = ["happy", "jolly", "dreamy", "sad", "angry", "pensive", "focused", "sleepy", "quiet", "loud", "quick", "slow"]
nouns = ["apple", "dinosaur", "ball", "toaster", "goat", "dragon", "hammer", "duck", "panda"]

# Main function: generates a username by combining a random adjective and a random noun. 
def generate_username():
    # Select a random adjective and a random noun.
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    # Combine them into a username and return it!
    username = adjective + noun 
    return username

# Let's create some fun usernames!
for i in range(10):
    username = generate_username()
    print(username)

"""
Well, that was a blast, wasn't it? 
Feel free to run the program again for a fresh new set of usernames! 
Happy coding, fellow Pythonista! :)
"""


