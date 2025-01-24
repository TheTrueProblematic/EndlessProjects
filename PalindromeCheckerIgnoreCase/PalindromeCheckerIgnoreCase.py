
# PalindromeCheckerIgnoreCase.py
# Yay! Welcome to PalindromeCheckerIgnoreCase.py!
# This little script has the magical ability to tell you whether a provided string is a palindrome.

# How does it do that, you ask? Well, you'll find that our little script here is quite clever. It
# takes the string you give it and, ignoring case, punctuation, and spaces, determines if it reads 
# the same forward and backwards - the very definition of a palindrome!

# With no GUI, and zero dependencies, our script is ready to run on your command line right off the bat
# in the simplest of Python environments. Even on a brand new computer. Ain't that cool?

# Now, without further ado, let's dive into the code and see how our script tackles the palindrome conundrum with grace and elegance!

def is_palindrome(input_string):
    """A function to check if a string is palindrome or not.
    
    Args:
    input_string (str): A string provided by the user.

    Returns:
    bool: Returns True if the string is a palindrome (ignoring spaces, punctuation, and case), otherwise False.
    """
    
    # Let's start by removing spaces, punctuation and making the string all lovercase.
    stripped_string = "".join(ch for ch in input_string if ch.isalnum()).lower()
    
    # Time to check if the stripped string is a palindrome.
    # We can do that by simply checking if the string is the same as its own reverse!
    # We'll use [::-1] trick here to reverse the string.
    return stripped_string == stripped_string[::-1]

def main():
    """Main function to drive the script."""
    
    # Let's greet our user and ask them to provide a string for us to check.
    print('Hi there! Welcome to PALINDROME CHECKER! Please, give me a string to check.')
    
    input_string = input()
    
    if is_palindrome(input_string):
        print('Congrats, your string is a PALINDROME!')
    else:
        print('Oops! Your string is NOT a palindrome.')
    
if __name__ == '__main__':
    main()

# Yay! Our script is finished! I hope you had as much fun as I did while we wrote it.
# Now, just run it from the command line and check as many strings as you want. Enjoy!

