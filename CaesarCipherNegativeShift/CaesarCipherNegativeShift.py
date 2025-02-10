
# Howdy! Welcome to "CaesarCipherNegativeShift". I hope you are excited to read this as much as I was when writing it! Let's go!

# We all love a bit of Roman History, don't we? Julius Caesar, a flamboyant character from history, used to communicate with his generals using a simple encryption technique. Turns out, we still love and use it as the Caesar Cipher.

# Our goal is to take this to the next level and shift it negatively too! Sounds fun, doesn't it? To do this, we'll be using nothing but Python - as pure as a Python can get.

# First things first, let's define our alphabet. Nothing hard about it - just good old a to z!
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Let's create our function to handle CaesarCipher with negative shifts!. We've named it caesar_cipher. It takes two input parameters - your message and the amount of shift.
def caesar_cipher(text, shift):

    # An empty string to hold our encoded message. Let's call it encoded_text!
    encoded_text = ""

    # Now, let's get to each character in our input message. We'll process them one by one!
    for character in text:

        # Now, we need to consider if our character is a letter. For that, let's check if it's in our alphabet!
        if character in alphabet:

            # Bingo! We have a letter. Let's find its index in the alphabet to start our fun.
            old_index = alphabet.index(character)

            # At this point, we'll calculate the new index by adding our shift to the old index.
            # To handle a negative shift and ensure our result remains in the alphabet's range,
            # we add len(alphabet) to the shift. Sneaky, isn't it?
            new_index = (old_index + shift) % len(alphabet)

            # Time to get the corresponding letter from our alphabet and add it to our encoded text!
            encoded_text += alphabet[new_index]

        else:
            # What do we do with non-alphabetic characters? Well, we just pass them as they are into our encoded text.
            encoded_text += character

    # Boom! We have our encoded text ready. Let's share it with the world!
    return encoded_text

# Wonderful! Looks like we're all done. Now let's go and crack some secret messages!
# Feel empowered and experience the feel of being a Roman Emperor, breathe the Caesar Cipher. Remember, the world is your oyster!

# Have fun and keep coding!
