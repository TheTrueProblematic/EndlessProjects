
# Hey there, happy coder! This is the PalindromeChecker program!
# This fun little script checks if a word or sentence is a palindrome. It's palindrome party time!

def main():
    # First things first, let's get some input from the user.
    original_string = input("Enter a word or sentence: ").lower()

    # We're going to need a copy of this string, but spaces and punctuation can be tricky,
    # so we'll just work with the alphabetic characters.
    cleaned_string = ''.join(character for character in original_string if character.isalpha())

    # Creating the reverse of this cleaned string should be as easy as saying our ABCs backwards.
    # But in Python it's even easier! Just use slicing with a step of -1
    reversed_string = cleaned_string[::-1]
    
    # Now comes the moment of truth. Drum roll please...
    if cleaned_string == reversed_string:
        print("Hooray! The original string is a palindrome!")
    else:
        # This isn't a palindrome, but we can still be positive about it!
        print("Oh no! The original string is not a palindrome. But don't worry, better luck next time! :)")

# There you have it, our palindrome checker. You can call this function to start the fun
# So let's get this show on the road! This line will start the program automatically
# when you run this file from the command line.
if __name__ == '__main__':
    main()

