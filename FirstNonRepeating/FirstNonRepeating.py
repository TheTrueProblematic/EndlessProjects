
# Hello, fellow programmer! You are about to dive into a fun piece of code that finds the first non-repeating character in a string!
# So sit down, buckle up, and enjoy the fun ride. 🎢

# Import our one and only necessary library for this.
from collections import OrderedDict

def firstNonRepeating(input_string):
    """
    Function to find the first non-repeating character
    Bakes in a delicious OrderedDict to keep things in order!
    
    input_string: string, the string to be processed 
    """

    # Let's create an ordered dictionary, because order matters in the kitchen, and in our string!
    ordered_dict = OrderedDict()

    # Iterate over all characters in the string.
    # If we've seen it before, increment the count, otherwise set it to one.
    for character in input_string:
        if character in ordered_dict:
            ordered_dict[character] +=1
        else:
            ordered_dict[character] = 1
            
    # Now we've stored all characters and their counts.
    # Time to check our order preserved menu and find who gets the first "non-repeating" trophy
    for key, value in ordered_dict.items():
        if value == 1:  # found a character that occurs only once i.e., a non-repeating character.
            # and it holds the first order as well
            return key

    # If we've reached here, every character repeats at least once, so there's no non-repeating character.
    # Bummer! But gotta handle all cases, right?
    return None

# Firing off the test ride -> all aboard! 🚀
print(firstNonRepeating("PythonRocks"))  # Should output 'P'

# Voila! 🎉 You've reached the end of our fun python script.
# Now you have a handy function to find the first non-repeating letter in a string.
# Keep coding, keep learning and keep having fun! 🐍💻

