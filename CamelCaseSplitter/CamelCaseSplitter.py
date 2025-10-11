
# Hey there! Welcome to the CamelCaseSplitter module.
# We're here to take those stiff, stuck-together CamelCase words,
# and give them a little space to breathe.
# So, let's not just stand around, let's dive right in and split some words!

# And just a quick note, this module is perfectly capable 
# of running without any dependencies, on a brand new Python installation,
# because who has the time to set up dependencies, am I right?

import re

# Define our main function
def camel_case_splitter(camel_case_string):
    """
    A function to split a CamelCase string into separate words.
    
    Parameters:

    camel_case_string (str): The string in CamelCase format that needs to be split

    Returns:

    str: A string of separated words
    """

    # Let me explain the magical pattern matching happening here:
    # we are identifying words in a string that start with a lowercase letter(s),
    # followed by uppercase letter(s),
    # and this pattern may repeat for multiple words. Got it? No? It's okay, it takes time.

    words = re.findall('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', camel_case_string)

    # Now that we collected all the words let's join them back with spaces
    # to create a smooth sentence. It's like we're giving the words a nice little yoga stretch.

    spaced_string = ' '.join(words)
    return spaced_string

# And that's it! Easy peasy lemon squeezy. Go ahead and run the script with your favorite CamelCase phrases!
# Now kick back, relax and rejoice in the beauty of separated, free-flowing words.

# Life is good when code is fun, isn't it?
