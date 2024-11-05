
# Hello there! Welcome to the SentenceCapitalizer file! Here we're going to play with a string and capitalize the first letter of every sentence!

def capitalize_sentences(text):
    # First we'll split the text into sentences using python's built-in split method.
    sentences = text.split('. ')
    # It's ok if we have an empty entry at the end due to splitting, we'll remove it in the next step.

    # Let's loop through the sentences and capitalize the first letter of each!
    for i in range(len(sentences)):
        # We're using Python's built-in capitalize method to do the heavy lifting here
        sentences[i] = sentences[i].capitalize()

    # Now let's rejoin our sentences into a whole piece of text.
    result = '. '.join(sentences)
    # Ta-da! We're done! Just going to return the result here.
    return result

# Now we're going to test our handy little function here!
# Remember to input your text here
text = "" # e.g. "hello world. how are you?" to "Hello world. How are you?"

# Let's call our function on our sample text and print out the result
print(capitalize_sentences(text))

# Wasn't that fun? Python makes text processing super easy and enjoyable! Keep coding and having fun!

