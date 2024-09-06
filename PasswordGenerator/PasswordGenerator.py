
# Funtastic Password Generator: For when you just can't remember your cat's birthday anymore!

# Python is really great. It's got all this built-in stuff that makes life much easier.
# And we're starting off by importing some of these built-in modules:

# 'string' provides various string operations. This is where we'll get our letters, digits and punctuation.
# 'random' is... well, it's for randomness. For when life becomes too predictable!

import string
import random

def password_generator(length=8):
    """
    This ridiculously awesome function generates a super-secure password!
    The best part? You can specify how long you want it to be. 
    
    Parameter:
        - length (int): The length of the password (default is 8).
        
    Returns:
        A stunning password, ready to protect your secrets from evil doers!
    """

    # A list of potential characters in our password: a-z, A-Z, 0-9, and some cool looking symbols
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # The magic (and by magic, I mean 'random.choice') happens here:
    # A password is born! Random characters are selected from our list for the length specified
    
    password = ''.join(random.choice(all_characters) for i in range(length))

    # Voila! Your shiny new password is ready
    return password

# The main function, the star of the show, the head honcho
def main():
    print("Welcome to Funtastic Password Generator!")
    length = int(input("Please enter desired password length: "))
    print(f"Your new password is: {password_generator(length)}")

# When this script is run, we want to invoke the main function, so this checks if this script is the main entry point, 
# and if it does, it shines the spotlight on our leading function 

if __name__ == "__main__":
    main()
