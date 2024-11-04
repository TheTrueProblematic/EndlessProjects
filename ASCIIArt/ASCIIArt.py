
# Woohoo! It's ASCII art time! This tiny little script is a magician.  
# It takes text or patterns and turns them into enticing little bits of ASCII art! 
# One might wonder, how can one create beautiful art on a humble console?
# Well, let's dive in and see!

# We would usually import a library or two here, but hey, we're playing by the rules, so we're doing this on vanilla Python, baby!

def draw_ascii_art(text, pattern):
    # Let's draw some ASCII art! We get our text and our pattern, and we're ready to rock and roll.

    # Just a little validation – we want to make sure our text isn't empty.
    # No text, no art. That's the rule!
    if not text:
        print("Oops! It looks like you forgot to give me some text to work with. Better luck next time!")
        return

    # And we need a pattern, too. The pattern is the soul of our ASCII art, after all!
    if not pattern:
        print("Oops! It looks like you forgot to give me a pattern. I can't create art without a brush!")
        return

    # Alright, we're off to the races. Let's start by creating an empty canvas for our ASCII art.
    ascii_art = ""

    # Now here comes the fun part – we'll cycle through our text, character by character.
    for char in text:
        # We'll take each character, and replace it with our pattern.
        # This is the essence of our ASCII art.
        ascii_art += pattern.replace('*', char)
        # And just for a little readability, let's add a line break after each character. 
        ascii_art += '\n'

    # And voila, our masterpiece is complete! Time to unveil it to the world.
    print(ascii_art)

# All right, now that we've got our brush and canvas, let's make some art!

draw_ascii_art("HELLO", "*")
draw_ascii_art("WORLD", "*")

# Magnifique! So simple, yet so elegant. Who knew we could create such beauty in the console, right?
# Till next time, keep creating!


