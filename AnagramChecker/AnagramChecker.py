
# Hey there! This is AnagramChecker, your pet Python script, that loves checking `anagrams` or no-sir-not-anagrams!
# It doesn't need the internet, or fancy APIs, heck, it doesn't even need a GUI. Just plain old Python, like the good ol' days.

# All it needs? Two words love! Just feed 'em, and it'll tell you if they're anagrams or just anagram-ish!

# Okay, into the coding rabbit hole we go! *whee*

def is_anagram(word1, word2):
    '''
    This function takes in two words, breaks them into alphabets, 
    and checks if they make sense in a different order. 
    Basically, words going under the knife (but don't worry, no words were harmed in the process).
    '''
    
    # Python's built-in sorted function is our hero. Splits and sorts our words into a list, alphabetically. Neat, eh?
    word1_sorted = sorted(word1.lower()) 
    word2_sorted = sorted(word2.lower()) 

    # Remember the whole going-under-the-knife spiel? We're going to stitch 'em back together now! Only a bit... twisted!
    #  We join our sorted words back into a single string
    word1_sorted = "".join(word1_sorted)
    word2_sorted = "".join(word2_sorted)

    # And the moment you've been waiting for - the face-off! Or should I say, word-off?
    # If our newly stitched words match - we got ourselves an anagram! If not... better luck next time!
    if word1_sorted == word2_sorted:
        return True
    else:
        return False

# Armed with our function, let's run a command-line based program to get user input
if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    # Let's pass our words to our anagram detective function!
    is_it_anagram = is_anagram(word1, word2)
    
    # Add a dash of suspense, and reveal the results!
    if is_it_anagram:
        print("Voila! The words are anagrams!")
    else:
        print("Oh no! The words are not anagrams!")

# Phew! The mystery has been solved. Until next time, AnagramChecker out!
