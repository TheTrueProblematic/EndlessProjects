
# Hi there, fellow coder! Welcome to this exciting RandomArtASCII program!
# This is all about generating random ASCII art patterns, because, let's face it, who doesn't love art?
# Blow off some steam, sit back, and let us generate some ASCII magic for you!

import random  # of course, we need random. Where would we be without it?

def random_art(width=40, height=40):
    """
    Generates random ASCII patterns by utilizing the random module and ASCII characters.
    
    Parameters:
    width (int): The width of the ASCII art (default: 40)
    height (int): The height of the ASCII art (default: 40)

    Returns:
    None
    """
    
    # I chose these characters because they give a pretty neat effect when printed out, but feel free to experiment!
    chars = ['@', '#', '$', '%', '&', ' ', ' ']
    
    # Time to create that beautiful ASCII art!
    for i in range(height):
        for j in range(width):
            print(random.choice(chars), end="")  # the beauty of randomness!
        print()  # Starting a new row
        
# Now let's put this beautiful function to use! And make some art!
if __name__ == '__main__':
    random_art(60, 30)

# And voila, we're done here! Just like life, each running of the script is different and unique.
# Hope you have as much fun using this script as I had creating it! Happy ASCII Art-ing! 

