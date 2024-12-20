# This is Python code for a fun little project called 'WordReversal'.
# It's about as simple as it sounds - it'll reverse the order of words in a sentence. Let's go!

def reverse_words(sentence):
    """Function to reverse the order of words in a sentence.
    
    Args:
        sentence (str): Sentence whose words are to be reversed.
        
    Returns:
        str: Sentence with words in reverse order.
    """
    # Step 1: Split the sentence into words using 'split' function.
    words = sentence.split()

    # Step 2: Reverse the list of words with [::-1] syntax.
    # This is just a cool python trick that says 'start from the end and go to the beginning'.
    words.reverse()
    
    # Step 3: Join the words back together into a sentence using 'join'.
    # Space ' ' is used as a delimiter here. The amazing part is reversing and then joining back.
    reversed_sentence = ' '.join(words)
    
    # Now that we've reversed and joined our words back together,
    # let's return this new version of old sentence
    return reversed_sentence


# Let's check how our code works in the command line environment,
# We will get the input sentence from the user.
if __name__ == "__main__":
    sentence = input("Please enter a sentence you want reversed: ")
    reversed_sentence = reverse_words(sentence)
    print("Here is your sentence with the words reversed:", reversed_sentence)

# And there we have it!
# This awesome little piece of python will reverse the order of words in a sentence taken from user.
# Can't wait to see it work on some really crazy sentences!