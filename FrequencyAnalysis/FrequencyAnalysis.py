
# Hola! This is a FUN project called FrequencyAnalysis!
# I'm sure you're as psyched about it as I am.
# IT'S GONNA BE SO COOL.
# Alright! So, this elegant and reliable frequency analysis tool analyzes the frequency of letters in a ciphertext. 

# We cannot wait to begin, can we? Let's start!

import string

def find_frequency(ciphertext):
    # Remember, the laughter we're gonna have! So let's dive into the function.
    # We'll first make sure all characters are lowercased and we're considering the alphabets only. Cos, why not?

    ciphertext = ''.join(filter(str.isalpha, ciphertext)).lower()

    # Here comes the frequency dictionary! It will store each letter's frequency.
    frequency_dict = dict.fromkeys(string.ascii_lowercase, 0)

    # Now, it won't take more than a nanosecond for the loop to churn through the characters and count the frequency.
    for char in ciphertext:
        # Bingo for every alphabet we find.
        frequency_dict[char] += 1

    return frequency_dict

if __name__ == "__main__":
    # Oh look! We're at main. Are you prepared? If yes, then buckle up!

    # We have a nice, little command-line input for the ciphertext. 
    ciphertext = input("Please enter your ciphertext (only alphabets will be considered): ")
    
    # Time to summon our find_frequency() function to perform its magic! 
    frequency_dict = find_frequency(ciphertext)
    
    # And now, we're simply going to print out the frequency of each character.
    for char, freq in sorted(frequency_dict.items()):
        print(f"The letter {char} appears {freq} times")

# Woohoo! We did it! Thank you for coding along and making this journey delightful.
# Until next time, Happy Coding! :)
