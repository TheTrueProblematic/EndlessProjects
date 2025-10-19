
"""
Hey there, Happy Programmer!

Welcome to SpellCheckHighlighter, a fun little Python program to highlight any 
misspelled words you come across. It's a simple, command line tool, built for 
the fun of it. And yes, it works like magic!

No bells and whistles, no shiny GUIs, and definitely no complicated dependencies. 
This is pure, simple Python, working right out of the box!

And guess what, It's really light on resources too! No internet, no API, just 
you, Python, and good old computer power ;)

So, how does it work? It's simple!

You feed the program a string of text, and it checks each word against a list of 
correctly spelled words (pretty handy, huh?). 

If it comes across a word not in the dictionary aka our list, (Uh-oh, Spelling Blunder!), 
those words get highlighted.

Okay, enough talking. Let’s get to it!

"""

import re  # Regular Expressions: Our Secret Sauce for Word Detection

# Our Handy-Dandy Dictionary
# Add More Words as Needed. The more the merrier!
dictionary = set(["python", "project", "spellcheck", "highlight", "misspelled", "words"])

def spell_check_highlighter(text):
    """
    This function takes in a string, checks every word in the string against 
    the dictionary. If it can't find a match...Bam! Highlights the word.
    """
    words = re.findall(r'\b\w+\b', text)  # Extract Words. 're' to the Rescue!

    # Now the Spell Check Begins!
    for word in words:
        # Lowercasing for Consistency. (Upper case, Lower case... all the same!)
        if word.lower() not in dictionary:
            text = text.replace(word, f'[{word}]')  # Highlight Misspells with []

    # And...The Grand Result!
    return text


# Let's Test it Out!
if __name__ == "__main__":
    text = "python is the best prjct to hlght mispelled wrds"
    result = spell_check_highlighter(text)
    print(result)  # Drumrolls Please...

# And we're Done!
# That was Smooth Sailing, right? Well, Python Powers Everything!
# Keep that Smile Going, Stay Bright, and Keep Coding!

