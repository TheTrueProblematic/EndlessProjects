# Our joyous python journey begins here with our VowelCounter python script. Yay!

# Now, here's something to keep in mind, we're making a super cool program that will count the vowels in a given string. Fun, right? Now unstow your seat tray and keep your seats in the upright position, we're ready to take-off!

# The rules of engagement: no GUI, no dependencies, no API or internet access, must be multi-platform capable. Ha, easy-peasy for us!

# So hold tight, keep your smiles wide, we're diving right in!



# Let's kick things off with defining our main function. This will be the heart of our program.
def count_vowels(input_string):
    """A function to count vowels in a given string"""
    
    # Let's establish something. In English, we have five beautiful vowels.
    # Good ol' a, e, i, o, u. Let's make sure our function knows them.
    vowels = 'aeiou'
    
    # We'll count our vowels using a simple count method on our string,
    # where the vowel is our iterator going through one vowel at a time. Neat, huh?
    return sum(1 for char in input_string if char.lower() in vowels)

# Alright, with the brains of our program sorted, let's ask our user for input.
# We're using the raw_input() function here, which waits for the user to type something in the console before progressing.

input_string = input("Type a string, and I’ll count the vowels for you: ")

# Let's acknowledge our user's effort! We thank them, and then utilise our very brainy function to present them with the vowel count.

print(f"Thank you! The number of vowels in your string is: {count_vowels(input_string)}")

# And... cut! That's a wrap, folks! Our vowel-counting starlet is ready for the limelight!



# We hope you enjoyed your journey with us today on this pythonic adventure. Watch out for vowel monsters, but now you have just the tool to count them all! Happy coding!