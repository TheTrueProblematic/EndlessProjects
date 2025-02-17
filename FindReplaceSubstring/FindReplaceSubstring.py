
# Hello, fellow Python lovers! Isn't Python such a lovely language? 
# It's like a friend who's always got your back, ready to lend you a helpful hand (or should I say, a helpful "import") when you're in need.
# This time we're having a bit of fun with strings. Yes, Python strings, those sequences of characters that we all love (and sometimes love to hate)!

# So what are we doing exactly? We're writing a Python script that finds and replaces all instances of a substring within a string. 
# It's like playing hide-and-seek with characters!

def find_and_replace(input_string, substring_to_find, substring_to_replace):
    """
    This function takes an input string, and replaces all instances of the "substring_to_find" 
    with the "substring_to_replace".
    
    Parameters:
    input_string (str): The original string
    substring_to_find (str): The substring that needs to be replaced
    substring_to_replace (str): The substring with which to replace the original substring

    Returns:
    (str): The output string after replacement
    """
    # Python's str.replace method is super friendly. It's going to help us replace all instances of the substring in one go. Isn't that awesome?
    return input_string.replace(substring_to_find, substring_to_replace)

if __name__ == "__main__":
    # Now let's have some fun! Let's substitute all the 'beautiful' Zs in the alphabet with the lovely 'Zebra' string!
    print(find_and_replace("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Z", "Zebra"))
    # Expect output: ABCDEFGHIJKLMNOPQRSTUVWXYPZebra

# There you have it! Simple, isn't it? That's one of the things I love about Python - it makes difficult things easy and fun.
# So next time you're caught in a string-quandary, remember this little script. It may just be the friend in need you were looking for. Happy coding!
