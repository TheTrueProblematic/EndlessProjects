
# PalindromeCounter.py

# Hey there, Happy Programmer! Thanks for checking out my code!
# This script is a light-hearted take on counting the number of palindromes in a sentence
# Absolutely no rockets were harmed in the making of this project 🚀 😉

# Let's kick things off with defining our palindrome finder function!
def is_palindrome(word):
    # A palindrome is a word that remains the same when its letters are reversed
    # Let's compare our word with its reversed self and see if they match!
    # One other thing to consider: we should ignore case, so let's make everything lower
    return word.lower() == word[::-1].lower()

# Onto the main event! Time for the function to count our palindromes
def count_palindromes(sentence):
    # We'll use a counter to keep track of our palindromes!
    palindrome_count = 0

    # breaking down the sentence into individual words
    words = sentence.split()

    # Let's loop through each word and check if its a palindrome!
    for word in words:
        if is_palindrome(word):
            # Each time we find a palindrome, let's increment our counter by 1
            palindrome_count += 1
            
    # Once we've looped through all our words, we can return the count!
    return palindrome_count

# Time for the moment of truth! Let's test our functions!
if __name__ == "__main__":
    sentence = input("Enter a sentence to check for palindromes: ")
    print(f"\nWow! Your sentence contains {count_palindromes(sentence)} palindrome(s)! How exciting!")
    
# And that's all folks! 🐷 See you on the next programming adventure!

