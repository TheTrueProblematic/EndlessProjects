
# Hello there, friendly folks! Welcome to our super-snazzy simple spell checker!
# This little friend will help us check the spelling of words in a string using a predefined dictionary.
# The super-cool thing about this is that we can run it directly from our command line interface (CLI) - no fancy GUIs here, my friends! 

# Since we want to keep things simple and easy, we've made sure that this script has absolutely no dependencies. 
# That means you won't need to install anything extra. It's a solo act, baby!
# And guess what? This doesn't access the internet or use any APIs. We're keeping it totally off-grid, for those of you who love a bit of digital detox!
# On top of that, we've made our little spell checker multi-platform capable - it'll run smoothly no matter what computer you are using.

# So enough of the intro, we're sure you're eager to see how this beauty works. Let's dive in!

# Here goes:

# We start by defining a dictionary of correctly spelled words. Now, this is a simple, basic dictionary. 
# Of course, you can make your dictionary as big and complicated as you want. But for demonstrations, let's stick to basics.

correct_spelled_words = {"hello", "world", "python", "script"}

# Now we define a function that will act as our spell checker.
# This function will take a string of words and check each word with our pre-defined dictionary.

def spell_checker(text):
 
    # Let's first normalize our text to lower case and split it into words
    words = text.lower().split()

    # Now let's find out which words in our text are not in our dictionary (aka possibly misspelled)
    misspelled_words = set(word for word in words if word not in correct_spelled_words)

    if misspelled_words:
        print(f"Oops, seems like we have some spelling errors! These words don't match our dictionary: {misspelled_words}")
    else:
        print("Yay! All words in our text are correctly spelled as per our dictionary.")
        
# Well, that's it - our friendly and simple spell-checker is all ready to go. 
# We can't wait to see how well it serves you in your text-checking pursuits. And remember - no matter how complex the code, keep the fun in it!

