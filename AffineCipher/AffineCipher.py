
# Welcome to HappyCoder's cheerful Affine Cipher Python module!
# Grab your coffee, put up your feet, and enjoy the ride!

# We only need built-in Python tools for this adventure
import math

# All English letters - that's a party of 26!
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The fun begins here, time to encode!
def encode_affine_cipher(message, a, b):
    """Encode a message with the Affine Cipher."""
    # Let's keep all the text uppercase, just to keep things simple and fun
    message = message.upper()

    # Compute inverse of a (modulo size of the alphabet)
    a_inv = pow(a, -1, len(LETTERS))

    # Now, time for the actual encoding!
    # Just a simple application of the Affine Cipher formula
    encoded = []
    for character in message:
        if character in LETTERS:
            idx = LETTERS.index(character)
            encoded_char = LETTERS[(a * idx + b) % len(LETTERS)]
            encoded.append(encoded_char)
        else:
            encoded.append(character)

    # Let's join all encoded characters into a one big happy encoded message!
    return ''.join(encoded)


# As every party ends, so does the encoding. As we encoded, it's time to decode now!
def decode_affine_cipher(encoded_message, a, b):
    """Decode a message from the Affine Cipher."""
    # Keep it all UPPERCASE
    encoded_message = encoded_message.upper()

    # Compute inverse of a (modulo size of the alphabet)
    a_inv = pow(a, -1, len(LETTERS))
    
    # ....and reverse the encoding!
    decoded = []
    for character in encoded_message:
        if character in LETTERS:
            idx = LETTERS.index(character)
            decoded_char = LETTERS[(a_inv * (idx - b)) % len(LETTERS)]
            decoded.append(decoded_char)
        else:
            decoded.append(character)

    # Bring all fellow characters back together again!
    return ''.join(decoded)


# We're in the business of having fun, aren't we? How about a command line interface to play around with?
if __name__ == "__main__":
    message = input("Enter your message: ")
    print("Let's encode. We will use '5' as 'a' and '8' as 'b'")
    encoded_message = encode_affine_cipher(message, 5, 8)
    print("Your encoded message: ", encoded_message)

    print("Wonder what that means? Let's decode it now...")
    decoded_message = decode_affine_cipher(encoded_message, 5, 8)
    print("Your decoded message: ", decoded_message)

    print("Isn't Python super fun? Happy coding!")

