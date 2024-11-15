
# Hello Happy Programmer!
# Welcome to the WordCounter python script project
# This script helps in counting the number of words in a sentence
# What's more fun than knowing how verbose you are, eh?

# Now, let's dive into creating the Python script!

# We'll begin by defining the main function of our script named count_words 
def count_words(sentence):     
    # Python's split() function is perfect for this, it separates a sentence into a list of words! Fantastic, isn't it?
    words = sentence.split() 

    # Now we'll count the number of words in our list using the len() function
    # Who knew counting could be this easy!
    num_words = len(words) 

    # Finally, we'll return this count back to whoever asked for it, just like a well-trained pet :D   
    return num_words

if __name__ == '__main__':
    # This is where our script will start execution when run from the command line

    # Let's take a sentence as an input from the user with a fun prompt 
    sentence = input("Hey there, type a sentence and I'll count the words for you: ")

    # We'll call our main function count_words to do its magic!
    num_words = count_words(sentence)

    # And the moment of truth! We print the number of words back to the command line
    print(f'Wow, there are {num_words} words in your sentence. Cool, huh?')

# And it's a wrap, awesome human!
# Hope you enjoyed creating this WordCounter script.
# Now go ahead, run it and have fun! :)    

