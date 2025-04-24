
# Howdy, partner! Welcome to our little Python rodeo!
# We're going to have ourselves a grand ol' time writing a program
# to check if a string is a valid palindrome. That means it's the same
# backwards as it is forwards, ignoring spaces, punctuation, and case.

# I reckon we'll do a little thing called importing the string module
# We won't be going online or importing any shiny new packages, don't you worry
import string

# Let's git to defining our main function
def is_palindrome(input_string):
    # First thing's first: we've gotta make sure our string doesn't have any pesky punctuation in it
    # We'll use a fancy thing called a translation table to get this done
    translator = str.maketrans('', '', string.punctuation)

    # Now we'll actually get rid of that punctuation
    stripped_string = input_string.translate(translator)

    # Spaces are just as pesky, so let's get rid of them bright and early
    stripped_string = stripped_string.replace(" ", "")

    # Making sure we're not case-sensitive, so let's make everything lower-case
    stripped_string = stripped_string.lower()

    # Now for the fun part: checking if our new-fangled stripped_string is a palindrome!
    # We'll just compare it to its reversed self
    return stripped_string == stripped_string[::-1]

# Time to test our function
print("Is 'A man, a plan, a canal: Panama' a palindrome?")
print(is_palindrome('A man, a plan, a canal: Panama'))  # This should print True

print("\nIs 'Just a regular string' a palindrome?")
print(is_palindrome('Just a regular string'))  # This should print False

# That's all, folks! Hope you had as much fun as I did.

