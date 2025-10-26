
# Hey there, fellow coder! Welcome to the TextEntropyCalculator!

# The script measures the Shannon entropy of a given text sample.

# It's a beautiful, wonderful and exciting measure of unpredictability, randomness and chaos in data!
# Sounds thrilling, doesn't it? Yeah, I believe so too!

# We are going to use Python's standard libraries, so no need to download anything to run the script.

# Ready for some entropy chaos? Let's dive in!

# We start by importing Python's standard library.
import math
import sys

# Let's open up the mystical world of functions.
# We start with a function to calculate the entropy of a given text.

def calculate_entropy(text):
    """
    This function takes a text as an argument and calculates its entropy.
    """

    # First, let's initialize a dictionary to store the frequency of each character
    frequency = dict()

    # Now we calculate the frequency of each character
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Compute the probabilities
    probabilities = [float(frequency[char]) / len(text) for char in frequency]
    
    # Here comes the big moment, let's calculate the entropy!
    # Entropy is the sum of probabilities times the log base 2 of probabilities.
    entropy = -sum([p * math.log(p, 2) for p in probabilities])

    # There you have it, chaos in all its glory.
    return entropy  
            
# Next, we will need a function to fetch the text from a user.
def fetch_text():
    """
    This function fetches text from a user via the command line.
    """

    # The idea is very simple, 
    # We take user input!
    # I'm sure you can't control your excitement (Neither can I!)
    text = input("Enter the text: ")

    # There you have it, the chosen one.
    # You've got the string, time to shake things up with a bit of entropy!
    return text

# Our main function is where all the magic will happen.
def main():
    """
    The main function of our script.
    """
    
    # The almighty 'text' bestowed upon us by the user.
    text = fetch_text()

    # Oh boy, oh boy, the entropy!
    entropy = calculate_entropy(text)
    
    # I can feel the excitement building!
    print('The Shannon entropy of the given text is:', entropy)
  
# And the party doesn't start until main walks in.
if __name__ == "__main__":
    main()

# You've made it through, coder!
# Pat yourself on the back, you have just coded up an entropy calculator! 
# Now, go on and calculate the entropy of your favorite quotes, song lyrics or even code snippets!
# The world of chaos, randomness and unpredictability awaits you!
