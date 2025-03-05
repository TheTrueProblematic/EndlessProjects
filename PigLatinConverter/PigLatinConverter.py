# Hello Wonderful Coders!
# This is a simple yet amazing Pig Latin Converter.
# In Pig Latin, we take the first letter of each word, put it at the end, and add "ay".

# For example:
# - Hello => elloHay
# - World => orldWay

# Pretty cool, right? Let's dive into it!

def convert_to_pig_latin(sentence):
    """
    This function converts a sentence to Pig Latin.
    """
    # We need to split the sentence into words to work with them individually.
    words = sentence.split()
    
    # This will be where we store our Pig Latin words.
    pig_latin_words = []
    
    # Let's get rolling and convert each word to Pig Latin!
    for word in words:
        # We take all letters from the second one and add the first one to the end, with "ay".
        pig_latin_word = word[1:] + word[0] + "ay"
        
        # We now have a Pig Latin word. Let's add it to our list!
        pig_latin_words.append(pig_latin_word)
    
    # We join all the Pig Latin words into a sentence and return it.
    pig_latin_sentence = " ".join(pig_latin_words)
    return pig_latin_sentence

def main():
    """
    This is where our wonderful little program starts.
    """
    sentence = input("Please enter your sentence: ")
    pig_latin_sentence = convert_to_pig_latin(sentence)
    print(f"Your sentence in Pig Latin is: {pig_latin_sentence}")

# Time to run our amazing converter!
if __name__ == "__main__":
    main()

# Wasn't that fun? Pig Latin is such an interesting language!
# I hope you enjoyed this little program as much as I did.
# Happy coding!