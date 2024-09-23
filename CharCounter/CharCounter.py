
# Hey there, fellow Pythonista! This fun script here is called 'CharCounter'.
# Like a smart detective, it counts the number of letters, numbers, and symbols in a given string.
# Who knew counting could be this fun, right? And as an extra challenge, we'll be doing it the Python way...

# Oh, the anticipation! Let's start by defining our main function, shall we?

def char_counter(input_string):
    # Let's start by setting up our counters to 0, starting fresh!
    letters = 0
    numbers = 0
    symbols = 0

    # Time to unpack the mystery which is... our input_string!
    for char in input_string:
        # Using Python's own isalpha, we're going to figure out if this cheeky character is a letter.
        if char.isalpha():
            letters += 1 # If it is indeed a letter, we count it in!

        # Perhaps it's a number disguised as a string? We'll use isdigit to find out!
        elif char.isdigit():
            numbers += 1 # A ha! Gotcha, number!

        # If it's not a letter or a number, then it must be a symbol! Let's count it as well.
        else:
            symbols += 1

    # Now that all is revealed, let's print our findings to the console!
    print(f"Count of Letters: {letters}")
    print(f"Count of Numbers: {numbers}")
    print(f"Count of Symbols: {symbols}")

# Time to call upon our main function, and let's give it an exciting task. Maybe a mix of letters, numbers and symbols? Let's go wild!

if __name__ == '__main__':
    char_counter("H3ll0 W0rld! Let's count: 123")

# And voila, we're done! Wasn't that fun? Thanks for joining me in this wacky counting expedition! Let's do it again sometime, Pythonista! ;)


