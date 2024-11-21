
# Hey there, fellow traveller of the code cosmos!
# Strap in for another adventure! Let's ride!
#
# Today's heroic quest, should you choose to accept it,
# is to craft a shiny, blazing CharHistogram, a device of such magnificent
# splendor that it simply radiates coolness (or heat, if you prefer).
#
# This divine creation will generate a histogram displaying
# the splendid occurrence of each marvelous character in a given string.
# Downright handy, don't you think?
#
# Fear not! This Python script is CLI-based. Curious, isn't it, how we're
# able to weave such intricate stories of drama and suspense through a mere command line?



def character_histogram(input_string):
    """A function that reveals the frequency of each character in a whimsical string."""
    # Pull your seat belts tight, we're about to get started.

    # First things first. We've got to make a home for our data.
    histogram = {}

    # Now let's nab each character from the string. Sneaky, eh?
    for character in input_string:
        if character in histogram:
            # If we've spotted this character before, up the count!
            histogram[character] += 1
        else:
            # If this character is a new discovery, add it to our treasure trove!
            histogram[character] = 1
    # Bingo! A wild histogram appears!

    return histogram


def print_histogram(histogram):
    """A print function to display our stunning histogram."""
    # Prepare to unleash the beauty upon the world! Brace yourselves, for here comes the histogram!

    for character, frequency in histogram.items():
        # Print each character alongside its frequency. A match made in heaven!
        print(f"'{character}': {frequency}")


def main():
    """A magical main function where our journey begins!"""
    # Energise the engines! We're heading into the unknown!

    # Fetch us a cool string from the command line, will ya, mate?
    input_string = input("Enter a cool string: ")

    # Generate that sumptuous histogram! Feel the power!
    histogram = character_histogram(input_string)

    # Behold the grand spectacle that awaits you! Reveal the histogram!
    print_histogram(histogram)


# Here we go, hitting the hyperspace button at the speed of Python!
# Fingers crossed, let the magic happen!
if __name__ == "__main__":
    main()
