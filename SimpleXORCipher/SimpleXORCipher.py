
# Hey there, happy programmers! This is your shiny new SimpleXORCipher script.
# This bad boy can encrypt and decrypt text using XOR with a single-byte key. Let's get started!

# Just a quick heads-up! Even though it might be tempting to add some fancy GUI or reach out to the internet,
# remember our rule: We're keeping it simple and straightforward. CLI all the way! This way we can guarantee
# it'll work like a charm in a brand spanking new Python install on any platform. 

def simple_xor_cipher(text, key):
    """A simple XOR cipher that encrypts/decrypts text using a single-byte key.
    Args:
        text (str): The text to encrypt/decrypt.
        key (str): The single-byte key to use for encryption/decryption.
    Returns:
        The encrypted/decrypted text.
    """

    # Gotta turn the text into bytes. It's XOR time!
    text_bytes = text.encode()

    # The magic step! For each byte b in the text, XOR it with the key.
    encrypted_bytes = [b ^ ord(key) for b in text_bytes]

    # Convert the list of bytes back into a string.
    encrypted_text = "".join(chr(b) for b in encrypted_bytes)

    return encrypted_text

def main():
    # There you have it! Now you're ready to encrypt or decrypt to your heart's content.
    # This is just a simple demonstration of how you might use this function.
    print('Enter E for Encryption, D for Decryption: ')
    mode = input()
    print('Enter the text: ')
    text = input()
    print('Enter the key (Single character): ')
    key = input()

    if(mode.lower() == 'e'):
        print('Encrypted Text: ', simple_xor_cipher(text, key))
    elif(mode.lower() == 'd'):
        print('Decrypted Text: ', simple_xor_cipher(text, key))
    else:
        print('Invalid Input')

# Don't forget to call the function!
if __name__ == "__main__":
    main()

# You're all set! Enjoy your new XOR cipher.
# Remember, with great power comes great responsibility. 
# Don't use it for evil! (We're looking at you, Bob...) 

