
# Hello there, awesome programmer! I am so stoked to have you here.
# The file we're gonna be looking at today is called SnakeToCamel.
# You dare guess what it does? Oh yeah, you're right. We're going to be converting snake_case identifiers to CamelCase.

# Let's get started, mate!

# First off, as always, let's use our favourite language, Python. Because what else, right?
# The beauty of Python is that it doesn't need any kind of GUI, dependencies, not even the internet. 
# I mean, who doesn't love Python, right?

# Alright, so down to business. What we are going to do is write a function to convert snake_case identifiers to CamelCase.
# Let's name that function 'convert_to_camel' because, well, it's fun.

def convert_to_camel(snake_str):
    """Convert a snake_case string to CamelCase"""
    # Split the string by underscore - it is how we catch those pesky little snakes!
    words = snake_str.split('_')
    
    # And now, for the magic trick! We're going to capitalize the first letter of each word,
    # and then join them together. The result - a beautiful CamelCase from an ugly snake_case.
    camel_word = ''.join(word.title() for word in words)
    
    # And tada! Here it is, our proudly converted CamelCase word, ladies and gentlemen!
    return camel_word

# Finally, let us allow our script to take the snake_case identifier as a command line argument. 
# This will allow us to run the script right from the terminal which is just plain awesome!
if __name__ == "__main__":
    import sys   # We import the sys module, but don't worry because it comes bundled with Python!

    # Now we made sure that our script has been run directly, and isn't imported as a module, let's jump right in!
    # The first command line argument is the script name itself, and the second one is our dearest snake_case identifier.
    if len(sys.argv) > 1:
        snake_case_identifier = sys.argv[1]
        print(convert_to_camel(snake_case_identifier))
    else:
        # Hang on, you did remember to pass your identifier, right?
        print("Oops, looks like you forgot to provide the snake_case identifier!")

