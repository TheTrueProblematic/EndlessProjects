
'''
Hello lovely people! 
Guess what we're doing today? Yes, you got it right! 
We're creating an awesome tool called ParagraphSummarizer! 
It's purpose? To extract the most important sentences from a chunk of text. 
Isn't that cool? And the best part? 
We don't need any dependencies or internet connection at all! Purely python magic!
Let's get started, shall we?
'''

import re
import heapq

# Define a function to preprocess the text
def preprocess_text(text):
    '''
    This function preprocesses the text by converting all to the same case, 
    removing unwanted characters and splitting into sentences
    '''
    # Convert text to lower case to avoid case-sensitivity related confusions
    text = text.lower()
    
    # Replace everything except alphabets with space
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    # Split text into sentences
    sentences = text.split(".")
    
    return sentences

# Define our main summarizer function
def summarize_paragraph(text, summary_length=3):
    '''
    This function receives a paragraph of text and returns summary_length number of important sentences
    The default value for summary_length is 3
    '''

    # Preprocess our text
    sentences = preprocess_text(text)

    # Calculate frequency of each word  
    word_frequencies = {}
    for sentence in sentences:
        for word in sentence.split(" "):
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    
    # Get maximum frequency
    max_frequency = max(word_frequencies.values())

    # Normalize frequencies
    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    # Calculate sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split(" "):
            if word in word_frequencies.keys():
                if sentence not in sentence_scores.keys():
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
                    
    # Get the summary
    summary_sentences = heapq.nlargest(summary_length, sentence_scores, key=sentence_scores.get)
    summary = '. '.join(summary_sentences)
    
    return summary

# That's it, our ParagraphSummarizer is good to go! 
# Give it a try, feed it with some chunk of text and grab a coffee while it does the job for you.

'''
This is the end of our journey my friends. 
I hope you had fun and learned something along the way. 
Remember that programming is all about solving problems and having fun!
Until next time!
'''
