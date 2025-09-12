
# Hey, there programmer! You've found your happy place with 'VigenereCipher'. Today we're making secret messages. Shhhh! 🔏🕵️‍♀️

# The Vigenère Cipher is an old-school method of encrypting (secretifying) and decrypting (unsecretifying) text. 
# Here we're going to implement that in good old Python!

def encode_vigenere(plain_text, key):
    """
    Function to encode the plain text using vigenere cipher technique
    """
    cipher_text = ""  # Our secret message holder.
    key_length = len(key)
    key_as_int = [ord(i) for i in key]  # Each character in key as its ASCII integer value. So high-tech, much wow.
    plain_text_int = [ord(i) for i in plain_text]  # Doing the same with our message.
    
    for i in range(len(plain_text_int)):
        value = (plain_text_int[i] + key_as_int[i % key_length]) % 26  # The actual encoding happens here.
        cipher_text += chr(value + 65)  # Changing back to characters.
    return cipher_text


def decode_vigenere(cipher_text, key):
    """
    Function to decode the cipher text using vigenere cipher technique
    """
    plain_text = ""  # This will hold our decoded message.
    key_length = len(key)
    key_as_int = [ord(i) for i in key]  # ASCII-ing the key again!
    cipher_text_int = [ord(i) for i in cipher_text]  # And the coded message.
    
    for i in range(len(cipher_text_int)):
        value = (cipher_text_int[i] - key_as_int[i % key_length]) % 26  # The decoding magic.
        plain_text += chr(value + 65)  # Back to la lettre.
    return plain_text


def main():  
    # Main function to capture user's choice for encoding or decoding
    print('\n=== Welcome to Secret Messages with the Vigenere Cipher! ===\n')
    choice = input('Choose:\n1. Encoding\n2. Decoding\n')
    if choice == '1':
        plain_text = input('\nEnter text to encode: ')
        key = input('Enter key: ')
        print('Encoded text: ', encode_vigenere(plain_text.upper(), key.upper()))
    elif choice == '2':
        cipher_text = input('\nEnter text to decode: ')
        key = input('Enter key: ')
        print('Decoded text: ', decode_vigenere(cipher_text.upper(), key.upper()))
    else:
        print('Invalid choice. Please choose between 1 (Encoding) or 2 (Decoding).')

# It takes 2 to tango, but not for VigenereCipher. Just run it!
if __name__ == "__main__":
    main()

