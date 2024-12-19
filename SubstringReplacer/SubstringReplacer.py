
# Hey fellow Pythonista! Welcome to the SubstringReplacer script.
# This handy little tool is all about replacing substrings in a text, and it's just as excited to get going as you are!
# Fun and functionality, all wrapped up in one neat package of Python code. So let's dive right in!

# First things first: defining a function "replace_substring" with the parameters of input_string, old_substring, and new_substring.
def replace_substring(input_string, old_substring, new_substring):
    # Guess what?! Python has a built-in method for string objects that does exactly what we need!
    # It's called "replace" and it's super easy to use. All we have to do is:
    # - Specify the substring we want to find (old_substring)
    # - Specify what we want to replace it with (new_substring)
    # Python will then happily trot off and replace all occurrences of old_substring with new_substring in input_string.
    # And it'll do it without complaint, even if the substring occurs a zillion times. What a champ!
    return input_string.replace(old_substring, new_substring)

# Now that our function is defined, let's move on to collecting user input from the command line.
# We'll use the built-in "input" function for this. It's simple and does the trick wonderfully.

# Grab the initial string from the user.
print("Enter the text that you wish to work with:")
text = input()

# Don't forget the old substring!
print("Enter the substring that need to be replaced:")
substring = input()

# And finally, get the new substring.
print("Enter the new substring to replace the old one:")
replacement = input()

# Now that we have our inputs, it's time to put our function to work.
result = replace_substring(text, substring, replacement)

# Let's print out the result to the console so the user can see the fruits of their (and our) hard work.
print("\nVoila! Here's your new text:")
print(result)

# And we're done! That wasn't so bad, was it?
# This script is a friendly reminder of how cool Python is allows us to create powerful things with simple, readable code.
# Keep Python-ing and catch you on the flip side!
