
# Hey there, lovely Programmer!
# Welcome to RandomQuoteCLI, a fun, little python script that exists purely within the comfiest boundaries of your command line interface.
# So, you're ready to get started? Awesome! 
# But remember, we're not making any calls to the internet, using APIs, or relying on any dependencies here. It's just us and our very own installation of Python. Ready? Let's go!

import random

# We're going to need to access a local text file filled with quotes. I am using `quotes.txt` as the name. You should replace it if your filename's different.
filename = 'quotes.txt'

# Open our text file using with. You don't have to worry about closing files if you open them using with, isn't that cool?
# Also, we're opening the file in read mode. 'r' stands for read! Easy, right?
with open(filename, 'r') as f:

    # Here, we read all the lines from our lovely text file and store them in a list.
    # Later, we're going to choose a random quote from this list. Exciting!
    quotes = f.readlines()

# Now time for some magic to happen. We use Python's random.choice method to randomly choose a quote from our list.
random_quote = random.choice(quotes)

# And now, the reveal! We print the random quote.
# Brace yourself, you're about to be enlightened, or intrigued, or amused, or something!
print(random_quote)

