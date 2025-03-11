
# Hey there, fellow coder! You've stumbled upon a little Morse code translator.
# Perfect for those day-to-day Morse code translations you so often need (or, you know, just playing around).
# Brace yourselves, fun code ahead!

# First up, we'll need our Morse code dictionary. It's encoded, just like our messages! Convenient, isn't it?
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
                   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
                   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
                   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
                   'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
                   '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
                   '!': '-.-.--', ' ': '/'}

# Let's flip our dictionary to reverse the key/value pairs
# We're decoding Morse code into text, so we need this!
morse_code_dict = {value: key for key, value in morse_code_dict.items()}

def morse_to_text(morse_code):
    # Here we're going to convert our Morse code string into a meaningful message
    # First, we split our input at spaces (remember, spaces separate the Morse code letters!)
    morse_code_words = morse_code.split(' ')

    # Now, we'll translate each Morse code word into a letter
    letters = [morse_code_dict[word] for word in morse_code_words if word in morse_code_dict]

    # Finally, let's join all the letters together into a lovely, meaningful message.
    # And voila! Morse code magic completed!
    return ''.join(letters)

# Now for the fun part - let's get user input!
while True:
    morse_code = input("\nHey, do you have any Morse code for me to decode? (or 'exit' to stop) ")
    # It's always good to give your users a way out of the loop - 'exit' seems fair!
    if morse_code.lower() == 'exit':
        print("\nOkay, bye-bye for now!")
        break
    else:
        # Aha! Let's see what you've got for us...
        print("\nAlrighty, looks like your decoded message reads...", morse_to_text(morse_code))

# And that, my friend, is how you become a Morse code master. Thanks for stopping by!
