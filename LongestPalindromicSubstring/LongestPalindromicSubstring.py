
# Howdy, Pythonistas! Welcome to the "LongestPalindromicSubstring" Show!
# Buckle up because we're about to have some fun finding palindromes! Yee-haw!

# First thing you gotta know about this here program is that it's all about palindromes in a string!
# What is a palindrome, you ask? It's a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization! Cool huh?
# Now lets get down to business and create some magic!


def longest_palindromic_substring(string):
    """
    This lovely function takes a string and finds the longest palindromic substring in it.
    Looks like magic? Well, it kind of is! 😄 
    """
    # Let's start the journey by initializing some helpful variables.
    result = ""
    max_length = 0

    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            
            # Set the stage by getting the substring.
            substr = string[i:j]

            # Our main show: checking if the substring is a palindrome!
            if substr == substr[::-1]:  # [::-1] is a nifty Python trick for reversing a string!
                
                # Is the palindrome substring the longest one so far?
                # If so, then it's our new king of the hill!
                if len(substr) > max_length:
                    max_length = len(substr)
                    result = substr

    # Time to take a bow! We return the longest palindromic substring we found.
    return result


# Okay, now that the magic show happened, let's take this function for a spin!
if __name__ == "__main__":
    
    # Some test strings to dazzle the audience.
    test_strings = ["babad", "cbbd", "hello", "racecar"]
    
    for test in test_strings:
        print(f"The longest palindromic substring in '{test}' is '{longest_palindromic_substring(test)}'")
        
# Isn't Python grand? Thanks, and have a good one!


