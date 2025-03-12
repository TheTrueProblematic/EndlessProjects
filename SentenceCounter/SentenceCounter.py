
# Welcome to the wonderful world of SentenceCounter!
# Our fantastic journey today involves discovering 
# the amazing number of sentences hidden in the mysterious land of Paragraph!

# As specified, we need to be self-sufficient and not rely on any external dependencies.
# No problem for a brave programmer like me. Let's dive right in!

# We use the core regex library to find our periods, question marks, and exclamation marks. 
# These punctuation characters help us mark the boundary of sentences.
import re 

def count_sentences(paragraph):
    """Count the number of sentences in the paragraph."""
    # HOORAY! A new adventure awaits us inside this function!
  
    # To count the sentences in a paragraph, we are using regex (avoids dependencies on NLTK and others.)
    # We are considering a sentence ending with '.', '!', '?' as a valid sentence.
  
    # Using regex we are splitting the paragraph into sentences. SOO EXCITING!
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', paragraph)
  
    # OK, now we have a list of sentences, 
    # but wait...there might be empty ones due to the split. Let's clean those up!

    sentences = [s for s in sentences if s]

    # Now we just count our sentences. 1, 2, 3, 4...THIS IS FUN!
  
    return len(sentences)  


# Testing the waters with an example paragraph 

example_paragraph = "Hi! My name is Mr.Assistant. How can I help you today?"

print(f"The mighty SentenceCounter found {count_sentences(example_paragraph)} sentences! Wooohoo!")

# Leave no stone unturned! We’ve boldly ventured into the mysterious land of Paragraph, 
# and triumphantly returned with the shimmering treasure of Sentence Count in hand! 
# Great job, explorer!

