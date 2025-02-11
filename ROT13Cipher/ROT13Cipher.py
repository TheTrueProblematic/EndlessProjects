
# Hello there magnificent person! 🎩✨
# Today, we're on a mission to encode and decode text using the ROT13 cipher - a simple letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet. ROT13 is a special case of the Caesar cipher, which was developed in ancient Rome.

def rot13(text):
    '''A function to encode or decode texts according to the ROT13 cipher.'''
    result = ""
    
    # Looping through each character in the text
    for char in text:
        # For uppercase characters
        if 'A' <= char <= 'Z':
            # Get the ASCII value of the character, subtract the ASCII value of 'A' (to start from 0), add 13 (for the ROT13 rotation), 
            # modulo 26 (to wrap around the alphabet), then add the ASCII value of 'A' back to get the encoded/decoded character
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        # For lowercase characters
        elif 'a' <= char <= 'z':
            # Do the same as above, but with 'a' instead of 'A'
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        # For non-alphabetical characters
        else:
            # Keep them as they are
            result += char

    return result

def main():
    '''The main function of our script.'''
    while True:
        # Keep asking the user for texts to encode/decode until they wish to stop.
        text = input('Please enter the text you wish to encode/decode using ROT13 (or "quit" to stop): ')
        if text.lower() == 'quit':
            break
        print(f'The encoded/decoded version of your text is: {rot13(text)}')

if __name__  == '__main__':
    # And...Action! 🎬
    main()

