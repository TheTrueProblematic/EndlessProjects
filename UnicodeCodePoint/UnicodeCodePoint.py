
# Hello my awesome code reader! Welcome to UnicodeCodePoint.py (hooray!)
# This little gem of a script is designed to accept a string and spit out the Unicode code points of each character.
# No graphics, no API calls, not even a cute little Python turtle to play with. Just pure, wholesome Python!

# Alright, let's roll up our sleeves and dive right in!

def unicode_code_point(my_string):
    # Taking a deep breath, and here we go!
    # We're going on a character-by-character journey through your string.
    for character in my_string:
        # We will find the Unicode code point for each of these adventurous little characters.
        code_point = ord(character)
        
        # and... print it out! Woohoo!
        print(f"The Unicode code point of {character} is: {code_point}. What a thrill!")

def main():
    # So, you've got a string in mind, right? Don't be shy, pass it in as an argument when you run this script.
    import sys

    # Let's grab it  right from the command line argument! Does this make us hackers now? Wink Wink!
    input_string = sys.argv[1]
    
    # And here we go, let the Unicode explorations commence!
    unicode_code_point(input_string)


# This 'if' makes sure the code doesn't run if this file is imported as a module. Neat, huh?
if __name__ == "__main__":
    main()

# So, that was our merry little trip through the land of Python and Unicode. Sounds fun, right?
# Next time you're having a long day, just remember: your Python script is out there, smiling and winking as it runs through strings and numbers.
# Keep coding and stay awesome! 🚀🚀🚀 

