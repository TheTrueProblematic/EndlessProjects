
# Hello fellow programmer, welcome to our Mad Libs game! 
# Isn't it fun to code stuff that can make people laugh and entertain them? 
# Nothing cheers up a rainy day like a little Mad Libs fun, don't you think?

# Alright, let's dig in!

# First, we need to ask our user to provide some words to fill in our story's blanks.
# We'll need a collection to store our user's precious entries, let's go for a dictionary.
# Python's input() function will be our friend here!

def collect_words():
    words_dict = {}

    print("Welcome to our Mad Libs game! Please, provide some words to fill in the blanks:")
    words_dict['adjective'] = input("Please enter an adjective: ")
    words_dict['verb_past'] = input("Please enter a past tense verb: ")
    words_dict['noun'] = input("Please enter a noun: ")
    words_dict['adverb'] = input("Please enter an adverb: ")
    
    # There we have it! We've got all our words.
    # Quick and easy, right? Well, that's the power of Python. ;)

    return words_dict

# Now the meaty part: our Mad Libs tale! We'll insert the user's words into our story's blanks.
# We shall use Python's fabulous .format() method to fill our tale with user-provided words!

def create_story(words_dict):

    # Let's write our little tale:
    print("""Once upon a time, in a {} forest, a fox who had {} too much 
    decided to pick up a new hobby: {} sweeping! 
    The fox went about it {}""".format(words_dict['adjective'], words_dict['verb_past'], 
    words_dict['noun'], words_dict['adverb']))

# You see? That wasn't hard at all! Now let the hilariousness ensue!

# We shall now combine our functions in a main function, because clean, organized code is happy code!
def main():
    words_dict = collect_words()
    create_story(words_dict)

# And now we shall use Python's delightful __name__ == "__main__" idiom.
# This will execute our game only when the script is run directly, not when imported. 
# Security first, friends!

if __name__ == "__main__":
    main()

# And voilá, our beautiful little Mad Libs game is ready to roll!
# Why don't we give it a spin?
# Have fun! And remember: the world needs your code. Keep on rocking!
