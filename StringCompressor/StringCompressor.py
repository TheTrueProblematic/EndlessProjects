
# Hey there, fellow code explorer! 🚀
# You've just stumbled upon my little python gem, StringCompressor.py
# Here, we're all about squishing down those pesky, long strings into something a bit more manageable.
# Sit back, grab a cup of joe ☕ and let's dive right in!

def string_compression(input_string):
    """The heart and soul of our operation: string_compression function.
    
    This cool cat takes in a string and compresses it using the counts of repeated characters.
    For instance, the string 'aaabbbccc' would be compressed to 'a3b3c3'.
    However, if the "compressed" string isn't smaller than the original string, 
    we'll just return the original string. Handy, right?
    
    Parameters:
    -----------
        input_string (str): the string you want compressed.

    Returns:
    --------
        str: the compressed string... or the original string if it's shorter.

    """
    
    # First, we'll do some basic checks
    if not input_string:  # Is the string empty? If so, there's nothing to do here.
        return input_string 
    
    # Now, let's initialize some variables. 🏁
    output = ''  # This will hold our "compressed" string. It's empty for now.
    current_char = input_string[0]  # Start with the first character in the string.
    count = 0  # A counter to keep track of how many times a character repeats.
    
    # Now we'll loop through the string one character at a time. 👉
    for char in input_string:
        if char == current_char:
            count += 1  # If the char is the same as the current_char, increment the count.
        else:
            # If the char is different, it's time to update our output and current_char.
            output += current_char + str(count)
            current_char = char
            count = 1  # Start the count over for the new character.
    
    # Don't forget about the last set of characters!
    output += current_char + str(count)
    
    # Finally, we'll return the compressed string if it's shorter than the original string.
    # Otherwise, we'll return the original string.
    return output if len(output) < len(input_string) else input_string

# Now, let's test our function! 🧪
# Don't forget to remove this section when using this file as a module.
if __name__ == "__main__":
    sample_string = 'aabbbccc'
    print(f"Original String: {sample_string}")
    print(f"Compressed String: {string_compression(sample_string)}")

# And that's a wrap! 🌯 
# Thanks for joining me on this fun coding adventure. Until next time, happy coding! 🎉
