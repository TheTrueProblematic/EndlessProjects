
# Hey, great to see y'all! I'm your friendly Python script, SentenceSplitter! Here's what we're gonna do today...
# we're gonna take an entire paragraph, and split it up nice and dandy into the sentences it's made up of. We're gonna
# keep things nice and simple, no GUI, no internet access, and no dependencies. Ready? Leggo!

import re  # We only need the built-in re module for some hot regex action!

def split_paragraph_into_sentences(paragraph):
    """
    Hello, I'm a function that takes a string paragraph and splices it into its constituent sentences.
    """
    sentenceEnders = re.compile(r"""
        # Split sentences on whitespace between them.
        (?:               # Group for two positive lookbehinds.
          (?<=[.!?])      # Either an end of sentence punct,
        | (?<=[.!?]['"])  # or end of sentence punct and quote.
        )                 # End group of two positive lookbehinds.
        (?<!  Mr\.   )    # Don't end sentence on "Mr."
        (?<!  Mrs\.  )    # Don't end sentence on "Mrs."
        (?<!  Jr\.   )    # Don't end sentence on "Jr."
        (?<!  Dr\.   )    # Don't end sentence on "Dr."
        (?<!  Prof\. )    # Don't end sentence on "Prof."
        (?<!  Sr\.   )    # Don't end sentence on "Sr."
        \s+               # Split on whitespace between sentences.
        """, 
        re.IGNORECASE | re.VERBOSE)
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList
    

# OK, there you have it! Just call the 'split_paragraph_into_sentences' function with your paragraph as a string parameter.
# The function will return a list with the sentences. Have a good time using it! Ciao!

# One last thing though! Could you please make sure you're feeding paragraphs into my function? It gets a bit uncomfy with different data types!
# Thanks a ton, and enjoy your sentence splitting party!
