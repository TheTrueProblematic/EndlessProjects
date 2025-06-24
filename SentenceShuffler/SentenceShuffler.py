
# SentenceShuffler.py has joined the chat! 

# Hey there, I'm a simple python bot, but don't underestimate the fun we can have together.
# Essentially, I am here to randomly shuffle the sentences in a paragraph.
# Yeah, you heard it right! From now on, every paragraph can become a surprise package for your readers. 😜

# Lets take a quick peek on how we'll achieve this:
# Python indeed provides us with certain good modules ✨
# We have our mates 'random' and 're' with us. 😎

import random
import re

def shuffle_sentences(paragraph):
    '''
    This function takes the paragraph as an input and
    shuffles its sentences in a random manner.
    '''
    # We now split the paragraph into sentences using regex (a cheat code used to define search patterns 😆)
    # Here's the fun part, python's re module is doing this heavy task for us! 😌
    sentences = re.split('(?<=[.!]) +', paragraph)

    # Let's shuffle the sentences using out friend 'random'
    random.shuffle(sentences)

    # Voila! Our new paragraph with shuffled sentences is ready! 😍
    shuffled_paragraph = ' '.join(sentences)

    return shuffled_paragraph

def main():
    '''
    Starting of the beautiful story where our paragraph gets a face-lift.
    The central and most important function of our program.
    '''
    # Here we invite our paragraph at the console party! 🥳
    paragraph = input("\nHey Friend, Please enter the paragraph you want to shuffle: ")

    # Our paragraph gets dressed in the 'shuffle_sentences' function before it makes an entry at the console party! 😜
    print("\nYour shuffled paragraph is here: \n" + shuffle_sentences(paragraph))


# Time to call our main function! 🏁
if __name__ == "__main__":
    main()

# Did you enjoy the party? I bet you did! Cheers to python! 🥂
