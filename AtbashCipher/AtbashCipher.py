
# Hey there, Happy coders! This is a little python script implementing the Atbash substitution cipher.
# For those who don't know, Atbash is a simple substitution cipher for the Hebrew alphabet.
# But don't worry, we are going to use it for English ;)
# 'A' is replaced by 'Z', 'B' by 'Y', 'C' by 'X', etc.

# This script is ready to run in a fresh environment, no need of any internet connection or any API.
# It's completely self-sufficient like a hermit in the woods!
# And yes!! It's multi-platform capable.

def atbash_cipher(text):
    """ Encoding and decoding function for Atbash cipher """

    # start the magic
    cipher = ""  # our secret message will end up here.
    for char in text:  # let's take each character from the text one by one, like tasting different chocolates from a box. Yumm!
        if char.isalpha():  # Just checking if the character is an alphabet, because we only transform alphabets. Numbers are excused from our little magic here.
            if char.isupper():  # Is the character shouting (in uppercase)? Let's keep the tone after transforming.
                cipher += chr(90 - (ord(char) - 65))  # Don't be scared! We're just doing ASCII transformations. 90 and 65 are ASCII values of 'Z' and 'A' respectively.
            else:  # Or our character is chilled (in lowercase). Let's keep it chilled.
                cipher += chr(122 - (ord(char) - 97))  # Same transformation. But 'z' and 'a' have ASCII values 122 and 97.
        else:  # It's a number or special character. Let it be itself. Transformation is not for everyone ;)
            cipher += char
    return cipher  # Let's return our secret message to the world!


# This is for command line arguments 'cause that's where real coders play.
if __name__ == "__main__":
    import sys  # Importing library to use command line arguments.
    if len(sys.argv) < 2:  # Making sure you give something to transform before running the script.
        print("Please provide the text as an argument that you want to apply the Atbash cipher.")
        sys.exit(1) # Exiting the script if no text provided.
    text = sys.argv[1]  # Taking the text from the command line arguments.
    result = atbash_cipher(text)  # Giving your text to our magic function.
    print("The transformed text is: ", result)  # Celebrations! Let's see what our magic function returns.

