
# Woohoo! Let's start coding! I am excited about this project. It's all about fun and work at the same time.
# We're going to build a python script which aligns text to the left, center or right.
# The most fun part is - it's only CLI. Old school, ha?

def align_text(text, alignment, width):
    '''
    My good friend function here takes in three parameters:
    - text: The string we want to align. Yes, we are nothing without the text.
    - alignment: How we want our text aligned - left, right or center. We are flexible!
    - width: Total width for alignment. Cool huh?
    '''
    if alignment == 'left':
        # If we've selected "left", we'll use Python's built-in ljust function, with a cherry topping of width.
        return text.ljust(width)

    elif alignment == 'right':
        # Okay, "right" huh? Interesting! That's when we've the rjust function coming to action!
        return text.rjust(width)

    elif alignment == 'center':
        # We won't forget "center". Why should "center" feel left out? Here's the center function, to the rescue!
        return text.center(width)

    else:
        # Oh oh someone's playing with us. Called in a alignment that doesn't exist.
        # Let's politely tell them, their alignment doesn't exist.
        return 'Error: Invalid alignment type. Please choose: left, right, center.'

def main():
    '''
    Our main function, the captain of this ship.
    Let's test out our little script with it.
    '''
    text = "I'm a happy string!"  # Whoa! I'm one happy string to be manipulated.
    width = 30  # Feelin' a bit wide today.

    for alignment in ['left', 'right', 'center']:
        # Alright, let's show them our power, our flexibility! Center, Left, Right - we've got you covered!
        print(align_text(text, alignment, width))

# Calling captain! Let the fun time roll!
if __name__ == "__main__":
    main()

# And that's a wrap! Interesting, wasn't it? Now, every time you want to align a string and show off to your friends,
# You know which script to use. Happy coding, buddy!

