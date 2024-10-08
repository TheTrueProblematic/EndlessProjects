
# Wooho! Let's create some magic and cryptography!
# This super awesome python script is called FileEncryption and,
# as you could probably guess from its fancy name, it is designed to encrypt and decrypt text files.
# Cryptography, fun, isn't it? :-)

import os
# Imports, not as fun as the decryption, are still important, 
# though we're only dealing with our little old friend os.

def encrypt(file_name, key):
    # This little magical function encrypts your file. Cool, huh?
    # It takes a filename and a key as its inputs.

    encrypted_file = ""
    # Define an empty string where our encrypted data will be stashed!

    def xor(character, key):
        # Awww, isn't XOR operation cute? It helps us to mask our characters.
        # The function takes a character and a key, and returns their XOR operation.
        return chr(ord(character) ^ key)

    with open(file_name, 'r') as f:
        # Open up that file, we've got some encrypting to do!

        text = f.read()
        # Read the whole text from your file.
    
        for c in text:
            # Let's go on a little journey through each character in your text.

            encrypted_file += xor(c, key)
            # Encrypt each character by XOR'ing it with the key and add it to our encrypted_file string.

    with open(file_name, 'w') as f:
        # And now, let's open up that file again, but this time to write in it.

        f.write(encrypted_file)
        # Write our newly encrypted text back in file and VOILA! Encryption done!

def decrypt(file_name, key):
    # Time to decrypt! That's always fun - we'll find out if our encrypting worked.
    # To turn the gibberish back into text, we'll use the same XOR operation.

    return encrypt(file_name, key)
    # Extra convenience! By reusing the encryption function with the same key,
    # we can decrypt text. I know, crazy right! But in XOR land, it works!

if __name__ == "__main__":
    # Don't be shy, jump in!

    import argparse
    # Let's add some command-line interface goodness here.

    parser = argparse.ArgumentParser(description="Let's encrypt and decrypt text files!")
    parser.add_argument('file', help='File to encrypt/decrypt')
    parser.add_argument('key', type=int, help='Encryption/decryption key must be an integer')
    parser.add_argument('-d', '--decrypt', action='store_true', help='Decrypt file')
    args = parser.parse_args()
    # We got some arguments to parse: the file to apply operation on, the key to use, 
    # and a flag to specify whether we're gonna decrypt.

    if args.decrypt:
        decrypt(args.file, args.key)
        # If the decrypt argument is passed, we decrypt the file.
        print('File has been decrypted. YAY!')
    else:
        encrypt(args.file, args.key)
        # No decrypt? Okay, we encrypt!
        print('File has been encrypted. BOOM!')

# Well, we've reached the end. Ta-Da!. Happy encrypting and decrypting folks!

