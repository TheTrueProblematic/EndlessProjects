
# Hey there, fellow programmer! Welcome to the exciting world of cryptography! 
# Today, we're going to simulate a simple one-time pad cipher with a random key. It's like playing spies but with Python! 

# Oh, don't know what a one-time pad cipher is? It's a type of encryption where each plaintext character from a message 
# is 'mixed' with a character from a secret random key (same length as the message). This is commonly done with the XOR operation.
# When the same key is used to decrypt the ciphertext, you end up with the original plaintext. Magic!

# Let's make sure we keep all the exclusivity - No GUIs. No dependencies. No API. No internet access. Just pure Python stuff.
# Fresh Python install on a brand new PC? No problemo! We've got it covered. Now let's dive into the code!

import os
import sys

# XOR operation for a pair of characters 
def xor_characters(character1, character2):
    return chr(ord(character1) ^ ord(character2))

# Encryption and decryption using the One Time Pad
def one_time_pad(message, key):
    return ''.join(xor_characters(m, k) for m, k in zip(message, key))

# Our random key generator
def generate_key(length):
    # We'll use the os module to generate a key of specific length
    return os.urandom(length).decode('latin-1')

def main():
    # The driver code

    # We'll take the input message from command line argument
    if len(sys.argv) != 2:
        print("Error: Provide a message to encrypt as a command line argument.")
        sys.exit(1)

    message = sys.argv[1]
    print("Your message is: ", message)

    # Generate our secret key of the same length as the message
    key = generate_key(len(message))
    print("Generated secret key is: ", key)

    ciphertext = one_time_pad(message, key)
    print("Encrypted message (ciphertext) is: ", ciphertext)

    # Now let's decrypt it back with the same key
    decrypted_message = one_time_pad(ciphertext, key)
    print("Decrypted message is: ", decrypted_message)

    if message == decrypted_message:
        print("Hurray! The decrypted message matches the original!")
    else:
        print("Oops, something went wrong.")

if __name__ == "__main__":
    main()
# And there you have it! A one-time pad cipher simulator. It's quirky, fun, and easy. Happy coding!

