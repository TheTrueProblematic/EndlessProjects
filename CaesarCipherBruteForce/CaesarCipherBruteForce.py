
# Hey there! Welcome to the CaesarCipherBruteForce.py! This nifty script is your secret agent tool for
# cracking any cipher encrypted using a Caesar cipher. Get ready to feel like a real-life James Bond!
# No fancy gadgets or martinis needed. ;)

# Since this is a command-line script, it's all text-based - no fancy GUIs here.
# It's as barebones as possible - no dependencies, no internet usage, completely self-contained.
# This little guy speaks only Python and is multi-platform ready - it goes anywhere you do!

# Standard library imports only. Isn't Python great?
import string

# Here is our magical function to decode a Caesar cipher!
def decode_caesar(ciphertext, shift):
    # Sonic boom! We're using the maketrans function to create a translation table.
    # This is kind of like a decoder ring - it maps the encrypted characters to the decrypted characters.
    # The string module is super helpful here, offering up two constant strings: ascii_lowercase and ascii_uppercase.

    trans = str.maketrans(
        string.ascii_lowercase + string.ascii_uppercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift] +
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )

    # And now, the grand reveal! We return the decoded message using the translate function with our decoder ring (the trans table).
    return ciphertext.translate(trans)

# Alrighty! Here comes our brute-force method! Get ready for some code karate!
def brute_force_caesar(ciphertext):
    # Since there are only 26 possible shifts in a Caesar cipher, we just need to try them all!
    for i in range(1, 26):
        # Print out the shift and the decoded text at that shift.
        print(f'Shift {i}: {decode_caesar(ciphertext, i)}')

# Time to put our superagent tool to good use.
# Let's bravely venture forth into command line arguments handling territory.
if __name__ == '__main__':
    import sys
    ciphertext = sys.argv[1] if len(sys.argv) > 1 else ''
    print(f'Trying to decode: {ciphertext}')
    brute_force_caesar(ciphertext)
# This is the end of our adventure, but the beginning of yours with CaesarCipherBruteForce.py!
# Dive in, make a mess, and have fun decoding your secret messages. Happy Programming!

